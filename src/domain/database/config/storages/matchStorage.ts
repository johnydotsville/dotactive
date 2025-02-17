import { IStorage } from "../IDbConfig";

export const matchStorageConfig: IStorage = {
  name: "matches",
  options: {
    keyPath: "id"
  },
  indexes: [
    {
      name: "lobby_type_index",
      keyPath: "lobbyType",
    },
    {
      name: "start_date_index",
      keyPath: "startDateTime",
    }
  ]
};