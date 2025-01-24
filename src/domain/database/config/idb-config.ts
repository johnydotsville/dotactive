export const idbConfig = {
  version: 1,
  dbname: 'dotastats',
  storages: [
    {
      name: "matches",
      settings: {
        keyPath: "id"
      },
      indexes: [
        {
          name: "lobby_type",
          keyPath: "lobbyType",
          options: { }
        }
      ]
    },
    {
      name: "constants",
      settings: { },
      indexes: []
    }
  ]
}

/*
  TODO: сделать проверки в местах, пользующихся конфигом - если поля нет, например, settings, чтобы они не пытались к нему
  обращаться. Это позволит убрать из конфига пустые объекты и массивы.
*/