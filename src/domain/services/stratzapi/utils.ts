import axios from 'axios';

import { AxiosGraphqlQueryAdapter } from "@utils/AxiosGraphqlQueryAdapter";
import { stratzRequestConfig } from '@utils/stratz-request-config';


export async function checkIfTokenValid(token: string): Promise<boolean> {
  const testQuery = AxiosGraphqlQueryAdapter.toAxiosQuery(testStratzApiQuery, "tokenTestQuery")
  const requestConfig: any = stratzRequestConfig;
  requestConfig.headers = {
    ...requestConfig.headers,
    "Authorization": `Bearer ${token}`,
  }
  requestConfig.data = testQuery;
  try {
    const response = await axios.request(requestConfig);  // TODO: вынести это как-то, чтобы не писать эти три мутные строчки, а просто запрос отдать
    if (response.status !== 403) {
      return true;
    }
  } catch (err) { 
    console.log(err); 
  }
  return false;
}


const testStratzApiQuery = `
  {
    stratz {
      status {
        isRedisOnline
      }
    }
  }
`;