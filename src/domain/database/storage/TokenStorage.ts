import { StorageName } from "../config/storages/StorageName";
import { Storage } from "./Storage";


export class TokenStorage extends Storage<Token, number> {
  public constructor(database: IDBDatabase, storageName: StorageName) {
    super(database, storageName);
  }
}


export type Token = {
  id?: number;
  token: string;
}