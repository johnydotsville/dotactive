import React from 'react';
import { createContext } from "react";


import { MyDatabase } from '@domain/database/MyDatabase';
import Matches from "@components/Matches/Matches";


export const DatabaseContext = createContext(null);


export const App: React.FC<Props> = ({ database }) => {
  return (
    <DatabaseContext.Provider value={database}>
      <Matches />
    </DatabaseContext.Provider>
  )
}


type Props = {
  database: MyDatabase;
}