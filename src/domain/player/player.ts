export class Player {
  firstMatchDate;
  matchCount;
  winCount;
  behaviorScore;
  isAnonymous;
  smurf;
  dotaAccountLevel;
  accountId;
  accountCreationDate;

  private constructor() {

  }

  public static create(obj): Player {
    const player = new Player();
    player.firstMatchDate = obj.firstMatchDate;
    player.matchCount = obj.matchCount;
    player.winCount = obj.winCount;
    player.behaviorScore = obj.behaviorScore;
    player.isAnonymous = obj.steamAccount.isAnonymous;
    player.smurf = obj.steamAccount.smurfFlag;
    player.dotaAccountLevel = obj.steamAccount.dotaAccountLevel;
    player.accountId = obj.steamAccount.id;
    player.accountCreationDate = obj.steamAccount.timeCreated;
    return player;
  }
}



/*
Полный набор доступных данных
{
  player(steamAccountId: 1191745794) {
    steamAccountId,
    steamAccount {
      id
      timeCreated
      dotaAccountLevel
      rankShift
      isAnonymous
      seasonRank
      smurfFlag
    },
    firstMatchDate
    matchCount
    winCount
    behaviorScore
    simpleSummary {
      lastUpdateDateTime
      matchCount
      coreCount
      supportCount
      imp
      activity
    }
    performance {
      imp
      rank
      kills
      killsAverage
      deaths
      deathsAverage
      assists
      assistsAverage
      cs
      csAverage
      gpm
      gpmAverage
      xpm
      xpmAverage
    }
  }
}


*/