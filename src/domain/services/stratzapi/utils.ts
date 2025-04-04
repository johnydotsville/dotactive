import axios from 'axios';

import { AxiosGraphqlQueryAdapter } from "@utils/AxiosGraphqlQueryAdapter";
import { stratzRequestConfig } from '@utils/stratz-request-config';


export async function checkIfTokenValid(token: string): Promise<[boolean, Error]> {
  const testQuery = AxiosGraphqlQueryAdapter.toAxiosQuery(testIfTokenValid, "tokenTestQuery")
  const requestConfig: any = stratzRequestConfig;
  requestConfig.headers = {
    ...requestConfig.headers,
    "Authorization": `Bearer ${token}`,
  }
  requestConfig.data = testQuery;
  try {
    const response = await axios.request(requestConfig);  // TODO: вынести это как-то, чтобы не писать эти три мутные строчки, а просто запрос отдать
    if (response.status === 200) {
      return [true, null];
    }
  } catch (error) { 
    return [false, error];
  }
}


const testIfTokenValid = `
  {
    stratz {
      status {
        isRedisOnline
      }
    }
  }
`;


export async function checkIfSteamAccountIdValid(steamAccountId: string): Promise<boolean> {
  const testIfSteamAccountIdValid = `{ player(steamAccountId:${steamAccountId}) { matchCount } }`;
  const testQuery = AxiosGraphqlQueryAdapter.toAxiosQuery(testIfSteamAccountIdValid, "tokenTestQuery")
  const token = window.localStorage.getItem("current_token");
  const requestConfig: any = stratzRequestConfig;
  requestConfig.headers = {
    ...requestConfig.headers,
    "Authorization": `Bearer ${token}`,
  }
  requestConfig.data = testQuery;
  try {
    const response = await axios.request(requestConfig);  // TODO: вынести это как-то, чтобы не писать эти три мутные строчки, а просто запрос отдать
    if (response.data.data.player.matchCount !== null) {
      return true;
    }
  } catch (err) { 
    console.log(err); 
  }
  return false;
}