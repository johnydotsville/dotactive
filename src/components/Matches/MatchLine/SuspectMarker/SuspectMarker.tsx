import * as styles from "./SuspectMarker.module.css";


type SuspectMarkerProps = {
  suspPoints: number;
}


// TODO: Здесь картинку можно сделать SVG и менять ей цвет программно в зависимости
// от количества очков подозрительности, чтобы не плодить кучу png.
export const SuspectMarker: React.FC<SuspectMarkerProps> = ({ suspPoints }) => {
  const suspimg = `/assets/img/misc/susp_match.png`;
  let isSusp = false;

  if (suspPoints > 0) {
    isSusp = true;
  }

  return (
    <div className={styles.wrapper}>
      {isSusp && <img className={styles.suspectPic} src={suspimg} />}
    </div>
  )
}