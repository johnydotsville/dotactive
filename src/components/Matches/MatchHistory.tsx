import { DataGrid, GridColDef } from '@mui/x-data-grid';
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Typography } from '@mui/material';
import { Stack } from '@mui/material';
import { Box } from '@mui/material';

import { useState } from 'react';
import { useEffect } from "react";
import { useContext } from 'react';
import { useNavigate } from "react-router-dom";

import { DatabaseContext } from '@components/App';
import { MatchStorage } from '@domain/database/storage/MatchStorage';
import { MatchService } from '@domain/services/matches/MatchService';
import { StorageName } from '@domain/database/config/storages/StorageName';
import { MyDatabase } from '@domain/database/MyDatabase';

import { getCurrentUser } from '@utils/UserUtils';
import { getPlayerPlaceByPerformance } from "@domain/services/analyze/utils";
import { kdaRatio } from "@domain/services/analyze/utils";
import { SuspChecker } from "@domain/services/analyze/SuspChecker";
import { DateUtils } from "@utils/DateUtils";
import { secondsToHMS } from "@utils/time-utils";

import { PlayerMetricValue, PlayerMetricIcon, Metrics } from "@components/Common/PlayerMetric";
import { HeroPortrait } from "@components/Common/HeroPortrait";
import { PlayerPosition } from "@components/Common/PlayerPosition";
import { SuspectMatchIcon } from '@components/Common/MiscIcons';


export function MatchHistory() {
  const navigate = useNavigate();
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

  const playerAccountId = getCurrentUser();  // TODO: Если не найден, тогда отобразить приглашение перейти на страницу с выбором пользователя.

  const rows = matches.map(m => {
    const player = m.matchPlayers.find(p => p.steamAccountid === playerAccountId);
    const teammates = m.matchPlayers.filter(p => p.isRadiant === player.isRadiant && p.steamAccountid !== playerAccountId);
    const enemies = m.matchPlayers.filter(p => p.isRadiant !== player.isRadiant);
    
    const kdaString = `${player.kills}/${player.deaths}/${player.assists}`;
    const kda = getPlayerPlaceByPerformance(kdaRatio(player.kills, player.deaths, player.assists),
      teammates.map(p => kdaRatio(p.kills, p.deaths, p.assists)),
      enemies.map(p => kdaRatio(p.kills, p.deaths, p.assists))
    );

    const suspect = SuspChecker.checkMatchForSuspicious(m);
    const matchDuration = secondsToHMS(m.durationSeconds);

    const gpm = getPlayerPlaceByPerformance(player.goldPerMinute, teammates.map(t => t.goldPerMinute), enemies.map(e => e.goldPerMinute));
    const xpm = getPlayerPlaceByPerformance(player.experiencePerMinute, teammates.map(t => t.experiencePerMinute), enemies.map(e => e.experiencePerMinute));
    const heroDmg = getPlayerPlaceByPerformance(player.heroDamage, teammates.map(t => t.heroDamage), enemies.map(e => e.heroDamage));
    const towerDmg = getPlayerPlaceByPerformance(player.towerDamage, teammates.map(t => t.towerDamage), enemies.map(e => e.towerDamage));

    const handleMatchLineClick = (matchId: number) => {
      navigate(`/matches/${matchId}`, { state: m });  // TODO: переделать потом, чтобы не хардкодить URL
    }

    return {
      matchId: m.id,
      suspect: <SuspectMarker suspPoints={suspect} />,
      isVictory: player.isVictory,
      lobbyType: <LobbyType lobbyType={m.lobbyType} />,
      matchDuration: <Typography>{matchDuration}</Typography>,
      hero: <HeroPortrait heroname={player.heroShortName} w="80px" />,
      position: <PlayerPosition position={player.position} w="30px" />,
      kda: <PlayerMetricBox metric="KDA" value={kda} altValue={kdaString} />,
      gpm: <PlayerMetricBox metric="GPM" value={gpm} />,
      xpm: <PlayerMetricBox metric="XPM" value={xpm} />,
      herodmg: <PlayerMetricBox metric="HERODMG" value={heroDmg} />,
      towerdmg: <PlayerMetricBox metric="TOWERDMG" value={towerDmg} />,
      miscinfo: <MiscMatchInfo matchId={m.id} startDateTimeUnix={m.startDateTime} />,
      gotoMatchDetails: handleMatchLineClick
    }
  });


  return (
    <TableContainer>
      <Table>
        <TableBody
          // sx={{ bgcolor: "#1D242D" }}
        >
          { rows.map(r => (
            <TableRow 
              key={r.matchId}
              onClick={() => r.gotoMatchDetails(r.matchId)}
              sx={{ bgcolor: r.isVictory ? "#70E154" : "#E37777" }}
            >
              <TableCell>{ r.suspect }</TableCell>
              <TableCell>{ r.lobbyType }</TableCell>
              <TableCell>{ r.matchDuration }</TableCell>
              <TableCell>{ r.hero }</TableCell>
              <TableCell>{ r.position }</TableCell>
              <TableCell>{ r.kda }</TableCell>
              <TableCell>{ r.gpm }</TableCell>
              <TableCell>{ r.xpm }</TableCell>
              <TableCell>{ r.herodmg }</TableCell>
              <TableCell>{ r.towerdmg }</TableCell>
              <TableCell>{ r.miscinfo }</TableCell>
            </TableRow>
          )) }
        </TableBody>
      </Table>
    </TableContainer>
  );
}


type PlayerMetricBoxProps = {
  metric: Metrics,
  value: [number, number, number]
  altValue?: string;
}

function PlayerMetricBox({ metric, value, altValue }: PlayerMetricBoxProps) {
  return (
    <Stack direction="row" alignItems="center" spacing={1}>
      <PlayerMetricIcon metric={metric} w="25px" h="25px" />
      <PlayerMetricValue value={value} altValue={altValue} />
    </Stack>
  )
}


function MiscMatchInfo({ matchId, startDateTimeUnix }) {
  return (
    <Stack>
      <Typography>{ DateUtils.formatUnixToDate(startDateTimeUnix) }</Typography>
      <Typography>{ matchId }</Typography>
    </Stack>
  )
}


function LobbyType({ lobbyType }) {
  const lobby = lobbyType.slice(0, 2).toUpperCase();
  
  const colorMap = {
    RANKED: "#34CDCD",
    UNRANKED: "#DCD8D8",
    TURBO: "#DFF77F"
  }
  const bgcolor = colorMap[lobbyType] || "#DFF77F";

  return (
    <Stack
      direction="row"
      bgcolor={bgcolor}
      justifyContent="center"
      sx={{ fontSize: "1.5rem" }}
    >
      {lobby}
    </Stack>
  )
}


function SuspectMarker({ suspPoints }) {
  let isSusp = false;

  if (suspPoints > 0) {
    isSusp = true;
  }

  return (
    <Box>
      { isSusp && <SuspectMatchIcon w="35px" h="35px" />}
    </Box>
  )
}