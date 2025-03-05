import classNames from "classnames";


import * as styles from "./LobbyType.module.css";


type LobbyTypeProps = {
  lobbyType: string;
}


export const LobbyType: React.FC<LobbyTypeProps> = ({ lobbyType }) => {
  const lobby = lobbyType.slice(0, 2).toUpperCase();
  const classes = classNames(
    styles.base, 
    { 
      [styles.ranked]: lobbyType === "RANKED" ,
      [styles.unranked]: lobbyType === "UNRANKED",
      [styles.turbo]: lobbyType === "TURBO" 
    }
  );

  return <div className={classes}>{lobby}</div>
}