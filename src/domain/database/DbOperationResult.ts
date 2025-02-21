
/*
TODO: переделать, чтобы был массив ошибок и массив результатов. Потому что
дополнительно проходить по всему считанному из БД массиву, чтобы вытащить
из каждого элемента данные матча - это хрень полная. Пусть в result будет
сразу массив матче, а в error - массив ошибок. Т.е. "отчет" об операции чтения
будет не "массив отчетов", а "отчет с массивами", смекаешь?
*/

export class DbOperationResult<T> {
  public readonly succeeded: boolean;
  public readonly error?: Error;
  public readonly result?: T;


  private constructor({ succeeded, error, result }: { succeeded: boolean, error?: Error, result?: T }) { 
    this.succeeded = succeeded;
    this.error = error;
    this.result = result;
  }


  public static success<T>(result?: T): DbOperationResult<T> {
    return new DbOperationResult<T>({ succeeded: true, result });
  }


  public static fail<T>(error: Error, result?: T): DbOperationResult<T> {
    return new DbOperationResult<T>({ succeeded: false, error, result });
  }
}