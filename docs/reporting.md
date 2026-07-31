# 🐛 Reporting bugs & ideas

Found a bug, or have an idea? Post it in **[the Discord](https://discord.gg/SwcwXcCN4k)** — that is
the whole process. **You do not need a GitHub account.** A bot turns your post into a tracked issue,
replies in your thread with what it needs from you, and posts back there when it is closed.

One page for all four mods: the process is identical, and the mod-specific detail is in the tabs
below.

1. **You** open a post in the mod's tickets thread and pick a tag.
2. **The bot** reads it within ~10 minutes and files a tracked issue, labelled from your tag.
3. **The bot replies in your thread** saying what it still needs from you, if anything.
4. **shiero** fixes it in a release.
5. **The bot posts back** in your thread when the issue closes. 🎉

## Pick the right tag

The tag you choose decides how the report is handled — and what the bot asks you for. It is the one
thing worth getting right.

| Tag | Use it when | What the bot does |
|---|---|---|
| 🚨 **Crash** | the game closes, freezes or fails to start | jumps the queue; asks for the crash report |
| 🐛 **Bug** | something works, but wrong | asks for versions, loader and steps |
| 💡 **Idea** | you want something that does not exist yet | files it against the roadmap — no logs needed |
| 💬 **Feedback** | an impression, a balance opinion, a "this felt off" | recorded; nothing else needed from you |

## What makes a great report

- **What you did**, **what you expected**, and **what happened** instead.
- The **mod version**, your **loader** (Fabric or NeoForge), and whether you are on a modpack.
- If the game crashed: attach `crash-reports/crash-*.txt`, or `logs/latest.log` if there is no crash
  report. **The stack trace is what turns a hunt into a fix.**
- A screenshot or a short clip, if it is something you can see.

!!! example "A report that gets fixed fast"
    > Placing a picnic table underwater near coral crashes the client. MC 1.21.1, Cobblemon 1.7.3,
    > Picnic 1.26.0, Fabric. Happens every time; crash report attached. Only other furniture mod is
    > Handcrafted.

## Extra detail, per mod

=== "Routes"

    - **Where** it happened: the zone name the mod showed you — a route, an area, a town, or the
      Wild.
    - Whether the world was **generated with this version** of Routes or an older one, since roads
      are baked in at worldgen.
    - For map problems: which map mod (Xaero's Minimap, World Map, JourneyMap) and its version.

=== "Nuzlocke & Soul Link"

    - **Which rule** misbehaved: one catch per zone, permadeath, nicknames, shiny clause, level caps,
      or a Soul Link pairing.
    - **Where you were**: the zone name the mod showed you.
    - For Soul Link: **how many players** were linked, and what each was doing at the time.

    !!! tip "Zone problems are usually Routes problems"
        "One catch per zone" is defined against Routes' zone model — the routes, areas and towns it
        generates **are** the capture zones. If the *zone itself* looks wrong (missing, badly shaped,
        oddly named), that is a Routes report, not a Nuzlocke one.

    !!! warning "Not released yet"
        The Nuzlocke and Soul Link rules currently ship **inside Routes**. Until the split lands,
        report them in the **Routes** tickets thread and mention it is about the Nuzlocke ruleset.

=== "Picnic"

    - Whether it was the **re-roll**, the **social** side (benches, shiny aura, care) or the
      **trainer battles**.
    - What was around the table: biome, other spawners, and whether a modpack tuned the spawn rules.
    - For furniture or model issues, whether **Handcrafted** or **CobbleFurnies** are installed.

=== "Ditto HMs"

    - **Which HM**, and whether it was used as an **active** ability or a **toggle**.
    - Whether you had learned it from a disc or via `/dittohm learn_all`.

    !!! tip "Hunger and cooldowns are configurable"
        Before reporting "this HM costs too much", check
        [Configuration](ditto-hms/configuration.md) — every ability's hunger cost, cooldown and
        power is a server-side slider, so a modpack may have tuned it away from the defaults.

    **Suggesting a new HM?** Those are the most common request, and plenty on the
    [Roadmap](ditto-hms/roadmap.md) started that way. The ones that get built fastest describe: the
    **Pokémon move** it is based on, what it should **do in Minecraft**, and whether it feels like an
    **active** (press to use, costs hunger) or a **toggle** (passive, blocks part of your hunger bar).

## What happens next

Your post becomes an issue labelled from its tag, and the bot replies in the thread so you know it
landed. When the issue is closed, it posts back there — saying whether it was **fixed** or **closed
without a change**, because those are not the same thing and you deserve to know which.

Everyone who reports gets thanked on the mod's community credits page:
[Routes](routes/credits.md) · [Nuzlocke](nuzlocke/credits.md) · [Picnic](picnic/credits.md) ·
[Ditto HMs](ditto-hms/credits.md). 💚
