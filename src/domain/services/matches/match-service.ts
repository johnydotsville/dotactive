import { stratzRequestConfig } from '@utils/stratz-request-config';
import axios, {isCancel, AxiosError} from '../../../../node_modules/axios';
// import axios, {isCancel, AxiosError} from 'axios';
import { Match } from './model/match';
import { MatchQueryBuilder} from './match-query-builder';
import { AxiosGraphqlQueryAdapter } from '@utils/axios-graphql-query-adapter';

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
    // if (!fromDb) {  // Возвращался пустой массив в случае отсутствия данных. А раньше будто undefined было. Разобраться.
    if (fromDb.length === 0) {
      const loaded = await this.loadMatchesForPlayer(playerAccountId);
      this.matches = await this.saveMatches(loaded);
    } else {
      this.matches = fromDb;
    }
  }

  private async loadMatchesForPlayer(playerAccountId: number) {
    const builder = new MatchQueryBuilder();
    builder.account(playerAccountId).take(50);
    const matchQuery = AxiosGraphqlQueryAdapter.toAxiosQuery(builder.build(), "getMatchInfo");

    this.requestConfig.data = matchQuery;
    const response = await axios.request(this.requestConfig);

    return response.data.data.player.matches.map(m => Match.create(m));
  }

  private async saveMatches(matches: Match[]): Promise<Match[]> {
    // return await this.database.saveMany(this.storage, matches);
    const result = await this.database.save(this.storage, matches);
    return result;
  }

  public getAllMatches(): Match[] {
    return this.matches;
  }

  public async getMatch(id) {
    const result = await this.database.read(this.storage, id);
    return result;
  }
}