/**
 * Основа запроса к stratz api. Содержит url, метод запроса и обязательные заголовки
 * (включая токен).
 */
export const stratzRequestConfig = {
  url: "https://api.stratz.com/graphql",
  method: "post",
  timeout: 7000,
  headers: {
    "content-type": "application/json",
    "User-Agent": "STRATZ_API"
  }
};