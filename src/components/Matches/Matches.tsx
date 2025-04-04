import {useState} from 'react';
import { useEffect } from "react";
import { MatchLine } from './MatchLine/MatchLine';

import { useContext } from 'react';
import { DatabaseContext } from '@components/App/App';
import { MatchStorage } from '@domain/database/storage/MatchStorage';
import { MatchService } from '@domain/services/matches/MatchService';
import { StorageName } from '@domain/database/config/storages/StorageName';
import { MyDatabase } from '@domain/database/MyDatabase';
import { getCurrentUser } from '@utils/UserUtils';

import { MatchHistory } from './MatchHistory';


export default function Matches() {
  const database: MyDatabase = useContext(DatabaseContext);
  const [matches, setMatches] = useState([]);  // TODO: Как типизировать состояние?

  useEffect(() => {
    init();
    async function init() {
      const matchStorage = database.getStorage<MatchStorage>(StorageName.Matches);
      const ms = new MatchService(matchStorage);

      const accountId = getCurrentUser();  // TODO: Если не найден, тогда отобразить приглашение перейти на страницу с выбором пользователя.
      await ms.init(accountId);

      const allMatches = await ms.getAllMatches();
      setMatches(allMatches.result.reverse());
    }
  }, []);

  const displayMatches = matches.map(m => <MatchLine key={m.id} match={m} ></MatchLine>);

  return (
    <MatchHistory />
  )
  // return (
  //   <div>
  //     { displayMatches }
  //   </div>
  // )
}