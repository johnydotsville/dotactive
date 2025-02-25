import { FakeModel } from "@domain/services/matches/model/FakeModel";
import { Storage } from "./Storage";
import { Match } from "@domain/services/matches/model/match";


export class ConstantStorage extends Storage<FakeModel, string> {
  public constructor(database: IDBDatabase, storageName: string) {
    super(database, storageName);
  }
}