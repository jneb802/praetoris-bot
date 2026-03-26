"""Wiki section content — edit this file to update wiki text."""

ICON_URL = "https://gcdn.thunderstore.io/live/repository/icons/warpalicious-Praetoris-5.6.0.png"
MODPACK_URL = "https://thunderstore.io/c/valheim/p/warpalicious/Praetoris/"
ENFORCER_URL = "https://thunderstore.io/c/valheim/p/MidnightMods/ValheimEnforcer/"
VBNET_URL = "https://thunderstore.io/c/valheim/p/VitByr/VBNetTweaks/"

# ── Main embed (always visible) ──

WIKI_DESCRIPTION = (
    "*Season 5 \u2014 Hardcore exploration modpack by warpalicious*\n\n"
    "Welcome to Praetoris, a curated Valheim server focused on "
    "challenging combat, no-portal exploration, and meaningful "
    "progression. The world is harder, the loot is better, and "
    "every expedition matters.\n\n"
    "Use the buttons and menus below to explore server info, "
    "mod configs, and gameplay guides."
)

WIKI_FIELDS = [
    {
        "name": "World Settings",
        "value": (
            "- **Combat:** Hard\n"
            "- **Portals:** Disabled"
        ),
        "inline": False,
    },
    {
        "name": "Server Info",
        "value": (
            "- **Host:** GPortal \u2014 US East (Washington, D.C.)\n"
            "- **Daily restart:** <t:1774425600:t>\n"
            "- **Mod enforcement:** [ValheimEnforcer]({enforcer}) \u2014 mismatched mods are blocked on join\n"
            "- **Network:** [VBNetTweaks]({vbnet}) for improved performance"
        ).format(enforcer=ENFORCER_URL, vbnet=VBNET_URL),
        "inline": False,
    },
]

# ── Mod Configs (dropdown options) ──

MOD_CONFIGS = {
    "useful_paths": {
        "label": "Useful Paths",
        "description": "Path speed and stamina bonuses",
        "title": "Useful Paths",
        "color": 0x3498DB,
        "content": (
            "- **Cultivated ground:** +50% stamina regen\n"
            "- **Dirt paths:** +10% speed\n"
            "- **Paved roads:** +20% speed, \u221210% run stamina drain\n"
            "- **Snow:** \u221210% speed"
        ),
    },
    "epicloot": {
        "label": "EpicLoot",
        "description": "Bounties, drop rates, loot system",
        "title": "EpicLoot",
        "color": 0xE67E22,
        "content": (
            "- **Bounties:** 10\n"
            "- **99%** chance to drop materials\n"
            "- **1%** chance to drop unidentified item"
        ),
    },
    "inventory": {
        "label": "Inventory",
        "description": "Extra rows, quick slots, utility slots",
        "title": "Inventory",
        "color": 0x9B59B6,
        "content": (
            "- **+2** extra inventory rows\n"
            "- **+3** extra quick slots\n"
            "- **+1** extra utility slot"
        ),
    },
    "post_boss": {
        "label": "Post-Boss Spawns",
        "description": "Post-boss biome invasion settings",
        "title": "Post-Boss Biome Spawns",
        "color": 0xE74C3C,
        "content": (
            "Post-boss spawn invasions are **disabled** \u2014 killing a boss "
            "will not cause new creature types to appear in earlier biomes.\n\n"
            "For example:\n"
            "- No Fulings in Meadows after Yagluth\n"
            "- No Seekers in Plains after The Queen"
        ),
    },
    "star_levels": {
        "label": "Star Levels Expanded",
        "description": "Difficulty scaling, damage multipliers",
        "title": "Star Levels Expanded \u2014 Difficulty",
        "color": 0xE74C3C,
        "content": (
            "**Default Damage Scaling**\n"
            "```\n"
            "Star Level  \u2502 Normal Creatures \u2502 Bosses\n"
            "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n"
            "0 stars     \u2502 1.0x (100%)      \u2502 1.0x  (100%)\n"
            "1 star      \u2502 1.1x (110%)      \u2502 1.02x (102%)\n"
            "2 stars     \u2502 1.2x (120%)      \u2502 1.04x (104%)\n"
            "3 stars     \u2502 1.3x (130%)      \u2502 1.06x (106%)\n"
            "5 stars     \u2502 1.5x (150%)      \u2502 1.10x (110%)\n"
            "10 stars    \u2502 2.0x (200%)      \u2502 1.20x (120%)\n"
            "```\n"
            "`EnemyDamageLevelMultiplier` = 0.1 \u2022 `BossEnemyDamageMultiplier` = 0.02\n"
            "Formula: `damage_multiplier = 1 + (star_level \u00d7 DamagePerLevel)`"
        ),
    },
}

