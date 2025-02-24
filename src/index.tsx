import ReactDOM from 'react-dom/client';
import { App } from "./components/App/App";

import { defaultDbConfig } from './domain/database/config/defaultDbConfig';
import { MyDatabase } from '@domain/database/MyDatabase';
import { ConstantManager } from './domain/services/constants/constant-manager';
import { PlayerService } from '@domain/services/player/player-service';
import { MatchService } from '@domain/services/matches/MatchService';
import { Match } from '@domain/services/matches/model/match';
import { StorageName } from '@domain/database/config/storages/StorageName';


async function prepare() {
  const database = MyDatabase.getInstance();
  await database.init();
  const connection = database.getConnection();

  const matchStorage = database.getStorage(StorageName.Matches);
  const ms = new MatchService(matchStorage);

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