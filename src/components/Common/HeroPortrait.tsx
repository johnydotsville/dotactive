import { Box } from "@mui/material";

import { useState } from "react";


export function HeroPortrait({ heroname, w = "100%", h = "100%" }) {
  const [heroIconLoadingError, setHeroIconLoadingError] = useState(false);

  const heroimg = heroIconLoadingError ? "stubportrait" : heroname;
  const heroimgPath = `/assets/img/heroes/${heroimg}.png`;  // TODO: Сделать пути до ассетов через глобальную переменную, чтобы не хардкодить

  const handleHeroIconLoadingError = () => setHeroIconLoadingError(true);

  return (
    <Box 
      component="img"
      src={heroimgPath}
      onError={handleHeroIconLoadingError} 
      loading="lazy" 
      alt={heroname}
      sx={{ display: "block", width: w, height: h }}
    />
  )
}