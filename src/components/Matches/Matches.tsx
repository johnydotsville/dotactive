import {useState} from 'react';
import { useEffect } from "react";
import { Match } from "./Match/Match";
import { MatchLine } from './MatchLine/MatchLine';

import { useContext } from 'react';
import { DatabaseContext } from '@components/App/App';
import { MatchStorage } from '@domain/database/storage/MatchStorage';
import { MatchService } from '@domain/services/matches/MatchService';
import { StorageName } from '@domain/database/config/storages/StorageName';
import { StratzAPI } from '@domain/services/stratzapi/StratzAPI';
import { MyDatabase } from '@domain/database/MyDatabase';


export default function Matches() {
  const database: MyDatabase = useContext(DatabaseContext);
  const [matches, setMatches] = useState([]);  // TODO: Как типизировать состояние?

  useEffect(() => {
    init();
    async function init() {
      const matchStorage = database.getStorage<MatchStorage>(StorageName.Matches);
      const api = new StratzAPI();
      const ms = new MatchService(matchStorage, api);

      const accountId = 56831765;
      await ms.init(accountId);

      const allMatches = await ms.getAllMatches();
      setMatches(allMatches.result.reverse());
    }
  }, []);

  // const matchesList = matches.map(m => <Match match={m} />);
  // const allPaint = matches.map(m => <div key={m.id}>{m.id}</div>);
  const displayMatches = matches.map(m => <MatchLine key={m.id} match={m} ></MatchLine>);

  return (
    <div>
      { displayMatches }
    </div>
  )
}