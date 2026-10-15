<!-- CurseForge description of Keel Performance (paste in Markdown mode). Summary field: -->
<!-- Vanilla Minecraft, faster: the optimizers the Modkeel lab measured, tested together, with a crash safety net. -->

# Keel Performance

**Vanilla Minecraft, only faster.** Every mod in this pack was measured by the
[Modkeel lab](https://modkeel.com) before it got in, and the whole pack is started on a real
server and client before each release. Nothing here changes how the game plays.

![The same flight over a village with 200 animals, Keel Performance against no mods, live frame rate](https://raw.githubusercontent.com/Modkeel/packs/main/performance/gallery/fps-reel.webp)

![Keel Performance against no mods on Minecraft 26.2: frame rate in three scenes](https://raw.githubusercontent.com/Modkeel/packs/main/performance/gallery/measured-26.2.png)

[![Modkeel lab](https://img.shields.io/badge/Lab_data-modkeel.com-f08a3c?style=for-the-badge&labelColor=0c131d)](https://modkeel.com/minecraft/) [![Crashed](https://img.shields.io/badge/Crashed-Find_the_mod-f08a3c?style=for-the-badge&labelColor=0c131d)](https://modkeel.com/crashes/diagnose) [![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&labelColor=0c131d&logo=discord&logoColor=white)](https://discord.gg/9MPy4ucDCC)

## Why these mods, and not others

Most performance packs collect every optimizer they can find. This one keeps a mod only if the
lab measured it helping, and leaves out the ones that made things worse. Numbers are the lab's,
at render distance 24, against the same game without the mod:

| Mod | What it does | What the lab measured |
|---|---|---|
| [Sodium](https://modkeel.com/mods/sodium) | Rewrites the renderer | Terrain frame rate +34% on 26.2, +102% on 1.21.1 |
| [EntityCulling](https://modkeel.com/mods/entityculling) | Skips mobs and blocks you cannot see | 300 mobs behind a wall: +80% (26.2) to +134% (1.21.1) |
| [ImmediatelyFast](https://modkeel.com/mods/immediatelyfast) | Faster text, items and particles | 300 mobs on screen: +45% on 1.21.1 |
| [MoreCulling](https://modkeel.com/mods/moreculling) | Hides more hidden block faces | Terrain +13% on 1.21.1 |
| [Lithium](https://modkeel.com/mods/lithium) | Faster game logic (singleplayer runs a server too) | Tick time with 400 mobs -52%, redstone -37% |
| [FerriteCore](https://modkeel.com/mods/ferritecore) | Uses less memory | Memory after startup -6% |
| [ModernFix](https://modkeel.com/mods/modernfix) | Faster startup, less memory | 1.21.1 only: no 26.2 file on CurseForge yet |
| Dynamic FPS | Lowers the frame rate while the game is in the background | Saves power and heat, not frames |
| [Mod Menu](https://modkeel.com/mods/modmenu), Cloth Config, Fabric API | Settings screens and the libraries the mods need | |

On 26.2, Sodium + EntityCulling + ImmediatelyFast together measured **+38%** on terrain and
**+306%** with 300 mobs behind a wall.

**Left out on purpose:** C2ME (it cut the client's frame rate by 48% on 26.2), ScalableLux
(faster lighting, but twice the memory after exploring), Krypton and Very Many Players (they
help multiplayer servers, not your game).

## Measured on this pack

The whole pack against the same game with no mods, on one PC (GeForce GTX 1650), 1280x720,
render distance 24, no VSync. Median frame rate, two rounds each, a no-mods run before and
after every pack run:

![Keel Performance against no mods on Minecraft 1.21.1](https://raw.githubusercontent.com/Modkeel/packs/main/performance/gallery/measured-1.21.1.png)

| Minecraft | Terrain | 300 mobs on screen | 300 mobs behind a wall |
|---|---|---|---|
| 1.21.1 | 636 FPS vs 296 (+115%) | 210 vs 103 (+104%) | 437 vs 86 (+407%) |
| 26.2 | 403 FPS vs 281 (+44%) | 190 vs 105 (+80%) | 352 vs 87 (+307%) |

26.2's vanilla renderer is already faster than 1.21.1's, so there is less left to gain on
terrain. Dynamic FPS, Mod Menu and Cloth Config were left out of these runs: Dynamic FPS lowers
the frame rate when the window is not focused, and the other two do not draw anything in game.

## Tested together, every release

Before each release the pack is started on a real dedicated server and a real client that
joins a world, with these exact files from CurseForge. A release ships only when both start and
nothing crashes. Every dependency is checked against the pack first, which is how Cloth Config
got in: MoreCulling needs it.

## With a safety net: Modkeel Companion

The pack includes [Modkeel Companion](https://www.curseforge.com/minecraft/mc-mods/modkeel).
Add your own mods on top, and if one crashes the game, the next start names the mod that most
likely caused it and turns it off in one click. Your world is copied before it ever loads with
a different set of mods. It does not patch the game (no mixins), so it cannot slow it down or
break it. Do not want it? Remove it from the pack's mods; nothing depends on it.

![After a crash: the likely mod and a one-click fix](https://raw.githubusercontent.com/Modkeel/companion/main/images/2-crash.png)

## Versions

| Minecraft | Loader | Mods |
|---|---|---|
| 26.2 | Fabric | 11 |
| 1.21.1 | Fabric | 12 (with ModernFix) |

26.3 comes as soon as every mod has a tested file for it.

## Questions

- **Shaders?** Use Keel Shaders, this pack plus Iris (26.2). On 1.21.1 the Iris that runs
  with this Sodium is still a beta (1.8.14-beta.1); the older release refuses it.
- **Can I add mods?** Yes, that is what it is for. If one crashes the game, the Companion tells
  you which.
- **Servers?** Lithium, FerriteCore and ModernFix also help a server; the client-only mods
  stay off it on their own.
- **Something wrong?** Ask on [Discord](https://discord.gg/9MPy4ucDCC) or
  [open an issue](https://github.com/Modkeel/packs/issues/new?template=pack.yml).

## Credits

Every mod belongs to its authors and is downloaded from its own CurseForge page; this pack only
picks them and tests them together. Sodium and Lithium by JellySquid (CaffeineMC),
EntityCulling by tr7zw, ImmediatelyFast by RaphiMC, MoreCulling by FX_PR0CESS, FerriteCore by
malte0811, ModernFix by embeddedt, Dynamic FPS by juliand665 and LostLuma, Mod Menu by
Prospector, Cloth Config by shedaniel, Fabric API by FabricMC.

**Made with AI.** The pack was put together, tested and described with Claude (Anthropic's AI),
directed and reviewed by its developer. The numbers come from the Modkeel lab's own runs; the
mods are the work of their authors.
