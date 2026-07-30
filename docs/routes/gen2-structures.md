# Gen2 structure reference

Every structure found in the COBBLEVERSE pack (vanilla + all mods), for configuring which count
as **cities** in the native route network. Copy the exact ids you want into
**`gen2_settlement_allowlist`** in `config/cobblemon_routes.json` — a non-empty list overrides
the automatic rule completely.

- **Automatic rule** (used while the allowlist is empty): a structure counts as a settlement if
  it is in the `#minecraft:village` tag, or its id names a village/town/city — and never if the
  id contains `ancient`, `mineshaft` or `ruin`.
- ✅ = the automatic rule classifies it as a settlement today (by name; tag members may add more).
- Regenerate the live list anytime with `/routes structures` in-game (writes
  `cobblemon_routes_structures.txt` with real tags).


## bca

- `bca:village/dark_mid` ✅
- `bca:village/dark_small` ✅
- `bca:village/default_large` ✅
- `bca:village/default_mid` ✅
- `bca:village/default_small` ✅
- `bca:village/fighting_large` ✅
- `bca:village/fighting_mid` ✅
- `bca:village/fighting_small` ✅
- `bca:village/witch_hut`

## cobblemon

- `cobblemon:fishing_boat/beach`
- `cobblemon:fishing_boat/deep_ocean`
- `cobblemon:fishing_boat/warm_ocean`
- `cobblemon:fossils/prehistoric_birch_tree`
- `cobblemon:fossils/prehistoric_dripstone_oasis`
- `cobblemon:fossils/prehistoric_enhydro_agate`
- `cobblemon:fossils/prehistoric_eroded_pillar`
- `cobblemon:fossils/prehistoric_frozen_pond`
- `cobblemon:fossils/prehistoric_frozen_spike`
- `cobblemon:fossils/prehistoric_hydrothermal_vents`
- `cobblemon:fossils/prehistoric_lush_den`
- `cobblemon:fossils/prehistoric_mossy_pond`
- `cobblemon:fossils/prehistoric_mud_pit`
- `cobblemon:fossils/prehistoric_oak_tree`
- `cobblemon:fossils/prehistoric_powdered_deposit`
- `cobblemon:fossils/prehistoric_preserved_skeleton`
- `cobblemon:fossils/prehistoric_rooted_pit`
- `cobblemon:fossils/prehistoric_sandy_den`
- `cobblemon:fossils/prehistoric_spruce_tree`
- `cobblemon:fossils/prehistoric_submerged_impact`
- `cobblemon:fossils/prehistoric_submerged_spike`
- `cobblemon:fossils/prehistoric_sunscorched_den`
- `cobblemon:fossils/prehistoric_sunscorched_remains`
- `cobblemon:fossils/prehistoric_suspicious_mound`
- `cobblemon:fossils/prehistoric_underwater_fissure`
- `cobblemon:fossils/prehistoric_vibrant_hydrothermal_vents`
- `cobblemon:ruins/crumbling_arch_ruins`
- `cobblemon:ruins/decaying_crypt_ruins`
- `cobblemon:ruins/deserted_gimmi_tower`
- `cobblemon:ruins/deserted_house_ruins`
- `cobblemon:ruins/deserted_tower_ruins`
- `cobblemon:ruins/deserted_town_center_ruins`
- `cobblemon:ruins/fallen_statue_ruins`
- `cobblemon:ruins/frozen_gimmi_tower`
- `cobblemon:ruins/hidden_bunker_ruins`
- `cobblemon:ruins/luna_henge_ruins`
- `cobblemon:ruins/lush_gimmi_tower`
- `cobblemon:ruins/mossy_oubliette_ruins`
- `cobblemon:ruins/rooted_arch_ruins`
- `cobblemon:ruins/rooted_gimmi_tower`
- `cobblemon:ruins/sol_henge_ruins`
- `cobblemon:ruins/stonjourner_henge_ruins`
- `cobblemon:ruins/sunscorched_gimmi_tower`
- `cobblemon:ruins/temperate_gimmi_tower`
- `cobblemon:ruins/toppled_pillars_ruins`
- `cobblemon:ruins/unstable_cave_ruins`
- `cobblemon:shipwreck_coves/lush_shipwreck_cove`
- `cobblemon:shipwreck_coves/submerged_shipwreck_cove`

## cobbleverse

