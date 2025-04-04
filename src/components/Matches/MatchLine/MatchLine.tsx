import React from "react";
import Stack from "@mui/material/Stack";
import classNames from "classnames";
import { useMemo } from "react";
import { useNavigate } from "react-router-dom";


import * as styles from "./MatchLine.module.css";

import { Match } from "@domain/services/stratzapi/datamodel/Match";
import { PlayerMetricValue, PlayerMetricIcon, Metrics } from "@components/Common/PlayerMetric";
import { MiscMatchInfo } from "./MiscMatchInfo/MiscMatchInfo";
import { LobbyType } from "./LobbyType/LobbyType";
import { PlayerRole } from "../Common/PlayerRole/PlayerRole";
import { SuspectMarker } from "./SuspectMarker/SuspectMarker";
import { secondsToHMS } from "@utils/time-utils";
import { getPlayerPlaceByPerformance } from "@domain/services/analyze/utils";
import { kdaRatio } from "@domain/services/analyze/utils";
import { SuspChecker } from "@domain/services/analyze/SuspChecker";
import { getCurrentUser } from "@utils/UserUtils";


type MatchLineProps = {
  match: Match
}


export const MatchLine: React.FC<MatchLineProps> = ({ match }) => {
  const navigate = useNavigate();
  const info = useMemo(() => {
    const matchDuration = secondsToHMS(match.durationSeconds);
    
    const playerAccountId = getCurrentUser();  // TODO: Если не найден, тогда отобразить приглашение перейти на страницу с выбором пользователя.
    const player = match.matchPlayers.find(p => p.steamAccountid === playerAccountId);
    const teammates = match.matchPlayers.filter(p => p.isRadiant === player.isRadiant && p.steamAccountid !== playerAccountId);
    const enemies = match.matchPlayers.filter(p => p.isRadiant !== player.isRadiant);
    
    const kdaString = `${player.kills}/${player.deaths}/${player.assists}`;
    const kda = getPlayerPlaceByPerformance(kdaRatio(player.kills, player.deaths, player.assists),
      teammates.map(p => kdaRatio(p.kills, p.deaths, p.assists)),
      enemies.map(p => kdaRatio(p.kills, p.deaths, p.assists))
    );

    const gpm = getPlayerPlaceByPerformance(player.goldPerMinute, teammates.map(t => t.goldPerMinute), enemies.map(e => e.goldPerMinute));
    const xpm = getPlayerPlaceByPerformance(player.experiencePerMinute, teammates.map(t => t.experiencePerMinute), enemies.map(e => e.experiencePerMinute));
    const heroDmg = getPlayerPlaceByPerformance(player.heroDamage, teammates.map(t => t.heroDamage), enemies.map(e => e.heroDamage));
    const towerDmg = getPlayerPlaceByPerformance(player.towerDamage, teammates.map(t => t.towerDamage), enemies.map(e => e.towerDamage));

    const suspect = SuspChecker.checkMatchForSuspicious(match);

    return {
      matchDuration,
      player,
      kdaString,
      kda,
      gpm,
      xpm,
      heroDmg,
      towerDmg,
      suspect
    }
    }, [match.id]
  );


  const handleMatchLineClick = (matchId: number) => {
    navigate(`/matches/${matchId}`, { state: match });  // TODO: переделать потом, чтобы не хардкодить URL
  }

  return (
    <Stack 
      direction="row" 
      onClick={() => handleMatchLineClick(match.id)} 
      height="35px"
      justifyContent="space-between"
      sx={{ bgcolor: info.player.isVictory ? "#70E154" : "#E37777" }}
    >
      <SuspectMarker suspPoints={info.suspect} />
      <LobbyType lobbyType={match.lobbyType} />
      <div className={styles.matchDuration}>{info.matchDuration}</div>
      <PlayerRole heroname={info.player.heroShortName} position={info.player.position} />
      <PlayerMetricBox metric="KDA" value={info.kda} altValue={info.kdaString}/>
      <PlayerMetricBox metric="GPM" value={info.gpm} />
      <PlayerMetricBox metric="XPM" value={info.xpm} />
      <PlayerMetricBox metric="HERODMG" value={info.heroDmg} />
      <PlayerMetricBox metric="TOWERDMG" value={info.towerDmg} />
      <MiscMatchInfo matchId={match.id} startDateTimeUnix={match.startDateTime} />
    </Stack>
  )
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