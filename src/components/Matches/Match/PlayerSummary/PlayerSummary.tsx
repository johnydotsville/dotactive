import * as styles from "./PlayerSummary.module.css";
import Hero from "@components/Matches/Match/Hero/Hero";


export default function PlayerSummary({summary}) {  // TODO: типизировать
  const {position, heroname, stats} = summary;

  return (
    <div className={styles.playerStatus}>
      {/* <img src={`/assets/img/pos_icons/${position ?? "unknown"}.svg`} width={35} height={35} /> */}
      <Hero heroname={heroname} position={position} />
      {getInfo(stats)}
    </div>
  )
}

function getPortrait(heroname) {
  const heroimg = `/assets/img/heroes/${heroname}.png`;  // TODO: переделать как-то, чтобы все компоненты получали путь до картинок единым образом
  // const winlose = summary.win ? styles.win : styles.lose;
  // return <img className={`${winlose} ${styles.portrait}`} src={heroimg} />
  return <img className={styles.portrait} src={heroimg} />
}

function getInfo(stats) {
  const arr = Object.entries(stats).map(([k, v]) => `${k}: ${v}`);
  // arr.forEach(x => console.log(x));
  return (
    <div className={styles.brief}>
      { arr.map(x => <div>{x}</div>) }
    </div>
  );
}

