import { stratzRequestConfig } from '@utils/stratz-request-config';
import { MatchQueryBuilder } from './querymodel/MatchQueryBuilder';
import { AxiosGraphqlQueryAdapter } from '@utils/AxiosGraphqlQueryAdapter';
import axios, {isCancel, AxiosError} from 'axios';
import { Match } from '@domain/services/stratzapi/datamodel/Match';


// TODO: возможно надо будет сделать более специализированные классы, вроде MatchAPI
// и объединить их здесь.


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