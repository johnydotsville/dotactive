import { GameVersion } from "@domain/constants/game-version";
import { ConstantService } from './constant-service';
import { ConstantNames } from "./constant-names";

export class GameVersionCS extends ConstantService {
  private gameVersionChanged: boolean = false;

  public constructor(database, storage) {
    super(database, storage, ConstantNames.GameVersions);
  }

  public async init(reload: boolean = false) {
    // const gql = {
    //   operationName: "getGameVersions",
    //   query: `query getGameVersions 
    //     { 
    //       constants { 
    //         gameVersions { 
    //           id, 
    //           name, 
    //           asOfDateTime 
    //         } 
    //       } 
    //     }`,
    //   variables: {}
    // };

    // let gameVersion;
    // const fromServer = (await this.loadValuesFromServer(gql))[0];
    // const fromDb = await this.loadValuesFromDb();
    // if (fromDb === undefined) {
    //   gameVersion = await this.save(fromServer);
    // } else {
    //   if (fromDb.id !== fromServer.id) {
    //     await this.clean();
    //     gameVersion = await this.save(fromServer);
    //     this.gameVersionChanged = true;
    //   } else {
    //     gameVersion = fromServer;
    //   }
    // }
    // this.values = [GameVersion.create(gameVersion)];
    this.values = [{id: 176, name: '7.37', asOfDateTime: 1722470400}];
  }
  
  public getGameVersion() {
    return this.values[0];
  }

  public gameVersionHasChanged(): boolean {
    return this.gameVersionChanged;
  }
}