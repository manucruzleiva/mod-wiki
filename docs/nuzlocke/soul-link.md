# ❤️‍🔥 Soul Link (co-op)

The cooperative Nuzlocke: two to four players **sign a contract**, and from then on the Pokémon they
caught in the same place are bound to each other. One dies, they all die.

## The bind is where you caught it

Not a party slot, not the order you caught things in — **the zone**. You and your partner both catch
something on Route 3, and those two Pokémon are soulmates for the rest of the run.

<div class="grid cards" markdown>

-   ### 🔗 Bound

    Two or more members have caught in that zone. The Pokémon are tied together and free to battle.

-   ### ⏳ Pending

    You caught somewhere your partner has not reached yet. **It cannot battle** until they catch
    there too — the chat tells you which zone it is waiting on.

-   ### 💀 Orphaned

    Your partner **failed** that zone's encounter, so the other half is never coming. The Pokémon
    that was waiting dies.

</div>

Every Pokémon in a linked run must be bound; *pending* is the only legitimate exception. An unbound
Pokémon is one whose death would cost the group nothing, which is the one thing a Soul Link is.

Your **starter** counts as its own shared zone, so starters bind to starters. Gifts, trades and
anything else you did not catch in the world share that same zone.

## Signing

Right-click a player and pick **Soul Link** from Cobblemon's interaction wheel, next to Trade and
Duel — or type `/nuzlocke soullink link <player>`.

Being offered a link is **a screen you have to answer**: a dialogue box at the bottom of the screen
with the face of the player who sent it, Accept or Decline, no escape key, and it comes back if you
die or log out while it is open. Agreeing to a Soul Link means agreeing that somebody else's mistakes
can end your run, so it is not a line of chat that scrolls away.

- **It counts down.** A bar under the box drains with "Expires in m:ss" and turns red in the last 15
  seconds. When the offer is gone — it expired, someone declined, or the sender left — the box closes
  itself.
- **The sender sees every answer as it comes in.** A card at the top right lists each invited player
  with their face and whether they are pending, have accepted or have declined, over the same draining
  bar. It never stops you playing, players who have already accepted see it too, and it moves down out
  of the way of your potion effect icons. When the offer ends it shows **Linked** in green, or who
  declined, or that it expired, in red, for three seconds.

Signing binds **what you already own**, matched up by zone on the spot. Anything caught somewhere
your partner has not been simply waits.

### Bringing in a third and a fourth

A contract can be extended at any time. Whoever joins binds into every zone they have already caught
in, and the binds the others had already formed stay exactly as they were — nobody loses their team
because somebody else signed.

## When it goes wrong

- **Shared death** — a linked Pokémon dies and every soulmate dies with it, even if its owner is
  offline. They meet the news on their next login.
- **No lone combat** — a bound Pokémon stays in its ball unless its partners are in their owners'
  active parties, and those owners are online.
- **One last chance** — being wiped out by *your partner's* loss is not instantly a Game Over. With
  zones still left to catch in, you may travel and try one more encounter. Land it and the run
  continues; fail it and it ends.
- **Starting over** — [`/pokemonrestart`](commands.md#quick-reference) takes you out of the
  contract. Your Pokémon leave every bind they were in and the others keep theirs; a bind left with
  only one member dissolves, so its Pokémon is free rather than pending.

## The Soul Link tab

While you are in a link, Cobblemon's Pokémon summary gets a **Soul Link** tab right after the
[Log](nuzlocke.md#the-log) tab, and `/nuzlocke soullink summary` opens your party's summary on it.
Outside a link the tab is not there.

- **Every soul is a row of slots joined by a chain.** Each player has a column, yours first and
  framed in white, so your side of every soul is always in the same place.
- **A living soul** has grey slots and the chain between them holds. **A lost one** turns
  Cobblemon's fainted red, its Pokémon go see-through, and the chain is broken.
- **A soul still waiting on a partner** shows who owes the catch and where: a dashed, empty slot with
  their name and the zone, behind a faded chain. Those are the Pokémon that cannot battle yet.
- **Hover a Pokémon** to read its full name, level, HP and owner. Partners who are offline still
  appear, showing the last state the run recorded.

The [Log](nuzlocke.md#the-log) tab becomes the link's log too: every member's encounter in a zone is a
slot of its own, so a broken soul shows a red slot in its line, and it shows who is on a
[Gym Leader Challenge](nuzlocke.md#gym-leader-challenge), and on what type, for every partner who is
online.

## Settings

| Option | Default | What it does |
| --- | :---: | --- |
| `enable_soul_link` | on | master toggle for the whole system |
| `soul_link_max_players` | 4 | how many players one contract may hold (2–4) |
| `soul_link_request_seconds` | 120 | how long an offer stays open, 15–600 seconds |
| `prevent_lone_combat` | on | a bound Pokémon needs its partners active to be sent out |

Soul Link sits on top of the [Hardcore Nuzlocke](nuzlocke.md) rules — set both up from the same
**NUZLOCKE** tab at world creation, or later with
[`/nuzlocke set`](commands.md).
