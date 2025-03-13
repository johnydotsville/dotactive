import { useRef } from "react";
import { useState } from "react";

import * as styles from "./CheckAndSaveValue.module.css";


type CheckAndSaveValueProps = {
  label: string,
  checkFunc: any,
  saveFunc: any
}


export const CheckAndSaveValue: React.FC<CheckAndSaveValueProps> = ({label, checkFunc, saveFunc}) => {
  const [ valueInputEnabled, setValueInputEnabled ] = useState(true);
  const [ valueSaveEnabled, setValueSaveEnabled ] = useState(false);

  const valueRef = useRef<HTMLInputElement | null>(null);

  const checkValue = async () => {
    setValueInputEnabled(false);
    const valueIsOk = await checkFunc(valueRef.current.value);
    if (valueIsOk) {
      setValueSaveEnabled(true);
    } else {
      setValueInputEnabled(true);
    }
  }

  const saveValue = async () => {
    await saveFunc(valueRef.current.value);
    setValueSaveEnabled(false);
    setValueInputEnabled(true);
    valueRef.current.value = "";
  }

  return (
    <div className={styles.wrapper}>
      <div className={styles.inputPair}>
        <label htmlFor="valueForCheck">{label}</label>
        <input id="valueForCheck" ref={valueRef} className={styles.inputPairText} type="text" disabled={!valueInputEnabled} />
      </div>
      <div className={styles.inputPair}>
        <button onClick={checkValue}>Проверить</button>
        { valueSaveEnabled && <button onClick={saveValue}>Сохранить</button> }
      </div>
    </div>
  )
}

// export const AddToken = () => {
//   const [ tokenInputEnabled, setTokenInputEnabled ] = useState(true);
//   const [ tokenValid, setTokenValid ] = useState(false);
  
//   const tokenRef = useRef<HTMLInputElement | null>(null);
//   const database: MyDatabase = useContext(DatabaseContext);

//   const api = useMemo(() => {
//     return new StratzAPI();
//   }, []);

//   const checkToken = async () => {
//     setTokenInputEnabled(false);
//     api.setToken(tokenRef.current.value);
//     const tokenIsOk = await api.checkToken();
//     if (tokenIsOk) {
//       setTokenValid(true);
//     } else {
//       setTokenInputEnabled(true);
//     }
//   }

//   const saveToken = async () => {
//     const storage = database.getStorage<TokenStorage>(StorageName.Tokens);
//     const token: Token = { token: tokenRef.current.value };
//     const saveTokenResult = await storage.save(token);  // TODO: Сделать мб проверку на уже существующий такой же токен, чтобы не сохранять одинаковые?
//     const errors = saveTokenResult.error;
//     const result = saveTokenResult.result[0];
//     window.localStorage.setItem("current_token", result.token);
//     setTokenValid(false);
//     setTokenInputEnabled(true);
//     tokenRef.current.value = "";
//   }

//   return (
//     <div className={styles.wrapper}>
//       <div className={styles.inputPair}>
//         <label htmlFor="token">Stratz Token:</label>
//         <input id="token" ref={tokenRef} className={styles.inputPairText} type="text" disabled={!tokenInputEnabled} />
//       </div>
//       <div className={styles.inputPair}>
//         <button onClick={checkToken}>Проверить</button>
//         { tokenValid && <button onClick={saveToken}>Сохранить</button> }
//       </div>
//     </div>
//   )
// }


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