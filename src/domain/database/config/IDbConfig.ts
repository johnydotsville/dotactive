import { IStorage } from "../storage/IStorage";
import { StorageName } from "./storages/StorageName";


export interface IDbConfig {
  dbname: string;
  version: number;
  storages: IStorageConfig<any, any>[];  // TODO: Здесь разве что можно union какой-то придумать из возможных типов данных
}


export interface IStorageConfig<T, K> {
  storageName: StorageName;
  oftype: new (database: IDBDatabase, storageName: string) => IStorage<T, K>;
  options?: IStorageOptions; 
  indexes?: IStorageIndex[]
}


export interface IStorageOptions {
  keyPath?: string;
  autoIncrement?: boolean;
}


export interface IStorageIndex {
  storageIndexName: string
  keyPath: string;
  options?: {
    unique: boolean;
    multiEntry: boolean;
  }
}