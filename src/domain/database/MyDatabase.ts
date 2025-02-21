import { IDbConfig } from "./config/IDbConfig";
import { IStorageConfig } from "./config/IDbConfig";
import { IStorageIndex } from "./config/IDbConfig";
import { defaultDbConfig } from "./config/defaultDbConfig";
import { IStorage } from "./storage/IStorage";
import { StorageName } from "@domain/database/config/storages/StorageName";


export class MyDatabase {
  private config: IDbConfig;
  private connection: IDBDatabase;
  private static instance: MyDatabase;
  private storages: Map<StorageName, IStorage<any, any>>;

  
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
      const openRequest: IDBOpenDBRequest = indexedDB.open(this.config.dbname, this.config.version);

      openRequest.onupgradeneeded = () => {
        const database: IDBDatabase = openRequest.result;
        this.createStorages(database, this.config.storages);
      };

      openRequest.onsuccess = () => {
        this.connection = openRequest.result;
        this.createStorageInstances(this.connection);
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


  // TODO: мб сделать еще метод для закрытия соединения?

  
  private createStorages(database: IDBDatabase, storages: IStorageConfig[]) {
    storages.forEach(s => {
      if (!database.objectStoreNames.contains(s.storageName)) {
        const storage: IDBObjectStore = database.createObjectStore(s.storageName, s?.options);
        if (s.indexes) {
          this.createIndexes(storage, s.indexes);
        }
      }
    });
  }


  private createIndexes(storage: IDBObjectStore, indexes: IStorageIndex[]) {
    indexes.forEach(x => storage.createIndex(x.storageIndexName, x.keyPath, x?.options));
  }


  private createStorageInstances(connection: IDBDatabase) {
    this.storages = new Map();
    this.config.storages.forEach(s => {
      if (s.oftype) {
        this.storages.set(s.storageName, new s.oftype(connection, s.storageName));
      }
    });
  }

  public getStorage(storageName: StorageName) {
    return this.storages.get(storageName);
  }
}
