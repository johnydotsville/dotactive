import React from 'react';
import { CssBaseline } from '@mui/material';

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { createContext } from "react";


import { MyDatabase } from '@domain/database/MyDatabase';

import Matches from "@components/Matches/Matches";
import { Welcome } from '@components/Welcome/Welcome';
import { MatchDetails } from '@components/Matches/MatchDetails/MatchDetails';


export const DatabaseContext = createContext(null);


export const App: React.FC<Props> = ({ database }) => {
  return (
    <CssBaseline>
      <DatabaseContext.Provider value={database}>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Welcome />}/>
            <Route path="/matches/:id" element={<MatchDetails />} />
            <Route path="/matches" element={<Matches />} />
          </Routes>
        </BrowserRouter>
      </DatabaseContext.Provider>
    </CssBaseline>
  )
}


type Props = {
  database: MyDatabase;
}