# The Gym Vault

A player-held gym has a **vault**: the CobbleDollars that challengers lost to its leader. The holder
sets the **penalty** a challenger risks, and takes the vault's money when they like.

Everything here is on the **Vault** tab of the [Gym Manager](gyms.md#the-gym-manager), which only the
gym's holder sees. City gyms led by an RCT leader have no vault; their
[penalty](gyms.md#fighting-a-city-leader) is destroyed.

## Setting the penalty

The tab shows the **Penalty** and what the **Vault** holds.

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
- **Winning costs nothing,** and neither does a battle the server stops with no winner.
- If the gym's licence ends during the battle, or you spent the money meanwhile, nothing moves.

## Withdrawing

**Withdraw** appears when the vault holds money and moves all of it to your CobbleDollars. If
CobbleDollars refuses the payment, the vault keeps its money and you can try again.

## When the licence ends

Renouncing, expiring or a takeover pays the **whole vault to the holder** before the gym goes vacant.
A holder who is offline gets it on their **next login**, and is told then. The money is not lost if
CobbleDollars refuses it: it is kept for the next login.

## Switching it off

With `vault.enabled` off, no player leader charges a penalty and a challenger needs none to start. The
tab says penalties are off; vaults keep what they hold, can still be withdrawn, and are still paid out
when a licence ends.
