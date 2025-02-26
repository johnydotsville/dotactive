import { Builder } from "./Builder";


export abstract class DataStructureBuilder extends Builder {
  protected shards: Set<string>;


  public constructor() {
    super();
    this.shards = new Set();
  }

  
  protected setShard(shardName: string): DataStructureBuilder {
    this.shards.add(shardName);
    return this;
  }


  protected mergeShards(): string {
    return Array.from(this.shards).join(",");
  }
}