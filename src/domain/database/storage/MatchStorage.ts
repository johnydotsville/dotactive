import { StorageName } from "../config/storages/StorageName";
import { Storage } from "./Storage";
import { Match } from "@domain/services/matches/model/match";


export class MatchStorage extends Storage<Match, number> {
  public constructor(database: IDBDatabase, storageName: StorageName) {
    super(database, storageName);
  }
}