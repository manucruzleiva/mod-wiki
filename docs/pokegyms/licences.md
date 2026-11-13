# Licences

A **licence** is what lets a player run a gym as its leader. The rules below are in the mod today.

!!! note "A City gym's licence has to be earned"
    Every gym in this build is a [City gym](gyms.md#city-gyms-and-their-leaders), led by an RCT
    leader. Its licence is for sale only to a player who
    [beat that leader](gyms.md#unlocking-a-city-gym); to everyone else the Licence tab does not appear.

## The rules

- **One licence per player on the whole server**, whatever the dimension.
- **It costs 25,000 CobbleDollars** by default, paid at the gym's Gym Manager. The server sets the
  price ([Configuration](commands.md#configuration)).
- **A City gym sells its licence only to a player who beat its leader**, at the same price and with the
  same one licence per player. Beating them is remembered even with licences switched off. While the
  gym is held its leader is gone; when the licence ends the leader is back and the gym is locked again
  for everyone, the former holder included.
- **A held gym can be taken over** with its leader's medal and a fee, which moves the licence to the taker; see
  [Taking over a gym](gyms.md#taking-over-a-gym). The taker's own previous licence is given up first.
- **It ends after 30 days without logging in** by default, or when its holder renounces it. Either
  way a town gym goes vacant, anyone can buy it again, and the former holder may buy another (a City
  gym goes back to its leader, as above). The
  server checks when it starts and once a day after. With the days set to 0, a licence never
  expires.

## The Licence tab

At a vacant town gym, a City gym whose leader you beat, or a gym a player holds, the Gym Manager screen adds a **Licence** tab:

- **For a visitor**: the price, how many CobbleDollars you have, and a **Buy** button. If you
  already hold a licence, the tab says which gym it is; if you are short, it says how much more you
  need. The server checks the price and your balance again when you click.
- **At a gym a player holds** (a visitor, or a disciple of that gym): the **takeover fee**, how many CobbleDollars you
  have and a **Take over** button. Hold the leader's medal in your main hand when you click; see
  [Taking over a gym](gyms.md#taking-over-a-gym).
- **For the holder**: the gym's [vault](vault.md) and its **Penalty** (click the row to raise it, shift-click to lower
  it), when the licence expires (**Expiry**), the penalty's **Range** (only while penalties are on), a **Withdraw**
  button in the bottom-left box and a **Renounce** button in the bottom-right one, which asks for a second click to
  confirm and pays the vault out, [split with the disciples](vault.md#splitting-the-vault) if you set shares. Renounce is
  refused with a message while a challenger is battling the leader or one of the disciples; try again when the battle ends.

## After a crash

When the server starts, it checks every licence against the gym it names, and **the gym wins**: a
licence whose gym no longer names its player is dropped, a gym naming a holder the licence list
forgot is added to it, and if one player ends up holding two gyms, the second goes vacant. Each fix
is written to the server log. Licences of gyms in a dimension that is not loaded are left alone.

Switching licences off ([Configuration](commands.md#configuration)) stops every gym from
selling its licence. Licences already held stay, and still expire or can be renounced.
