import { DbOperationResult } from "../DbOperationResult";

export interface IStorage<T, K> {
  save(...data: T[]): Promise<DbOperationResult<T>[]>;
  delete(...keys: K[]): Promise<DbOperationResult<K>[]>;
  read(...keys: K[]): Promise<DbOperationResult<T | K>[]>;
}