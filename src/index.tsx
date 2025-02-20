import ReactDOM from 'react-dom/client';
import { App } from "./components/App/App";

import { defaultDbConfig } from './domain/database/config/defaultDbConfig';
import { MyDatabase } from '@domain/database/MyDatabase';
import { ConstantManager } from './domain/services/constants/constant-manager';
import { PlayerService } from '@domain/services/player/player-service';
import { MatchService } from '@domain/services/matches/match-service';
import { Match } from '@domain/services/matches/model/match';
import { MatchesStorage } from '@domain/database/storage/MatchesStorage';

async function prepare() {
  const database = new MyDatabase(defaultDbConfig);
  
  // const connection = await database.getConnection();

  const accountId = 56831765;

  const connection = await database.getConnection();

  // // const matchStorage = new MatchesStorage(connection, "matches");
  const matchStorage = new MatchesStorage(database, "matches", connection);
  // await matchStorage.init();


  const ms = new MatchService(matchStorage);
  await ms.init(accountId);
  // // const matches = await ms.getAllMatches();
  const matches = await ms.getMatches();
  console.log(matches);

  // // // const match = await ms.getMatch(8145432965);
  const match = await ms.getMatches(8145432965);
  console.log(match);

  let fewMatches = await ms.getMatches(8146456949, 8148280087, 8166687583, 228);
  console.log(fewMatches);

  // debugger;
  const reportDelete = await ms.deleteMatches(8146456949, 8148280087, 8166687583);
  console.log(reportDelete);

  fewMatches = await ms.getMatches(8146456949, 8148280087, 8166687583, 228);
  console.log(fewMatches);

  debugger;
  const clearReport = await ms.deleteMatches();

  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <App />
  );
}

prepare();