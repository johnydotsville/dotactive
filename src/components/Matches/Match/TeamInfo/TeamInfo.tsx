import * as styles from "./TeamInfo.module.css";

// TODO:
/*
  Сделать расстояние между героями и если у них известна роль, то отобразить значок этой ролик рядом с портретом героя.
  Или может в углу картинки героя. Роли можно взять картинками меч, щит, лук, как в самой игре.
*/

export default function TeamInfo({ summary } : { summary: TeamStats }) {
  return (
    <div className={styles.teamInfoBody}>
      <Score score={summary.score} win={summary.win} />
      <HeroLine players={summary.players} />
    </div>
  )
}

function Score({score, win}) {
  const scoreStyle = `${styles.score} ${win ? styles.scoreWin : styles.scoreLose}`;

  return (
    <div className={scoreStyle}>{score}</div>
  )
}

function HeroLine({players}) {
  return players.map(p => 
    <div className={styles.heroLine}>
      <img src={`/assets/img/pos_icons/${p.position ?? "unknown"}.svg`} width={35} height={35} />
      <img className={styles.heropic} src={`/assets/img/heroes/${p.heroname}.png`} />
      <div>{p.kills}/{p.deaths}/{p.assists}</div>
    </div>
  );
}

export type TeamStats = {
  score: number,
  win: boolean,
  players: PlayerStats[]
}

export type PlayerStats = {
  heroname: string,
  position: string,
  kills: number,
  deaths: number,
  assists: number,
  networth: number
}