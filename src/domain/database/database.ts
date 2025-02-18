/*
  Актуальные вопросы:
  * Сохранение.
    * Сохранение одной записи и многих записей сделать разными методами или объединить в одном?
    * Как реализовать сохранение многих записей -
      * Сохранять каждую отдельно в своей транзакции?
      * Или сохранить все разом в одной транзакции?
    * В случае сохранения многих записей, если происходит ошибка, то
      * Откатывать все записи?
      * Или сохраненные успешно оставить, а провальные вернуть каким-нибудь списком?
  * Типизация:
    * Мб в местах сохранения и т.д. сделать дженерики? А потом создать типы под работу
      с конкретными хранилищами?
*/

import { IDbConfig } from "./config/IDbConfig";
import { IStorageConfig } from "./config/IDbConfig";
import { IStorageIndex } from "./config/IDbConfig";
import { DbOperationResult } from "./DbOperationResult";


export class Database {
  private config: IDbConfig;
  public database: IDBDatabase;

  constructor(config: IDbConfig) {
    this.config = config;
  }

  init(): Promise<boolean | Error> {
    return new Promise((resolve, reject) => {
      if (this.database) {
        console.log("База данных уже открыта.");
        resolve(true);
        return;
      };
      console.log("База данных не обнаружена. Создаю базу данных...");
      const openRequest: IDBOpenDBRequest = indexedDB.open(this.config.name, this.config.version);

      openRequest.onupgradeneeded = () => {
        const database: IDBDatabase = openRequest.result;
        this.createStorages(database, this.config.storages);
      };

      openRequest.onsuccess = () => {
        this.database = openRequest.result;
        resolve(true);
      };

      openRequest.onerror = () => {
        reject(openRequest.error);
      };
    })
  }

  private createStorages(database: IDBDatabase, storages: IStorageConfig[]) {
    storages.forEach(s => {
      if (!database.objectStoreNames.contains(s.name)) {
        const storage: IDBObjectStore = database.createObjectStore(s.name, s?.options);
        if (s.indexes) {
          this.createIndexes(storage, s.indexes);
        }
      }
    });
  }

  private createIndexes(storage: IDBObjectStore, indexes: IStorageIndex[]) {
    indexes.forEach(x => storage.createIndex(x.name, x.keyPath, x?.options));
  }
  
  /**
   * Метод сохраняет данные в указанное хранилище. Всегда возвращает успешный промис
   * с массивом отчетов о сохранении. Может сохранять как одиночный объект, так и массив объектов.
   * Все объекты сохраняются в пределах одной транзакции.
   * @param storageName 
   * @param data 
   * @returns 
   */
  save(storageName: string, data: any) {
    return new Promise(resolve => {
      const tx: IDBTransaction = this.database.transaction(storageName, "readwrite");
      const storage: IDBObjectStore = tx.objectStore(storageName);
      const saveReport: DbOperationResult<any>[] = [];

      if (Array.isArray(data)) {
        data.forEach(x => this.trySave(storage, x, saveReport));
      } else {
        this.trySave(storage, data, saveReport);
      }

      tx.onerror = (event) => {
        event.preventDefault();
      }
      tx.oncomplete = (event) => {
        resolve(saveReport);
      }
    })
  }

  /**
   * Метод пытается сохранить данные в указанное хранилище. Результат сохранения,
   * будь то успешный или не успешный, добавляет в массив отчета о сохранении.
   * @param storage Объект хранилища, в которое осуществляется сохранение.
   * @param data Данные, которые пытаемся сохранить.
   * @param result Массив под отчеты о результате сохранения.
   */
  private trySave(storage:IDBObjectStore, data: any, result: DbOperationResult<any>[]) {
    const saveRequest: IDBRequest = storage.add(data);
    saveRequest.onsuccess = () => {
      result.push({ succeeded: true, error: null, data });
    }
    saveRequest.onerror = () => {
      result.push({ succeeded: false, error: saveRequest.error, data });
    }
  }

