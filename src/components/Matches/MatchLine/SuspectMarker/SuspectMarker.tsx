import * as styles from "./SuspectMarker.module.css";


type SuspectMarkerProps = {
  suspect: boolean;
}


export const SuspectMarker: React.FC<SuspectMarkerProps> = ({ suspect }) => {
  const suspimg = `/assets/img/misc/susp_match.png`;

  return (
    <div className={styles.wrapper}>
      {suspect && <img className={styles.suspectPic} src={suspimg} />}
    </div>
  )
}