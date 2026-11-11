# Commands & Config

The mod needs no setup. Everything here is for operators who want to change the defaults.

## The config file

`config/cobblemon_defeated_catch_chance.json` is written the first time the mod runs and holds every
setting:

```json
{
  "window": {
    "enabled": true,
    "window_seconds": 60
  },
  "flee": {
    "enabled": true,
    "flee_ticks": 60
  }
}
```

| Setting | Default | Range | What it does |
| --- | --- | --- | --- |
| `window.enabled` | `true` | | Off: a beaten wild Pokémon vanishes as in plain Cobblemon, with no window. A Pokémon already in its window finishes it. |
| `window.window_seconds` | `60` | 5 to 3,600 | How long a beaten Pokémon stays down and catchable, in seconds. |
| `flee.enabled` | `true` | | Off: a missed ball does not wake the Pokémon; it vanishes in a puff within a few seconds. |
| `flee.flee_ticks` | `60` | 1 to 1,200 | How long the run before it vanishes lasts, in ticks (20 ticks = 1 second). |

A missing value takes its default, and one out of range is pulled to the nearest end of its range. The
file is written back whole each time the mod reads or changes it, so every setting is always in it.

!!! warning "A file that is not valid JSON"
    The mod logs a warning, runs on the defaults and **leaves the file as it is**. Changes made with
    `/dcc config` are then not saved until the file is fixed and the server restarted.

## `/dcc config`

Operators only (permission level 2). Every change applies at once, on a live server, and is saved to
the file.

| Command | What it does |
| --- | --- |
| `/dcc config` | Lists both features, whether each is on, and each setting (with its default when it differs). |
| `/dcc config <window\|flee>` | Lists one feature. |
| `/dcc config <window\|flee> enabled <true\|false>` | Switches a whole feature on or off. |
| `/dcc config window window_seconds <5-3600>` | Sets the window's length, in seconds. |
| `/dcc config flee flee_ticks <1-1200>` | Sets the run's length, in ticks. |
| `/dcc config <window\|flee> reset` | Puts the feature back to its defaults and switches it on. |

The command takes numbers only inside each setting's range. A value outside it is refused by the
command itself.
