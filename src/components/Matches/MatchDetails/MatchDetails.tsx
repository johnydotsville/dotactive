import { useParams } from "react-router-dom"
import { useLocation } from "react-router-dom";

import * as styles from "./MatchDetails.module.css"
import { CarryIcon, MidIcon } from "@components/Misc/PositionIcons";


export const MatchDetails = () => {
  const params = useParams();
  const match = useLocation().state;
  let result;

  if (match) {
    result = `Матч ${match.id} ${match.startDateTime} был ну вообще отпад...`;
  } else {
    result = "Надо из БД грузить. Напрямую страницу открыли."
  }

  return (
    <div className={styles.wrapper}>
      {result}
    </div>
  )
}