# ── Guides & Tips (dropdown options) ──

GUIDES = {
    "wild_shrine": {
        "label": "Wild Shrine Rewards",
        "description": "Solo tribute costs and loot per biome",
        "title": "EpicLoot \u2014 Wild Shrine Rewards (Solo)",
        "color": 0xE67E22,
        "content": (
            "**Meadows** \u2014 3 Boar Trophies\n"
            "> 10 Magic Dust/Essence, 17 Magic Reagent\n\n"
            "**Black Forest** \u2014 3 Greydwarf or Skeleton Trophies\n"
            "> 10 Rare Dust/Essence, 15 Rare Reagent\n\n"
            "**Swamp** \u2014 3 Draugr Trophies\n"
            "> 5 Rare Dust/Essence, 10 Rare Reagent\n"
            "> 3 Epic Dust/Essence, 6 Epic Reagent\n\n"
            "**Mountain** \u2014 3 Wolf Trophies\n"
            "> 10 Epic Dust/Essence, 15 Epic Reagent\n"
            "> 5 Legendary Dust/Essence, 10 Legendary Reagent\n\n"
            "**Plains** \u2014 3 Fuling Trophies\n"
            "> 10 Epic Dust/Essence, 15 Epic Reagent\n"
            "> 10 Legendary Dust/Essence, 15 Legendary Reagent\n\n"
            "**Mistlands** \u2014 3 Seeker Trophies\n"
            "> 10 Epic Dust/Essence, 15 Epic Reagent\n"
            "> 10 Legendary Dust/Essence, 15 Legendary Reagent\n"
            "> 5 Mythic Dust/Essence/Reagent"
        ),
    },
    "spawn_chances": {
        "label": "Star Level Spawn Chances",
        "description": "Spawn formula, base chances, biome caps",
        "title": "Star Levels \u2014 Spawn Chances & Biome Caps",
        "color": 0xE74C3C,
        "content": (
            "Sequential roll: random number 0\u2013100, creature levels up while "
            "roll < threshold.\n\n"
            "`effective_chance = (base + dist_bonus \u00d7 dist_influence) \u00d7 night_bonus`\n"
            "- `dist_influence` = 1.5 most biomes, 0.5 Ashlands/Deep North\n"
            "- `night_bonus` = 1.5\u00d7 at night\n\n"
            "**Base Chances**\n"
            "```\n"
            "Star \u2502 Base %     Star \u2502 Base %\n"
            "\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500   \u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n"
            "  1  \u2502  20       5  \u2502  1\n"
            "  2  \u2502  10       6  \u2502  0.5\n"
            "  3  \u2502   5       7  \u2502  0.25\n"
            "  4  \u2502   2     8-25 \u2502  halving\n"
            "```\n\n"
            "**Biome Max Star Caps**\n"
            "```\n"
            "Biome         \u2502 Max \u2502 Dist.\n"
            "\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\n"
            "Meadows       \u2502   4 \u2502 1.5\u00d7\n"
            "Black Forest  \u2502   6 \u2502 1.5\u00d7\n"
            "Swamp         \u2502  10 \u2502 1.5\u00d7\n"
            "Mountain      \u2502  14 \u2502 1.5\u00d7\n"
            "Plains        \u2502  18 \u2502 1.5\u00d7\n"
            "Mistlands     \u2502  22 \u2502 1.5\u00d7\n"
            "Ashlands      \u2502  26 \u2502 0.5\u00d7\n"
            "Deep North    \u2502  26 \u2502 0.5\u00d7\n"
            "```"
        ),
    },
    "distance_table": {
        "label": "Distance Bonus Table",
        "description": "Star spawn bonuses by world ring distance",
        "title": "Star Levels \u2014 Distance Bonus Table",
        "color": 0xE74C3C,
        "content": (
            "Bonuses **added** to base chances (then \u00d7 distance_influence):\n"
            "```\n"
            "Star\u2502 750  1.2k  2k   3k   4k   5k   6k   7k   8k   9.1k\n"
            "\u2500\u2500\u2500\u2500\u253c\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\n"
            "  1 \u2502 +15  +18  +24  +32  +40  +50  +60  +70  +80  +100\n"
            "  2 \u2502  +5   +7  +10  +16  +25  +35  +40  +50  +60   +80\n"
            "  3 \u2502  +1  +1.5  +3   +8  +12  +18  +20  +25  +40   +60\n"
            "  4 \u2502   -  +0.5  +1   +3   +4   +6   +9  +10  +12   +20\n"
            "  5 \u2502   -    -  +0.5  +1   +2   +3   +6   +8  +10   +15\n"
            "  6 \u2502   -    -    -  +0.5  +1   +2   +3   +6   +8   +12\n"
            "  7 \u2502   -    -    -    -  +0.5  +1   +2   +4   +6   +10\n"
            "  8 \u2502   -    -    -    -    -  +0.5  +1   +2   +4    +8\n"
            "  9 \u2502   -    -    -    -    -    -  +0.5  +1   +2    +6\n"
            " 10 \u2502   -    -    -    -    -    -  +.25 +0.5  +1    +4\n"
            "11+ \u2502   -    -    -    -    -    -    -   escalates ...\n"
            "```"
        ),
    },
}

