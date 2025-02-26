import { MatchRequestFilterBuilder } from "./MatchRequestFilterBuilder";
import { MatchRequestDataStructureBuilder } from "./MatchRequestDataStructureBuilder";


export class MatchRequestBuilder {
  public readonly filter: MatchRequestFilterBuilder;
  public readonly data: MatchRequestDataStructureBuilder;

  public constructor(filterBuilder: MatchRequestFilterBuilder, 
                     dataStructureBuilder: MatchRequestDataStructureBuilder) {
    this.filter = filterBuilder;
    this.data = dataStructureBuilder;
  }

  public build(): string {
    const filters = this.filter.build()
    const datas = this.data.build();
    return `matches(request:{${filters}}){${datas}}`;
  }
}