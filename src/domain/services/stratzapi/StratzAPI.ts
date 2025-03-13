import { stratzRequestConfig } from '@utils/stratz-request-config';
import { MatchQueryBuilder } from './builders/MatchQueryBuilder';
import { AxiosGraphqlQueryAdapter } from '@utils/AxiosGraphqlQueryAdapter';
import axios, {isCancel, AxiosError} from 'axios';
import { Match } from '@domain/services/stratzapi/datamodel/Match';


// TODO: возможно надо будет сделать более специализированные классы, вроде MatchAPI
// и объединить их здесь.


export class StratzAPI {
  private requestConfig;

  public constructor() {
    this.requestConfig = stratzRequestConfig;
    this.setToken(window.localStorage.getItem("current_token"));
  }


  public setToken(token: string): void {
    this.requestConfig.headers = {
      ...this.requestConfig.headers,
      "Authorization": `Bearer ${token}`,
    }
  }


  public async getMatchesByPlayerId(playerAccountId: number, matchesCount?: number): Promise<Match[]> {
    let result: Match[] = [];
    const builder = new MatchQueryBuilder();
    const maxMatchesPerRequest = 100;
    const matchesToFetch = matchesCount ?? 1000;

    const cycles = Math.ceil(matchesToFetch / maxMatchesPerRequest);

    builder.account(playerAccountId).take(100);

    for (let i = 0; i < cycles; i++) {
      builder.skip(i * maxMatchesPerRequest);
      const matchQuery = AxiosGraphqlQueryAdapter.toAxiosQuery(builder.build(), "getMatchInfo");

      this.requestConfig.data = matchQuery;
      const response = await axios.request(this.requestConfig);

      const pack = response.data.data.player.matches.map(m => Match.create(m));
      result = result.concat(pack);
    }

    return result;
  }
}