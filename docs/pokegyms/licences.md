# Licences

A **licence** is what lets a player run a gym as its leader. The rules below are in the mod today.

!!! note "No gym sells a licence yet"
    Only a **town gym** sells its licence, and in this build every gym is a
    [City gym](gyms.md#city-gyms), held by its Cities & Structures leader. So no Gym Manager offers
    a licence yet, and the Licence tab does not appear.

## The rules

- **One licence per player on the whole server**, whatever the dimension.
- **It costs 25,000 CobbleDollars** by default, paid at the gym's Gym Manager. The server sets the
  price ([Configuration](commands.md#configuration)).
- **A City gym never sells its licence.**
- **It ends after 30 days without logging in** by default, or when its holder renounces it. Either
  way the gym goes vacant, anyone can buy it again, and the former holder may buy another. The
  server checks when it starts and once a day after. With the days set to 0, a licence never
  expires.

## The Licence tab

At a vacant town gym, the Gym Manager screen adds a **Licence** tab:

- **For a visitor**: the price, how many CobbleDollars you have, and a **Buy** button. If you
  already hold a licence, the tab says which gym it is; if you are short, it says how much more you
  need. The server checks the price and your balance again when you click.
- **For the holder**: when the licence expires, and a **Renounce** button, which asks for a second
  click to confirm.

## After a crash

When the server starts, it checks every licence against the gym it names, and **the gym wins**: a
licence whose gym no longer names its player is dropped, a gym naming a holder the licence list
forgot is added to it, and if one player ends up holding two gyms, the second goes vacant. Each fix
is written to the server log. Licences of gyms in a dimension that is not loaded are left alone.

Switching licences off ([Configuration](commands.md#configuration)) stops every vacant gym from
selling its licence. Licences already held stay, and still expire or can be renounced.
