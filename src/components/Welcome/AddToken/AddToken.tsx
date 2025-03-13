import { checkIfTokenValid } from "@domain/services/stratzapi/utils";
import { CheckAndSaveValue } from "../CheckAndSaveValue/CheckAndSaveValue";


//eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdWJqZWN0IjoiNmVmNzRjMmItMjJiZi00Mzk3LTgyMTUtY2VjYjk3ZDY2YmNkIiwiU3RlYW1JZCI6IjU2ODMxNzY1IiwibmJmIjoxNzE2ODk2ODk5LCJleHAiOjE3NDg0MzI4OTksImlhdCI6MTcxNjg5Njg5OSwiaXNzIjoiaHR0cHM6Ly9hcGkuc3RyYXR6LmNvbSJ9.QoAd60oMIUV4D8N73Lcj6b2MTqc-96vv6PzFcLQqrhg

export const AddToken = () => {
  const checkToken = async (token: string) => {
    return await checkIfTokenValid(token);
  }

  const saveToken = async (token: string) => {
    window.localStorage.setItem("current_token", token);
  }

  return (
    <CheckAndSaveValue label="Stratz token" checkFunc={checkToken} saveFunc={saveToken} />
  )
}