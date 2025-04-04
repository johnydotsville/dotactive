import { Box, Stack, Typography } from "@mui/material";

export type Metrics = "GPM" | "XPM" | "KDA" | "HERODMG" | "TOWERDMG";



/**
 * 
 * @param
 * pic - путь до картинки иконки.
 * @param
 * stat - кортеж, где первое значение - это непосредственно показатель игрока (например 500 gpm), 
 * второе значение - место игрока среди своей команды по этому показателю (например 1),
 * третье значение - место игрока среди вражеской команды (например 3)
 * @param
 * altValue - используется, когда надо вместо показателя игрока отобразить что-то другое.
 * Например, вместо коэффициента kda (например 1.7) отобразить строку с непосредственными
 * значениями kda (например, 10 / 7 / 21)
 * @returns 
 */
export function PlayerMetricValue({ value, altValue }) {
  const valuePretty = value[0].toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");  // 12000 -> 12.000
  const result: string = altValue ? 
    `${altValue} [${value[1]}] [${value[2]}]` :
    `${valuePretty} [${value[1]}] [${value[2]}]`;
  
  return (
    <Typography>{result}</Typography>
  )
}


export function PlayerMetricIcon({ metric, w = "100%", h = "100%" } : { metric: Metrics, w?: string, h?: string }) {
  switch (metric) {
    case "GPM": return <MetricStub w={w} h={h} />
    case "XPM": return <MetricStub w={w} h={h} />
    case "KDA": return <MetricStub w={w} h={h} />
    case "HERODMG": return <MetricStub w={w} h={h} />
    case "TOWERDMG": return <MetricStub w={w} h={h} />
  }
}


function MetricStub({ w = "100%", h = "100%" } : { w?: string, h?: string}) {
  return (
    <svg viewBox="0 0 24 24" width={w} height={h}>
      <circle cx="12" cy="12" r="10" fill="url(#coin_gradient)"/>
      <circle cx="12" cy="12" r="9.5" fill="url(#coin_highlight)" fillOpacity="0.6"/>
      <path d="M9 9L15 15M15 9L9 15" 
            stroke="#8B7500" 
            strokeWidth="1.5" 
            strokeLinecap="round"/>
      <defs>
        <linearGradient id="coin_gradient" x1="6" y1="6" x2="18" y2="18" gradientUnits="userSpaceOnUse">
          <stop stopColor="#FFD700"/>
          <stop offset="1" stopColor="#D4AF37"/>
        </linearGradient>
        <radialGradient id="coin_highlight" cx="0.35" cy="0.35" r="0.8" gradientUnits="objectBoundingBox">
          <stop offset="0%" stopColor="#FFF9C4"/>
          <stop offset="100%" stopColor="transparent"/>
        </radialGradient>
      </defs>
    </svg>
  )
}