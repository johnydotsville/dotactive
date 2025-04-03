import { getRadiantTeam, getDireTeam } from "@domain/services/analyze/utils";
import { HeroPortrait } from "@components/Common/HeroPortrait/HeroPortrait";
import { PlayerPosition } from "@components/Common/PlayerPosition/PlayerPosition";

import { Box, Stack, Typography } from "@mui/material";
import { Match } from "@domain/services/stratzapi/datamodel/Match";


export function Matchup({ match } : { match: Match }) {
  const radiant = getRadiantTeam(match.matchPlayers);
  const dire = getDireTeam(match.matchPlayers);

  return (
    <Stack direction="column" spacing={3}>
      <TeamLine team={radiant} score={match.radiantScore} win={match.didRadiantWin} />
      <TeamLine team={dire} score={match.direScore} win={match.didDireWin} />
    </Stack>
  )
}


function TeamLine({team, score, win}) {
  return (
    <Stack 
      direction="row" 
      spacing={5}
      height="50px"
    >
      <TeamScore score={score} win={win} />
      { team.map(p => <PlayerHeroAndPosition player={p} />) }
    </Stack>
  )
}


function PlayerHeroAndPosition({player}) {
  return (
    <Stack
      direction="row" 
      bgcolor="#B7AFAF" 
      border="2px solid" 
      borderColor="black"
      alignItems="center"
      height="100%"
    >
      <Stack direction="row" height="100%" alignItems="center">
        <HeroPortrait heroname={player.heroShortName} />
      </Stack>
      <Stack direction="row" height="70%" alignItems="center">
        <PlayerPosition position={player.position} />
      </Stack>
    </Stack>
  )
}


function TeamScore({score, win}) {
  const color = (win === true) ? "green" : "red";
  return (
    <Box sx={{
      bgcolor: color,
      height:"100%",
      aspectRatio:"1/1",
      display: "flex",
      border: "2px solid black",
    }} justifyContent="center" alignItems="center">
      <Typography variant="body1" sx={{ fontSize: "2rem" }}>{ score }</Typography>
    </Box>
  )
}