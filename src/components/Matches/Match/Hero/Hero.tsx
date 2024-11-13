import * as styles from "./Hero.module.css";

export default function Hero({heroname, position}) {
  const heroimg = `/assets/img/heroes/${heroname}.png`;
  const posimg = `/assets/img/pos_icons/${position ?? "unknown"}.svg`;

  return (
    <div className={styles.heroBox}>
      <img className={styles.portraitBox} src={heroimg} />
      <img className={styles.positionBox} src={posimg} />
    </div>
  );
}