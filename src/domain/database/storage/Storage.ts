import { StorageName } from "../config/storages/StorageName";
import { IStorage } from "./IStorage";
import { DbOperationResult } from "@domain/database/DbOperationResult";


export abstract class Storage<T, K> implements IStorage<T, K> {
  protected database: IDBDatabase;
  protected storageName: string;


  public constructor(database: IDBDatabase, storageName: StorageName) {
    this.database = database;
    this.storageName = storageName;
  }


  public save(data: T | T[]): Promise<DbOperationResult<T>> {
    return new Promise((resolve, reject) => {
      const [storage, tx] = this.getStorageRW();
      const saveReport = new DbOperationResult<T>();

      if (Array.isArray(data)) {
        if (data.length === 0) {
          const error = new Error("Не переданы данные для сохранения.");
          saveReport.addError(error)
          return Promise.reject(saveReport);
        }
        data.forEach(x => this.trySave(storage, x, saveReport));
      } else {
        this.trySave(storage, data, saveReport);
      }

      tx.onerror = (event) => event.preventDefault();
      tx.oncomplete = () => resolve(saveReport);
    })
  }


  private trySave(storage:IDBObjectStore, data: T, report: DbOperationResult<T>): void {
    try {
      const saveRequest: IDBRequest = storage.put(data);
      saveRequest.onsuccess = () => {
        // TODO: Мб стоит сделать какой-то общий класс "Сохраняемый объект", а в нем опциональное поле id
        // и объктам, у которых по природе нет id, добавлять id полученный от БД при автоинкременте
        // if (!data.hasOwnProperty("id")) {
        //   data.id = saveRequest.result;
        // }
        report.addResult(data);
      }
  
      saveRequest.onerror = () => {
        report.addError(saveRequest.error);
      }
    } catch (error) {
      report.addError(error);
    }
  }


  /**
   * Считывает из хранилища записи с переданными ключами. Если метод вызывается
   * без указания ключей, то считываются все записи.
   * @param key
   * @returns 
   */
  public read(key?: K | K[]): Promise<DbOperationResult<T>> {
    return new Promise((resolve, reject) => {
      const [storage, tx] = this.getStorageRO();
      const readReport = new DbOperationResult<T>();
      
      if (Array.isArray(key)) {
        if (key.length === 0) {
          const error = new Error("Не переданы ключи.");
          readReport.addError(error);
          return Promise.reject(readReport);
        }
        key.forEach(k => this.tryRead(storage, k, readReport));
      } else if (key) {
        this.tryRead(storage, key, readReport);
      } else {
        const readRequest = storage.getAll();
        readRequest.onsuccess = () => {
          readRequest.result.forEach(d => {
            readReport.addResult(d);
          });
        }
        readRequest.onerror = () => {
          readReport.addError(readRequest.error);
        }
      }

      tx.onerror = (event) => event.preventDefault();
      tx.oncomplete = () => resolve(readReport);
    });
  }


  private tryRead(storage:IDBObjectStore, key: K, report: DbOperationResult<T>): void {
    const singleKey = IDBKeyRange.only(key);
    try {
      const readRequest: IDBRequest = storage.get(singleKey);
      
      readRequest.onsuccess = () => {
        if (readRequest.result) {
          report.addResult(readRequest.result);
        } else {
          const error = new Error(`Матч ${key} не найден`);
          report.addError(error);
        }
      }

      readRequest.onerror = () => {
        report.addError(readRequest.error);
      }
    } catch (error) {
      report.addError(error);
    }
  }


  /**
   * Удаляет из хранилища записи с указанными ключами. Если метод вызывается без
   * указания ключей, тогда хранилище полностью очищается.
   * @param key
   * @returns 
   */
  public delete(key?: K | K[]): Promise<DbOperationResult<T>> {
    return new Promise(resolve => {
      const [storage, tx] = this.getStorageRW();
      const deleteReport = new DbOperationResult<T>;
      
      if (Array.isArray(key)) {
        if (key.length === 0) {
          const error = new Error("Не переданы ключи.");
          deleteReport.addError(error);
          return Promise.reject(deleteReport);
        }
        key.forEach(k => this.tryDelete(storage, k, deleteReport));
      } else if (key) {
        this.tryDelete(storage, key, deleteReport);
      } else {
        const deleteRequest = storage.clear();
        
        deleteRequest.onerror = () => {
          deleteReport.addError(deleteRequest.error);
        }
      }

      tx.onerror = (event) => event.preventDefault();
      tx.oncomplete = () => resolve(deleteReport);
    });
  }


  private tryDelete(storage:IDBObjectStore, key: K, report: DbOperationResult<T>): void {
    const singleKey = IDBKeyRange.only(key);
    try {
      const deleteRequest: IDBRequest = storage.delete(singleKey);

      deleteRequest.onerror = () => {
        report.addError(deleteRequest.error);
      }
    } catch (error) {
      report.addError(error);
    }
  }

  
  private getStorage(mode: IDBTransactionMode): [IDBObjectStore, IDBTransaction] {
    const tx: IDBTransaction = this.database.transaction(this.storageName, mode);
    return [tx.objectStore(this.storageName), tx];
  }


  protected getStorageRO(): [IDBObjectStore, IDBTransaction] {
    return this.getStorage("readonly");
  }

  
  protected getStorageRW(): [IDBObjectStore, IDBTransaction] {
    return this.getStorage("readwrite");
  }
}




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
