import React from "react";

import * as styles from "./MatchLine.module.css";

import { Match } from "@domain/services/stratzapi/datamodel/Match";
import { PlayerStat } from "./PlayerStat/PlayerStat";
import { MiscMatchInfo } from "./MiscMatchInfo/MiscMatchInfo";
import { LobbyType } from "./LobbyType/LobbyType";

import { secondsToHMS } from "@utils/time-utils";


type MatchLineProps = {
  match: Match
}


export const MatchLine: React.FC<MatchLineProps> = ({ match }) => {
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

  const heroimg = `/assets/img/heroes/${player.heroShortName}.png`;
  const posimg = `/assets/img/pos_icons/${player.position ?? "unknown"}.svg`;
  const statStub = `/assets/img/player_stats_icons/tmp_stat.svg`;
  const suspimg = `/assets/img/misc/susp_match.png`;

  const bgColor = player.isVictory ? winBgColor : loseBgColor;

  return (
    <div className={styles.matchLine} style={{backgroundColor: bgColor}}>
      <div className={styles.suspMatch}>
        <img className={styles.suspMatchImg} src={suspimg} />
      </div>
      <LobbyType lobbyType={match.lobbyType} />
      {matchDuration}
      <div className={styles.playerHero}>
        <img className={styles.playerHeroImg} src={heroimg} />
      </div>
      <div className={styles.playerPosition}>
        <img className={styles.playerPositionImg} src={posimg} />
      </div>
      <PlayerStat pic={statStub} stat={kda} alt={kdaString}/>
      <PlayerStat pic={statStub} stat={gpm} />
      <PlayerStat pic={statStub} stat={xpm} />
      <PlayerStat pic={statStub} stat={heroDmg} />
      <PlayerStat pic={statStub} stat={towerDmg} />
      <MiscMatchInfo matchId={match.id} startDateTimeUnix={match.startDateTime} />
    </div>
  )
}


const winBgColor = "#70E154";
const loseBgColor = "#F02121";


function getPlayerPlaceByPerformance(player: number, team: number[], enemies: number[]): [player: number, team: number, enemies: number] {
  const desc = (a: number, b: number): number => b - a;
  team.push(player);
  team.sort(desc);
  enemies.push(player);
  enemies.sort(desc);
  const positionInTeam = team.indexOf(player) + 1;
  const positionInEnemies = enemies.indexOf(player) + 1;
  return [player, positionInTeam, positionInEnemies];
}


function kdaRatio(kill: number, death: number, assist: number): number {
  const rawKda = (kill + assist) / death;
  return Math.round(rawKda * 100) / 100;
}