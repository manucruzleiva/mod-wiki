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
- **Tap R** to recall and pick another. **Hold R for 2 seconds** to run from a wild fight; against a
  trainer or a player it asks you to hold again, and the second hold forfeits as a loss.
- **EXP and EVs are paid at each knock-out**, by Cobblemon's own rules, to every Pokémon you drove in
  the fight. Level-up moves and evolutions wait for the fight to end.
- **A dropped connection** gets 15 seconds of grace: come back and your Pokémon goes out again where
  it stood.

## NPC trainers

Cobblemon's own NPC trainers send their party out in front of them one at a time (two in doubles),
each fighting like a wild Pokémon that never flees. The next comes out 1.5 seconds after one faints.
They **switch** out of a bad type matchup, or under 25 % HP for a healthier Pokémon, at most once
every 10 seconds. Beating the whole party wins.

## RCT trainers

With **Radical Cobblemon Trainers**, its trainers fight the same way, and the fight still counts in
RCT:

- **a win** adds the trainer to your progress, moves the series on, raises your level cap and drops
  its loot;
- **a loss** counts nothing and starts the trainer's cooldown;
- **a fight with no winner** (you ran, walked away, the server stopped) frees the trainer again.

The trainer's datapack win commands are not run in a real-time fight. If a future RCT version
changes what Action Combat calls, the server log says so once and RCT battles go back to turn-based.

## Player against player

Both players drive their Pokémon. With `/cac config pvp time_limit_seconds` above 0 the fight ends
at the limit: the side with more Pokémon standing wins, then the one with more HP left, and a full
tie is a draw. Warnings come a minute, 30 and 10 seconds before. Off by default.

## Doubles

Each Trainer drives one Pokémon and an ally AI runs the next healthy one beside it. **H** swaps
control and camera between the two, and when the one you drive faints, control goes to the ally at
once. The spread moves that hit the partner in the games (Earthquake, Surf, Explosion, Discharge...)
hit your partner in the blast too.
