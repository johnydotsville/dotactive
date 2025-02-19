import { IStorage } from "./IStorage";
import { DbOperationResult } from "../DbOperationResult";

export class Storage<T, K> implements IStorage<T, K> {
  protected database: IDBDatabase;
  protected storageName: string;


  public constructor(database: IDBDatabase, storageName: string) {
    this.database = database;
    this.storageName = storageName;
  }


  public save(...data: T[]): Promise<DbOperationResult<T>[]> {
    return new Promise((resolve, reject) => {
      const saveReport: DbOperationResult<T>[] = [];

      if (data.length === 0) {
        saveReport.push({
          succeeded: false,
          error: new Error("В метод сохранения не переданы никакие данные.")
        });
        reject(saveReport);
      }
      const [storage, tx] = this.getStorageRW();
      data.forEach(x => this.trySave(storage, x, saveReport));

      tx.onerror = (event) => event.preventDefault();
      tx.oncomplete = () => resolve(saveReport);
    })
  }


  private trySave(storage:IDBObjectStore, data: T, result: DbOperationResult<T>[]): void {
    const saveRequest: IDBRequest = storage.put(data);

    saveRequest.onsuccess = () => {
      result.push(DbOperationResult.success<T>(data));
    }

    saveRequest.onerror = () => {
      result.push(DbOperationResult.fail<T>(saveRequest.error, data))
    }
  }


  /**
   * Считывает из хранилища записи с переданными ключами. Если метод вызывается
   * без указания ключей, то считываются все записи.
   * @param keys
   * @returns 
   */
  public read(...keys: K[]): Promise<DbOperationResult<T | K>[]> {
    return new Promise((resolve, reject) => {
      const [storage, tx] = this.getStorageRO();
      const readReport: DbOperationResult<T | K>[] = [];
      
      if (keys.length > 0) {
        keys.forEach(k => this.tryRead(storage, k, readReport));
      } else {
        const readRequest = storage.getAll();
        readRequest.onsuccess = () => {
          readRequest.result.forEach(d => {
            readReport.push(DbOperationResult.success<T>(d));
          });
        }
        readRequest.onerror = () => {
          readReport.push(DbOperationResult.fail<T>(readRequest.error));
        }
      }

      tx.onerror = (event) => event.preventDefault();
      tx.oncomplete = () => resolve(readReport);
    });
  }


  private tryRead(storage:IDBObjectStore, key: K, report: DbOperationResult<T | K>[]): void {
    const singleKey = IDBKeyRange.only(key);
    const readRequest: IDBRequest = storage.get(singleKey);
    
    readRequest.onsuccess = () => {
      if (readRequest.result) {
        report.push(DbOperationResult.success<T>(readRequest.result))
      } else {
        report.push(DbOperationResult.fail<K>(new Error("Матч не найден"), key));
      }
    }

    readRequest.onerror = () => {
      report.push(DbOperationResult.fail<K>(readRequest.error, key));
    }
  }


  /**
   * Удаляет из хранилища записи с указанными ключами. Если метод вызывается без
   * указания ключей, тогда хранилище полностью очищается.
   * @param keys
   * @returns 
   */
  public delete(...keys: K[]): Promise<DbOperationResult<K>[]> {
    return new Promise(resolve => {
      const [storage, tx] = this.getStorageRW();
      const deleteReport: DbOperationResult<K>[] = [];
      
      if (keys.length > 0) {
        keys.forEach(k => this.tryDelete(storage, k, deleteReport));
      } else {
        const deleteRequest = storage.clear();
        deleteRequest.onsuccess = () => {
          deleteReport.push(DbOperationResult.success<K>());
        }
        deleteRequest.onerror = () => {
          deleteReport.push(DbOperationResult.fail<K>(deleteRequest.error));
        }
      }

      tx.onerror = (event) => event.preventDefault();
      tx.oncomplete = () => resolve(deleteReport);
    });
  }


  private tryDelete(storage:IDBObjectStore, key: K, report: DbOperationResult<K>[]): void {
    const singleKey = IDBKeyRange.only(key);
    const deleteRequest: IDBRequest = storage.delete(singleKey);

    deleteRequest.onsuccess = () => {
      report.push(DbOperationResult.success<K>(key));
    }

    deleteRequest.onerror = () => {
      report.push(DbOperationResult.fail<K>(deleteRequest.error, key));
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
