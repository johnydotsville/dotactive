export type DbOperationResult<T> = {
  succeeded: boolean;
  error?: Error;
  data?: T;
}