import { StorageName } from "../config/storages/StorageName";
import { Storage } from "./Storage";
import { Match } from "@domain/services/stratzapi/datamodel/Match";


export class MatchStorage extends Storage<Match, number> {
  public constructor(database: IDBDatabase, storageName: StorageName) {
    super(database, storageName);
  }
}