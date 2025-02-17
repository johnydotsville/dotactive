import { IDbConfig } from "./IDbConfig";
import { matchStorageConfig } from "./storages/matchStorage";
import { constantStorageConfig } from "./storages/constantStorage";

/**
 * Дефолтная конфигурация для indexedDb. Версия БД, имя для БД, а также массив
 * с настройками для хранилищ.
 */
export const defaultDbConfig: IDbConfig = {
  version: 1,
  name: 'dotactive',
  storages: [
    matchStorageConfig,
    constantStorageConfig  
  ]
}