  // // TODO: Подумать, стоит ли объединить метод сохранения одного и многих значений в один
  // // и если да, то как лучше и нагляднее это сделать.
  // // https://stackoverflow.com/questions/54176735/correct-way-to-add-multiple-objects-in-indexeddb
  // saveMany(storage, data) {
  //   return new Promise((resolve, reject) => {
  //     const tx = this.database.transaction(storage, "readwrite");
  //     const st = tx.objectStore(storage);

  //     data.forEach(d => st.add(d));

  //     tx.oncomplete = () => {
  //       resolve(data);
  //     }
  //     tx.onabort = () => {
  //       reject("Сохранение провалилось.");
  //     }
  //   })
  // }

  delete(storageName: string, key) {
    return new Promise((resolve, reject) => {
      const tx = this.database.transaction(storageName, "readwrite");
      const storage = tx.objectStore(storageName);
      const deleteRequest = storage.delete(key);

      deleteRequest.onsuccess = () => {
        resolve(true);
      };
      deleteRequest.onerror = () => {
        reject(deleteRequest.error);
      }
    });
  }

  read(storage: string, key) {
    return new Promise((resolve, reject) => {
      const tx = this.database.transaction(storage);
      const st = tx.objectStore(storage);
      const itemRequest = key ? st.get(key) : st.getAll();

      itemRequest.onsuccess = () => {
        resolve(itemRequest.result);
      }
    });
  }


  // // Считывает из указанного хранилища все записи
  // // TODO как сделать так, чтобы не пришлось явно указывать имя хранилища, из которого читать?
  // // Вероятно, сделать обертку над голой БД и сделать говорящие методы.
  // // Но пока пусть будет так.
  // read(storeName, key) {
  //   return new Promise((resolve, reject) => {
  //     const request = indexedDB.open(this.dbname);
      
  //     request.onsuccess = () => {
  //       try {
  //         const db = request.result;
  //         const tx = db.transaction(storeName, 'readonly');
  //         const store = tx.objectStore(storeName);
  //         const res = key ? store.get(key) : store.getAll();
  //         res.onsuccess = () => {
  //           resolve(res.result);  // TODO: В result всегда массив?
  //         }
  //       } catch (err) {
  //         reject(err);
  //       }
  //     };

  //     request.onerror = () => {
  //       const error = request.error?.message
  //       if (error) {
  //         reject(error);
  //       } else {
  //         reject('Unknown error');
  //       }
  //     };
  //   });
  // }


  // // Возвращает последнюю сохраненную запись из указанного хранилища
  // // TODO: чтобы это работало, наверное должен быть индекс в хранилище? UPD. Индекс тут не при чем.
  // // И вообще этот метод актуален только для хранилищ, где хранятся объекты одинаковой структуры.
  // readLast(storeName) {
  //   return new Promise((resolve, reject) => {
  //     const ropen = indexedDB.open(this.dbname);
      
  //     ropen.onsuccess = (e: any) => {
  //       try {
  //         const db = e.target.result;
  //         const tx = db.transaction(storeName, 'readonly');
  //         const store = tx.objectStore(storeName);
  //         const rcursor = store.openCursor(null, "prev");
          
  //         rcursor.onsuccess = (e) => {
  //           const cursor = e.target.result;
  //           if (cursor) {
  //             resolve(cursor.value);
  //           } else {
  //             resolve(null);
  //           }
  //         }
  //       } catch (err) {
  //         reject(err);
  //       }
  //     };
  //   });
  // }


  // // Считывает из указанного хранилища пачку записей
  // // TODO: Возможно, есть смысл считывать вообще все записи в память и страничить уже из памяти.
  // readPage(storeName, pageNum, pageSize) {
  //   return new Promise((resolve, reject) => {
  //     const ropen = indexedDB.open(this.dbname);
      
  //     ropen.onsuccess = (e: any) => {
  //       try {
  //         const matches = [];
  //         let skip = true;
  //         const skipSize = (pageNum - 1) * pageSize;
          
  //         const db = e.target.result;
  //         const tx = db.transaction(storeName, 'readonly');
  //         const store = tx.objectStore(storeName);
  //         const rcursor = store.openCursor(null, "prev");
          
