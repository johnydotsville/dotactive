import { stratzRequestConfig } from '@utils/stratz-request-config';
import axios, {isCancel, AxiosError} from 'axios';
import { Match } from './model/match';

export class MatchService {
  private database;
  private requestConfig;
  private matches: Match[];
  private storage: string = "matches";

  public constructor(database) {
    this.database = database;
    this.requestConfig = stratzRequestConfig;
  }

  public async init(playerAccountId: number) {
    const fromDb = await this.database.read(this.storage);
    if (!fromDb) {
      const loaded = await this.loadMatchesForPlayer(playerAccountId);
      this.matches = await this.saveMatches(loaded);
    } else {
      this.matches = fromDb;
    }
  }

  private async loadMatchesForPlayer(playerAccountId: number) {
    const query = this.getMatchInfoQuery(playerAccountId);
    this.requestConfig.data = query;
    const response = await axios.request(this.requestConfig);

    return response.data.data.player.matches.map(m => Match.create(m));
  }

  private async saveMatches(matches: Match[]): Promise<Match[]> {
    return await this.database.saveMany(this.storage, matches);
  }

  public getAllMatches(): Match[] {
    return this.matches;
  }

  private getMatchInfoQuery(playerAccountId: number) {
    // TODO: фильтры по типу лобби и т.д. можно добавить, сколько выбрать матчей и т.д.
    return {
      operationName: "getMatchInfo",
      query: `query getMatchInfo
        {
          player(steamAccountId: ${playerAccountId}) {
            steamAccountId,
            matches(request: {
              take: 20
            }) {
              id
              startDateTime
              durationSeconds
              lobbyType
              didRadiantWin
              gameMode
              bracket
              players {
                steamAccount {
                  id
                  timeCreated
                  dotaAccountLevel
                  isAnonymous
                  seasonRank
                  smurfFlag
                }
                hero {
                  id
                  displayName
                  shortName
                }
                isRadiant
                isVictory
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
              }
            }
          }
        }`,
      variables: {}
    }
  }

}

/*
{
  player(steamAccountId: 1191745794) {
    steamAccountId,
    matches(request: {
    	matchIds: []
      lobbyTypeIds: [7]
      skip: 1
    }) {
      id
    }
  }
}

*/