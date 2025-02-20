import ReactDOM from 'react-dom/client';
import { App } from "./components/App/App";

import { defaultDbConfig } from './domain/database/config/defaultDbConfig';
import { MyDatabase } from '@domain/database/MyDatabase';
import { ConstantManager } from './domain/services/constants/constant-manager';
import { PlayerService } from '@domain/services/player/player-service';
import { MatchService } from '@domain/services/matches/MatchService';
import { Match } from '@domain/services/matches/model/match';
import { MatchesStorage } from '@domain/database/storage/MatchesStorage';

async function prepare() {
  const database = new MyDatabase(defaultDbConfig);

  const accountId = 56831765;

  const matchStorage = new MatchesStorage(database, "matches");

  const ms = new MatchService(matchStorage);
  await ms.init(accountId);

  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <App />
  );
}

prepare();