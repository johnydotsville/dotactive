export class MatchPlayer {
  steamAccountid
  steamAccounttimeCreated
  dotaAccountLevel
  isAnonymous
  seasonRank
  smurfFlag
  heroId
  heroDisplayName
  heroShortName
  isRadiant: boolean;
  isVictory: boolean;
  kills
  deaths
  assists
  goldPerMinute
  experiencePerMinute
  networth
  level
  heroDamage
  towerDamage
  position
  lane
  intentionalFeeding

  private constructor() { }

  public static create(obj) {
    const player = new MatchPlayer();
    player.steamAccountid = obj.steamAccount.id;
    player.steamAccounttimeCreated = obj.steamAccount.timeCreated;
    player.dotaAccountLevel = obj.steamAccount.dotaAccountLevel;
    player.isAnonymous = obj.steamAccount.isAnonymous;
    player.seasonRank = obj.steamAccount.seasonRank;
    player.smurfFlag = obj.steamAccount.smurfFlag;

    player.heroId = obj.hero.id;
    player.heroDisplayName = obj.hero.displayName;
    player.heroShortName = obj.hero.shortName;

    player.isRadiant = obj.isRadiant;
    player.isVictory = obj.isVictory;
    player.kills = obj.kills;
    player.deaths = obj.deaths;
    player.assists = obj.assists;
    player.goldPerMinute = obj.goldPerMinute;
    player.experiencePerMinute = obj.experiencePerMinute;
    player.networth = obj.networth;
    player.level = obj.level;
    player.heroDamage = obj.heroDamage;
    player.towerDamage = obj.towerDamage;
    player.position = obj.position;
    player.lane = obj.lane;
    player.intentionalFeeding = obj.intentionalFeeding;

    return player;
  }
}