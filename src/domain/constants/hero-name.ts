export class HeroName {
  id: number;
  displayName: string;
  shortName: string;

  // constructor(id: number, displayName: string, shortName: string) {
  //   this.id = id;
  //   this.displayName = displayName;
  //   this.shortName = shortName;
  // }

  public static create(obj): HeroName {
    const hn = new HeroName();
    hn.id = obj.id;
    hn.displayName = obj.displayName;
    hn.shortName = obj.shortName;
    return hn;
  }
}