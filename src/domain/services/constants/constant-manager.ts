import { GameModeCS } from './game-mode-cs';
import { GameVersionCS } from './game-version-cs';
import { LobbyTypeCS } from './lobby-type-cs';
import { HeroNamesCS } from "./hero-names-cs";

/**
  При первом запуске приложения все константы загружаются с сервера и сохраняются в локальную БД.
  При повторном запуске приложения с сервера загружается только версия игры. Если выяснилось, что
  версия изменилась, то все константы удаляются из локальной БД и перезагружаются заново. Если не
  изменилась, то константы берутся из БД.
*/
export class ConstantManager {
  private storage = "constants";   // TODO: как лучше связать имена таблиц, чтобы не хардкодить?

  private gameModes: GameModeCS;
  private gameVersion: GameVersionCS;
  private lobbyTypes: LobbyTypeCS;
  private heroNames: HeroNamesCS

  public constructor(database) {
    this.gameModes = new GameModeCS(database, this.storage)
    this.gameVersion = new GameVersionCS(database, this.storage);
    this.lobbyTypes = new LobbyTypeCS(database, this.storage);
    this.heroNames = new HeroNamesCS(database, this.storage);
  }

  // TODO: все константы можно было выбрать одним запросом (кроме версии игры, ее надо отдельным, т.к.
  // она нужна для выбора героев), а потом уже полученные данные распихать по БД. Переписать?
  public async init() {
    await this.gameVersion.init();
    const needReloadConstants = this.gameVersion.gameVersionHasChanged();
    await this.gameModes.init(needReloadConstants);
    await this.lobbyTypes.init(needReloadConstants);
    await this.heroNames.init(this.gameVersion.getGameVersion().id, needReloadConstants);
  }

  // --------------------------------------- LOBBIE TYPES --------------------------------------
  public getLobbyTypes() {
    return this.lobbyTypes.getAllValues();
  }

  public getLobbyTypeById(id: number) {
    return this.lobbyTypes.getValueById(id);
  }

  // --------------------------------------- GAME MODES -----------------------------------------
  public getGameModes() {
    return this.gameModes.getAllValues();
  }

  public getGameModeById(id: number) {
    return this.gameModes.getValueById(id);
  }

  // --------------------------------------- GAME VERSION ----------------------------------------
  public getGameVersion() {
    return this.gameVersion.getGameVersion();
  }

  public gameVersionHasChanged() {
    return this.gameVersion.gameVersionHasChanged();
  }
}