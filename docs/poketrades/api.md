# For Mod Authors

PokeTrades has a public API in the package `com.shier.poketrades.api`, for mods that want to react to
trades, add their own ask conditions, make their own entities trade, or pay money offers in their own
currency.

!!! warning "Experimental"
    The API is marked `@ApiStatus.Experimental` until the mod's 0.3 milestone. Until 1.0.0, a breaking
    change to it is named in the mod's changelog under the version that makes it.

Everything here runs on the logical server unless it says otherwise. Register from your mod
initialiser, on both sides, before datapacks load.

## Trade events

`PokeTradesEvents.TRADE_PRE` and `TRADE_POST` are Cobblemon observables, used like Cobblemon's own
events:

```kotlin
PokeTradesEvents.TRADE_PRE.subscribe { event ->
    if (event.trader.id == "mymod:grumpy" && event.player.level().isNight) event.cancel()
}
```

- `TRADE_PRE` runs after every check and before anything moves. Cancelling it refuses the trade with
  nothing lost; the player reads that it was cancelled.
- `TRADE_POST` runs once the trade happened: what changed hands moved, and the offer and the history
  are written.

Both carry the `player`, the trader's entity (`npc`), its `TraderDefinition` (`trader`), the
`OfferDefinition` (`offer`), and the Pokémon on each side: `gave` is null when the player pays,
`received` when the trader pays. They run for every offer type. A swap of two Pokémon also posts
Cobblemon's own `TRADE_EVENT_PRE` / `TRADE_EVENT_POST`, with the trader as the other participant, so
a mod that already listens to Cobblemon trades sees these too.

## Ask conditions

`AskConditionTypes.register(id, parser)` adds a condition a datapack writes in an ask as
`{"condition": "<id>", ...}`. The mod's own conditions (`species`, `form`, `gender`, `nature`,
`ability`, `ivs`, `level`, `shiny`, `ball`) are registered the same way, under bare ids; yours goes
under your namespace.

```kotlin
AskConditionTypes.register("mymod:max_level") { reader ->
    MaxLevel(reader.int("max", 1..100))
}

data class MaxLevel(val max: Int) : AskCondition {
    override fun matches(facts: PokemonFacts) = facts.level <= max
    override fun describe(): Component = Component.translatable("mymod.condition.max_level", max)
}
```

A datapack then writes `{"condition": "mymod:max_level", "max": 20}`.

- The parser reads its fields through `ConditionReader` (`string`, `id`, `int`, `choice`, their `opt`
  versions, and `json` for anything else). A missing or wrong value fails the offer with a message
  that names the field, and a key no parser asks about is reported as unknown, so read every key your
  condition has.
- `matches` judges a Pokémon from its `PokemonFacts`: species, forms, gender, nature, ability, IVs,
  level, shiny and ball. `describe` is the line the trade screen and `/poketrades info` show next to
  the pass or fail mark.
- A registered condition counts as one condition toward the [tier](traders.md#tiers) its ask fits.
- The client reads the offers it is sent with the same registry: a client without your condition
  leaves the offer off its screen. Register it on both sides.

## Trader sources

A `TraderSource` says which entities of one kind trade, and as which trader. The mod's Cobblemon NPCs
(`cobblemon_poketrades:npc`), villagers (`cobblemon_poketrades:villager`) and, with Radical Cobblemon
Trainers, its trainers (`cobblemon_poketrades:rct`) are all registered sources. Register yours with
`TraderSources.register(id, source)`:

```kotlin
object GymLeaders : TraderSource {
    override fun traderOf(entity: Entity) = (entity as? GymLeader)?.let { "mymod:gym_${it.type}" }
    override fun tradersIn(level: ServerLevel, box: AABB) = level.getEntitiesOfClass(GymLeader::class.java, box)
}
```

- Your source wires its entity's right-click itself, and calls `TraderSources.open(player, entity)`
  from it on the server. That opens the trade screen, or tells the player the trader is closed or has
  nothing left.
- `tradersIn` feeds the [markers](traders.md#the-marker) over traders with an offer left; the mod
  filters them per player.
- Each entity rolls its offers from `keyOf(entity)` (its UUID by default) the first time anyone uses
  it, and who took which offer is kept under the same key. A source whose entities stand for one
  character returns the same key for each, so they share their offers.
- `isOpenTo(entity, player)` (true by default) hides the trader from a player: no screen, no marker.
- `receive(entity, trader, pokemon)` takes a Pokémon traded to a trader whose destination is `team`;
  false (the default) discards it.

## Currencies

A `CurrencyProvider` pays for money offers: `balance`, `withdraw` (false, with nothing taken, when the
player has less), `deposit`, and `format`, how an amount reads (`1,500 ₽`). Amounts are whole units.
Register it with `Currencies.register(id, provider)`.

Money offers use the first currency registered; with none they are left off every trader. The mod
registers CobbleDollars itself when it is installed.
