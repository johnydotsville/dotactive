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
      result.push({
        succeeded: true, 
        data 
      });
    }

    saveRequest.onerror = () => {
      result.push({ 
        succeeded: false, 
        error: saveRequest.error, 
        data 
      });
    }
  }


  public read(...keys: K[]): Promise<DbOperationResult<T | K>[]> {
    return new Promise((resolve, reject) => {
      const [storage, tx] = this.getStorageRO();
      const readReport: DbOperationResult<T | K>[] = [];
      
      if (keys.length > 0) {
        keys.forEach(k => this.tryRead(storage, k, readReport));
      } else {
        const readRequest = storage.getAll();
        readRequest.onsuccess = () => {
          readRequest.result.forEach(r => {
            readReport.push({ succeeded: true, data: r });
          });
        }
        readRequest.onerror = () => {
          readReport.push({ succeeded: false, error: readRequest.error });
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
        report.push({ 
          succeeded: true, 
          data: readRequest.result 
        });
      } else {
        report.push({ 
          succeeded: false, 
          error: new Error("Матч не найден"), 
          data: key 
        });
      }
    }

    readRequest.onerror = () => {
      report.push({ 
        succeeded: false, 
        error: readRequest.error, 
        data: key 
      });
    }
  }


  public delete(...keys: K[]): Promise<DbOperationResult<K>[]> {
    return new Promise(resolve => {
      const [storage, tx] = this.getStorageRW();
      const deleteReport: DbOperationResult<K>[] = [];
      
      if (keys.length > 0) {
        keys.forEach(k => this.tryDelete(storage, k, deleteReport));
      } else {
        const deleteRequest = storage.clear();
        deleteRequest.onsuccess = () => {
          deleteReport.push({ 
            succeeded: true 
          });
        }
        deleteRequest.onerror = () => {
          deleteReport.push({ 
            succeeded: false, 
            error: deleteRequest.error 
          });
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
      report.push({ 
        succeeded: true, 
        data: key 
      });
    }

    deleteRequest.onerror = () => {
      report.push({ 
        succeeded: false, 
        error: deleteRequest.error, 
        data: key 
      });
    }
  }

  
  private getStorage(mode: string): [IDBObjectStore, IDBTransaction] {
    const tx: IDBTransaction = this.database.transaction(this.storageName, "readwrite");
    return [tx.objectStore(this.storageName), tx];
  }


  protected getStorageRO(): [IDBObjectStore, IDBTransaction] {
    return this.getStorage("readonly");
  }

  
  protected getStorageRW(): [IDBObjectStore, IDBTransaction] {
    return this.getStorage("readwrite");
  }
}