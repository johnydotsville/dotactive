import * as styles from "./LobbyType.module.css";


type LobbyTypeProps = {
  lobbyType: string;
}


export const LobbyType: React.FC<LobbyTypeProps> = ({ lobbyType }) => {
  const lobby = lobbyType.slice(0, 2).toUpperCase();
  
  return <div>{lobby}</div>
}