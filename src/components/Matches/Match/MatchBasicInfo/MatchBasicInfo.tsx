import * as styles from "./MatchBasicInfo.module.css";

// TODO: как указать тип для пропсов?
export default function MatchSummary({summary}) {
  return (
    <div className={styles.ololo}>{summary.lobbyType}, {summary.whenPlayed}, {summary.duration}, {summary.matchId}</div>
  )
}

export type SummaryProps = {
  lobbyType: string,
  whenPlayed: number,
  duration: number
}