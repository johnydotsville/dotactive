export class GameVersion {
  id: number;
  name: string;
  releaseDate: number;

  // constructor(id: number, name: string, releaseDate: number) {
  //   this.id = id;
  //   this.name = name;
  //   this.releaseDate = releaseDate;
  // }

  public static create(obj): GameVersion {
    const gv = new GameVersion();
    gv.id = obj.id;
    gv.name = obj.name;
    gv.releaseDate = obj.asOfDateTime;
    return gv;
  }
}