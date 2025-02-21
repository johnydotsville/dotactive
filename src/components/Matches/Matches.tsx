import {useState} from 'react';
import { useEffect } from "react";
import Match from "./Match/Match";

import { useContext } from 'react';
import { DatabaseContext } from '@components/App/App';
import { MatchStorage } from '@domain/database/storage/MatchStorage';
import { MatchService } from '@domain/services/matches/MatchService';


export default function Matches() {
  const database = useContext(DatabaseContext);
  const [matches, setMatches] = useState([]);

  useEffect(() => {
    init();
    async function init() {
      // const accountId = 56831765;
      // const matchStorage = new MatchStorage(database, "matches");
      // const ms = new MatchService(matchStorage);
      // await ms.init(accountId);
      // const allMatches = await ms.getAllMatches();
      // setMatches(allMatches.filter(m => m.succeeded).map(m => m.result));
    }
  }, []);

  // const matchesList = matches.map(m => <Match match={m} />);
  const allPaint = matches.map(m => <div key={m.id}>{m.id}</div>);

  return (
    <div>
      { allPaint }
      {/* <div>{matchesList}</div> */}
    </div>
  )
}