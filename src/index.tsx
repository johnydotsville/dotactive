import ReactDOM from 'react-dom/client';
import { App } from "./components/App/App";

import { defaultDbConfig } from './domain/database/config/defaultDbConfig';
import { Database } from '@domain/database/Database';
import { ConstantManager } from './domain/services/constants/constant-manager';
import { PlayerService } from '@domain/services/player/player-service';
import { MatchService } from '@domain/services/matches/match-service';
import { Match } from '@domain/services/matches/model/match';
import { MatchesStorage } from '@domain/database/storage/MatchesStorage';

async function prepare() {
  const database = new Database(defaultDbConfig);
  await database.init();

  const accountId = 56831765;

  const matchStorage = new MatchesStorage(database.database, "matches");
  const ms = new MatchService(database, matchStorage);
  await ms.init(accountId);
  const matches = await ms.getAllMatches();
  console.log(matches);

  const match = await ms.getMatch(8145432965);
  console.log(match);

  const fewMatches = await ms.getMatches(8146456949, 8148280087, 8166687583);
  console.log(fewMatches);

  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <App />
  );
}

prepare();