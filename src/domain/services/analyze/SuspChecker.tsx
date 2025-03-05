import { Match } from "../stratzapi/datamodel/Match";


export class SuspChecker {
  // TODO: Потом продумать, как можно задать критерии подозрительности, чтобы не хардкодить их тут
  public static checkMatchForSuspicious(match: Match): number {
    let suspPoints = 0;
    const durationThresholdInSeconds = 1800;  // < 30 минут обычно однокалиточные

    if (match.durationSeconds < durationThresholdInSeconds) {
      suspPoints += 1;
    }

    

    return suspPoints;
  }

}