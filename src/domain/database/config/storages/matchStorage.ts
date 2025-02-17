import { IStorageConfig } from "../IDbConfig";

// Сюда, возможно надо добавить еще тип данных, с которым будет работать хранилище.
// Например, это хранилище - под матчи. Значит как-то сюда этот тип указать, чтобы
// при создании экземпляров хранилища оно могло типизироваться этим типом.

export const matchStorageConfig: IStorageConfig = {
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