# Keel modpacks

The source of the Keel modpacks by [Modkeel](https://modkeel.com): which mods each pack carries,
the exact files it was last built from, and what was verified before release. Report a problem
with a pack here: [open an issue](https://github.com/Modkeel/packs/issues/new?template=pack.yml).

| Pack | Minecraft | Where |
|---|---|---|
| Keel Performance | 1.21.1, 26.2 (Fabric) | [CurseForge](https://www.curseforge.com/minecraft/modpacks/keel-performance) |
| Keel Shaders | 26.2 (Fabric) | [CurseForge](https://www.curseforge.com/minecraft/modpacks/keel-shaders) |
| Keel Vanilla+ | 1.21.1, 26.2 (Fabric) | [CurseForge](https://www.curseforge.com/minecraft/modpacks/keel-vanilla) |
| Keel: Better Structures | 26.2 (Fabric) | [Modrinth](https://modrinth.com/modpack/eV8jcYlQ) |

Every pack ships the [Modkeel Companion](https://github.com/Modkeel/companion), which backs up
your worlds when the mod set changes and names the mod behind a crash. A problem with the
Companion itself goes to [its own tracker](https://github.com/Modkeel/companion/issues).

## What each folder holds

- `pack.toml`: the pack's definition: name, version, Minecraft versions, loader, its mods and
  why some are left out.
- `lock-<minecraft>.json` / `lock.json`: the exact file of every mod the last build used.
- `verified-<minecraft>.json` / `verified.json`: what was checked on that build (server and
  client start, the mod set loaded) before it was released.
- `curseforge.md` / `modrinth.md`: the store description.
- `icon.png`, `gallery/`: store images.

The packs are built and tested by Modkeel's own tooling; this repository is a read-only mirror
of it, updated with each change. Pull requests are welcome as suggestions, but changes land
through the mirror rather than by merging here.

## License

The pack definitions here are MIT ([LICENSE](LICENSE)). The mods each pack downloads keep their
own authors' licenses; no mod files are stored in this repository.
