export class GameMode {
  id: number;
  name: string;

  // constructor(id: number, name: string) {
  //   this.id = id;
  //   this.name = name;
  // }

  public static create(obj): GameMode {
    const gm = new GameMode();
    gm.id = obj.id;
    gm.name = obj.name;
    return gm;
  }
}