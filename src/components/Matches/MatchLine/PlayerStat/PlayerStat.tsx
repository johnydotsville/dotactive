import * as styles from "./PlayerStat.module.css";


type PlayerStatProps = {
  pic: string;
  stat: [number, number, number]
  alt?: string;
}

export const PlayerStat: React.FC<PlayerStatProps> = ({ pic, stat, alt }) => {
  const valuePretty = stat[0].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  const result: string = alt ? 
    `${alt} [${stat[1]}] [${stat[2]}]` :
    `${valuePretty} [${stat[1]}] [${stat[2]}]`;
  return (
    <div className={styles.playerStat}>
      <img src={pic} style={{width: "30px"}}/>
      {result}
    </div>
  )
}