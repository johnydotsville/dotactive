import { IStorage } from "../storage/IStorage";
import { StorageName } from "./storages/StorageName";


export interface IDbConfig {
  dbname: string;
  version: number;
  storages: IStorageConfig<unknown, unknown>[];
}


export interface IStorageConfig<T, K> {
  storageName: StorageName;
  // TODO: а что если тут написать typeof Storage<T, K>
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