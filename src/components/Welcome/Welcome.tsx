import { Link } from "react-router-dom";


import * as styles from "./Welcome.module.css";
import { AddToken } from "./AddToken/AddToken";


export const Welcome = () => {

  return (
    <div className={styles.wrapper}>
      <AddToken />
      {/* { savedUsersExists ? <SelectUser/> : <AddUser/> } */}
    </div>
  )
}
