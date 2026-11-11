# The Gym Vault

A player-held gym has a **vault**: the CobbleDollars that challengers lost to its leader. The holder
sets the **penalty** a challenger risks, and takes the vault's money when they like.

Everything here is on the **Licence** tab of the [Gym Manager](gyms.md#the-gym-manager), which only the
gym's holder sees (see [Licences](licences.md#the-licence-tab)). City gyms led by an RCT leader have no vault; their
[penalty](gyms.md#fighting-a-city-leader) is destroyed.

## Setting the penalty

The holder's Licence tab shows the **Penalty**, what the **Vault** holds, when the licence expires (**Expiry**) and
the penalty's **Range** (only while penalties are on).

- **Click the Penalty row to raise it** by a tenth of the server's range. **Shift-click lowers it.**
  Past either end it wraps round to the other.
- **It stays within the server's range**, `vault.penalty_min` to `vault.penalty_max` (100 to 10,000
  CobbleDollars by default; see [Configuration](commands.md#configuration)). The server checks it
  again, so no other amount gets through.
- **A new holder starts on the least.**
- **It is locked while your leader is battling.** You are told to change it when the battle ends, so a
  challenger never pays more than they agreed to.

## Challengers

- **You need the penalty in hand** to challenge the leader. There are no debts: if you carry less, you
  are told what it costs and what you have, and the fight does not start.
- **Losing pays it.** A loss, a forfeit or running away moves exactly the penalty from you into the
  vault. You are told what you paid.
- **Winning costs nothing,** and neither does a battle the server stops with no winner. A win over a
  player leader also pays you a share of the vault: see [Winner's share](#winners-share).
- If the gym's licence ends during the battle, or you spent the money meanwhile, nothing moves.

## Winner's share

Beating a **player leader** pays you a share of the gym's vault: `winner_share.percent` of what it holds,
**10% by default**, rounded down. A vault of 1,000 pays 100 and keeps 900. The chat tells you how much you took.

- **Only the leader pays.** Nothing is taken from the vault if the leader is not the one you beat.
- **A vault too small to give a whole CobbleDollar pays nothing.**
- **It is paid at once,** and if CobbleDollars refuses it, you get it on your **next login**. The money
  leaves the vault either way, so it is never lost.
- **Nothing moves if the gym is no longer held,** for instance when its licence ended during the battle
  (the vault has already gone to the holder).
- **Operators can change it** with [`/pokegyms config winner_share`](commands.md#configuration): `percent`
  from 0 to 100, or `enabled false`. 0 percent pays nothing too.

## Splitting the vault

The holder can give each [disciple](gyms.md#disciples) a share of the vault. Open the **Disciples** tab:
each disciple's row shows their name and share (`Name 25%`), and a last **Leader** row shows what you keep.

- **Click a disciple to give them 5% more.** Once you have nothing left to give, the next click puts them back on 0%.
  Shift-click still removes the disciple.
- **The shares always add up to 100%.** The leader keeps whatever the disciples' shares leave, and the server refuses
  a split over 100%. Only the holder can set shares.
- **A new disciple starts on 0%.** A disciple you remove gives their share back to the leader. After a
  [takeover](gyms.md#taking-over-a-gym) the new leader keeps the disciples' shares as they were.
- **Changing a share does not restart the challengers' progress** through the gym's disciples.
- **Operators can switch it off** with [`/pokegyms config vault_split enabled false`](commands.md#configuration): the
  whole vault goes to the leader and no share can be set. The shares already set are kept for when it is back on.

## Withdrawing

**Withdraw** sits in the bottom-left box of the Licence tab. It appears when the vault holds money and pays all of it
out at once: each disciple gets their [share](#splitting-the-vault), rounded down, and you get the rest, rounding
included. With no shares set, all of it goes to you. The vault goes back to 0, and you are told what you kept.

- **A disciple who is online** is paid at once and told so.
- **A disciple who is offline** is paid on their **next login**.
- **If CobbleDollars refuses a payment,** that player gets it on their next login instead: no one's share is lost.

## When the licence ends

Renouncing (the **Renounce** button, bottom-right, whose confirm text says you get the vault) or expiring pays the
**whole vault out** before the gym goes vacant, split like a [withdrawal](#withdrawing): each disciple their share and
the holder the rest. The same goes for a gym given up to make a [takeover](gyms.md#taking-over-a-gym). The gym taken
over keeps its vault for the new leader.
Anyone who is offline gets their money on their **next login**, and is told then. The money is not lost if
CobbleDollars refuses it: it is kept for the next login.

## Switching it off

With `vault.enabled` off, no player leader charges a penalty and a challenger needs none to start. The
Licence tab says penalties are off; vaults keep what they hold, can still be withdrawn, and are still paid out
when a licence ends. The [winner's share](#winners-share) has its own switch and is not turned off by it.
