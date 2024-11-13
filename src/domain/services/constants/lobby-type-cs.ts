import { LobbyType } from "@domain/constants/lobby-type";
import { ConstantService } from './constant-service';
import { ConstantNames } from "./constant-names";

export class LobbyTypeCS extends ConstantService {
  public constructor(database, storage) {
    super(database, storage, ConstantNames.LobbyTypes);
  }

  public async init(reload: boolean = false) {
    const gql = {
      operationName: "getLobbyTypes",
      query: `query getLobbyTypes
        {
          constants {
            lobbyTypes {
              id,
              name
            }
          }
        }`,
      variables: {}
    };

    let lobbieTypes;
    if (reload) {
      this.clean();
    }
    const fromDb = await this.loadValuesFromDb();
    if (fromDb === undefined) {
      const fromServer = await this.loadValuesFromServer(gql);
      lobbieTypes = await this.save(fromServer);
    } else {
      lobbieTypes = fromDb;
    }
    this.values = lobbieTypes.map(x => LobbyType.create(x));
  }
}