import { Builder } from "./Builder";


export abstract class FilterBuilder extends Builder {
  protected shards: Map<string, any>;


  public constructor() {
    super();
    this.shards = new Map();
  }

  
  protected setShard(shardName: string, shardValue: any): FilterBuilder {
    this.shards.set(shardName, shardValue);
    return this;
  }


  protected mergeShards(): string {
    return Array.from(this.shards).map(r => `${r[0]}:${r[1]}`).join(",");
  }
}