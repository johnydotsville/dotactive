import * as styles from "./PlayerStat.module.css";


type PlayerStatProps = {
  pic: string;
  stat: [number, number, number]
  altValue?: string;
}

export const PlayerStat: React.FC<PlayerStatProps> = ({ pic, stat, altValue }) => {
  const valuePretty = stat[0].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
  const result: string = altValue ? 
    `${altValue} [${stat[1]}] [${stat[2]}]` :
    `${valuePretty} [${stat[1]}] [${stat[2]}]`;

  return (
    <div className={styles.playerStat}>
      <img className={styles.statPic} src={pic} />
      {result}
    </div>
  )
}