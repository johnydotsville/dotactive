import { useState } from "react";


import * as styles from "./FirstVisit.module.css";

import { checkIfTokenValid } from "@domain/services/stratzapi/utils";
import { checkIfSteamAccountIdValid } from "@domain/services/stratzapi/utils";
import { CheckAndSaveValue } from "../CheckAndSaveValue/CheckAndSaveValue";


export type ActionResult = {
  success: boolean,
  message: string
}

const values = [
  { 
    label: "Stratz API токен", 
    check: {
      func: checkToken, 
      message: "Проверка токена..."
    },
    save: {
      func: saveToken,
      message: "Сохранение токена..."
    }
  },
  { 
    label: "Steam ID", 
    check: {
      func: checkAccount, 
      message: "Проверка Steam ID..."
    },
    save: {
      func: saveAccount ,
      message: "Сохранение Steam ID..."
    }
  },
];

export const FirstVisit = () => {
  const [ currentValue, setCurrentValue ] = useState(0);

  let currentScreen;
  if (currentValue < values.length) {
    currentScreen = <CheckAndSaveValue
      key={ currentValue }
      label={ values[currentValue].label } 
      check={ values[currentValue].check} save={values[currentValue].save }
      next={ () => setCurrentValue(prev => prev + 1) }
    />;
  } else {
    currentScreen = <div>Все шаги выполнены.</div>
    // TODO: добавить ссылку для перехода на страницу матчей
  }
  return currentScreen;
}


async function checkToken(token: string): Promise<ActionResult> {
  const isValid = await checkIfTokenValid(token);
  return {
    success: isValid,
    message: isValid ? "Токен в порядке." : "Введенный токен не работает."
  }
}


async function saveToken(token: string): Promise<ActionResult> {
  try {
    localStorage.setItem("current_token", token);
  } catch (error) {
    console.log(error);
    return { 
      success: false, 
      message: "Не удалось сохранить токен." 
    };
  }
  return { 
    success: true, 
    message: "Токен сохранен успешно." 
  };
}


async function checkAccount(account: string): Promise<ActionResult> {
  const isValid = await checkIfSteamAccountIdValid(account);
  return {
    success: isValid,
    message: isValid ? "Аккаунт в порядке." : "Введенный аккаунт не найден."
  }
}

async function saveAccount(account: string): Promise<ActionResult> {
  try {
    localStorage.setItem("current_user", account);
  } catch (error) {
    console.log(error);
    return { 
      success: false, 
      message: "Не удалось сохранить аккаунт." 
    };
  }
  return { 
    success: true, 
    message: "Аккаунт сохранен успешно." 
  };
}
