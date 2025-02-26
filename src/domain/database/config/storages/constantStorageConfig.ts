import { FakeModel } from "@domain/services/stratzapi/datamodel/FakeModel";
import { IStorageConfig } from "../IDbConfig";
import { StorageName } from "./StorageName";
import { ConstantStorage } from "@domain/database/storage/ConstantStorage";


export const constantStorageConfig: IStorageConfig<FakeModel, string> = {
  storageName: StorageName.Constants,
  oftype: ConstantStorage,
  options: {
    keyPath: "id"
  },
};