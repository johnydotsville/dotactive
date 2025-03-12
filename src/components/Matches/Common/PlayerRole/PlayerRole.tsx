import { useState } from "react";

import * as styles from "./PlayerRole.module.css";
import { CarryIcon, MidIcon, HardlineIcon, SoftSupportIcon, HardSupportIcon } from "@components/Misc/PositionIcons";


type PlayerRoleProps = {
  heroname: string;
  position: string;
}


export const PlayerRole: React.FC<PlayerRoleProps> = ({ heroname, position }) => {
  const [heroIconLoadingError, setHeroIconLoadingError] = useState(false);

  const heroimg = heroIconLoadingError ? "stubportrait" : heroname;
  const heroimgPath = `/assets/img/heroes/${heroimg}.png`;  // TODO: Сделать пути до ассетов через глобальную переменную, чтобы не хардкодить
  let posImg;
  const defaultSize = "60%";
  switch (position) {
    case "POSITION_1":
      posImg = <CarryIcon size={defaultSize}/>;
      break;
    case "POSITION_2":
      posImg = <MidIcon size={defaultSize}/>;
      break;
    case "POSITION_3":
      posImg = <HardlineIcon size={defaultSize}/>;
      break;
    case "POSITION_4":
      posImg = <SoftSupportIcon size={defaultSize}/>;
      break;
    case "POSITION_5":
      posImg = <HardSupportIcon size={defaultSize}/>;
      break;
    default:
      const posimgPath = `/assets/img/misc/position_unknown.svg`;
      posImg = <img src={posimgPath} loading="lazy" alt={position} height={"70%"} />
  }

  const handleHeroIconLoadingError = () => setHeroIconLoadingError(true);

  return (
    <div className={styles.wrapper}>
      <img className={styles.hero} src={heroimgPath} onError={handleHeroIconLoadingError} loading="lazy" alt={heroname} />
      <div className={styles.position}>{ posImg }</div>
    </div>
  )
}