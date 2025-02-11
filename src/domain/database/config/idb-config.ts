/**
 * Конфигурация для indexedDb. Версия БД, имя для БД, а также массив
 * с настройками для хранилищ.
 */
export const idbConfig = {
  // TODO: написать тип для этого конфига.
  // TODO: описание хранилища можно сделать отдельным классом тоже.
  version: 1,
  dbname: 'dotactive',
  storages: [
    {
      name: "matches",
      options: {
        keyPath: "id"
      },
      indexes: [
        {
          name: "lobby_type_index",
          keyPath: "lobbyType",
          options: { }
        },
        {
          name: "start_date_index",
          keyPath: "startDateTime",
          options: { }
        }
      ]
    },
    {
      name: "constants",
      options: { },
      indexes: []
    }
  ]
}

/*
  TODO: сделать проверки в местах, пользующихся конфигом - если поля нет, 
  например, settings, чтобы они не пытались к нему
  обращаться. Это позволит убрать из конфига пустые объекты и массивы.
*/