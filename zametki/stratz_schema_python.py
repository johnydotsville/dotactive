import sgqlc.types
import sgqlc.types.datetime


stratz_schema_python = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
class AbilityDispellEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('NO', 'NONE', 'YES', 'YES_STRONG')


class AghanimLabDepthListAscensionAbilitiesEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('AGHSFORT_ASCENSION_INVIS', 'ASCENSION_ARMOR', 'ASCENSION_ARMOR_SAPPING', 'ASCENSION_ATTACK_SPEED', 'ASCENSION_BOMB', 'ASCENSION_BULWARK', 'ASCENSION_CHILLING_TOUCH', 'ASCENSION_CRIT', 'ASCENSION_DAMAGE', 'ASCENSION_DRUNKEN', 'ASCENSION_EMBIGGEN', 'ASCENSION_EXTRA_FAST', 'ASCENSION_FIREFLY', 'ASCENSION_FLICKER', 'ASCENSION_HEAL_SUPPRESSION', 'ASCENSION_MAGIC_IMMUNITY', 'ASCENSION_MAGIC_RESIST', 'ASCENSION_MAGNETIC_FIELD', 'ASCENSION_METEORIC', 'ASCENSION_PLASMA_FIELD', 'ASCENSION_SILENCE', 'ASCENSION_VAMPIRIC', 'ASCENSION_VENGEANCE')


class AghanimLabDepthListEncounterEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ENCOUNTER_AGHANIM', 'ENCOUNTER_ALCHEMIST', 'ENCOUNTER_AQUA_MANOR', 'ENCOUNTER_AZIYOG_CAVERNS', 'ENCOUNTER_BABY_OGRES', 'ENCOUNTER_BAMBOO_GARDEN', 'ENCOUNTER_BANDITS', 'ENCOUNTER_BEACH_TRAPS', 'ENCOUNTER_BEARS_LAIR', 'ENCOUNTER_BIG_OGRES', 'ENCOUNTER_BLOB_DUNGEON', 'ENCOUNTER_BOG_TRAPS', 'ENCOUNTER_BOMBERS', 'ENCOUNTER_BOMB_SQUAD', 'ENCOUNTER_BONUS_CHICKEN', 'ENCOUNTER_BONUS_GALLERY', 'ENCOUNTER_BONUS_HOOKING', 'ENCOUNTER_BONUS_LIVESTOCK', 'ENCOUNTER_BONUS_MANGO_ORCHARD', 'ENCOUNTER_BONUS_SMASH_CHICKENS', 'ENCOUNTER_BOSS_AMOEBA', 'ENCOUNTER_BOSS_ARC_WARDEN', 'ENCOUNTER_BOSS_CLOCKWERK_TINKER', 'ENCOUNTER_BOSS_DARK_WILLOW', 'ENCOUNTER_BOSS_EARTHSHAKER', 'ENCOUNTER_BOSS_RIZZRICK', 'ENCOUNTER_BOSS_STOREGGA', 'ENCOUNTER_BOSS_TIMBERSAW', 'ENCOUNTER_BOSS_VISAGE', 'ENCOUNTER_BOSS_VOID_SPIRIT', 'ENCOUNTER_BOSS_WINTER_WYVERN', 'ENCOUNTER_BREWMASTER', 'ENCOUNTER_BRIDGE_TRAPS', 'ENCOUNTER_BROODMOTHERS', 'ENCOUNTER_BURNING_MESA', 'ENCOUNTER_CANOPY_TRAPS', 'ENCOUNTER_CASTLE_TRAPS', 'ENCOUNTER_CATACOMBS', 'ENCOUNTER_CAVERN_TRAPS', 'ENCOUNTER_CLIFF_PASS', 'ENCOUNTER_COLLAPSED_MINES', 'ENCOUNTER_CRYPT_GATE', 'ENCOUNTER_CRYPT_TRAPS', 'ENCOUNTER_DARK_FOREST', 'ENCOUNTER_DARK_SEER', 'ENCOUNTER_DEEP_TRAPS', 'ENCOUNTER_DEMONIC_WOODS', 'ENCOUNTER_DESERT_OASIS', 'ENCOUNTER_DIRE_SIEGE', 'ENCOUNTER_DRAGON_KNIGHT', 'ENCOUNTER_DROW_RANGER_MINIBOSS', 'ENCOUNTER_DUNGEON_TRAPS', 'ENCOUNTER_EGGS_HOLDOUT', 'ENCOUNTER_ELEMENTAL_TINY', 'ENCOUNTER_EMPTY_BEACH', 'ENCOUNTER_EMPTY_CAVERN', 'ENCOUNTER_ENRAGED_WILDWINGS', 'ENCOUNTER_EVENT_ALCHEMIST_NEUTRAL_ITEMS', 'ENCOUNTER_EVENT_BIG_TINY_GROW', 'ENCOUNTER_EVENT_BREWMASTER_BAR', 'ENCOUNTER_EVENT_DOOM_LIFE_SWAP', 'ENCOUNTER_EVENT_LESHRAC', 'ENCOUNTER_EVENT_LIFE_SHOP', 'ENCOUNTER_EVENT_MINOR_SHARD_SHOP', 'ENCOUNTER_EVENT_MORPHLING_ATTRIBUTE_SHIFT', 'ENCOUNTER_EVENT_NAGA_BOTTLE_RUNE', 'ENCOUNTER_EVENT_NECROPHOS', 'ENCOUNTER_EVENT_OGRE_MAGI_CASINO', 'ENCOUNTER_EVENT_SLARK', 'ENCOUNTER_EVENT_SMALL_TINY_SHRINK', 'ENCOUNTER_EVENT_TINKER_RANGE_RETROFIT', 'ENCOUNTER_EVENT_WARLOCK_LIBRARY', 'ENCOUNTER_EVENT_ZEUS', 'ENCOUNTER_FIRE_ROSHAN', 'ENCOUNTER_FORBIDDEN_PALACE', 'ENCOUNTER_FORSAKEN_PIT', 'ENCOUNTER_FRIGID_PINNACLE', 'ENCOUNTER_FROZEN_RAVINE', 'ENCOUNTER_GAOLERS', 'ENCOUNTER_GAUNTLET', 'ENCOUNTER_GOLEM_GORGE', 'ENCOUNTER_HEDGE_TRAPS', 'ENCOUNTER_HELLBEARS_PORTAL_V_3', 'ENCOUNTER_HELLFIRE_CANYON', 'ENCOUNTER_HIDDEN_COLOSSEUM', 'ENCOUNTER_ICY_POOLS', 'ENCOUNTER_INNER_RING', 'ENCOUNTER_JUNGLE_FIRE_MAZE', 'ENCOUNTER_JUNGLE_HIJINX', 'ENCOUNTER_JUNGLE_TRAPS', 'ENCOUNTER_JUNGLE_TREK', 'ENCOUNTER_KUNKKA_TIDE', 'ENCOUNTER_LEGION_COMMANDER', 'ENCOUNTER_LESHRAC', 'ENCOUNTER_MINING_TRAPS', 'ENCOUNTER_MIRANA', 'ENCOUNTER_MOLE_CAVE', 'ENCOUNTER_MORPHLINGS_B', 'ENCOUNTER_MORTY_TRANSITION', 'ENCOUNTER_MULTIPLICITY', 'ENCOUNTER_MUSHROOM_MINES', 'ENCOUNTER_MUSHROOM_MINES_2021', 'ENCOUNTER_MYSTICAL_TRAPS', 'ENCOUNTER_NAGA_SIREN', 'ENCOUNTER_OGRE_SEALS', 'ENCOUNTER_OUTWORLD', 'ENCOUNTER_PALACE_TRAPS', 'ENCOUNTER_PANGOLIER', 'ENCOUNTER_PENGUINS_TRANSITION', 'ENCOUNTER_PENGUIN_SLEDDING', 'ENCOUNTER_PHOENIX', 'ENCOUNTER_PINECONES', 'ENCOUNTER_PINE_GROVE', 'ENCOUNTER_POLARITY_SWAP', 'ENCOUNTER_PRIMAL_BEAST', 'ENCOUNTER_PRISON_TRAPS', 'ENCOUNTER_PUCKS', 'ENCOUNTER_PUDGE_MINIBOSS', 'ENCOUNTER_PUGNA_NETHER_REACHES', 'ENCOUNTER_PUSH_PULL', 'ENCOUNTER_QUILL_BEASTS', 'ENCOUNTER_REGAL_TRAPS', 'ENCOUNTER_ROCK_GOLEMS', 'ENCOUNTER_RUINOUS_TRAPS', 'ENCOUNTER_SACRED_GROUNDS', 'ENCOUNTER_SALTY_SHORE', 'ENCOUNTER_SHADOW_DEMONS', 'ENCOUNTER_SMASHY_AND_BASHY', 'ENCOUNTER_SNAPFIRE', 'ENCOUNTER_SPECTRES', 'ENCOUNTER_SPLITSVILLE', 'ENCOUNTER_SPOOK_TOWN', 'ENCOUNTER_STONEHALL_CITADEL', 'ENCOUNTER_STOREGGA', 'ENCOUNTER_SWAMP_OF_SADNESS', 'ENCOUNTER_TEMPLE_GARDEN', 'ENCOUNTER_TEMPLE_GUARDIANS', 'ENCOUNTER_TEMPLE_SIEGE', 'ENCOUNTER_TEMPLE_TRAPS', 'ENCOUNTER_THUNDER_MOUNTAIN', 'ENCOUNTER_TOXIC_TERRACE', 'ENCOUNTER_TRANSITION_GATEWAY', 'ENCOUNTER_TROLL_WARLORD', 'ENCOUNTER_TROPICAL_KEEP', 'ENCOUNTER_TUSK_SKELETONS', 'ENCOUNTER_TWILIGHT_MAZE', 'ENCOUNTER_UNDEAD_WOODS', 'ENCOUNTER_VILLAGE_TRAPS', 'ENCOUNTER_WARLOCKS', 'ENCOUNTER_WAVE_BLASTERS', 'ENCOUNTER_WENDIGOES', 'ENCOUNTER_ZEALOT_SCARABS')


class AghanimLabDepthListRewardEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('REWARD_TYPE_EXTRA_LIVES', 'REWARD_TYPE_GOLD', 'REWARD_TYPE_NONE', 'REWARD_TYPE_TREASURE')


class AghanimLabMatchDifficultyEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('APEXMAGE', 'APPRENTICE', 'GRANDMAGUS', 'MAGICIAN', 'SORCERER')


class AghanimLabPlayerBlessingEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ATTACK_RANGE', 'BOSS_TOME', 'BOTTLE_CHARGES', 'BOTTLE_REGEN_DURATION', 'BOTTLE_REGEN_MOVEMENT_SPEED', 'CAST_RANGE', 'DAMAGE_ON_STUNNED', 'DEATH_DETONATION', 'DEBUFF_DURATION_INCREASE', 'ELITE_UPGRADE', 'EXTRA_LIFE', 'LOW_HP_OUTGOING_DAMAGE', 'MELEE_CLEAVE', 'MODIFIER_BLESSING_AGILITY', 'MODIFIER_BLESSING_ARMOR', 'MODIFIER_BLESSING_ATTACK_SPEED', 'MODIFIER_BLESSING_BASE', 'MODIFIER_BLESSING_BOOK_AGILITY', 'MODIFIER_BLESSING_BOOK_INTELLIGENCE', 'MODIFIER_BLESSING_BOOK_STRENGTH', 'MODIFIER_BLESSING_BOTTLE_UPGRADE', 'MODIFIER_BLESSING_DAMAGE_BONUS', 'MODIFIER_BLESSING_DAMAGE_REFLECT', 'MODIFIER_BLESSING_DETONATION', 'MODIFIER_BLESSING_EVASION', 'MODIFIER_BLESSING_HEALTH_BOOST', 'MODIFIER_BLESSING_INTELLIGENCE', 'MODIFIER_BLESSING_LIFE_STEAL', 'MODIFIER_BLESSING_MAGIC_DAMAGE_BONUS', 'MODIFIER_BLESSING_MAGIC_RESIST', 'MODIFIER_BLESSING_MANA_BOOST', 'MODIFIER_BLESSING_MOVEMENT_SPEED', 'MODIFIER_BLESSING_POTION_ARCANIST', 'MODIFIER_BLESSING_POTION_DRAGON', 'MODIFIER_BLESSING_POTION_ECHO_SLAM', 'MODIFIER_BLESSING_POTION_HEALTH', 'MODIFIER_BLESSING_POTION_MANA', 'MODIFIER_BLESSING_POTION_PURIFICATION', 'MODIFIER_BLESSING_POTION_RAVAGE', 'MODIFIER_BLESSING_POTION_SHADOW_WAVE', 'MODIFIER_BLESSING_POTION_TORRENT', 'MODIFIER_BLESSING_REFRESHER_SHARD', 'MODIFIER_BLESSING_RESPAWN_INVULNERABILITY', 'MODIFIER_BLESSING_RESPAWN_TIME_REDUCTION', 'MODIFIER_BLESSING_RESTORE_MANA', 'MODIFIER_BLESSING_SPELL_LIFE_STEAL', 'MODIFIER_BLESSING_STRENGTH', 'ORACLE_SHOP_DISCOUNT', 'POTION_HEALTH', 'POTION_MANA', 'PROJECTILE_SPEED', 'PURIFICATION_POTION', 'REGEN_AROUND_ALLIES', 'RESPAWN_ATTACK_SPEED', 'RESPAWN_HASTE', 'RESPAWN_INVULNERABILITY', 'RESPAWN_TIME_REDUCTION', 'ROSHAN_SHOP_DISCOUNT', 'STARTING_GOLD', 'START_TOME', 'STAT_AGI', 'STAT_DAMAGE', 'STAT_EVASION', 'STAT_HEALTH', 'STAT_INT', 'STAT_MAGIC_RESIST', 'STAT_MANA', 'STAT_SPELL_AMP', 'STAT_STR', 'UPGRADE_REROLL')


class BasicRegionType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('CHINA', 'EUROPE', 'NORTH_AMERICA', 'SEA', 'SOUTH_AMERICA')


Boolean = sgqlc.types.Boolean

class BuildingType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('BARRACKS', 'FORT', 'HEALER', 'OUTPOST', 'TOWER')


class Byte(sgqlc.types.Scalar):
    __schema__ = stratz_schema_python


class Damage(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('MAGICAL', 'PHYSICAL', 'PURE', 'UNKNOWN')


DateTime = sgqlc.types.datetime.DateTime

class Decimal(sgqlc.types.Scalar):
    __schema__ = stratz_schema_python


class FeatEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('DOTA_ACCOUNT_LEVEL', 'HIGH_IMP', 'RAMPAGE', 'WIN_STREAK')


class FilterAghanimLabMatchOrderBy(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('DURATION', 'END_DATE_TIME')


class FilterDireTide2020CustomGameMatchOrderBy(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('CANDY_SCORED', 'END_DATE_TIME')


class FilterHeroWinRequestGroupBy(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ALL', 'HERO_ID', 'HERO_ID_DURATION_MINUTES', 'HERO_ID_POSITION_BRACKET', 'TIME')


class FilterLeaderboardGuildOrderBy(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('BATTLE_PASS_LEVELS', 'ID', 'MEMBER_COUNT', 'POINTS', 'PREVIOUS_WEEK_RANK', 'RANK')


class FilterLeaderboardOrder(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('FIRST', 'LEVEL', 'RECENT')


class FilterMatchGroupOrderByEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('MATCH_COUNT', 'WIN_COUNT')


class FilterOrder(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ASC', 'DESC')


class FilterOrderBy(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ID', 'LAST_MATCH_TIME', 'LAST_MATCH_TIME_THEN_TIER', 'NONE', 'START_DATE_THEN_TIER')


class FilterPlayerTeammateEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('AGAINST', 'WITH')


class FindMatchPlayerGroupBy(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ASSISTS', 'AWARD', 'CLUSTER', 'DATE_DAY', 'DATE_DAY_HERO', 'DEATHS', 'DURATION_MINUTES', 'FACTION', 'GAME_MODE', 'GAME_VERSION', 'GOLD_PER_MINUTE', 'HERO', 'HERO_PERFORMANCE', 'HOUR', 'IS_INTENTIONAL_FEEDING', 'IS_LEAGUE', 'IS_LEAVER', 'IS_PARTY', 'IS_RANDOM', 'IS_SERIES', 'IS_STATS', 'IS_VICTORY', 'KILLS', 'LANE', 'LEAGUE_ID', 'LEVEL', 'LOBBY_TYPE', 'POSITION', 'REGION', 'ROAM_LANE', 'ROLE', 'STEAM_ACCOUNT_ID', 'STEAM_ACCOUNT_ID_AGAINST_TEAM', 'STEAM_ACCOUNT_ID_HERO_ID', 'STEAM_ACCOUNT_ID_HERO_ID_AGAINST_TEAM', 'STEAM_ACCOUNT_ID_HERO_ID_WITH_TEAM', 'STEAM_ACCOUNT_ID_WITH_TEAM', 'TEAM', 'TOTAL_KILLS')


class FindMatchPlayerList(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('AGAINST', 'ALL', 'SINGLE', 'WITH')


class FindMatchPlayerOrderBy(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ASC', 'DESC')


Float = sgqlc.types.Float

class GameModeEnumType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ABILITY_DRAFT', 'ALL_PICK', 'ALL_PICK_RANKED', 'ALL_RANDOM', 'ALL_RANDOM_DEATH_MATCH', 'BALANCED_DRAFT', 'CAPTAINS_DRAFT', 'CAPTAINS_MODE', 'COMPENDIUM_MATCHMAKING', 'CUSTOM', 'EVENT', 'INTRO', 'LEAST_PLAYED', 'MID_ONLY', 'MUTATION', 'NEW_PLAYER_POOL', 'NONE', 'RANDOM_DRAFT', 'REVERSE_CAPTAINS_MODE', 'SINGLE_DRAFT', 'SOLO_MID', 'THE_DIRETIDE', 'THE_GREEVILING', 'TURBO', 'TUTORIAL', 'UNKNOWN')


class GoldReason(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ABADONS', 'BOUNTY', 'BUY_BACK', 'COURIERS', 'COURIERS_2', 'CREEPS', 'DEATH', 'DOOM_DEVOURER', 'HEROES', 'NEUTRAL', 'OTHER', 'ROSHAN', 'SELLS', 'STRUCTURES', 'WARD_DESTRUCTION')


class Guid(sgqlc.types.Scalar):
    __schema__ = stratz_schema_python


class HeroPrimaryAttributeType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('AGI', 'ALL', 'INT', 'STR')


class HeroRoleEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('CARRY', 'DISABLER', 'DURABLE', 'ESCAPE', 'INITIATOR', 'JUNGLER', 'NUKER', 'PUSHER', 'SUPPORT')


ID = sgqlc.types.ID

Int = sgqlc.types.Int

class LaneOutcomeEnums(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('DIRE_STOMP', 'DIRE_VICTORY', 'RADIANT_STOMP', 'RADIANT_VICTORY', 'TIE')


class LanguageEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('BRAZILIAN', 'BULGARIAN', 'CZECH', 'DANISH', 'DUTCH', 'ENGLISH', 'FINNISH', 'FRENCH', 'GERMAN', 'GREEK', 'HUNGARIAN', 'ITALIAN', 'JAPANESE', 'KOREAN', 'KOREANA', 'NORWEGIAN', 'POLISH', 'PORTUGUESE', 'ROMANIAN', 'RUSSIAN', 'SPANISH', 'SWEDISH', 'S_CHINESE', 'THAI', 'TURKISH', 'T_CHINESE', 'UKRAINIAN')


class LeaderboardDivision(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('AMERICAS', 'CHINA', 'EUROPE', 'SE_ASIA')


class LeagueNodeDefaultGroupEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('BEST_OF_FIVE', 'BEST_OF_ONE', 'BEST_OF_THREE', 'BEST_OF_TWO', 'INVALID')


class LeagueNodeGroupTypeEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('BRACKET_DOUBLE_ALL_WINNER', 'BRACKET_DOUBLE_SEED_LOSER', 'BRACKET_SINGLE', 'GSL', 'INVALID', 'ORGANIZATIONAL', 'PLACEMENT', 'ROUND_ROBIN', 'SHOWMATCH', 'SWISS')


class LeagueRegion(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('CHINA', 'CIS', 'EUROPE', 'NA', 'SA', 'SEA', 'UNSET')


class LeagueStage(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('CHAMPIONS_QUALIFERS', 'CLOSED_QUALIFERS', 'GROUP_STAGE', 'MAIN_EVENT', 'OPEN_QUALIFERS')


class LeagueTier(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('AMATEUR', 'DPC_LEAGUE', 'DPC_LEAGUE_FINALS', 'DPC_LEAGUE_QUALIFIER', 'DPC_QUALIFIER', 'INTERNATIONAL', 'MAJOR', 'MINOR', 'PROFESSIONAL', 'UNSET')


class LeaverStatusEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ABANDONED', 'AFK', 'DECLINED_READY_UP', 'DISCONNECTED', 'DISCONNECTED_TOO_LONG', 'FAILED_TO_READY_UP', 'NEVER_CONNECTED', 'NEVER_CONNECTED_TOO_LONG', 'NONE')


class LobbyTypeEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('BATTLE_CUP', 'COOP_VS_BOTS', 'DIRE_TIDE', 'EVENT', 'PRACTICE', 'RANKED', 'SOLO_MID', 'SOLO_QUEUE', 'TEAM_MATCH', 'TOURNAMENT', 'TUTORIAL', 'UNRANKED')


class Long(sgqlc.types.Scalar):
    __schema__ = stratz_schema_python


class MapLocationEnums(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('DIRE_BASE', 'DIRE_FOUNTAIN', 'DIRE_MID_LANE', 'DIRE_OFF_LANE', 'DIRE_SAFE_LANE', 'RADIANT_BASE', 'RADIANT_FOUNTAIN', 'RADIANT_MID_LANE', 'RADIANT_OFF_LANE', 'RADIANT_SAFE_LANE', 'RIVER', 'ROAMING', 'ROSHAN')


class MatchAnalysisOutcomeType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('CLOSE_GAME', 'COMEBACK', 'NONE', 'STOMPED')


class MatchLaneType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('JUNGLE', 'MID_LANE', 'OFF_LANE', 'ROAMING', 'SAFE_LANE', 'UNKNOWN')


class MatchLiveGameState(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('CUSTOM_GAME_SETUP', 'DISCONNECT', 'GAME_IN_PROGRESS', 'HERO_SELECTION', 'INIT', 'LAST', 'PLAYER_DRAFT', 'POST_GAME', 'PRE_GAME', 'SCENARIO_SETUP', 'STRATEGY_TIME', 'TEAM_SHOWCASE', 'WAIT_FOR_MAP_TO_LOAD', 'WAIT_FOR_PLAYERS_TO_LOAD')


class MatchLiveRequestOrderBy(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('AVERAGE_RANK', 'GAME_TIME', 'MATCH_ID', 'SPECTATOR_COUNT')


class MatchPlayerAward(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('MVP', 'NONE', 'TOP_CORE', 'TOP_SUPPORT')


class MatchPlayerPositionType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ALL', 'FILTERED', 'POSITION_1', 'POSITION_2', 'POSITION_3', 'POSITION_4', 'POSITION_5', 'UNKNOWN')


class MatchPlayerRoleType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('CORE', 'HARD_SUPPORT', 'LIGHT_SUPPORT', 'UNKNOWN')


class MatchPlayerTeamPickOrderType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('FIFTH_PICK', 'FIRST_PICK', 'FOURTH_PICK', 'SECOND_PICK', 'THIRD_PICK')


class NeutralItemTierEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('TIER_1', 'TIER_2', 'TIER_3', 'TIER_4', 'TIER_5')


class PatchNoteType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('GENERAL', 'GENERIC', 'HERO', 'ITEM', 'NPC')


class PlayerBattlePassGroupByEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('BRACKET', 'COUNTRY_CODE')


class PlayerBehaviorActivity(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('HIGH', 'INTENSE', 'LOW', 'MEDIUM', 'NONE', 'VERY_HIGH', 'VERY_LOW')


class PlusLetterType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('A', 'B', 'C', 'D', 'F', 'S')


class ROSHDifficultyEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ALPHA', 'EASY', 'EXPERT', 'HARD', 'MEDIUM')


class RankBracket(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ANCIENT', 'ARCHON', 'CRUSADER', 'DIVINE', 'GUARDIAN', 'HERALD', 'IMMORTAL', 'LEGEND', 'UNCALIBRATED')


class RankBracketBasicEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ALL', 'CRUSADER_ARCHON', 'DIVINE_IMMORTAL', 'FILTERED', 'HERALD_GUARDIAN', 'LEGEND_ANCIENT', 'UNCALIBRATED')


class RuneAction(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('BOTTLE', 'PICKUP')


class RuneEnums(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('ARCANE', 'BOUNTY', 'DOUBLE_DAMAGE', 'HASTE', 'ILLUSION', 'INVISIBILITY', 'REGEN', 'SHIELD', 'WATER', 'WISDOM')


class SearchEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('CASTERS', 'GUILDS', 'LEAGUES', 'MATCHES', 'PLAYERS', 'PRO_PLAYERS', 'TEAMS')


class SeriesEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('BEST_OF_FIVE', 'BEST_OF_ONE', 'BEST_OF_THREE', 'BEST_OF_TWO')


class Short(sgqlc.types.Scalar):
    __schema__ = stratz_schema_python


class SpawnActionType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('DESPAWN', 'SPAWN')


class StratzApiType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('DATA_COLLECTOR', 'MULTI_KEY')


class Streak(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('KILL_STREAK', 'MULTI_KILL')


String = sgqlc.types.String

class TableCalculateEnum(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('AVERAGE', 'HIGHEST', 'LOWEST', 'MEDIAN')


class UShort(sgqlc.types.Scalar):
    __schema__ = stratz_schema_python


class WardType(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('OBSERVER', 'SENTRY')


class XpReason(sgqlc.types.Enum):
    __schema__ = stratz_schema_python
    __choices__ = ('CREEPS', 'HEROES', 'OTHER', 'OUTPOSTS', 'ROSHAN', 'TOME_OF_KNOWLEDGE')



########################################################################
# Input Objects
########################################################################
class CaptainJackIdentityProfileUpdateRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('email', 'feed_level', 'email_level', 'daily_email', 'weekly_email', 'monthly_email', 'pro_circuit_feed_level', 'pro_circuit_email_level', 'theme_type', 'language', 'email_hour', 'is_stratz_public')
    email = sgqlc.types.Field(String, graphql_name='email')
    feed_level = sgqlc.types.Field(Byte, graphql_name='feedLevel')
    email_level = sgqlc.types.Field(Byte, graphql_name='emailLevel')
    daily_email = sgqlc.types.Field(Boolean, graphql_name='dailyEmail')
    weekly_email = sgqlc.types.Field(Boolean, graphql_name='weeklyEmail')
    monthly_email = sgqlc.types.Field(Boolean, graphql_name='monthlyEmail')
    pro_circuit_feed_level = sgqlc.types.Field(Byte, graphql_name='proCircuitFeedLevel')
    pro_circuit_email_level = sgqlc.types.Field(Byte, graphql_name='proCircuitEmailLevel')
    theme_type = sgqlc.types.Field(Byte, graphql_name='themeType')
    language = sgqlc.types.Field(LanguageEnum, graphql_name='language')
    email_hour = sgqlc.types.Field(Byte, graphql_name='emailHour')
    is_stratz_public = sgqlc.types.Field(Boolean, graphql_name='isStratzPublic')


class DeleteProSteamAccountRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'name', 'real_name')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    name = sgqlc.types.Field(String, graphql_name='name')
    real_name = sgqlc.types.Field(String, graphql_name='realName')


class FilterAghanimLabHeroCompositionRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('difficulty', 'order_direction', 'take', 'skip')
    difficulty = sgqlc.types.Field(sgqlc.types.non_null(AghanimLabMatchDifficultyEnum), graphql_name='difficulty')
    order_direction = sgqlc.types.Field(FilterOrder, graphql_name='orderDirection')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class FilterAghanimLabMatchRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_ids', 'steam_account_id', 'did_win', 'depth', 'difficulty', 'min_depth', 'region_ids', 'created_before_date_time', 'created_after_date_time', 'order_by', 'order_direction', 'take', 'skip', 'season_id')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    did_win = sgqlc.types.Field(Boolean, graphql_name='didWin')
    depth = sgqlc.types.Field(Byte, graphql_name='depth')
    difficulty = sgqlc.types.Field(AghanimLabMatchDifficultyEnum, graphql_name='difficulty')
    min_depth = sgqlc.types.Field(Byte, graphql_name='minDepth')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='regionIds')
    created_before_date_time = sgqlc.types.Field(Long, graphql_name='createdBeforeDateTime')
    created_after_date_time = sgqlc.types.Field(Long, graphql_name='createdAfterDateTime')
    order_by = sgqlc.types.Field(FilterAghanimLabMatchOrderBy, graphql_name='orderBy')
    order_direction = sgqlc.types.Field(FilterOrder, graphql_name='orderDirection')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')
    season_id = sgqlc.types.Field(Byte, graphql_name='seasonId')


class FilterDireTideCustomMatchRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'order_by', 'order_direction', 'take', 'skip')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    order_by = sgqlc.types.Field(FilterDireTide2020CustomGameMatchOrderBy, graphql_name='orderBy')
    order_direction = sgqlc.types.Field(FilterOrder, graphql_name='orderDirection')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class FilterHeroRampageType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'bracket_basic_ids', 'take', 'after', 'before')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId')
    bracket_basic_ids = sgqlc.types.Field(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds')
    take = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='take')
    after = sgqlc.types.Field(Long, graphql_name='after')
    before = sgqlc.types.Field(Long, graphql_name='before')


class FilterLeaderboardGuildRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('order_by', 'order', 'region', 'is_full', 'is_unlocked', 'min_member_count', 'max_member_count', 'member_count', 'language', 'created_before_date_time', 'created_after_date_time', 'min_required_rank', 'max_required_rank', 'take', 'skip')
    order_by = sgqlc.types.Field(FilterLeaderboardGuildOrderBy, graphql_name='orderBy')
    order = sgqlc.types.Field(FilterOrder, graphql_name='order')
    region = sgqlc.types.Field(Byte, graphql_name='region')
    is_full = sgqlc.types.Field(Boolean, graphql_name='isFull')
    is_unlocked = sgqlc.types.Field(Boolean, graphql_name='isUnlocked')
    min_member_count = sgqlc.types.Field(Byte, graphql_name='minMemberCount')
    max_member_count = sgqlc.types.Field(Byte, graphql_name='maxMemberCount')
    member_count = sgqlc.types.Field(Byte, graphql_name='memberCount')
    language = sgqlc.types.Field(Byte, graphql_name='language')
    created_before_date_time = sgqlc.types.Field(Long, graphql_name='createdBeforeDateTime')
    created_after_date_time = sgqlc.types.Field(Long, graphql_name='createdAfterDateTime')
    min_required_rank = sgqlc.types.Field(Long, graphql_name='minRequiredRank')
    max_required_rank = sgqlc.types.Field(Long, graphql_name='maxRequiredRank')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class FilterLeaderboardHeroRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_ids', 'bracket_ids', 'take', 'skip')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    bracket_ids = sgqlc.types.Field(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds')
    take = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class FilterMatchReplayUploadRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('with_enemy_steam_account', 'with_friend_hero_id', 'with_enemy_hero_id', 'with_friend_banned_hero_id', 'with_enemy_banned_hero_id', 'by_match_id', 'by_match_ids', 'by_match_upload_file_name', 'by_match_upload_uploader_captain_jack_id', 'by_steam_account_id', 'by_steam_account_ids', 'by_hero_id', 'by_league_id', 'by_series_id', 'by_series_ids', 'by_team_id', 'by_game_mode', 'by_lobby_type', 'by_game_version', 'is_league', 'is_validated', 'is_complete', 'is_active', 'is_victory', 'is_radiant', 'filter_position_is_us', 'filter_position', 'filter_position_order', 'is_radiant_first_pick', 'first_pick', 'min_duration', 'max_duration', 'min_game_version_id', 'max_game_version_id', 'start_date_time', 'end_date_time', 'take', 'skip')
    with_enemy_steam_account = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withEnemySteamAccount')
    with_friend_hero_id = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='withFriendHeroId')
    with_enemy_hero_id = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='withEnemyHeroId')
    with_friend_banned_hero_id = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='withFriendBannedHeroId')
    with_enemy_banned_hero_id = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='withEnemyBannedHeroId')
    by_match_id = sgqlc.types.Field(String, graphql_name='byMatchId')
    by_match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='byMatchIds')
    by_match_upload_file_name = sgqlc.types.Field(String, graphql_name='byMatchUploadFileName')
    by_match_upload_uploader_captain_jack_id = sgqlc.types.Field(Guid, graphql_name='byMatchUploadUploaderCaptainJackId')
    by_steam_account_id = sgqlc.types.Field(Long, graphql_name='bySteamAccountId')
    by_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='bySteamAccountIds')
    by_hero_id = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='byHeroId')
    by_league_id = sgqlc.types.Field(Int, graphql_name='byLeagueId')
    by_series_id = sgqlc.types.Field(String, graphql_name='bySeriesId')
    by_series_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='bySeriesIds')
    by_team_id = sgqlc.types.Field(Int, graphql_name='byTeamId')
    by_game_mode = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='byGameMode')
    by_lobby_type = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='byLobbyType')
    by_game_version = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='byGameVersion')
    is_league = sgqlc.types.Field(Boolean, graphql_name='isLeague')
    is_validated = sgqlc.types.Field(Boolean, graphql_name='isValidated')
    is_complete = sgqlc.types.Field(Boolean, graphql_name='isComplete')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    is_victory = sgqlc.types.Field(Boolean, graphql_name='isVictory')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    filter_position_is_us = sgqlc.types.Field(Boolean, graphql_name='filterPositionIsUs')
    filter_position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='filterPosition')
    filter_position_order = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerTeamPickOrderType), graphql_name='filterPositionOrder')
    is_radiant_first_pick = sgqlc.types.Field(Boolean, graphql_name='isRadiantFirstPick')
    first_pick = sgqlc.types.Field(Boolean, graphql_name='firstPick')
    min_duration = sgqlc.types.Field(String, graphql_name='minDuration')
    max_duration = sgqlc.types.Field(String, graphql_name='maxDuration')
    min_game_version_id = sgqlc.types.Field(String, graphql_name='minGameVersionId')
    max_game_version_id = sgqlc.types.Field(String, graphql_name='maxGameVersionId')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class FilterSearchRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('query', 'search_type', 'minimum_rank', 'maximum_rank', 'last_match_played_ago', 'leaderboard_region_ids', 'league_tier_ids', 'team_is_pro', 'take')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')
    search_type = sgqlc.types.Field(sgqlc.types.list_of(SearchEnum), graphql_name='searchType')
    minimum_rank = sgqlc.types.Field(Int, graphql_name='minimumRank')
    maximum_rank = sgqlc.types.Field(Int, graphql_name='maximumRank')
    last_match_played_ago = sgqlc.types.Field(Long, graphql_name='lastMatchPlayedAgo')
    leaderboard_region_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='leaderboardRegionIds')
    league_tier_ids = sgqlc.types.Field(sgqlc.types.list_of(LeagueTier), graphql_name='leagueTierIds')
    team_is_pro = sgqlc.types.Field(Boolean, graphql_name='teamIsPro')
    take = sgqlc.types.Field(Int, graphql_name='take')


class FilterSeasonLeaderboardRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('query', 'leader_board_division', 'hero_id', 'position', 'country_code', 'team_id')
    query = sgqlc.types.Field(String, graphql_name='query')
    leader_board_division = sgqlc.types.Field(LeaderboardDivision, graphql_name='leaderBoardDivision')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    country_code = sgqlc.types.Field(String, graphql_name='countryCode')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')


class FilterSeriesRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('take', 'skip')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class HeroPickBanRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_ids', 'league_id', 'series_id', 'team_id', 'is_parsed', 'start_date_time', 'end_date_time', 'game_mode_ids', 'lobby_type_ids', 'game_version_ids', 'region_ids', 'rank_ids', 'bracket_ids', 'is_stats', 'hero_ids', 'lane_ids', 'role_ids', 'position_ids', 'award_ids', 'is_party', 'has_award', 'min_game_version_id', 'max_game_version_id', 'after', 'before')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    is_parsed = sgqlc.types.Field(Boolean, graphql_name='isParsed')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    game_version_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameVersionIds')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='regionIds')
    rank_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rankIds')
    bracket_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='bracketIds')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    lane_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='laneIds')
    role_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roleIds')
    position_ids = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds')
    award_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='awardIds')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    has_award = sgqlc.types.Field(Boolean, graphql_name='hasAward')
    min_game_version_id = sgqlc.types.Field(Int, graphql_name='minGameVersionId')
    max_game_version_id = sgqlc.types.Field(Int, graphql_name='maxGameVersionId')
    after = sgqlc.types.Field(Long, graphql_name='after')
    before = sgqlc.types.Field(Long, graphql_name='before')


class ImpGeneratorPlayerEventRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'kills', 'deaths', 'assists', 'cs', 'dn', 'level', 'physical_damage', 'magical_damage', 'pure_damage', 'damage_received', 'healing_allies', 'rune_power', 'neutrals')
    time = sgqlc.types.Field(sgqlc.types.non_null(Byte), graphql_name='time')
    kills = sgqlc.types.Field(sgqlc.types.non_null(UShort), graphql_name='kills')
    deaths = sgqlc.types.Field(sgqlc.types.non_null(UShort), graphql_name='deaths')
    assists = sgqlc.types.Field(sgqlc.types.non_null(UShort), graphql_name='assists')
    cs = sgqlc.types.Field(sgqlc.types.non_null(UShort), graphql_name='cs')
    dn = sgqlc.types.Field(sgqlc.types.non_null(UShort), graphql_name='dn')
    level = sgqlc.types.Field(sgqlc.types.non_null(Byte), graphql_name='level')
    physical_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='physicalDamage')
    magical_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='magicalDamage')
    pure_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pureDamage')
    damage_received = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='damageReceived')
    healing_allies = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='healingAllies')
    rune_power = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='runePower')
    neutrals = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='neutrals')


class ImpGeneratorPlayerRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'bracket', 'position', 'events')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId')
    bracket = sgqlc.types.Field(sgqlc.types.non_null(RankBracket), graphql_name='bracket')
    position = sgqlc.types.Field(sgqlc.types.non_null(MatchPlayerPositionType), graphql_name='position')
    events = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ImpGeneratorPlayerEventRequestType)), graphql_name='events')


class ImpGeneratorRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('bans', 'players', 'is_turbo')
    bans = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Short)), graphql_name='bans')
    players = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(ImpGeneratorPlayerRequestType)), graphql_name='players')
    is_turbo = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isTurbo')


class ImportPickBanType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('player_slot', 'is_pick', 'hero_id', 'time', 'is_radiant', 'order', 'was_banned_successfully')
    player_slot = sgqlc.types.Field(Byte, graphql_name='playerSlot')
    is_pick = sgqlc.types.Field(Boolean, graphql_name='isPick')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    time = sgqlc.types.Field(Byte, graphql_name='time')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    order = sgqlc.types.Field(Byte, graphql_name='order')
    was_banned_successfully = sgqlc.types.Field(Boolean, graphql_name='wasBannedSuccessfully')


class LeagueMatchesRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'match_ids', 'series_id', 'team_id', 'is_parsed', 'start_date_time', 'end_date_time', 'game_mode_ids', 'lobby_type_ids', 'game_version_ids', 'region_ids', 'rank_ids', 'is_stats', 'hero_ids', 'lane_ids', 'role_ids', 'position_ids', 'award_ids', 'is_party', 'has_award', 'league_stage_type_ids', 'with_friend_steam_account_ids', 'with_friend_hero_ids', 'take', 'skip')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    is_parsed = sgqlc.types.Field(Boolean, graphql_name='isParsed')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    game_version_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameVersionIds')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='regionIds')
    rank_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rankIds')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    lane_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='laneIds')
    role_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roleIds')
    position_ids = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds')
    award_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='awardIds')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    has_award = sgqlc.types.Field(Boolean, graphql_name='hasAward')
    league_stage_type_ids = sgqlc.types.Field(sgqlc.types.list_of(LeagueStage), graphql_name='leagueStageTypeIds')
    with_friend_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withFriendSteamAccountIds')
    with_friend_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withFriendHeroIds')
    take = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='take')
    skip = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='skip')


class LeagueRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('league_id', 'league_ids', 'tiers', 'require_image', 'require_prize_pool', 'require_start_and_end_dates', 'has_live_matches', 'league_ended', 'is_future_league', 'start_date_time', 'end_date_time', 'between_start_date_time', 'between_end_date_time', 'order_by', 'take', 'skip')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    league_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='leagueIds')
    tiers = sgqlc.types.Field(sgqlc.types.list_of(LeagueTier), graphql_name='tiers')
    require_image = sgqlc.types.Field(Boolean, graphql_name='requireImage')
    require_prize_pool = sgqlc.types.Field(Boolean, graphql_name='requirePrizePool')
    require_start_and_end_dates = sgqlc.types.Field(Boolean, graphql_name='requireStartAndEndDates')
    has_live_matches = sgqlc.types.Field(Boolean, graphql_name='hasLiveMatches')
    league_ended = sgqlc.types.Field(Boolean, graphql_name='leagueEnded')
    is_future_league = sgqlc.types.Field(Boolean, graphql_name='isFutureLeague')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    between_start_date_time = sgqlc.types.Field(Long, graphql_name='betweenStartDateTime')
    between_end_date_time = sgqlc.types.Field(Long, graphql_name='betweenEndDateTime')
    order_by = sgqlc.types.Field(FilterOrderBy, graphql_name='orderBy')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class MatchLiveRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'league_id', 'is_parsing', 'is_completed', 'league_ids', 'game_states', 'tiers', 'last_playback_event_only', 'order_by', 'is_league', 'take', 'skip')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    is_parsing = sgqlc.types.Field(Boolean, graphql_name='isParsing')
    is_completed = sgqlc.types.Field(Boolean, graphql_name='isCompleted')
    league_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='leagueIds')
    game_states = sgqlc.types.Field(sgqlc.types.list_of(MatchLiveGameState), graphql_name='gameStates')
    tiers = sgqlc.types.Field(sgqlc.types.list_of(LeagueTier), graphql_name='tiers')
    last_playback_event_only = sgqlc.types.Field(Boolean, graphql_name='lastPlaybackEventOnly')
    order_by = sgqlc.types.Field(MatchLiveRequestOrderBy, graphql_name='orderBy')
    is_league = sgqlc.types.Field(Boolean, graphql_name='isLeague')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class MergeProSteamAccountRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'name', 'real_name')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    name = sgqlc.types.Field(String, graphql_name='name')
    real_name = sgqlc.types.Field(String, graphql_name='realName')


class PlayerBreakdownRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_ids', 'league_id', 'series_id', 'team_id', 'is_parsed', 'is_league', 'is_team', 'min_duration', 'max_duration', 'start_date_time', 'end_date_time', 'game_mode_ids', 'lobby_type_ids', 'game_version_ids', 'min_game_version_id', 'max_game_version_id', 'region_ids', 'rank_ids', 'is_stats', 'hero_ids', 'lane_ids', 'role_ids', 'position_ids', 'award_ids', 'is_party', 'is_radiant', 'party_counts', 'has_award', 'with_friend_steam_account_ids', 'with_friend_hero_ids')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    is_parsed = sgqlc.types.Field(Boolean, graphql_name='isParsed')
    is_league = sgqlc.types.Field(Boolean, graphql_name='isLeague')
    is_team = sgqlc.types.Field(Boolean, graphql_name='isTeam')
    min_duration = sgqlc.types.Field(Int, graphql_name='minDuration')
    max_duration = sgqlc.types.Field(Int, graphql_name='maxDuration')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    game_version_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameVersionIds')
    min_game_version_id = sgqlc.types.Field(Int, graphql_name='minGameVersionId')
    max_game_version_id = sgqlc.types.Field(Int, graphql_name='maxGameVersionId')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='regionIds')
    rank_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rankIds')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    lane_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='laneIds')
    role_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roleIds')
    position_ids = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds')
    award_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='awardIds')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    party_counts = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='partyCounts')
    has_award = sgqlc.types.Field(Boolean, graphql_name='hasAward')
    with_friend_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withFriendSteamAccountIds')
    with_friend_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withFriendHeroIds')


class PlayerHeroPerformanceMatchesRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_group_order_by', 'order_by', 'match_ids', 'league_id', 'league_ids', 'series_id', 'team_id', 'is_parsed', 'is_league', 'is_team', 'min_duration', 'max_duration', 'start_date_time', 'end_date_time', 'game_mode_ids', 'lobby_type_ids', 'game_version_ids', 'min_game_version_id', 'max_game_version_id', 'region_ids', 'rank_ids', 'is_stats', 'hero_ids', 'lane_ids', 'role_ids', 'position_ids', 'award_ids', 'is_party', 'is_radiant', 'party_counts', 'has_award', 'with_friend_steam_account_ids', 'with_enemy_steam_account_ids', 'with_friend_hero_ids', 'with_enemy_hero_ids', 'take', 'skip')
    match_group_order_by = sgqlc.types.Field(FilterMatchGroupOrderByEnum, graphql_name='matchGroupOrderBy')
    order_by = sgqlc.types.Field(FindMatchPlayerOrderBy, graphql_name='orderBy')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    league_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='leagueIds')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    is_parsed = sgqlc.types.Field(Boolean, graphql_name='isParsed')
    is_league = sgqlc.types.Field(Boolean, graphql_name='isLeague')
    is_team = sgqlc.types.Field(Boolean, graphql_name='isTeam')
    min_duration = sgqlc.types.Field(Int, graphql_name='minDuration')
    max_duration = sgqlc.types.Field(Int, graphql_name='maxDuration')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    game_version_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameVersionIds')
    min_game_version_id = sgqlc.types.Field(Int, graphql_name='minGameVersionId')
    max_game_version_id = sgqlc.types.Field(Int, graphql_name='maxGameVersionId')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='regionIds')
    rank_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rankIds')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    lane_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='laneIds')
    role_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roleIds')
    position_ids = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds')
    award_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='awardIds')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    party_counts = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='partyCounts')
    has_award = sgqlc.types.Field(Boolean, graphql_name='hasAward')
    with_friend_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withFriendSteamAccountIds')
    with_enemy_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withEnemySteamAccountIds')
    with_friend_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withFriendHeroIds')
    with_enemy_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withEnemyHeroIds')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class PlayerHeroesPerformanceMatchesRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_ids', 'league_id', 'series_id', 'team_id', 'is_parsed', 'is_league', 'is_team', 'min_duration', 'max_duration', 'start_date_time', 'end_date_time', 'game_mode_ids', 'lobby_type_ids', 'game_version_ids', 'min_game_version_id', 'max_game_version_id', 'region_ids', 'rank_ids', 'is_stats', 'hero_ids', 'lane_ids', 'role_ids', 'position_ids', 'award_ids', 'is_party', 'is_radiant', 'party_counts', 'has_award', 'with_friend_steam_account_ids', 'with_enemy_steam_account_ids', 'with_friend_hero_ids', 'with_enemy_hero_ids', 'take', 'skip')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    is_parsed = sgqlc.types.Field(Boolean, graphql_name='isParsed')
    is_league = sgqlc.types.Field(Boolean, graphql_name='isLeague')
    is_team = sgqlc.types.Field(Boolean, graphql_name='isTeam')
    min_duration = sgqlc.types.Field(Int, graphql_name='minDuration')
    max_duration = sgqlc.types.Field(Int, graphql_name='maxDuration')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    game_version_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameVersionIds')
    min_game_version_id = sgqlc.types.Field(Int, graphql_name='minGameVersionId')
    max_game_version_id = sgqlc.types.Field(Int, graphql_name='maxGameVersionId')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='regionIds')
    rank_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rankIds')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    lane_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='laneIds')
    role_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roleIds')
    position_ids = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds')
    award_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='awardIds')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    party_counts = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='partyCounts')
    has_award = sgqlc.types.Field(Boolean, graphql_name='hasAward')
    with_friend_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withFriendSteamAccountIds')
    with_enemy_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withEnemySteamAccountIds')
    with_friend_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withFriendHeroIds')
    with_enemy_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withEnemyHeroIds')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class PlayerMatchesGroupByRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('player_list', 'group_by', 'match_ids', 'league_id', 'league_ids', 'series_id', 'team_id', 'is_parsed', 'start_date_time', 'end_date_time', 'is_league', 'game_mode_ids', 'lobby_type_ids', 'game_version_ids', 'region_ids', 'rank_ids', 'bracket_ids', 'is_stats', 'hero_ids', 'lane_ids', 'role_ids', 'position_ids', 'award_ids', 'is_party', 'is_victory', 'is_radiant', 'has_award', 'with_friend_steam_account_ids', 'with_enemy_steam_account_ids', 'with_friend_hero_ids', 'with_enemy_hero_ids', 'min_game_version_id', 'max_game_version_id', 'take', 'skip')
    player_list = sgqlc.types.Field(sgqlc.types.non_null(FindMatchPlayerList), graphql_name='playerList')
    group_by = sgqlc.types.Field(sgqlc.types.non_null(FindMatchPlayerGroupBy), graphql_name='groupBy')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    league_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='leagueIds')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    is_parsed = sgqlc.types.Field(Boolean, graphql_name='isParsed')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    is_league = sgqlc.types.Field(Boolean, graphql_name='isLeague')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    game_version_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameVersionIds')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='regionIds')
    rank_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rankIds')
    bracket_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='bracketIds')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    lane_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='laneIds')
    role_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roleIds')
    position_ids = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds')
    award_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='awardIds')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    is_victory = sgqlc.types.Field(Boolean, graphql_name='isVictory')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    has_award = sgqlc.types.Field(Boolean, graphql_name='hasAward')
    with_friend_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withFriendSteamAccountIds')
    with_enemy_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withEnemySteamAccountIds')
    with_friend_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withFriendHeroIds')
    with_enemy_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withEnemyHeroIds')
    min_game_version_id = sgqlc.types.Field(Int, graphql_name='minGameVersionId')
    max_game_version_id = sgqlc.types.Field(Int, graphql_name='maxGameVersionId')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class PlayerMatchesRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_ids', 'league_id', 'league_ids', 'series_id', 'team_id', 'team_id_steam_account', 'is_parsed', 'start_date_time', 'end_date_time', 'game_mode_ids', 'lobby_type_ids', 'game_version_ids', 'region_ids', 'rank_ids', 'bracket_ids', 'is_stats', 'hero_ids', 'lane_ids', 'role_ids', 'position_ids', 'award_ids', 'is_party', 'has_award', 'with_friend_steam_account_ids', 'with_enemy_steam_account_ids', 'with_friend_hero_ids', 'with_enemy_hero_ids', 'is_victory', 'is_radiant', 'min_game_version_id', 'max_game_version_id', 'min_imp', 'max_imp', 'player_list', 'take', 'skip', 'after', 'before', 'order_by')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    league_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='leagueIds')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    team_id_steam_account = sgqlc.types.Field(Int, graphql_name='teamIdSteamAccount')
    is_parsed = sgqlc.types.Field(Boolean, graphql_name='isParsed')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    game_version_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameVersionIds')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='regionIds')
    rank_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rankIds')
    bracket_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='bracketIds')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    lane_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='laneIds')
    role_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roleIds')
    position_ids = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds')
    award_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='awardIds')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    has_award = sgqlc.types.Field(Boolean, graphql_name='hasAward')
    with_friend_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withFriendSteamAccountIds')
    with_enemy_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withEnemySteamAccountIds')
    with_friend_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withFriendHeroIds')
    with_enemy_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withEnemyHeroIds')
    is_victory = sgqlc.types.Field(Boolean, graphql_name='isVictory')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    min_game_version_id = sgqlc.types.Field(Int, graphql_name='minGameVersionId')
    max_game_version_id = sgqlc.types.Field(Int, graphql_name='maxGameVersionId')
    min_imp = sgqlc.types.Field(Int, graphql_name='minImp')
    max_imp = sgqlc.types.Field(Int, graphql_name='maxImp')
    player_list = sgqlc.types.Field(FindMatchPlayerList, graphql_name='playerList')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')
    after = sgqlc.types.Field(Long, graphql_name='after')
    before = sgqlc.types.Field(Long, graphql_name='before')
    order_by = sgqlc.types.Field(FindMatchPlayerOrderBy, graphql_name='orderBy')


class PlayerPerformanceMatchesRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_ids', 'league_id', 'series_id', 'team_id', 'is_parsed', 'is_league', 'is_team', 'start_date_time', 'end_date_time', 'game_mode_ids', 'lobby_type_ids', 'game_version_ids', 'tier', 'region_ids', 'rank_ids', 'is_stats', 'lane_ids', 'role_ids', 'position_ids', 'award_ids', 'is_party', 'has_award', 'is_victory', 'is_radiant', 'with_friend_steam_account_ids', 'with_friend_hero_ids')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    is_parsed = sgqlc.types.Field(Boolean, graphql_name='isParsed')
    is_league = sgqlc.types.Field(Boolean, graphql_name='isLeague')
    is_team = sgqlc.types.Field(Boolean, graphql_name='isTeam')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    game_version_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameVersionIds')
    tier = sgqlc.types.Field(LeagueTier, graphql_name='tier')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='regionIds')
    rank_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rankIds')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    lane_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='laneIds')
    role_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roleIds')
    position_ids = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds')
    award_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='awardIds')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    has_award = sgqlc.types.Field(Boolean, graphql_name='hasAward')
    is_victory = sgqlc.types.Field(Boolean, graphql_name='isVictory')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    with_friend_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withFriendSteamAccountIds')
    with_friend_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withFriendHeroIds')


class PlayerTeammatesGroupByRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('player_teammate_sort', 'match_group_order_by', 'order_by', 'match_ids', 'league_id', 'league_ids', 'series_id', 'team_id', 'team_id_steam_account', 'is_parsed', 'start_date_time', 'end_date_time', 'game_mode_ids', 'lobby_type_ids', 'game_version_ids', 'region_ids', 'rank_ids', 'bracket_ids', 'is_stats', 'hero_ids', 'lane_ids', 'role_ids', 'position_ids', 'award_ids', 'is_party', 'has_award', 'with_friend_steam_account_ids', 'with_friend_hero_ids', 'min_game_version_id', 'max_game_version_id', 'match_limit_min', 'match_limit_max', 'only_casters', 'only_pros', 'take', 'skip')
    player_teammate_sort = sgqlc.types.Field(sgqlc.types.non_null(FilterPlayerTeammateEnum), graphql_name='playerTeammateSort')
    match_group_order_by = sgqlc.types.Field(sgqlc.types.non_null(FilterMatchGroupOrderByEnum), graphql_name='matchGroupOrderBy')
    order_by = sgqlc.types.Field(FindMatchPlayerOrderBy, graphql_name='orderBy')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    league_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='leagueIds')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    team_id_steam_account = sgqlc.types.Field(Int, graphql_name='teamIdSteamAccount')
    is_parsed = sgqlc.types.Field(Boolean, graphql_name='isParsed')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    game_version_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameVersionIds')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='regionIds')
    rank_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rankIds')
    bracket_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='bracketIds')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    lane_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='laneIds')
    role_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roleIds')
    position_ids = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds')
    award_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='awardIds')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    has_award = sgqlc.types.Field(Boolean, graphql_name='hasAward')
    with_friend_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withFriendSteamAccountIds')
    with_friend_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withFriendHeroIds')
    min_game_version_id = sgqlc.types.Field(Int, graphql_name='minGameVersionId')
    max_game_version_id = sgqlc.types.Field(Int, graphql_name='maxGameVersionId')
    match_limit_min = sgqlc.types.Field(Int, graphql_name='matchLimitMin')
    match_limit_max = sgqlc.types.Field(Int, graphql_name='matchLimitMax')
    only_casters = sgqlc.types.Field(Boolean, graphql_name='onlyCasters')
    only_pros = sgqlc.types.Field(Boolean, graphql_name='onlyPros')
    take = sgqlc.types.Field(Int, graphql_name='take')
    skip = sgqlc.types.Field(Int, graphql_name='skip')


class PlusDraftMissingLetterRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('bans', 'game_mode', 'players', 'game_version_id')
    bans = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='bans')
    game_mode = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gameMode')
    players = sgqlc.types.Field(sgqlc.types.list_of('PlusDraftPlayerRequestType'), graphql_name='players')
    game_version_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='gameVersionId')


class PlusDraftPlayerRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'slot', 'hero_id', 'rank', 'position')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    slot = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='slot')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    rank = sgqlc.types.Field(Byte, graphql_name='rank')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')


class PlusDraftRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'bans', 'game_mode', 'players', 'game_version_id')
    match_id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='matchId')
    bans = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='bans')
    game_mode = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gameMode')
    players = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(PlusDraftPlayerRequestType)), graphql_name='players')
    game_version_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='gameVersionId')


class PlusPlayerHoverRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_ids', 'game_mode_ids', 'lobby_type_ids', 'take', 'should_radiant_win')
    steam_account_ids = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(Long)), graphql_name='steamAccountIds')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    take = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='take')
    should_radiant_win = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='shouldRadiantWin')


class ROSHMatchesRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('start_date_time', 'end_date_time', 'is_user_action_first', 'is_radiant', 'bracket_ids', 'is_completed')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    is_user_action_first = sgqlc.types.Field(Boolean, graphql_name='isUserActionFirst')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    bracket_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='bracketIds')
    is_completed = sgqlc.types.Field(Boolean, graphql_name='isCompleted')


class TeamMatchesRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'match_ids', 'league_id', 'series_id', 'is_parsed', 'start_date_time', 'end_date_time', 'game_mode_ids', 'lobby_type_ids', 'game_version_ids', 'region_ids', 'rank_ids', 'is_stats', 'hero_ids', 'lane_ids', 'role_ids', 'position_ids', 'award_ids', 'is_party', 'has_award', 'with_friend_steam_account_ids', 'with_friend_hero_ids', 'player_list', 'take', 'skip')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    match_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='matchIds')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    is_parsed = sgqlc.types.Field(Boolean, graphql_name='isParsed')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    game_mode_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='gameModeIds')
    lobby_type_ids = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='lobbyTypeIds')
    game_version_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='gameVersionIds')
    region_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='regionIds')
    rank_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='rankIds')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    lane_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='laneIds')
    role_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roleIds')
    position_ids = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds')
    award_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='awardIds')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    has_award = sgqlc.types.Field(Boolean, graphql_name='hasAward')
    with_friend_steam_account_ids = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='withFriendSteamAccountIds')
    with_friend_hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='withFriendHeroIds')
    player_list = sgqlc.types.Field(FindMatchPlayerList, graphql_name='playerList')
    take = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='take')
    skip = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='skip')


class UpdateFollowerRequestType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('feed_level', 'email_level', 'daily_email', 'weekly_email', 'monthly_email', 'override_all_users')
    feed_level = sgqlc.types.Field(Byte, graphql_name='feedLevel')
    email_level = sgqlc.types.Field(Byte, graphql_name='emailLevel')
    daily_email = sgqlc.types.Field(Boolean, graphql_name='dailyEmail')
    weekly_email = sgqlc.types.Field(Boolean, graphql_name='weeklyEmail')
    monthly_email = sgqlc.types.Field(Boolean, graphql_name='monthlyEmail')
    override_all_users = sgqlc.types.Field(Boolean, graphql_name='overrideAllUsers')


class UpdateMatchReplayMatchUploadPlayerObjectType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'position')
    steam_account_id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='steamAccountId')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')


class UpdateMatchReplayUploadObjectType(sgqlc.types.Input):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_replay_upload_team_id', 'match_id', 'league_id', 'radiant_team_id', 'dire_team_id', 'is_active', 'notes', 'players')
    match_replay_upload_team_id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId')
    match_id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='matchId')
    league_id = sgqlc.types.Field(Long, graphql_name='leagueId')
    radiant_team_id = sgqlc.types.Field(Long, graphql_name='radiantTeamId')
    dire_team_id = sgqlc.types.Field(Long, graphql_name='direTeamId')
    is_active = sgqlc.types.Field(Boolean, graphql_name='isActive')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    players = sgqlc.types.Field(sgqlc.types.list_of(UpdateMatchReplayMatchUploadPlayerObjectType), graphql_name='players')



########################################################################
# Output Objects and Interfaces
########################################################################
class AbilityActiveListType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'ability0', 'ability1', 'ability2', 'ability3', 'ability4', 'ability5', 'ability6', 'ability7')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    ability0 = sgqlc.types.Field(Short, graphql_name='ability0')
    ability1 = sgqlc.types.Field(Short, graphql_name='ability1')
    ability2 = sgqlc.types.Field(Short, graphql_name='ability2')
    ability3 = sgqlc.types.Field(Short, graphql_name='ability3')
    ability4 = sgqlc.types.Field(Short, graphql_name='ability4')
    ability5 = sgqlc.types.Field(Short, graphql_name='ability5')
    ability6 = sgqlc.types.Field(Short, graphql_name='ability6')
    ability7 = sgqlc.types.Field(Short, graphql_name='ability7')


class AbilityAttributeType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('name', 'value', 'linked_special_bonus_ability_id', 'requires_scepter')
    name = sgqlc.types.Field(String, graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')
    linked_special_bonus_ability_id = sgqlc.types.Field(Short, graphql_name='linkedSpecialBonusAbilityId')
    requires_scepter = sgqlc.types.Field(Boolean, graphql_name='requiresScepter')


class AbilityCustomGameLanguageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('display_name', 'description')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    description = sgqlc.types.Field(String, graphql_name='description')


class AbilityCustomGameType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'ability_name', 'language')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    ability_name = sgqlc.types.Field(String, graphql_name='abilityName')
    language = sgqlc.types.Field(AbilityCustomGameLanguageType, graphql_name='language')


class AbilityLanguageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('display_name', 'description', 'attributes', 'lore', 'aghanim_description', 'shard_description', 'notes')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    description = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='description')
    attributes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='attributes')
    lore = sgqlc.types.Field(String, graphql_name='lore')
    aghanim_description = sgqlc.types.Field(String, graphql_name='aghanimDescription')
    shard_description = sgqlc.types.Field(String, graphql_name='shardDescription')
    notes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='notes')


class AbilityLearnEventsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'ability_id', 'level_obtained', 'level', 'is_ultimate', 'is_talent', 'is_max_level')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    ability_id = sgqlc.types.Field(Short, graphql_name='abilityId')
    level_obtained = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='levelObtained')
    level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='level')
    is_ultimate = sgqlc.types.Field(Boolean, graphql_name='isUltimate')
    is_talent = sgqlc.types.Field(Boolean, graphql_name='isTalent')
    is_max_level = sgqlc.types.Field(Boolean, graphql_name='isMaxLevel')


class AbilityStatType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('ability_id', 'type', 'behavior', 'unit_target_type', 'unit_target_team', 'unit_target_flags', 'unit_damage_type', 'spell_immunity', 'modifier_support_value', 'modifier_support_bonus', 'is_on_castbar', 'is_on_learnbar', 'fight_recap_level', 'is_granted_by_scepter', 'has_scepter_upgrade', 'max_level', 'levels_between_upgrades', 'required_level', 'hot_key_override', 'display_additional_heroes', 'cast_range', 'cast_range_buffer', 'cast_point', 'channel_time', 'cooldown', 'damage', 'mana_cost', 'is_ultimate', 'duration', 'charges', 'charge_restore_time', 'has_shard_upgrade', 'is_granted_by_shard', 'dispellable', 'linked_ability_id', 'is_innate')
    ability_id = sgqlc.types.Field(Short, graphql_name='abilityId')
    type = sgqlc.types.Field(Int, graphql_name='type')
    behavior = sgqlc.types.Field(Long, graphql_name='behavior')
    unit_target_type = sgqlc.types.Field(Long, graphql_name='unitTargetType')
    unit_target_team = sgqlc.types.Field(Int, graphql_name='unitTargetTeam')
    unit_target_flags = sgqlc.types.Field(Long, graphql_name='unitTargetFlags')
    unit_damage_type = sgqlc.types.Field(Int, graphql_name='unitDamageType')
    spell_immunity = sgqlc.types.Field(Int, graphql_name='spellImmunity')
    modifier_support_value = sgqlc.types.Field(Float, graphql_name='modifierSupportValue')
    modifier_support_bonus = sgqlc.types.Field(Short, graphql_name='modifierSupportBonus')
    is_on_castbar = sgqlc.types.Field(Boolean, graphql_name='isOnCastbar')
    is_on_learnbar = sgqlc.types.Field(Boolean, graphql_name='isOnLearnbar')
    fight_recap_level = sgqlc.types.Field(Short, graphql_name='fightRecapLevel')
    is_granted_by_scepter = sgqlc.types.Field(Boolean, graphql_name='isGrantedByScepter')
    has_scepter_upgrade = sgqlc.types.Field(Boolean, graphql_name='hasScepterUpgrade')
    max_level = sgqlc.types.Field(Byte, graphql_name='maxLevel')
    levels_between_upgrades = sgqlc.types.Field(Byte, graphql_name='levelsBetweenUpgrades')
    required_level = sgqlc.types.Field(Byte, graphql_name='requiredLevel')
    hot_key_override = sgqlc.types.Field(String, graphql_name='hotKeyOverride')
    display_additional_heroes = sgqlc.types.Field(Boolean, graphql_name='displayAdditionalHeroes')
    cast_range = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='castRange')
    cast_range_buffer = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='castRangeBuffer')
    cast_point = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='castPoint')
    channel_time = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='channelTime')
    cooldown = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='cooldown')
    damage = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='damage')
    mana_cost = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='manaCost')
    is_ultimate = sgqlc.types.Field(Boolean, graphql_name='isUltimate')
    duration = sgqlc.types.Field(String, graphql_name='duration')
    charges = sgqlc.types.Field(String, graphql_name='charges')
    charge_restore_time = sgqlc.types.Field(String, graphql_name='chargeRestoreTime')
    has_shard_upgrade = sgqlc.types.Field(Boolean, graphql_name='hasShardUpgrade')
    is_granted_by_shard = sgqlc.types.Field(Boolean, graphql_name='isGrantedByShard')
    dispellable = sgqlc.types.Field(AbilityDispellEnum, graphql_name='dispellable')
    linked_ability_id = sgqlc.types.Field(Short, graphql_name='linkedAbilityId')
    is_innate = sgqlc.types.Field(Boolean, graphql_name='isInnate')


class AbilityType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'uri', 'language', 'stat', 'attributes', 'is_talent')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    uri = sgqlc.types.Field(String, graphql_name='uri')
    language = sgqlc.types.Field(AbilityLanguageType, graphql_name='language')
    stat = sgqlc.types.Field(AbilityStatType, graphql_name='stat')
    attributes = sgqlc.types.Field(sgqlc.types.list_of(AbilityAttributeType), graphql_name='attributes')
    is_talent = sgqlc.types.Field(Boolean, graphql_name='isTalent')


class AbilityUsedEventsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'ability_id', 'attacker', 'target')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    ability_id = sgqlc.types.Field(Short, graphql_name='abilityId')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')
    target = sgqlc.types.Field(Short, graphql_name='target')


class AdminMutation(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('merge_pro_steam_account', 'delete_pro_steam_account')
    merge_pro_steam_account = sgqlc.types.Field(Boolean, graphql_name='mergeProSteamAccount', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(MergeProSteamAccountRequestType)), graphql_name='request', default=None)),
))
    )
    delete_pro_steam_account = sgqlc.types.Field(Boolean, graphql_name='deleteProSteamAccount', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(DeleteProSteamAccountRequestType), graphql_name='request', default=None)),
))
    )


class AdminQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('api_memory_report',)
    api_memory_report = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='apiMemoryReport')


class AghanimLabDepthListAscensionAbilitiesObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('type', 'ability_id', 'modifier_id')
    type = sgqlc.types.Field(AghanimLabDepthListAscensionAbilitiesEnum, graphql_name='type')
    ability_id = sgqlc.types.Field(Short, graphql_name='abilityId')
    modifier_id = sgqlc.types.Field(Short, graphql_name='modifierId')


class AghanimLabHeroAbilityType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('difficulty', 'hero_id', 'custom_ability_id', 'match_count', 'win_count', 'pick_count')
    difficulty = sgqlc.types.Field(AghanimLabMatchDifficultyEnum, graphql_name='difficulty')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    custom_ability_id = sgqlc.types.Field(Short, graphql_name='customAbilityId')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    pick_count = sgqlc.types.Field(Int, graphql_name='pickCount')


class AghanimLabHeroCompositionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('difficulty', 'hero_id1', 'hero_id2', 'hero_id3', 'hero_id4', 'match_count', 'win_count', 'duration', 'wilson_score')
    difficulty = sgqlc.types.Field(AghanimLabMatchDifficultyEnum, graphql_name='difficulty')
    hero_id1 = sgqlc.types.Field(Short, graphql_name='heroId1')
    hero_id2 = sgqlc.types.Field(Short, graphql_name='heroId2')
    hero_id3 = sgqlc.types.Field(Short, graphql_name='heroId3')
    hero_id4 = sgqlc.types.Field(Short, graphql_name='heroId4')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    duration = sgqlc.types.Field(Int, graphql_name='duration')
    wilson_score = sgqlc.types.Field(Decimal, graphql_name='wilsonScore')


class AghanimLabHeroWinRateType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('difficulty', 'hero_id', 'match_count', 'win_count')
    difficulty = sgqlc.types.Field(AghanimLabMatchDifficultyEnum, graphql_name='difficulty')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')


class AghanimLabMatchDepthListType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('selected_elite', 'selected_encounter', 'selected_encounter_enum', 'selected_hidden', 'selected_reward', 'unselected_elite', 'unselected_encounter', 'unselected_hidden', 'unselected_reward', 'ascension_abilities')
    selected_elite = sgqlc.types.Field(Boolean, graphql_name='selectedElite')
    selected_encounter = sgqlc.types.Field(AghanimLabDepthListEncounterEnum, graphql_name='selectedEncounter')
    selected_encounter_enum = sgqlc.types.Field(Byte, graphql_name='selectedEncounterEnum')
    selected_hidden = sgqlc.types.Field(Boolean, graphql_name='selectedHidden')
    selected_reward = sgqlc.types.Field(AghanimLabDepthListRewardEnum, graphql_name='selectedReward')
    unselected_elite = sgqlc.types.Field(Boolean, graphql_name='unselectedElite')
    unselected_encounter = sgqlc.types.Field(AghanimLabDepthListEncounterEnum, graphql_name='unselectedEncounter')
    unselected_hidden = sgqlc.types.Field(Boolean, graphql_name='unselectedHidden')
    unselected_reward = sgqlc.types.Field(AghanimLabDepthListRewardEnum, graphql_name='unselectedReward')
    ascension_abilities = sgqlc.types.Field(sgqlc.types.list_of(AghanimLabDepthListAscensionAbilitiesObjectType), graphql_name='ascensionAbilities')


class AghanimLabMatchType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'did_win', 'duration_seconds', 'start_date_time', 'end_date_time', 'cluster_id', 'lobby_type', 'num_kills', 'num_deaths', 'num_human_players', 'game_mode', 'replay_salt', 'difficulty', 'depth', 'seed', 'battle_points', 'score', 'arcane_fragments', 'gold_bags', 'region_id', 'players', 'depth_list')
    id = sgqlc.types.Field(Long, graphql_name='id')
    did_win = sgqlc.types.Field(Boolean, graphql_name='didWin')
    duration_seconds = sgqlc.types.Field(Short, graphql_name='durationSeconds')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    cluster_id = sgqlc.types.Field(Short, graphql_name='clusterId')
    lobby_type = sgqlc.types.Field(Byte, graphql_name='lobbyType')
    num_kills = sgqlc.types.Field(Short, graphql_name='numKills')
    num_deaths = sgqlc.types.Field(Short, graphql_name='numDeaths')
    num_human_players = sgqlc.types.Field(Byte, graphql_name='numHumanPlayers')
    game_mode = sgqlc.types.Field(Byte, graphql_name='gameMode')
    replay_salt = sgqlc.types.Field(Long, graphql_name='replaySalt')
    difficulty = sgqlc.types.Field(AghanimLabMatchDifficultyEnum, graphql_name='difficulty')
    depth = sgqlc.types.Field(Byte, graphql_name='depth')
    seed = sgqlc.types.Field(Int, graphql_name='seed')
    battle_points = sgqlc.types.Field(Short, graphql_name='battlePoints')
    score = sgqlc.types.Field(Int, graphql_name='score')
    arcane_fragments = sgqlc.types.Field(Short, graphql_name='arcaneFragments')
    gold_bags = sgqlc.types.Field(Short, graphql_name='goldBags')
    region_id = sgqlc.types.Field(Byte, graphql_name='regionId')
    players = sgqlc.types.Field(sgqlc.types.list_of('AghanimLabPlayerSeasonOneType'), graphql_name='players', args=sgqlc.types.ArgDict((
        ('steam_account_id', sgqlc.types.Arg(Long, graphql_name='steamAccountId', default=None)),
))
    )
    depth_list = sgqlc.types.Field(sgqlc.types.list_of(AghanimLabMatchDepthListType), graphql_name='depthList')


class AghanimLabPlayerBlessingObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('type', 'value')
    type = sgqlc.types.Field(AghanimLabPlayerBlessingEnum, graphql_name='type')
    value = sgqlc.types.Field(Short, graphql_name='value')


class AghanimLabPlayerDepthListType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('num_deaths', 'gold_bags', 'kills', 'level', 'networth', 'rarity', 'selected_reward_ability_id', 'selected_reward_ability', 'un_selected_reward_ability_id1', 'un_selected_reward_ability1', 'un_selected_reward_ability_id2', 'un_selected_reward_ability2', 'selected_reward_image_ability_id')
    num_deaths = sgqlc.types.Field(Short, graphql_name='numDeaths')
    gold_bags = sgqlc.types.Field(Short, graphql_name='goldBags')
    kills = sgqlc.types.Field(Short, graphql_name='kills')
    level = sgqlc.types.Field(Byte, graphql_name='level')
    networth = sgqlc.types.Field(Int, graphql_name='networth')
    rarity = sgqlc.types.Field(Byte, graphql_name='rarity')
    selected_reward_ability_id = sgqlc.types.Field(Short, graphql_name='selectedRewardAbilityId')
    selected_reward_ability = sgqlc.types.Field(AbilityCustomGameType, graphql_name='selectedRewardAbility', args=sgqlc.types.ArgDict((
        ('langauge_id', sgqlc.types.Arg(Int, graphql_name='langaugeId', default=None)),
))
    )
    un_selected_reward_ability_id1 = sgqlc.types.Field(Short, graphql_name='unSelectedRewardAbilityId1')
    un_selected_reward_ability1 = sgqlc.types.Field(AbilityCustomGameType, graphql_name='unSelectedRewardAbility1', args=sgqlc.types.ArgDict((
        ('langauge_id', sgqlc.types.Arg(Int, graphql_name='langaugeId', default=None)),
))
    )
    un_selected_reward_ability_id2 = sgqlc.types.Field(Short, graphql_name='unSelectedRewardAbilityId2')
    un_selected_reward_ability2 = sgqlc.types.Field(AbilityCustomGameType, graphql_name='unSelectedRewardAbility2', args=sgqlc.types.ArgDict((
        ('langauge_id', sgqlc.types.Arg(Int, graphql_name='langaugeId', default=None)),
))
    )
    selected_reward_image_ability_id = sgqlc.types.Field(Short, graphql_name='selectedRewardImageAbilityId')


class AghanimLabPlayerSeasonOneType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'player_slot', 'steam_account_id', 'steam_account', 'is_victory', 'hero_id', 'hero', 'deaths', 'leaver_status', 'num_last_hits', 'gold_per_minute', 'networth', 'experience_per_minute', 'level', 'gold_spent', 'party_id', 'item0_id', 'item1_id', 'item2_id', 'item3_id', 'item4_id', 'item5_id', 'neutral0_id', 'arcane_fragments', 'bonus_arcane_fragments', 'gold_bags', 'neutral_item_id', 'player_depth_list', 'blessings')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    player_slot = sgqlc.types.Field(Byte, graphql_name='playerSlot')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    is_victory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVictory')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    hero = sgqlc.types.Field('HeroType', graphql_name='hero')
    deaths = sgqlc.types.Field(Long, graphql_name='deaths')
    leaver_status = sgqlc.types.Field(Byte, graphql_name='leaverStatus')
    num_last_hits = sgqlc.types.Field(Short, graphql_name='numLastHits')
    gold_per_minute = sgqlc.types.Field(Short, graphql_name='goldPerMinute')
    networth = sgqlc.types.Field(Int, graphql_name='networth')
    experience_per_minute = sgqlc.types.Field(Short, graphql_name='experiencePerMinute')
    level = sgqlc.types.Field(Byte, graphql_name='level')
    gold_spent = sgqlc.types.Field(Int, graphql_name='goldSpent')
    party_id = sgqlc.types.Field(Byte, graphql_name='partyId')
    item0_id = sgqlc.types.Field(Short, graphql_name='item0Id')
    item1_id = sgqlc.types.Field(Short, graphql_name='item1Id')
    item2_id = sgqlc.types.Field(Short, graphql_name='item2Id')
    item3_id = sgqlc.types.Field(Short, graphql_name='item3Id')
    item4_id = sgqlc.types.Field(Short, graphql_name='item4Id')
    item5_id = sgqlc.types.Field(Short, graphql_name='item5Id')
    neutral0_id = sgqlc.types.Field(Long, graphql_name='neutral0Id')
    arcane_fragments = sgqlc.types.Field(Short, graphql_name='arcaneFragments')
    bonus_arcane_fragments = sgqlc.types.Field(Short, graphql_name='bonusArcaneFragments')
    gold_bags = sgqlc.types.Field(Short, graphql_name='goldBags')
    neutral_item_id = sgqlc.types.Field(Short, graphql_name='neutralItemId')
    player_depth_list = sgqlc.types.Field(sgqlc.types.list_of(AghanimLabPlayerDepthListType), graphql_name='playerDepthList')
    blessings = sgqlc.types.Field(sgqlc.types.list_of(AghanimLabPlayerBlessingObjectType), graphql_name='blessings')


class AghanimLabRoomType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('difficulty', 'encounter_id', 'match_count', 'win_count', 'pick_count', 'death_count', 'elite_match_count', 'elite_win_count', 'elite_pick_count', 'elite_death_count')
    difficulty = sgqlc.types.Field(AghanimLabMatchDifficultyEnum, graphql_name='difficulty')
    encounter_id = sgqlc.types.Field(AghanimLabDepthListEncounterEnum, graphql_name='encounterId')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    pick_count = sgqlc.types.Field(Int, graphql_name='pickCount')
    death_count = sgqlc.types.Field(Int, graphql_name='deathCount')
    elite_match_count = sgqlc.types.Field(Int, graphql_name='eliteMatchCount')
    elite_win_count = sgqlc.types.Field(Int, graphql_name='eliteWinCount')
    elite_pick_count = sgqlc.types.Field(Int, graphql_name='elitePickCount')
    elite_death_count = sgqlc.types.Field(Int, graphql_name='eliteDeathCount')


class AssistDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'attacker', 'target', 'gold', 'xp', 'sub_time', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')
    target = sgqlc.types.Field(Short, graphql_name='target')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    xp = sgqlc.types.Field(Int, graphql_name='xp')
    sub_time = sgqlc.types.Field(Int, graphql_name='subTime')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')


class BattlepassPredictionHeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'hero', 'match_count', 'match_count_banned', 'win_rate', 'kill_avg', 'assist_avg', 'death_avg', 'last_hit_avg', 'experience_per_minute_avg', 'most_kills', 'most_deaths', 'most_assists', 'most_last_hits')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    hero = sgqlc.types.Field('HeroType', graphql_name='hero')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    match_count_banned = sgqlc.types.Field(Int, graphql_name='matchCountBanned')
    win_rate = sgqlc.types.Field(Float, graphql_name='winRate')
    kill_avg = sgqlc.types.Field(Float, graphql_name='killAvg')
    assist_avg = sgqlc.types.Field(Float, graphql_name='assistAvg')
    death_avg = sgqlc.types.Field(Float, graphql_name='deathAvg')
    last_hit_avg = sgqlc.types.Field(Float, graphql_name='lastHitAvg')
    experience_per_minute_avg = sgqlc.types.Field(Float, graphql_name='experiencePerMinuteAvg')
    most_kills = sgqlc.types.Field(Int, graphql_name='mostKills')
    most_deaths = sgqlc.types.Field(Int, graphql_name='mostDeaths')
    most_assists = sgqlc.types.Field(Int, graphql_name='mostAssists')
    most_last_hits = sgqlc.types.Field(Int, graphql_name='mostLastHits')


class BattlepassPredictionIdValueType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'match_count')
    id = sgqlc.types.Field(Long, graphql_name='id')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')


class BattlepassPredictionPlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'match_count', 'kill_avg', 'most_kills', 'death_avg', 'assist_avg', 'most_assists', 'last_hit_avg', 'most_last_hits', 'most_gold_per_minute', 'gold_per_minute_avg', 'hero_count')
    steam_account_id = sgqlc.types.Field(Int, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    kill_avg = sgqlc.types.Field(Float, graphql_name='killAvg')
    most_kills = sgqlc.types.Field(Int, graphql_name='mostKills')
    death_avg = sgqlc.types.Field(Float, graphql_name='deathAvg')
    assist_avg = sgqlc.types.Field(Float, graphql_name='assistAvg')
    most_assists = sgqlc.types.Field(Int, graphql_name='mostAssists')
    last_hit_avg = sgqlc.types.Field(Float, graphql_name='lastHitAvg')
    most_last_hits = sgqlc.types.Field(Int, graphql_name='mostLastHits')
    most_gold_per_minute = sgqlc.types.Field(Int, graphql_name='mostGoldPerMinute')
    gold_per_minute_avg = sgqlc.types.Field(Int, graphql_name='goldPerMinuteAvg')
    hero_count = sgqlc.types.Field(Int, graphql_name='heroCount')


class BattlepassPredictionTeamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('team_id', 'team', 'match_count', 'most_kills', 'kill_avg', 'least_deaths', 'most_assists', 'longest_game_seconds', 'shortest_game_seconds', 'game_seconds_avg', 'hero_count')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    most_kills = sgqlc.types.Field(Float, graphql_name='mostKills')
    kill_avg = sgqlc.types.Field(Float, graphql_name='killAvg')
    least_deaths = sgqlc.types.Field(Float, graphql_name='leastDeaths')
    most_assists = sgqlc.types.Field(Float, graphql_name='mostAssists')
    longest_game_seconds = sgqlc.types.Field(Int, graphql_name='longestGameSeconds')
    shortest_game_seconds = sgqlc.types.Field(Int, graphql_name='shortestGameSeconds')
    game_seconds_avg = sgqlc.types.Field(Float, graphql_name='gameSecondsAvg')
    hero_count = sgqlc.types.Field(Int, graphql_name='heroCount')


class BattlepassPredictionTournamentType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('heroes_picked', 'heroes_banned', 'total_kills', 'longest_game', 'solo_kills', 'solo_deaths', 'solo_assists', 'solo_gold_per_minute')
    heroes_picked = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionIdValueType), graphql_name='heroesPicked')
    heroes_banned = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionIdValueType), graphql_name='heroesBanned')
    total_kills = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionIdValueType), graphql_name='totalKills')
    longest_game = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionIdValueType), graphql_name='longestGame')
    solo_kills = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionIdValueType), graphql_name='soloKills')
    solo_deaths = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionIdValueType), graphql_name='soloDeaths')
    solo_assists = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionIdValueType), graphql_name='soloAssists')
    solo_gold_per_minute = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionIdValueType), graphql_name='soloGoldPerMinute')


class BlogType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'captain_jack_identity_id', 'title', 'banner_image_url', 'data', 'live_date_time', 'link')
    id = sgqlc.types.Field(Byte, graphql_name='id')
    captain_jack_identity_id = sgqlc.types.Field(Guid, graphql_name='captainJackIdentityId')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    banner_image_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='bannerImageUrl')
    data = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='data')
    live_date_time = sgqlc.types.Field(DateTime, graphql_name='liveDateTime')
    link = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='link')


class BuyBackDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'hero_id', 'death_time_remaining', 'cost')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    death_time_remaining = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='deathTimeRemaining')
    cost = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='cost')


class CaptainJackIdentityApiApplicationType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('captain_jack_identity_id', 'token_type', 'email_address', 'discord_address', 'website_address', 'description', 'is_approved', 'api_key', 'secret_key', 'issuer', 'matomo_reference_token')
    captain_jack_identity_id = sgqlc.types.Field(Guid, graphql_name='captainJackIdentityId')
    token_type = sgqlc.types.Field(StratzApiType, graphql_name='tokenType')
    email_address = sgqlc.types.Field(String, graphql_name='emailAddress')
    discord_address = sgqlc.types.Field(String, graphql_name='discordAddress')
    website_address = sgqlc.types.Field(String, graphql_name='websiteAddress')
    description = sgqlc.types.Field(String, graphql_name='description')
    is_approved = sgqlc.types.Field(Boolean, graphql_name='isApproved')
    api_key = sgqlc.types.Field(String, graphql_name='apiKey')
    secret_key = sgqlc.types.Field(String, graphql_name='secretKey')
    issuer = sgqlc.types.Field(String, graphql_name='issuer')
    matomo_reference_token = sgqlc.types.Field(String, graphql_name='matomoReferenceToken')


class CaptainJackIdentityPrivateProfileType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('captain_jack_identity_id', 'name', 'email', 'twitter', 'facebook', 'twitch', 'you_tube', 'premium_end_date', 'is_admin', 'feed_level', 'email_level', 'daily_email', 'weekly_email', 'monthly_email', 'pro_circuit_feed_level', 'pro_circuit_email_level', 'theme_type', 'language_id', 'email_validation_code', 'is_email_validated', 'email_hour', 'last_read_feed_time', 'last_daily_email', 'last_weekly_email', 'last_monthly_email', 'last_league_daily_email', 'last_team_daily_email', 'last_pro_circuit_daily_email', 'unsubscribe_code', 'last_seen', 'steam_account_id', 'steam_account', 'rosh')
    captain_jack_identity_id = sgqlc.types.Field(Guid, graphql_name='captainJackIdentityId')
    name = sgqlc.types.Field(String, graphql_name='name')
    email = sgqlc.types.Field(String, graphql_name='email')
    twitter = sgqlc.types.Field(String, graphql_name='twitter')
    facebook = sgqlc.types.Field(String, graphql_name='facebook')
    twitch = sgqlc.types.Field(String, graphql_name='twitch')
    you_tube = sgqlc.types.Field(String, graphql_name='youTube')
    premium_end_date = sgqlc.types.Field(Long, graphql_name='premiumEndDate')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    feed_level = sgqlc.types.Field(Byte, graphql_name='feedLevel')
    email_level = sgqlc.types.Field(Byte, graphql_name='emailLevel')
    daily_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='dailyEmail')
    weekly_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='weeklyEmail')
    monthly_email = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='monthlyEmail')
    pro_circuit_feed_level = sgqlc.types.Field(Byte, graphql_name='proCircuitFeedLevel')
    pro_circuit_email_level = sgqlc.types.Field(Byte, graphql_name='proCircuitEmailLevel')
    theme_type = sgqlc.types.Field(Byte, graphql_name='themeType')
    language_id = sgqlc.types.Field(Byte, graphql_name='languageId')
    email_validation_code = sgqlc.types.Field(String, graphql_name='emailValidationCode')
    is_email_validated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isEmailValidated')
    email_hour = sgqlc.types.Field(Byte, graphql_name='emailHour')
    last_read_feed_time = sgqlc.types.Field(Long, graphql_name='lastReadFeedTime')
    last_daily_email = sgqlc.types.Field(Long, graphql_name='lastDailyEmail')
    last_weekly_email = sgqlc.types.Field(Long, graphql_name='lastWeeklyEmail')
    last_monthly_email = sgqlc.types.Field(Long, graphql_name='lastMonthlyEmail')
    last_league_daily_email = sgqlc.types.Field(Long, graphql_name='lastLeagueDailyEmail')
    last_team_daily_email = sgqlc.types.Field(Long, graphql_name='lastTeamDailyEmail')
    last_pro_circuit_daily_email = sgqlc.types.Field(Long, graphql_name='lastProCircuitDailyEmail')
    unsubscribe_code = sgqlc.types.Field(String, graphql_name='unsubscribeCode')
    last_seen = sgqlc.types.Field(Long, graphql_name='lastSeen')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    rosh = sgqlc.types.Field(sgqlc.types.list_of('ROSHCaptainJackIdentityStatDifficultyType'), graphql_name='rosh', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(ROSHMatchesRequestType, graphql_name='request', default=None)),
))
    )


class CaptainJackIdentityPublicProfileType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('captain_jack_identity_id', 'name', 'twitter', 'facebook', 'twitch', 'you_tube', 'is_admin', 'steam_account_id', 'steam_account')
    captain_jack_identity_id = sgqlc.types.Field(Guid, graphql_name='captainJackIdentityId')
    name = sgqlc.types.Field(String, graphql_name='name')
    twitter = sgqlc.types.Field(String, graphql_name='twitter')
    facebook = sgqlc.types.Field(String, graphql_name='facebook')
    twitch = sgqlc.types.Field(String, graphql_name='twitch')
    you_tube = sgqlc.types.Field(String, graphql_name='youTube')
    is_admin = sgqlc.types.Field(Boolean, graphql_name='isAdmin')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')


class ClusterType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'region_id')
    id = sgqlc.types.Field(Int, graphql_name='id')
    region_id = sgqlc.types.Field(Short, graphql_name='regionId')


class ConstantQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero', 'heroes', 'roles', 'item', 'items', 'ability', 'abilities', 'game_modes', 'lobby_types', 'clusters', 'regions', 'game_version', 'game_versions', 'npc', 'npcs', 'patch_notes', 'custom_abilities', 'modifiers', 'pro_steam_accounts', 'popular_team_ids', 'casters', 'ti_winners', 'facets')
    hero = sgqlc.types.Field('HeroType', graphql_name='hero', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='id', default=None)),
        ('game_version_id', sgqlc.types.Arg(Short, graphql_name='gameVersionId', default=None)),
        ('language', sgqlc.types.Arg(LanguageEnum, graphql_name='language', default=None)),
))
    )
    heroes = sgqlc.types.Field(sgqlc.types.list_of('HeroType'), graphql_name='heroes', args=sgqlc.types.ArgDict((
        ('game_version_id', sgqlc.types.Arg(Short, graphql_name='gameVersionId', default=None)),
        ('language', sgqlc.types.Arg(LanguageEnum, graphql_name='language', default=None)),
))
    )
    roles = sgqlc.types.Field(sgqlc.types.list_of('RoleType'), graphql_name='roles')
    item = sgqlc.types.Field('ItemType', graphql_name='item', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('game_version_id', sgqlc.types.Arg(Short, graphql_name='gameVersionId', default=None)),
        ('language', sgqlc.types.Arg(LanguageEnum, graphql_name='language', default=None)),
))
    )
    items = sgqlc.types.Field(sgqlc.types.list_of('ItemType'), graphql_name='items', args=sgqlc.types.ArgDict((
        ('game_version_id', sgqlc.types.Arg(Short, graphql_name='gameVersionId', default=None)),
        ('language', sgqlc.types.Arg(LanguageEnum, graphql_name='language', default=None)),
))
    )
    ability = sgqlc.types.Field(AbilityType, graphql_name='ability', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
        ('game_version_id', sgqlc.types.Arg(Short, graphql_name='gameVersionId', default=None)),
        ('language', sgqlc.types.Arg(LanguageEnum, graphql_name='language', default=None)),
))
    )
    abilities = sgqlc.types.Field(sgqlc.types.list_of(AbilityType), graphql_name='abilities', args=sgqlc.types.ArgDict((
        ('game_version_id', sgqlc.types.Arg(Short, graphql_name='gameVersionId', default=None)),
        ('language', sgqlc.types.Arg(LanguageEnum, graphql_name='language', default=None)),
))
    )
    game_modes = sgqlc.types.Field(sgqlc.types.list_of('GameModeType'), graphql_name='gameModes')
    lobby_types = sgqlc.types.Field(sgqlc.types.list_of('LobbyTypeType'), graphql_name='lobbyTypes')
    clusters = sgqlc.types.Field(sgqlc.types.list_of(ClusterType), graphql_name='clusters')
    regions = sgqlc.types.Field(sgqlc.types.list_of('RegionType'), graphql_name='regions')
    game_version = sgqlc.types.Field('GameVersionType', graphql_name='gameVersion', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='id', default=None)),
))
    )
    game_versions = sgqlc.types.Field(sgqlc.types.list_of('GameVersionType'), graphql_name='gameVersions')
    npc = sgqlc.types.Field('NpcType', graphql_name='npc', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='id', default=None)),
        ('game_version_id', sgqlc.types.Arg(Short, graphql_name='gameVersionId', default=None)),
))
    )
    npcs = sgqlc.types.Field(sgqlc.types.list_of('NpcType'), graphql_name='npcs', args=sgqlc.types.ArgDict((
        ('game_version_id', sgqlc.types.Arg(Short, graphql_name='gameVersionId', default=None)),
))
    )
    patch_notes = sgqlc.types.Field(sgqlc.types.list_of('PatchNoteLanguageType'), graphql_name='patchNotes', args=sgqlc.types.ArgDict((
        ('language_id', sgqlc.types.Arg(LanguageEnum, graphql_name='languageId', default=None)),
        ('game_version_id', sgqlc.types.Arg(Short, graphql_name='gameVersionId', default=None)),
))
    )
    custom_abilities = sgqlc.types.Field(sgqlc.types.list_of(AbilityCustomGameType), graphql_name='customAbilities', args=sgqlc.types.ArgDict((
        ('language_id', sgqlc.types.Arg(LanguageEnum, graphql_name='languageId', default=None)),
))
    )
    modifiers = sgqlc.types.Field(sgqlc.types.list_of('ModifierType'), graphql_name='modifiers', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    pro_steam_accounts = sgqlc.types.Field(sgqlc.types.list_of('ProSteamAccountType'), graphql_name='proSteamAccounts')
    popular_team_ids = sgqlc.types.Field(sgqlc.types.list_of('TeamType'), graphql_name='popularTeamIds')
    casters = sgqlc.types.Field(sgqlc.types.list_of('SteamAccountType'), graphql_name='casters')
    ti_winners = sgqlc.types.Field(sgqlc.types.list_of('SteamAccountType'), graphql_name='tiWinners')
    facets = sgqlc.types.Field(sgqlc.types.list_of('FacetType'), graphql_name='facets', args=sgqlc.types.ArgDict((
        ('game_version_id', sgqlc.types.Arg(Short, graphql_name='gameVersionId', default=None)),
        ('language', sgqlc.types.Arg(LanguageEnum, graphql_name='language', default=None)),
))
    )


class DeathDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'attacker', 'is_from_illusion', 'target', 'by_ability', 'by_item', 'gold_fed', 'xp_fed', 'time_dead', 'reliable_gold', 'unreliable_gold', 'position_x', 'position_y', 'gold_lost', 'assist', 'is_ward_walk_through', 'is_attempt_tp_out', 'is_die_back', 'is_burst', 'is_engaged_on_death', 'has_heal_available', 'is_tracked', 'is_feed')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')
    is_from_illusion = sgqlc.types.Field(Boolean, graphql_name='isFromIllusion')
    target = sgqlc.types.Field(Short, graphql_name='target')
    by_ability = sgqlc.types.Field(Short, graphql_name='byAbility')
    by_item = sgqlc.types.Field(Short, graphql_name='byItem')
    gold_fed = sgqlc.types.Field(Int, graphql_name='goldFed')
    xp_fed = sgqlc.types.Field(Int, graphql_name='xpFed')
    time_dead = sgqlc.types.Field(Int, graphql_name='timeDead')
    reliable_gold = sgqlc.types.Field(Int, graphql_name='reliableGold')
    unreliable_gold = sgqlc.types.Field(Int, graphql_name='unreliableGold')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')
    gold_lost = sgqlc.types.Field(Int, graphql_name='goldLost')
    assist = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='assist')
    is_ward_walk_through = sgqlc.types.Field(Boolean, graphql_name='isWardWalkThrough')
    is_attempt_tp_out = sgqlc.types.Field(Boolean, graphql_name='isAttemptTpOut')
    is_die_back = sgqlc.types.Field(Boolean, graphql_name='isDieBack')
    is_burst = sgqlc.types.Field(Boolean, graphql_name='isBurst')
    is_engaged_on_death = sgqlc.types.Field(Boolean, graphql_name='isEngagedOnDeath')
    has_heal_available = sgqlc.types.Field(Boolean, graphql_name='hasHealAvailable')
    is_tracked = sgqlc.types.Field(Boolean, graphql_name='isTracked')
    is_feed = sgqlc.types.Field(Boolean, graphql_name='isFeed')


class DireTideCustomGameHeroWinDayType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('day', 'hero_id', 'win_count', 'match_count', 'candy_scored')
    day = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='day')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    candy_scored = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='candyScored')


class DireTideCustomGameMatchType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'did_radiant_win', 'duration_seconds', 'start_date_time', 'end_date_time', 'cluster_id', 'replay_salt', 'candy_lost', 'candy_picked_up', 'candy_scored', 'radiant_candy_scored', 'dire_candy_scored', 'players')
    id = sgqlc.types.Field(Long, graphql_name='id')
    did_radiant_win = sgqlc.types.Field(Boolean, graphql_name='didRadiantWin')
    duration_seconds = sgqlc.types.Field(Short, graphql_name='durationSeconds')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    cluster_id = sgqlc.types.Field(Short, graphql_name='clusterId')
    replay_salt = sgqlc.types.Field(Long, graphql_name='replaySalt')
    candy_lost = sgqlc.types.Field(Short, graphql_name='candyLost')
    candy_picked_up = sgqlc.types.Field(Short, graphql_name='candyPickedUp')
    candy_scored = sgqlc.types.Field(Short, graphql_name='candyScored')
    radiant_candy_scored = sgqlc.types.Field(Short, graphql_name='radiantCandyScored')
    dire_candy_scored = sgqlc.types.Field(Short, graphql_name='direCandyScored')
    players = sgqlc.types.Field(sgqlc.types.list_of('DireTideCustomGamePlayerType'), graphql_name='players', args=sgqlc.types.ArgDict((
        ('steam_account_id', sgqlc.types.Arg(Long, graphql_name='steamAccountId', default=None)),
))
    )


class DireTideCustomGamePlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'player_slot', 'steam_account_id', 'steam_account', 'is_victory', 'hero_id', 'hero', 'kills', 'deaths', 'assists', 'leaver_status', 'num_last_hits', 'gold_per_minute', 'gold_spent', 'level', 'hero_damage', 'hero_healing', 'networth', 'item0_id', 'item1_id', 'item2_id', 'item3_id', 'item4_id', 'item5_id', 'backpack0_id', 'backpack1_id', 'backpack2_id', 'neutral0_id', 'party_id', 'candy_lost', 'candy_picked_up', 'candy_scored')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    player_slot = sgqlc.types.Field(Byte, graphql_name='playerSlot')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    is_victory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVictory')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    hero = sgqlc.types.Field('HeroType', graphql_name='hero')
    kills = sgqlc.types.Field(Byte, graphql_name='kills')
    deaths = sgqlc.types.Field(Byte, graphql_name='deaths')
    assists = sgqlc.types.Field(Byte, graphql_name='assists')
    leaver_status = sgqlc.types.Field(Byte, graphql_name='leaverStatus')
    num_last_hits = sgqlc.types.Field(Short, graphql_name='numLastHits')
    gold_per_minute = sgqlc.types.Field(Short, graphql_name='goldPerMinute')
    gold_spent = sgqlc.types.Field(Int, graphql_name='goldSpent')
    level = sgqlc.types.Field(Byte, graphql_name='level')
    hero_damage = sgqlc.types.Field(Int, graphql_name='heroDamage')
    hero_healing = sgqlc.types.Field(Int, graphql_name='heroHealing')
    networth = sgqlc.types.Field(Int, graphql_name='networth')
    item0_id = sgqlc.types.Field(Short, graphql_name='item0Id')
    item1_id = sgqlc.types.Field(Short, graphql_name='item1Id')
    item2_id = sgqlc.types.Field(Short, graphql_name='item2Id')
    item3_id = sgqlc.types.Field(Short, graphql_name='item3Id')
    item4_id = sgqlc.types.Field(Short, graphql_name='item4Id')
    item5_id = sgqlc.types.Field(Short, graphql_name='item5Id')
    backpack0_id = sgqlc.types.Field(Short, graphql_name='backpack0Id')
    backpack1_id = sgqlc.types.Field(Short, graphql_name='backpack1Id')
    backpack2_id = sgqlc.types.Field(Short, graphql_name='backpack2Id')
    neutral0_id = sgqlc.types.Field(Short, graphql_name='neutral0Id')
    party_id = sgqlc.types.Field(Byte, graphql_name='partyId')
    candy_lost = sgqlc.types.Field(Short, graphql_name='candyLost')
    candy_picked_up = sgqlc.types.Field(Short, graphql_name='candyPickedUp')
    candy_scored = sgqlc.types.Field(Short, graphql_name='candyScored')


class DotaMutation(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('yogurt', 'user', 'admin', 'rosh', 'retry_match_download')
    yogurt = sgqlc.types.Field('YogurtMutation', graphql_name='yogurt')
    user = sgqlc.types.Field('DotaUserMutation', graphql_name='user')
    admin = sgqlc.types.Field(AdminMutation, graphql_name='admin')
    rosh = sgqlc.types.Field('ROSHMutation', graphql_name='rosh')
    retry_match_download = sgqlc.types.Field(Boolean, graphql_name='retryMatchDownload', args=sgqlc.types.ArgDict((
        ('match_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchId', default=None)),
))
    )


class DotaNextQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('enemy', 'ally', 'player_hero')
    enemy = sgqlc.types.Field(sgqlc.types.list_of('DotaNextWithAllyType'), graphql_name='enemy', args=sgqlc.types.ArgDict((
        ('steam_account_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Long)), graphql_name='steamAccountIds', default=None)),
        ('match_steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchSteamAccountId', default=None)),
))
    )
    ally = sgqlc.types.Field(sgqlc.types.list_of('DotaNextWithAllyType'), graphql_name='ally', args=sgqlc.types.ArgDict((
        ('steam_account_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Long)), graphql_name='steamAccountIds', default=None)),
        ('match_steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchSteamAccountId', default=None)),
))
    )
    player_hero = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of('MatchPlayerItemPurchaseEventType')), graphql_name='playerHero', args=sgqlc.types.ArgDict((
        ('steam_account_ids', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='steamAccountIds', default=None)),
        ('hero_id', sgqlc.types.Arg(Short, graphql_name='heroId', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.non_null(Byte), graphql_name='gameModeIds', default=None)),
        ('lobby_type_ids', sgqlc.types.Arg(sgqlc.types.non_null(Byte), graphql_name='lobbyTypeIds', default=None)),
        ('limit_by_item_ids', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='limitByItemIds', default=None)),
        ('start_date_time', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='startDateTime', default=None)),
))
    )


class DotaNextWithAllyType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'lifetime_match_count', 'lifetime_win_match_count')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    lifetime_match_count = sgqlc.types.Field(Int, graphql_name='lifetimeMatchCount')
    lifetime_win_match_count = sgqlc.types.Field(Int, graphql_name='lifetimeWinMatchCount')


class DotaPlusWeekType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('week', 'active', 'expired')
    week = sgqlc.types.Field(Int, graphql_name='week')
    active = sgqlc.types.Field(Int, graphql_name='active')
    expired = sgqlc.types.Field(Int, graphql_name='expired')


class DotaQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match', 'matches', 'player', 'players', 'team', 'teams', 'league', 'leagues', 'guild', 'yogurt', 'plus', 'stratz', 'hero_stats', 'constants', 'leaderboard', 'live', 'vendor')
    match = sgqlc.types.Field('MatchType', graphql_name='match', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    matches = sgqlc.types.Field(sgqlc.types.list_of('MatchType'), graphql_name='matches', args=sgqlc.types.ArgDict((
        ('ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Long)), graphql_name='ids', default=None)),
))
    )
    player = sgqlc.types.Field('PlayerType', graphql_name='player', args=sgqlc.types.ArgDict((
        ('steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='steamAccountId', default=None)),
))
    )
    players = sgqlc.types.Field(sgqlc.types.list_of('PlayerType'), graphql_name='players', args=sgqlc.types.ArgDict((
        ('steam_account_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Long)), graphql_name='steamAccountIds', default=None)),
))
    )
    team = sgqlc.types.Field('TeamType', graphql_name='team', args=sgqlc.types.ArgDict((
        ('team_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='teamId', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.list_of('TeamType'), graphql_name='teams', args=sgqlc.types.ArgDict((
        ('team_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='teamIds', default=None)),
))
    )
    league = sgqlc.types.Field('LeagueType', graphql_name='league', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    leagues = sgqlc.types.Field(sgqlc.types.list_of('LeagueType'), graphql_name='leagues', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(LeagueRequestType), graphql_name='request', default=None)),
))
    )
    guild = sgqlc.types.Field('GuildType', graphql_name='guild', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    yogurt = sgqlc.types.Field('YogurtQuery', graphql_name='yogurt')
    plus = sgqlc.types.Field('PlusQuery', graphql_name='plus')
    stratz = sgqlc.types.Field('StratzQuery', graphql_name='stratz')
    hero_stats = sgqlc.types.Field('HeroStatsQuery', graphql_name='heroStats')
    constants = sgqlc.types.Field(ConstantQuery, graphql_name='constants')
    leaderboard = sgqlc.types.Field('LeaderboardQuery', graphql_name='leaderboard')
    live = sgqlc.types.Field('LiveQuery', graphql_name='live')
    vendor = sgqlc.types.Field('VendorQuery', graphql_name='vendor')


class DotaSubscription(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_count', 'player_count', 'feed_live', 'match_live', 'match_live_league')
    match_count = sgqlc.types.Field('TotalMatchCountType', graphql_name='matchCount')
    player_count = sgqlc.types.Field('TotalPlayerCountType', graphql_name='playerCount')
    feed_live = sgqlc.types.Field('LiveEventType', graphql_name='feedLive')
    match_live = sgqlc.types.Field('MatchLiveType', graphql_name='matchLive', args=sgqlc.types.ArgDict((
        ('match_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchId', default=None)),
))
    )
    match_live_league = sgqlc.types.Field('MatchLiveType', graphql_name='matchLiveLeague', args=sgqlc.types.ArgDict((
        ('league_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='leagueId', default=None)),
))
    )


class DotaUserMutation(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('read_all_feed', 'validate_email', 'unsubscribe_email', 'update_profile', 'follow_player', 'unfollow_player', 'update_following', 'update_all_following', 'update_following_favorite', 'follow_league', 'unfollow_league', 'apply_stratz_api_key', 'check_public_dota_account')
    read_all_feed = sgqlc.types.Field(Boolean, graphql_name='readAllFeed')
    validate_email = sgqlc.types.Field(Boolean, graphql_name='validateEmail', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(Guid), graphql_name='code', default=None)),
))
    )
    unsubscribe_email = sgqlc.types.Field(Boolean, graphql_name='unsubscribeEmail', args=sgqlc.types.ArgDict((
        ('code', sgqlc.types.Arg(sgqlc.types.non_null(Guid), graphql_name='code', default=None)),
))
    )
    update_profile = sgqlc.types.Field(Boolean, graphql_name='updateProfile', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(CaptainJackIdentityProfileUpdateRequestType), graphql_name='request', default=None)),
))
    )
    follow_player = sgqlc.types.Field(Boolean, graphql_name='followPlayer', args=sgqlc.types.ArgDict((
        ('steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='steamAccountId', default=None)),
))
    )
    unfollow_player = sgqlc.types.Field(Boolean, graphql_name='unfollowPlayer', args=sgqlc.types.ArgDict((
        ('steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='steamAccountId', default=None)),
))
    )
    update_following = sgqlc.types.Field(Boolean, graphql_name='updateFollowing', args=sgqlc.types.ArgDict((
        ('followed_steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='followedSteamAccountId', default=None)),
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFollowerRequestType), graphql_name='request', default=None)),
))
    )
    update_all_following = sgqlc.types.Field(Boolean, graphql_name='updateAllFollowing', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(UpdateFollowerRequestType), graphql_name='request', default=None)),
))
    )
    update_following_favorite = sgqlc.types.Field(Boolean, graphql_name='updateFollowingFavorite', args=sgqlc.types.ArgDict((
        ('followed_steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='followedSteamAccountId', default=None)),
        ('is_favorite', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isFavorite', default=None)),
))
    )
    follow_league = sgqlc.types.Field(Boolean, graphql_name='followLeague', args=sgqlc.types.ArgDict((
        ('league_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='leagueId', default=None)),
))
    )
    unfollow_league = sgqlc.types.Field(Boolean, graphql_name='unfollowLeague', args=sgqlc.types.ArgDict((
        ('league_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='leagueId', default=None)),
))
    )
    apply_stratz_api_key = sgqlc.types.Field(Boolean, graphql_name='applyStratzApiKey', args=sgqlc.types.ArgDict((
        ('token_type', sgqlc.types.Arg(sgqlc.types.non_null(StratzApiType), graphql_name='tokenType', default=None)),
        ('email_address', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='emailAddress', default=None)),
        ('discord_address', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='discordAddress', default=None)),
        ('website_address', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='websiteAddress', default=None)),
        ('description', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='description', default=None)),
))
    )
    check_public_dota_account = sgqlc.types.Field(Boolean, graphql_name='checkPublicDotaAccount')


class ExperienceDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'amount', 'reason', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amount')
    reason = sgqlc.types.Field(XpReason, graphql_name='reason')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')


class FacetLanguageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('display_name', 'description')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    description = sgqlc.types.Field(String, graphql_name='description')


class FacetType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'color', 'icon', 'gradient_id', 'language')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    color = sgqlc.types.Field(String, graphql_name='color')
    icon = sgqlc.types.Field(String, graphql_name='icon')
    gradient_id = sgqlc.types.Field(Short, graphql_name='gradientId')
    language = sgqlc.types.Field(FacetLanguageType, graphql_name='language')


class FeatType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('type', 'value', 'hero_id', 'hero', 'match_id', 'match')
    type = sgqlc.types.Field(sgqlc.types.non_null(FeatEnum), graphql_name='type')
    value = sgqlc.types.Field(Int, graphql_name='value')
    hero_id = sgqlc.types.Field(Int, graphql_name='heroId')
    hero = sgqlc.types.Field('HeroType', graphql_name='hero')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    match = sgqlc.types.Field('MatchType', graphql_name='match')


class FeedResponseType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('data', 'count', 'attack_animation_point')
    data = sgqlc.types.Field(sgqlc.types.list_of('FeedType'), graphql_name='data')
    count = sgqlc.types.Field(Int, graphql_name='count')
    attack_animation_point = sgqlc.types.Field(DateTime, graphql_name='attackAnimationPoint')


class FeedType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'league', 'target_steam_account_id', 'type', 'match_id', 'hero_id', 'date', 'value', 'did_win')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    league = sgqlc.types.Field('LeagueType', graphql_name='league')
    target_steam_account_id = sgqlc.types.Field(Long, graphql_name='targetSteamAccountId')
    type = sgqlc.types.Field(Byte, graphql_name='type')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    date = sgqlc.types.Field(Long, graphql_name='date')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')
    did_win = sgqlc.types.Field(Boolean, graphql_name='didWin')


class FollowerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('captain_jack_identity_id', 'captain_jack_identity_profile', 'steam_account_id', 'steam_account', 'feed_level', 'email_level', 'daily_email', 'weekly_email', 'monthly_email', 'is_favorite', 'last_email', 'did_manual_update')
    captain_jack_identity_id = sgqlc.types.Field(Guid, graphql_name='captainJackIdentityId')
    captain_jack_identity_profile = sgqlc.types.Field(CaptainJackIdentityPublicProfileType, graphql_name='captainJackIdentityProfile')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    feed_level = sgqlc.types.Field(Byte, graphql_name='feedLevel')
    email_level = sgqlc.types.Field(Byte, graphql_name='emailLevel')
    daily_email = sgqlc.types.Field(Boolean, graphql_name='dailyEmail')
    weekly_email = sgqlc.types.Field(Boolean, graphql_name='weeklyEmail')
    monthly_email = sgqlc.types.Field(Boolean, graphql_name='monthlyEmail')
    is_favorite = sgqlc.types.Field(Boolean, graphql_name='isFavorite')
    last_email = sgqlc.types.Field(Long, graphql_name='lastEmail')
    did_manual_update = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='didManualUpdate')


class GameModeType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class GameVersionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'as_of_date_time')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    as_of_date_time = sgqlc.types.Field(Long, graphql_name='asOfDateTime')


class GoldDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'amount', 'reason', 'npc_id', 'is_valid_for_stats')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amount')
    reason = sgqlc.types.Field(GoldReason, graphql_name='reason')
    npc_id = sgqlc.types.Field(Int, graphql_name='npcId')
    is_valid_for_stats = sgqlc.types.Field(Boolean, graphql_name='isValidForStats')


class GuildMemberType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('guild_id', 'steam_account_id', 'join_date_time', 'guild', 'steam_account', 'match_count', 'win_count', 'imp')
    guild_id = sgqlc.types.Field(Int, graphql_name='guildId')
    steam_account_id = sgqlc.types.Field(Int, graphql_name='steamAccountId')
    join_date_time = sgqlc.types.Field(Long, graphql_name='joinDateTime')
    guild = sgqlc.types.Field('GuildType', graphql_name='guild')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    imp = sgqlc.types.Field(Int, graphql_name='imp')


class GuildType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'motd', 'name', 'tag', 'created_date_time', 'language', 'flags', 'logo', 'region', 'description', 'required_rank', 'primary_color', 'secondary_color', 'pattern', 'points', 'past_weekly_rank', 'past_weekly_percentile', 'current_percentile', 'last_update_date_time', 'members', 'matches', 'member_count', 'total_battle_pass_levels', 'rank')
    id = sgqlc.types.Field(Int, graphql_name='id')
    motd = sgqlc.types.Field(String, graphql_name='motd')
    name = sgqlc.types.Field(String, graphql_name='name')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    created_date_time = sgqlc.types.Field(Long, graphql_name='createdDateTime')
    language = sgqlc.types.Field(Byte, graphql_name='language')
    flags = sgqlc.types.Field(Int, graphql_name='flags')
    logo = sgqlc.types.Field(String, graphql_name='logo')
    region = sgqlc.types.Field(Byte, graphql_name='region')
    description = sgqlc.types.Field(String, graphql_name='description')
    required_rank = sgqlc.types.Field(Byte, graphql_name='requiredRank')
    primary_color = sgqlc.types.Field(Byte, graphql_name='primaryColor')
    secondary_color = sgqlc.types.Field(Byte, graphql_name='secondaryColor')
    pattern = sgqlc.types.Field(Byte, graphql_name='pattern')
    points = sgqlc.types.Field(Int, graphql_name='points')
    past_weekly_rank = sgqlc.types.Field(Int, graphql_name='pastWeeklyRank')
    past_weekly_percentile = sgqlc.types.Field(Byte, graphql_name='pastWeeklyPercentile')
    current_percentile = sgqlc.types.Field(Byte, graphql_name='currentPercentile')
    last_update_date_time = sgqlc.types.Field(Long, graphql_name='lastUpdateDateTime')
    members = sgqlc.types.Field(sgqlc.types.list_of(GuildMemberType), graphql_name='members')
    matches = sgqlc.types.Field(sgqlc.types.list_of('MatchType'), graphql_name='matches', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    member_count = sgqlc.types.Field(Byte, graphql_name='memberCount')
    total_battle_pass_levels = sgqlc.types.Field(Int, graphql_name='totalBattlePassLevels')
    rank = sgqlc.types.Field(Byte, graphql_name='rank')


class HealDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'attacker', 'target', 'value', 'by_ability', 'by_item')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')
    target = sgqlc.types.Field(Short, graphql_name='target')
    value = sgqlc.types.Field(Int, graphql_name='value')
    by_ability = sgqlc.types.Field(Short, graphql_name='byAbility')
    by_item = sgqlc.types.Field(Short, graphql_name='byItem')


class HeroAbilityMaxType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'week', 'bracket_basic_ids', 'position', 'ability_id', 'level', 'match_count', 'win_count')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='week')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    ability_id = sgqlc.types.Field(Int, graphql_name='abilityId')
    level = sgqlc.types.Field(Int, graphql_name='level')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')


class HeroAbilityMinType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'week', 'bracket_basic_ids', 'position', 'ability_id', 'level', 'match_count', 'win_count')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='week')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    ability_id = sgqlc.types.Field(Int, graphql_name='abilityId')
    level = sgqlc.types.Field(Int, graphql_name='level')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')


class HeroAbilityTalentType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'week', 'bracket_basic_ids', 'position', 'ability_id', 'match_count', 'win_count', 'time', 'wins_average', 'time_average')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='week')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    ability_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='abilityId')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='matchCount')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='winCount')
    time = sgqlc.types.Field(Long, graphql_name='time')
    wins_average = sgqlc.types.Field(Decimal, graphql_name='winsAverage')
    time_average = sgqlc.types.Field(Decimal, graphql_name='timeAverage')


class HeroAbilityType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('slot', 'game_version_id', 'ability_id', 'ability')
    slot = sgqlc.types.Field(sgqlc.types.non_null(Byte), graphql_name='slot')
    game_version_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='gameVersionId')
    ability_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='abilityId')
    ability = sgqlc.types.Field(AbilityType, graphql_name='ability', args=sgqlc.types.ArgDict((
        ('language', sgqlc.types.Arg(LanguageEnum, graphql_name='language', default=None)),
))
    )


class HeroBanType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'day', 'bracket_basic_ids', 'match_count', 'win_count')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    day = sgqlc.types.Field(Int, graphql_name='day')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')


class HeroDamageDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'attacker', 'target', 'value', 'by_ability', 'by_item', 'damage_type', 'from_npc', 'to_npc', 'from_illusion', 'to_illusion', 'is_physical_attack', 'is_source_main_hero', 'is_target_main_hero')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')
    target = sgqlc.types.Field(Short, graphql_name='target')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')
    by_ability = sgqlc.types.Field(Short, graphql_name='byAbility')
    by_item = sgqlc.types.Field(Short, graphql_name='byItem')
    damage_type = sgqlc.types.Field(Damage, graphql_name='damageType')
    from_npc = sgqlc.types.Field(Short, graphql_name='fromNpc')
    to_npc = sgqlc.types.Field(Short, graphql_name='toNpc')
    from_illusion = sgqlc.types.Field(Boolean, graphql_name='fromIllusion')
    to_illusion = sgqlc.types.Field(Boolean, graphql_name='toIllusion')
    is_physical_attack = sgqlc.types.Field(Boolean, graphql_name='isPhysicalAttack')
    is_source_main_hero = sgqlc.types.Field(Boolean, graphql_name='isSourceMainHero')
    is_target_main_hero = sgqlc.types.Field(Boolean, graphql_name='isTargetMainHero')


class HeroDotaPlusLeaderboardRankTopType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'steam_account_id', 'level', 'created_date_time', 'steam_account')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    level = sgqlc.types.Field(Byte, graphql_name='level')
    created_date_time = sgqlc.types.Field(Long, graphql_name='createdDateTime')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')


class HeroDotaPlusLeaderboardRankType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'steam_account_id', 'level', 'total_actions', 'created_date_time', 'steam_account')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    level = sgqlc.types.Field(Byte, graphql_name='level')
    total_actions = sgqlc.types.Field(Long, graphql_name='totalActions')
    created_date_time = sgqlc.types.Field(Long, graphql_name='createdDateTime')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')


class HeroDryadType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'with_', 'match_count_with', 'vs', 'match_count_vs')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    with_ = sgqlc.types.Field(sgqlc.types.list_of('HeroStatsHeroDryadType'), graphql_name='with')
    match_count_with = sgqlc.types.Field(Long, graphql_name='matchCountWith')
    vs = sgqlc.types.Field(sgqlc.types.list_of('HeroStatsHeroDryadType'), graphql_name='vs')
    match_count_vs = sgqlc.types.Field(Long, graphql_name='matchCountVs')


class HeroFacetType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('ability_id', 'facet_id', 'slot')
    ability_id = sgqlc.types.Field(Short, graphql_name='abilityId')
    facet_id = sgqlc.types.Field(Short, graphql_name='facetId')
    slot = sgqlc.types.Field(Byte, graphql_name='slot')


class HeroGuideListType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'match_count', 'guides')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    guides = sgqlc.types.Field(sgqlc.types.list_of('HeroGuideType'), graphql_name='guides', args=sgqlc.types.ArgDict((
        ('item_id', sgqlc.types.Arg(Short, graphql_name='itemId', default=None)),
        ('neutral_item_id', sgqlc.types.Arg(Short, graphql_name='neutralItemId', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )


class HeroGuideType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'steam_account_id', 'match_id', 'match', 'match_player', 'created_date_time', 'item_ids', 'neutral_item_ids')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    match_player = sgqlc.types.Field('MatchPlayerType', graphql_name='matchPlayer')
    created_date_time = sgqlc.types.Field(Long, graphql_name='createdDateTime')
    item_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='itemIds')
    neutral_item_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='neutralItemIds')


class HeroItemBootPurchaseType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'week', 'bracket_basic_ids', 'position', 'item_id', 'instance', 'time', 'time_average', 'match_count', 'win_count', 'win_average', 'kills', 'kills_average', 'deaths', 'deaths_average', 'assists', 'assists_average', 'gold_earned', 'gold_earned_average', 'xp', 'xp_average', 'activations', 'activations_average', 'activation_time', 'activations_time_average')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='week')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='itemId')
    instance = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instance')
    time = sgqlc.types.Field(Long, graphql_name='time')
    time_average = sgqlc.types.Field(Decimal, graphql_name='timeAverage')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')
    win_average = sgqlc.types.Field(Decimal, graphql_name='winAverage')
    kills = sgqlc.types.Field(Long, graphql_name='kills')
    kills_average = sgqlc.types.Field(Decimal, graphql_name='killsAverage')
    deaths = sgqlc.types.Field(Long, graphql_name='deaths')
    deaths_average = sgqlc.types.Field(Decimal, graphql_name='deathsAverage')
    assists = sgqlc.types.Field(Long, graphql_name='assists')
    assists_average = sgqlc.types.Field(Decimal, graphql_name='assistsAverage')
    gold_earned = sgqlc.types.Field(Long, graphql_name='goldEarned')
    gold_earned_average = sgqlc.types.Field(Decimal, graphql_name='goldEarnedAverage')
    xp = sgqlc.types.Field(Long, graphql_name='xp')
    xp_average = sgqlc.types.Field(Decimal, graphql_name='xpAverage')
    activations = sgqlc.types.Field(Long, graphql_name='activations')
    activations_average = sgqlc.types.Field(Decimal, graphql_name='activationsAverage')
    activation_time = sgqlc.types.Field(Long, graphql_name='activationTime')
    activations_time_average = sgqlc.types.Field(Decimal, graphql_name='activationsTimeAverage')


class HeroItemPurchaseType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'week', 'bracket_basic_ids', 'position', 'item_id', 'instance', 'time', 'match_count', 'win_count', 'wins_average')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='week')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='itemId')
    instance = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instance')
    time = sgqlc.types.Field(Long, graphql_name='time')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')
    wins_average = sgqlc.types.Field(Decimal, graphql_name='winsAverage')


class HeroItemStartingPurchaseType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'week', 'bracket_basic_ids', 'position', 'item_id', 'instance', 'was_given', 'match_count', 'win_count', 'wins_average')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='week')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='itemId')
    instance = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='instance')
    was_given = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wasGiven')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')
    wins_average = sgqlc.types.Field(Decimal, graphql_name='winsAverage')


class HeroLaneOutcomeType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id1', 'week', 'bracket_basic_ids', 'position', 'match_count', 'draw_count', 'win_count', 'loss_count', 'stomp_win_count', 'stomp_loss_count', 'match_win_count', 'cs_count', 'hero_id2')
    hero_id1 = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId1')
    week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='week')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    draw_count = sgqlc.types.Field(Long, graphql_name='drawCount')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')
    loss_count = sgqlc.types.Field(Long, graphql_name='lossCount')
    stomp_win_count = sgqlc.types.Field(Long, graphql_name='stompWinCount')
    stomp_loss_count = sgqlc.types.Field(Long, graphql_name='stompLossCount')
    match_win_count = sgqlc.types.Field(Long, graphql_name='matchWinCount')
    cs_count = sgqlc.types.Field(Long, graphql_name='csCount')
    hero_id2 = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId2')


class HeroLanguageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('display_name', 'lore', 'hype')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    lore = sgqlc.types.Field(String, graphql_name='lore')
    hype = sgqlc.types.Field(String, graphql_name='hype')


class HeroMatchupType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('advantage', 'disadvantage')
    advantage = sgqlc.types.Field(sgqlc.types.list_of(HeroDryadType), graphql_name='advantage')
    disadvantage = sgqlc.types.Field(sgqlc.types.list_of(HeroDryadType), graphql_name='disadvantage')


class HeroNeutralItemType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'week', 'bracket_basic_ids', 'position', 'item_id', 'item', 'match_count', 'win_count', 'equipped_match_count', 'equipped_match_win_count')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='week')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    item_id = sgqlc.types.Field(Int, graphql_name='itemId')
    item = sgqlc.types.Field('ItemType', graphql_name='item')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')
    equipped_match_count = sgqlc.types.Field(Long, graphql_name='equippedMatchCount')
    equipped_match_win_count = sgqlc.types.Field(Long, graphql_name='equippedMatchWinCount')


class HeroPositionTimeDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'week', 'time', 'position', 'bracket_basic_ids', 'match_count', 'remaining_match_count', 'win_count', 'mvp', 'top_core', 'top_support', 'courier_kills', 'apm', 'casts', 'ability_casts', 'kills', 'deaths', 'assists', 'networth', 'xp', 'cs', 'dn', 'neutrals', 'hero_damage', 'tower_damage', 'physical_damage', 'magical_damage', 'physical_damage_received', 'magical_damage_received', 'triple_kill', 'ultra_kill', 'rampage', 'god_like', 'gold_per_minute', 'disable_count', 'disable_duration', 'stun_count', 'stun_duration', 'slow_count', 'slow_duration', 'healing_self', 'healing_allies', 'invisible_count', 'rune_power', 'rune_bounty', 'level', 'camps_stacked', 'support_gold', 'purge_modifiers', 'ancients', 'team_kills', 'gold_lost', 'gold_fed', 'buyback_count', 'weaken_count', 'weaken_duration', 'physical_item_damage', 'magical_item_damage', 'healing_item_self', 'healing_item_allies', 'xp_fed', 'pure_damage_received', 'attack_damage', 'attack_count', 'cast_damage', 'damage_received', 'damage', 'pure_damage', 'k_daaverage', 'kill_contribution_average', 'stomp_won', 'stomp_lost', 'come_back_won', 'come_back_lost')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId')
    week = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='week')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    remaining_match_count = sgqlc.types.Field(Long, graphql_name='remainingMatchCount')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')
    mvp = sgqlc.types.Field(Decimal, graphql_name='mvp')
    top_core = sgqlc.types.Field(Decimal, graphql_name='topCore')
    top_support = sgqlc.types.Field(Decimal, graphql_name='topSupport')
    courier_kills = sgqlc.types.Field(Decimal, graphql_name='courierKills')
    apm = sgqlc.types.Field(Decimal, graphql_name='apm')
    casts = sgqlc.types.Field(Decimal, graphql_name='casts')
    ability_casts = sgqlc.types.Field(Decimal, graphql_name='abilityCasts')
    kills = sgqlc.types.Field(Decimal, graphql_name='kills')
    deaths = sgqlc.types.Field(Decimal, graphql_name='deaths')
    assists = sgqlc.types.Field(Decimal, graphql_name='assists')
    networth = sgqlc.types.Field(Decimal, graphql_name='networth')
    xp = sgqlc.types.Field(Decimal, graphql_name='xp')
    cs = sgqlc.types.Field(Decimal, graphql_name='cs')
    dn = sgqlc.types.Field(Decimal, graphql_name='dn')
    neutrals = sgqlc.types.Field(Decimal, graphql_name='neutrals')
    hero_damage = sgqlc.types.Field(Decimal, graphql_name='heroDamage')
    tower_damage = sgqlc.types.Field(Decimal, graphql_name='towerDamage')
    physical_damage = sgqlc.types.Field(Decimal, graphql_name='physicalDamage')
    magical_damage = sgqlc.types.Field(Decimal, graphql_name='magicalDamage')
    physical_damage_received = sgqlc.types.Field(Decimal, graphql_name='physicalDamageReceived')
    magical_damage_received = sgqlc.types.Field(Decimal, graphql_name='magicalDamageReceived')
    triple_kill = sgqlc.types.Field(Decimal, graphql_name='tripleKill')
    ultra_kill = sgqlc.types.Field(Decimal, graphql_name='ultraKill')
    rampage = sgqlc.types.Field(Decimal, graphql_name='rampage')
    god_like = sgqlc.types.Field(Decimal, graphql_name='godLike')
    gold_per_minute = sgqlc.types.Field(Decimal, graphql_name='goldPerMinute')
    disable_count = sgqlc.types.Field(Decimal, graphql_name='disableCount')
    disable_duration = sgqlc.types.Field(Decimal, graphql_name='disableDuration')
    stun_count = sgqlc.types.Field(Decimal, graphql_name='stunCount')
    stun_duration = sgqlc.types.Field(Decimal, graphql_name='stunDuration')
    slow_count = sgqlc.types.Field(Decimal, graphql_name='slowCount')
    slow_duration = sgqlc.types.Field(Decimal, graphql_name='slowDuration')
    healing_self = sgqlc.types.Field(Decimal, graphql_name='healingSelf')
    healing_allies = sgqlc.types.Field(Decimal, graphql_name='healingAllies')
    invisible_count = sgqlc.types.Field(Decimal, graphql_name='invisibleCount')
    rune_power = sgqlc.types.Field(Decimal, graphql_name='runePower')
    rune_bounty = sgqlc.types.Field(Decimal, graphql_name='runeBounty')
    level = sgqlc.types.Field(Decimal, graphql_name='level')
    camps_stacked = sgqlc.types.Field(Decimal, graphql_name='campsStacked')
    support_gold = sgqlc.types.Field(Decimal, graphql_name='supportGold')
    purge_modifiers = sgqlc.types.Field(Decimal, graphql_name='purgeModifiers')
    ancients = sgqlc.types.Field(Decimal, graphql_name='ancients')
    team_kills = sgqlc.types.Field(Decimal, graphql_name='teamKills')
    gold_lost = sgqlc.types.Field(Decimal, graphql_name='goldLost')
    gold_fed = sgqlc.types.Field(Decimal, graphql_name='goldFed')
    buyback_count = sgqlc.types.Field(Decimal, graphql_name='buybackCount')
    weaken_count = sgqlc.types.Field(Decimal, graphql_name='weakenCount')
    weaken_duration = sgqlc.types.Field(Decimal, graphql_name='weakenDuration')
    physical_item_damage = sgqlc.types.Field(Decimal, graphql_name='physicalItemDamage')
    magical_item_damage = sgqlc.types.Field(Decimal, graphql_name='magicalItemDamage')
    healing_item_self = sgqlc.types.Field(Decimal, graphql_name='healingItemSelf')
    healing_item_allies = sgqlc.types.Field(Decimal, graphql_name='healingItemAllies')
    xp_fed = sgqlc.types.Field(Decimal, graphql_name='xpFed')
    pure_damage_received = sgqlc.types.Field(Decimal, graphql_name='pureDamageReceived')
    attack_damage = sgqlc.types.Field(Decimal, graphql_name='attackDamage')
    attack_count = sgqlc.types.Field(Decimal, graphql_name='attackCount')
    cast_damage = sgqlc.types.Field(Decimal, graphql_name='castDamage')
    damage_received = sgqlc.types.Field(Decimal, graphql_name='damageReceived')
    damage = sgqlc.types.Field(Decimal, graphql_name='damage')
    pure_damage = sgqlc.types.Field(Decimal, graphql_name='pureDamage')
    k_daaverage = sgqlc.types.Field(Decimal, graphql_name='kDAAverage')
    kill_contribution_average = sgqlc.types.Field(Decimal, graphql_name='killContributionAverage')
    stomp_won = sgqlc.types.Field(Decimal, graphql_name='stompWon')
    stomp_lost = sgqlc.types.Field(Decimal, graphql_name='stompLost')
    come_back_won = sgqlc.types.Field(Decimal, graphql_name='comeBackWon')
    come_back_lost = sgqlc.types.Field(Decimal, graphql_name='comeBackLost')


class HeroRampageObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'match', 'time', 'steam_account_id', 'hero_ids', 'steam_account')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    time = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='time')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    hero_ids = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroIds')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')


class HeroRoleType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('role_id', 'level')
    role_id = sgqlc.types.Field(HeroRoleEnum, graphql_name='roleId')
    level = sgqlc.types.Field(Short, graphql_name='level')


class HeroStatType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('enabled', 'hero_unlock_order', 'team', 'c_menabled', 'new_player_enabled', 'attack_type', 'starting_armor', 'starting_magic_armor', 'starting_damage_min', 'starting_damage_max', 'attack_rate', 'attack_animation_point', 'attack_acquisition_range', 'attack_range', 'primary_attribute', 'strength_base', 'strength_gain', 'intelligence_base', 'intelligence_gain', 'agility_base', 'agility_gain', 'hp_regen', 'mp_regen', 'move_speed', 'move_turn_rate', 'hp_bar_offset', 'vision_daytime_range', 'vision_nighttime_range', 'complexity', 'primary_attribute_enum')
    enabled = sgqlc.types.Field(Boolean, graphql_name='enabled')
    hero_unlock_order = sgqlc.types.Field(Float, graphql_name='heroUnlockOrder')
    team = sgqlc.types.Field(Boolean, graphql_name='team')
    c_menabled = sgqlc.types.Field(Boolean, graphql_name='cMEnabled')
    new_player_enabled = sgqlc.types.Field(Boolean, graphql_name='newPlayerEnabled')
    attack_type = sgqlc.types.Field(String, graphql_name='attackType')
    starting_armor = sgqlc.types.Field(Float, graphql_name='startingArmor')
    starting_magic_armor = sgqlc.types.Field(Float, graphql_name='startingMagicArmor')
    starting_damage_min = sgqlc.types.Field(Float, graphql_name='startingDamageMin')
    starting_damage_max = sgqlc.types.Field(Float, graphql_name='startingDamageMax')
    attack_rate = sgqlc.types.Field(Float, graphql_name='attackRate')
    attack_animation_point = sgqlc.types.Field(Float, graphql_name='attackAnimationPoint')
    attack_acquisition_range = sgqlc.types.Field(Float, graphql_name='attackAcquisitionRange')
    attack_range = sgqlc.types.Field(Float, graphql_name='attackRange')
    primary_attribute = sgqlc.types.Field(String, graphql_name='primaryAttribute')
    strength_base = sgqlc.types.Field(Float, graphql_name='strengthBase')
    strength_gain = sgqlc.types.Field(Float, graphql_name='strengthGain')
    intelligence_base = sgqlc.types.Field(Float, graphql_name='intelligenceBase')
    intelligence_gain = sgqlc.types.Field(Float, graphql_name='intelligenceGain')
    agility_base = sgqlc.types.Field(Float, graphql_name='agilityBase')
    agility_gain = sgqlc.types.Field(Float, graphql_name='agilityGain')
    hp_regen = sgqlc.types.Field(Float, graphql_name='hpRegen')
    mp_regen = sgqlc.types.Field(Float, graphql_name='mpRegen')
    move_speed = sgqlc.types.Field(Float, graphql_name='moveSpeed')
    move_turn_rate = sgqlc.types.Field(Float, graphql_name='moveTurnRate')
    hp_bar_offset = sgqlc.types.Field(Float, graphql_name='hpBarOffset')
    vision_daytime_range = sgqlc.types.Field(Float, graphql_name='visionDaytimeRange')
    vision_nighttime_range = sgqlc.types.Field(Float, graphql_name='visionNighttimeRange')
    complexity = sgqlc.types.Field(Byte, graphql_name='complexity')
    primary_attribute_enum = sgqlc.types.Field(HeroPrimaryAttributeType, graphql_name='primaryAttributeEnum')


class HeroStatsHeroDryadType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id1', 'hero_id2', 'week', 'bracket_basic_ids', 'kills', 'match_count', 'deaths', 'assists', 'networth', 'duration', 'win_count', 'first_blood_time', 'cs', 'dn', 'gold_earned', 'xp', 'hero_damage', 'tower_damage', 'hero_healing', 'level', 'synergy', 'win_rate_hero_id1', 'win_rate_hero_id2', 'wins_average')
    hero_id1 = sgqlc.types.Field(Short, graphql_name='heroId1')
    hero_id2 = sgqlc.types.Field(Short, graphql_name='heroId2')
    week = sgqlc.types.Field(Int, graphql_name='week')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    kills = sgqlc.types.Field(Long, graphql_name='kills')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    deaths = sgqlc.types.Field(Long, graphql_name='deaths')
    assists = sgqlc.types.Field(Long, graphql_name='assists')
    networth = sgqlc.types.Field(Long, graphql_name='networth')
    duration = sgqlc.types.Field(Long, graphql_name='duration')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')
    first_blood_time = sgqlc.types.Field(Long, graphql_name='firstBloodTime')
    cs = sgqlc.types.Field(Long, graphql_name='cs')
    dn = sgqlc.types.Field(Long, graphql_name='dn')
    gold_earned = sgqlc.types.Field(Long, graphql_name='goldEarned')
    xp = sgqlc.types.Field(Long, graphql_name='xp')
    hero_damage = sgqlc.types.Field(Long, graphql_name='heroDamage')
    tower_damage = sgqlc.types.Field(Long, graphql_name='towerDamage')
    hero_healing = sgqlc.types.Field(Long, graphql_name='heroHealing')
    level = sgqlc.types.Field(Long, graphql_name='level')
    synergy = sgqlc.types.Field(Decimal, graphql_name='synergy')
    win_rate_hero_id1 = sgqlc.types.Field(Decimal, graphql_name='winRateHeroId1')
    win_rate_hero_id2 = sgqlc.types.Field(Decimal, graphql_name='winRateHeroId2')
    wins_average = sgqlc.types.Field(Decimal, graphql_name='winsAverage')


class HeroStatsQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('stats', 'match_up', 'item_full_purchase', 'item_starting_purchase', 'item_boot_purchase', 'item_neutral', 'lane_outcome', 'hero_vs_hero_matchup', 'talent', 'win_hour', 'win_day', 'win_week', 'win_month', 'win_game_version', 'guide', 'rampages', 'ability_min_level', 'ability_max_level', 'ban_day')
    stats = sgqlc.types.Field(sgqlc.types.list_of(HeroPositionTimeDetailType), graphql_name='stats', args=sgqlc.types.ArgDict((
        ('hero_ids', sgqlc.types.Arg(sgqlc.types.list_of(Short), graphql_name='heroIds', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
        ('group_by_time', sgqlc.types.Arg(Boolean, graphql_name='groupByTime', default=None)),
        ('group_by_position', sgqlc.types.Arg(Boolean, graphql_name='groupByPosition', default=None)),
        ('group_by_bracket', sgqlc.types.Arg(Boolean, graphql_name='groupByBracket', default=None)),
        ('min_time', sgqlc.types.Arg(Int, graphql_name='minTime', default=None)),
        ('max_time', sgqlc.types.Arg(Int, graphql_name='maxTime', default=None)),
))
    )
    match_up = sgqlc.types.Field(sgqlc.types.list_of(HeroDryadType), graphql_name='matchUp', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(Short, graphql_name='heroId', default=None)),
        ('hero_ids', sgqlc.types.Arg(sgqlc.types.list_of(Short), graphql_name='heroIds', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('order_by', sgqlc.types.Arg(Byte, graphql_name='orderBy', default=None)),
        ('match_limit', sgqlc.types.Arg(Int, graphql_name='matchLimit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    item_full_purchase = sgqlc.types.Field(sgqlc.types.list_of(HeroItemPurchaseType), graphql_name='itemFullPurchase', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
        ('min_time', sgqlc.types.Arg(Int, graphql_name='minTime', default=None)),
        ('max_time', sgqlc.types.Arg(Int, graphql_name='maxTime', default=None)),
        ('match_limit', sgqlc.types.Arg(Int, graphql_name='matchLimit', default=None)),
))
    )
    item_starting_purchase = sgqlc.types.Field(sgqlc.types.list_of(HeroItemStartingPurchaseType), graphql_name='itemStartingPurchase', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
))
    )
    item_boot_purchase = sgqlc.types.Field(sgqlc.types.list_of(HeroItemBootPurchaseType), graphql_name='itemBootPurchase', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
))
    )
    item_neutral = sgqlc.types.Field(sgqlc.types.list_of(HeroNeutralItemType), graphql_name='itemNeutral', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
))
    )
    lane_outcome = sgqlc.types.Field(sgqlc.types.list_of(HeroLaneOutcomeType), graphql_name='laneOutcome', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(Short, graphql_name='heroId', default=None)),
        ('is_with', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isWith', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
))
    )
    hero_vs_hero_matchup = sgqlc.types.Field(HeroMatchupType, graphql_name='heroVsHeroMatchup', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('match_limit', sgqlc.types.Arg(Int, graphql_name='matchLimit', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    talent = sgqlc.types.Field(sgqlc.types.list_of(HeroAbilityTalentType), graphql_name='talent', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
))
    )
    win_hour = sgqlc.types.Field(sgqlc.types.list_of('HeroWinHourType'), graphql_name='winHour', args=sgqlc.types.ArgDict((
        ('hero_ids', sgqlc.types.Arg(sgqlc.types.list_of(Short), graphql_name='heroIds', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('bracket_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
        ('region_ids', sgqlc.types.Arg(sgqlc.types.list_of(BasicRegionType), graphql_name='regionIds', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.list_of(GameModeEnumType), graphql_name='gameModeIds', default=None)),
        ('group_by', sgqlc.types.Arg(FilterHeroWinRequestGroupBy, graphql_name='groupBy', default=None)),
))
    )
    win_day = sgqlc.types.Field(sgqlc.types.list_of('HeroWinDayType'), graphql_name='winDay', args=sgqlc.types.ArgDict((
        ('hero_ids', sgqlc.types.Arg(sgqlc.types.list_of(Short), graphql_name='heroIds', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('bracket_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
        ('region_ids', sgqlc.types.Arg(sgqlc.types.list_of(BasicRegionType), graphql_name='regionIds', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.list_of(GameModeEnumType), graphql_name='gameModeIds', default=None)),
        ('group_by', sgqlc.types.Arg(FilterHeroWinRequestGroupBy, graphql_name='groupBy', default=None)),
))
    )
    win_week = sgqlc.types.Field(sgqlc.types.list_of('HeroWinWeekType'), graphql_name='winWeek', args=sgqlc.types.ArgDict((
        ('hero_ids', sgqlc.types.Arg(sgqlc.types.list_of(Short), graphql_name='heroIds', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('bracket_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
        ('region_ids', sgqlc.types.Arg(sgqlc.types.list_of(BasicRegionType), graphql_name='regionIds', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.list_of(GameModeEnumType), graphql_name='gameModeIds', default=None)),
        ('group_by', sgqlc.types.Arg(FilterHeroWinRequestGroupBy, graphql_name='groupBy', default=None)),
))
    )
    win_month = sgqlc.types.Field(sgqlc.types.list_of('HeroWinMonthType'), graphql_name='winMonth', args=sgqlc.types.ArgDict((
        ('hero_ids', sgqlc.types.Arg(sgqlc.types.list_of(Short), graphql_name='heroIds', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('bracket_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
        ('region_ids', sgqlc.types.Arg(sgqlc.types.list_of(BasicRegionType), graphql_name='regionIds', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.list_of(GameModeEnumType), graphql_name='gameModeIds', default=None)),
        ('group_by', sgqlc.types.Arg(FilterHeroWinRequestGroupBy, graphql_name='groupBy', default=None)),
))
    )
    win_game_version = sgqlc.types.Field(sgqlc.types.list_of('HeroWinGameVersionType'), graphql_name='winGameVersion', args=sgqlc.types.ArgDict((
        ('hero_ids', sgqlc.types.Arg(sgqlc.types.list_of(Short), graphql_name='heroIds', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('bracket_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
        ('region_ids', sgqlc.types.Arg(sgqlc.types.list_of(BasicRegionType), graphql_name='regionIds', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.list_of(GameModeEnumType), graphql_name='gameModeIds', default=None)),
        ('group_by', sgqlc.types.Arg(FilterHeroWinRequestGroupBy, graphql_name='groupBy', default=None)),
))
    )
    guide = sgqlc.types.Field(sgqlc.types.list_of(HeroGuideListType), graphql_name='guide', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(Short, graphql_name='heroId', default=None)),
        ('with_hero_id', sgqlc.types.Arg(Short, graphql_name='withHeroId', default=None)),
        ('against_hero_id', sgqlc.types.Arg(Short, graphql_name='againstHeroId', default=None)),
        ('is_pro', sgqlc.types.Arg(Boolean, graphql_name='isPro', default=None)),
        ('position_id', sgqlc.types.Arg(MatchPlayerPositionType, graphql_name='positionId', default=None)),
        ('item_id', sgqlc.types.Arg(Short, graphql_name='itemId', default=None)),
        ('neutral_item_id', sgqlc.types.Arg(Short, graphql_name='neutralItemId', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    rampages = sgqlc.types.Field(sgqlc.types.list_of(HeroRampageObjectType), graphql_name='rampages', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(FilterHeroRampageType), graphql_name='request', default=None)),
))
    )
    ability_min_level = sgqlc.types.Field(sgqlc.types.list_of(HeroAbilityMinType), graphql_name='abilityMinLevel', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
))
    )
    ability_max_level = sgqlc.types.Field(sgqlc.types.list_of(HeroAbilityMaxType), graphql_name='abilityMaxLevel', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('position_ids', sgqlc.types.Arg(sgqlc.types.list_of(MatchPlayerPositionType), graphql_name='positionIds', default=None)),
))
    )
    ban_day = sgqlc.types.Field(sgqlc.types.list_of(HeroBanType), graphql_name='banDay', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('day', sgqlc.types.Arg(Int, graphql_name='day', default=None)),
        ('bracket_basic_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracketBasicEnum), graphql_name='bracketBasicIds', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('group_by_day', sgqlc.types.Arg(Boolean, graphql_name='groupByDay', default=None)),
        ('group_by_rank', sgqlc.types.Arg(Boolean, graphql_name='groupByRank', default=None)),
))
    )


class HeroTalentType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('ability_id', 'slot')
    ability_id = sgqlc.types.Field(Short, graphql_name='abilityId')
    slot = sgqlc.types.Field(Byte, graphql_name='slot')


class HeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'display_name', 'short_name', 'aliases', 'game_version_id', 'abilities', 'roles', 'language', 'talents', 'facets', 'stats')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    short_name = sgqlc.types.Field(String, graphql_name='shortName')
    aliases = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='aliases')
    game_version_id = sgqlc.types.Field(Short, graphql_name='gameVersionId')
    abilities = sgqlc.types.Field(sgqlc.types.list_of(HeroAbilityType), graphql_name='abilities')
    roles = sgqlc.types.Field(sgqlc.types.list_of(HeroRoleType), graphql_name='roles')
    language = sgqlc.types.Field(HeroLanguageType, graphql_name='language')
    talents = sgqlc.types.Field(sgqlc.types.list_of(HeroTalentType), graphql_name='talents')
    facets = sgqlc.types.Field(sgqlc.types.list_of(HeroFacetType), graphql_name='facets')
    stats = sgqlc.types.Field(HeroStatType, graphql_name='stats')


class HeroWinDayType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('day', 'hero_id', 'win_count', 'match_count')
    day = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='day')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')


class HeroWinGameVersionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('game_version_id', 'hero_id', 'duration_minute', 'win_count', 'match_count')
    game_version_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='gameVersionId')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId')
    duration_minute = sgqlc.types.Field(sgqlc.types.non_null(Byte), graphql_name='durationMinute')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')


class HeroWinHourType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hour', 'hero_id', 'win_count', 'match_count')
    hour = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='hour')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')


class HeroWinMonthType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('month', 'hero_id', 'duration_minute', 'win_count', 'match_count')
    month = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='month')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId')
    duration_minute = sgqlc.types.Field(sgqlc.types.non_null(Byte), graphql_name='durationMinute')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')


class HeroWinWeekType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('week', 'hero_id', 'duration_minute', 'win_count', 'match_count')
    week = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='week')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId')
    duration_minute = sgqlc.types.Field(sgqlc.types.non_null(Byte), graphql_name='durationMinute')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')


class HomepageHeroDryadType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('main_hero_id', 'comparison_hero_id', 'bracket_basic_ids', 'match_count', 'win_count', 'synergy', 'wins_average', 'comparison_hero_base_win_rate')
    main_hero_id = sgqlc.types.Field(Short, graphql_name='mainHeroId')
    comparison_hero_id = sgqlc.types.Field(Short, graphql_name='comparisonHeroId')
    bracket_basic_ids = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='bracketBasicIds')
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Long, graphql_name='winCount')
    synergy = sgqlc.types.Field(Decimal, graphql_name='synergy')
    wins_average = sgqlc.types.Field(Decimal, graphql_name='winsAverage')
    comparison_hero_base_win_rate = sgqlc.types.Field(Decimal, graphql_name='comparisonHeroBaseWinRate')


class HomepageHeroSynergyType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('main_hero_id', 'main_hero_base_win_rate', 'hero_dryads')
    main_hero_id = sgqlc.types.Field(Short, graphql_name='mainHeroId')
    main_hero_base_win_rate = sgqlc.types.Field(Decimal, graphql_name='mainHeroBaseWinRate')
    hero_dryads = sgqlc.types.Field(sgqlc.types.list_of(HomepageHeroDryadType), graphql_name='heroDryads')


class ImpGeneratorMatchPlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('win_chance', 'win_rate_by_player_minute_values', 'events', 'imp_values')
    win_chance = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='winChance')
    win_rate_by_player_minute_values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(Float)), graphql_name='winRateByPlayerMinuteValues')
    events = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of('ImpGeneratorPlayerEventType')), graphql_name='events')
    imp_values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(Int)), graphql_name='impValues')


class ImpGeneratorPlayerEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'kills', 'deaths', 'assists', 'cs', 'dn', 'level', 'physical_damage', 'magical_damage', 'pure_damage', 'damage_received', 'healing_allies', 'rune_power', 'neutrals')
    time = sgqlc.types.Field(Byte, graphql_name='time')
    kills = sgqlc.types.Field(UShort, graphql_name='kills')
    deaths = sgqlc.types.Field(UShort, graphql_name='deaths')
    assists = sgqlc.types.Field(UShort, graphql_name='assists')
    cs = sgqlc.types.Field(UShort, graphql_name='cs')
    dn = sgqlc.types.Field(UShort, graphql_name='dn')
    level = sgqlc.types.Field(Byte, graphql_name='level')
    physical_damage = sgqlc.types.Field(Int, graphql_name='physicalDamage')
    magical_damage = sgqlc.types.Field(Int, graphql_name='magicalDamage')
    pure_damage = sgqlc.types.Field(Int, graphql_name='pureDamage')
    damage_received = sgqlc.types.Field(Int, graphql_name='damageReceived')
    healing_allies = sgqlc.types.Field(Int, graphql_name='healingAllies')
    rune_power = sgqlc.types.Field(Int, graphql_name='runePower')
    neutrals = sgqlc.types.Field(Int, graphql_name='neutrals')


class ImpGeneratorPlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('win_chance', 'win_rate_by_player_minute_values', 'events', 'imp_values')
    win_chance = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='winChance')
    win_rate_by_player_minute_values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(Float)), graphql_name='winRateByPlayerMinuteValues')
    events = sgqlc.types.Field(sgqlc.types.list_of(ImpGeneratorPlayerEventType), graphql_name='events')
    imp_values = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.list_of(Int)), graphql_name='impValues')


class ImpQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_generator', 'player_generator')
    match_generator = sgqlc.types.Field(ImpGeneratorMatchPlayerType, graphql_name='matchGenerator', args=sgqlc.types.ArgDict((
        ('match_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchId', default=None)),
))
    )
    player_generator = sgqlc.types.Field(ImpGeneratorPlayerType, graphql_name='playerGenerator', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(ImpGeneratorRequestType), graphql_name='request', default=None)),
))
    )


class InventoryObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('item_id', 'charges', 'secondary_charges')
    item_id = sgqlc.types.Field(Short, graphql_name='itemId')
    charges = sgqlc.types.Field(Int, graphql_name='charges')
    secondary_charges = sgqlc.types.Field(Int, graphql_name='secondaryCharges')


class InventoryType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'back_pack0', 'back_pack1', 'back_pack2', 'teleport0', 'neutral0')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    item0 = sgqlc.types.Field(InventoryObjectType, graphql_name='item0')
    item1 = sgqlc.types.Field(InventoryObjectType, graphql_name='item1')
    item2 = sgqlc.types.Field(InventoryObjectType, graphql_name='item2')
    item3 = sgqlc.types.Field(InventoryObjectType, graphql_name='item3')
    item4 = sgqlc.types.Field(InventoryObjectType, graphql_name='item4')
    item5 = sgqlc.types.Field(InventoryObjectType, graphql_name='item5')
    back_pack0 = sgqlc.types.Field(InventoryObjectType, graphql_name='backPack0')
    back_pack1 = sgqlc.types.Field(InventoryObjectType, graphql_name='backPack1')
    back_pack2 = sgqlc.types.Field(InventoryObjectType, graphql_name='backPack2')
    teleport0 = sgqlc.types.Field(InventoryObjectType, graphql_name='teleport0')
    neutral0 = sgqlc.types.Field(InventoryObjectType, graphql_name='neutral0')


class IpGeoLookupType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('query', 'status', 'continent', 'continent_code', 'country', 'country_code', 'region', 'region_name', 'city', 'district', 'zip', 'lat', 'lon', 'timezone', 'offset', 'currency', 'isp', 'org', 'as_', 'as_name', 'mobile', 'proxy', 'hosting')
    query = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='query')
    status = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='status')
    continent = sgqlc.types.Field(String, graphql_name='continent')
    continent_code = sgqlc.types.Field(String, graphql_name='continentCode')
    country = sgqlc.types.Field(String, graphql_name='country')
    country_code = sgqlc.types.Field(String, graphql_name='countryCode')
    region = sgqlc.types.Field(String, graphql_name='region')
    region_name = sgqlc.types.Field(String, graphql_name='regionName')
    city = sgqlc.types.Field(String, graphql_name='city')
    district = sgqlc.types.Field(String, graphql_name='district')
    zip = sgqlc.types.Field(String, graphql_name='zip')
    lat = sgqlc.types.Field(Float, graphql_name='lat')
    lon = sgqlc.types.Field(Float, graphql_name='lon')
    timezone = sgqlc.types.Field(String, graphql_name='timezone')
    offset = sgqlc.types.Field(Int, graphql_name='offset')
    currency = sgqlc.types.Field(String, graphql_name='currency')
    isp = sgqlc.types.Field(String, graphql_name='isp')
    org = sgqlc.types.Field(String, graphql_name='org')
    as_ = sgqlc.types.Field(String, graphql_name='as')
    as_name = sgqlc.types.Field(String, graphql_name='asName')
    mobile = sgqlc.types.Field(Boolean, graphql_name='mobile')
    proxy = sgqlc.types.Field(Boolean, graphql_name='proxy')
    hosting = sgqlc.types.Field(Boolean, graphql_name='hosting')


class ItemAttributeType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('name', 'value')
    name = sgqlc.types.Field(String, graphql_name='name')
    value = sgqlc.types.Field(String, graphql_name='value')


class ItemComponentType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('index', 'component_id')
    index = sgqlc.types.Field(Byte, graphql_name='index')
    component_id = sgqlc.types.Field(Short, graphql_name='componentId')


class ItemLanguageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('display_name', 'description', 'lore', 'notes', 'attributes')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    description = sgqlc.types.Field(String, graphql_name='description')
    lore = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='lore')
    notes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='notes')
    attributes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='attributes')


class ItemPurchaseType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'item_id')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    item_id = sgqlc.types.Field(Short, graphql_name='itemId')


class ItemStatType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('behavior', 'unit_target_type', 'unit_target_team', 'unit_target_flags', 'fight_recap_level', 'cast_range', 'cast_point', 'mana_cost', 'channel_time', 'shared_cooldown', 'cost', 'shop_tags', 'aliases', 'quality', 'is_sellable', 'is_droppable', 'is_purchasable', 'is_side_shop', 'is_stackable', 'is_permanent', 'is_hide_charges', 'is_requires_charges', 'is_display_charges', 'is_support', 'is_alertable', 'is_tempest_double_clonable', 'stock_max', 'initial_charges', 'initial_stock', 'stock_time', 'initial_stock_time', 'is_recipe', 'needs_components', 'upgrade_item', 'upgrade_recipe', 'item_result', 'neutral_item_drop_time', 'neutral_item_tier')
    behavior = sgqlc.types.Field(Long, graphql_name='behavior')
    unit_target_type = sgqlc.types.Field(Long, graphql_name='unitTargetType')
    unit_target_team = sgqlc.types.Field(Long, graphql_name='unitTargetTeam')
    unit_target_flags = sgqlc.types.Field(Long, graphql_name='unitTargetFlags')
    fight_recap_level = sgqlc.types.Field(Byte, graphql_name='fightRecapLevel')
    cast_range = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='castRange')
    cast_point = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='castPoint')
    mana_cost = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='manaCost')
    channel_time = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='channelTime')
    shared_cooldown = sgqlc.types.Field(String, graphql_name='sharedCooldown')
    cost = sgqlc.types.Field(Int, graphql_name='cost')
    shop_tags = sgqlc.types.Field(String, graphql_name='shopTags')
    aliases = sgqlc.types.Field(String, graphql_name='aliases')
    quality = sgqlc.types.Field(String, graphql_name='quality')
    is_sellable = sgqlc.types.Field(Boolean, graphql_name='isSellable')
    is_droppable = sgqlc.types.Field(Boolean, graphql_name='isDroppable')
    is_purchasable = sgqlc.types.Field(Boolean, graphql_name='isPurchasable')
    is_side_shop = sgqlc.types.Field(Boolean, graphql_name='isSideShop')
    is_stackable = sgqlc.types.Field(Boolean, graphql_name='isStackable')
    is_permanent = sgqlc.types.Field(Boolean, graphql_name='isPermanent')
    is_hide_charges = sgqlc.types.Field(Boolean, graphql_name='isHideCharges')
    is_requires_charges = sgqlc.types.Field(Boolean, graphql_name='isRequiresCharges')
    is_display_charges = sgqlc.types.Field(Boolean, graphql_name='isDisplayCharges')
    is_support = sgqlc.types.Field(Boolean, graphql_name='isSupport')
    is_alertable = sgqlc.types.Field(Boolean, graphql_name='isAlertable')
    is_tempest_double_clonable = sgqlc.types.Field(Boolean, graphql_name='isTempestDoubleClonable')
    stock_max = sgqlc.types.Field(Short, graphql_name='stockMax')
    initial_charges = sgqlc.types.Field(Short, graphql_name='initialCharges')
    initial_stock = sgqlc.types.Field(Short, graphql_name='initialStock')
    stock_time = sgqlc.types.Field(Int, graphql_name='stockTime')
    initial_stock_time = sgqlc.types.Field(Short, graphql_name='initialStockTime')
    is_recipe = sgqlc.types.Field(Boolean, graphql_name='isRecipe')
    needs_components = sgqlc.types.Field(Boolean, graphql_name='needsComponents')
    upgrade_item = sgqlc.types.Field(Short, graphql_name='upgradeItem')
    upgrade_recipe = sgqlc.types.Field(Short, graphql_name='upgradeRecipe')
    item_result = sgqlc.types.Field(Short, graphql_name='itemResult')
    neutral_item_drop_time = sgqlc.types.Field(Short, graphql_name='neutralItemDropTime')
    neutral_item_tier = sgqlc.types.Field(NeutralItemTierEnum, graphql_name='neutralItemTier')


class ItemType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'display_name', 'short_name', 'is_support_full_item', 'language', 'stat', 'attributes', 'components', 'image')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    short_name = sgqlc.types.Field(String, graphql_name='shortName')
    is_support_full_item = sgqlc.types.Field(Boolean, graphql_name='isSupportFullItem')
    language = sgqlc.types.Field(ItemLanguageType, graphql_name='language')
    stat = sgqlc.types.Field(ItemStatType, graphql_name='stat')
    attributes = sgqlc.types.Field(sgqlc.types.list_of(ItemAttributeType), graphql_name='attributes')
    components = sgqlc.types.Field(sgqlc.types.list_of(ItemComponentType), graphql_name='components')
    image = sgqlc.types.Field(String, graphql_name='image')


class ItemUsedEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'item_id', 'attacker', 'target')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    item_id = sgqlc.types.Field(Short, graphql_name='itemId')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')
    target = sgqlc.types.Field(Short, graphql_name='target')


class KillDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'attacker', 'is_from_illusion', 'target', 'by_ability', 'by_item', 'gold', 'xp', 'position_x', 'position_y', 'assist', 'is_solo', 'is_gank', 'is_invisible', 'is_smoke', 'is_tp_recently', 'is_rune_effected')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')
    is_from_illusion = sgqlc.types.Field(Boolean, graphql_name='isFromIllusion')
    target = sgqlc.types.Field(Short, graphql_name='target')
    by_ability = sgqlc.types.Field(Short, graphql_name='byAbility')
    by_item = sgqlc.types.Field(Short, graphql_name='byItem')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    xp = sgqlc.types.Field(Int, graphql_name='xp')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')
    assist = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='assist')
    is_solo = sgqlc.types.Field(Boolean, graphql_name='isSolo')
    is_gank = sgqlc.types.Field(Boolean, graphql_name='isGank')
    is_invisible = sgqlc.types.Field(Boolean, graphql_name='isInvisible')
    is_smoke = sgqlc.types.Field(Boolean, graphql_name='isSmoke')
    is_tp_recently = sgqlc.types.Field(Boolean, graphql_name='isTpRecently')
    is_rune_effected = sgqlc.types.Field(Boolean, graphql_name='isRuneEffected')


class LanguageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'language_code', 'displa_language_namey_name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Byte), graphql_name='id')
    language_code = sgqlc.types.Field(String, graphql_name='languageCode')
    displa_language_namey_name = sgqlc.types.Field(String, graphql_name='displaLanguageNameyName')


class LastHitDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'attacker', 'is_from_illusion', 'npc_id', 'by_ability', 'by_item', 'gold', 'xp', 'position_x', 'position_y', 'is_creep', 'is_neutral', 'is_ancient', 'map_location')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')
    is_from_illusion = sgqlc.types.Field(Boolean, graphql_name='isFromIllusion')
    npc_id = sgqlc.types.Field(Short, graphql_name='npcId')
    by_ability = sgqlc.types.Field(Short, graphql_name='byAbility')
    by_item = sgqlc.types.Field(Short, graphql_name='byItem')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    xp = sgqlc.types.Field(Int, graphql_name='xp')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')
    is_creep = sgqlc.types.Field(Boolean, graphql_name='isCreep')
    is_neutral = sgqlc.types.Field(Boolean, graphql_name='isNeutral')
    is_ancient = sgqlc.types.Field(Boolean, graphql_name='isAncient')
    map_location = sgqlc.types.Field(MapLocationEnums, graphql_name='mapLocation')


class LeaderboardQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('season', 'dota_plus', 'dota_plus_week', 'dota_plus_top_levels', 'battle_pass', 'battle_pass_group_by', 'coaching', 'guild', 'hero')
    season = sgqlc.types.Field('SteamAccountSeasonActiveLeaderboardType', graphql_name='season', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(FilterSeasonLeaderboardRequestType, graphql_name='request', default=None)),
))
    )
    dota_plus = sgqlc.types.Field('PlayerHeroDotaPlusLeaderboardRankResponseType', graphql_name='dotaPlus', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(Short, graphql_name='heroId', default=None)),
        ('order_by', sgqlc.types.Arg(FilterLeaderboardOrder, graphql_name='orderBy', default=None)),
        ('level', sgqlc.types.Arg(Byte, graphql_name='level', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    dota_plus_week = sgqlc.types.Field(sgqlc.types.list_of(DotaPlusWeekType), graphql_name='dotaPlusWeek')
    dota_plus_top_levels = sgqlc.types.Field(sgqlc.types.list_of(HeroDotaPlusLeaderboardRankTopType), graphql_name='dotaPlusTopLevels')
    battle_pass = sgqlc.types.Field('PlayerBattlePassResponseType', graphql_name='battlePass', args=sgqlc.types.ArgDict((
        ('event_id', sgqlc.types.Arg(Byte, graphql_name='eventId', default=None)),
        ('country_code', sgqlc.types.Arg(String, graphql_name='countryCode', default=None)),
        ('levels', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='levels', default=None)),
))
    )
    battle_pass_group_by = sgqlc.types.Field(sgqlc.types.list_of('PlayerBattlePassGroupByType'), graphql_name='battlePassGroupBy', args=sgqlc.types.ArgDict((
        ('group_by', sgqlc.types.Arg(sgqlc.types.non_null(PlayerBattlePassGroupByEnum), graphql_name='groupBy', default=None)),
        ('player_count_at', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='playerCountAt', default=None)),
        ('event_id', sgqlc.types.Arg(Byte, graphql_name='eventId', default=None)),
        ('country_code', sgqlc.types.Arg(String, graphql_name='countryCode', default=None)),
))
    )
    coaching = sgqlc.types.Field('PlayerCoachingLeaderboardResponseType', graphql_name='coaching', args=sgqlc.types.ArgDict((
        ('levels', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='levels', default=None)),
))
    )
    guild = sgqlc.types.Field(sgqlc.types.list_of(GuildType), graphql_name='guild', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(FilterLeaderboardGuildRequestType, graphql_name='request', default=None)),
))
    )
    hero = sgqlc.types.Field(sgqlc.types.list_of('PlayerLeaderBoardByHeroType'), graphql_name='hero', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(FilterLeaderboardHeroRequestType, graphql_name='request', default=None)),
))
    )


class LeagueBattlePassType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('count', 'average')
    count = sgqlc.types.Field(Int, graphql_name='count')
    average = sgqlc.types.Field(Int, graphql_name='average')


class LeagueDpcPositionStatObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('position', 'match_count', 'avg_kills', 'avg_deaths', 'avg_assists')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')


class LeagueMetaDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'win_count', 'loss_count', 'win_rate', 'pick_rate', 'pick_count', 'ban_rate', 'ban_count')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    loss_count = sgqlc.types.Field(Int, graphql_name='lossCount')
    win_rate = sgqlc.types.Field(Decimal, graphql_name='winRate')
    pick_rate = sgqlc.types.Field(Decimal, graphql_name='pickRate')
    pick_count = sgqlc.types.Field(Int, graphql_name='pickCount')
    ban_rate = sgqlc.types.Field(Decimal, graphql_name='banRate')
    ban_count = sgqlc.types.Field(Int, graphql_name='banCount')


class LeagueMetaType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('league_id', 'best_record', 'most_picked', 'most_banned', 'missing_match_count', 'total_match_count', 'league')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    best_record = sgqlc.types.Field(LeagueMetaDetailType, graphql_name='bestRecord')
    most_picked = sgqlc.types.Field(LeagueMetaDetailType, graphql_name='mostPicked')
    most_banned = sgqlc.types.Field(LeagueMetaDetailType, graphql_name='mostBanned')
    missing_match_count = sgqlc.types.Field(Int, graphql_name='missingMatchCount')
    total_match_count = sgqlc.types.Field(Int, graphql_name='totalMatchCount')
    league = sgqlc.types.Field('LeagueType', graphql_name='league')


class LeagueNodeGroupType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'parent_node_group_id', 'advancing_node_group_id', 'advancing_team_count', 'team_count', 'default_node_type', 'node_group_type', 'round', 'max_rounds', 'is_tie_breaker', 'is_final_group', 'is_completed', 'phase', 'region', 'start_date', 'end_date', 'secondary_advancing_node_group_id', 'secondary_advancing_team_count', 'tertiary_advancing_node_group_id', 'tertiary_advancing_team_count', 'elimination_dpcpoints', 'nodes')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    parent_node_group_id = sgqlc.types.Field(Short, graphql_name='parentNodeGroupId')
    advancing_node_group_id = sgqlc.types.Field(Short, graphql_name='advancingNodeGroupId')
    advancing_team_count = sgqlc.types.Field(Byte, graphql_name='advancingTeamCount')
    team_count = sgqlc.types.Field(Byte, graphql_name='teamCount')
    default_node_type = sgqlc.types.Field(LeagueNodeDefaultGroupEnum, graphql_name='defaultNodeType')
    node_group_type = sgqlc.types.Field(LeagueNodeGroupTypeEnum, graphql_name='nodeGroupType')
    round = sgqlc.types.Field(Byte, graphql_name='round')
    max_rounds = sgqlc.types.Field(Byte, graphql_name='maxRounds')
    is_tie_breaker = sgqlc.types.Field(Boolean, graphql_name='isTieBreaker')
    is_final_group = sgqlc.types.Field(Boolean, graphql_name='isFinalGroup')
    is_completed = sgqlc.types.Field(Boolean, graphql_name='isCompleted')
    phase = sgqlc.types.Field(Byte, graphql_name='phase')
    region = sgqlc.types.Field(Byte, graphql_name='region')
    start_date = sgqlc.types.Field(Long, graphql_name='startDate')
    end_date = sgqlc.types.Field(Long, graphql_name='endDate')
    secondary_advancing_node_group_id = sgqlc.types.Field(Short, graphql_name='secondaryAdvancingNodeGroupId')
    secondary_advancing_team_count = sgqlc.types.Field(Byte, graphql_name='secondaryAdvancingTeamCount')
    tertiary_advancing_node_group_id = sgqlc.types.Field(Short, graphql_name='tertiaryAdvancingNodeGroupId')
    tertiary_advancing_team_count = sgqlc.types.Field(Byte, graphql_name='tertiaryAdvancingTeamCount')
    elimination_dpcpoints = sgqlc.types.Field(Int, graphql_name='eliminationDPCPoints')
    nodes = sgqlc.types.Field(sgqlc.types.list_of('LeagueNodeType'), graphql_name='nodes')


class LeagueNodeType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('node_group_id', 'id', 'name', 'winning_node_id', 'losing_node_id', 'node_type', 'scheduled_time', 'actual_time', 'series_id', 'matches', 'team_one_id', 'team_one', 'team_two_id', 'team_two', 'team_one_wins', 'team_two_wins', 'has_started', 'is_completed', 'stream_ids', 'streams')
    node_group_id = sgqlc.types.Field(Short, graphql_name='nodeGroupId')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    winning_node_id = sgqlc.types.Field(Short, graphql_name='winningNodeId')
    losing_node_id = sgqlc.types.Field(Short, graphql_name='losingNodeId')
    node_type = sgqlc.types.Field(LeagueNodeDefaultGroupEnum, graphql_name='nodeType')
    scheduled_time = sgqlc.types.Field(Long, graphql_name='scheduledTime')
    actual_time = sgqlc.types.Field(Long, graphql_name='actualTime')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    matches = sgqlc.types.Field(sgqlc.types.list_of('MatchType'), graphql_name='matches')
    team_one_id = sgqlc.types.Field(Int, graphql_name='teamOneId')
    team_one = sgqlc.types.Field('TeamType', graphql_name='teamOne')
    team_two_id = sgqlc.types.Field(Int, graphql_name='teamTwoId')
    team_two = sgqlc.types.Field('TeamType', graphql_name='teamTwo')
    team_one_wins = sgqlc.types.Field(Byte, graphql_name='teamOneWins')
    team_two_wins = sgqlc.types.Field(Byte, graphql_name='teamTwoWins')
    has_started = sgqlc.types.Field(Boolean, graphql_name='hasStarted')
    is_completed = sgqlc.types.Field(Boolean, graphql_name='isCompleted')
    stream_ids = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='streamIds')
    streams = sgqlc.types.Field(sgqlc.types.list_of('LeagueStreamType'), graphql_name='streams')


class LeaguePrizePoolPercentageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('league_id', 'index', 'percentage')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    index = sgqlc.types.Field(Byte, graphql_name='index')
    percentage = sgqlc.types.Field(Int, graphql_name='percentage')


class LeagueRegisteredPlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('league_id', 'league', 'team_id', 'radiant_team', 'steam_account_id', 'steam_account')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    league = sgqlc.types.Field('LeagueType', graphql_name='league')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    radiant_team = sgqlc.types.Field('TeamType', graphql_name='radiantTeam')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')


class LeagueStatType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_count', 'radiant_win_match_count', 'average_match_duration_seconds')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    radiant_win_match_count = sgqlc.types.Field(Int, graphql_name='radiantWinMatchCount')
    average_match_duration_seconds = sgqlc.types.Field(Int, graphql_name='averageMatchDurationSeconds')


class LeagueStreamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'language_id', 'name', 'broadcast_provider', 'stream_url', 'vod_url')
    id = sgqlc.types.Field(Int, graphql_name='id')
    language_id = sgqlc.types.Field(LanguageEnum, graphql_name='languageId')
    name = sgqlc.types.Field(String, graphql_name='name')
    broadcast_provider = sgqlc.types.Field(Byte, graphql_name='broadcastProvider')
    stream_url = sgqlc.types.Field(String, graphql_name='streamUrl')
    vod_url = sgqlc.types.Field(String, graphql_name='vodUrl')


class LeagueTableHeroLanesObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'match_count', 'match_wins')
    id = sgqlc.types.Field(Byte, graphql_name='id')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    match_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchWins')


class LeagueTableHeroOverviewType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_count', 'match_wins', 'pick_phase_one', 'pick_phase_two', 'pick_phase_three', 'ban_count', 'ban_phase_one', 'ban_phase_two', 'ban_phase_three')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    match_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchWins')
    pick_phase_one = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pickPhaseOne')
    pick_phase_two = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pickPhaseTwo')
    pick_phase_three = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pickPhaseThree')
    ban_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='banCount')
    ban_phase_one = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='banPhaseOne')
    ban_phase_two = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='banPhaseTwo')
    ban_phase_three = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='banPhaseThree')


class LeagueTableHeroPlayersObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_id', 'match_count', 'match_wins', 'imp', 'kills', 'deaths', 'assists', 'cs', 'gpm', 'xpm', 'heal', 'hero_damage', 'tower_damage', 'kill_contribution')
    steam_id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='steamId')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    match_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchWins')
    imp = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='imp')
    kills = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='kills')
    deaths = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='deaths')
    assists = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='assists')
    cs = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cs')
    gpm = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='gpm')
    xpm = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xpm')
    heal = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='heal')
    hero_damage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='heroDamage')
    tower_damage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='towerDamage')
    kill_contribution = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='killContribution')


class LeagueTableHeroStatsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('kills', 'deaths', 'assists', 'cs', 'gpm', 'xpm', 'heal', 'hero_damage', 'tower_damage', 'kill_contribution')
    kills = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='kills')
    deaths = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='deaths')
    assists = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='assists')
    cs = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cs')
    gpm = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='gpm')
    xpm = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xpm')
    heal = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='heal')
    hero_damage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='heroDamage')
    tower_damage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='towerDamage')
    kill_contribution = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='killContribution')


class LeagueTableHeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'overview', 'stats', 'heroes', 'lanes')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    overview = sgqlc.types.Field(LeagueTableHeroOverviewType, graphql_name='overview')
    stats = sgqlc.types.Field(LeagueTableHeroStatsType, graphql_name='stats')
    heroes = sgqlc.types.Field(sgqlc.types.list_of(LeagueTableHeroPlayersObjectType), graphql_name='heroes')
    lanes = sgqlc.types.Field(sgqlc.types.list_of(LeagueTableHeroLanesObjectType), graphql_name='lanes')


class LeagueTablePlayerHeroesObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'match_count', 'match_wins', 'imp')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    match_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchWins')
    imp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='imp')


class LeagueTablePlayerLanesObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'match_count', 'match_wins')
    id = sgqlc.types.Field(Byte, graphql_name='id')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    match_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchWins')


class LeagueTablePlayerOverviewType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('points', 'earnings', 'series_count', 'series_wins', 'match_count', 'match_wins', 'imp')
    points = sgqlc.types.Field(Float, graphql_name='points')
    earnings = sgqlc.types.Field(Float, graphql_name='earnings')
    series_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seriesCount')
    series_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seriesWins')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    match_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchWins')
    imp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='imp')


class LeagueTablePlayerStatsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('kills', 'deaths', 'assists', 'cs', 'gpm', 'xpm', 'heal', 'hero_damage', 'tower_damage', 'kill_contribution')
    kills = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='kills')
    deaths = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='deaths')
    assists = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='assists')
    cs = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cs')
    gpm = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='gpm')
    xpm = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xpm')
    heal = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='heal')
    hero_damage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='heroDamage')
    tower_damage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='towerDamage')
    kill_contribution = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='killContribution')


class LeagueTablePlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'overview', 'stats', 'heroes', 'lanes')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    overview = sgqlc.types.Field(LeagueTablePlayerOverviewType, graphql_name='overview')
    stats = sgqlc.types.Field(LeagueTablePlayerStatsType, graphql_name='stats')
    heroes = sgqlc.types.Field(sgqlc.types.list_of(LeagueTablePlayerHeroesObjectType), graphql_name='heroes')
    lanes = sgqlc.types.Field(sgqlc.types.list_of(LeagueTablePlayerLanesObjectType), graphql_name='lanes')


class LeagueTableTeamHeroesObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'match_count', 'match_wins', 'imp', 'ban_count')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    match_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchWins')
    imp = sgqlc.types.Field(Decimal, graphql_name='imp')
    ban_count = sgqlc.types.Field(Int, graphql_name='banCount')


class LeagueTableTeamLanesObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'match_count', 'match_wins')
    id = sgqlc.types.Field(Byte, graphql_name='id')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    match_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchWins')


class LeagueTableTeamOverviewType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('points', 'earnings', 'series_count', 'series_wins', 'series_draws', 'match_count', 'match_wins', 'tmp')
    points = sgqlc.types.Field(Float, graphql_name='points')
    earnings = sgqlc.types.Field(Float, graphql_name='earnings')
    series_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seriesCount')
    series_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seriesWins')
    series_draws = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='seriesDraws')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    match_wins = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchWins')
    tmp = sgqlc.types.Field(Float, graphql_name='tmp')


class LeagueTableTeamStatsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('kills', 'deaths', 'assists', 'cs', 'gpm', 'xpm', 'heal', 'hero_damage', 'tower_damage', 'duration')
    kills = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='kills')
    deaths = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='deaths')
    assists = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='assists')
    cs = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='cs')
    gpm = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='gpm')
    xpm = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='xpm')
    heal = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='heal')
    hero_damage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='heroDamage')
    tower_damage = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='towerDamage')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='duration')


class LeagueTableTeamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('team_id', 'team', 'members', 'overview', 'stats', 'heroes', 'lanes')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    members = sgqlc.types.Field(sgqlc.types.list_of(LeagueRegisteredPlayerType), graphql_name='members')
    overview = sgqlc.types.Field(LeagueTableTeamOverviewType, graphql_name='overview')
    stats = sgqlc.types.Field(LeagueTableTeamStatsType, graphql_name='stats')
    heroes = sgqlc.types.Field(sgqlc.types.list_of(LeagueTableTeamHeroesObjectType), graphql_name='heroes')
    lanes = sgqlc.types.Field(sgqlc.types.list_of(LeagueTableTeamLanesObjectType), graphql_name='lanes')


class LeagueTableType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('league_id', 'table_teams', 'table_heroes', 'table_players')
    league_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='leagueId')
    table_teams = sgqlc.types.Field(sgqlc.types.list_of(LeagueTableTeamType), graphql_name='tableTeams')
    table_heroes = sgqlc.types.Field(sgqlc.types.list_of(LeagueTableHeroType), graphql_name='tableHeroes')
    table_players = sgqlc.types.Field(sgqlc.types.list_of(LeagueTablePlayerType), graphql_name='tablePlayers')


class LeagueType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'banner', 'base_prize_pool', 'stop_sales_time', 'tier', 'region', 'private', 'free_to_spectate', 'start_date_time', 'end_date_time', 'tournament_url', 'last_match_date', 'has_live_matches', 'prize_pool', 'image_uri', 'display_name', 'description', 'country', 'venue', 'is_followed', 'node_groups', 'live_matches', 'matches', 'matches_group_by', 'series', 'tables', 'battle_pass', 'stats', 'prize_pool_percentages', 'standings', 'streams')
    id = sgqlc.types.Field(Int, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    banner = sgqlc.types.Field(String, graphql_name='banner')
    base_prize_pool = sgqlc.types.Field(Int, graphql_name='basePrizePool')
    stop_sales_time = sgqlc.types.Field(DateTime, graphql_name='stopSalesTime')
    tier = sgqlc.types.Field(LeagueTier, graphql_name='tier')
    region = sgqlc.types.Field(LeagueRegion, graphql_name='region')
    private = sgqlc.types.Field(Boolean, graphql_name='private')
    free_to_spectate = sgqlc.types.Field(Boolean, graphql_name='freeToSpectate')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    tournament_url = sgqlc.types.Field(String, graphql_name='tournamentUrl')
    last_match_date = sgqlc.types.Field(Long, graphql_name='lastMatchDate')
    has_live_matches = sgqlc.types.Field(Boolean, graphql_name='hasLiveMatches')
    prize_pool = sgqlc.types.Field(Int, graphql_name='prizePool')
    image_uri = sgqlc.types.Field(String, graphql_name='imageUri')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    description = sgqlc.types.Field(String, graphql_name='description')
    country = sgqlc.types.Field(String, graphql_name='country')
    venue = sgqlc.types.Field(String, graphql_name='venue')
    is_followed = sgqlc.types.Field(Boolean, graphql_name='isFollowed')
    node_groups = sgqlc.types.Field(sgqlc.types.list_of(LeagueNodeGroupType), graphql_name='nodeGroups')
    live_matches = sgqlc.types.Field(sgqlc.types.list_of('MatchLiveType'), graphql_name='liveMatches')
    matches = sgqlc.types.Field(sgqlc.types.list_of('MatchType'), graphql_name='matches', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(LeagueMatchesRequestType), graphql_name='request', default=None)),
))
    )
    matches_group_by = sgqlc.types.Field(sgqlc.types.list_of('MatchGroupByType'), graphql_name='matchesGroupBy', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlayerMatchesGroupByRequestType), graphql_name='request', default=None)),
))
    )
    series = sgqlc.types.Field(sgqlc.types.list_of('SeriesType'), graphql_name='series', args=sgqlc.types.ArgDict((
        ('league_stage_type_ids', sgqlc.types.Arg(sgqlc.types.list_of(LeagueStage), graphql_name='leagueStageTypeIds', default=None)),
        ('series_id', sgqlc.types.Arg(Int, graphql_name='seriesId', default=None)),
        ('team_id', sgqlc.types.Arg(Int, graphql_name='teamId', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    tables = sgqlc.types.Field(LeagueTableType, graphql_name='tables', args=sgqlc.types.ArgDict((
        ('league_stage_type_ids', sgqlc.types.Arg(sgqlc.types.list_of(LeagueStage), graphql_name='leagueStageTypeIds', default=None)),
        ('calculate_type_id', sgqlc.types.Arg(TableCalculateEnum, graphql_name='calculateTypeId', default=None)),
))
    )
    battle_pass = sgqlc.types.Field(LeagueBattlePassType, graphql_name='battlePass')
    stats = sgqlc.types.Field(LeagueStatType, graphql_name='stats', args=sgqlc.types.ArgDict((
        ('league_stage_type_ids', sgqlc.types.Arg(sgqlc.types.list_of(LeagueStage), graphql_name='leagueStageTypeIds', default=None)),
))
    )
    prize_pool_percentages = sgqlc.types.Field(sgqlc.types.list_of(LeaguePrizePoolPercentageType), graphql_name='prizePoolPercentages')
    standings = sgqlc.types.Field(sgqlc.types.list_of('TeamPrizeType'), graphql_name='standings')
    streams = sgqlc.types.Field(sgqlc.types.list_of(LeagueStreamType), graphql_name='streams')


class LiveEventMatchDireTideStompType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match',)
    match = sgqlc.types.Field(DireTideCustomGameMatchType, graphql_name='match')


class LiveEventPlayerDireTideCandyScoredType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'candy_scored')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field(DireTideCustomGameMatchType, graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    candy_scored = sgqlc.types.Field(Short, graphql_name='candyScored')


class LiveEventPlayerHeroAssistsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'assist_count')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    assist_count = sgqlc.types.Field(Byte, graphql_name='assistCount')


class LiveEventPlayerHeroBuildingDamageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'building_damage')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    building_damage = sgqlc.types.Field(Int, graphql_name='buildingDamage')


class LiveEventPlayerHeroDewardType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'deward_count')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    deward_count = sgqlc.types.Field(Byte, graphql_name='dewardCount')


class LiveEventPlayerHeroDotaPlusLevelType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'level')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    level = sgqlc.types.Field(Byte, graphql_name='level')


class LiveEventPlayerHeroExpPerMinuteType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'exp_per_minute')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    exp_per_minute = sgqlc.types.Field(Short, graphql_name='expPerMinute')


class LiveEventPlayerHeroGoldPerMinuteType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'gold_per_minute')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    gold_per_minute = sgqlc.types.Field(Short, graphql_name='goldPerMinute')


class LiveEventPlayerHeroHealingType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'healing_amount')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    healing_amount = sgqlc.types.Field(Int, graphql_name='healingAmount')


class LiveEventPlayerHeroHeroDamageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'hero_damage')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    hero_damage = sgqlc.types.Field(Int, graphql_name='heroDamage')


class LiveEventPlayerHeroHighImpType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'imp')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    imp = sgqlc.types.Field(Byte, graphql_name='imp')


class LiveEventPlayerHeroItemPurchaseType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'item_id', 'item_count')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    item_id = sgqlc.types.Field(Short, graphql_name='itemId')
    item_count = sgqlc.types.Field(Byte, graphql_name='itemCount')


class LiveEventPlayerHeroKillsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'kill_count')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    kill_count = sgqlc.types.Field(Byte, graphql_name='killCount')


class LiveEventPlayerHeroWinStreakType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'win_streak_count')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    win_streak_count = sgqlc.types.Field(Byte, graphql_name='winStreakCount')


class LiveEventPlayerRampageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'hero_id', 'rampage_count')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    rampage_count = sgqlc.types.Field(Byte, graphql_name='rampageCount')


class LiveEventPlayerRankUpType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'rank')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    rank = sgqlc.types.Field(Byte, graphql_name='rank')


class LiveEventPlayerWinStreakType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match', 'win_streak_count')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    win_streak_count = sgqlc.types.Field(Byte, graphql_name='winStreakCount')


class LiveEventProPlayerLiveType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_accounts', 'match')
    steam_accounts = sgqlc.types.Field(sgqlc.types.list_of('SteamAccountType'), graphql_name='steamAccounts')
    match = sgqlc.types.Field('MatchLiveType', graphql_name='match')


class LiveQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match', 'matches')
    match = sgqlc.types.Field('MatchLiveType', graphql_name='match', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
        ('skip_playback_duration', sgqlc.types.Arg(Int, graphql_name='skipPlaybackDuration', default=None)),
))
    )
    matches = sgqlc.types.Field(sgqlc.types.list_of('MatchLiveType'), graphql_name='matches', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(MatchLiveRequestType, graphql_name='request', default=None)),
))
    )


class LobbyTypeType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')


class MatchGroupByAssistsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('assist_count', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    assist_count = sgqlc.types.Field(Long, graphql_name='assistCount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByAwardType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('award', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    award = sgqlc.types.Field(MatchPlayerAward, graphql_name='award')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByClusterType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('cluster', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    cluster = sgqlc.types.Field(Long, graphql_name='cluster')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByDateDayHeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('date_day', 'hero_id', 'hero', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    date_day = sgqlc.types.Field(Long, graphql_name='dateDay')
    hero_id = sgqlc.types.Field(Long, graphql_name='heroId')
    hero = sgqlc.types.Field(HeroType, graphql_name='hero', args=sgqlc.types.ArgDict((
        ('game_version_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='gameVersionId', default=None)),
))
    )
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByDateDayType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('date_day', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    date_day = sgqlc.types.Field(Long, graphql_name='dateDay')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByDeathsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('death_count', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    death_count = sgqlc.types.Field(Long, graphql_name='deathCount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByDurationMinutesType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('duration_minutes', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    duration_minutes = sgqlc.types.Field(Long, graphql_name='durationMinutes')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByFactionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_radiant', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByGameModeType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('game_mode', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    game_mode = sgqlc.types.Field(Long, graphql_name='gameMode')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByGameVersionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('game_version', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    game_version = sgqlc.types.Field(Long, graphql_name='gameVersion')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByGoldPerMinuteType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('gold_per_minute', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    gold_per_minute = sgqlc.types.Field(Long, graphql_name='goldPerMinute')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByHeroPerformanceType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'position', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByHeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'hero', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    hero_id = sgqlc.types.Field(Long, graphql_name='heroId')
    hero = sgqlc.types.Field(HeroType, graphql_name='hero', args=sgqlc.types.ArgDict((
        ('game_version_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='gameVersionId', default=None)),
))
    )
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByHourType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hour', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    hour = sgqlc.types.Field(Short, graphql_name='hour')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByIsIntentionalFeedingType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_intentional_feeding', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    is_intentional_feeding = sgqlc.types.Field(Boolean, graphql_name='isIntentionalFeeding')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByIsLeagueType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_league', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    is_league = sgqlc.types.Field(Boolean, graphql_name='isLeague')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByIsLeaverType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_leaver', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    is_leaver = sgqlc.types.Field(Boolean, graphql_name='isLeaver')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByIsPartyType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_party', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    is_party = sgqlc.types.Field(Boolean, graphql_name='isParty')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByIsRandomType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_random', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    is_random = sgqlc.types.Field(Boolean, graphql_name='isRandom')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByIsSeriesType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_series', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    is_series = sgqlc.types.Field(Boolean, graphql_name='isSeries')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByIsStatsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_stats', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByIsVictoryType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_victory', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    is_victory = sgqlc.types.Field(Boolean, graphql_name='isVictory')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByKillsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('kill_count', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    kill_count = sgqlc.types.Field(Long, graphql_name='killCount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByLaneType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('lane', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    lane = sgqlc.types.Field(MatchLaneType, graphql_name='lane')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByLeagueIdType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('league_id', 'league', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    league_id = sgqlc.types.Field(Long, graphql_name='leagueId')
    league = sgqlc.types.Field(LeagueType, graphql_name='league')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByLevelType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('level', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    level = sgqlc.types.Field(Long, graphql_name='level')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByLobbyTypeType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('lobby_type', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    lobby_type = sgqlc.types.Field(Long, graphql_name='lobbyType')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByPositionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('position', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByRegionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('region', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    region = sgqlc.types.Field(Long, graphql_name='region')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByRoamLaneType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('roam_lane', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    roam_lane = sgqlc.types.Field(MatchPlayerAward, graphql_name='roamLane')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByRoleType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('role', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    role = sgqlc.types.Field(MatchPlayerRoleType, graphql_name='role')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupBySteamAccountIdAgainstTeamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupBySteamAccountIdHeroIdAgainstTeamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'hero_id', 'hero', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    hero = sgqlc.types.Field(HeroType, graphql_name='hero', args=sgqlc.types.ArgDict((
        ('game_version_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='gameVersionId', default=None)),
))
    )
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupBySteamAccountIdHeroIdType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'hero_id', 'hero', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    hero = sgqlc.types.Field(HeroType, graphql_name='hero', args=sgqlc.types.ArgDict((
        ('game_version_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='gameVersionId', default=None)),
))
    )
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupBySteamAccountIdHeroIdWithTeamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'hero_id', 'hero', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    hero = sgqlc.types.Field(HeroType, graphql_name='hero', args=sgqlc.types.ArgDict((
        ('game_version_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='gameVersionId', default=None)),
))
    )
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupBySteamAccountIdType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupBySteamAccountIdWithTeamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByTeamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('team_id', 'team', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    team_id = sgqlc.types.Field(Long, graphql_name='teamId')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchGroupByTotalKillsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('total_kills', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'avg_tower_damage', 'last_match_date_time', 'first_match_date_time')
    total_kills = sgqlc.types.Field(Long, graphql_name='totalKills')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    avg_tower_damage = sgqlc.types.Field(Float, graphql_name='avgTowerDamage')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class MatchLiveBuildingDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'index_id', 'type', 'is_alive', 'position_x', 'position_y', 'is_radiant', 'npc_id')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    index_id = sgqlc.types.Field(Int, graphql_name='indexId')
    type = sgqlc.types.Field(BuildingType, graphql_name='type')
    is_alive = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAlive')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    npc_id = sgqlc.types.Field(Int, graphql_name='npcId')


class MatchLiveInsightType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('team_one_vs_win_count', 'team_two_vs_win_count', 'team_one_league_win_count', 'team_one_league_match_count', 'team_two_league_win_count', 'team_two_league_match_count', 'last_series')
    team_one_vs_win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='teamOneVsWinCount')
    team_two_vs_win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='teamTwoVsWinCount')
    team_one_league_win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='teamOneLeagueWinCount')
    team_one_league_match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='teamOneLeagueMatchCount')
    team_two_league_win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='teamTwoLeagueWinCount')
    team_two_league_match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='teamTwoLeagueMatchCount')
    last_series = sgqlc.types.Field(sgqlc.types.list_of('SeriesType'), graphql_name='lastSeries')


class MatchLivePickBanType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_pick', 'hero_id', 'order', 'banned_hero_id', 'is_radiant', 'base_win_rate', 'adjusted_win_rate', 'letter', 'position_values', 'win_rate_values', 'duration_values', 'position')
    is_pick = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPick')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    order = sgqlc.types.Field(Int, graphql_name='order')
    banned_hero_id = sgqlc.types.Field(Short, graphql_name='bannedHeroId')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    base_win_rate = sgqlc.types.Field(Float, graphql_name='baseWinRate')
    adjusted_win_rate = sgqlc.types.Field(Float, graphql_name='adjustedWinRate')
    letter = sgqlc.types.Field(PlusLetterType, graphql_name='letter')
    position_values = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='positionValues')
    win_rate_values = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='winRateValues')
    duration_values = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='durationValues')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')


class MatchLivePlaybackDataType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('roshan_events', 'building_events', 'pick_bans', 'radiant_score', 'dire_score')
    roshan_events = sgqlc.types.Field(sgqlc.types.list_of('MatchLiveRoshanDetailType'), graphql_name='roshanEvents')
    building_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLiveBuildingDetailType), graphql_name='buildingEvents')
    pick_bans = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePickBanType), graphql_name='pickBans')
    radiant_score = sgqlc.types.Field(sgqlc.types.list_of('MatchLiveTeamScoreDetailType'), graphql_name='radiantScore')
    dire_score = sgqlc.types.Field(sgqlc.types.list_of('MatchLiveTeamScoreDetailType'), graphql_name='direScore')


class MatchLivePlayerAssistDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    position_x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionX')
    position_y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionY')


class MatchLivePlayerDeathDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    position_x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionX')
    position_y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionY')


class MatchLivePlayerDenyDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    position_x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionX')
    position_y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionY')


class MatchLivePlayerExperienceDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'exp_per_minute')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    exp_per_minute = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='expPerMinute')


class MatchLivePlayerGoldDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'gold', 'networth', 'networth_difference', 'gold_per_minute')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    gold = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gold')
    networth = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='networth')
    networth_difference = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='networthDifference')
    gold_per_minute = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='goldPerMinute')


class MatchLivePlayerImpDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'imp')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    imp = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='imp')


class MatchLivePlayerInventoryDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'item_id0', 'item_id1', 'item_id2', 'item_id3', 'item_id4', 'item_id5', 'backpack_id0', 'backpack_id1', 'backpack_id2')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    item_id0 = sgqlc.types.Field(Short, graphql_name='itemId0')
    item_id1 = sgqlc.types.Field(Short, graphql_name='itemId1')
    item_id2 = sgqlc.types.Field(Short, graphql_name='itemId2')
    item_id3 = sgqlc.types.Field(Short, graphql_name='itemId3')
    item_id4 = sgqlc.types.Field(Short, graphql_name='itemId4')
    item_id5 = sgqlc.types.Field(Short, graphql_name='itemId5')
    backpack_id0 = sgqlc.types.Field(Short, graphql_name='backpackId0')
    backpack_id1 = sgqlc.types.Field(Short, graphql_name='backpackId1')
    backpack_id2 = sgqlc.types.Field(Short, graphql_name='backpackId2')


class MatchLivePlayerKillDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    position_x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionX')
    position_y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionY')


class MatchLivePlayerLastHitDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    position_x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionX')
    position_y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionY')


class MatchLivePlayerLevelDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'level')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='level')


class MatchLivePlayerPositionDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'x', 'y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='y')


class MatchLivePlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'hero_id', 'hero', 'name', 'player_slot', 'steam_account_id', 'steam_account', 'is_radiant', 'num_kills', 'num_deaths', 'num_assists', 'leaver_status', 'num_last_hits', 'num_denies', 'gold_per_minute', 'experience_per_minute', 'level', 'gold', 'gold_spent', 'hero_damage', 'tower_damage', 'item_id0', 'item_id1', 'item_id2', 'item_id3', 'item_id4', 'item_id5', 'backpack_id0', 'backpack_id1', 'backpack_id2', 'playback_data', 'networth', 'respawn_timer', 'ultimate_cooldown', 'ultimate_state', 'imp_per_minute', 'game_version_id', 'base_win_rate_value', 'position')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    hero = sgqlc.types.Field(HeroType, graphql_name='hero')
    name = sgqlc.types.Field(String, graphql_name='name')
    player_slot = sgqlc.types.Field(Byte, graphql_name='playerSlot')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    num_kills = sgqlc.types.Field(Byte, graphql_name='numKills')
    num_deaths = sgqlc.types.Field(Byte, graphql_name='numDeaths')
    num_assists = sgqlc.types.Field(Byte, graphql_name='numAssists')
    leaver_status = sgqlc.types.Field(Byte, graphql_name='leaverStatus')
    num_last_hits = sgqlc.types.Field(UShort, graphql_name='numLastHits')
    num_denies = sgqlc.types.Field(UShort, graphql_name='numDenies')
    gold_per_minute = sgqlc.types.Field(UShort, graphql_name='goldPerMinute')
    experience_per_minute = sgqlc.types.Field(UShort, graphql_name='experiencePerMinute')
    level = sgqlc.types.Field(Byte, graphql_name='level')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    gold_spent = sgqlc.types.Field(Int, graphql_name='goldSpent')
    hero_damage = sgqlc.types.Field(Int, graphql_name='heroDamage')
    tower_damage = sgqlc.types.Field(Int, graphql_name='towerDamage')
    item_id0 = sgqlc.types.Field(Short, graphql_name='itemId0')
    item_id1 = sgqlc.types.Field(Short, graphql_name='itemId1')
    item_id2 = sgqlc.types.Field(Short, graphql_name='itemId2')
    item_id3 = sgqlc.types.Field(Short, graphql_name='itemId3')
    item_id4 = sgqlc.types.Field(Short, graphql_name='itemId4')
    item_id5 = sgqlc.types.Field(Short, graphql_name='itemId5')
    backpack_id0 = sgqlc.types.Field(Short, graphql_name='backpackId0')
    backpack_id1 = sgqlc.types.Field(Short, graphql_name='backpackId1')
    backpack_id2 = sgqlc.types.Field(Short, graphql_name='backpackId2')
    playback_data = sgqlc.types.Field('MatchPlayerLivePlaybackDataType', graphql_name='playbackData')
    networth = sgqlc.types.Field(Int, graphql_name='networth')
    respawn_timer = sgqlc.types.Field(Short, graphql_name='respawnTimer')
    ultimate_cooldown = sgqlc.types.Field(Short, graphql_name='ultimateCooldown')
    ultimate_state = sgqlc.types.Field(Short, graphql_name='ultimateState')
    imp_per_minute = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerImpDetailType), graphql_name='impPerMinute')
    game_version_id = sgqlc.types.Field(Short, graphql_name='gameVersionId')
    base_win_rate_value = sgqlc.types.Field(Float, graphql_name='baseWinRateValue')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')


class MatchLiveRoshanDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'is_alive', 'respawn_timer')
    time = sgqlc.types.Field(Int, graphql_name='time')
    is_alive = sgqlc.types.Field(Boolean, graphql_name='isAlive')
    respawn_timer = sgqlc.types.Field(Int, graphql_name='respawnTimer')


class MatchLiveTeamScoreDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'score')
    time = sgqlc.types.Field(Int, graphql_name='time')
    score = sgqlc.types.Field(Short, graphql_name='score')


class MatchLiveType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'radiant_score', 'dire_score', 'league_id', 'league', 'delay', 'spectators', 'average_rank', 'building_state', 'radiant_lead', 'lobby_id', 'lobby_type', 'server_steam_id', 'game_time', 'completed', 'is_updating', 'is_parsing', 'radiant_team_id', 'dire_team_id', 'radiant_team', 'dire_team', 'parse_begin_game_time', 'num_human_players', 'game_mode', 'playback_data', 'game_state', 'game_minute', 'players', 'created_date_time', 'modified_date_time', 'insight', 'win_rate_values', 'duration_values', 'live_win_rate_values')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    radiant_score = sgqlc.types.Field(Byte, graphql_name='radiantScore')
    dire_score = sgqlc.types.Field(Byte, graphql_name='direScore')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    league = sgqlc.types.Field(LeagueType, graphql_name='league')
    delay = sgqlc.types.Field(Short, graphql_name='delay')
    spectators = sgqlc.types.Field(Int, graphql_name='spectators')
    average_rank = sgqlc.types.Field(Int, graphql_name='averageRank')
    building_state = sgqlc.types.Field(Long, graphql_name='buildingState')
    radiant_lead = sgqlc.types.Field(Int, graphql_name='radiantLead')
    lobby_id = sgqlc.types.Field(Long, graphql_name='lobbyId')
    lobby_type = sgqlc.types.Field(LobbyTypeEnum, graphql_name='lobbyType')
    server_steam_id = sgqlc.types.Field(Long, graphql_name='serverSteamId')
    game_time = sgqlc.types.Field(Int, graphql_name='gameTime')
    completed = sgqlc.types.Field(Boolean, graphql_name='completed')
    is_updating = sgqlc.types.Field(Boolean, graphql_name='isUpdating')
    is_parsing = sgqlc.types.Field(Boolean, graphql_name='isParsing')
    radiant_team_id = sgqlc.types.Field(Int, graphql_name='radiantTeamId')
    dire_team_id = sgqlc.types.Field(Int, graphql_name='direTeamId')
    radiant_team = sgqlc.types.Field('TeamType', graphql_name='radiantTeam')
    dire_team = sgqlc.types.Field('TeamType', graphql_name='direTeam')
    parse_begin_game_time = sgqlc.types.Field(Int, graphql_name='parseBeginGameTime')
    num_human_players = sgqlc.types.Field(Byte, graphql_name='numHumanPlayers')
    game_mode = sgqlc.types.Field(GameModeEnumType, graphql_name='gameMode')
    playback_data = sgqlc.types.Field(MatchLivePlaybackDataType, graphql_name='playbackData')
    game_state = sgqlc.types.Field(MatchLiveGameState, graphql_name='gameState')
    game_minute = sgqlc.types.Field(Short, graphql_name='gameMinute')
    players = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerType), graphql_name='players')
    created_date_time = sgqlc.types.Field(Long, graphql_name='createdDateTime')
    modified_date_time = sgqlc.types.Field(Long, graphql_name='modifiedDateTime')
    insight = sgqlc.types.Field(MatchLiveInsightType, graphql_name='insight')
    win_rate_values = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='winRateValues')
    duration_values = sgqlc.types.Field(sgqlc.types.list_of(Float), graphql_name='durationValues')
    live_win_rate_values = sgqlc.types.Field(sgqlc.types.list_of('MatchLiveWinRateDetailType'), graphql_name='liveWinRateValues')


class MatchLiveWinRateDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'win_rate')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    win_rate = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='winRate')


class MatchPickBanGroupByType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'match_count', 'pick_count', 'ban_count')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    pick_count = sgqlc.types.Field(Int, graphql_name='pickCount')
    ban_count = sgqlc.types.Field(Int, graphql_name='banCount')


class MatchPlaybackDataBuildingEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'index_id', 'type', 'hp', 'max_hp', 'position_x', 'position_y', 'is_radiant', 'npc_id', 'did_shrine_activate')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    index_id = sgqlc.types.Field(Int, graphql_name='indexId')
    type = sgqlc.types.Field(BuildingType, graphql_name='type')
    hp = sgqlc.types.Field(Int, graphql_name='hp')
    max_hp = sgqlc.types.Field(Int, graphql_name='maxHp')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    npc_id = sgqlc.types.Field(Int, graphql_name='npcId')
    did_shrine_activate = sgqlc.types.Field(Boolean, graphql_name='didShrineActivate')


class MatchPlaybackDataCourierEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'owner_hero', 'is_radiant', 'events')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    owner_hero = sgqlc.types.Field(Int, graphql_name='ownerHero')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    events = sgqlc.types.Field(sgqlc.types.list_of('MatchplaybackDataCourierEventObjectType'), graphql_name='events')


class MatchPlaybackDataRoshanEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'hp', 'max_hp', 'create_time', 'x', 'y', 'total_damage_taken', 'item0', 'item1', 'item2', 'item3', 'item4', 'item5')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    hp = sgqlc.types.Field(Int, graphql_name='hp')
    max_hp = sgqlc.types.Field(Int, graphql_name='maxHp')
    create_time = sgqlc.types.Field(Int, graphql_name='createTime')
    x = sgqlc.types.Field(Int, graphql_name='x')
    y = sgqlc.types.Field(Int, graphql_name='y')
    total_damage_taken = sgqlc.types.Field(Int, graphql_name='totalDamageTaken')
    item0 = sgqlc.types.Field(Int, graphql_name='item0')
    item1 = sgqlc.types.Field(Int, graphql_name='item1')
    item2 = sgqlc.types.Field(Int, graphql_name='item2')
    item3 = sgqlc.types.Field(Int, graphql_name='item3')
    item4 = sgqlc.types.Field(Int, graphql_name='item4')
    item5 = sgqlc.types.Field(Int, graphql_name='item5')


class MatchPlaybackDataRuneEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('index_id', 'time', 'position_x', 'position_y', 'location', 'rune', 'action')
    index_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='indexId')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    position_x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionX')
    position_y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionY')
    location = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='location')
    rune = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rune')
    action = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='action')


class MatchPlaybackDataTowerDeathEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'radiant', 'dire')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    radiant = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='radiant')
    dire = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dire')


class MatchPlaybackDataType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('courier_events', 'rune_events', 'ward_events', 'building_events', 'tower_death_events', 'roshan_events', 'radiant_captain_hero_id', 'dire_captain_hero_id')
    courier_events = sgqlc.types.Field(sgqlc.types.list_of(MatchPlaybackDataCourierEventType), graphql_name='courierEvents')
    rune_events = sgqlc.types.Field(sgqlc.types.list_of(MatchPlaybackDataRuneEventType), graphql_name='runeEvents')
    ward_events = sgqlc.types.Field(sgqlc.types.list_of('MatchPlaybackDataWardEventType'), graphql_name='wardEvents')
    building_events = sgqlc.types.Field(sgqlc.types.list_of(MatchPlaybackDataBuildingEventType), graphql_name='buildingEvents')
    tower_death_events = sgqlc.types.Field(sgqlc.types.list_of(MatchPlaybackDataTowerDeathEventType), graphql_name='towerDeathEvents')
    roshan_events = sgqlc.types.Field(sgqlc.types.list_of(MatchPlaybackDataRoshanEventType), graphql_name='roshanEvents')
    radiant_captain_hero_id = sgqlc.types.Field(Long, graphql_name='radiantCaptainHeroId')
    dire_captain_hero_id = sgqlc.types.Field(Long, graphql_name='direCaptainHeroId')


class MatchPlaybackDataWardEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('index_id', 'time', 'position_x', 'position_y', 'from_player', 'ward_type', 'action', 'player_destroyed')
    index_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='indexId')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    position_x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionX')
    position_y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionY')
    from_player = sgqlc.types.Field(Int, graphql_name='fromPlayer')
    ward_type = sgqlc.types.Field(WardType, graphql_name='wardType')
    action = sgqlc.types.Field(SpawnActionType, graphql_name='action')
    player_destroyed = sgqlc.types.Field(Int, graphql_name='playerDestroyed')


class MatchPlayerAdditionalUnitType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('item0_id', 'item1_id', 'item2_id', 'item3_id', 'item4_id', 'item5_id', 'backpack0_id', 'backpack1_id', 'backpack2_id', 'neutral0_id')
    item0_id = sgqlc.types.Field(Short, graphql_name='item0Id')
    item1_id = sgqlc.types.Field(Short, graphql_name='item1Id')
    item2_id = sgqlc.types.Field(Short, graphql_name='item2Id')
    item3_id = sgqlc.types.Field(Short, graphql_name='item3Id')
    item4_id = sgqlc.types.Field(Short, graphql_name='item4Id')
    item5_id = sgqlc.types.Field(Short, graphql_name='item5Id')
    backpack0_id = sgqlc.types.Field(Short, graphql_name='backpack0Id')
    backpack1_id = sgqlc.types.Field(Short, graphql_name='backpack1Id')
    backpack2_id = sgqlc.types.Field(Short, graphql_name='backpack2Id')
    neutral0_id = sgqlc.types.Field(Short, graphql_name='neutral0Id')


class MatchPlayerHeroDamageSourceAbilityReportObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('ability_id', 'count', 'amount')
    ability_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='abilityId')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amount')


class MatchPlayerHeroDamageSourceItemReportObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('item_id', 'count', 'amount')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='itemId')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amount')


class MatchPlayerHeroDamageTargetReportObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('target', 'amount')
    target = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='target')
    amount = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='amount')


class MatchPlayerHeroDamageTotalRecievedReportObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('physical_damage', 'magical_damage', 'pure_damage', 'heal', 'stun_count', 'stun_duration', 'disable_count', 'disable_duration', 'slow_count', 'slow_duration')
    physical_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='physicalDamage')
    magical_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='magicalDamage')
    pure_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pureDamage')
    heal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heal')
    stun_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='stunCount')
    stun_duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='stunDuration')
    disable_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='disableCount')
    disable_duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='disableDuration')
    slow_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='slowCount')
    slow_duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='slowDuration')


class MatchPlayerHeroDamageTotalReportObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('physical_damage', 'magical_damage', 'pure_damage', 'self_heal', 'ally_heal', 'stun_count', 'stun_duration', 'disable_count', 'disable_duration', 'slow_count', 'slow_duration')
    physical_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='physicalDamage')
    magical_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='magicalDamage')
    pure_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pureDamage')
    self_heal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='selfHeal')
    ally_heal = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='allyHeal')
    stun_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='stunCount')
    stun_duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='stunDuration')
    disable_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='disableCount')
    disable_duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='disableDuration')
    slow_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='slowCount')
    slow_duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='slowDuration')


class MatchPlayerInventoryObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('item_id', 'charges', 'secondary_charges')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='itemId')
    charges = sgqlc.types.Field(Int, graphql_name='charges')
    secondary_charges = sgqlc.types.Field(Int, graphql_name='secondaryCharges')


class MatchPlayerInventoryType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'back_pack0', 'back_pack1', 'back_pack2', 'neutral0')
    item0 = sgqlc.types.Field(MatchPlayerInventoryObjectType, graphql_name='item0')
    item1 = sgqlc.types.Field(MatchPlayerInventoryObjectType, graphql_name='item1')
    item2 = sgqlc.types.Field(MatchPlayerInventoryObjectType, graphql_name='item2')
    item3 = sgqlc.types.Field(MatchPlayerInventoryObjectType, graphql_name='item3')
    item4 = sgqlc.types.Field(MatchPlayerInventoryObjectType, graphql_name='item4')
    item5 = sgqlc.types.Field(MatchPlayerInventoryObjectType, graphql_name='item5')
    back_pack0 = sgqlc.types.Field(MatchPlayerInventoryObjectType, graphql_name='backPack0')
    back_pack1 = sgqlc.types.Field(MatchPlayerInventoryObjectType, graphql_name='backPack1')
    back_pack2 = sgqlc.types.Field(MatchPlayerInventoryObjectType, graphql_name='backPack2')
    neutral0 = sgqlc.types.Field(MatchPlayerInventoryObjectType, graphql_name='neutral0')


class MatchPlayerItemPurchaseEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'item_id')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='itemId')


class MatchPlayerLivePlaybackDataType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('position_events', 'gold_events', 'level_events', 'kill_events', 'death_events', 'assist_events', 'cs_events', 'deny_events', 'experience_events', 'inventory_events')
    position_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerPositionDetailType), graphql_name='positionEvents')
    gold_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerGoldDetailType), graphql_name='goldEvents')
    level_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerLevelDetailType), graphql_name='levelEvents')
    kill_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerKillDetailType), graphql_name='killEvents')
    death_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerDeathDetailType), graphql_name='deathEvents')
    assist_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerAssistDetailType), graphql_name='assistEvents')
    cs_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerLastHitDetailType), graphql_name='csEvents')
    deny_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerDenyDetailType), graphql_name='denyEvents')
    experience_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerExperienceDetailType), graphql_name='experienceEvents')
    inventory_events = sgqlc.types.Field(sgqlc.types.list_of(MatchLivePlayerInventoryDetailType), graphql_name='inventoryEvents')


class MatchPlayerPlaybackDataType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('ability_learn_events', 'ability_used_events', 'ability_active_lists', 'item_used_events', 'player_update_position_events', 'player_update_gold_events', 'player_update_attribute_events', 'player_update_level_events', 'player_update_health_events', 'player_update_battle_events', 'kill_events', 'death_events', 'assist_events', 'cs_events', 'gold_events', 'experience_events', 'heal_events', 'hero_damage_events', 'tower_damage_events', 'inventory_events', 'purchase_events', 'buy_back_events', 'streak_events', 'rune_events', 'spirit_bear_inventory_events')
    ability_learn_events = sgqlc.types.Field(sgqlc.types.list_of(AbilityLearnEventsType), graphql_name='abilityLearnEvents')
    ability_used_events = sgqlc.types.Field(sgqlc.types.list_of(AbilityUsedEventsType), graphql_name='abilityUsedEvents')
    ability_active_lists = sgqlc.types.Field(sgqlc.types.list_of(AbilityActiveListType), graphql_name='abilityActiveLists')
    item_used_events = sgqlc.types.Field(sgqlc.types.list_of(ItemUsedEventType), graphql_name='itemUsedEvents')
    player_update_position_events = sgqlc.types.Field(sgqlc.types.list_of('PlayerUpdatePositionDetailType'), graphql_name='playerUpdatePositionEvents')
    player_update_gold_events = sgqlc.types.Field(sgqlc.types.list_of('PlayerUpdateGoldDetailType'), graphql_name='playerUpdateGoldEvents')
    player_update_attribute_events = sgqlc.types.Field(sgqlc.types.list_of('PlayerUpdateAttributeDetailType'), graphql_name='playerUpdateAttributeEvents')
    player_update_level_events = sgqlc.types.Field(sgqlc.types.list_of('PlayerUpdateLevelDetailType'), graphql_name='playerUpdateLevelEvents')
    player_update_health_events = sgqlc.types.Field(sgqlc.types.list_of('PlayerUpdateHealthDetailType'), graphql_name='playerUpdateHealthEvents')
    player_update_battle_events = sgqlc.types.Field(sgqlc.types.list_of('PlayerUpdateBattleDetailType'), graphql_name='playerUpdateBattleEvents')
    kill_events = sgqlc.types.Field(sgqlc.types.list_of(KillDetailType), graphql_name='killEvents')
    death_events = sgqlc.types.Field(sgqlc.types.list_of(DeathDetailType), graphql_name='deathEvents')
    assist_events = sgqlc.types.Field(sgqlc.types.list_of(AssistDetailType), graphql_name='assistEvents')
    cs_events = sgqlc.types.Field(sgqlc.types.list_of(LastHitDetailType), graphql_name='csEvents')
    gold_events = sgqlc.types.Field(sgqlc.types.list_of(GoldDetailType), graphql_name='goldEvents')
    experience_events = sgqlc.types.Field(sgqlc.types.list_of(ExperienceDetailType), graphql_name='experienceEvents')
    heal_events = sgqlc.types.Field(sgqlc.types.list_of(HealDetailType), graphql_name='healEvents')
    hero_damage_events = sgqlc.types.Field(sgqlc.types.list_of(HeroDamageDetailType), graphql_name='heroDamageEvents')
    tower_damage_events = sgqlc.types.Field(sgqlc.types.list_of('TowerDamageDetailType'), graphql_name='towerDamageEvents')
    inventory_events = sgqlc.types.Field(sgqlc.types.list_of(InventoryType), graphql_name='inventoryEvents')
    purchase_events = sgqlc.types.Field(sgqlc.types.list_of(ItemPurchaseType), graphql_name='purchaseEvents')
    buy_back_events = sgqlc.types.Field(sgqlc.types.list_of(BuyBackDetailType), graphql_name='buyBackEvents')
    streak_events = sgqlc.types.Field(sgqlc.types.list_of('StreakEventType'), graphql_name='streakEvents')
    rune_events = sgqlc.types.Field(sgqlc.types.list_of('PlayerRuneDetailType'), graphql_name='runeEvents')
    spirit_bear_inventory_events = sgqlc.types.Field(sgqlc.types.list_of('SpiritBearInventoryType'), graphql_name='spiritBearInventoryEvents')


class MatchPlayerSpectatorType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_id', 'is_radiant_coach', 'is_victory')
    steam_id = sgqlc.types.Field(Long, graphql_name='steamId')
    is_radiant_coach = sgqlc.types.Field(Boolean, graphql_name='isRadiantCoach')
    is_victory = sgqlc.types.Field(Boolean, graphql_name='isVictory')


class MatchPlayerSpiritBearInventoryType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('item0_id', 'item1_id', 'item2_id', 'item3_id', 'item4_id', 'item5_id', 'back_pack0_id', 'back_pack1_id', 'back_pack2_id', 'neutral0_id')
    item0_id = sgqlc.types.Field(Int, graphql_name='item0Id')
    item1_id = sgqlc.types.Field(Int, graphql_name='item1Id')
    item2_id = sgqlc.types.Field(Int, graphql_name='item2Id')
    item3_id = sgqlc.types.Field(Int, graphql_name='item3Id')
    item4_id = sgqlc.types.Field(Int, graphql_name='item4Id')
    item5_id = sgqlc.types.Field(Int, graphql_name='item5Id')
    back_pack0_id = sgqlc.types.Field(Int, graphql_name='backPack0Id')
    back_pack1_id = sgqlc.types.Field(Int, graphql_name='backPack1Id')
    back_pack2_id = sgqlc.types.Field(Int, graphql_name='backPack2Id')
    neutral0_id = sgqlc.types.Field(Int, graphql_name='neutral0Id')


class MatchPlayerStatsAbilityCastObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('target', 'count', 'damage', 'duration')
    target = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='target')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='damage')
    duration = sgqlc.types.Field(Int, graphql_name='duration')


class MatchPlayerStatsAbilityCastReportType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('ability_id', 'count', 'targets')
    ability_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='abilityId')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    targets = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsAbilityCastObjectType), graphql_name='targets')


class MatchPlayerStatsActionReportType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('move_to_position', 'move_to_target', 'attack_position', 'attack_target', 'cast_position', 'cast_target', 'cast_no_target', 'held_position', 'glyph_cast', 'scan_used', 'ping_used')
    move_to_position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='moveToPosition')
    move_to_target = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='moveToTarget')
    attack_position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='attackPosition')
    attack_target = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='attackTarget')
    cast_position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='castPosition')
    cast_target = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='castTarget')
    cast_no_target = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='castNoTarget')
    held_position = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heldPosition')
    glyph_cast = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='glyphCast')
    scan_used = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='scanUsed')
    ping_used = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pingUsed')


class MatchPlayerStatsAllTalkEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'message', 'paused_tick')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    message = sgqlc.types.Field(String, graphql_name='message')
    paused_tick = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pausedTick')


class MatchPlayerStatsAssistEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'target', 'gold', 'xp', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    target = sgqlc.types.Field(Int, graphql_name='target')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    xp = sgqlc.types.Field(Int, graphql_name='xp')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')


class MatchPlayerStatsBuffEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'ability_id', 'item_id', 'stack_count')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    ability_id = sgqlc.types.Field(Int, graphql_name='abilityId')
    item_id = sgqlc.types.Field(Int, graphql_name='itemId')
    stack_count = sgqlc.types.Field(Int, graphql_name='stackCount')


class MatchPlayerStatsChatWheelEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'chat_wheel_id', 'pause_tick')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    chat_wheel_id = sgqlc.types.Field(Short, graphql_name='chatWheelId')
    pause_tick = sgqlc.types.Field(Int, graphql_name='pauseTick')


class MatchPlayerStatsCourierKillEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')


class MatchPlayerStatsDeathEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'attacker', 'target', 'by_ability', 'by_item', 'gold_fed', 'xp_fed', 'time_dead', 'position_x', 'position_y', 'gold_lost', 'assist', 'is_ward_walk_through', 'is_attempt_tp_out', 'is_die_back', 'is_burst', 'is_engaged_on_death', 'has_heal_available', 'is_tracked')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')
    target = sgqlc.types.Field(Int, graphql_name='target')
    by_ability = sgqlc.types.Field(Int, graphql_name='byAbility')
    by_item = sgqlc.types.Field(Int, graphql_name='byItem')
    gold_fed = sgqlc.types.Field(Int, graphql_name='goldFed')
    xp_fed = sgqlc.types.Field(Int, graphql_name='xpFed')
    time_dead = sgqlc.types.Field(Int, graphql_name='timeDead')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')
    gold_lost = sgqlc.types.Field(Int, graphql_name='goldLost')
    assist = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Short)), graphql_name='assist')
    is_ward_walk_through = sgqlc.types.Field(Boolean, graphql_name='isWardWalkThrough')
    is_attempt_tp_out = sgqlc.types.Field(Boolean, graphql_name='isAttemptTpOut')
    is_die_back = sgqlc.types.Field(Boolean, graphql_name='isDieBack')
    is_burst = sgqlc.types.Field(Boolean, graphql_name='isBurst')
    is_engaged_on_death = sgqlc.types.Field(Boolean, graphql_name='isEngagedOnDeath')
    has_heal_available = sgqlc.types.Field(Boolean, graphql_name='hasHealAvailable')
    is_tracked = sgqlc.types.Field(Boolean, graphql_name='isTracked')


class MatchPlayerStatsFarmDistributionObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'count', 'gold', 'xp')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='count')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    xp = sgqlc.types.Field(Int, graphql_name='xp')


class MatchPlayerStatsFarmDistributionReportType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('creep_type', 'creep_location', 'neutral_location', 'ancient_location', 'buildings', 'buy_back_gold', 'abandon_gold', 'bounty_gold', 'other')
    creep_type = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsFarmDistributionObjectType), graphql_name='creepType')
    creep_location = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsFarmDistributionObjectType), graphql_name='creepLocation')
    neutral_location = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsFarmDistributionObjectType), graphql_name='neutralLocation')
    ancient_location = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsFarmDistributionObjectType), graphql_name='ancientLocation')
    buildings = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsFarmDistributionObjectType), graphql_name='buildings')
    buy_back_gold = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='buyBackGold')
    abandon_gold = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='abandonGold')
    bounty_gold = sgqlc.types.Field(MatchPlayerStatsFarmDistributionObjectType, graphql_name='bountyGold')
    other = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsFarmDistributionObjectType), graphql_name='other')


class MatchPlayerStatsHeroDamageReportType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('dealt_total', 'received_total', 'dealt_targets', 'received_targets', 'dealt_source_ability', 'received_source_ability', 'dealt_source_item', 'received_source_item')
    dealt_total = sgqlc.types.Field(MatchPlayerHeroDamageTotalReportObjectType, graphql_name='dealtTotal')
    received_total = sgqlc.types.Field(MatchPlayerHeroDamageTotalRecievedReportObjectType, graphql_name='receivedTotal')
    dealt_targets = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerHeroDamageTargetReportObjectType), graphql_name='dealtTargets')
    received_targets = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerHeroDamageTargetReportObjectType), graphql_name='receivedTargets')
    dealt_source_ability = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerHeroDamageSourceAbilityReportObjectType), graphql_name='dealtSourceAbility')
    received_source_ability = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerHeroDamageSourceAbilityReportObjectType), graphql_name='receivedSourceAbility')
    dealt_source_item = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerHeroDamageSourceItemReportObjectType), graphql_name='dealtSourceItem')
    received_source_item = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerHeroDamageSourceItemReportObjectType), graphql_name='receivedSourceItem')


class MatchPlayerStatsItemUsedEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('item_id', 'count')
    item_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='itemId')
    count = sgqlc.types.Field(Int, graphql_name='count')


class MatchPlayerStatsKillEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'target', 'by_ability', 'by_item', 'gold', 'xp', 'position_x', 'position_y', 'assist', 'is_solo', 'is_gank', 'is_invisible', 'is_smoke', 'is_tp_recently')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    target = sgqlc.types.Field(Int, graphql_name='target')
    by_ability = sgqlc.types.Field(Int, graphql_name='byAbility')
    by_item = sgqlc.types.Field(Int, graphql_name='byItem')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    xp = sgqlc.types.Field(Int, graphql_name='xp')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')
    assist = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null(Int)), graphql_name='assist')
    is_solo = sgqlc.types.Field(Boolean, graphql_name='isSolo')
    is_gank = sgqlc.types.Field(Boolean, graphql_name='isGank')
    is_invisible = sgqlc.types.Field(Boolean, graphql_name='isInvisible')
    is_smoke = sgqlc.types.Field(Boolean, graphql_name='isSmoke')
    is_tp_recently = sgqlc.types.Field(Boolean, graphql_name='isTpRecently')


class MatchPlayerStatsLocationReportType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('position_x', 'position_y')
    position_x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionX')
    position_y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='positionY')


class MatchPlayerStatsRuneEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'rune', 'action', 'gold', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    rune = sgqlc.types.Field(RuneEnums, graphql_name='rune')
    action = sgqlc.types.Field(RuneAction, graphql_name='action')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')


class MatchPlayerStatsTowerDamageReportType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('npc_id', 'damage', 'damage_creeps', 'damage_from_ability')
    npc_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='npcId')
    damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='damage')
    damage_creeps = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='damageCreeps')
    damage_from_ability = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='damageFromAbility')


class MatchPlayerStatsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'steam_account_id', 'game_version_id', 'level', 'kill_events', 'death_events', 'assist_events', 'last_hits_per_minute', 'gold_per_minute', 'experience_per_minute', 'heal_per_minute', 'hero_damage_per_minute', 'tower_damage_per_minute', 'tower_damage_report', 'courier_kills', 'wards', 'item_purchases', 'item_used', 'all_talks', 'chat_wheels', 'actions_per_minute', 'action_report', 'location_report', 'farm_distribution_report', 'runes', 'ability_cast_report', 'hero_damage_report', 'inventory_report', 'networth_per_minute', 'camp_stack', 'match_player_buff_event', 'denies_per_minute', 'imp_per_minute', 'trips_fountain_per_minute', 'spirit_bear_inventory_report', 'hero_damage_received_per_minute', 'ward_destruction')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    game_version_id = sgqlc.types.Field(Short, graphql_name='gameVersionId')
    level = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='level')
    kill_events = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsKillEventType), graphql_name='killEvents')
    death_events = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsDeathEventType), graphql_name='deathEvents')
    assist_events = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsAssistEventType), graphql_name='assistEvents')
    last_hits_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='lastHitsPerMinute')
    gold_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='goldPerMinute')
    experience_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='experiencePerMinute')
    heal_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='healPerMinute')
    hero_damage_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='heroDamagePerMinute')
    tower_damage_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='towerDamagePerMinute')
    tower_damage_report = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsTowerDamageReportType), graphql_name='towerDamageReport')
    courier_kills = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsCourierKillEventType), graphql_name='courierKills')
    wards = sgqlc.types.Field(sgqlc.types.list_of('MatchPlayerStatsWardEventType'), graphql_name='wards')
    item_purchases = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerItemPurchaseEventType), graphql_name='itemPurchases')
    item_used = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsItemUsedEventType), graphql_name='itemUsed')
    all_talks = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsAllTalkEventType), graphql_name='allTalks')
    chat_wheels = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsChatWheelEventType), graphql_name='chatWheels')
    actions_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='actionsPerMinute')
    action_report = sgqlc.types.Field(MatchPlayerStatsActionReportType, graphql_name='actionReport')
    location_report = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsLocationReportType), graphql_name='locationReport')
    farm_distribution_report = sgqlc.types.Field(MatchPlayerStatsFarmDistributionReportType, graphql_name='farmDistributionReport')
    runes = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsRuneEventType), graphql_name='runes')
    ability_cast_report = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsAbilityCastReportType), graphql_name='abilityCastReport')
    hero_damage_report = sgqlc.types.Field(MatchPlayerStatsHeroDamageReportType, graphql_name='heroDamageReport')
    inventory_report = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerInventoryType), graphql_name='inventoryReport')
    networth_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='networthPerMinute')
    camp_stack = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='campStack')
    match_player_buff_event = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerStatsBuffEventType), graphql_name='matchPlayerBuffEvent')
    denies_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='deniesPerMinute')
    imp_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='impPerMinute')
    trips_fountain_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='tripsFountainPerMinute')
    spirit_bear_inventory_report = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerSpiritBearInventoryType), graphql_name='spiritBearInventoryReport')
    hero_damage_received_per_minute = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='heroDamageReceivedPerMinute')
    ward_destruction = sgqlc.types.Field(sgqlc.types.list_of('MatchPlayerWardDestuctionObjectType'), graphql_name='wardDestruction')


class MatchPlayerStatsWardEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'type', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    type = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='type')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')


class MatchPlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'match', 'player_slot', 'steam_account_id', 'steam_account', 'is_radiant', 'is_victory', 'hero_id', 'game_version_id', 'hero', 'kills', 'deaths', 'assists', 'leaver_status', 'num_last_hits', 'num_denies', 'gold_per_minute', 'networth', 'experience_per_minute', 'level', 'gold', 'gold_spent', 'hero_damage', 'tower_damage', 'hero_healing', 'party_id', 'is_random', 'lane', 'position', 'streak_prediction', 'intentional_feeding', 'role', 'role_basic', 'imp', 'award', 'item0_id', 'item1_id', 'item2_id', 'item3_id', 'item4_id', 'item5_id', 'backpack0_id', 'backpack1_id', 'backpack2_id', 'neutral0_id', 'behavior', 'stats', 'playback_data', 'hero_average', 'additional_unit', 'dota_plus', 'abilities', 'invisible_seconds', 'dota_plus_hero_xp', 'variant')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    match = sgqlc.types.Field('MatchType', graphql_name='match')
    player_slot = sgqlc.types.Field(Byte, graphql_name='playerSlot')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    is_victory = sgqlc.types.Field(Boolean, graphql_name='isVictory')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    game_version_id = sgqlc.types.Field(Short, graphql_name='gameVersionId')
    hero = sgqlc.types.Field(HeroType, graphql_name='hero')
    kills = sgqlc.types.Field(Byte, graphql_name='kills')
    deaths = sgqlc.types.Field(Byte, graphql_name='deaths')
    assists = sgqlc.types.Field(Byte, graphql_name='assists')
    leaver_status = sgqlc.types.Field(LeaverStatusEnum, graphql_name='leaverStatus')
    num_last_hits = sgqlc.types.Field(Short, graphql_name='numLastHits')
    num_denies = sgqlc.types.Field(Short, graphql_name='numDenies')
    gold_per_minute = sgqlc.types.Field(Short, graphql_name='goldPerMinute')
    networth = sgqlc.types.Field(Int, graphql_name='networth')
    experience_per_minute = sgqlc.types.Field(Short, graphql_name='experiencePerMinute')
    level = sgqlc.types.Field(Byte, graphql_name='level')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    gold_spent = sgqlc.types.Field(Int, graphql_name='goldSpent')
    hero_damage = sgqlc.types.Field(Int, graphql_name='heroDamage')
    tower_damage = sgqlc.types.Field(Int, graphql_name='towerDamage')
    hero_healing = sgqlc.types.Field(Int, graphql_name='heroHealing')
    party_id = sgqlc.types.Field(Byte, graphql_name='partyId')
    is_random = sgqlc.types.Field(Boolean, graphql_name='isRandom')
    lane = sgqlc.types.Field(MatchLaneType, graphql_name='lane')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    streak_prediction = sgqlc.types.Field(Short, graphql_name='streakPrediction')
    intentional_feeding = sgqlc.types.Field(Boolean, graphql_name='intentionalFeeding')
    role = sgqlc.types.Field(MatchPlayerRoleType, graphql_name='role')
    role_basic = sgqlc.types.Field(MatchPlayerRoleType, graphql_name='roleBasic')
    imp = sgqlc.types.Field(Short, graphql_name='imp')
    award = sgqlc.types.Field(MatchPlayerAward, graphql_name='award')
    item0_id = sgqlc.types.Field(Short, graphql_name='item0Id')
    item1_id = sgqlc.types.Field(Short, graphql_name='item1Id')
    item2_id = sgqlc.types.Field(Short, graphql_name='item2Id')
    item3_id = sgqlc.types.Field(Short, graphql_name='item3Id')
    item4_id = sgqlc.types.Field(Short, graphql_name='item4Id')
    item5_id = sgqlc.types.Field(Short, graphql_name='item5Id')
    backpack0_id = sgqlc.types.Field(Short, graphql_name='backpack0Id')
    backpack1_id = sgqlc.types.Field(Short, graphql_name='backpack1Id')
    backpack2_id = sgqlc.types.Field(Short, graphql_name='backpack2Id')
    neutral0_id = sgqlc.types.Field(Short, graphql_name='neutral0Id')
    behavior = sgqlc.types.Field(Short, graphql_name='behavior')
    stats = sgqlc.types.Field(MatchPlayerStatsType, graphql_name='stats')
    playback_data = sgqlc.types.Field(MatchPlayerPlaybackDataType, graphql_name='playbackData')
    hero_average = sgqlc.types.Field(sgqlc.types.list_of(HeroPositionTimeDetailType), graphql_name='heroAverage')
    additional_unit = sgqlc.types.Field(MatchPlayerAdditionalUnitType, graphql_name='additionalUnit')
    dota_plus = sgqlc.types.Field(HeroDotaPlusLeaderboardRankType, graphql_name='dotaPlus')
    abilities = sgqlc.types.Field(sgqlc.types.list_of('PlayerAbilityType'), graphql_name='abilities', args=sgqlc.types.ArgDict((
        ('game_verion_id', sgqlc.types.Arg(Int, graphql_name='gameVerionId', default=None)),
))
    )
    invisible_seconds = sgqlc.types.Field(Int, graphql_name='invisibleSeconds')
    dota_plus_hero_xp = sgqlc.types.Field(Int, graphql_name='dotaPlusHeroXp')
    variant = sgqlc.types.Field(Byte, graphql_name='variant')


class MatchPlayerWardDestuctionObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'gold', 'experience', 'is_ward')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    experience = sgqlc.types.Field(Int, graphql_name='experience')
    is_ward = sgqlc.types.Field(Boolean, graphql_name='isWard')


class MatchReplayUploadHeroDuoSummaryType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'win_count_with', 'win_count_against', 'match_count_with', 'match_count_against')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    win_count_with = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCountWith')
    win_count_against = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCountAgainst')
    match_count_with = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCountWith')
    match_count_against = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCountAgainst')


class MatchReplayUploadHeroSummaryType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'win_count_with', 'win_count_against', 'match_count_with', 'match_count_against', 'ban_count_with', 'ban_count_against', 'duos')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    win_count_with = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCountWith')
    win_count_against = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCountAgainst')
    match_count_with = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCountWith')
    match_count_against = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCountAgainst')
    ban_count_with = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='banCountWith')
    ban_count_against = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='banCountAgainst')
    duos = sgqlc.types.Field(sgqlc.types.list_of(MatchReplayUploadHeroDuoSummaryType), graphql_name='duos')


class MatchReplayUploadMatchType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_upload_team_id', 'id', 'file_name', 'uploader_captain_jack_identity_id', 'is_validated', 'is_complete', 'is_active', 'did_radiant_win', 'duration_seconds', 'duration_minutes', 'start_date_time', 'end_date_time', 'lobby_type', 'num_human_players', 'num_human_spectators', 'league_id', 'series_id', 'game_mode', 'radiant_team_id', 'radiant_kills', 'dire_team_id', 'dire_kills', 'is_radiant_first_pick', 'game_version_id', 'notes', 'players', 'spectators', 'pick_bans', 'radiant_team', 'dire_team', 'league')
    match_upload_team_id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='matchUploadTeamId')
    id = sgqlc.types.Field(Long, graphql_name='id')
    file_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='fileName')
    uploader_captain_jack_identity_id = sgqlc.types.Field(Guid, graphql_name='uploaderCaptainJackIdentityId')
    is_validated = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isValidated')
    is_complete = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isComplete')
    is_active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isActive')
    did_radiant_win = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='didRadiantWin')
    duration_seconds = sgqlc.types.Field(Short, graphql_name='durationSeconds')
    duration_minutes = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='durationMinutes')
    start_date_time = sgqlc.types.Field(DateTime, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(DateTime, graphql_name='endDateTime')
    lobby_type = sgqlc.types.Field(Byte, graphql_name='lobbyType')
    num_human_players = sgqlc.types.Field(Byte, graphql_name='numHumanPlayers')
    num_human_spectators = sgqlc.types.Field(Byte, graphql_name='numHumanSpectators')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    game_mode = sgqlc.types.Field(Byte, graphql_name='gameMode')
    radiant_team_id = sgqlc.types.Field(Int, graphql_name='radiantTeamId')
    radiant_kills = sgqlc.types.Field(Byte, graphql_name='radiantKills')
    dire_team_id = sgqlc.types.Field(Int, graphql_name='direTeamId')
    dire_kills = sgqlc.types.Field(Byte, graphql_name='direKills')
    is_radiant_first_pick = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRadiantFirstPick')
    game_version_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gameVersionId')
    notes = sgqlc.types.Field(String, graphql_name='notes')
    players = sgqlc.types.Field(sgqlc.types.list_of('MatchReplayUploadPlayerType'), graphql_name='players')
    spectators = sgqlc.types.Field(sgqlc.types.list_of(Long), graphql_name='spectators')
    pick_bans = sgqlc.types.Field(sgqlc.types.list_of('MatchReplayUploadPickBanType'), graphql_name='pickBans')
    radiant_team = sgqlc.types.Field('TeamType', graphql_name='radiantTeam')
    dire_team = sgqlc.types.Field('TeamType', graphql_name='direTeam')
    league = sgqlc.types.Field(LeagueType, graphql_name='league')


class MatchReplayUploadOverviewType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_count', 'win_count', 'matches')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    matches = sgqlc.types.Field(sgqlc.types.list_of(MatchReplayUploadMatchType), graphql_name='matches')


class MatchReplayUploadPickBanType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('player_slot', 'is_pick', 'hero_id', 'banned_hero_id', 'time', 'is_radiant', 'order', 'was_banned_successfully')
    player_slot = sgqlc.types.Field(Byte, graphql_name='playerSlot')
    is_pick = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPick')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    banned_hero_id = sgqlc.types.Field(Short, graphql_name='bannedHeroId')
    time = sgqlc.types.Field(Byte, graphql_name='time')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    order = sgqlc.types.Field(Byte, graphql_name='order')
    was_banned_successfully = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='wasBannedSuccessfully')


class MatchReplayUploadPlayerStatsItemsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('item0_id_list', 'item1_id_list', 'item2_id_list', 'item3_id_list', 'item4_id_list', 'item5_id_list', 'backpack0_id_list', 'backpack1_id_list', 'backpack2_id_list')
    item0_id_list = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='item0IdList')
    item1_id_list = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='item1IdList')
    item2_id_list = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='item2IdList')
    item3_id_list = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='item3IdList')
    item4_id_list = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='item4IdList')
    item5_id_list = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='item5IdList')
    backpack0_id_list = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='backpack0IdList')
    backpack1_id_list = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='backpack1IdList')
    backpack2_id_list = sgqlc.types.Field(sgqlc.types.list_of(Byte), graphql_name='backpack2IdList')


class MatchReplayUploadPlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'player_slot', 'match_upload_team_id', 'steam_account_id', 'steam_account', 'is_radiant', 'is_dire', 'team_slot', 'hero_id', 'kills', 'deaths', 'assists', 'networth', 'last_hits', 'denies', 'gold_per_minute', 'experience_per_minute', 'total_gold_spent', 'gold_spent_on_buybacks', 'gold_spent_on_consumables', 'gold_spent_on_items', 'gold_spent_on_support', 'hero_damage', 'tower_damage', 'tower_kills', 'hero_healing', 'level', 'item0_id', 'item1_id', 'item2_id', 'item3_id', 'item4_id', 'item5_id', 'backpack0_id', 'backpack1_id', 'backpack2_id', 'lane', 'role', 'position', 'pick_order', 'team_pick_order', 'is_victory', 'kills_list', 'assists_list', 'deaths_list', 'streak_list', 'level_list', 'total_earned_gold_list', 'reliable_gold_list', 'unreliable_gold_list', 'total_earned_xp_list', 'shared_gold_list', 'hero_kill_gold_list', 'creep_kill_gold_list', 'income_gold_list', 'networth_list', 'deny_count_list', 'last_hit_count_list', 'last_hit_streak_list', 'last_hit_multi_kill_list', 'nearby_creep_death_count_list', 'claimed_deny_count_list', 'claimed_miss_count_list', 'miss_count_list', 'stuns_list', 'hero_healing_list', 'tower_kills_list', 'roshan_kills_list', 'observer_wards_placed_list', 'sentry_wards_placed_list', 'creep_stack_list', 'camp_stack_list', 'rune_picksup_list', 'gold_spent_on_support_list', 'hero_damage_list', 'wards_purchased_list', 'wards_destroyed_list', 'commands_issued_list', 'gold_spent_on_consumables_list', 'gold_spent_on_items_list', 'gold_spent_on_buybacks_list', 'gold_lost_to_death_list', 'max_health_list', 'max_mana_list', 'bkb_charges_used_list', 'damage_min_list', 'damage_max_list', 'damage_bonus_list', 'strength_total_list', 'agility_total_list', 'intellect_total_list', 'tower_damage_list', 'items')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    player_slot = sgqlc.types.Field(Byte, graphql_name='playerSlot')
    match_upload_team_id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='matchUploadTeamId')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    is_radiant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRadiant')
    is_dire = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDire')
    team_slot = sgqlc.types.Field(Byte, graphql_name='teamSlot')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    kills = sgqlc.types.Field(Byte, graphql_name='kills')
    deaths = sgqlc.types.Field(Byte, graphql_name='deaths')
    assists = sgqlc.types.Field(Byte, graphql_name='assists')
    networth = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='networth')
    last_hits = sgqlc.types.Field(Short, graphql_name='lastHits')
    denies = sgqlc.types.Field(Short, graphql_name='denies')
    gold_per_minute = sgqlc.types.Field(Short, graphql_name='goldPerMinute')
    experience_per_minute = sgqlc.types.Field(Short, graphql_name='experiencePerMinute')
    total_gold_spent = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalGoldSpent')
    gold_spent_on_buybacks = sgqlc.types.Field(Int, graphql_name='goldSpentOnBuybacks')
    gold_spent_on_consumables = sgqlc.types.Field(Int, graphql_name='goldSpentOnConsumables')
    gold_spent_on_items = sgqlc.types.Field(Int, graphql_name='goldSpentOnItems')
    gold_spent_on_support = sgqlc.types.Field(Int, graphql_name='goldSpentOnSupport')
    hero_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroDamage')
    tower_damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='towerDamage')
    tower_kills = sgqlc.types.Field(Short, graphql_name='towerKills')
    hero_healing = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroHealing')
    level = sgqlc.types.Field(Byte, graphql_name='level')
    item0_id = sgqlc.types.Field(Short, graphql_name='item0Id')
    item1_id = sgqlc.types.Field(Short, graphql_name='item1Id')
    item2_id = sgqlc.types.Field(Short, graphql_name='item2Id')
    item3_id = sgqlc.types.Field(Short, graphql_name='item3Id')
    item4_id = sgqlc.types.Field(Short, graphql_name='item4Id')
    item5_id = sgqlc.types.Field(Short, graphql_name='item5Id')
    backpack0_id = sgqlc.types.Field(Short, graphql_name='backpack0Id')
    backpack1_id = sgqlc.types.Field(Short, graphql_name='backpack1Id')
    backpack2_id = sgqlc.types.Field(Short, graphql_name='backpack2Id')
    lane = sgqlc.types.Field(MatchLaneType, graphql_name='lane')
    role = sgqlc.types.Field(MatchPlayerRoleType, graphql_name='role')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    pick_order = sgqlc.types.Field(Byte, graphql_name='pickOrder')
    team_pick_order = sgqlc.types.Field(MatchPlayerTeamPickOrderType, graphql_name='teamPickOrder')
    is_victory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVictory')
    kills_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='killsList')
    assists_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='assistsList')
    deaths_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='deathsList')
    streak_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='streakList')
    level_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='levelList')
    total_earned_gold_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='totalEarnedGoldList')
    reliable_gold_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='reliableGoldList')
    unreliable_gold_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='unreliableGoldList')
    total_earned_xp_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='totalEarnedXpList')
    shared_gold_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='sharedGoldList')
    hero_kill_gold_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='heroKillGoldList')
    creep_kill_gold_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='creepKillGoldList')
    income_gold_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='incomeGoldList')
    networth_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='networthList')
    deny_count_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='denyCountList')
    last_hit_count_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='lastHitCountList')
    last_hit_streak_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='lastHitStreakList')
    last_hit_multi_kill_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='lastHitMultiKillList')
    nearby_creep_death_count_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='nearbyCreepDeathCountList')
    claimed_deny_count_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='claimedDenyCountList')
    claimed_miss_count_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='claimedMissCountList')
    miss_count_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='missCountList')
    stuns_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='stunsList')
    hero_healing_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='heroHealingList')
    tower_kills_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='towerKillsList')
    roshan_kills_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='roshanKillsList')
    observer_wards_placed_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='observerWardsPlacedList')
    sentry_wards_placed_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='sentryWardsPlacedList')
    creep_stack_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='creepStackList')
    camp_stack_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='campStackList')
    rune_picksup_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='runePicksupList')
    gold_spent_on_support_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='goldSpentOnSupportList')
    hero_damage_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='heroDamageList')
    wards_purchased_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='wardsPurchasedList')
    wards_destroyed_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='wardsDestroyedList')
    commands_issued_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='commandsIssuedList')
    gold_spent_on_consumables_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='goldSpentOnConsumablesList')
    gold_spent_on_items_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='goldSpentOnItemsList')
    gold_spent_on_buybacks_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='goldSpentOnBuybacksList')
    gold_lost_to_death_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='goldLostToDeathList')
    max_health_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='maxHealthList')
    max_mana_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='maxManaList')
    bkb_charges_used_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='bkbChargesUsedList')
    damage_min_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='damageMinList')
    damage_max_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='damageMaxList')
    damage_bonus_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='damageBonusList')
    strength_total_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='strengthTotalList')
    agility_total_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='agilityTotalList')
    intellect_total_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='intellectTotalList')
    tower_damage_list = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='towerDamageList')
    items = sgqlc.types.Field(MatchReplayUploadPlayerStatsItemsType, graphql_name='items')


class MatchReplayUploadTeamMemberType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('captain_jack_identity_id', 'match_upload_team_id', 'is_admin', 'is_default_team', 'steam_account')
    captain_jack_identity_id = sgqlc.types.Field(Guid, graphql_name='captainJackIdentityId')
    match_upload_team_id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='matchUploadTeamId')
    is_admin = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAdmin')
    is_default_team = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isDefaultTeam')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')


class MatchReplayUploadTeamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'email', 'team_id', 'creator_captain_jack_identity_id', 'team', 'members', 'is_default')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    email = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='email')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='teamId')
    creator_captain_jack_identity_id = sgqlc.types.Field(Guid, graphql_name='creatorCaptainJackIdentityId')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    members = sgqlc.types.Field(sgqlc.types.list_of(MatchReplayUploadTeamMemberType), graphql_name='members')
    is_default = sgqlc.types.Field(Boolean, graphql_name='isDefault')


class MatchStatsChatEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'type', 'from_hero_id', 'to_hero_id', 'value', 'paused_tick', 'is_radiant')
    time = sgqlc.types.Field(Int, graphql_name='time')
    type = sgqlc.types.Field(Int, graphql_name='type')
    from_hero_id = sgqlc.types.Field(Short, graphql_name='fromHeroId')
    to_hero_id = sgqlc.types.Field(Short, graphql_name='toHeroId')
    value = sgqlc.types.Field(Short, graphql_name='value')
    paused_tick = sgqlc.types.Field(Int, graphql_name='pausedTick')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')


class MatchStatsLaneReportFactionLaneObject(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('melee_count', 'range_count', 'siege_count', 'deny_count', 'neutral_count')
    melee_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='meleeCount')
    range_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rangeCount')
    siege_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='siegeCount')
    deny_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='denyCount')
    neutral_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='neutralCount')


class MatchStatsLaneReportFactionObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('mid_lane', 'off_lane', 'safe_lane')
    mid_lane = sgqlc.types.Field(MatchStatsLaneReportFactionLaneObject, graphql_name='midLane')
    off_lane = sgqlc.types.Field(MatchStatsLaneReportFactionLaneObject, graphql_name='offLane')
    safe_lane = sgqlc.types.Field(MatchStatsLaneReportFactionLaneObject, graphql_name='safeLane')


class MatchStatsLaneReportType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('radiant', 'dire')
    radiant = sgqlc.types.Field(sgqlc.types.list_of(MatchStatsLaneReportFactionObjectType), graphql_name='radiant')
    dire = sgqlc.types.Field(sgqlc.types.list_of(MatchStatsLaneReportFactionObjectType), graphql_name='dire')


class MatchStatsOutpostReportObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('npc_id', 'is_controlled_by_radiant', 'is_radiant_side')
    npc_id = sgqlc.types.Field(Int, graphql_name='npcId')
    is_controlled_by_radiant = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isControlledByRadiant')
    is_radiant_side = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRadiantSide')


class MatchStatsPickBanType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_pick', 'hero_id', 'order', 'banned_hero_id', 'is_radiant', 'player_index', 'was_banned_successfully', 'is_captain', 'base_win_rate', 'adjusted_win_rate', 'letter')
    is_pick = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPick')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    order = sgqlc.types.Field(Int, graphql_name='order')
    banned_hero_id = sgqlc.types.Field(Short, graphql_name='bannedHeroId')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    player_index = sgqlc.types.Field(Int, graphql_name='playerIndex')
    was_banned_successfully = sgqlc.types.Field(Boolean, graphql_name='wasBannedSuccessfully')
    is_captain = sgqlc.types.Field(Boolean, graphql_name='isCaptain')
    base_win_rate = sgqlc.types.Field(Byte, graphql_name='baseWinRate')
    adjusted_win_rate = sgqlc.types.Field(Byte, graphql_name='adjustedWinRate')
    letter = sgqlc.types.Field(Int, graphql_name='letter')


class MatchStatsTowerDeathType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'npc_id', 'is_radiant', 'attacker')
    time = sgqlc.types.Field(Int, graphql_name='time')
    npc_id = sgqlc.types.Field(Short, graphql_name='npcId')
    is_radiant = sgqlc.types.Field(Boolean, graphql_name='isRadiant')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')


class MatchStatsTowerReportObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('npc_id', 'hp')
    npc_id = sgqlc.types.Field(Int, graphql_name='npcId')
    hp = sgqlc.types.Field(Int, graphql_name='hp')


class MatchStatsTowerReportType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('towers', 'outposts')
    towers = sgqlc.types.Field(sgqlc.types.list_of(MatchStatsTowerReportObjectType), graphql_name='towers')
    outposts = sgqlc.types.Field(sgqlc.types.list_of(MatchStatsOutpostReportObjectType), graphql_name='outposts')


class MatchType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'did_radiant_win', 'duration_seconds', 'start_date_time', 'end_date_time', 'tower_status_radiant', 'tower_status_dire', 'barracks_status_radiant', 'barracks_status_dire', 'cluster_id', 'first_blood_time', 'lobby_type', 'num_human_players', 'game_mode', 'replay_salt', 'is_stats', 'tournament_id', 'tournament_round', 'actual_rank', 'average_rank', 'average_imp', 'parsed_date_time', 'stats_date_time', 'league_id', 'league', 'radiant_team_id', 'radiant_team', 'dire_team_id', 'dire_team', 'series_id', 'series', 'game_version_id', 'region_id', 'sequence_num', 'rank', 'bracket', 'analysis_outcome', 'predicted_outcome_weight', 'players', 'radiant_networth_leads', 'radiant_experience_leads', 'radiant_kills', 'dire_kills', 'pick_bans', 'tower_status', 'lane_report', 'win_rates', 'predicted_win_rates', 'chat_events', 'tower_deaths', 'playback_data', 'spectators', 'bottom_lane_outcome', 'mid_lane_outcome', 'top_lane_outcome', 'did_request_download')
    id = sgqlc.types.Field(Long, graphql_name='id')
    did_radiant_win = sgqlc.types.Field(Boolean, graphql_name='didRadiantWin')
    duration_seconds = sgqlc.types.Field(Int, graphql_name='durationSeconds')
    start_date_time = sgqlc.types.Field(Long, graphql_name='startDateTime')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    tower_status_radiant = sgqlc.types.Field(Int, graphql_name='towerStatusRadiant')
    tower_status_dire = sgqlc.types.Field(Int, graphql_name='towerStatusDire')
    barracks_status_radiant = sgqlc.types.Field(Short, graphql_name='barracksStatusRadiant')
    barracks_status_dire = sgqlc.types.Field(Short, graphql_name='barracksStatusDire')
    cluster_id = sgqlc.types.Field(Int, graphql_name='clusterId')
    first_blood_time = sgqlc.types.Field(Int, graphql_name='firstBloodTime')
    lobby_type = sgqlc.types.Field(LobbyTypeEnum, graphql_name='lobbyType')
    num_human_players = sgqlc.types.Field(Int, graphql_name='numHumanPlayers')
    game_mode = sgqlc.types.Field(GameModeEnumType, graphql_name='gameMode')
    replay_salt = sgqlc.types.Field(Long, graphql_name='replaySalt')
    is_stats = sgqlc.types.Field(Boolean, graphql_name='isStats')
    tournament_id = sgqlc.types.Field(Int, graphql_name='tournamentId')
    tournament_round = sgqlc.types.Field(Short, graphql_name='tournamentRound')
    actual_rank = sgqlc.types.Field(Short, graphql_name='actualRank')
    average_rank = sgqlc.types.Field(Short, graphql_name='averageRank')
    average_imp = sgqlc.types.Field(Short, graphql_name='averageImp')
    parsed_date_time = sgqlc.types.Field(Long, graphql_name='parsedDateTime')
    stats_date_time = sgqlc.types.Field(Long, graphql_name='statsDateTime')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    league = sgqlc.types.Field(LeagueType, graphql_name='league')
    radiant_team_id = sgqlc.types.Field(Int, graphql_name='radiantTeamId')
    radiant_team = sgqlc.types.Field('TeamType', graphql_name='radiantTeam')
    dire_team_id = sgqlc.types.Field(Int, graphql_name='direTeamId')
    dire_team = sgqlc.types.Field('TeamType', graphql_name='direTeam')
    series_id = sgqlc.types.Field(Long, graphql_name='seriesId')
    series = sgqlc.types.Field('SeriesType', graphql_name='series')
    game_version_id = sgqlc.types.Field(Short, graphql_name='gameVersionId')
    region_id = sgqlc.types.Field(Byte, graphql_name='regionId')
    sequence_num = sgqlc.types.Field(Long, graphql_name='sequenceNum')
    rank = sgqlc.types.Field(Int, graphql_name='rank')
    bracket = sgqlc.types.Field(Byte, graphql_name='bracket')
    analysis_outcome = sgqlc.types.Field(MatchAnalysisOutcomeType, graphql_name='analysisOutcome')
    predicted_outcome_weight = sgqlc.types.Field(Byte, graphql_name='predictedOutcomeWeight')
    players = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerType), graphql_name='players', args=sgqlc.types.ArgDict((
        ('steam_account_id', sgqlc.types.Arg(Long, graphql_name='steamAccountId', default=None)),
))
    )
    radiant_networth_leads = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='radiantNetworthLeads')
    radiant_experience_leads = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='radiantExperienceLeads')
    radiant_kills = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='radiantKills')
    dire_kills = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='direKills')
    pick_bans = sgqlc.types.Field(sgqlc.types.list_of(MatchStatsPickBanType), graphql_name='pickBans')
    tower_status = sgqlc.types.Field(sgqlc.types.list_of(MatchStatsTowerReportType), graphql_name='towerStatus')
    lane_report = sgqlc.types.Field(MatchStatsLaneReportType, graphql_name='laneReport')
    win_rates = sgqlc.types.Field(sgqlc.types.list_of(Decimal), graphql_name='winRates')
    predicted_win_rates = sgqlc.types.Field(sgqlc.types.list_of(Decimal), graphql_name='predictedWinRates')
    chat_events = sgqlc.types.Field(sgqlc.types.list_of(MatchStatsChatEventType), graphql_name='chatEvents')
    tower_deaths = sgqlc.types.Field(sgqlc.types.list_of(MatchStatsTowerDeathType), graphql_name='towerDeaths')
    playback_data = sgqlc.types.Field(MatchPlaybackDataType, graphql_name='playbackData')
    spectators = sgqlc.types.Field(sgqlc.types.list_of(MatchPlayerSpectatorType), graphql_name='spectators')
    bottom_lane_outcome = sgqlc.types.Field(LaneOutcomeEnums, graphql_name='bottomLaneOutcome')
    mid_lane_outcome = sgqlc.types.Field(LaneOutcomeEnums, graphql_name='midLaneOutcome')
    top_lane_outcome = sgqlc.types.Field(LaneOutcomeEnums, graphql_name='topLaneOutcome')
    did_request_download = sgqlc.types.Field(Boolean, graphql_name='didRequestDownload')


class MatchesDayType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('day', 'match_count')
    day = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='day')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')


class MatchesGameVersionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('game_version_id', 'match_count')
    game_version_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='gameVersionId')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')


class MatchesHourType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hour', 'match_count')
    hour = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='hour')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')


class MatchesMonthType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('month', 'match_count')
    month = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='month')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')


class MatchesWeekType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('week', 'match_count')
    week = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='week')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')


class MatchmakingStatsType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'u_swest', 'u_seast', 'europe', 'singapore', 'brazil', 'stockholm', 'austria', 'australia', 'south_africa', 'perfect_world_telecom', 'perfect_world_unicom', 'dubai', 'chile', 'peru', 'india', 'perfect_world_telecom_guangdong', 'perfect_world_telecom_zhejiang', 'japan', 'perfect_world_telecom_wuhan', 'taiwan', 'perfect_world_unicom_tianjin')
    time = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='time')
    u_swest = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='uSWest')
    u_seast = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='uSEast')
    europe = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='europe')
    singapore = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='singapore')
    brazil = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='brazil')
    stockholm = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='stockholm')
    austria = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='austria')
    australia = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='australia')
    south_africa = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='southAfrica')
    perfect_world_telecom = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='perfectWorldTelecom')
    perfect_world_unicom = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='perfectWorldUnicom')
    dubai = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='dubai')
    chile = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='chile')
    peru = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='peru')
    india = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='india')
    perfect_world_telecom_guangdong = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='perfectWorldTelecomGuangdong')
    perfect_world_telecom_zhejiang = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='perfectWorldTelecomZhejiang')
    japan = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='japan')
    perfect_world_telecom_wuhan = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='perfectWorldTelecomWuhan')
    taiwan = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='taiwan')
    perfect_world_unicom_tianjin = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='perfectWorldUnicomTianjin')


class MatchplaybackDataCourierEventObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'position_x', 'position_y', 'hp', 'is_flying', 'respawn_time', 'did_cast_boost', 'item0_id', 'item1_id', 'item2_id', 'item3_id', 'item4_id', 'item5_id')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')
    hp = sgqlc.types.Field(Int, graphql_name='hp')
    is_flying = sgqlc.types.Field(Boolean, graphql_name='isFlying')
    respawn_time = sgqlc.types.Field(Int, graphql_name='respawnTime')
    did_cast_boost = sgqlc.types.Field(Boolean, graphql_name='didCastBoost')
    item0_id = sgqlc.types.Field(Int, graphql_name='item0Id')
    item1_id = sgqlc.types.Field(Int, graphql_name='item1Id')
    item2_id = sgqlc.types.Field(Int, graphql_name='item2Id')
    item3_id = sgqlc.types.Field(Int, graphql_name='item3Id')
    item4_id = sgqlc.types.Field(Int, graphql_name='item4Id')
    item5_id = sgqlc.types.Field(Int, graphql_name='item5Id')


class ModifierType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'buff_duration', 'is_root', 'is_stun', 'is_silence', 'is_invisible', 'is_shackle', 'is_hex', 'is_sleep', 'is_cyclone', 'is_taunt', 'is_disarm', 'is_blind', 'is_ethereal', 'is_movement_slow', 'is_attack_slow', 'is_break', 'is_armor_reduce', 'is_attack_reduce', 'is_mute', 'is_damage_amplified', 'is_movement_debuff', 'is_knockback', 'is_weaken', 'is_item', 'is_banished')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    buff_duration = sgqlc.types.Field(Int, graphql_name='buffDuration')
    is_root = sgqlc.types.Field(Boolean, graphql_name='isRoot')
    is_stun = sgqlc.types.Field(Boolean, graphql_name='isStun')
    is_silence = sgqlc.types.Field(Boolean, graphql_name='isSilence')
    is_invisible = sgqlc.types.Field(Boolean, graphql_name='isInvisible')
    is_shackle = sgqlc.types.Field(Boolean, graphql_name='isShackle')
    is_hex = sgqlc.types.Field(Boolean, graphql_name='isHex')
    is_sleep = sgqlc.types.Field(Boolean, graphql_name='isSleep')
    is_cyclone = sgqlc.types.Field(Boolean, graphql_name='isCyclone')
    is_taunt = sgqlc.types.Field(Boolean, graphql_name='isTaunt')
    is_disarm = sgqlc.types.Field(Boolean, graphql_name='isDisarm')
    is_blind = sgqlc.types.Field(Boolean, graphql_name='isBlind')
    is_ethereal = sgqlc.types.Field(Boolean, graphql_name='isEthereal')
    is_movement_slow = sgqlc.types.Field(Boolean, graphql_name='isMovementSlow')
    is_attack_slow = sgqlc.types.Field(Boolean, graphql_name='isAttackSlow')
    is_break = sgqlc.types.Field(Boolean, graphql_name='isBreak')
    is_armor_reduce = sgqlc.types.Field(Boolean, graphql_name='isArmorReduce')
    is_attack_reduce = sgqlc.types.Field(Boolean, graphql_name='isAttackReduce')
    is_mute = sgqlc.types.Field(Boolean, graphql_name='isMute')
    is_damage_amplified = sgqlc.types.Field(Boolean, graphql_name='isDamageAmplified')
    is_movement_debuff = sgqlc.types.Field(Boolean, graphql_name='isMovementDebuff')
    is_knockback = sgqlc.types.Field(Boolean, graphql_name='isKnockback')
    is_weaken = sgqlc.types.Field(Boolean, graphql_name='isWeaken')
    is_item = sgqlc.types.Field(Boolean, graphql_name='isItem')
    is_banished = sgqlc.types.Field(Boolean, graphql_name='isBanished')


class NewsItemType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'title', 'uri', 'author', 'contents', 'feed_label', 'date', 'feed_name')
    id = sgqlc.types.Field(Long, graphql_name='id')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    uri = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uri')
    author = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='author')
    contents = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='contents')
    feed_label = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='feedLabel')
    date = sgqlc.types.Field(Long, graphql_name='date')
    feed_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='feedName')


class NpcStatType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('level', 'status_health', 'status_health_regen', 'status_mana', 'status_mana_regen', 'movement_speed', 'movement_turn_rate', 'day_time_vision', 'night_time_vision', 'attack_range_buffer', 'attack_range', 'is_neutral_unit_type', 'is_ancient', 'can_be_dominated', 'auto_attacks_by_default', 'attack_damage_min', 'attack_damage_max', 'attack_rate', 'attack_animation_point', 'projectile_speed', 'team_name', 'combat_class_attack', 'combat_class_defend', 'unit_relationship_class', 'attack_desire', 'has_inventory', 'wakes_neutrals')
    level = sgqlc.types.Field(Float, graphql_name='level')
    status_health = sgqlc.types.Field(Float, graphql_name='statusHealth')
    status_health_regen = sgqlc.types.Field(Float, graphql_name='statusHealthRegen')
    status_mana = sgqlc.types.Field(Float, graphql_name='statusMana')
    status_mana_regen = sgqlc.types.Field(Float, graphql_name='statusManaRegen')
    movement_speed = sgqlc.types.Field(Float, graphql_name='movementSpeed')
    movement_turn_rate = sgqlc.types.Field(Float, graphql_name='movementTurnRate')
    day_time_vision = sgqlc.types.Field(Float, graphql_name='dayTimeVision')
    night_time_vision = sgqlc.types.Field(Float, graphql_name='nightTimeVision')
    attack_range_buffer = sgqlc.types.Field(Float, graphql_name='attackRangeBuffer')
    attack_range = sgqlc.types.Field(Float, graphql_name='attackRange')
    is_neutral_unit_type = sgqlc.types.Field(Boolean, graphql_name='isNeutralUnitType')
    is_ancient = sgqlc.types.Field(Boolean, graphql_name='isAncient')
    can_be_dominated = sgqlc.types.Field(Boolean, graphql_name='canBeDominated')
    auto_attacks_by_default = sgqlc.types.Field(Boolean, graphql_name='autoAttacksByDefault')
    attack_damage_min = sgqlc.types.Field(Float, graphql_name='attackDamageMin')
    attack_damage_max = sgqlc.types.Field(Float, graphql_name='attackDamageMax')
    attack_rate = sgqlc.types.Field(Float, graphql_name='attackRate')
    attack_animation_point = sgqlc.types.Field(Float, graphql_name='attackAnimationPoint')
    projectile_speed = sgqlc.types.Field(Float, graphql_name='projectileSpeed')
    team_name = sgqlc.types.Field(String, graphql_name='teamName')
    combat_class_attack = sgqlc.types.Field(String, graphql_name='combatClassAttack')
    combat_class_defend = sgqlc.types.Field(String, graphql_name='combatClassDefend')
    unit_relationship_class = sgqlc.types.Field(String, graphql_name='unitRelationshipClass')
    attack_desire = sgqlc.types.Field(Float, graphql_name='attackDesire')
    has_inventory = sgqlc.types.Field(Boolean, graphql_name='hasInventory')
    wakes_neutrals = sgqlc.types.Field(Boolean, graphql_name='wakesNeutrals')


class NpcType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'stat')
    id = sgqlc.types.Field(Short, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    stat = sgqlc.types.Field(NpcStatType, graphql_name='stat')


class PageAghanimQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match', 'matches', 'hero_compositions', 'hero_composition', 'win_rate', 'hero_ability', 'room', 'room_modifier')
    match = sgqlc.types.Field(AghanimLabMatchType, graphql_name='match', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    matches = sgqlc.types.Field(sgqlc.types.list_of(AghanimLabMatchType), graphql_name='matches', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(FilterAghanimLabMatchRequestType, graphql_name='request', default=None)),
))
    )
    hero_compositions = sgqlc.types.Field(sgqlc.types.list_of(AghanimLabHeroCompositionType), graphql_name='heroCompositions', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(FilterAghanimLabHeroCompositionRequestType), graphql_name='request', default=None)),
))
    )
    hero_composition = sgqlc.types.Field(AghanimLabHeroCompositionType, graphql_name='heroComposition', args=sgqlc.types.ArgDict((
        ('hero_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Short)), graphql_name='heroIds', default=None)),
        ('difficulty', sgqlc.types.Arg(sgqlc.types.non_null(AghanimLabMatchDifficultyEnum), graphql_name='difficulty', default=None)),
))
    )
    win_rate = sgqlc.types.Field(AghanimLabHeroWinRateType, graphql_name='winRate', args=sgqlc.types.ArgDict((
        ('difficulty', sgqlc.types.Arg(sgqlc.types.non_null(AghanimLabMatchDifficultyEnum), graphql_name='difficulty', default=None)),
))
    )
    hero_ability = sgqlc.types.Field(sgqlc.types.list_of(AghanimLabHeroAbilityType), graphql_name='heroAbility', args=sgqlc.types.ArgDict((
        ('difficulty', sgqlc.types.Arg(sgqlc.types.non_null(AghanimLabMatchDifficultyEnum), graphql_name='difficulty', default=None)),
))
    )
    room = sgqlc.types.Field(sgqlc.types.list_of(AghanimLabRoomType), graphql_name='room', args=sgqlc.types.ArgDict((
        ('difficulty', sgqlc.types.Arg(sgqlc.types.non_null(AghanimLabMatchDifficultyEnum), graphql_name='difficulty', default=None)),
))
    )
    room_modifier = sgqlc.types.Field(sgqlc.types.list_of('TI2020CustomGameRoomModifierType'), graphql_name='roomModifier', args=sgqlc.types.ArgDict((
        ('difficulty', sgqlc.types.Arg(sgqlc.types.non_null(AghanimLabMatchDifficultyEnum), graphql_name='difficulty', default=None)),
))
    )


class PageBattlepassQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('predictions_hero', 'predictions_teams', 'predictions_players', 'predictions_tournament')
    predictions_hero = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionHeroType), graphql_name='predictionsHero', args=sgqlc.types.ArgDict((
        ('league_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='leagueIds', default=None)),
))
    )
    predictions_teams = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionTeamType), graphql_name='predictionsTeams', args=sgqlc.types.ArgDict((
        ('team_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='teamIds', default=None)),
        ('league_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='leagueIds', default=None)),
        ('averaged', sgqlc.types.Arg(Boolean, graphql_name='averaged', default=None)),
))
    )
    predictions_players = sgqlc.types.Field(sgqlc.types.list_of(BattlepassPredictionPlayerType), graphql_name='predictionsPlayers', args=sgqlc.types.ArgDict((
        ('team_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='teamIds', default=None)),
        ('league_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='leagueIds', default=None)),
))
    )
    predictions_tournament = sgqlc.types.Field(BattlepassPredictionTournamentType, graphql_name='predictionsTournament', args=sgqlc.types.ArgDict((
        ('team_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='teamIds', default=None)),
        ('league_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Int)), graphql_name='leagueIds', default=None)),
))
    )


class PageDireTideQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match', 'matches', 'win_day')
    match = sgqlc.types.Field(DireTideCustomGameMatchType, graphql_name='match', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    matches = sgqlc.types.Field(sgqlc.types.list_of(DireTideCustomGameMatchType), graphql_name='matches', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(FilterDireTideCustomMatchRequestType), graphql_name='request', default=None)),
))
    )
    win_day = sgqlc.types.Field(sgqlc.types.list_of(DireTideCustomGameHeroWinDayType), graphql_name='winDay', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )


class PageLeaguesQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('dpc_position_stats',)
    dpc_position_stats = sgqlc.types.Field(sgqlc.types.list_of(LeagueDpcPositionStatObjectType), graphql_name='dpcPositionStats')


class PageMatchesQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('matches_stats_hour', 'matches_stats_day', 'matches_stats_week', 'matches_stats_month', 'matches_stats_game_version', 'matchmaking_stats')
    matches_stats_hour = sgqlc.types.Field(sgqlc.types.list_of(MatchesHourType), graphql_name='matchesStatsHour', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('bracket_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds', default=None)),
        ('region_ids', sgqlc.types.Arg(sgqlc.types.list_of(BasicRegionType), graphql_name='regionIds', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.list_of(GameModeEnumType), graphql_name='gameModeIds', default=None)),
))
    )
    matches_stats_day = sgqlc.types.Field(sgqlc.types.list_of(MatchesDayType), graphql_name='matchesStatsDay', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('bracket_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds', default=None)),
        ('region_ids', sgqlc.types.Arg(sgqlc.types.list_of(BasicRegionType), graphql_name='regionIds', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.list_of(GameModeEnumType), graphql_name='gameModeIds', default=None)),
))
    )
    matches_stats_week = sgqlc.types.Field(sgqlc.types.list_of(MatchesWeekType), graphql_name='matchesStatsWeek', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('bracket_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds', default=None)),
        ('region_ids', sgqlc.types.Arg(sgqlc.types.list_of(BasicRegionType), graphql_name='regionIds', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.list_of(GameModeEnumType), graphql_name='gameModeIds', default=None)),
))
    )
    matches_stats_month = sgqlc.types.Field(sgqlc.types.list_of(MatchesMonthType), graphql_name='matchesStatsMonth', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('bracket_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds', default=None)),
        ('region_ids', sgqlc.types.Arg(sgqlc.types.list_of(BasicRegionType), graphql_name='regionIds', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.list_of(GameModeEnumType), graphql_name='gameModeIds', default=None)),
))
    )
    matches_stats_game_version = sgqlc.types.Field(sgqlc.types.list_of(MatchesGameVersionType), graphql_name='matchesStatsGameVersion', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('bracket_ids', sgqlc.types.Arg(sgqlc.types.list_of(RankBracket), graphql_name='bracketIds', default=None)),
        ('region_ids', sgqlc.types.Arg(sgqlc.types.list_of(BasicRegionType), graphql_name='regionIds', default=None)),
        ('game_mode_ids', sgqlc.types.Arg(sgqlc.types.list_of(GameModeEnumType), graphql_name='gameModeIds', default=None)),
))
    )
    matchmaking_stats = sgqlc.types.Field(sgqlc.types.list_of(MatchmakingStatsType), graphql_name='matchmakingStats')


class PagePlayerQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('conduct', 'simple_summary', 'performance', 'hero_performance', 'heroes_performance', 'played_with_pro', 'breakdown', 'peers')
    conduct = sgqlc.types.Field('PlayerConductResponseType', graphql_name='conduct')
    simple_summary = sgqlc.types.Field('PlayerCardHoverType', graphql_name='simpleSummary')
    performance = sgqlc.types.Field('PlayerPerformanceType', graphql_name='performance', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlayerPerformanceMatchesRequestType), graphql_name='request', default=None)),
))
    )
    hero_performance = sgqlc.types.Field('PlayerPerformanceType', graphql_name='heroPerformance', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlayerHeroPerformanceMatchesRequestType), graphql_name='request', default=None)),
))
    )
    heroes_performance = sgqlc.types.Field(sgqlc.types.list_of('PlayerHeroesPerformanceType'), graphql_name='heroesPerformance', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(PlayerHeroesPerformanceMatchesRequestType, graphql_name='request', default=None)),
))
    )
    played_with_pro = sgqlc.types.Field('PlayerPlayedWithProType', graphql_name='playedWithPro')
    breakdown = sgqlc.types.Field('PlayerBreakdownType', graphql_name='breakdown', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlayerBreakdownRequestType), graphql_name='request', default=None)),
))
    )
    peers = sgqlc.types.Field(sgqlc.types.list_of('PlayerTeammateType'), graphql_name='peers', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlayerTeammatesGroupByRequestType), graphql_name='request', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )


class PagePlayersQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_by_rank',)
    steam_account_by_rank = sgqlc.types.Field(sgqlc.types.list_of('SteamAccountByRankType'), graphql_name='steamAccountByRank', args=sgqlc.types.ArgDict((
        ('week', sgqlc.types.Arg(Long, graphql_name='week', default=None)),
))
    )


class PageQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('player', 'players', 'matches', 'leagues', 'aghanim', 'imp', 'dire_tide', 'battle_pass', 'rosh')
    player = sgqlc.types.Field(PagePlayerQuery, graphql_name='player', args=sgqlc.types.ArgDict((
        ('steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='steamAccountId', default=None)),
))
    )
    players = sgqlc.types.Field(PagePlayersQuery, graphql_name='players')
    matches = sgqlc.types.Field(PageMatchesQuery, graphql_name='matches')
    leagues = sgqlc.types.Field(PageLeaguesQuery, graphql_name='leagues')
    aghanim = sgqlc.types.Field(PageAghanimQuery, graphql_name='aghanim')
    imp = sgqlc.types.Field(ImpQuery, graphql_name='imp')
    dire_tide = sgqlc.types.Field(PageDireTideQuery, graphql_name='direTide')
    battle_pass = sgqlc.types.Field(PageBattlepassQuery, graphql_name='battlePass')
    rosh = sgqlc.types.Field('RoshQuery', graphql_name='rosh')


class PatchNoteLanguageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'game_version_id', 'language_id', 'index', 'ability_id', 'item_id', 'hero_id', 'general_id', 'text')
    id = sgqlc.types.Field(String, graphql_name='id')
    game_version_id = sgqlc.types.Field(Short, graphql_name='gameVersionId')
    language_id = sgqlc.types.Field(Byte, graphql_name='languageId')
    index = sgqlc.types.Field(Byte, graphql_name='index')
    ability_id = sgqlc.types.Field(Short, graphql_name='abilityId')
    item_id = sgqlc.types.Field(Short, graphql_name='itemId')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    general_id = sgqlc.types.Field(PatchNoteType, graphql_name='generalId')
    text = sgqlc.types.Field(String, graphql_name='text')


class PlayerAbilityType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('ability_id', 'time', 'level', 'game_version_id', 'ability_type', 'is_talent')
    ability_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='abilityId')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='level')
    game_version_id = sgqlc.types.Field(Short, graphql_name='gameVersionId')
    ability_type = sgqlc.types.Field(AbilityType, graphql_name='abilityType', args=sgqlc.types.ArgDict((
        ('game_verion_id', sgqlc.types.Arg(Int, graphql_name='gameVerionId', default=None)),
        ('langauge_id', sgqlc.types.Arg(Int, graphql_name='langaugeId', default=None)),
))
    )
    is_talent = sgqlc.types.Field(Boolean, graphql_name='isTalent')


class PlayerActivitySummaryType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('activity',)
    activity = sgqlc.types.Field(PlayerBehaviorActivity, graphql_name='activity')


class PlayerBadgeType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('badge_id', 'slot', 'created_date_time')
    badge_id = sgqlc.types.Field(Byte, graphql_name='badgeId')
    slot = sgqlc.types.Field(Byte, graphql_name='slot')
    created_date_time = sgqlc.types.Field(Long, graphql_name='createdDateTime')


class PlayerBattlePassGroupByType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'player_count', 'sum_levels', 'player_count_at')
    id = sgqlc.types.Field(String, graphql_name='id')
    player_count = sgqlc.types.Field(Long, graphql_name='playerCount')
    sum_levels = sgqlc.types.Field(Long, graphql_name='sumLevels')
    player_count_at = sgqlc.types.Field(Long, graphql_name='playerCountAt')


class PlayerBattlePassResponseType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('players', 'levels')
    players = sgqlc.types.Field(sgqlc.types.list_of('PlayerBattlePassType'), graphql_name='players', args=sgqlc.types.ArgDict((
        ('minimum_level', sgqlc.types.Arg(Int, graphql_name='minimumLevel', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    levels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='levels')


class PlayerBattlePassType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'level')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='level')


class PlayerBreakdownObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'match_count', 'win', 'imp', 'last_seen_date_time')
    id = sgqlc.types.Field(Int, graphql_name='id')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    win = sgqlc.types.Field(Int, graphql_name='win')
    imp = sgqlc.types.Field(Int, graphql_name='imp')
    last_seen_date_time = sgqlc.types.Field(Long, graphql_name='lastSeenDateTime')


class PlayerBreakdownType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('matches', 'is_stats_matches', 'rank_matches', 'lobby_matches', 'game_mode_matches', 'faction_matches', 'region_matches', 'lane_matches', 'role_matches', 'party_matches', 'imp_matches', 'duration_matches', 'hero_attribute_matches', 'day_of_week_matches', 'time_of_day_matches', 'week_end_matches')
    matches = sgqlc.types.Field(PlayerBreakdownObjectType, graphql_name='matches')
    is_stats_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='isStatsMatches')
    rank_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='rankMatches')
    lobby_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='lobbyMatches')
    game_mode_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='gameModeMatches')
    faction_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='factionMatches')
    region_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='regionMatches')
    lane_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='laneMatches')
    role_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='roleMatches')
    party_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='partyMatches')
    imp_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='impMatches')
    duration_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='durationMatches')
    hero_attribute_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='heroAttributeMatches')
    day_of_week_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='dayOfWeekMatches')
    time_of_day_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='timeOfDayMatches')
    week_end_matches = sgqlc.types.Field(sgqlc.types.list_of(PlayerBreakdownObjectType), graphql_name='weekEndMatches')


class PlayerCardHoverHeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'win_count', 'loss_count')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    loss_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='lossCount')


class PlayerCardHoverType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'last_update_date_time', 'match_count', 'core_count', 'support_count', 'imp', 'heroes', 'activity')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    last_update_date_time = sgqlc.types.Field(Long, graphql_name='lastUpdateDateTime')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    core_count = sgqlc.types.Field(Int, graphql_name='coreCount')
    support_count = sgqlc.types.Field(Int, graphql_name='supportCount')
    imp = sgqlc.types.Field(Int, graphql_name='imp')
    heroes = sgqlc.types.Field(sgqlc.types.list_of(PlayerCardHoverHeroType), graphql_name='heroes')
    activity = sgqlc.types.Field(Byte, graphql_name='activity')


class PlayerCoachingLeaderboardResponseType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('players', 'levels')
    players = sgqlc.types.Field(sgqlc.types.list_of('PlayerCoachingLeaderboardType'), graphql_name='players', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    levels = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Int))), graphql_name='levels')


class PlayerCoachingLeaderboardType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'rating', 'match_count', 'win_count', 'first_match_date_time', 'last_match_date_time')
    steam_account_id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    rating = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rating')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')


class PlayerConductResponseType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('last_incident_date_time', 'last_incident_match_id', 'recent_match_incidents', 'behavior_score')
    last_incident_date_time = sgqlc.types.Field(Long, graphql_name='lastIncidentDateTime')
    last_incident_match_id = sgqlc.types.Field(Long, graphql_name='lastIncidentMatchId')
    recent_match_incidents = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='recentMatchIncidents')
    behavior_score = sgqlc.types.Field(Short, graphql_name='behaviorScore')


class PlayerDraftHeroHighlightType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('last_played', 'win_count', 'match_count', 'imp_all_time', 'mvp_count_last_month', 'top_core_count_last_month', 'top_support_count_last_month', 'win_count_last_month', 'match_count_last_month', 'imp_last_month', 'win_count_last_six_months', 'match_count_last_six_months', 'imp_last_six_months')
    last_played = sgqlc.types.Field(Long, graphql_name='lastPlayed')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    imp_all_time = sgqlc.types.Field(Int, graphql_name='impAllTime')
    mvp_count_last_month = sgqlc.types.Field(Int, graphql_name='mvpCountLastMonth')
    top_core_count_last_month = sgqlc.types.Field(Int, graphql_name='topCoreCountLastMonth')
    top_support_count_last_month = sgqlc.types.Field(Int, graphql_name='topSupportCountLastMonth')
    win_count_last_month = sgqlc.types.Field(Int, graphql_name='winCountLastMonth')
    match_count_last_month = sgqlc.types.Field(Int, graphql_name='matchCountLastMonth')
    imp_last_month = sgqlc.types.Field(Int, graphql_name='impLastMonth')
    win_count_last_six_months = sgqlc.types.Field(Int, graphql_name='winCountLastSixMonths')
    match_count_last_six_months = sgqlc.types.Field(Int, graphql_name='matchCountLastSixMonths')
    imp_last_six_months = sgqlc.types.Field(Int, graphql_name='impLastSixMonths')


class PlayerHeroDotaPlusLeaderboardRankResponseType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('players',)
    players = sgqlc.types.Field(sgqlc.types.list_of(HeroDotaPlusLeaderboardRankType), graphql_name='players')


class PlayerHeroPerformanceLongestStreakType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'longest_streak', 'current_streak')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    longest_streak = sgqlc.types.Field(Int, graphql_name='longestStreak')
    current_streak = sgqlc.types.Field(Int, graphql_name='currentStreak')


class PlayerHeroesPerformanceScoreType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'score', 'match_count', 'win_count', 'imp')
    id = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='id')
    score = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='score')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    imp = sgqlc.types.Field(Int, graphql_name='imp')


class PlayerHeroesPerformanceType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'hero', 'win_count', 'k_da', 'avg_kills', 'avg_deaths', 'avg_assists', 'duration', 'imp', 'best', 'match_count', 'gold_per_minute', 'experience_per_minute', 'position_score', 'last_played_date_time')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='heroId')
    hero = sgqlc.types.Field(HeroType, graphql_name='hero')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    k_da = sgqlc.types.Field(Float, graphql_name='kDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    duration = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='duration')
    imp = sgqlc.types.Field(Int, graphql_name='imp')
    best = sgqlc.types.Field(Float, graphql_name='best')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    gold_per_minute = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='goldPerMinute')
    experience_per_minute = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='experiencePerMinute')
    position_score = sgqlc.types.Field(sgqlc.types.list_of(PlayerHeroesPerformanceScoreType), graphql_name='positionScore')
    last_played_date_time = sgqlc.types.Field(Long, graphql_name='lastPlayedDateTime')


class PlayerLeaderBoardByHeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'season_bracket', 'steam_account_id', 'steam_account', 'imp_average', 'position', 'wins', 'losses', 'win_streak', 'region_id', 'change_in_ranking', 'created_date_time')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    season_bracket = sgqlc.types.Field(Byte, graphql_name='seasonBracket')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    imp_average = sgqlc.types.Field(Byte, graphql_name='impAverage')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    wins = sgqlc.types.Field(Byte, graphql_name='wins')
    losses = sgqlc.types.Field(Byte, graphql_name='losses')
    win_streak = sgqlc.types.Field(Byte, graphql_name='winStreak')
    region_id = sgqlc.types.Field(Byte, graphql_name='regionId')
    change_in_ranking = sgqlc.types.Field(Short, graphql_name='changeInRanking')
    created_date_time = sgqlc.types.Field(Long, graphql_name='createdDateTime')


class PlayerPerformanceCompositionHeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'match_count', 'win_count')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')


class PlayerPerformanceCompositionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('allies', 'foes')
    allies = sgqlc.types.Field(sgqlc.types.list_of(PlayerPerformanceCompositionHeroType), graphql_name='allies')
    foes = sgqlc.types.Field(sgqlc.types.list_of(PlayerPerformanceCompositionHeroType), graphql_name='foes')


class PlayerPerformancePositionObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('lane_type', 'lane_match_count', 'lane_win_count')
    lane_type = sgqlc.types.Field(Byte, graphql_name='laneType')
    lane_match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='laneMatchCount')
    lane_win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='laneWinCount')


class PlayerPerformancePositionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('role_type', 'role_match_count', 'role_win_count', 'lanes')
    role_type = sgqlc.types.Field(MatchPlayerRoleType, graphql_name='roleType')
    role_match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='roleMatchCount')
    role_win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='roleWinCount')
    lanes = sgqlc.types.Field(sgqlc.types.list_of(PlayerPerformancePositionObjectType), graphql_name='lanes')


class PlayerPerformanceType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'match_count', 'win_count', 'streak', 'max_streak', 'imp', 'rank', 'mmr_tier', 'mmr_bracket', 'award_match_count', 'mvp_count', 'top_core_count', 'top_support_count', 'kills', 'kills_average', 'deaths', 'deaths_average', 'assists', 'assists_average', 'cs', 'cs_average', 'gpm', 'gpm_average', 'xpm', 'xpm_average', 'composition', 'position', 'pick_order')
    hero_id = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroId')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    streak = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='streak')
    max_streak = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxStreak')
    imp = sgqlc.types.Field(Int, graphql_name='imp')
    rank = sgqlc.types.Field(Int, graphql_name='rank')
    mmr_tier = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mmrTier')
    mmr_bracket = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mmrBracket')
    award_match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='awardMatchCount')
    mvp_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mvpCount')
    top_core_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='topCoreCount')
    top_support_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='topSupportCount')
    kills = sgqlc.types.Field(Int, graphql_name='kills')
    kills_average = sgqlc.types.Field(Decimal, graphql_name='killsAverage')
    deaths = sgqlc.types.Field(Int, graphql_name='deaths')
    deaths_average = sgqlc.types.Field(Decimal, graphql_name='deathsAverage')
    assists = sgqlc.types.Field(Int, graphql_name='assists')
    assists_average = sgqlc.types.Field(Decimal, graphql_name='assistsAverage')
    cs = sgqlc.types.Field(Int, graphql_name='cs')
    cs_average = sgqlc.types.Field(Decimal, graphql_name='csAverage')
    gpm = sgqlc.types.Field(Int, graphql_name='gpm')
    gpm_average = sgqlc.types.Field(Decimal, graphql_name='gpmAverage')
    xpm = sgqlc.types.Field(Int, graphql_name='xpm')
    xpm_average = sgqlc.types.Field(Decimal, graphql_name='xpmAverage')
    composition = sgqlc.types.Field(PlayerPerformanceCompositionType, graphql_name='composition')
    position = sgqlc.types.Field(sgqlc.types.list_of(PlayerPerformancePositionType), graphql_name='position')
    pick_order = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='pickOrder')


class PlayerPlayedWithProPlayerMatchType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'match')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    match = sgqlc.types.Field(MatchType, graphql_name='match')


class PlayerPlayedWithProPlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_id', 'steam_account', 'with_', 'vs')
    steam_id = sgqlc.types.Field(Long, graphql_name='steamId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    with_ = sgqlc.types.Field(PlayerPlayedWithProPlayerMatchType, graphql_name='with')
    vs = sgqlc.types.Field(PlayerPlayedWithProPlayerMatchType, graphql_name='vs')


class PlayerPlayedWithProTeamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('team_id', 'team_logo', 'team_name', 'players')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='teamId')
    team_logo = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamLogo')
    team_name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='teamName')
    players = sgqlc.types.Field(sgqlc.types.list_of(PlayerPlayedWithProPlayerType), graphql_name='players')


class PlayerPlayedWithProType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('played_count', 'total_count', 'casters', 'teams', 'international_winners')
    played_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='playedCount')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')
    casters = sgqlc.types.Field(sgqlc.types.list_of(PlayerPlayedWithProPlayerType), graphql_name='casters')
    teams = sgqlc.types.Field(sgqlc.types.list_of(PlayerPlayedWithProTeamType), graphql_name='teams')
    international_winners = sgqlc.types.Field(sgqlc.types.list_of(PlayerPlayedWithProTeamType), graphql_name='internationalWinners')


class PlayerRuneDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'rune', 'action', 'gold', 'position_x', 'position_y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    rune = sgqlc.types.Field(RuneEnums, graphql_name='rune')
    action = sgqlc.types.Field(RuneAction, graphql_name='action')
    gold = sgqlc.types.Field(Int, graphql_name='gold')
    position_x = sgqlc.types.Field(Int, graphql_name='positionX')
    position_y = sgqlc.types.Field(Int, graphql_name='positionY')


class PlayerTeammateType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'match_count', 'win_count', 'avg_imp', 'avg_gold_per_minute', 'avg_experience_per_minute', 'avg_kda', 'avg_kills', 'avg_deaths', 'avg_assists', 'last_match_date_time', 'first_match_date_time')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    avg_imp = sgqlc.types.Field(Int, graphql_name='avgImp')
    avg_gold_per_minute = sgqlc.types.Field(Int, graphql_name='avgGoldPerMinute')
    avg_experience_per_minute = sgqlc.types.Field(Int, graphql_name='avgExperiencePerMinute')
    avg_kda = sgqlc.types.Field(Float, graphql_name='avgKDA')
    avg_kills = sgqlc.types.Field(Float, graphql_name='avgKills')
    avg_deaths = sgqlc.types.Field(Float, graphql_name='avgDeaths')
    avg_assists = sgqlc.types.Field(Float, graphql_name='avgAssists')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')


class PlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'identity', 'steam_account', 'match_count', 'win_count', 'imp', 'first_match_date', 'last_match_date', 'last_match_region_id', 'ranks', 'leaderboard_ranks', 'badges', 'names', 'behavior_score', 'team', 'guild_member', 'activity', 'is_followed', 'simple_summary', 'performance', 'hero_performance', 'heroes_performance', 'matches', 'matches_group_by', 'dota_plus', 'hero_streaks', 'feats')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    identity = sgqlc.types.Field(CaptainJackIdentityPublicProfileType, graphql_name='identity')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    imp = sgqlc.types.Field(Int, graphql_name='imp')
    first_match_date = sgqlc.types.Field(Long, graphql_name='firstMatchDate')
    last_match_date = sgqlc.types.Field(Long, graphql_name='lastMatchDate')
    last_match_region_id = sgqlc.types.Field(Byte, graphql_name='lastMatchRegionId')
    ranks = sgqlc.types.Field(sgqlc.types.list_of('SteamAccountSeasonRankType'), graphql_name='ranks', args=sgqlc.types.ArgDict((
        ('season_rank_ids', sgqlc.types.Arg(sgqlc.types.list_of(Byte), graphql_name='seasonRankIds', default=None)),
))
    )
    leaderboard_ranks = sgqlc.types.Field(sgqlc.types.list_of('SteamAccountSeasonLeaderBoardRankType'), graphql_name='leaderboardRanks', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    badges = sgqlc.types.Field(sgqlc.types.list_of(PlayerBadgeType), graphql_name='badges')
    names = sgqlc.types.Field(sgqlc.types.list_of('SteamAccountNameType'), graphql_name='names', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    behavior_score = sgqlc.types.Field(Short, graphql_name='behaviorScore')
    team = sgqlc.types.Field('SteamAccountTeamMemberType', graphql_name='team')
    guild_member = sgqlc.types.Field(GuildMemberType, graphql_name='guildMember')
    activity = sgqlc.types.Field(PlayerActivitySummaryType, graphql_name='activity')
    is_followed = sgqlc.types.Field(Boolean, graphql_name='isFollowed')
    simple_summary = sgqlc.types.Field(PlayerCardHoverType, graphql_name='simpleSummary')
    performance = sgqlc.types.Field(PlayerPerformanceType, graphql_name='performance')
    hero_performance = sgqlc.types.Field(PlayerPerformanceType, graphql_name='heroPerformance', args=sgqlc.types.ArgDict((
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlayerHeroPerformanceMatchesRequestType), graphql_name='request', default=None)),
))
    )
    heroes_performance = sgqlc.types.Field(sgqlc.types.list_of(PlayerHeroesPerformanceType), graphql_name='heroesPerformance', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(PlayerHeroPerformanceMatchesRequestType, graphql_name='request', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    matches = sgqlc.types.Field(sgqlc.types.list_of(MatchType), graphql_name='matches', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlayerMatchesRequestType), graphql_name='request', default=None)),
))
    )
    matches_group_by = sgqlc.types.Field(sgqlc.types.list_of('MatchGroupByType'), graphql_name='matchesGroupBy', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlayerMatchesGroupByRequestType), graphql_name='request', default=None)),
))
    )
    dota_plus = sgqlc.types.Field(sgqlc.types.list_of(HeroDotaPlusLeaderboardRankType), graphql_name='dotaPlus')
    hero_streaks = sgqlc.types.Field(sgqlc.types.list_of(PlayerHeroPerformanceLongestStreakType), graphql_name='heroStreaks', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(PlayerMatchesRequestType, graphql_name='request', default=None)),
))
    )
    feats = sgqlc.types.Field(sgqlc.types.list_of(FeatType), graphql_name='feats', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )


class PlayerUpdateAttributeDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'agi', 'int', 'str')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    agi = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='agi')
    int = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='int')
    str = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='str')


class PlayerUpdateBattleDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'damage_min_max', 'damage_bonus', 'hp_regen', 'mp_regen')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    damage_min_max = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='damageMinMax')
    damage_bonus = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='damageBonus')
    hp_regen = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hpRegen')
    mp_regen = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mpRegen')


class PlayerUpdateGoldDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'gold', 'unreliable_gold', 'networth', 'networth_difference')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    gold = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='gold')
    unreliable_gold = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='unreliableGold')
    networth = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='networth')
    networth_difference = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='networthDifference')


class PlayerUpdateHealthDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'hp', 'max_hp', 'mp', 'max_mp')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    hp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='hp')
    max_hp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxHp')
    mp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='mp')
    max_mp = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='maxMp')


class PlayerUpdateLevelDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'level')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    level = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='level')


class PlayerUpdatePositionDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'x', 'y')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    x = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='x')
    y = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='y')


class PlusDraftPlayerHeroObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'pick_value', 'win_values', 'score', 'letter')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    pick_value = sgqlc.types.Field(Decimal, graphql_name='pickValue')
    win_values = sgqlc.types.Field(sgqlc.types.list_of(Decimal), graphql_name='winValues')
    score = sgqlc.types.Field(Float, graphql_name='score')
    letter = sgqlc.types.Field(PlusLetterType, graphql_name='letter')


class PlusDraftPlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('slot', 'position', 'position_values', 'heroes')
    slot = sgqlc.types.Field(Byte, graphql_name='slot')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    position_values = sgqlc.types.Field(sgqlc.types.list_of(Decimal), graphql_name='positionValues')
    heroes = sgqlc.types.Field(sgqlc.types.list_of(PlusDraftPlayerHeroObjectType), graphql_name='heroes')


class PlusDraftType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('mid_outcome', 'safe_outcome', 'off_outcome', 'win_values', 'duration_values', 'players')
    mid_outcome = sgqlc.types.Field(Decimal, graphql_name='midOutcome')
    safe_outcome = sgqlc.types.Field(Decimal, graphql_name='safeOutcome')
    off_outcome = sgqlc.types.Field(Decimal, graphql_name='offOutcome')
    win_values = sgqlc.types.Field(sgqlc.types.list_of(Decimal), graphql_name='winValues')
    duration_values = sgqlc.types.Field(sgqlc.types.list_of(Decimal), graphql_name='durationValues')
    players = sgqlc.types.Field(sgqlc.types.list_of(PlusDraftPlayerType), graphql_name='players')


class PlusHeroTeamStatusAveragesType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('cs', 'deaths', 'tower_damage', 'physical_damage', 'magical_damage', 'physical_damage_received', 'magical_damage_received', 'disable_count', 'disable_duration', 'stun_count', 'stun_duration', 'slow_count', 'slow_duration', 'healing_allies', 'purge_modifiers', 'weaken_count', 'weaken_duration', 'pure_damage_received', 'pure_damage')
    cs = sgqlc.types.Field(Decimal, graphql_name='cs')
    deaths = sgqlc.types.Field(Decimal, graphql_name='deaths')
    tower_damage = sgqlc.types.Field(Decimal, graphql_name='towerDamage')
    physical_damage = sgqlc.types.Field(Decimal, graphql_name='physicalDamage')
    magical_damage = sgqlc.types.Field(Decimal, graphql_name='magicalDamage')
    physical_damage_received = sgqlc.types.Field(Decimal, graphql_name='physicalDamageReceived')
    magical_damage_received = sgqlc.types.Field(Decimal, graphql_name='magicalDamageReceived')
    disable_count = sgqlc.types.Field(Decimal, graphql_name='disableCount')
    disable_duration = sgqlc.types.Field(Decimal, graphql_name='disableDuration')
    stun_count = sgqlc.types.Field(Decimal, graphql_name='stunCount')
    stun_duration = sgqlc.types.Field(Decimal, graphql_name='stunDuration')
    slow_count = sgqlc.types.Field(Decimal, graphql_name='slowCount')
    slow_duration = sgqlc.types.Field(Decimal, graphql_name='slowDuration')
    healing_allies = sgqlc.types.Field(Decimal, graphql_name='healingAllies')
    purge_modifiers = sgqlc.types.Field(Decimal, graphql_name='purgeModifiers')
    weaken_count = sgqlc.types.Field(Decimal, graphql_name='weakenCount')
    weaken_duration = sgqlc.types.Field(Decimal, graphql_name='weakenDuration')
    pure_damage_received = sgqlc.types.Field(Decimal, graphql_name='pureDamageReceived')
    pure_damage = sgqlc.types.Field(Decimal, graphql_name='pureDamage')


class PlusHeroTeamStatusDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'basic_bracket', 'position', 'averages')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    basic_bracket = sgqlc.types.Field(RankBracketBasicEnum, graphql_name='basicBracket')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    averages = sgqlc.types.Field(PlusHeroTeamStatusAveragesType, graphql_name='averages')


class PlusHoverBanType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'score', 'flags')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    score = sgqlc.types.Field(Decimal, graphql_name='score')
    flags = sgqlc.types.Field(Byte, graphql_name='flags')


class PlusHoverType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('players', 'bans')
    players = sgqlc.types.Field(sgqlc.types.list_of('PlusPlayerHoverType'), graphql_name='players')
    bans = sgqlc.types.Field(sgqlc.types.list_of(PlusHoverBanType), graphql_name='bans')


class PlusPlayerHoverHeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'win_count', 'loss_count')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    loss_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='lossCount')


class PlusPlayerHoverPlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'match_count', 'win_count', 'last_match_date_time')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')


class PlusPlayerHoverType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account', 'match_count', 'win_count', 'core_count', 'support_count', 'imp', 'heroes', 'activity', 'language_code', 'friends', 'enemies', 'last_match_date_time', 'heroes_experience', 'behavior_score')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')
    core_count = sgqlc.types.Field(Int, graphql_name='coreCount')
    support_count = sgqlc.types.Field(Int, graphql_name='supportCount')
    imp = sgqlc.types.Field(Int, graphql_name='imp')
    heroes = sgqlc.types.Field(sgqlc.types.list_of(PlusPlayerHoverHeroType), graphql_name='heroes')
    activity = sgqlc.types.Field(Byte, graphql_name='activity')
    language_code = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='languageCode')
    friends = sgqlc.types.Field(sgqlc.types.list_of(PlusPlayerHoverPlayerType), graphql_name='friends')
    enemies = sgqlc.types.Field(sgqlc.types.list_of(PlusPlayerHoverPlayerType), graphql_name='enemies')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    heroes_experience = sgqlc.types.Field(sgqlc.types.list_of(Short), graphql_name='heroesExperience')
    behavior_score = sgqlc.types.Field(Short, graphql_name='behaviorScore')


class PlusQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('draft', 'player_match_history', 'player_hero_highlight', 'team_hero_status', 'draft_missing_letter')
    draft = sgqlc.types.Field(PlusDraftType, graphql_name='draft', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlusDraftRequestType), graphql_name='request', default=None)),
))
    )
    player_match_history = sgqlc.types.Field(PlusHoverType, graphql_name='playerMatchHistory', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlusPlayerHoverRequestType), graphql_name='request', default=None)),
))
    )
    player_hero_highlight = sgqlc.types.Field(PlayerDraftHeroHighlightType, graphql_name='playerHeroHighlight', args=sgqlc.types.ArgDict((
        ('steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='steamAccountId', default=None)),
        ('hero_id', sgqlc.types.Arg(sgqlc.types.non_null(Short), graphql_name='heroId', default=None)),
))
    )
    team_hero_status = sgqlc.types.Field(sgqlc.types.list_of(PlusHeroTeamStatusDetailType), graphql_name='teamHeroStatus', args=sgqlc.types.ArgDict((
        ('rank_bracket', sgqlc.types.Arg(sgqlc.types.non_null(RankBracketBasicEnum), graphql_name='rankBracket', default=None)),
))
    )
    draft_missing_letter = sgqlc.types.Field(PlusLetterType, graphql_name='draftMissingLetter', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlusDraftMissingLetterRequestType), graphql_name='request', default=None)),
))
    )


class ProPlayerFollowType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'activity', 'steam_account')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    activity = sgqlc.types.Field(Int, graphql_name='activity')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')


class ProSteamAccountType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'real_name', 'fantasy_role', 'team_id', 'sponsor', 'is_locked', 'is_pro', 'total_earnings', 'birthday', 'romanized_real_name', 'roles', 'aliases', 'statuses', 'twitter_link', 'twitch_link', 'instagram_link', 'vk_link', 'you_tube_link', 'facebook_link', 'weibo_link', 'signature_heroes', 'position', 'countries', 'team')
    id = sgqlc.types.Field(Long, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    real_name = sgqlc.types.Field(String, graphql_name='realName')
    fantasy_role = sgqlc.types.Field(Byte, graphql_name='fantasyRole')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    sponsor = sgqlc.types.Field(String, graphql_name='sponsor')
    is_locked = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isLocked')
    is_pro = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isPro')
    total_earnings = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalEarnings')
    birthday = sgqlc.types.Field(Long, graphql_name='birthday')
    romanized_real_name = sgqlc.types.Field(String, graphql_name='romanizedRealName')
    roles = sgqlc.types.Field(Short, graphql_name='roles')
    aliases = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='aliases')
    statuses = sgqlc.types.Field(Byte, graphql_name='statuses')
    twitter_link = sgqlc.types.Field(String, graphql_name='twitterLink')
    twitch_link = sgqlc.types.Field(String, graphql_name='twitchLink')
    instagram_link = sgqlc.types.Field(String, graphql_name='instagramLink')
    vk_link = sgqlc.types.Field(String, graphql_name='vkLink')
    you_tube_link = sgqlc.types.Field(String, graphql_name='youTubeLink')
    facebook_link = sgqlc.types.Field(String, graphql_name='facebookLink')
    weibo_link = sgqlc.types.Field(String, graphql_name='weiboLink')
    signature_heroes = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='signatureHeroes')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    countries = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='countries')
    team = sgqlc.types.Field('TeamType', graphql_name='team')


class ROSHCaptainJackIdentityStatDifficultyType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('difficulty', 'match_count', 'win_count', 'max_score')
    difficulty = sgqlc.types.Field(ROSHDifficultyEnum, graphql_name='difficulty')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    max_score = sgqlc.types.Field(Float, graphql_name='maxScore')


class ROSHGlobalStatType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('difficulty', 'match_count', 'win_count', 'max_score')
    difficulty = sgqlc.types.Field(ROSHDifficultyEnum, graphql_name='difficulty')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    max_score = sgqlc.types.Field(Float, graphql_name='maxScore')


class ROSHMutation(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('create', 'update')
    create = sgqlc.types.Field(Long, graphql_name='create', args=sgqlc.types.ArgDict((
        ('difficulty', sgqlc.types.Arg(sgqlc.types.non_null(ROSHDifficultyEnum), graphql_name='difficulty', default=None)),
        ('bracket', sgqlc.types.Arg(sgqlc.types.non_null(RankBracket), graphql_name='bracket', default=None)),
        ('is_user_radiant', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isUserRadiant', default=None)),
        ('is_radiant_first_pick', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isRadiantFirstPick', default=None)),
))
    )
    update = sgqlc.types.Field(Boolean, graphql_name='update', args=sgqlc.types.ArgDict((
        ('match_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchId', default=None)),
        ('score', sgqlc.types.Arg(sgqlc.types.non_null(Float), graphql_name='score', default=None)),
        ('did_user_win', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='didUserWin', default=None)),
))
    )


class RabbitDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('last_updated', 'is_online', 'match_history', 'match_detail', 'match_detail_delay', 'match_stats', 'steam_account', 'match_live')
    last_updated = sgqlc.types.Field(Long, graphql_name='lastUpdated')
    is_online = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOnline')
    match_history = sgqlc.types.Field('RabbitQueueDetailType', graphql_name='matchHistory')
    match_detail = sgqlc.types.Field('RabbitQueueDetailType', graphql_name='matchDetail')
    match_detail_delay = sgqlc.types.Field('RabbitQueueDetailType', graphql_name='matchDetailDelay')
    match_stats = sgqlc.types.Field('RabbitQueueDetailType', graphql_name='matchStats')
    steam_account = sgqlc.types.Field('RabbitQueueDetailType', graphql_name='steamAccount')
    match_live = sgqlc.types.Field('RabbitQueueDetailType', graphql_name='matchLive')


class RabbitQueueDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('queue_count', 'queue_in_rate', 'queue_out_rate')
    queue_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='queueCount')
    queue_in_rate = sgqlc.types.Field(Decimal, graphql_name='queueInRate')
    queue_out_rate = sgqlc.types.Field(Decimal, graphql_name='queueOutRate')


class RegionType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'client_name', 'display_name', 'leaderboard_division', 'lang_key', 'latitude', 'longitude', 'code', 'match_group', 'weekend_tourney_division')
    id = sgqlc.types.Field(Byte, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    client_name = sgqlc.types.Field(String, graphql_name='clientName')
    display_name = sgqlc.types.Field(String, graphql_name='displayName')
    leaderboard_division = sgqlc.types.Field(String, graphql_name='leaderboardDivision')
    lang_key = sgqlc.types.Field(String, graphql_name='langKey')
    latitude = sgqlc.types.Field(Decimal, graphql_name='latitude')
    longitude = sgqlc.types.Field(Decimal, graphql_name='longitude')
    code = sgqlc.types.Field(String, graphql_name='code')
    match_group = sgqlc.types.Field(Byte, graphql_name='matchGroup')
    weekend_tourney_division = sgqlc.types.Field(String, graphql_name='weekendTourneyDivision')


class RoleType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('role_id', 'name', 'lang_key')
    role_id = sgqlc.types.Field(Short, graphql_name='roleId')
    name = sgqlc.types.Field(String, graphql_name='name')
    lang_key = sgqlc.types.Field(String, graphql_name='langKey')


class RoshQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('stats',)
    stats = sgqlc.types.Field(sgqlc.types.list_of(ROSHGlobalStatType), graphql_name='stats', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(ROSHMatchesRequestType, graphql_name='request', default=None)),
))
    )


class SearchType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('players', 'matches', 'leagues', 'teams', 'pro_players', 'casters', 'guild', 'dire_tide_matches')
    players = sgqlc.types.Field(sgqlc.types.list_of('SteamAccountType'), graphql_name='players')
    matches = sgqlc.types.Field(sgqlc.types.list_of(MatchType), graphql_name='matches')
    leagues = sgqlc.types.Field(sgqlc.types.list_of(LeagueType), graphql_name='leagues')
    teams = sgqlc.types.Field(sgqlc.types.list_of('TeamType'), graphql_name='teams')
    pro_players = sgqlc.types.Field(sgqlc.types.list_of('SteamAccountType'), graphql_name='proPlayers')
    casters = sgqlc.types.Field(sgqlc.types.list_of('SteamAccountType'), graphql_name='casters')
    guild = sgqlc.types.Field(GuildType, graphql_name='guild')
    dire_tide_matches = sgqlc.types.Field(sgqlc.types.list_of(DireTideCustomGameMatchType), graphql_name='direTideMatches')


class SeriesType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'type', 'team_one_id', 'team_two_id', 'league_id', 'team_one_win_count', 'team_two_win_count', 'winning_team_id', 'last_match_date_time', 'matches', 'team_one', 'team_two', 'league', 'node')
    id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='id')
    type = sgqlc.types.Field(SeriesEnum, graphql_name='type')
    team_one_id = sgqlc.types.Field(Int, graphql_name='teamOneId')
    team_two_id = sgqlc.types.Field(Int, graphql_name='teamTwoId')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    team_one_win_count = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='teamOneWinCount')
    team_two_win_count = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='teamTwoWinCount')
    winning_team_id = sgqlc.types.Field(Int, graphql_name='winningTeamId')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    matches = sgqlc.types.Field(sgqlc.types.list_of(MatchType), graphql_name='matches')
    team_one = sgqlc.types.Field('TeamType', graphql_name='teamOne')
    team_two = sgqlc.types.Field('TeamType', graphql_name='teamTwo')
    league = sgqlc.types.Field(LeagueType, graphql_name='league')
    node = sgqlc.types.Field(LeagueNodeType, graphql_name='node')


class ServerStatusType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_redis_online', 'steam_api_detail', 'rabbit_detail')
    is_redis_online = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isRedisOnline')
    steam_api_detail = sgqlc.types.Field('SteamApiDetailType', graphql_name='steamApiDetail')
    rabbit_detail = sgqlc.types.Field(RabbitDetailType, graphql_name='rabbitDetail')


class SpiritBearInventoryObjectType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('item_id',)
    item_id = sgqlc.types.Field(Short, graphql_name='itemId')


class SpiritBearInventoryType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'back_pack0', 'back_pack1', 'back_pack2', 'teleport0', 'neutral0')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    item0 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='item0')
    item1 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='item1')
    item2 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='item2')
    item3 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='item3')
    item4 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='item4')
    item5 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='item5')
    back_pack0 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='backPack0')
    back_pack1 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='backPack1')
    back_pack2 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='backPack2')
    teleport0 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='teleport0')
    neutral0 = sgqlc.types.Field(SpiritBearInventoryObjectType, graphql_name='neutral0')


class SteamAccountBattlePassType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'event_id', 'level')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    event_id = sgqlc.types.Field(Byte, graphql_name='eventId')
    level = sgqlc.types.Field(Int, graphql_name='level')


class SteamAccountByRankType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('rank', 'player_count')
    rank = sgqlc.types.Field(sgqlc.types.non_null(Short), graphql_name='rank')
    player_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='playerCount')


class SteamAccountNameType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('name', 'last_seen_date_time')
    name = sgqlc.types.Field(String, graphql_name='name')
    last_seen_date_time = sgqlc.types.Field(Long, graphql_name='lastSeenDateTime')


class SteamAccountSeasonActiveLeaderboardCountryDataType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('country_code', 'player_count')
    country_code = sgqlc.types.Field(String, graphql_name='countryCode')
    player_count = sgqlc.types.Field(Int, graphql_name='playerCount')


class SteamAccountSeasonActiveLeaderboardPositionDataType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('position', 'player_count')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    player_count = sgqlc.types.Field(Int, graphql_name='playerCount')


class SteamAccountSeasonActiveLeaderboardRankType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'avg_imp', 'division_id', 'last_update_date_time', 'match_count', 'position', 'position_value', 'rank', 'rank_shift', 'top_hero_one', 'top_hero_two', 'top_hero_three', 'win_rate')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    avg_imp = sgqlc.types.Field(Short, graphql_name='avgImp')
    division_id = sgqlc.types.Field(LeaderboardDivision, graphql_name='divisionId')
    last_update_date_time = sgqlc.types.Field(Long, graphql_name='lastUpdateDateTime')
    match_count = sgqlc.types.Field(Short, graphql_name='matchCount')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    position_value = sgqlc.types.Field(Byte, graphql_name='positionValue')
    rank = sgqlc.types.Field(Short, graphql_name='rank')
    rank_shift = sgqlc.types.Field(Short, graphql_name='rankShift')
    top_hero_one = sgqlc.types.Field(Short, graphql_name='topHeroOne')
    top_hero_two = sgqlc.types.Field(Short, graphql_name='topHeroTwo')
    top_hero_three = sgqlc.types.Field(Short, graphql_name='topHeroThree')
    win_rate = sgqlc.types.Field(Byte, graphql_name='winRate')


class SteamAccountSeasonActiveLeaderboardType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('player_count', 'players', 'country_data', 'position_data', 'team_data', 'team_id_data')
    player_count = sgqlc.types.Field(Int, graphql_name='playerCount')
    players = sgqlc.types.Field(sgqlc.types.list_of(SteamAccountSeasonActiveLeaderboardRankType), graphql_name='players', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Long, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Long, graphql_name='take', default=None)),
))
    )
    country_data = sgqlc.types.Field(sgqlc.types.list_of(SteamAccountSeasonActiveLeaderboardCountryDataType), graphql_name='countryData')
    position_data = sgqlc.types.Field(sgqlc.types.list_of(SteamAccountSeasonActiveLeaderboardPositionDataType), graphql_name='positionData')
    team_data = sgqlc.types.Field(sgqlc.types.list_of('TeamType'), graphql_name='teamData')
    team_id_data = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='teamIdData')


class SteamAccountSeasonLeaderBoardRankType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'season_rank_id', 'as_of_date_time', 'season_leader_board_division_id', 'rank')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    season_rank_id = sgqlc.types.Field(Byte, graphql_name='seasonRankId')
    as_of_date_time = sgqlc.types.Field(Long, graphql_name='asOfDateTime')
    season_leader_board_division_id = sgqlc.types.Field(LeaderboardDivision, graphql_name='seasonLeaderBoardDivisionId')
    rank = sgqlc.types.Field(Short, graphql_name='rank')


class SteamAccountSeasonRankType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('season_rank_id', 'as_of_date_time', 'is_core', 'rank')
    season_rank_id = sgqlc.types.Field(Byte, graphql_name='seasonRankId')
    as_of_date_time = sgqlc.types.Field(Long, graphql_name='asOfDateTime')
    is_core = sgqlc.types.Field(Boolean, graphql_name='isCore')
    rank = sgqlc.types.Field(Byte, graphql_name='rank')


class SteamAccountTeamMemberType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'steam_account', 'player', 'team_id', 'first_match_id', 'first_match_date_time', 'last_match_id', 'last_match_date_time', 'team')
    steam_account_id = sgqlc.types.Field(sgqlc.types.non_null(Long), graphql_name='steamAccountId')
    steam_account = sgqlc.types.Field('SteamAccountType', graphql_name='steamAccount')
    player = sgqlc.types.Field(PlayerType, graphql_name='player')
    team_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='teamId')
    first_match_id = sgqlc.types.Field(Long, graphql_name='firstMatchId')
    first_match_date_time = sgqlc.types.Field(Long, graphql_name='firstMatchDateTime')
    last_match_id = sgqlc.types.Field(Long, graphql_name='lastMatchId')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    team = sgqlc.types.Field('TeamType', graphql_name='team')


class SteamAccountType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'profile_uri', 'real_name', 'time_created', 'country_code', 'state_code', 'city_id', 'community_visible_state', 'name', 'last_log_off', 'avatar', 'primary_clan_id', 'is_dota_plus_subscriber', 'dota_account_level', 'rank_shift', 'is_anonymous', 'is_stratz_public', 'season_rank', 'season_leaderboard_rank', 'season_leaderboard_division_id', 'pro_steam_account', 'activity', 'smurf_flag', 'last_match_date_time', 'last_match_region_id', 'battlepass', 'guild', 'is_caster')
    id = sgqlc.types.Field(Long, graphql_name='id')
    profile_uri = sgqlc.types.Field(String, graphql_name='profileUri')
    real_name = sgqlc.types.Field(String, graphql_name='realName')
    time_created = sgqlc.types.Field(Long, graphql_name='timeCreated')
    country_code = sgqlc.types.Field(String, graphql_name='countryCode')
    state_code = sgqlc.types.Field(String, graphql_name='stateCode')
    city_id = sgqlc.types.Field(Int, graphql_name='cityId')
    community_visible_state = sgqlc.types.Field(Int, graphql_name='communityVisibleState')
    name = sgqlc.types.Field(String, graphql_name='name')
    last_log_off = sgqlc.types.Field(Long, graphql_name='lastLogOff')
    avatar = sgqlc.types.Field(String, graphql_name='avatar')
    primary_clan_id = sgqlc.types.Field(Long, graphql_name='primaryClanId')
    is_dota_plus_subscriber = sgqlc.types.Field(Boolean, graphql_name='isDotaPlusSubscriber')
    dota_account_level = sgqlc.types.Field(Short, graphql_name='dotaAccountLevel')
    rank_shift = sgqlc.types.Field(Short, graphql_name='rankShift')
    is_anonymous = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isAnonymous')
    is_stratz_public = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isStratzPublic')
    season_rank = sgqlc.types.Field(Byte, graphql_name='seasonRank')
    season_leaderboard_rank = sgqlc.types.Field(Short, graphql_name='seasonLeaderboardRank')
    season_leaderboard_division_id = sgqlc.types.Field(Byte, graphql_name='seasonLeaderboardDivisionId')
    pro_steam_account = sgqlc.types.Field(ProSteamAccountType, graphql_name='proSteamAccount')
    activity = sgqlc.types.Field(PlayerActivitySummaryType, graphql_name='activity')
    smurf_flag = sgqlc.types.Field(Byte, graphql_name='smurfFlag')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    last_match_region_id = sgqlc.types.Field(Byte, graphql_name='lastMatchRegionId')
    battlepass = sgqlc.types.Field(sgqlc.types.list_of(SteamAccountBattlePassType), graphql_name='battlepass')
    guild = sgqlc.types.Field(GuildMemberType, graphql_name='guild')
    is_caster = sgqlc.types.Field(Boolean, graphql_name='isCaster')


class SteamApiDetailOutageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('seconds_offline', 'date_time')
    seconds_offline = sgqlc.types.Field(Int, graphql_name='secondsOffline')
    date_time = sgqlc.types.Field(Long, graphql_name='dateTime')


class SteamApiDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('is_online', 'outages')
    is_online = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isOnline')
    outages = sgqlc.types.Field(sgqlc.types.list_of(SteamApiDetailOutageType), graphql_name='outages')


class StratzQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('admin', 'user', 'page', 'blogs', 'news', 'ticker', 'status', 'languages', 'match_retry', 'search')
    admin = sgqlc.types.Field(AdminQuery, graphql_name='admin')
    user = sgqlc.types.Field('UserQuery', graphql_name='user')
    page = sgqlc.types.Field(PageQuery, graphql_name='page')
    blogs = sgqlc.types.Field(sgqlc.types.list_of(BlogType), graphql_name='blogs', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    news = sgqlc.types.Field(sgqlc.types.list_of(NewsItemType), graphql_name='news')
    ticker = sgqlc.types.Field(sgqlc.types.list_of(Int), graphql_name='ticker')
    status = sgqlc.types.Field(ServerStatusType, graphql_name='status')
    languages = sgqlc.types.Field(sgqlc.types.list_of(LanguageType), graphql_name='languages')
    match_retry = sgqlc.types.Field(Boolean, graphql_name='matchRetry', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='id', default=None)),
))
    )
    search = sgqlc.types.Field(SearchType, graphql_name='search', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(FilterSearchRequestType, graphql_name='request', default=None)),
))
    )


class StreakEventType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'hero_id', 'type', 'value')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    type = sgqlc.types.Field(Streak, graphql_name='type')
    value = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='value')


class TI2020CustomGameRoomModifierType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('difficulty', 'modifier_id', 'match_count', 'win_count', 'death_count', 'elite_match_count', 'elite_win_count', 'elite_death_count')
    difficulty = sgqlc.types.Field(AghanimLabMatchDifficultyEnum, graphql_name='difficulty')
    modifier_id = sgqlc.types.Field(Short, graphql_name='modifierId')
    match_count = sgqlc.types.Field(Int, graphql_name='matchCount')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    death_count = sgqlc.types.Field(Int, graphql_name='deathCount')
    elite_match_count = sgqlc.types.Field(Int, graphql_name='eliteMatchCount')
    elite_win_count = sgqlc.types.Field(Int, graphql_name='eliteWinCount')
    elite_death_count = sgqlc.types.Field(Int, graphql_name='eliteDeathCount')


class TeamPrizeType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('league_id', 'league', 'team_id', 'team', 'standing', 'prize_amount')
    league_id = sgqlc.types.Field(Int, graphql_name='leagueId')
    league = sgqlc.types.Field(LeagueType, graphql_name='league')
    team_id = sgqlc.types.Field(Int, graphql_name='teamId')
    team = sgqlc.types.Field('TeamType', graphql_name='team')
    standing = sgqlc.types.Field(Int, graphql_name='standing')
    prize_amount = sgqlc.types.Field(Float, graphql_name='prizeAmount')


class TeamType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('id', 'name', 'tag', 'date_created', 'is_pro', 'is_locked', 'country_code', 'url', 'logo', 'base_logo', 'banner_logo', 'win_count', 'loss_count', 'last_match_date_time', 'country_name', 'coach_steam_account_id', 'coach_steam_account', 'matches', 'series', 'members', 'matches_group_by', 'hero_pick_ban', 'leagues')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    tag = sgqlc.types.Field(String, graphql_name='tag')
    date_created = sgqlc.types.Field(Long, graphql_name='dateCreated')
    is_pro = sgqlc.types.Field(Boolean, graphql_name='isPro')
    is_locked = sgqlc.types.Field(Boolean, graphql_name='isLocked')
    country_code = sgqlc.types.Field(String, graphql_name='countryCode')
    url = sgqlc.types.Field(String, graphql_name='url')
    logo = sgqlc.types.Field(String, graphql_name='logo')
    base_logo = sgqlc.types.Field(String, graphql_name='baseLogo')
    banner_logo = sgqlc.types.Field(String, graphql_name='bannerLogo')
    win_count = sgqlc.types.Field(Int, graphql_name='winCount')
    loss_count = sgqlc.types.Field(Int, graphql_name='lossCount')
    last_match_date_time = sgqlc.types.Field(Long, graphql_name='lastMatchDateTime')
    country_name = sgqlc.types.Field(String, graphql_name='countryName')
    coach_steam_account_id = sgqlc.types.Field(Long, graphql_name='coachSteamAccountId')
    coach_steam_account = sgqlc.types.Field(SteamAccountType, graphql_name='coachSteamAccount')
    matches = sgqlc.types.Field(sgqlc.types.list_of(MatchType), graphql_name='matches', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(TeamMatchesRequestType), graphql_name='request', default=None)),
))
    )
    series = sgqlc.types.Field(sgqlc.types.list_of(SeriesType), graphql_name='series', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(FilterSeriesRequestType), graphql_name='request', default=None)),
))
    )
    members = sgqlc.types.Field(sgqlc.types.list_of(SteamAccountTeamMemberType), graphql_name='members', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    matches_group_by = sgqlc.types.Field(sgqlc.types.list_of('MatchGroupByType'), graphql_name='matchesGroupBy', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(PlayerMatchesGroupByRequestType), graphql_name='request', default=None)),
))
    )
    hero_pick_ban = sgqlc.types.Field(sgqlc.types.list_of(MatchPickBanGroupByType), graphql_name='heroPickBan', args=sgqlc.types.ArgDict((
        ('request', sgqlc.types.Arg(sgqlc.types.non_null(HeroPickBanRequestType), graphql_name='request', default=None)),
))
    )
    leagues = sgqlc.types.Field(sgqlc.types.list_of(LeagueType), graphql_name='leagues')


class TopPlayersByHeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'players')
    hero_id = sgqlc.types.Field(Short, graphql_name='heroId')
    players = sgqlc.types.Field(sgqlc.types.list_of(PlayerLeaderBoardByHeroType), graphql_name='players')


class TotalMatchCountType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_count',)
    match_count = sgqlc.types.Field(Long, graphql_name='matchCount')


class TotalPlayerCountType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('player_count',)
    player_count = sgqlc.types.Field(Long, graphql_name='playerCount')


class TowerDamageDetailType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('time', 'attacker', 'npc_id', 'damage', 'by_ability', 'by_item', 'from_npc')
    time = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='time')
    attacker = sgqlc.types.Field(Short, graphql_name='attacker')
    npc_id = sgqlc.types.Field(Short, graphql_name='npcId')
    damage = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='damage')
    by_ability = sgqlc.types.Field(Short, graphql_name='byAbility')
    by_item = sgqlc.types.Field(Short, graphql_name='byItem')
    from_npc = sgqlc.types.Field(Short, graphql_name='fromNpc')


class TwitchTrackerPlayerHeroType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('hero_id', 'match_count', 'win_count')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    match_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCount')
    win_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCount')


class TwitchTrackerPlayerMatchType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('match_id', 'hero_id', 'lane', 'role', 'position', 'kill_count', 'death_count', 'assist_count', 'end_date_time', 'is_victory', 'award')
    match_id = sgqlc.types.Field(Long, graphql_name='matchId')
    hero_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='heroId')
    lane = sgqlc.types.Field(MatchLaneType, graphql_name='lane')
    role = sgqlc.types.Field(MatchPlayerRoleType, graphql_name='role')
    position = sgqlc.types.Field(MatchPlayerPositionType, graphql_name='position')
    kill_count = sgqlc.types.Field(Short, graphql_name='killCount')
    death_count = sgqlc.types.Field(Short, graphql_name='deathCount')
    assist_count = sgqlc.types.Field(Short, graphql_name='assistCount')
    end_date_time = sgqlc.types.Field(Long, graphql_name='endDateTime')
    is_victory = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='isVictory')
    award = sgqlc.types.Field(Byte, graphql_name='award')


class TwitchTrackerPlayerType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('steam_account_id', 'activity', 'name', 'avatar', 'rank', 'leaderboard_rank', 'pro_player_name', 'match_count_last100', 'win_count_last100', 'unique_hero_last100', 'core_count_last100', 'top_hero_last100', 'matches')
    steam_account_id = sgqlc.types.Field(Long, graphql_name='steamAccountId')
    activity = sgqlc.types.Field(PlayerBehaviorActivity, graphql_name='activity')
    name = sgqlc.types.Field(String, graphql_name='name')
    avatar = sgqlc.types.Field(String, graphql_name='avatar')
    rank = sgqlc.types.Field(Int, graphql_name='rank')
    leaderboard_rank = sgqlc.types.Field(Int, graphql_name='leaderboardRank')
    pro_player_name = sgqlc.types.Field(String, graphql_name='proPlayerName')
    match_count_last100 = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='matchCountLast100')
    win_count_last100 = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='winCountLast100')
    unique_hero_last100 = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='uniqueHeroLast100')
    core_count_last100 = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='coreCountLast100')
    top_hero_last100 = sgqlc.types.Field(sgqlc.types.list_of(TwitchTrackerPlayerHeroType), graphql_name='topHeroLast100')
    matches = sgqlc.types.Field(sgqlc.types.list_of(TwitchTrackerPlayerMatchType), graphql_name='matches')


class UserHomepageType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('blogs', 'upcoming_leagues', 'in_progress_leagues', 'league_metas', 'top_pro_players', 'top_players_by_hero_type', 'top_synergies_by_hero', 'match_awards', 'recent_rampages', 'recent_win_streaks', 'recent_high_imps', 'recent_matches', 'active_league_games', 'top_live_games', 'total_components')
    blogs = sgqlc.types.Field(sgqlc.types.list_of(BlogType), graphql_name='blogs', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('excluded_blog_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='excludedBlogIds', default=None)),
))
    )
    upcoming_leagues = sgqlc.types.Field(sgqlc.types.list_of(LeagueType), graphql_name='upcomingLeagues', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('excluded_league_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='excludedLeagueIds', default=None)),
        ('included_league_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='includedLeagueIds', default=None)),
        ('included_league_tier_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='includedLeagueTierIds', default=None)),
))
    )
    in_progress_leagues = sgqlc.types.Field(sgqlc.types.list_of(LeagueType), graphql_name='inProgressLeagues', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('excluded_league_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='excludedLeagueIds', default=None)),
        ('included_league_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='includedLeagueIds', default=None)),
        ('included_league_tier_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='includedLeagueTierIds', default=None)),
))
    )
    league_metas = sgqlc.types.Field(sgqlc.types.list_of(LeagueMetaType), graphql_name='leagueMetas', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('excluded_league_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='excludedLeagueIds', default=None)),
        ('included_league_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='includedLeagueIds', default=None)),
        ('included_league_tier_ids', sgqlc.types.Arg(sgqlc.types.list_of(Int), graphql_name='includedLeagueTierIds', default=None)),
))
    )
    top_pro_players = sgqlc.types.Field(sgqlc.types.list_of(ProPlayerFollowType), graphql_name='topProPlayers', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    top_players_by_hero_type = sgqlc.types.Field(sgqlc.types.list_of(TopPlayersByHeroType), graphql_name='topPlayersByHeroType', args=sgqlc.types.ArgDict((
        ('hero_components_take', sgqlc.types.Arg(Int, graphql_name='heroComponentsTake', default=None)),
        ('players_take', sgqlc.types.Arg(Int, graphql_name='playersTake', default=None)),
        ('hero_ids', sgqlc.types.Arg(Int, graphql_name='heroIds', default=None)),
        ('rank_bracket_ids', sgqlc.types.Arg(Int, graphql_name='rankBracketIds', default=None)),
))
    )
    top_synergies_by_hero = sgqlc.types.Field(sgqlc.types.list_of(HomepageHeroSynergyType), graphql_name='topSynergiesByHero', args=sgqlc.types.ArgDict((
        ('synergy_components_take', sgqlc.types.Arg(Int, graphql_name='synergyComponentsTake', default=None)),
        ('hero_ids', sgqlc.types.Arg(Int, graphql_name='heroIds', default=None)),
))
    )
    match_awards = sgqlc.types.Field(sgqlc.types.list_of(HomepageHeroSynergyType), graphql_name='matchAwards', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('match_player_award_type_ids', sgqlc.types.Arg(sgqlc.types.list_of(Byte), graphql_name='matchPlayerAwardTypeIds', default=None)),
))
    )
    recent_rampages = sgqlc.types.Field(sgqlc.types.list_of(HomepageHeroSynergyType), graphql_name='recentRampages', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    recent_win_streaks = sgqlc.types.Field(sgqlc.types.list_of(HomepageHeroSynergyType), graphql_name='recentWinStreaks', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    recent_high_imps = sgqlc.types.Field(sgqlc.types.list_of(HomepageHeroSynergyType), graphql_name='recentHighImps', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    recent_matches = sgqlc.types.Field(sgqlc.types.list_of(HomepageHeroSynergyType), graphql_name='recentMatches', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    active_league_games = sgqlc.types.Field(sgqlc.types.list_of(HomepageHeroSynergyType), graphql_name='activeLeagueGames', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    top_live_games = sgqlc.types.Field(sgqlc.types.list_of(HomepageHeroSynergyType), graphql_name='topLiveGames', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
))
    )
    total_components = sgqlc.types.Field(Int, graphql_name='totalComponents')


class UserQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('profile', 'homepage', 'followers', 'following', 'feed', 'ip_geo_lookup')
    profile = sgqlc.types.Field('UserType', graphql_name='profile')
    homepage = sgqlc.types.Field(UserHomepageType, graphql_name='homepage', args=sgqlc.types.ArgDict((
        ('take', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='take', default=None)),
))
    )
    followers = sgqlc.types.Field(sgqlc.types.list_of(FollowerType), graphql_name='followers')
    following = sgqlc.types.Field(sgqlc.types.list_of(FollowerType), graphql_name='following')
    feed = sgqlc.types.Field(FeedResponseType, graphql_name='feed', args=sgqlc.types.ArgDict((
        ('skip', sgqlc.types.Arg(Int, graphql_name='skip', default=None)),
        ('take', sgqlc.types.Arg(Int, graphql_name='take', default=None)),
))
    )
    ip_geo_lookup = sgqlc.types.Field(IpGeoLookupType, graphql_name='ipGeoLookup')


class UserType(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('profile', 'steam_account', 'recent_match', 'following_count', 'follower_count', 'following_league_count', 'following_team_count', 'stratz_api_applications')
    profile = sgqlc.types.Field(CaptainJackIdentityPrivateProfileType, graphql_name='profile')
    steam_account = sgqlc.types.Field(SteamAccountType, graphql_name='steamAccount')
    recent_match = sgqlc.types.Field(MatchType, graphql_name='recentMatch')
    following_count = sgqlc.types.Field(Int, graphql_name='followingCount')
    follower_count = sgqlc.types.Field(Int, graphql_name='followerCount')
    following_league_count = sgqlc.types.Field(Int, graphql_name='followingLeagueCount')
    following_team_count = sgqlc.types.Field(Int, graphql_name='followingTeamCount')
    stratz_api_applications = sgqlc.types.Field(sgqlc.types.list_of(CaptainJackIdentityApiApplicationType), graphql_name='stratzApiApplications')


class VendorQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('dota_next', 'twitch_tracker')
    dota_next = sgqlc.types.Field(DotaNextQuery, graphql_name='dotaNext')
    twitch_tracker = sgqlc.types.Field(TwitchTrackerPlayerType, graphql_name='twitchTracker', args=sgqlc.types.ArgDict((
        ('steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='steamAccountId', default=None)),
))
    )


class YogurtMutation(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('create_team', 'update_team', 'add_team_member', 'update_team_member', 'set_team_member_default_team', 'remove_team_member', 'update', 'validate', 'invalidate', 'delete', 'link_series_id', 'remove_series_id', 'import_match', 'import_pick_bans')
    create_team = sgqlc.types.Field(MatchReplayUploadTeamType, graphql_name='createTeam', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='matchReplayUploadTeamName', default=None)),
        ('email_address', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='emailAddress', default=None)),
        ('team_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='teamId', default=None)),
))
    )
    update_team = sgqlc.types.Field(Boolean, graphql_name='updateTeam', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('match_replay_upload_team_name', sgqlc.types.Arg(String, graphql_name='matchReplayUploadTeamName', default=None)),
        ('team_id', sgqlc.types.Arg(Int, graphql_name='teamId', default=None)),
))
    )
    add_team_member = sgqlc.types.Field(Boolean, graphql_name='addTeamMember', args=sgqlc.types.ArgDict((
        ('steam_account_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='steamAccountId', default=None)),
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
))
    )
    update_team_member = sgqlc.types.Field(Boolean, graphql_name='updateTeamMember', args=sgqlc.types.ArgDict((
        ('captain_jack_identity_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='captainJackIdentityId', default=None)),
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('is_admin', sgqlc.types.Arg(sgqlc.types.non_null(Boolean), graphql_name='isAdmin', default=None)),
))
    )
    set_team_member_default_team = sgqlc.types.Field(Boolean, graphql_name='setTeamMemberDefaultTeam', args=sgqlc.types.ArgDict((
        ('captain_jack_identity_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='captainJackIdentityId', default=None)),
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
))
    )
    remove_team_member = sgqlc.types.Field(Boolean, graphql_name='removeTeamMember', args=sgqlc.types.ArgDict((
        ('captain_jack_identity_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='captainJackIdentityId', default=None)),
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
))
    )
    update = sgqlc.types.Field(Boolean, graphql_name='update', args=sgqlc.types.ArgDict((
        ('update_match_replay_upload_object', sgqlc.types.Arg(sgqlc.types.non_null(UpdateMatchReplayUploadObjectType), graphql_name='updateMatchReplayUploadObject', default=None)),
))
    )
    validate = sgqlc.types.Field(Boolean, graphql_name='validate', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('match_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchId', default=None)),
))
    )
    invalidate = sgqlc.types.Field(Boolean, graphql_name='invalidate', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('match_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchId', default=None)),
))
    )
    delete = sgqlc.types.Field(Boolean, graphql_name='delete', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('match_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchId', default=None)),
))
    )
    link_series_id = sgqlc.types.Field(Boolean, graphql_name='linkSeriesId', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('match_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Long)), graphql_name='matchIds', default=None)),
))
    )
    remove_series_id = sgqlc.types.Field(Boolean, graphql_name='removeSeriesId', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('match_ids', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(Long)), graphql_name='matchIds', default=None)),
))
    )
    import_match = sgqlc.types.Field(Boolean, graphql_name='importMatch', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('match_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchId', default=None)),
))
    )
    import_pick_bans = sgqlc.types.Field(Boolean, graphql_name='importPickBans', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('match_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchId', default=None)),
        ('pick_bans', sgqlc.types.Arg(sgqlc.types.non_null(sgqlc.types.list_of(ImportPickBanType)), graphql_name='pickBans', default=None)),
))
    )


class YogurtQuery(sgqlc.types.Type):
    __schema__ = stratz_schema_python
    __field_names__ = ('team', 'teams', 'default_team', 'team_members', 'overview', 'hero_summary')
    team = sgqlc.types.Field(MatchReplayUploadTeamType, graphql_name='team', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
))
    )
    teams = sgqlc.types.Field(sgqlc.types.list_of(MatchReplayUploadTeamType), graphql_name='teams')
    default_team = sgqlc.types.Field(MatchReplayUploadTeamType, graphql_name='defaultTeam')
    team_members = sgqlc.types.Field(sgqlc.types.list_of(MatchReplayUploadTeamMemberType), graphql_name='teamMembers', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
))
    )
    overview = sgqlc.types.Field(MatchReplayUploadOverviewType, graphql_name='overview', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('request', sgqlc.types.Arg(FilterMatchReplayUploadRequestType, graphql_name='request', default=None)),
))
    )
    hero_summary = sgqlc.types.Field(sgqlc.types.list_of(MatchReplayUploadHeroSummaryType), graphql_name='heroSummary', args=sgqlc.types.ArgDict((
        ('match_replay_upload_team_id', sgqlc.types.Arg(sgqlc.types.non_null(Long), graphql_name='matchReplayUploadTeamId', default=None)),
        ('request', sgqlc.types.Arg(FilterMatchReplayUploadRequestType, graphql_name='request', default=None)),
))
    )



########################################################################
# Unions
########################################################################
class LiveEventType(sgqlc.types.Union):
    __schema__ = stratz_schema_python
    __types__ = (LiveEventPlayerRampageType, LiveEventPlayerWinStreakType, LiveEventPlayerHeroWinStreakType, LiveEventPlayerHeroKillsType, LiveEventPlayerHeroAssistsType, LiveEventPlayerHeroBuildingDamageType, LiveEventPlayerHeroHealingType, LiveEventPlayerHeroHeroDamageType, LiveEventPlayerHeroGoldPerMinuteType, LiveEventPlayerHeroExpPerMinuteType, LiveEventPlayerHeroHighImpType, LiveEventPlayerHeroDotaPlusLevelType, LiveEventPlayerRankUpType, LiveEventProPlayerLiveType, LiveEventPlayerHeroItemPurchaseType, LiveEventPlayerHeroDewardType, LiveEventMatchDireTideStompType, LiveEventPlayerDireTideCandyScoredType)


class MatchGroupByType(sgqlc.types.Union):
    __schema__ = stratz_schema_python
    __types__ = (MatchGroupByHeroType, MatchGroupByFactionType, MatchGroupByKillsType, MatchGroupByDeathsType, MatchGroupByAssistsType, MatchGroupByIsLeaverType, MatchGroupByLevelType, MatchGroupByIsPartyType, MatchGroupByIsRandomType, MatchGroupByLaneType, MatchGroupByRoleType, MatchGroupByIsIntentionalFeedingType, MatchGroupByAwardType, MatchGroupByRoamLaneType, MatchGroupByIsVictoryType, MatchGroupByDurationMinutesType, MatchGroupByClusterType, MatchGroupByRegionType, MatchGroupByLobbyTypeType, MatchGroupByIsLeagueType, MatchGroupByIsSeriesType, MatchGroupByGameModeType, MatchGroupByIsStatsType, MatchGroupByGameVersionType, MatchGroupByTeamType, MatchGroupByHeroPerformanceType, MatchGroupBySteamAccountIdType, MatchGroupBySteamAccountIdHeroIdType, MatchGroupBySteamAccountIdWithTeamType, MatchGroupBySteamAccountIdHeroIdWithTeamType, MatchGroupBySteamAccountIdAgainstTeamType, MatchGroupBySteamAccountIdHeroIdAgainstTeamType, MatchGroupByLeagueIdType, MatchGroupByPositionType, MatchGroupByDateDayType, MatchGroupByDateDayHeroType, MatchGroupByTotalKillsType, MatchGroupByGoldPerMinuteType, MatchGroupByHourType)



########################################################################
# Schema Entry Points
########################################################################
stratz_schema_python.query_type = DotaQuery
stratz_schema_python.mutation_type = DotaMutation
stratz_schema_python.subscription_type = DotaSubscription

