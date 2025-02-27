import { FilterBuilder } from "../utils/ParamsBag";


export class MatchRequestFilterBuilder extends FilterBuilder {
  public take(matchesCount: number): MatchRequestFilterBuilder {
    super.setShard("take", matchesCount);
    return this;
  }


  public skip(matchesCount: number): MatchRequestFilterBuilder {
    super.setShard("skip", matchesCount);
    return this;
  }


  public build(): string {
    const filters = super.mergeShards();
    // return `request:{${filters}}`;
    return filters;
  }
}



/*
 Основные на данный момент поля настроек:
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