import { Match } from "@domain/services/stratzapi/datamodel/Match";
import { IStorageConfig } from "../IDbConfig";
import { StorageName } from "./StorageName";
import { MatchStorage } from "@domain/database/storage/MatchStorage";


export const matchStorageConfig: IStorageConfig<Match, number> = {
  storageName: StorageName.Matches,
  oftype: MatchStorage,
  options: {
    keyPath: "id"
  },
  indexes: [
    {
      storageIndexName: "lobby_type_index",
      keyPath: "lobbyType",
    },
    {
      storageIndexName: "start_date_index",
      keyPath: "startDateTime",
    }
  ]
};