import { StorageName } from "./storages/StorageName";


export interface IDbConfig {
  dbname: string;
  version: number;
  storages: IStorageConfig[];
}

export interface IStorageConfig {
  storageName: StorageName;
  oftype?: any,
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