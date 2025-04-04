import { Box } from "@mui/material";

import { useMemo } from "react";
import classNames from "classnames";


import * as styles from "./PlayerSummary.module.css"
import { MatchPlayer } from "@domain/services/stratzapi/datamodel/MatchPlayer"
import { PlayerRole } from "@components/Matches/Common/PlayerRole/PlayerRole";
import { getPlayerPlaceByPerformance } from "@domain/services/analyze/utils";
import { kdaRatio } from "@domain/services/analyze/utils";
import { icons } from "@utils/Ways";
// import { PlayerStat } from "@components/Matches/MatchLine/PlayerStat/PlayerMetric";


type PlayerSummaryProps = {
  player: MatchPlayer,
  mates: MatchPlayer[],
  enemies: MatchPlayer[],
  isUser: boolean  // Это игрок, который сейчас пользуется программой
}


export const PlayerSummary: React.FC<PlayerSummaryProps> = ({ player, mates, enemies, isUser }) => {
  const info = useMemo(() => {        
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

  const wrapper = classNames([
    styles.wrapper,
    isUser ? styles.userWrapper : styles.notUserWrapper
  ]);

  return (
    <div className={wrapper}>
      <div className={styles.playerRoleWrapper}>
        <PlayerRole heroname={player.heroShortName} position={player.position} />
      </div>
      <div className={styles.playerStatWrapper}>
        {/* <PlayerStat pic={icons.stub} stat={info.kda} altValue={info.kdaString} /> */}
      </div>
      <div className={styles.playerStatWrapper}>
        {/* <PlayerStat pic={icons.gpm} stat={info.gpm} /> */}
      </div>
      <div className={styles.playerStatWrapper}>
        {/* <PlayerStat pic={icons.xpm} stat={info.xpm} /> */}
      </div>
      <div className={styles.playerStatWrapper}>
        {/* <PlayerStat pic={icons.heroDmg} stat={info.heroDmg} /> */}
      </div>
      <div className={styles.playerStatWrapper}>
        {/* <PlayerStat pic={icons.towerDmg} stat={info.towerDmg} /> */}
      </div>
    </div>
  )
}