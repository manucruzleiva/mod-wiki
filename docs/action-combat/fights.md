# Fights

A real-time fight opens in place of the battle Cobblemon would have started. Your lead is thrown
out and is yours to drive; your Trainer stays where the fight began, unhurt and ignored by mobs. The
fight belongs to the ones in it: nothing outside it (a third player, a mob, an arrow, lava) can hurt
its Pokémon, and nobody else can challenge, catch or trade them.

Your Pokémon cannot go more than **32 blocks** from your Trainer. At the edge it slides along a
lit boundary instead of snapping back.

## Wild Pokémon

A wild Pokémon fights back with its own moves, by an **archetype** read from its moveset: most close
in to hit, ones with mostly ranged moves keep 6 to 10 blocks away and strafe, and one with nothing to
fight with runs. It stands still through each windup while its attack animation plays: that is your
opening to dodge. It also dodges some of your attacks.

**How it picks a move** (0.1.53 and later): each damaging move's chance is its power times its type
effectiveness on the target, so a super-effective move comes up twice as often as a neutral one of
the same power, and a move the target is immune to is never picked while another fits. It also uses
**Status moves that would do something right now** (a stat stage that can still move, a status or
confusion the target can take, a heal it needs): such a move weighs 30, about one move in nine next
to three attacks of power 80, and is paid and cooled down like any move. Swords Dance at +6, Thunder
Wave on a Pokémon that already has a status, or Sand Attack with `moves accuracy_stages` off are
never picked; weather, terrain and side moves are left out for now.
`/cac config wild_ai type_aware off` and `status_weight 0` bring back the old pick (by power alone).

**How it defends**: against a strong move (power 80 or more) a wild Pokémon raises **Protect**
instead of dashing, 30 % of the time (0.1.51 and later). The bubble goes up as the windup ends, it
holds still while Protect lasts, and it pays the same Stamina and waits the same cooldown yours does,
so it never chains Protect nor raises it mid-dash. `/cac config wild_ai protect_percent` sets how
often (0 turns it off and it dodges as before) and `protect_min_power` how strong a move must be.

- **It can start the fight**: an aggressive wild Pokémon that attacks you sends your lead out.
  After a fight, wild hits wait 10 seconds before they can start the next one.
- **Others join in**: a hostile wild Pokémon within 16 blocks joins on its own, and any free wild
  Pokémon your move hits joins too, up to 3 at once. An intruder is a full opponent: it pays EXP and
  can be caught. Fights against a trainer or a player stay closed.
- **It can run**: one that ends up past the 32-block edge gets away.

The fight is won once every wild Pokémon in it is knocked out or caught.

## Catching

With **PokeBelt**, **B** makes your Trainer throw the belt's selected ball at the target you locked
(or the one you face). It is Cobblemon's own ball and catch rate, so anything that listens to
captures still hears it. A wild Pokémon can dodge the ball, half as often as it dodges moves.
Catching the last wild Pokémon wins the fight. Without PokeBelt, B tells you a belt is needed.

## Knock-outs, switching and running

- **Your Pokémon faints**: it goes back to its ball and a wheel of your party opens. After 2 seconds
  click one, or press its number. Pick nothing for 30 seconds and the first healthy one goes out.
  With none left, you lose.
- **Tap R** to recall and pick another. After a switch of your own, R waits **15 seconds** before it
  recalls again; a tap too soon shows on the action bar how many seconds are left. The wait starts
  when the Pokémon you picked goes out. A knock-out, or a recall that did not come from R, is free:
  the next Pokémon comes out at once and the wait does not restart. `/cac config switch cooldown_seconds`
  sets it (0 turns it off). **Hold R for 2 seconds** to run from a wild fight; against a
  trainer or a player it asks you to hold again, and the second hold forfeits as a loss.
  Another mod can forbid running or forfeiting (Cobblemon Nuzlocke does): the fight goes on and the
  chat says why. Running and forfeiting can be blocked; switching only waits out its cooldown.
- **EXP and EVs are paid at each knock-out**, by Cobblemon's own rules, to every Pokémon you drove in
  the fight. Level-up moves and evolutions wait for the fight to end.
