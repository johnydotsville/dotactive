import ReactDOM from 'react-dom/client';
import { App } from "./components/App/App";

import { defaultDbConfig } from './domain/database/config/defaultDbConfig';
import { MyDatabase } from '@domain/database/MyDatabase';
import { ConstantManager } from './domain/services/constants/constant-manager';
import { PlayerService } from '@domain/services/player/player-service';
import { MatchService } from '@domain/services/matches/MatchService';
import { Match } from '@domain/services/stratzapi/datamodel/match';
import { StorageName } from '@domain/database/config/storages/StorageName';
import { MatchStorage } from '@domain/database/storage/MatchStorage';
import { StratzAPI } from '@domain/services/stratzapi/StratzAPI';


async function prepare() {
  const database = MyDatabase.getInstance();
  await database.init();
  const connection = database.getConnection();

  const matchStorage = database.getStorage<MatchStorage>(StorageName.Matches);
  // const matchStorage = database.getStorage(StorageName.Matches);
  const api = new StratzAPI();
  const ms = new MatchService(matchStorage, api);

  const accountId = 56831765;
  await ms.init(accountId);

  const allMatches = await ms.getAllMatches();
  console.log(allMatches);

  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    // <App database={connection} />
    <div>Hello, dotactive!</div>
  );
}

prepare();