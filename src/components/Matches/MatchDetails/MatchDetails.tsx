import { Box, Divider, Typography } from "@mui/material";
import { Container, Stack } from "@mui/material";

import { useLocation } from "react-router-dom";
import { useParams } from "react-router-dom";
import { useContext } from "react";
import { useEffect } from "react";
import { useState } from "react";
import { useMemo } from "react";

import { DatabaseContext } from "@components/App";
import { MyDatabase } from "@domain/database/MyDatabase";
import { MatchStorage } from "@domain/database/storage/MatchStorage";
import { StorageName } from "@domain/database/config/storages/StorageName";
import { Matchup } from "./Matchup";
import { getRadiantTeam, getDireTeam } from "@domain/services/analyze/utils";
import { getCurrentUser } from "@utils/UserUtils";


export const MatchDetails = () => {  
  const matchInfo = useLocation().state;
  const database: MyDatabase = useContext(DatabaseContext);
  const { id: matchId } = useParams();
  const [ match, setMatch ] = useState(null);
  const [ loading, setLoading ] = useState(true);

  useEffect(() => {
    if (matchInfo) {
      setMatch(matchInfo);
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

  const playerAccountId = getCurrentUser();

  const radiant = getRadiantTeam(match.matchPlayers);
  const dire = getDireTeam(match.matchPlayers);

  const matchupbox = (
    <Stack direction="column" alignItems="center" gap={5}>
      <Typography variant="body1" sx={{ fontSize: "2.5rem" }}>Состав команд</Typography>
      <Matchup match={match} />
    </Stack>
  ) 

  return (
    <Container>
      { matchupbox }
    </Container>
  )
}