import ReactDOM from 'react-dom/client';
import { App } from "./components/App/App";

import { defaultDbConfig } from './domain/database/config/defaultDbConfig';
import { MyDatabase } from '@domain/database/MyDatabase';
import { ConstantManager } from './domain/services/constants/constant-manager';
import { PlayerService } from '@domain/services/player/player-service';
import { MatchService } from '@domain/services/matches/MatchService';
import { Match } from '@domain/services/stratzapi/datamodel/Match';
import { StorageName } from '@domain/database/config/storages/StorageName';
import { MatchStorage } from '@domain/database/storage/MatchStorage';
import { StratzAPI } from '@domain/services/stratzapi/StratzAPI';

import { MatchQueryBuilder } from '@domain/services/stratzapi/builders/MatchQueryBuilder';


async function prepare() {
  const database = MyDatabase.getInstance();
  await database.init();

  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
    <App database={database} />
  );
}

prepare();