- `cobbleverse:ash`
- `cobbleverse:blaine`
- `cobbleverse:brock`
- `cobbleverse:crown_cemetery`
- `cobbleverse:crown_spire`
- `cobbleverse:dawn_tower`
- `cobbleverse:dusk_tower`
- `cobbleverse:erika`
- `cobbleverse:giovanni`
- `cobbleverse:kanto_league` ✅
- `cobbleverse:koga`
- `cobbleverse:legendary/articuno`
- `cobbleverse:legendary/moltres`
- `cobbleverse:legendary/zapdos`
- `cobbleverse:ltsurge`
- `cobbleverse:misty`
- `cobbleverse:mythical/mew`
- `cobbleverse:sabrina`
- `cobbleverse:team_rocket_tower` ✅

## legendarymonuments

- `legendarymonuments:distortion_portal`
- `legendarymonuments:eternatus_cocoon`
- `legendarymonuments:firescourge_shrine`
- `legendarymonuments:giratina_island`
- `legendarymonuments:grasswither_shrine`
- `legendarymonuments:groundblight_shrine`
- `legendarymonuments:icerend_shrine`
- `legendarymonuments:lake_acuity`
- `legendarymonuments:lake_valor`
- `legendarymonuments:lake_verity`
- `legendarymonuments:outskirt_stand`
- `legendarymonuments:stark_mountain`
- `legendarymonuments:turnback_cave`

## mega_showdown

- `mega_showdown:archaeological_site`
- `mega_showdown:mega_site`
- `mega_showdown:megaroid`
- `mega_showdown:observatory`
- `mega_showdown:wishing_weald`

## minecraft

- `minecraft:ancient_city`
- `minecraft:bastion_remnant`
- `minecraft:buried_treasure`
- `minecraft:desert_pyramid`
- `minecraft:end_city` ✅
- `minecraft:fortress`
- `minecraft:igloo`
- `minecraft:jungle_pyramid`
- `minecraft:mansion`
- `minecraft:mineshaft`
- `minecraft:mineshaft_mesa`
- `minecraft:monument`
- `minecraft:nether_fossil`
- `minecraft:ocean_ruin_cold`
- `minecraft:ocean_ruin_warm`
- `minecraft:pillager_outpost`
- `minecraft:ruined_portal`
- `minecraft:ruined_portal_desert`
- `minecraft:ruined_portal_jungle`
- `minecraft:ruined_portal_mountain`
- `minecraft:ruined_portal_nether`
- `minecraft:ruined_portal_ocean`
- `minecraft:ruined_portal_swamp`
- `minecraft:shipwreck`
- `minecraft:shipwreck_beached`
- `minecraft:stronghold`
- `minecraft:swamp_hut`
- `minecraft:trail_ruins`
- `minecraft:trial_chambers`
- `minecraft:village_desert` ✅
- `minecraft:village_plains` ✅
- `minecraft:village_savanna` ✅
- `minecraft:village_snowy` ✅
- `minecraft:village_taiga` ✅

## repurposed_structures

