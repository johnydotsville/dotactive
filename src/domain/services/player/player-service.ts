import { stratzRequestConfig } from '@utils/stratz-request-config';
import axios, {isCancel, AxiosError} from 'axios';
import { Player } from "@domain/player/player";

/*
  TODO: Планируется таблица под пользователей программы. Т.е. хотим например посмотреть свои матчи, то при входе
  указываем свой id, и инфа добавляется в эту таблицу. Потом хотим для другого игрока матчи посмотреть, опять же
  при входе (ну или не при входе, а в общем где-то в интерфейсе) вводим другой id и для него загружаются матчи.
  Т.е. получается таблица, грубо говоря, не под всех игроков, которые в матчах участвуют, а под тех, за чьей
  статистикой смотрим. Грубо говоря, это получается даже не игроки, а скорее "пользователи" программы. С другой
  стороны, этот сервис может использоваться и для загрузки инфы о любом игроке. Просто не каждый такой игрок
  будет сохранен в БД. Например, для детального анализа матча понадобится загружать инфу о каждом игроке, но 
  это не значит, что он будет сохранен в эту таблицу. Скорее всего эта инфа в этом случае будет сохранена в другую
  таблицу или вообще не сохранена.
*/

export class PlayerService {
  protected database;
  protected storage: string = "players";
  protected requestConfig: any;

  public constructor(database) {
    this.database = database;
    this.requestConfig = stratzRequestConfig;
  }

  public async loadPlayerInfo(accountId: number): Promise<Player> {
    const query = {
      operationName: "getPlayerInfo",
      query: `query getPlayerInfo
        {
          player(steamAccountId: ${accountId}) {
            steamAccountId,
            steamAccount {
              id
              timeCreated
              dotaAccountLevel
              isAnonymous
              smurfFlag
            },
            firstMatchDate
            matchCount
            winCount
            behaviorScore
          }
        }`,
      variables: {}
    };
    this.requestConfig.data = query;
    const response = await axios.request(this.requestConfig);

    return Player.create(response.data.data.player);
  }
}