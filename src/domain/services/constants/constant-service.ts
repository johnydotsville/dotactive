import axios, {isCancel, AxiosError} from 'axios';
import { ConstantNames } from "./constant-names";
import { stratzRequestConfig } from '@utils/stratz-request-config';

/**
  Базовый класс для всех сервисов констант. Содержит методы загрузки констант с сервера,
  из БД, а также методы сохранения \ очистки хранилища и возврата всех констант или одной
  конкретной константы.
*/
export class ConstantService {
  protected database;
  protected storage: string;
  protected constantName: ConstantNames;
  protected requestConfig: any;
  protected values: any;

  public constructor(database, storage, constantName: ConstantNames) {
    this.database = database;
    this.storage = storage;
    this.constantName = constantName;
    this.requestConfig = stratzRequestConfig;
  }

  protected async loadValuesFromServer(query) {
    this.requestConfig.data = query;
    const response = await axios.request(this.requestConfig);
    return response.data.data.constants[this.constantName]
  }

  protected async save(values) {
    return await this.database.save(this.storage, values, this.constantName);
  }

  protected async clean() {
    await this.database.delete(this.storage, this.constantName);
  }
  
  protected async loadValuesFromDb() {
    return await this.database.read(this.storage, this.constantName);
  }
  
  public getAllValues() {
    return this.values;
  }

  public getValueById(id: number) {
    return this.values.find(x => x.id === id)
  }
}