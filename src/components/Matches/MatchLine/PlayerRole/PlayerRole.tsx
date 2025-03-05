import { useState } from "react";


import * as styles from "./PlayerRole.module.css";


type PlayerRoleProps = {
  heroname: string;
  position: string;
}


export const PlayerRole: React.FC<PlayerRoleProps> = ({ heroname, position }) => {
  const [heroIconLoadingError, setHeroIconLoadingError] = useState(false);

  const heroimg = heroIconLoadingError ? "stubportrait" : heroname;
  const heroimgPath = `/assets/img/heroes/${heroimg}.png`;
  const posimgPath = `/assets/img/pos_icons/${position ?? "unknown"}.svg`;

  const handleHeroIconLoadingError = () => setHeroIconLoadingError(true);

  return (
    <div className={styles.wrapper}>
      <img className={styles.hero} src={heroimgPath} onError={handleHeroIconLoadingError} loading="lazy" alt={heroname} />
      <img className={styles.position} src={posimgPath} loading="lazy" alt={position} />
    </div>
  )
}