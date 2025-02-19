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