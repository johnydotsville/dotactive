export interface IDbConfig {
  version: number;
  name: string;
  storages: IStorage[];
}

export interface IStorage {
  name: string;
  options?: IStorageOptions; 
  indexes?: IStorageIndex[]
}

export interface IStorageOptions {
  keyPath?: string;
  autoIncrement?: boolean;
}

export interface IStorageIndex {
  name: string
  keyPath: string;
  options?: {
    unique: boolean;
    multiEntry: boolean;
  }
}