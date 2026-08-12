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

Your **starter** counts as its own shared zone, so starters bind to starters.

## Signing

Right-click a player and pick **Soul Link** from Cobblemon's interaction wheel, next to Trade and
Duel — or type `/nuzlocke soullink link <player>`.

Being offered a link is **a screen you have to answer**: Accept or Decline, no escape key, and it
comes back if you die or log out while it is open. Agreeing to a Soul Link means agreeing that
somebody else's mistakes can end your run, so it is not a line of chat that scrolls away.

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
  active parties.
- **One last chance** — being wiped out by *your partner's* loss is not instantly a Game Over. With
  zones still left to catch in, you may travel and try one more encounter. Land it and the run
  continues; fail it and it ends.

## The Soul Link log

While you are in a link, the **I** key opens the link's log instead of your own. It is the same
screen with the truth added:

| It shows | Why it matters |
| --- | --- |
| Every member's zones, labelled with whose they are | one member spending a zone changes what the others can still do |
| Your partner's Pokémon in full | species, nickname, and whether it is alive, dead or gone |
| Which binds are **waiting** | those are the Pokémon that cannot battle yet |
| Who is on a [Gym Leader Challenge](nuzlocke.md#gym-leader-challenge), and on what type | what your partner is even allowed to use |

Partners who are offline still appear, showing the last state the run recorded.

## Settings

| Option | Default | What it does |
| --- | :---: | --- |
| `enable_soul_link` | on | master toggle for the whole system |
| `soul_link_max_players` | 4 | how many players one contract may hold (2–4) |
| `soul_link_request_seconds` | 120 | how long an offer stays open |
| `prevent_lone_combat` | on | a bound Pokémon needs its partners active to be sent out |

Soul Link sits on top of the [Hardcore Nuzlocke](nuzlocke.md) rules — set both up from the same
**NUZLOCKE** tab at world creation, or later with
[`/nuzlocke set`](commands.md).
