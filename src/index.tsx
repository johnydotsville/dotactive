import ReactDOM from 'react-dom/client';
import { App } from "./components/App/App";

import { idbConfig } from './domain/database/config/idb-config';
import { Database } from "./domain/database/database";
import { ConstantManager } from './domain/services/constants/constant-manager';
import { PlayerService } from '@domain/services/player/player-service';
import { MatchService } from '@domain/services/matches/match-service';

async function prepare() {
  const database = new Database(idbConfig);
  await database.init();

  const accountId = 56831765;

  const ms = new MatchService(database);
  await ms.init(accountId);
  const matches = ms.getAllMatches();
  console.log(matches);
  const match = await ms.getMatch(8142183007);
  console.log(match);

  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <App />
  );
}

prepare();