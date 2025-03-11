import * as styles from "./PlayerStat.module.css";


type PlayerStatProps = {
  pic: string;
  stat: [number, number, number]
  altValue?: string;
}

/**
 * 
 * @param
 * pic - путь до картинки иконки.
 * @param
 * stat - кортеж, где первое значение - это непосредственно показатель игрока (например 500 gpm), 
 * второе значение - место игрока среди своей команды по этому показателю (например 1),
 * третье значение - место игрока среди вражеской команды (например 3)
 * @param
 * altValue - используется, когда надо вместо показателя игрока отобразить что-то другое.
 * Например, вместо коэффициента kda (например 1.7) отобразить строку с непосредственными
 * значениями kda (например, 10 / 7 / 21)
 * @returns 
 */
export const PlayerStat: React.FC<PlayerStatProps> = ({ pic, stat, altValue }) => {
  const valuePretty = stat[0].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");  // 12000 -> 12.000
  const result: string = altValue ? 
    `${altValue} [${stat[1]}] [${stat[2]}]` :
    `${valuePretty} [${stat[1]}] [${stat[2]}]`;

  return (
    <div className={styles.wrapper}>
      <img className={styles.statPic} src={pic} />
      {result}
    </div>
  )
}