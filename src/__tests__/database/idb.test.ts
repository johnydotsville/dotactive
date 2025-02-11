/*
  Что хочется протестировать:
  1. БД успешно создается и в ней создаются хранилища.
  2. CRUD-операции работают.

  Думаю создать какую-нибудь простую БД с простыми хранилищами и удалять ее после тестов.
*/

const idbConfig = {
  version: 1,
  dbname: 'dbtest',
  storages: [
    {
      name: "store1",
      settings: {
        keyPath: "id"
      }
    },
    {
      name: "store2",
      settings: { },
      indexes: []
    }
  ]
}

