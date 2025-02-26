import { DataStructureBuilder } from "../DataStructureBuilder";


export class MatchRequestDataStructureBuilder extends DataStructureBuilder {
  public build(): string {
    return this.mergeShards();
  }


  public id(): MatchRequestDataStructureBuilder {
    super.setShard("id");
    return this;
  }


  public startDateTime(): MatchRequestDataStructureBuilder {
    super.setShard("startDateTime");
    return this;
  }


  public durationSeconds(): MatchRequestDataStructureBuilder {
    super.setShard("durationSeconds");
    return this;
  }


  public lobbyType(): MatchRequestDataStructureBuilder {
    super.setShard("lobbyType");
    return this;
  }


  public didRadiantWin(): MatchRequestDataStructureBuilder {
    super.setShard("didRadiantWin");
    return this;
  }


  public radiantKills(): MatchRequestDataStructureBuilder {
    super.setShard("radiantKills");
    return this;
  }


  public direKills(): MatchRequestDataStructureBuilder {
    super.setShard("direKills");
    return this;
  }


  public gameMode(): MatchRequestDataStructureBuilder {
    super.setShard("gameMode");
    return this;
  }


  public bracket(): MatchRequestDataStructureBuilder {
    super.setShard("bracket");
    return this;
  }
}



/*
id
startDateTime
durationSeconds
lobbyType
didRadiantWin
radiantKills
direKills
gameMode
bracket
*/