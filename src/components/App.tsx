import React from 'react';
import { CssBaseline } from '@mui/material';

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { createContext } from "react";


import { MyDatabase } from '@domain/database/MyDatabase';

import { Welcome } from '@components/Welcome/Welcome';
import { MatchDetails } from '@components/Matches/MatchDetails/MatchDetails';
import { MatchHistory } from '@components/Matches/MatchHistory';


export const DatabaseContext = createContext(null);


export const App: React.FC<Props> = ({ database }) => {
  return (
    <CssBaseline>
      <DatabaseContext.Provider value={database}>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Welcome />}/>
            <Route path="/matches/:id" element={<MatchDetails />} />
            <Route path="/matches" element={<MatchHistory />} />
          </Routes>
        </BrowserRouter>
      </DatabaseContext.Provider>
    </CssBaseline>
  )
}


type Props = {
  database: MyDatabase;
}