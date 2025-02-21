import { Storage } from "./Storage";
import { Match } from "@domain/services/matches/model/match";


export class MatchStorage extends Storage<Match, number> {
  public constructor(database: IDBDatabase, storageName: string) {
    super(database, storageName);
  }
}