- `repurposed_structures:ancient_city_end`
- `repurposed_structures:ancient_city_nether`
- `repurposed_structures:ancient_city_ocean`
- `repurposed_structures:bastion_underground`
- `repurposed_structures:city_nether` ✅
- `repurposed_structures:city_overworld` ✅
- `repurposed_structures:fortress_jungle`
- `repurposed_structures:igloo_grassy`
- `repurposed_structures:igloo_mangrove`
- `repurposed_structures:igloo_mushroom`
- `repurposed_structures:igloo_stone`
- `repurposed_structures:mansion_birch`
- `repurposed_structures:mansion_desert`
- `repurposed_structures:mansion_jungle`
- `repurposed_structures:mansion_mangrove`
- `repurposed_structures:mansion_oak`
- `repurposed_structures:mansion_savanna`
- `repurposed_structures:mansion_snowy`
- `repurposed_structures:mansion_taiga`
- `repurposed_structures:mineshaft_basalt`
- `repurposed_structures:mineshaft_birch`
- `repurposed_structures:mineshaft_crimson`
- `repurposed_structures:mineshaft_dark_forest`
- `repurposed_structures:mineshaft_desert`
- `repurposed_structures:mineshaft_end`
- `repurposed_structures:mineshaft_icy`
- `repurposed_structures:mineshaft_jungle`
- `repurposed_structures:mineshaft_nether`
- `repurposed_structures:mineshaft_ocean`
- `repurposed_structures:mineshaft_savanna`
- `repurposed_structures:mineshaft_soul`
- `repurposed_structures:mineshaft_stone`
- `repurposed_structures:mineshaft_swamp`
- `repurposed_structures:mineshaft_taiga`
- `repurposed_structures:mineshaft_warped`
- `repurposed_structures:monument_desert`
- `repurposed_structures:monument_icy`
- `repurposed_structures:monument_jungle`
- `repurposed_structures:monument_nether`
- `repurposed_structures:outpost_badlands`
- `repurposed_structures:outpost_basalt`
- `repurposed_structures:outpost_birch`
- `repurposed_structures:outpost_crimson`
- `repurposed_structures:outpost_desert`
- `repurposed_structures:outpost_end`
- `repurposed_structures:outpost_giant_tree_taiga`
- `repurposed_structures:outpost_icy`
- `repurposed_structures:outpost_jungle`
- `repurposed_structures:outpost_mangrove`
- `repurposed_structures:outpost_nether_brick`
- `repurposed_structures:outpost_oak`
- `repurposed_structures:outpost_ocean`
- `repurposed_structures:outpost_savanna`
- `repurposed_structures:outpost_snowy`
- `repurposed_structures:outpost_soul`
- `repurposed_structures:outpost_taiga`
- `repurposed_structures:outpost_warped`
- `repurposed_structures:pyramid_badlands`
- `repurposed_structures:pyramid_dark_forest`
- `repurposed_structures:pyramid_end`
- `repurposed_structures:pyramid_flower_forest`
- `repurposed_structures:pyramid_giant_tree_taiga`
- `repurposed_structures:pyramid_icy`
- `repurposed_structures:pyramid_jungle`
- `repurposed_structures:pyramid_mushroom`
- `repurposed_structures:pyramid_nether`
- `repurposed_structures:pyramid_ocean`
- `repurposed_structures:pyramid_snowy`
- `repurposed_structures:ruined_portal_end`
- `repurposed_structures:ruins_land_cold`
- `repurposed_structures:ruins_land_hot`
- `repurposed_structures:ruins_land_icy`
- `repurposed_structures:ruins_land_warm`
- `repurposed_structures:ruins_nether`
- `repurposed_structures:shipwreck_crimson`
- `repurposed_structures:shipwreck_end`
- `repurposed_structures:shipwreck_nether_bricks`
- `repurposed_structures:shipwreck_warped`
- `repurposed_structures:stronghold_end`
- `repurposed_structures:stronghold_nether`
- `repurposed_structures:temple_nether_basalt`
- `repurposed_structures:temple_nether_crimson`
- `repurposed_structures:temple_nether_soul`
- `repurposed_structures:temple_nether_warped`
- `repurposed_structures:temple_nether_wasteland`
- `repurposed_structures:temple_ocean`
- `repurposed_structures:temple_taiga`
- `repurposed_structures:village_badlands` ✅
- `repurposed_structures:village_bamboo` ✅
- `repurposed_structures:village_birch` ✅
- `repurposed_structures:village_cherry` ✅
- `repurposed_structures:village_crimson` ✅
- `repurposed_structures:village_dark_forest` ✅
- `repurposed_structures:village_giant_taiga` ✅
- `repurposed_structures:village_jungle` ✅
- `repurposed_structures:village_mountains` ✅
- `repurposed_structures:village_mushroom` ✅
- `repurposed_structures:village_oak` ✅
- `repurposed_structures:village_ocean` ✅
- `repurposed_structures:village_swamp` ✅
- `repurposed_structures:village_warped` ✅
- `repurposed_structures:witch_hut_birch`
- `repurposed_structures:witch_hut_dark_forest`
- `repurposed_structures:witch_hut_giant_tree_taiga`
- `repurposed_structures:witch_hut_mangrove`
- `repurposed_structures:witch_hut_oak`
- `repurposed_structures:witch_hut_taiga`

## terralith

- `terralith:desert_outpost`
- `terralith:fortified_desert_village` ✅
- `terralith:fortified_village` ✅
- `terralith:glacial_hut`
- `terralith:igloo`
- `terralith:mage_complex`
- `terralith:mage_tower`
- `terralith:mage_tower_autumn`
- `terralith:mage_tower_spring`
- `terralith:mage_tower_summer`
- `terralith:mage_tower_winter`
- `terralith:rubble_desert`
- `terralith:rubble_forest`
- `terralith:rubble_jungle`
- `terralith:rubble_mesa`
- `terralith:rubble_mountain`
- `terralith:rubble_taiga`
- `terralith:spire`
- `terralith:underground/frosted_dungeon`
- `terralith:underground/giant_bee_hive`
- `terralith:underground/mining_outpost`
- `terralith:underground/oak_cabin`
- `terralith:underground/old_refinery`
- `terralith:underground/sunken_tower`
- `terralith:underground/witch_hut`
- `terralith:underground_cabin`
- `terralith:valley_lodge`
- `terralith:witch_hut`
