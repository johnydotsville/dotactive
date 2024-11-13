import * as styles from "./Match.module.css";
import MatchBasicInfo from "./MatchBasicInfo/MatchBasicInfo";
import PlayerSummary from "./PlayerSummary/PlayerSummary";
import TeamInfo, { PlayerStats } from "./TeamInfo/TeamInfo";
import { TeamStats } from "./TeamInfo/TeamInfo";

export default function Match({match}) {
  const matchBasicInfo = {
    matchId: match.id,
    lobbyType: match.lobbyType,
    whenPlayed: match.startDateTime,
    duration: match.durationSeconds,
  };

  const playerAccountId = 56831765;  // TODO: переделать, чтобы бралось из редакса или типа того

  const player = match.matchPlayers.find(p => p.steamAccountid === playerAccountId);
  const kda = ((player.kills + player.assists) / player.deaths).toFixed(1);
  const skda = `${player.kills}/${player.deaths}/${player.assists} (${kda})`;
  const playerSummary = {
    position: player.position,
    heroname: player.heroShortName,
    stats: {
      kda: skda,
      gpm: player.goldPerMinute,
      xpm: player.experiencePerMinute,
      net: player.networth,
      hdmg: player.heroDamage,
      tdmg: player.towerDamage,
      lvl: player.level,
    }
  };

  // TODO: сделать типы для матча
  const playerTeam = match.matchPlayers.filter(p => p.isRadiant === player.isRadiant);
  const enemyTeam = match.matchPlayers.filter(p => p.isRadiant !== player.isRadiant);

  // TODO: счет считать не по килам союзников, а по смертям соперников
  const playerTeamInfo: TeamStats = {
    score: playerTeam.reduce((acc, p) => acc + p.kills, 0),
    win: player.isVictory,
    players: playerTeam.sort(sortPlayersByRole).map(getPlayerStats)
  };
  const enemyTeamInfo: TeamStats = {
    score: enemyTeam.reduce((acc, p) => acc + p.kills, 0),
    win: !player.isVictory,
    players: enemyTeam.sort(sortPlayersByRole).map(getPlayerStats)
  };

  return (
    <div className={styles.matchBox}>
      <MatchBasicInfo summary={matchBasicInfo} />
      <div className={styles.matchBody}>
        <PlayerSummary summary={playerSummary} />
        <div className={styles.teamInfoBox}>
          <TeamInfo summary={playerTeamInfo} />
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