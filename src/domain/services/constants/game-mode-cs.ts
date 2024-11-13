import { GameMode } from "@domain/constants/game-mode";
import { ConstantService } from './constant-service';
import { ConstantNames } from "./constant-names";

export class GameModeCS extends ConstantService {
  public constructor(database, storage) {
    super(database, storage, ConstantNames.GameModes);
  }

  public async init(reload: boolean = false) {
    const gql = {
      operationName: "getLobbieTypes",
      query: `query getLobbieTypes
        {
          constants {
            gameModes {
              id,
              name
            }
          }
        }`,
      variables: {}
    };

    let gameModes;
    if (reload) {
      this.clean();
    }
    const fromDb = await this.loadValuesFromDb();
    if (fromDb === undefined) {
      const fromServer = await this.loadValuesFromServer(gql);
      gameModes = await this.save(fromServer);
    } else {
      gameModes = fromDb;
    }
    this.values = gameModes.map(x => GameMode.create(x));
  }
}