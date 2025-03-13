import { useRef } from "react";
import { useState } from "react";

import * as styles from "./CheckAndSaveValue.module.css";


type CheckAndSaveValueProps = {
  label: string,
  checkFunc: (value: string) => Promise<boolean>,
  saveFunc: (value: string) => Promise<void>
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
      <div className={styles.flexLine}>
        <label htmlFor="valueForCheck">{label}</label>
        <input id="valueForCheck" ref={valueRef} className={styles.inputPairText} 
               type="text" disabled={!valueInputEnabled} />
      </div>
      <div className={styles.flexLine}>
        <button onClick={checkValue}>Проверить</button>
        { valueSaveEnabled && <button onClick={saveValue}>Сохранить</button> }
      </div>
    </div>
  )
}