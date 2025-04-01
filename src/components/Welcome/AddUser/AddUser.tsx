import * as styles from "./SelectUser.module.css";
import { CheckAndSaveValue } from "../CheckAndSaveValue/CheckAndSaveValue";
import { checkIfSteamAccountIdValid } from "@domain/services/stratzapi/utils";


export const AddUser = () => {
  const checkAccount = async (account: string) => {
    return await checkIfSteamAccountIdValid(account);
  }

  const saveAccount = async (account: string) => {
    window.localStorage.setItem("current_user", account);
    // const allTokensKey = "all_tokens";
    // const allTokens = window.localStorage.getItem(allTokensKey);
    // if (!allTokens) {
    //   window.localStorage.setItem(allTokensKey, token);
    // } else {
    //   window.localStorage.setItem(allTokensKey, allTokens + `,${token}`)
    // }
  }

  return (
    // <CheckAndSaveValue label="Steam Account ID" checkFunc={checkAccount} saveFunc={saveAccount} />
    <div>sd</div>
  )
}