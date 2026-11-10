# Troubleshooting

If yours is not here, post it in the [Discord](https://discord.gg/SwcwXcCN4k): it files the ticket
for you.

## There is no Gym Manager in a city

- The city has **no gym building**: Lavender and Pallet never have one, and the other cities do not
  always build theirs. `/pokegyms gyms` lists the gyms the server found in your dimension.
- **Cobblemon Cities & Structures is not installed** on the server. Without it PokeGyms finds no
  gyms.
- The spot has not loaded yet. The Gym Manager is placed when its chunk is loaded; walk into the gym.

## /pokegyms gyms says "No gyms recorded"

No Cities & Structures city with a gym has loaded in that dimension yet, or Cities & Structures is
missing. Gyms are found as their cities load, so explore first.

## The game will not start and names a mod

One of the [requirements](getting-started.md#requirements) is missing or older than PokeGyms needs.
The message says which and which version; install that one.

## Right-clicking a Gym Manager says it belongs to no gym

That lectern was placed by hand, not by PokeGyms. Only the Gym Manager standing at a gym's own spot
opens the gym's screen.

## There is no Licence tab

That is expected in this build: no gym sells a licence yet ([Licences](licences.md)).

## The config file did not take my change

It is read when the server starts. On a live server, use `/pokegyms config` instead
([Commands & Configuration](commands.md#pokegyms-config)). If the file is not valid JSON, the server
runs on the defaults and says so in its log.
