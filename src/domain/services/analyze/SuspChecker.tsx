import { Match } from "../stratzapi/datamodel/Match";
import { MatchPlayer } from "../stratzapi/datamodel/MatchPlayer";
import { kdaRatio } from "./utils";


export class SuspChecker {
  // TODO: Потом продумать, как можно задать критерии подозрительности, чтобы не хардкодить их тут
  public static checkMatchForSuspicious(match: Match): number {
    let suspPoints = 0;

    suspPoints += this.durationFactor(match.durationSeconds, 1800);  // < 30 минут обычно однокалиточные
    suspPoints += this.badKdaFactor(match.matchPlayers, 1);

    return suspPoints;
  }


  private static durationFactor(matchDurationInSeconds: number, durationThresholdInSeconds: number): number {
    if (matchDurationInSeconds < durationThresholdInSeconds) {
      return 1;
    }

    return 0;
  }


  private static badKdaFactor(players: MatchPlayer[], kdaThreshold: number): number {
    const radiant = players.filter(p => p.isRadiant);
    const dire = players.filter(p => !p.isRadiant);

    const radiantBadKdaCount = badKdaCount(radiant);
    const direBadKdaCount = badKdaCount(dire);

    if (badKdaOnlyInSingleTeam(radiantBadKdaCount, direBadKdaCount)) {
      return 2;
    }
    if (radiantBadKdaCount - direBadKdaCount === 0) {  // Фидаков поровну в обеих командах
      return 0;
    } else {
      return 1;
    }

    function badKdaCount(team: MatchPlayer[]): number {
      return team
        .map(p => kdaRatio(p.kills, p.deaths, p.assists))
        .filter(k => k < kdaThreshold)
        .length;
    }

    function badKdaOnlyInSingleTeam(t1: number, t2: number): boolean {
      return (t1 === 0 && t2 > 0) || (t2 === 0 && t1 > 0);
    }
  }
}