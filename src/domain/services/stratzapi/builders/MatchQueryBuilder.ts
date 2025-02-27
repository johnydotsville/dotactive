import { ParamsBag } from "./utils/ParamsBag";
import { ParamType as Param } from "./utils/ParamsBag";

/**
 * Построитель запроса выборки матчей игрока. Содержит методы установки
 * параметров для шаблона запроса и метод генерации строки запроса.
 */
export class MatchQueryBuilder {
  private query: string;
  private bag: ParamsBag;


  constructor() {
    this.query = queryTemplate;
    this.bag = new ParamsBag();
  }


  public account(account: number): MatchQueryBuilder {
    this.bag.put(new Param("steamAccountId", account, ParamGroup.PlayerAccountId));
    return this;
  }


  public take(matchesCount: number): MatchQueryBuilder {
    this.bag.put(new Param("take", matchesCount, ParamGroup.MatchFilter));
    return this;
  }


  public skip(matchesCount: number): MatchQueryBuilder {
    this.bag.put(new Param("skip", matchesCount, ParamGroup.MatchFilter));
    return this;
  }


  public before(matchId: number): MatchQueryBuilder {
    this.bag.put(new Param("before", matchId, ParamGroup.MatchFilter));
    return this;
  }


  public after(matchId: number): MatchQueryBuilder {
    this.bag.put(new Param("after", matchId, ParamGroup.MatchFilter));
    return this;
  }


  public startDateTime(dateTimeUnix: number): MatchQueryBuilder {
    this.bag.put(new Param("startDateTime", dateTimeUnix, ParamGroup.MatchFilter));
    return this;
  }
  

  build() {
    const groups = this.bag.getAllGroupped();
    let query = this.query;
    for (let [group, params] of Object.entries(groups)) {
      const value = params.length > 1 ? 
        params.map(p => `${p.name}:${p.value}`).join(",") : 
        `${params[0].name}:${params[0].value}`;
      query = query.replace(`#${group}#`, value);
    }
    return query;
  }
}


enum ParamGroup {
  MatchFilter = "match_filter",
  PlayerAccountId = "player_account_id"
}


/**
 * Шаблон для запроса выбора матчей игрока. Содержит набор полей,
 * которые надо выбрать, а также параметры, которые надо заменить
 * на конкретные значения.
 */
const queryTemplate = `
  {
    player(#${ParamGroup.PlayerAccountId}#) {
      steamAccountId,
      matches(request: {
        #${ParamGroup.MatchFilter}#
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
  }
`;


/*
Пример как может выглядеть конечный запрос
operationName: "getMatchInfo",
      query: `query getMatchInfo
        {
          player(steamAccountId: 56834215) {
            steamAccountId,
            matches(request: {
              skip: 100,
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

*/

/*
Пример как можно использовать класс
const builder = new MatchQueryBuilder(queryTemplate);
console.log(builder
  .account(12345)
  .startDateTime(2)
  .endDateTime(3)
  .take(25)
  .build());
*/




/*
 Основные на данный момент поля фильтров матчей:
  // take: number;
  // skip: number;
  // after: number;
  // before: number;
  // matchIds: number[];
  // startDateTime: number;
  // lobbyTypeIds: number[];
 Еще некоторые поля, с которыми можно будет потом придумать что-нибудь интересное (возможно):
  // orderBy: ???;
  // heroIds: number[];
  // roleIds: number[];
  // positionIds: number[];
  // isVictory: boolean;
  // isRadiant: boolean;
*/