import { IDbConfig } from "./IDbConfig";
import { matchStorageConfig } from "./storages/matchStorageConfig";
import { constantStorageConfig } from "./storages/constantStorageConfig";
import { tokenStorageConfig } from "./storages/tokenStorageConfig";

/**
 * Дефолтная конфигурация для indexedDb. Версия БД, имя для БД, а также массив
 * с настройками для хранилищ.
 */
export const defaultDbConfig: IDbConfig = {
  version: 2,
  dbname: 'dotactive',
  storages: [
    matchStorageConfig,
    constantStorageConfig,
    tokenStorageConfig
  ]
}