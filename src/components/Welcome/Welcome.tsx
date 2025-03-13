import { Link } from "react-router-dom";


import * as styles from "./Welcome.module.css";
import { AddToken } from "./AddToken/AddToken";
import { SelectUser } from "./SelectUser/SelectUser";


export const Welcome = () => {

  return (
    <div className={styles.wrapper}>
      <AddToken />
      <SelectUser />
      {/* { savedUsersExists ? <SelectUser/> : <AddUser/> } */}
    </div>
  )
}
