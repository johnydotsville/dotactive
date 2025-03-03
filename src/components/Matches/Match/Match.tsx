import * as styles from "./Match.module.css";
import MatchBasicInfo from "./MatchBasicInfo/MatchBasicInfo";
import PlayerSummary from "./PlayerSummary/PlayerSummary";
import TeamInfo, { PlayerStats } from "./TeamInfo/TeamInfo";
import { TeamStats } from "./TeamInfo/TeamInfo";
import { Match as MatchModel } from "@domain/services/stratzapi/datamodel/Match";
import { MatchPlayer } from "@domain/services/stratzapi/datamodel/MatchPlayer";

type Props = {
  match: MatchModel
}

export const Match: React.FC<Props> = ({ match }) => {
  const matchBasicInfo = {
    matchId: match.id,
    lobbyType: match.lobbyType,
    whenPlayed: match.startDateTime,
    duration: match.durationSeconds,
  };

  const myAccountId = 56831765;  // TODO: переделать, чтобы бралось из редакса или типа того

  const me = match.matchPlayers.find(p => p.steamAccountid === myAccountId);
  const kda = ((me.kills + me.assists) / me.deaths).toFixed(1);
  const skda = `${me.kills}/${me.deaths}/${me.assists} (${kda})`;
  const mySummary = {
    position: me.position,
    heroname: me.heroShortName,
    stats: {
      kda: skda,
      gpm: me.goldPerMinute,
      xpm: me.experiencePerMinute,
      net: me.networth,
      hdmg: me.heroDamage,
      tdmg: me.towerDamage,
      lvl: me.level,
    }
  };

  // TODO: сделать типы для матча
  const myTeam = match.matchPlayers.filter(p => p.isRadiant === me.isRadiant);
  const enemyTeam = match.matchPlayers.filter(p => p.isRadiant !== me.isRadiant);

  // TODO: счет считать не по килам союзников, а по смертям соперников
  const myTeamInfo: TeamStats = {
    score: myTeam.reduce((acc, p) => acc + p.kills, 0),
    win: me.isVictory,
    players: myTeam.sort(sortPlayersByRole).map(getPlayerStats)
  };
  const enemyTeamInfo: TeamStats = {
    score: enemyTeam.reduce((acc, p) => acc + p.kills, 0),
    win: !me.isVictory,
    players: enemyTeam.sort(sortPlayersByRole).map(getPlayerStats)
  };

  return (
    <div className={styles.matchBox} key={matchBasicInfo.matchId}>
      <MatchBasicInfo summary={matchBasicInfo} />
      <div className={styles.matchBody}>
        <PlayerSummary summary={mySummary} />
        <div className={styles.teamInfoBox}>
          <TeamInfo summary={myTeamInfo} />
          <TeamInfo summary={enemyTeamInfo} />
        </div>
      </div>
    </div>
  )
}


function sortPlayersByRole(x, y) {
  if (x.position !== null && y.position !== null)
    return x.position.localeCompare(y.position);
  else 
    return 0;
}


function getPlayerStats(player): PlayerStats {
  return { 
    heroname: player.heroShortName,
    position: player.position,
    kills: player.kills,
    deaths: player.deaths,
    assists: player.assists,
    networth: player.networth
  };
}