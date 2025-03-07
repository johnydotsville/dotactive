import * as styles from "./Welcome.module.css";

import { Link } from "react-router-dom";


export const Welcome = () => {
  return (
    <div className={styles.wrapper}>
      Добро пожаловать в dotactive!
      <Link to="/matches">Перейти в историю матчей</Link>
    </div>
  )
}