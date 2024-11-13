import { HeroName } from "@domain/constants/hero-name";
import { ConstantService } from './constant-service';
import { ConstantNames } from "./constant-names";

export class HeroNamesCS extends ConstantService {
  public constructor(database, storage) {
    super(database, storage, ConstantNames.HeroNames);
  }

  public async init(currentGameVersionId: number, reload: boolean = false) {
    const gql = {
      operationName: "getHeroNames",
      query: `query getHeroNames
        {
          constants {
              heroes(gameVersionId: ${currentGameVersionId}, language: ENGLISH) {
                id,
                displayName,
                shortName
              }
            }
        }`,
      variables: {}
    };

    let heroNames;
    if (reload) {
      this.clean();
    }
    const fromDb = await this.loadValuesFromDb();
    if (fromDb === undefined) {
      const fromServer = await this.loadValuesFromServer(gql);
      heroNames = await this.save(fromServer);
    } else {
      heroNames = fromDb;
    }
    this.values = heroNames.map(x => HeroName.create(x));
  }
}