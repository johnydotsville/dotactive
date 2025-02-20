import { IDbConfig } from "./config/IDbConfig";
import { IStorageConfig } from "./config/IDbConfig";
import { IStorageIndex } from "./config/IDbConfig";


export class MyDatabase {
  private config: IDbConfig;
  private connection: IDBDatabase;


  constructor(config: IDbConfig) {
    this.config = config;
  }


  public init(): Promise<IDBDatabase> {
    return new Promise((resolve, reject) => {
      if (this.connection) {
        console.log("База данных уже открыта.");
        resolve(this.connection);
        return;
      };
      console.log("База данных не обнаружена. Создаю базу данных...");
      const openRequest: IDBOpenDBRequest = indexedDB.open(this.config.name, this.config.version);

      openRequest.onupgradeneeded = () => {
        const database: IDBDatabase = openRequest.result;
        this.createStorages(database, this.config.storages);
        console.log("База данных создана.");
      };

      openRequest.onsuccess = () => {
        this.connection = openRequest.result;
        console.log("Соединение открыто.");
        resolve(this.connection);
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
}
