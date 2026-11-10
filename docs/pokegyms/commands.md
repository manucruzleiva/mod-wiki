# Commands & Configuration

Every command is under `/pokegyms`, for **operators** only (permission level 2).

## /pokegyms gyms

Lists every gym the server has found in **your current dimension**, one line each: its coordinates,
its status (`canonical`, `vacant`, or `held by` a player), the city structure it stands in, and how
many of its five marks PokeGyms read (`5/5 markers` is a healthy gym).

Click the coordinates to get a `/tp` to that gym's Gym Manager in your chat box.

## /pokegyms config

Shows and changes every setting on a live server. A change takes effect at once, without a restart,
and is written to the config file so it survives one.

| Command | What it does |
| --- | --- |
| `/pokegyms config` | Lists every feature with its settings. |
| `/pokegyms config licences` | Lists one feature. A value that is not the default shows the default beside it. |
| `/pokegyms config licences enabled <true\|false>` | Switches the whole feature on or off. |
| `/pokegyms config licences <setting> <value>` | Sets a number, within the setting's range. |
| `/pokegyms config licences reset` | Puts the feature back to its defaults, switched on. |

## Configuration

The settings live in `config/cobblemon_pokegyms.json` on the server:

```json
{
  "licences": {
    "enabled": true,
    "price": 25000,
    "expiry_days": 30
  }
}
```

| Setting | Default | Range | What it does |
| --- | --- | --- | --- |
| `licences.enabled` | `true` | | Off: no vacant gym sells its licence. Licences already held stay, and still expire or can be renounced. |
| `licences.price` | `25000` | 0 or more | What a gym's licence costs, in CobbleDollars. |
| `licences.expiry_days` | `30` | 0 to 36,500 | Days a holder can stay offline before their licence ends. `0` keeps a licence for good. |

A setting missing from the file takes its default, and one out of range is pulled into it; the file is
then written back whole, so you always find every setting in it. A file that is not valid JSON is left
as it is, and the server runs on the defaults and says so in its log.

See [Licences](licences.md) for what a licence does.
