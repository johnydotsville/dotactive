import { useMemo } from "react";


import * as styles from "./PlayerSummary.module.css"
import { MatchPlayer } from "@domain/services/stratzapi/datamodel/MatchPlayer"
import { PlayerRole } from "@components/Matches/MatchLine/PlayerRole/PlayerRole";
import { getPlayerPlaceByPerformance } from "@domain/services/analyze/utils";
import { kdaRatio } from "@domain/services/analyze/utils";
import { icons } from "@utils/Ways";
import { PlayerStat } from "@components/Matches/MatchLine/PlayerStat/PlayerStat";


type PlayerSummaryProps = {
  player: MatchPlayer,
  mates: MatchPlayer[],
  enemies: MatchPlayer[]
}


export const PlayerSummary: React.FC<PlayerSummaryProps> = ({ player, mates, enemies }) => {
  const info = useMemo(() => {
        const playerAccountId = 56831765;  // TODO: переделать, чтобы бралось из редакса или типа того
        
        mates = mates.filter(p => p.steamAccountid !== player.steamAccountid);

        const kdaString = `${player.kills}/${player.deaths}/${player.assists}`;
        const kda = getPlayerPlaceByPerformance(kdaRatio(player.kills, player.deaths, player.assists),
          mates.map(p => kdaRatio(p.kills, p.deaths, p.assists)),
          enemies.map(p => kdaRatio(p.kills, p.deaths, p.assists))
        );
    
        const gpm = getPlayerPlaceByPerformance(player.goldPerMinute, mates.map(t => t.goldPerMinute), enemies.map(e => e.goldPerMinute));
        const xpm = getPlayerPlaceByPerformance(player.experiencePerMinute, mates.map(t => t.experiencePerMinute), enemies.map(e => e.experiencePerMinute));
        const heroDmg = getPlayerPlaceByPerformance(player.heroDamage, mates.map(t => t.heroDamage), enemies.map(e => e.heroDamage));
        const towerDmg = getPlayerPlaceByPerformance(player.towerDamage, mates.map(t => t.towerDamage), enemies.map(e => e.towerDamage));
    
        return {
          player,
          kdaString,
          kda,
          gpm,
          xpm,
          heroDmg,
          towerDmg,
        }
      }, []
    );

  return (
    <div className={styles.wrapper}>
      <div className={styles.playerRoleWrapper}>
        <PlayerRole heroname={player.heroShortName} position={player.position} />
      </div>
      <div className={styles.playerStatWrapper}>
        <PlayerStat pic={icons.stub} stat={info.kda} altValue={info.kdaString} />
      </div>
      <div className={styles.playerStatWrapper}>
        <PlayerStat pic={icons.gpm} stat={info.gpm} />
      </div>
      <div className={styles.playerStatWrapper}>
        <PlayerStat pic={icons.xpm} stat={info.xpm} />
      </div>
      <div className={styles.playerStatWrapper}>
        <PlayerStat pic={icons.heroDmg} stat={info.heroDmg} />
      </div>
      <div className={styles.playerStatWrapper}>
        <PlayerStat pic={icons.towerDmg} stat={info.towerDmg} />
      </div>
    </div>
  )
}