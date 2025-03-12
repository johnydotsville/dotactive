import { MatchPlayer } from "../stratzapi/datamodel/MatchPlayer";

/**
 * Рассчитывает, на каком месте находится показатель игрока относительно
 * показателей его тиммейтов и соперников.
 * @param player
 * Показатель игрока.
 * @param team
 * Массив показателей тиммейтов игрока.
 * @param enemies
 * Массив показателей соперников.
 * @returns
 * Возвращает кортеж с показателем игрока, местом среди своей команды и
 * местом среди соперников.
 */
export function getPlayerPlaceByPerformance(player: number, team: number[], enemies: number[]): [player: number, team: number, enemies: number] {
  const desc = (a: number, b: number): number => b - a;
  team.push(player);
  team.sort(desc);
  enemies.push(player);
  enemies.sort(desc);
  const positionInTeam = team.indexOf(player) + 1;
  const positionInEnemies = enemies.indexOf(player) + 1;

  return [player, positionInTeam, positionInEnemies];
}


export function kdaRatio(kill: number, death: number, assist: number): number {
  const rawKda = (kill + assist) / death;
  return Math.round(rawKda * 100) / 100;
}


export function getRadiantTeam(players: MatchPlayer[]): MatchPlayer[] {
  const radiant = players.filter(p => p.isRadiant);
  try {
    radiant.sort((p1, p2) => {
      if (p1.position && p2.position) {
        return p1.position.localeCompare(p2.position);
      } else {
        return -1;
      }
    });
  } catch (err) {
    console.log(err);
  }
  return radiant;
}


export function getDireTeam(players: MatchPlayer[]): MatchPlayer[] {
  const dire = players.filter(p => !p.isRadiant);
  try {
    dire.sort((p1, p2) => {
      if (p1.position && p2.position) {
        return p1.position.localeCompare(p2.position);
      } else {
        return -1;
      }
    });
  } catch (err) {
    console.log(err);
  }
  return dire;
}