  //         rcursor.onsuccess = (e) => {
  //           // Это получается "шаг цикла", обход курсора
  //           const cursor = e.target.result;
            
  //           if (skip && skipSize > 0) {
  //             skip = false;
  //             cursor.advance(skipSize);
  //             return;  // Это прервать текущий шаг и перейти на некст запись курсора
  //           }

  //           if (cursor) {
  //             matches.push(cursor.value);
  //             if (matches.length < pageSize) {
  //               cursor.continue();  // Похоже, приводит к возникновению onsuccess
  //             } else {
  //               resolve(matches);
  //             }
  //           }
  //         }
  //       } catch (err) {
  //         reject(err);
  //       }
  //     };
  //   });
  // }

  // saveWithKey(storeName, data, key) {
  //   return new Promise((resolve, reject) => {
  //     const request = indexedDB.open(this.dbname);

  //     request.onsuccess = () => {
  //       try {
  //         const db = request.result;
  //         const tx = db.transaction(storeName, 'readwrite');
  //         const store = tx.objectStore(storeName);
  //         store.add(data);  // TODO: Почему, когда тут возникает ошибка, она не ловится, а крашит? UPD. Потому, что ошибка происходит не синхронно, как бы "вне" промиса
  //         resolve(data);
  //       } catch (err) {
  //         reject(err);
  //       }
  //     };

  //     request.onerror = () => {
  //       const error = request.error?.message
  //       if (error) {
  //         reject(error);
  //       } else {
  //         reject('Unknown error');
  //       }
  //     };
  //   })
  // }

  // save(storeName, data) {
  //   return new Promise((resolve, reject) => {
  //     const request = indexedDB.open(this.dbname);

  //     request.onsuccess = () => {
  //       try {
  //         const db = request.result;
  //         const tx = db.transaction(storeName, 'readwrite');
  //         const store = tx.objectStore(storeName);
  //         store.add(data);  // TODO: Почему, когда тут возникает ошибка, она не ловится, а крашит? UPD. Потому, что ошибка происходит не синхронно, как бы "вне" промиса
  //         resolve(data);
  //       } catch (err) {
  //         reject(err);
  //       }
  //     };

  //     request.onerror = () => {
  //       const error = request.error?.message
  //       if (error) {
  //         reject(error);
  //       } else {
  //         reject('Unknown error');
  //       }
  //     };
  //   })
  // }


  // saveMany(storeName, data) {
  //   return new Promise((resolve, reject) => {
  //     const request = indexedDB.open(this.dbname);

  //     request.onsuccess = () => {
  //       try {
  //         const db = request.result;
  //         const tx = db.transaction(storeName, 'readwrite');
  //         const store = tx.objectStore(storeName);
  //         data.forEach(d => store.add(d));
  //         resolve(data);
  //       } catch (err) {
  //         reject(err);
  //       }
  //     };

  //     request.onerror = () => {
  //       const error = request.error?.message
  //       if (error) {
  //         reject(error);
  //       } else {
  //         reject('Unknown error');
  //       }
  //     };
  //   })
  // }


  // clear(storeName) {
  //   return new Promise((resolve, reject) => {
  //     const request = indexedDB.open(this.dbname);

  //     request.onsuccess = () => {
  //       try {
  //         const db = request.result;
  //         console.log('Попытка очистить хранилище...');
  //         const tx = db.transaction(storeName, 'readwrite');
  //         const store = tx.objectStore(storeName);
  //         const osr = store.clear();

  //         osr.onsuccess = () => {
  //           console.log('Хранилище очищено успешно.');
  //           resolve(true);
  //         }
          
  //         osr.onerror = () => {
  //           console.log('Не удалось очистить хранилище: ' + osr.error?.message);
  //           resolve(false);
  //         }
  //       } catch (err) {
  //         reject(err);
  //       }
  //     };

  //     request.onerror = () => {
  //       const error = request.error?.message
  //       if (error) {
  //         reject(error);
  //       } else {
  //         reject('Unknown error');
  //       }
  //     };
  //   })
  // }

}
