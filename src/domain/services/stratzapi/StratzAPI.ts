import { stratzRequestConfig } from '@utils/stratz-request-config';
import { MatchQueryBuilder } from './querymodel/MatchQueryBuilder';
import { AxiosGraphqlQueryAdapter } from '@utils/axios-graphql-query-adapter';
import axios, {isCancel, AxiosError} from 'axios';
import { Match } from './datamodel/match';


export class StratzAPI {
  private requestConfig;

  public constructor() {
    this.requestConfig = stratzRequestConfig;
  }

  public async getMatchesByPlayerId(playerAccountId: number) {
    const builder = new MatchQueryBuilder();
    builder.account(playerAccountId).take(50);
    const matchQuery = AxiosGraphqlQueryAdapter.toAxiosQuery(builder.build(), "getMatchInfo");

    this.requestConfig.data = matchQuery;
    const response = await axios.request(this.requestConfig);

    return response.data.data.player.matches.map(m => Match.create(m));
  }
}