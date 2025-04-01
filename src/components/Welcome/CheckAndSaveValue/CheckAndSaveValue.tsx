import { useState } from "react";
import classNames from "classnames";

import * as styles from "./CheckAndSaveValue.module.css";
import { ActionResult } from "../FirstVisit/FirstVisit";


// type CheckAndSaveValueProps = {
//   label: string,
//   checkFunc: (value: string) => Promise<ActionResult>,
//   saveFunc: (value: string) => Promise<ActionResult>,
//   // next: React.Dispatch<React.SetStateAction<number>>
//   next: () => void
// }


/*
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdWJqZWN0IjoiNmVmNzRjMmItMjJiZi00Mzk3LTgyMTUtY2VjYjk3ZDY2YmNkIiwiU3RlYW1JZCI6IjU2ODMxNzY1IiwibmJmIjoxNzE2ODk2ODk5LCJleHAiOjE3NDg0MzI4OTksImlhdCI6MTcxNjg5Njg5OSwiaXNzIjoiaHR0cHM6Ly9hcGkuc3RyYXR6LmNvbSJ9.QoAd60oMIUV4D8N73Lcj6b2MTqc-96vv6PzFcLQqrhg
56831765
*/


export const CheckAndSaveValue = ({label, check, save, next}) => {
  const [ stage, setStage ] = useState("input");  // stages: process, input, save, next
  const [ value, setValue ] = useState("");
  const [ notificatin, setNotification ] = useState(null);

  const checkValue = async () => {
    const { func, message } = check;
    setStage("process");
    setNotification(["wait", message]);
    const checkResult = await func(value);
    if (checkResult.success === true) {
      setStage("save");
      setNotification(["success", checkResult.message]);
    } else {
      setStage("input");
      setNotification(["failure", checkResult.message]);
    }
  }

  const saveValue = async () => {
    const { func, message } = save;
    setStage("process");
    setNotification(["wait", message]);
    const saveResult = await func(value);
    if (saveResult.success === true) {
      setStage("next");
      setNotification(["success", saveResult.message]);
    } else {
      setStage("save");
      setNotification(["failure", saveResult.message]);
    }
  }

  const cancelSave = () => {
    setStage("input");
    setNotification(null);
  }

  const goNextValue = () => {
    next();
  }
  
  const notificationbox = notificatin && <Status oftype={notificatin[0]} message={notificatin[1]} />;

  let displaybox;
  switch (stage) {
    case "input": {
      displaybox = (<>
        <div className={styles.flexLine}>
          <label>{label}</label>
          <div>
            <input onChange={e => setValue(e.target.value)} type="text" />
            <button onClick={checkValue}>Проверить</button>
          </div>
        </div>
        { notificationbox }
      </>)
      break;
    }
    case "save": {
      displaybox = (
        <div>
          { notificationbox }
          <button onClick={saveValue}>Сохранить</button>
          <button onClick={cancelSave}>Отмена</button>
        </div>
      )
      break;
    }
    case "next": {
      displaybox = (
        <div>
          { notificationbox }
          <button onClick={goNextValue}>Далее</button>
        </div>
      );
      break;
    }
    case "process": {
      displaybox = notificationbox;
      break;
    }
  }

  return (
    <div className={styles.wrapper}>
      { displaybox }
    </div>
  )
}


function Status({oftype, message}) {
  // TODO: сделать крутилку для ожидания, и другие значки для успеха \ провала
  /*
  if (oftype === "wait")
  if (oftype === "success")
  if (oftype === "failure")
  */
  return <div>{message}</div>
}