best_rpg_games = [
    "Final Fantasy XV",
    "Yakuza 0",
    "Chrono Trigger",
]

best_adventure_games = [
    "The Legend of Zelda: Breath of the Wild",
    "The Witcher 3",
]

import json

games = {
    "rpg": best_rpg_games,
    "adventure": best_adventure_games,
}

print(json.dumps(games, indent=4))
