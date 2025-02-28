import { Match } from '@domain/services/stratzapi/datamodel/Match';
import { MatchStorage } from '@domain/database/storage/MatchStorage';
import { StratzAPI } from '@domain/services/stratzapi/StratzAPI';


export class MatchService {
  private matches: Match[];
  private storage: MatchStorage;
  private api: StratzAPI

  public constructor(storage: MatchStorage, api: StratzAPI) {
    this.storage = storage;
    this.api = api;
  }

  public async init(playerAccountId: number) {
    try {
      const fromDb = (await this.storage.read()).result;
      if (fromDb.length === 0) {
        console.log("В БД матчей нет, загружаю их с сервера...");
        const loaded = await this.api.getMatchesByPlayerId(playerAccountId, 1000);
        const saved = await this.storage.save(loaded);
        this.matches = saved.result;
      } else {
        this.matches = fromDb;
      }
    } catch (error) {
      console.log(error);
    }
  }


  public async getAllMatches() {
    const result = await this.storage.read();
    return result;
  }


  public async getMatch(id: number) {
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