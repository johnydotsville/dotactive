import {useState} from 'react';
import { useEffect } from "react";
import Matches from "@components/Matches/Matches";

import * as classes from "./App.module.css";
import spectre from "@assets/img/heroes/spectre.png";

export const App = () => {

  return (
    <div>
      <Matches />
    </div>
  )
}