<!-- CurseForge description of Keel Vanilla+ (paste in Markdown mode). Summary field: -->
<!-- Vanilla Minecraft, faster and friendlier: measured optimizers plus the quality-of-life mods most packs carry, client-side only. -->

# Keel Vanilla+

**Vanilla Minecraft, faster and friendlier.** The measured optimizers of Keel Performance,
plus the quality-of-life mods that Fabric modpacks carry most. Every one is client-side: no new
blocks, items or recipes, so it joins any vanilla server and your worlds stay vanilla. The
[Modkeel lab](https://modkeel.com) measured what each mod costs before it got in, and the whole
pack is started on a real server and client before each release.

![Keel Vanilla+ against no mods on Minecraft 26.2: frame rate in three scenes](https://raw.githubusercontent.com/Modkeel/packs/main/vanilla-plus/gallery/measured-26.2.png)

[![Modkeel lab](https://img.shields.io/badge/Lab_data-modkeel.com-f08a3c?style=for-the-badge&labelColor=0c131d)](https://modkeel.com/minecraft/) [![Crashed](https://img.shields.io/badge/Crashed-Find_the_mod-f08a3c?style=for-the-badge&labelColor=0c131d)](https://modkeel.com/crashes/diagnose) [![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&labelColor=0c131d&logo=discord&logoColor=white)](https://discord.gg/9MPy4ucDCC)

## What is in it

**Faster** (the Keel Performance base): Sodium, EntityCulling, ImmediatelyFast, MoreCulling,
Lithium, FerriteCore, ModernFix (1.21.1), Dynamic FPS.

**Friendlier:**

| Mod | What it adds |
|---|---|
| AppleSkin | Hunger and saturation on the food bar |
| Mouse Tweaks | Drag and scroll items between inventories |
| Jade | What you are looking at, and its state, at the top of the screen |
| Shulker Box Tooltip | A shulker box's contents when you hover it |
| BetterF3 | A readable, colored debug screen |
| Zoomify | Zoom with a key |
| Skin Layers 3D | Skins' outer layer in 3D |
| Chat Heads | Players' heads next to their chat messages |
| No Chat Reports | Chat stays unsigned, as before 1.19 |
| Mod Menu, Cloth Config, YetAnotherConfigLib, Fabric Language Kotlin, Fabric API | Settings screens and the libraries the mods need |
| [Modkeel Companion](https://www.curseforge.com/minecraft/mc-mods/modkeel) | World copies before mod changes, crash diagnosis |

![In survival with Keel Vanilla+: Jade names the block in the crosshair](https://raw.githubusercontent.com/Modkeel/packs/main/vanilla-plus/gallery/hud-village.png)

**Left out on purpose:** Xaero's Minimap and World Map. Added to this pack on 1.21.1 they took
the terrain frame rate from 524 to 304 FPS (-43%) and 300 mobs on screen from 202 to 155. Every
other mod here cost 0 to 8%.

## Measured on this pack

The whole pack against the same game with no mods, on one PC (GeForce GTX 1650), 1280x720,
render distance 24, no VSync. Median frame rate, two rounds, a no-mods run before and after
every pack run:

![Keel Vanilla+ against no mods on Minecraft 1.21.1](https://raw.githubusercontent.com/Modkeel/packs/main/vanilla-plus/gallery/measured-1.21.1.png)

| Minecraft | Terrain | 300 mobs on screen | 300 mobs behind a wall |
|---|---|---|---|
| 1.21.1 | 524 FPS vs 287 (+83%) | 205 vs 102 (+102%) | 398 vs 84 (+372%) |
| 26.2 | 397 FPS vs 282 (+41%) | 190 vs 117 (+62%) | 324 vs 92 (+254%) |

Faster than vanilla with all the extras on.

## Tested together, every release

Before each release the pack is started on a real dedicated server and a real client that
joins a world, with these exact files from CurseForge. A release ships only when both start and
nothing crashes. Every dependency is checked against the pack first.

## With a safety net: Modkeel Companion

Add your own mods on top, and if one crashes the game, the next start names the mod that most
likely caused it and turns it off in one click. Your world is copied before it ever loads with
a different set of mods. It does not patch the game (no mixins), so it cannot slow it down or
break it. Do not want it? Remove it from the pack's mods; nothing depends on it.

![After a crash: the likely mod and a one-click fix](https://raw.githubusercontent.com/Modkeel/companion/main/images/2-crash.png)

## Versions

| Minecraft | Loader | Mods |
|---|---|---|
| 26.2 | Fabric | 22 |
| 1.21.1 | Fabric | 23 (with ModernFix) |

26.3 comes as soon as every mod has a tested file for it.

## Questions

- **A minimap?** Add one if you want it; the lab measured Xaero's at -43% terrain FPS on this
  pack, so expect a cost.
- **Shaders?** Add Iris on 26.2 (Keel Shaders is that pack).
- **Multiplayer?** Joins any vanilla or Fabric server; nothing needs installing there.
- **Something wrong?** Ask on [Discord](https://discord.gg/9MPy4ucDCC) or
  [open an issue](https://github.com/Modkeel/packs/issues/new?template=pack.yml).

## Credits

Every mod belongs to its authors and is downloaded from its own CurseForge page; this pack only
picks them and tests them together: Sodium and Lithium (CaffeineMC), EntityCulling and Skin
Layers 3D (tr7zw), ImmediatelyFast (RaphiMC), MoreCulling (FX_PR0CESS), FerriteCore
(malte0811), ModernFix (embeddedt), Dynamic FPS (juliand665, LostLuma), AppleSkin (squeek502),
Mouse Tweaks (YaLTeR), Jade (Snownee), Shulker Box Tooltip (MisterPeModder), BetterF3
(cominixo), Zoomify and YetAnotherConfigLib (isXander), Chat Heads (dzwdz), No Chat Reports
(Aizistral), Mod Menu (Prospector), Cloth Config (shedaniel), Fabric API and Fabric Language
Kotlin (FabricMC).

**Made with AI.** The pack was put together, tested and described with Claude (Anthropic's AI),
directed and reviewed by its developer. The numbers come from the Modkeel lab's own runs; the
mods are the work of their authors.
