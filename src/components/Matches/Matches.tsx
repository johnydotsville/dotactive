import {useState} from 'react';
import { useEffect } from "react";
import Match from "./Match/Match";

/*-----------------------------------------------------*/
import { defaultDbConfig } from '@domain/database/config/defaultDbConfig';
import { Database } from "@domain/database/database";
import { MatchService } from '@domain/services/matches/match-service';
/*-----------------------------------------------------*/

export default function Matches() {

  const [matches, setMatches] = useState([]);

  useEffect(() => {
    async function initDb() {
      const database = new Database(defaultDbConfig);
      await database.init();
      const accountId = 56831765;
      const ms = new MatchService(database);
      await ms.init(accountId);
      setMatches(ms.getAllMatches());
    }
    initDb();
  }, []);

  const matchesList = matches.map(m => <Match match={m} />);

  return (
    <div>
      <div>{matchesList}</div>
    </div>
  )
}