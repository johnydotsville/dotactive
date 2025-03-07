import React from "react";
import classNames from "classnames";
import { useMemo } from "react";

import * as styles from "./MatchLine.module.css";

import { Match } from "@domain/services/stratzapi/datamodel/Match";
import { PlayerStat } from "./PlayerStat/PlayerStat";
import { MiscMatchInfo } from "./MiscMatchInfo/MiscMatchInfo";
import { LobbyType } from "./LobbyType/LobbyType";
import { PlayerRole } from "./PlayerRole/PlayerRole";
import { SuspectMarker } from "./SuspectMarker/SuspectMarker";

import { secondsToHMS } from "@utils/time-utils";
import { getPlayerPlaceByPerformance } from "@domain/services/analyze/utils";
import { kdaRatio } from "@domain/services/analyze/utils";
import { SuspChecker } from "@domain/services/analyze/SuspChecker";


type MatchLineProps = {
  match: Match
}


export const MatchLine: React.FC<MatchLineProps> = ({ match }) => {
  const info = useMemo(() => {
    const matchDuration = secondsToHMS(match.durationSeconds);
    
    const playerAccountId = 56831765;  // TODO: переделать, чтобы бралось из редакса или типа того
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

  const statStub = `/assets/img/player_stats_icons/tmp_stat.svg`;  
  const wrapperStyles = classNames([styles.wrapper, info.player.isVictory ? styles.win : styles.lose])

  // TODO: Сделать, чтобы при наведении на MatchLine курсор менял вид на руку, как на ссылке.
  const handleMatchLineClick = (matchId: number) => {
    alert(`Должно открываться окно детальной информации о матче ${matchId}.`);
  }

  return (
    <div className={wrapperStyles} onClick={() => handleMatchLineClick(match.id)}>
      <SuspectMarker suspPoints={info.suspect} />
      <LobbyType lobbyType={match.lobbyType} />
      <div className={styles.matchDuration}>{info.matchDuration}</div>
      <PlayerRole heroname={info.player.heroShortName} position={info.player.position} />
      <PlayerStat pic={statStub} stat={info.kda} altValue={info.kdaString}/>
      <PlayerStat pic={statStub} stat={info.gpm} />
      <PlayerStat pic={statStub} stat={info.xpm} />
      <PlayerStat pic={statStub} stat={info.heroDmg} />
      <PlayerStat pic={statStub} stat={info.towerDmg} />
      <MiscMatchInfo matchId={match.id} startDateTimeUnix={match.startDateTime} />
    </div>
  )
}