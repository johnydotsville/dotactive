import { useLocation } from "react-router-dom";
import { useParams } from "react-router-dom";
import { useContext } from "react";
import { useEffect } from "react";
import { useState } from "react";
import { useMemo } from "react";

import * as styles from "./MatchDetails.module.css"
import { CarryIcon, MidIcon, HardlineIcon, SoftSupportIcon, HardSupportIcon } from "@components/Misc/PositionIcons";
import { DatabaseContext } from "@components/App/App";
import { MyDatabase } from "@domain/database/MyDatabase";
import { MatchStorage } from "@domain/database/storage/MatchStorage";
import { StorageName } from "@domain/database/config/storages/StorageName";


export const MatchDetails = () => {  
  const matchSent = useLocation().state;
  const database: MyDatabase = useContext(DatabaseContext);
  const { id: matchId } = useParams();
  const [ match, setMatch ] = useState(null);
  const [ loading, setLoading ] = useState(true);

  useEffect(() => {
    if (matchSent) {
      setMatch(matchSent);
      setLoading(false);  // TODO: разобраться получше, как все эти независимые состояния будут работать вместе, как они устанавливаются, как при перерисовке анализируются и т.д.
    } else {
      setLoading(true);
      loadMatch();
    }
    async function loadMatch() {
      const storage = database.getStorage<MatchStorage>(StorageName.Matches);
      const match = await storage.read(Number(matchId));
      setMatch(match.result[0]);
      setLoading(false);  // TODO: здесь норм такой порядок установки состояний?
    }
  }, []);

  if (loading) {
    return <div style={{fontSize: "50px"}}>Загружаю данные о матче из локальной БД...</div>
  }

  return (
    <div className={styles.wrapper}>
      { match.id }
    </div>
  )
}