# ── Button sections (ephemeral responses) ──

SECTIONS = {
    "how_to_join": {
        "title": "How to Join",
        "color": 0x2ECC71,
        "description": (
            "1. Download [r2modman](https://thunderstore.io/package/ebkr/r2modman/)\n"
            "2. Download the [Praetoris modpack]({modpack})\n"
            "3. **Do not update mods** \u2014 server enforces versions\n"
            "4. Launch modded\n"
            "5. Use the **FastLink** section (top right) to join Praetoris"
        ).format(modpack=MODPACK_URL),
    },
    "greylisted": {
        "title": "Greylisted (Optional) Mods",
        "color": 0x95A5A6,
        "description": (
            "These mods are allowed but not required:\n\n"
            "- [VNEI v0.17.4](https://thunderstore.io/c/valheim/p/MSchmoecker/VNEI/)\n"
            "- [SearsCatalog v1.8.0](https://thunderstore.io/c/valheim/p/ComfyMods/SearsCatalog/)\n"
            "- [Armoire v1.1.3](https://thunderstore.io/c/valheim/p/Advize/Armoire/)\n"
            "- [More Vanilla Build Prefabs v1.4.4](https://thunderstore.io/c/valheim/p/Searica/More_Vanilla_Build_Prefabs/)\n"
            "- [MyLittleUI v1.2.10](https://thunderstore.io/c/valheim/p/shudnal/MyLittleUI/)\n"
            "- [FastLink v1.4.8](https://thunderstore.io/c/valheim/p/Azumatt/FastLink/)\n"
            "- Newtonsoft.Json Detector v1.0.0\n"
            "- [RecipeManager v0.5.5](https://thunderstore.io/c/valheim/p/MidnightMods/RecipeManager/)\n"
            "- [TimeoutLimit v0.2.0](https://thunderstore.io/c/valheim/p/MSchmoecker/TimeoutLimit/)\n"
            "- [LocalizationCache v0.3.0](https://thunderstore.io/c/valheim/p/MSchmoecker/LocalizationCache/)\n"
            "- [Gizmo v1.15.0](https://thunderstore.io/c/valheim/p/ComfyMods/Gizmo/)\n"
            "- [Recipe Description Expansion v1.1.7](https://thunderstore.io/c/valheim/p/Azumatt/Recipe_Description_Expansion/)\n"
            "- [InstantEquip v1.0.6](https://thunderstore.io/c/valheim/p/Smoothbrain/InstantEquip/)\n"
            "- [Venture Farm Grid v0.1.2](https://thunderstore.io/c/valheim/p/VentureValheim/Venture_Farm_Grid/)\n"
            "- [Discord Screenshots v1.5.0](https://thunderstore.io/c/valheim/p/warpalicious/Discord_Screenshots/)\n"
            "- [AzuAutoStore v3.0.14](https://thunderstore.io/c/valheim/p/Azumatt/AzuAutoStore/)\n"
            "- [FirstPersonMode v1.3.12](https://thunderstore.io/c/valheim/p/Azumatt/FirstPersonMode/)\n"
            "- [Asocial Cartography v0.3.1](https://thunderstore.io/c/valheim/p/VentureValheim/Asocial_Cartography/)\n"
            "- [Ore Support v1.11.0](https://thunderstore.io/c/valheim/p/JereKuusela/Ore_Support/)\n"
            "- [DualWielder v1.1.1](https://thunderstore.io/c/valheim/p/RustyMods/DualWielder/)"
        ),
    },
}
