import { FakeModel } from "@domain/services/matches/model/FakeModel";
import { Storage } from "./Storage";
import { StorageName } from "../config/storages/StorageName";


export class ConstantStorage extends Storage<FakeModel, string> {
  public constructor(database: IDBDatabase, storageName: StorageName) {
    super(database, storageName);
  }
}