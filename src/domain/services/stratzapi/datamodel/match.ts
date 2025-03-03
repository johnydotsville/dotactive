import { MatchPlayer } from "@domain/services/stratzapi/datamodel/MatchPlayer";

export class Match {
  id: number;
  radiantScore: number;
  direScore: number;
  startDateTime: number;
  durationSeconds: number;
  lobbyType: string;
  didRadiantWin: boolean;
  radiantKills: number;
  direKills: number;
  gameMode
  bracket
  matchPlayers: MatchPlayer[];

  private constructor() { }

  public static create(obj) {
    const match = new Match();
    match.id = obj.id;
    match.startDateTime = obj.startDateTime;
    match.durationSeconds = obj.durationSeconds;
    match.lobbyType = obj.lobbyType;
    match.didRadiantWin = obj.didRadiantWin;
    match.gameMode = obj.gameMode;
    match.bracket = obj.bracket;
    match.matchPlayers = obj.players.map(p => MatchPlayer.create(p));

    match.radiantScore = match.matchPlayers
      .filter(p => p.isRadiant)
      .reduce((score, p) => score + p.kills, 0);
    match.direScore = match.matchPlayers
      .filter(p => !p.isRadiant)
      .reduce((score, p) => score + p.kills, 0);

    return match;
  }
}