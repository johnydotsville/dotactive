import { DbOperationResult } from "../DbOperationResult";

export interface IStorage<T, K> {
  save(data: T): Promise<DbOperationResult<T>[]>;
  delete(key?: K | K[]): Promise<DbOperationResult<K>[]>;
  read(key: K): Promise<DbOperationResult<T | K>[]>;
}