import { IStorageConfig } from "../IDbConfig";
import { StorageName } from "./StorageName";
import { MatchStorage } from "@domain/database/storage/MatchStorage";

// Сюда, возможно надо добавить еще тип данных, с которым будет работать хранилище.
// Например, это хранилище - под матчи. Значит как-то сюда этот тип указать, чтобы
// при создании экземпляров хранилища оно могло типизироваться этим типом.

export const matchStorageConfig: IStorageConfig = {
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