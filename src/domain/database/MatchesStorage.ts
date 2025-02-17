import { Storage } from "./IStorage";
import { Match } from "@domain/services/matches/model/match";

export class MatchesStorage extends Storage<Match, number> {
  public constructor(database: IDBDatabase, storageName: string) {
    super(database, storageName);
  }
}