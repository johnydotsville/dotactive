import { stratzRequestConfig } from '@utils/stratz-request-config';
import axios, {isCancel, AxiosError} from 'axios';
// import axios, {isCancel, AxiosError} from 'axios';
import { Match } from './model/match';
import { MatchQueryBuilder} from './match-query-builder';
import { AxiosGraphqlQueryAdapter } from '@utils/axios-graphql-query-adapter';
import { IStorage } from '@domain/database/storage/IStorage';
import { MatchStorage } from '@domain/database/storage/MatchStorage';
import { MyDatabase } from '@domain/database/MyDatabase';
import { StorageName } from '@domain/database/config/storages/StorageName';

export class MatchService {
  private requestConfig;
  private matches: Match[];
  private storage: MatchStorage;

  public constructor(storage: MatchStorage) {
    this.requestConfig = stratzRequestConfig;
    this.storage = storage;
  }

  public async init(playerAccountId: number) {
    try {
      const fromDb = await this.storage.read();
      if (fromDb.length === 0) {
        const loaded = await this.loadMatchesForPlayer(playerAccountId);
        const saved = await this.storage.save(loaded);
        this.matches = saved.map(x => x.result);
        // this.matches = await this.saveMatches(loaded);
      } else {
        // this.matches = fromDb.map(x => x.result);
      }
    } catch (error) {
      console.log(error);
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

  // private async saveMatches(matches: Match[]): Promise<Match[]> {
  //   // return await this.database.saveMany(this.storage, matches);
  //   const result = await this.database.save(this.storage, matches);
  //   return result;
  // }

  public async getAllMatches() {
    const result = await this.storage.read();
    return result;
  }

  public async getMatch(id: number) {
    // const result = await this.database.read(this.storage, id);
    const result = await this.storage.read(id);
    return result;
  }

  public async getMatches(...ids: number[]) {
    const result = await this.storage.read(...ids);
    return result;
  }

  public async deleteMatches(...ids: number[]) {
    const result = await this.storage.delete(...ids);
    return result;
  }
}