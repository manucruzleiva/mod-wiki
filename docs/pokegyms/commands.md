# Commands & Configuration

Every command is under `/pokegyms`, for **operators** only (permission level 2).

## /pokegyms gyms

Lists every gym the server has found in **your current dimension**, one line each: its coordinates,
its status (`canonical`, `vacant`, or `held by` a player), the city structure it stands in, and how
many of its five marks PokeGyms read (`5/5 markers` is a healthy gym).

Click the coordinates to get a `/tp` to that gym's Gym Manager in your chat box.

## /pokegyms battles

Lists the [gym battles](gyms.md#gym-battles) running now, one line each: the battle's id, who the
challenger faces (`leader`, `disciple` or `canonical_leader`), and the gym's coordinates and dimension,
as `/pokegyms gyms` lists them. With none running, it says `No gym battles running.`

## /pokegyms config

Shows and changes every setting on a live server. A change takes effect at once, without a restart,
and is written to the config file so it survives one.

| Command | What it does |
| --- | --- |
| `/pokegyms config` | Lists every feature with its settings. |
| `/pokegyms config licences` | Lists one feature. A value that is not the default shows the default beside it. |
| `/pokegyms config licences enabled <true\|false>` | Switches the whole feature on or off. |
| `/pokegyms config licences <setting> <value>` | Sets a number, within the setting's range. |
| `/pokegyms config canonical penalty <value>` | The same for the City-leader battle; `canonical` takes `enabled` and `reset` like `licences`. |
| `/pokegyms config leader enabled <true\|false>` | Opens or closes [team registration](gyms.md#registering-your-team); `leader` has no numbers, and takes `reset` too. |
| `/pokegyms config vault <setting> <value>` | Sets `penalty_min` or `penalty_max` of the [gym vault](vault.md); `vault` takes `enabled` and `reset` too. |
| `/pokegyms config winner_share <setting> <value>` | Sets `percent` of the [winner's share](vault.md#winners-share) of the vault; `winner_share` takes `enabled` and `reset` too. |
| `/pokegyms config rematch <setting> <value>` | Sets `cooldown_minutes` of the [rematch cooldown](gyms.md#rematch-cooldown); `rematch` takes `enabled` and `reset` too. |
| `/pokegyms config scaling enabled <true\|false>` | Switches [level scaling](gyms.md#level-scaling), of gym leaders and RCT trainers, on or off; `scaling` has no numbers, and takes `reset` too. |
| `/pokegyms config evolution enabled <true\|false>` | Switches the [evolution stage](gyms.md#level-scaling) of scaled teams on or off; needs `scaling` on, `evolution` has no numbers, and takes `reset` too. |
| `/pokegyms config medals enabled <true\|false>` | Switches the [medal](gyms.md#medals) for beating a player leader on or off; `medals` has no numbers, and takes `reset` too. |
| `/pokegyms config badges enabled <true\|false>` | Switches the [mainline badge](gyms.md#mainline-badges) for beating a City leader on or off; `badges` has no numbers, and takes `reset` too. |
| `/pokegyms config disciples enabled <true\|false>` | Switches [disciples](gyms.md#disciples) on or off; `disciples` has no numbers, and takes `reset` too. |
| `/pokegyms config city_disciples enabled <true\|false>` | Switches the [City disciples](gyms.md#city-disciples) on or off; `city_disciples` has no numbers, and takes `reset` too. |
| `/pokegyms config takeover <setting> <value>` | Sets `fee` of a [gym takeover](gyms.md#taking-over-a-gym); `takeover` takes `enabled` and `reset` too. |
| `/pokegyms config vault_split enabled <true\|false>` | Switches the [vault split](vault.md#splitting-the-vault) among leader and disciples on or off; `vault_split` has no numbers, and takes `reset` too. |
| `/pokegyms config roster enabled <true\|false>` | Switches the [Roster tab](gyms.md#challenging-a-gym) for challengers on or off; `roster` has no numbers, and takes `reset` too. |
| `/pokegyms config dialogue <setting> <value>` | Sets `max_length` of a [leader's line](gyms.md#leader-dialogue); `dialogue` takes `enabled` and `reset` too. |
| `/pokegyms config licences reset` | Puts the feature back to its defaults, switched on. |

## Configuration

The settings live in `config/cobblemon_pokegyms.json` on the server:

```json
{
  "licences": {
    "enabled": true,
    "price": 25000,
    "expiry_days": 30
  },
  "canonical": {
    "enabled": true,
    "penalty": 1000
  },
  "leader": {
    "enabled": true
  },
  "vault": {
    "enabled": true,
    "penalty_min": 100,
    "penalty_max": 10000
  },
  "rematch": {
    "enabled": true,
    "cooldown_minutes": 60
  },
  "scaling": {
    "enabled": true
  },
  "evolution": {
    "enabled": true
  },
  "medals": {
    "enabled": true
  },
  "badges": {
    "enabled": true
  },
  "winner_share": {
    "enabled": true,
    "percent": 10
  },
  "disciples": {
    "enabled": true
  },
  "city_disciples": {
    "enabled": true
  },
  "takeover": {
    "enabled": true,
    "fee": 10000
  },
  "vault_split": {
    "enabled": true
  },
  "roster": {
    "enabled": true
  },
  "dialogue": {
    "enabled": true,
    "max_length": 120
  }
}
```

| Setting | Default | Range | What it does |
| --- | --- | --- | --- |
| `licences.enabled` | `true` | | Off: no vacant gym sells its licence. Licences already held stay, and still expire or can be renounced. |
| `licences.price` | `25000` | 0 or more | What a gym's licence costs, in CobbleDollars. |
| `licences.expiry_days` | `30` | 0 to 36,500 | Days a holder can stay offline before their licence ends. `0` keeps a licence for good. |
| `canonical.enabled` | `true` | | Off: City gym leaders take no challenges. Battles already running finish, and a loss still costs the penalty. |
| `canonical.penalty` | `1000` | 0 or more | What losing to a City leader costs, in CobbleDollars, and the least a challenger must carry to start. It is destroyed, never paid to anyone. |
| `leader.enabled` | `true` | | Off: no holder can register or replace their gym's team. Teams already registered stay, with their leader. |
| `vault.enabled` | `true` | | Off: no player leader charges a penalty and no challenger needs one. Vaults keep their money, can still be withdrawn, and are still paid out when a licence ends. |
| `vault.penalty_min` | `100` | 0 or more | The least a holder may set as their gym's penalty, in CobbleDollars. A new holder starts on it. |
| `vault.penalty_max` | `10000` | 0 or more | The most a holder may set as their gym's penalty. A range given the wrong way round counts from its smaller end. |
| `rematch.enabled` | `true` | | Off: a challenger may challenge a player leader again at once. Finished challenges are still recorded, so switching it back on counts them. |
| `rematch.cooldown_minutes` | `60` | 0 to 525,600 | Minutes a challenger waits after a finished challenge, won or lost, before challenging that gym's leader again. `0` means no wait. |
| `scaling.enabled` | `true` | | Off: gym leaders' and RCT trainers' teams battle at the levels they were registered at, not at the challenger's. Battles already running keep theirs. |
| `evolution.enabled` | `true` | | Off: a scaled team keeps its registered species instead of taking the evolution stage of its new level. Needs `scaling` on. |
| `medals.enabled` | `true` | | Off: beating a player leader gives no medal. Medals already given stay. |
| `badges.enabled` | `true` | | Off: beating a City leader gives no badge. Badges already given stay. |
| `winner_share.enabled` | `true` | | Off: beating a player leader takes nothing from the vault. |
| `winner_share.percent` | `10` | 0 to 100 | The share of the gym's vault the winner takes, rounded down. `0` takes nothing. |
| `disciples.enabled` | `true` | | Off: a holder cannot invite, and an invited player cannot accept or register. Disciples already there stay, and the holder can still remove them. |
| `city_disciples.enabled` | `true` | | Off: City gyms put no RCT disciples out and their leader is challenged directly. The ones already chosen stay saved and stand again when it is back on. |
| `takeover.enabled` | `true` | | Off: nobody can take a held gym over. Gyms already taken stay as they are. |
| `takeover.fee` | `10000` | 0 or more | What taking a gym over costs, in CobbleDollars. It is destroyed, never paid to anyone. |
| `vault_split.enabled` | `true` | | Off: the whole vault goes to the leader and no share can be set. The shares already set are kept for when it is back on. |
| `roster.enabled` | `true` | | Off: challengers get no Roster tab. Clicking a trainer still challenges it, in the same order. |
| `dialogue.enabled` | `true` | | Off: gym leaders and disciples say nothing and the battle starts at once. Saved lines are kept. |
| `dialogue.max_length` | `120` | 1 to 256 | The longest a leader's line may be, in characters. A longer line is refused and nothing is saved. |

A setting missing from the file takes its default, and one out of range is pulled into it; the file is
then written back whole, so you always find every setting in it. A file that is not valid JSON is left
as it is, and the server runs on the defaults and says so in its log.

See [Licences](licences.md) for what a licence does.
