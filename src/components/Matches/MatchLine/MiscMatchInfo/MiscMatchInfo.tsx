import * as styles from "./MiscMatchInfo.module.css";

import { DateUtils } from "@utils/DateUtils";


type MiscMatchInfoProps = {
  matchId: number;
  startDateTimeUnix: number;
}


export const MiscMatchInfo: React.FC<MiscMatchInfoProps> = ({ matchId, startDateTimeUnix }) => {
  return <div className={styles.wrapper}>
    <div>{DateUtils.formatUnixToDate(startDateTimeUnix)}</div>
    <div>{matchId}</div>
  </div>
}