import { IDbConfig } from "./config/IDbConfig";
import { IStorageConfig } from "./config/IDbConfig";
import { IStorageIndex } from "./config/IDbConfig";
import { defaultDbConfig } from "./config/defaultDbConfig";


export class MyDatabase {
  private config: IDbConfig;
  private connection: IDBDatabase;
  private static instance: MyDatabase;

  
  private constructor(config: IDbConfig) {
    this.config = config;
  }


  public static getInstance(): MyDatabase {
    if (!this.instance) {
      this.instance = new MyDatabase(defaultDbConfig);
    }
    return this.instance;
  }


  public init(): Promise<IDBDatabase> {
    if (this.connection) {
      throw new Error("Нельзя повторно инициализировать БД, она уже инициализирована.");
    };
    return new Promise((resolve, reject) => {
      console.log("База данных не обнаружена. Создаю базу данных...");
      const openRequest: IDBOpenDBRequest = indexedDB.open(this.config.name, this.config.version);

      openRequest.onupgradeneeded = () => {
        const database: IDBDatabase = openRequest.result;
        this.createStorages(database, this.config.storages);
      };

      openRequest.onsuccess = () => {
        this.connection = openRequest.result;
        resolve(this.connection);
      };

      openRequest.onerror = () => {
        reject(openRequest.error);
      };
    })
  }


  public getConnection(): IDBDatabase {
    if (!this.connection) {
      throw new Error("БД не инициализирована.");
    }
    return this.connection;
  }


  // public getConnection(): Promise<IDBDatabase> {
  //   return new Promise((resolve, reject) => {
  //     if (this.connection) {
  //       console.log("База данных уже открыта.");
  //       resolve(this.connection);
  //       return;
  //     };
  //     console.log("База данных не обнаружена. Создаю базу данных...");
  //     const openRequest: IDBOpenDBRequest = indexedDB.open(this.config.name, this.config.version);

  //     openRequest.onupgradeneeded = () => {
  //       const database: IDBDatabase = openRequest.result;
  //       this.createStorages(database, this.config.storages);
  //     };

  //     openRequest.onsuccess = () => {
  //       this.connection = openRequest.result;
  //       resolve(this.connection);
  //     };

  //     openRequest.onerror = () => {
  //       reject(openRequest.error);
  //     };
  //   })
  // }


  // TODO: мб сделать еще метод для закрытия соединения?

  
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
