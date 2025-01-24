/**
 * Построитель запроса выборки матчей игрока. Содержит методы установки
 * параметров для шаблона запроса и метод генерации строки запроса.
 */
export class MatchQueryBuilder {
  private query: string;
  private requestParams: any;
  private singleParams: any;

  constructor() {
    this.query = queryTemplate;  // TODO: Так нормально делать? Или все же лучше отдельно в клиенте импортировать шаблон и передавать его через конструктор?
    this.requestParams = [];
    this.singleParams = [];
  }

  account(account) {
    this.singleParams.push({
      name: "playerAccountId",
      value: account
    });
    return this;
  }

  take(count) {
    this.requestParams.push({
      name: "take",
      value: count
    });
    return this;
  }

  startDateTime(dateTime) {
    this.requestParams.push({
      name: "startDateTime",
      value: dateTime
    });
    return this;
  }

  endDateTime(dateTime) {
    this.requestParams.push({
      name: "endDateTime",
      value: dateTime
    });
    return this;
  }

  replaceSingleParams() {
    this.query = this.singleParams.reduce((qt, p) => qt.replace(`#${p.name}#`, p.value), this.query);
  }

  replaceComplexParams() {
    const requestParamsUnited = this.requestParams
      .map(p => `${p.name}: ${p.value}`)
      .join(", ");

    this.query = this.query.replace("#requestParams#", requestParamsUnited)
  }

  build() {
    this.replaceSingleParams();
    this.replaceComplexParams();
    return this.query;
  }
}

/**
 * Шаблон для запроса выбора матчей игрока. Содержит набор полей,
 * которые надо выбрать, а также параметры, которые надо заменить
 * на конкретные значения.
 */
const queryTemplate = `
  {
    player(steamAccountId: #playerAccountId#) {
      steamAccountId,
      matches(request: {
        #requestParams#
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