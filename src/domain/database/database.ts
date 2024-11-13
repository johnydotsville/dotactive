
export class Database {
  config: any;
  database: any;

  // TODO: потом более продвинутую структуру можно сделать, чтобы таблицы во вложенном объекте были
  constructor(config) {
    this.config = config;
  }

  init() {
    return new Promise((resolve, reject) => {
      const openRequest = indexedDB.open(this.config.dbname, this.config.version);

      openRequest.onupgradeneeded = () => {
        const database = openRequest.result;
        this.createStorages(database, this.config.storages);
      }

      openRequest.onsuccess = () => {
        this.database = openRequest.result;
        resolve(true);
      }
    })
  }

  private createStorages(database, storages) {
    storages.forEach(s => {
      if (!database.objectStoreNames.contains(s.name)) {
        const storage = database.createObjectStore(s.name, s.settings);
        s.indexes.forEach(x => storage.createIndex(x.name, x.keyPath, x.options));
      }
    });
  }

  // TODO: Что если попробовать сохранить, а такой ключ уже есть?
  save(storage: string, data, key = null) {
    return new Promise((resolve, reject) => {
      const tx = this.database.transaction(storage, "readwrite");
      const st = tx.objectStore(storage);
      let addRequest;
      if (key) {
        addRequest = st.add(data, key);
      } else {
        addRequest = st.add(data);
      }
      
      addRequest.onsuccess = () => {
        resolve(data);
      }
    })
  }

  // TODO: Подумать, стоит ли объединить метод сохранения одного и многих значений в один
  // и если да, то как лучше и нагляднее это сделать.
  // https://stackoverflow.com/questions/54176735/correct-way-to-add-multiple-objects-in-indexeddb
  saveMany(storage, data) {
    return new Promise((resolve, reject) => {
      const tx = this.database.transaction(storage, "readwrite");
      const st = tx.objectStore(storage);

      data.forEach(d => st.add(d));

      tx.oncomplete = () => {
        resolve(data);
      }
    })
  }

  delete(storage: string, key) {
    return new Promise((resolve, reject) => {
      const tx = this.database.transaction(storage, "readwrite");
      const st = tx.objectStore(storage);
      const deleteRequest = st.delete(key);

      deleteRequest.onsuccess = () => {
        resolve(true);
      };
    });
  }

  // TODO: сделать для чтения единственного значения и всех значений разные методы или пусть будет в одном?
  // TODO: если не нашел данные, вернуть null?
  read(storage: string, key) {
    return new Promise((resolve, reject) => {
      const tx = this.database.transaction(storage);
      const st = tx.objectStore(storage);
      const itemRequest = key ? st.get(key) : st.getAll();

      // TODO: а если такого ключа нет в БД? UPD. Тогда в .result лежит undefined
      // Если getAll(), а данных нет, тоже будет undefined.
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
