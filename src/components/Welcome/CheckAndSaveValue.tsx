import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Stack from '@mui/material/Stack';
import Typography from '@mui/material/Typography';
import CircularProgress from '@mui/material/CircularProgress';
import Box from '@mui/material/Box';
import ErrorIcon from '@mui/icons-material/Error';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';

import { useState } from "react";

import { ActionResult } from './FirstVisit';


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
  const [ notification, setNotification ] = useState(null);

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
  
  const notificationbox = notification && <Status oftype={notification[0]} message={notification[1]} />;

  let stagebox;
  switch (stage) {
    case "input": {
      stagebox = (<>
        <TextField label={label} onChange={e => setValue(e.target.value)}
          variant="outlined" fullWidth margin="normal" />
        <Stack direction="row" justifyContent="end" spacing={2}>
          <Button onClick={checkValue} variant="contained">Проверить</Button>
        </Stack>
      </>)
      break;
    }
    case "save": {
      stagebox = (
        <Stack direction="row" justifyContent="end" spacing={2}>
          <Button onClick={saveValue} variant="contained" color="success">Сохранить</Button>
          <Button onClick={cancelSave} variant="contained" color="error">Отмена</Button>
        </Stack>
      )
      break;
    }
    case "next": {
      stagebox = (
        <Stack direction="row" justifyContent="end" spacing={2}>
          <Button onClick={goNextValue} variant="contained" color="primary">Далее</Button>
        </Stack>
      );
      break;
    }
    case "process": {
      stagebox = null;
      break;
    }
  }

  return (
    <Box sx={{ 
      border: "1px solid", borderColor: "primary", borderRadius: 1,
      p: { xs: 1, sm: 2, md: 4 },
    }}>
      <Stack direction="column" spacing={2}>
        { notificationbox }
        { stagebox }
      </Stack>
    </Box>
  )
}


function Status({oftype, message}) {
  let marker;
  switch (oftype) {
    case "wait": {
      marker = <CircularProgress />
      break;
    }
    case "success": {
      marker = <CheckCircleIcon color="success" fontSize="large" />;
      break;
    }
    case "failure": {
      marker = <ErrorIcon color="error" fontSize="large" />
      break;
    }
  }
  return (
    <Stack direction="row" justifyContent="center" alignItems="center" spacing={2}>
      {marker}
      <Typography variant="body1">{message}</Typography>
    </Stack>
  )
}