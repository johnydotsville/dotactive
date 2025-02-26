/**
 * Вспомогательный класс. Формирует из строки запроса объект, который нужен 
 * библиотеке axios для отправки graphql запроса.
 */
export class AxiosGraphqlQueryAdapter {
  static toAxiosQuery(queryString, queryName) {
    return {
      operationName: queryName,
      query: `query ${queryName} ${queryString}`,
      variables: {}
    }
  }
}