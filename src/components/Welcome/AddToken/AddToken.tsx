import { useRef } from "react";
import { useState } from "react";
import { useMemo } from "react";
import { useContext } from "react";


import * as styles from "./AddToken.module.css";
import { StratzAPI } from "@domain/services/stratzapi/StratzAPI";
import { DatabaseContext } from "@components/App/App";
import { MyDatabase } from "@domain/database/MyDatabase";
import { Token, TokenStorage } from "@domain/database/storage/TokenStorage";
import { StorageName } from "@domain/database/config/storages/StorageName";
import { checkIfTokenValid } from "@domain/services/stratzapi/utils";


//eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdWJqZWN0IjoiNmVmNzRjMmItMjJiZi00Mzk3LTgyMTUtY2VjYjk3ZDY2YmNkIiwiU3RlYW1JZCI6IjU2ODMxNzY1IiwibmJmIjoxNzE2ODk2ODk5LCJleHAiOjE3NDg0MzI4OTksImlhdCI6MTcxNjg5Njg5OSwiaXNzIjoiaHR0cHM6Ly9hcGkuc3RyYXR6LmNvbSJ9.QoAd60oMIUV4D8N73Lcj6b2MTqc-96vv6PzFcLQqrhg

export const AddToken = () => {
  const [ tokenInputEnabled, setTokenInputEnabled ] = useState(true);
  const [ tokenValid, setTokenValid ] = useState(false);
  
  const tokenRef = useRef<HTMLInputElement | null>(null);
  const database: MyDatabase = useContext(DatabaseContext);

  // const api = useMemo(() => {
  //   return new StratzAPI();
  // }, []);

  // const checkToken = async () => {
  //   setTokenInputEnabled(false);
  //   api.setToken(tokenRef.current.value);
  //   const tokenIsOk = await api.checkToken();
  //   if (tokenIsOk) {
  //     setTokenValid(true);
  //   } else {
  //     setTokenInputEnabled(true);
  //   }
  // }

  const checkToken = async () => {
    setTokenInputEnabled(false);
    const tokenIsOk = await checkIfTokenValid(tokenRef.current.value);
    if (tokenIsOk) {
      setTokenValid(true);
    } else {
      setTokenInputEnabled(true);
    }
  }

  const saveToken = async () => {
    const storage = database.getStorage<TokenStorage>(StorageName.Tokens);
    const token: Token = { token: tokenRef.current.value };
    const saveTokenResult = await storage.save(token);  // TODO: Сделать мб проверку на уже существующий такой же токен, чтобы не сохранять одинаковые?
    const errors = saveTokenResult.error;
    const result = saveTokenResult.result[0];
    window.localStorage.setItem("current_token", result.token);
    setTokenValid(false);
    setTokenInputEnabled(true);
    tokenRef.current.value = "";
  }

  return (
    <div className={styles.wrapper}>
      <div className={styles.inputPair}>
        <label htmlFor="token">Stratz Token:</label>
        <input id="token" ref={tokenRef} className={styles.inputPairText} type="text" disabled={!tokenInputEnabled} />
      </div>
      <div className={styles.inputPair}>
        <button onClick={checkToken}>Проверить</button>
        { tokenValid && <button onClick={saveToken}>Сохранить</button> }
      </div>
    </div>
  )
}


async function saveValidToken(token: string) {
  
}

/*
  Логика компонента:
  * Есть поле ввода под токен и кнопка Проверить.
  * Человек вводит токен, нажимает Проверить.
  * Поле ввода становится disabled, чтобы человек не мог изменить токен, пока не закончится обработка.
  * Если проверка показывает, что токен невалидный, то поле снова становится доступно для редактирования,
    чтобы человек мог исправить токен.
  * Если токен валидный, то поле все еще не доступно для редактирования, но появляется кнопка Сохранить.
  * После успешного сохранения поле ввода токена очищается и становится доступным для редактирования, а кнопка сохранения исчезает
*/