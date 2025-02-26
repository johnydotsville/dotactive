export abstract class Builder {
  protected abstract setShard(shardName: string, shardValue: any): Builder;
  protected abstract mergeShards(): string;
  public abstract build(): string;
}
