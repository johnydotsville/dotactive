import { DbOperationResult } from "../DbOperationResult";


export interface IStorage<T, K> {
  save(data: T | T[]): Promise<DbOperationResult<T>>;
  read(key?: K | K[]): Promise<DbOperationResult<T>>;
  delete(key?: K | K[]): Promise<DbOperationResult<T>>;
  // TODO: метод чтения последних N записей
  // TODO: метод считывания пачки записей (вроде пагинации, т.е. сколько читать, сколько скипнуть и т.д.)
}