import { Link } from "react-router-dom";


import * as styles from "./Welcome.module.css";
import { FirstVisit } from "./FirstVisit/FirstVisit";



export const Welcome = () => {
  let component = <FirstVisit />;
  if (localStorage.getItem("current_token") && localStorage.getItem("current_user")) {
    // Тогда не first visit, а выбор юзера
    component = <div>Налетай-торопись, выбирай юзер-пись!</div>
  }

  return (
    <div className={styles.wrapper}>
      { component }
    </div>
  )
}
