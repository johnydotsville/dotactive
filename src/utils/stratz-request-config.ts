import { token } from "@projconfig/misc/token";

export const stratzRequestConfig = {
  url: "https://api.stratz.com/graphql",
  method: "post",
  headers: {
    "content-type": "application/json",
    "Authorization": `Bearer ${token}`,
    "User-Agent": "STRATZ_API"
  }
};