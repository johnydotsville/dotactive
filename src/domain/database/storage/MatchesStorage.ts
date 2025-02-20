import { MyDatabase } from "@domain/database/MyDatabase";
import { Storage } from "./Storage";
import { Match } from "@domain/services/matches/model/match";

export class MatchesStorage extends Storage<Match, number> {
  public constructor(database: MyDatabase, storageName: string, connection?: IDBDatabase) {
    super(database, storageName, connection);
  }
}