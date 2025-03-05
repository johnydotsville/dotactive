
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