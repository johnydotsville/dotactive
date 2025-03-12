import { Token } from "@domain/database/storage/TokenStorage";
import { IStorageConfig } from "../IDbConfig";
import { StorageName } from "./StorageName";
import { TokenStorage } from "@domain/database/storage/TokenStorage";


export const tokenStorageConfig: IStorageConfig<Token, number> = {
  storageName: StorageName.Tokens,
  oftype: TokenStorage,
  options: {
    keyPath: "id",
    autoIncrement: true
  }
};