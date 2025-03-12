import { useRef } from "react";
import { useState } from "react";
import { useMemo } from "react";


import * as styles from "./AddToken.module.css";
import { StratzAPI } from "@domain/services/stratzapi/StratzAPI";


//eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdWJqZWN0IjoiNmVmNzRjMmItMjJiZi00Mzk3LTgyMTUtY2VjYjk3ZDY2YmNkIiwiU3RlYW1JZCI6IjU2ODMxNzY1IiwibmJmIjoxNzE2ODk2ODk5LCJleHAiOjE3NDg0MzI4OTksImlhdCI6MTcxNjg5Njg5OSwiaXNzIjoiaHR0cHM6Ly9hcGkuc3RyYXR6LmNvbSJ9.QoAd60oMIUV4D8N73Lcj6b2MTqc-96vv6PzFcLQqrhg

export const AddToken = () => {
  const [ tokenInputEnabled, setTokenInputEnabled ] = useState(true);
  const [ tokenValid, setTokenValid ] = useState(false);
  
  const tokenRef = useRef<HTMLInputElement | null>(null);

  const api = useMemo(() => {
    return new StratzAPI();
  }, []);

  const checkToken = async () => {
    setTokenInputEnabled(false);
    api.setToken(tokenRef.current.value);
    const tokenIsOk = await api.checkToken();
    if (tokenIsOk) {
      setTokenValid(true);
    } else {
      setTokenInputEnabled(true);
    }
  }

  const saveToken = async () => {
    await saveValidToken(tokenRef.current.value);
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