# Champions Trainer

From version **1.0.14**, everything this mod sells is bought from a **Champions Trainer**, an NPC
that stands somewhere in the world. That covers stat points, loading a saved set, the nature, the
ability and the moves of a Pokémon in training. The summary screen still shows all of it anywhere
you open it. It just doesn't sell anything on its own.

Prices are the same as before. [Training Costs](training-costs.md) lists them.

## Placing a trainer

The trainer is a regular Cobblemon NPC, so an operator places it with Cobblemon's own command:

```
/spawnnpc cobblemon_champions_training:champions_trainer
```

It does not despawn, cannot be hurt, and stays where it was placed across restarts. Cobblemon's NPC
tools (`/npcedit`, `/npcdelete`, the NPC editor item in creative) work on it like on any other NPC.
On a server, put one wherever players should go to train, such as a Pokémon Center or a gym.

## Training at the trainer

1. Walk up to the trainer and talk to it (right click).
2. Your party's summary opens, with every training control live: **SP**, **Sets → Load**, the
   **Nature** and **Ability** pickers on the **Info** page, and the move screen on **Moves**.
3. Buy what you want, exactly as described in [Stat Points](stat-points.md),
   [Saved Sets](sets.md) and [Nature, Ability & Moves](nature-ability-moves.md).
4. Close the summary when you are done. Talk to the trainer again to keep training.

If you have no Pokémon with you, the trainer says to come back when you do.

## Away from a trainer

Open the summary anywhere else (with the summary key, or from the PC) and you can still read
everything, but you can't change it:

- On **SP**, the **+**, **−**, **++**, **Save** and **Reset** buttons are greyed out and the footer
  says *Visit a Champions Trainer to change this Pokémon.*
- On **Sets**, **Load** is greyed out the same way. **Store**, **Delete** and renaming a set still
  work, because a set is only a note kept on your own computer.
- On **Info**, the **Nature** and **Ability** rows have no **▼** and don't open.
- On **Moves**, the move screen does not open for a Pokémon in training, and a notice says to visit
  a trainer. Reordering moves still works.

A Pokémon that is not in training (below 31 in every IV) is untouched: its summary and its moves
are plain Cobblemon everywhere.

## Distance

The server checks every purchase, not just the screen. You have to be in the same world as the
trainer that opened the summary and within **8 blocks** of it. If you walk away, or the trainer is
removed, the next purchase is refused with the same *Visit a Champions Trainer* message. Talk to a
trainer again to carry on.

## Server notes

- With **"Moves come from"** set to *Cobblemon's list, free*, the mod leaves moves alone and the move
  screen works anywhere, as in plain Cobblemon. The other two settings put move changes at the
  trainer too. See [the settings](commands.md#the-settings).
- Mints, Ability Capsules and Ability Patches are items, not summary controls. They follow their own
  settings and are not tied to the trainer.
- Every player who trains needs the mod on their client. On a client without it, the trainer does
  nothing.
