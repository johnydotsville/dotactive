import { checkIfTokenValid } from "@domain/services/stratzapi/utils";
import { CheckAndSaveValue } from "../CheckAndSaveValue/CheckAndSaveValue";


export const AddToken = () => {
  const checkToken = async (token: string) => {
    return await checkIfTokenValid(token);
  }

  const saveToken = async (token: string) => {
    window.localStorage.setItem("current_token", token);
    const allTokensKey = "all_tokens";
    const allTokens = window.localStorage.getItem(allTokensKey);
    if (!allTokens) {
      window.localStorage.setItem(allTokensKey, token);
    } else {
      window.localStorage.setItem(allTokensKey, allTokens + `,${token}`)
    }
  }

  return (
    // <CheckAndSaveValue label="Stratz token" checkFunc={checkToken} saveFunc={saveToken} />
    <div>sadf</div>
  )
}