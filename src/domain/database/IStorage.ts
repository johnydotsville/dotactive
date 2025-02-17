import { Match } from "@domain/services/matches/model/match";
import { DbOperationResult } from "./db-operation-result";

export interface IStorage<T, K> {
  save(data: T): Promise<DbOperationResult<T>[]>;
  // delete(key: K): Promise<boolean | Error>;
  // read(key: K): Promise<T>;
}

export class Storage<T, K> implements IStorage<T, K> {
  protected database: IDBDatabase;
  protected storageName: string;

  public constructor(database: IDBDatabase, storageName: string) {
    this.database = database;
    this.storageName = storageName;
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

  save(data: T): Promise<DbOperationResult<T>[]> {
    return new Promise(resolve => {
      const [storage, tx] = this.getStorageRW();
      const saveReport: DbOperationResult<T>[] = [];

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

  private trySave(storage:IDBObjectStore, data: any, result: DbOperationResult<any>[]) {
    const saveRequest: IDBRequest = storage.add(data);
    saveRequest.onsuccess = () => {
      result.push({ succeeded: true, error: null, data });
    }
    saveRequest.onerror = () => {
      result.push({ succeeded: false, error: saveRequest.error, data });
    }
  }

  // delete(storageName: string, key) {
  //   return new Promise((resolve, reject) => {
  //     const tx = this.database.transaction(storageName, "readwrite");
  //     const storage = tx.objectStore(storageName);
  //     const deleteRequest = storage.delete(key);

  //     deleteRequest.onsuccess = () => {
  //       resolve(true);
  //     };
  //     deleteRequest.onerror = () => {
  //       reject(deleteRequest.error);
  //     }
  //   });
  // }

  // read(storage: string, key) {
  //   return new Promise((resolve, reject) => {
  //     const tx = this.database.transaction(storage);
  //     const st = tx.objectStore(storage);
  //     const itemRequest = key ? st.get(key) : st.getAll();

  //     itemRequest.onsuccess = () => {
  //       resolve(itemRequest.result);
  //     }
  //   });
  // }
}