export class LobbyType {
  id: number;
  name: string;

  // constructor(id: number, name: string) {
  //   this.id = id;
  //   this.name = name;
  // }

  public static create(obj): LobbyType {
    const lt = new LobbyType();
    lt.id = obj.id;
    lt.name = obj.name;
    return lt;
  }
}