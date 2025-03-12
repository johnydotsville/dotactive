import { token } from "@projconfig/misc/token";

/**
 * Основа запроса к stratz api. Содержит url, метод запроса и обязательные заголовки
 * (включая токен).
 */
export const stratzRequestConfig = {
  url: "https://api.stratz.com/graphql",
  method: "post",
  headers: {
    "content-type": "application/json",
    // "Authorization": `Bearer ${token}`,
    "User-Agent": "STRATZ_API"
  }
};