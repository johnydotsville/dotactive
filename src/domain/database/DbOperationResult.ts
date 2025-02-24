export class DbOperationResult<T> {
  public readonly error: Error[];
  public readonly result: T[];


  public constructor() { 
    this.error = [];
    this.result = [];
  }


  public addError(error: Error) {
    this.error.push(error);
  }


  public addResult(result: T) {
    this.result.push(result);
  }
}