- **A dropped connection** gets 15 seconds of grace: come back and your Pokémon goes out again where
  it stood.

## NPC trainers

Cobblemon's own NPC trainers send their party out in front of them one at a time (two in doubles),
each fighting like a wild Pokémon that never flees. The next comes out 1.5 seconds after one faints.
They **switch** out of a bad type matchup, or under 25 % HP for a healthier Pokémon, at most once
every 10 seconds. Beating the whole party wins.

Pokémon on the other side now dodge each other's casts too (0.1.52 and later): a move started by a
wild Pokémon or an NPC trainer's Pokémon warns the other side's wild or NPC Pokémon the same way
yours warns them. They dash aside at their archetype's dodge chance or, against a strong move, raise
Protect. A Pokémon never answers its own cast nor its own side's, and a cast aimed elsewhere warns
no one. `/cac config wild_ai dodge_npc_casts off` turns it off (on by default).

## RCT trainers

With **Radical Cobblemon Trainers**, its trainers fight the same way, and the fight still counts in
RCT:

- **a win** adds the trainer to your progress, moves the series on, raises your level cap and drops
  its loot;
- **a loss** counts nothing and starts the trainer's cooldown;
- **a fight with no winner** (you ran, walked away, the server stopped) frees the trainer again;
- **the trainer's datapack `winCommands`** run when the fight ends (0.1.49 and later): the winning
  side's list, the player's on a win and the trainer's on a loss, after the rewards above. Nothing
  runs for a fight with no winner. RCT hands these commands to Cobblemon Trainer Battle Commands
  (tbcs), so tbcs must be installed for them to work at all, in a normal battle too; without it
  nothing runs. `/cac config npc rct_win_commands off` turns it off (on by default).

If a future RCT or tbcs version changes what Action Combat calls, the server log says so once: RCT
battles go back to turn-based, or just the win commands stop running.

## Player against player

Both players drive their Pokémon. With `/cac config pvp time_limit_seconds` above 0 the fight ends
at the limit: the side with more Pokémon standing wins, then the one with more HP left, and a full
tie is a draw. Warnings come a minute, 30 and 10 seconds before. Off by default.

## Doubles

Each Trainer drives one Pokémon and an ally AI runs the next healthy one beside it. **H** swaps
control and camera between the two, and when the one you drive faints, control goes to the ally at
once. The spread moves that hit the partner in the games (Earthquake, Surf, Explosion, Discharge...)
hit your partner in the blast too.

## For other mods

A real-time fight cancels the Cobblemon battle it replaces, so Cobblemon's own battle events never
fire for it, and `BattleRegistry` does not have the player in a battle. Action Combat gives other
mods two ways to follow a fight:

- **Events**, in `com.shier.actioncombat.api.CacEvents`: `FIGHT_STARTED`, `POKEMON_KNOCKED_OUT`,
  `POKEMON_CAPTURED`, `FIGHT_WON`, `FIGHT_FLED`, `FIGHT_ENDED`, and `FIGHT_LEAVING`, which lets a mod
  veto a flee or forfeit. `/cac debug events` prints them live in chat.
- **A query** (0.1.48 and later): `com.shier.actioncombat.api.CacFights.isFighting(UUID)` answers
  whether a player is in a fight right now. It is static, runs on the server thread, and is true from
  `FIGHT_STARTED` to `FIGHT_ENDED`, for any kind or size of fight. There is no client-side version: a
  mod that needs the answer on the client sends its own.

The class name and signature are stable. A mod that does not depend on Action Combat can look the
method up by reflection, once, and treat any failure (Action Combat missing, or older than 0.1.48) as
"not fighting":

```java
Method m = Class.forName("com.shier.actioncombat.api.CacFights").getMethod("isFighting", UUID.class); // once; null on failure
boolean fighting = m != null && (Boolean) m.invoke(null, player.getUUID());
```

Combine it with Cobblemon's own check for a complete answer: a player is in a battle when
`BattleRegistry` has them **or** `isFighting` is true.
