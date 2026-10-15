<!-- CurseForge description of Keel Shaders (paste in Markdown mode). Summary field: -->
<!-- Shaders on vanilla Minecraft: Iris on the optimizers the Modkeel lab measured, tested together, with a crash safety net. -->

# Keel Shaders

**Shaders on vanilla Minecraft, on a measured base.** This is
[Keel Performance](https://www.curseforge.com/minecraft/modpacks/keel-performance) plus
[Iris](https://www.curseforge.com/minecraft/mc-mods/irisshaders): every optimizer in it was
measured by the [Modkeel lab](https://modkeel.com) before it got in, and the whole pack is
started on a real server and client before each release. It starts with
[Complementary Reimagined](https://www.complementary.dev/) already on, so the first world you
open already has the light, water and sky of a shader; nothing here changes how the game plays.

![The same village at sunset, without shaders and with Keel Shaders](https://raw.githubusercontent.com/Modkeel/packs/main/shaders/gallery/before-after.jpg)

[![Modkeel lab](https://img.shields.io/badge/Lab_data-modkeel.com-f08a3c?style=for-the-badge&labelColor=0c131d)](https://modkeel.com/minecraft/) [![Crashed](https://img.shields.io/badge/Crashed-Find_the_mod-f08a3c?style=for-the-badge&labelColor=0c131d)](https://modkeel.com/crashes/diagnose) [![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&labelColor=0c131d&logo=discord&logoColor=white)](https://discord.gg/9MPy4ucDCC)

## What is in it

| Mod | What it does |
|---|---|
| [Complementary Reimagined](https://www.complementary.dev/) | The shader pack, on from the first start: light, shadows, water, sky, still vanilla in style |
| [Iris](https://modkeel.com/mods/iris) | Loads shader packs (OptiFine format) on top of Sodium |
| [Sodium](https://modkeel.com/mods/sodium) | Rewrites the renderer |
| [EntityCulling](https://modkeel.com/mods/entityculling) | Skips mobs and blocks you cannot see |
| [ImmediatelyFast](https://modkeel.com/mods/immediatelyfast) | Faster text, items and particles |
| [MoreCulling](https://modkeel.com/mods/moreculling) | Hides more hidden block faces |
| [Lithium](https://modkeel.com/mods/lithium) | Faster game logic (singleplayer runs a server too) |
| [FerriteCore](https://modkeel.com/mods/ferritecore) | Uses less memory |
| Dynamic FPS | Lowers the frame rate while the game is in the background |
| [Mod Menu](https://modkeel.com/mods/modmenu), Cloth Config, Fabric API | Settings screens and the libraries the mods need |
| [Modkeel Companion](https://www.curseforge.com/minecraft/mc-mods/modkeel) | World copies before mod changes, crash diagnosis |

![A pillager outpost in the snow at dusk](https://raw.githubusercontent.com/Modkeel/packs/main/shaders/gallery/outpost-dusk.jpg)

Rather another shader, or none? Options > Video Settings > Shader Packs: pick another (drop its
zip in the shaderpacks folder) or turn shaders off.

## Measured on this pack

The whole pack, with shaders off, against the same game with no mods, on one PC (GeForce GTX
1650), 1280x720, render distance 24, no VSync. Median frame rate, two rounds, a no-mods run
before and after every pack run:

| Minecraft | Terrain | 300 mobs on screen | 300 mobs behind a wall |
|---|---|---|---|
| 26.2 | 380 FPS vs 284 (+33%) | 182 vs 105 (+74%) | 342 vs 85 (+303%) |

With a shader pack on, the frame rate depends on the shader and the graphics card far more than
on any mod; the headroom above is what the shader gets to spend.

## Tested together, every release

Before each release the pack is started on a real dedicated server and a real client that
joins a world, with these exact files from CurseForge. A release ships only when both start and
nothing crashes.

## With a safety net: Modkeel Companion

Add your own mods on top, and if one crashes the game, the next start names the mod that most
likely caused it and turns it off in one click. Your world is copied before it ever loads with
a different set of mods. It does not patch the game (no mixins), so it cannot slow it down or
break it. Do not want it? Remove it from the pack's mods; nothing depends on it.

![After a crash: the likely mod and a one-click fix](https://raw.githubusercontent.com/Modkeel/companion/main/images/2-crash.png)

## Versions

| Minecraft | Loader | Mods |
|---|---|---|
| 26.2 | Fabric | 12 + Complementary Reimagined |

1.21.1 comes when Iris has a release (not a beta) there that runs with Sodium 0.8; 26.3 as soon
as every mod has a tested file for it.

## Questions

- **Too slow on my PC?** In Shader Packs > Shader Pack Settings, Complementary has a profile
  setting: Low or Potato runs on most graphics cards. Lighter packs (MakeUp - Ultra Fast) work
  too.
- **Another shader pack?** Any OptiFine-format pack Iris supports.
- **Can I add mods?** Yes. If one crashes the game, the Companion tells you which.
- **Something wrong?** Ask on [Discord](https://discord.gg/9MPy4ucDCC) or
  [open an issue](https://github.com/Modkeel/packs/issues/new?template=pack.yml).

## Credits

Every mod belongs to its authors and is downloaded from its own CurseForge page; this pack only
picks them and tests them together. Complementary Reimagined by EminGT
([complementary.dev](https://www.complementary.dev/)), included unmodified through CurseForge
under its license; a problem with it in this pack is ours to fix, so report it to us first.
Iris by coderbot and IMS, Sodium and Lithium by JellySquid
(CaffeineMC), EntityCulling by tr7zw, ImmediatelyFast by RaphiMC, MoreCulling by FX_PR0CESS,
FerriteCore by malte0811, Dynamic FPS by juliand665 and LostLuma, Mod Menu by Prospector, Cloth
Config by shedaniel, Fabric API by FabricMC.

**Made with AI.** The pack was put together, tested and described with Claude (Anthropic's AI),
directed and reviewed by its developer. The numbers come from the Modkeel lab's own runs; the
mods are the work of their authors.
