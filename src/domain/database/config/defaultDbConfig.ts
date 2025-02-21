import { IDbConfig } from "./IDbConfig";
import { matchStorageConfig } from "./storages/matchStorageConfig";
import { constantStorageConfig } from "./storages/constantStorageConfig";

/**
 * Дефолтная конфигурация для indexedDb. Версия БД, имя для БД, а также массив
 * с настройками для хранилищ.
 */
export const defaultDbConfig: IDbConfig = {
  version: 1,
  dbname: 'dotactive',
  storages: [
    matchStorageConfig,
    constantStorageConfig  
  ]
}