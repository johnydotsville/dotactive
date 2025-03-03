import { IDbConfig } from "./config/IDbConfig";
import { IStorageConfig } from "./config/IDbConfig";
import { IStorageIndex } from "./config/IDbConfig";
import { defaultDbConfig } from "./config/defaultDbConfig";
import { IStorage } from "./storage/IStorage";
import { StorageName } from "@domain/database/config/storages/StorageName";


// TODO: Можно придумать какой-нибудь класс StorageKeeper, который бы умел
// делать так, как предложили в интернете решить проблему с getStorage.
// Передать этот класс в БД и делегировать ему извлечение хранилища.


export class MyDatabase {
  private static instance: MyDatabase;
  private config: IDbConfig;
  private connection: IDBDatabase;
  private storages: Map<StorageName, IStorage<unknown, unknown>>;

  
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
      const openRequest: IDBOpenDBRequest = indexedDB.open(this.config.dbname, this.config.version);

      openRequest.onupgradeneeded = () => {
      console.log("База данных не обнаружена или требует обновления.");
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

  
  private createStorages(database: IDBDatabase, storages: IStorageConfig<any, any>[]) {
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
      this.storages.set(s.storageName, new s.oftype(connection, s.storageName));
    });
  }


  public getStorage<T>(storageName: StorageName): T  {
    return this.storages.get(storageName) as T;
  }
}



/*
Альтернативные варианты, как можно сделать метод getStorage, чтобы он проверял типы.

// ======================= Вариант 1

type DbOperationResult<T> = {preved: T};

interface IStorage<T, K> {
  save(data: T | T[]): Promise<DbOperationResult<T>[]>;
  medved: K;
}

interface IStorageConfig<T, K> {
    oftype: new (database: IDBDatabase, storageName: string) => IStorage<T, K>;
}





// --------------- использование --------------------
type Match = {a: number};
type Match2 = {b: string};

class MatchStorage implements IStorage<Match, number> {
  public constructor(database: IDBDatabase, storageName: string) {}
  medved = 1;
  save() {return 1 as never}
}

class Match2Storage implements IStorage<Match2, string> {
  public constructor(database: IDBDatabase, storageName: string) {}
  medved = '';
  save() {return 1 as never}
}

enum StorageName {
    Matches = 'Matches',
    Matches2 = 'Matches2'
}

const matchStorageConfig: IStorageConfig<Match, number> = {
    oftype: MatchStorage
}

const match2StorageConfig: IStorageConfig<Match2, string> = {
    oftype: Match2Storage
}


// сводный конфиг по всем
const fullConfig = {
    [StorageName.Matches]: matchStorageConfig,
    [StorageName.Matches2]: match2StorageConfig
} satisfies Record<StorageName, IStorageConfig<unknown, unknown>>;

type GetStorageType<N extends StorageName> = InstanceType<typeof fullConfig[N]['oftype']>;

// теперь не генерик, но знает обо всех типах стораджей
class Database {
    constructor(private db: IDBDatabase) {}

    getStorage<N extends StorageName>(name: N): GetStorageType<N> {
        const c = fullConfig[name];

        return new c.oftype(this.db, name) as GetStorageType<N>;
    }
}

declare const db: IDBDatabase;

// экземпляр
const database = new Database(db);




// ------------ использование database ------------
const matchStorage = database.getStorage(StorageName.Matches);

const x = matchStorage.save({a: 1});
//    ^?


const match2Storage = database.getStorage(StorageName.Matches2);

const y = match2Storage.save({b: ''});
//    ^?


// ======================= Вариант 2, с дженериками на самой БД

type FakeIDBDatabase = { }

type DbOperationResult<T> = {preved: T};

interface IStorage<T, K> {
  save(data: T | T[]): Promise<DbOperationResult<T>[]>;
  medved: K;
}

interface IStorageConfig<T, K> {
    oftype: new (database: FakeIDBDatabase, storageName: string) => IStorage<T, K>;
}

class Database<M extends Record<string, IStorageConfig<unknown, unknown>>> {
    constructor(private cfg: M, private db: FakeIDBDatabase) {}

    getStorage<N extends string & keyof M>(name: N): InstanceType<M[N]['oftype']> {
        const c = this.cfg[name];

        return new c.oftype(this.db, name) as InstanceType<M[N]['oftype']>;
    }
}



// --------------- использование --------------------
type Match = {a: number};
type Match2 = {b: string};

class MatchStorage implements IStorage<Match, number> {
  public constructor(database: FakeIDBDatabase, storageName: string) {}
  medved = 1;
  save() {return 1 as never}
}

class Match2Storage implements IStorage<Match2, string> {
  public constructor(database: FakeIDBDatabase, storageName: string) {}
  medved = '';
  save() {return 1 as never}
}

enum StorageName {
    Matches = 'Matches',
    Matches2 = 'Matches2'
}

const matchStorageConfig: IStorageConfig<Match, number> = {
    oftype: MatchStorage
}

const match2StorageConfig: IStorageConfig<Match2, string> = {
    oftype: Match2Storage
}



// ***********************************
// создаем Database со всеми конфигами
// ***********************************
// declare const db: IDBDatabase;
let db: FakeIDBDatabase = { };

const database = new Database({
    [StorageName.Matches]: matchStorageConfig,
    [StorageName.Matches2]: match2StorageConfig
}, db);




// ------------ использование database ------------
const matchStorage = database.getStorage(StorageName.Matches);

const x = matchStorage.save({a: 1});
//    ^?


const match2Storage = database.getStorage(StorageName.Matches2);

const y = match2Storage.save({b: ''});
//    ^?


*/