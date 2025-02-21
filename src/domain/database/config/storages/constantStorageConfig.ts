import { IStorageConfig } from "../IDbConfig";
import { StorageName } from "./StorageName";

// Здесь можно будет дописать только когда будет класс под это хранилище
// export const constantStorageConfig: IStorageConfig = {
export const constantStorageConfig = {
  storageName: StorageName.Constants,
};