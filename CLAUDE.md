# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

《光轨》(WOTA) is a Ren'Py visual novel / week-based raising sim about rebuilding a Wota艺 (glowstick dance) club at 北航. The player spends 20 in-game weeks choosing locations, practicing skills, building fame, and triggering character routes. The game uses the Ren'Py engine with Python for logic.

## Project structure

```
game/script/
  core/                   # Core game logic (keep stable, change rarely)
    datastore.rpy         # ALL game variables defined here with `default` keyword
    api.rpy               # Functions that modify variables (in `init python` block)
    gameflow.rpy          # Main game loop: game_start → week_loop → screens/story
  story/
    story.rpy             # Weekly story checks + special/random event triggers
  location/
    practice.rpy          # Location-specific actions (practice, etc.)
  screens/
    map_screen.rpy        # Custom Ren'Py screen for the map/action UI
  script.rpy              # Entry point: character definitions, opening scene → jump game_start
  gui.rpy                 # Ren'Py GUI config (stock template)
  screens.rpy             # Ren'Py system screens - contains map_screen integration
  options.rpy             # Ren'Py options (language, transitions, build config)
game/images/
  bg/                     # Background images (map, stage, lawn, auditorium, etc.)
  sprites/                # Character sprites (sylvie blue/green expressions)
  images.rpy              # Image declarations referencing images/bg/ and images/sprites/
assets/
  icons/                  # Platform icons (ico/icns/svg) + mobile icons (android/ios)
  android.json            # Ren'Py Android build config
  project.json            # Ren'Py build config
  progressive_download.txt
剧本讨论/                 # Design documents (script drafts, character profiles)
```

## Architecture conventions

- **Variable placement**: All game variables MUST be defined in `core/datastore.rpy` using Ren'Py's `default` keyword. Do NOT scatter `default` declarations across files.
- **State mutation**: All functions that modify global state go in `core/api.rpy` — this makes call-site tracking trivial (grep for the function name to find all mutations).
- **`default` vs `define`**: Use `default` for variables that change during gameplay (Ren'Py persists them in saves). Use `define` for constants (weather table, skill pool definitions).
- **Game flow**: `core/gameflow.rpy` drives the main loop. Each week: show map screen → check weekly story → check random events → check special events → loop. Story/location labels are `call`ed from here.
- **Story labels**: `story/story.rpy` has three check labels: `weekly_story_check` (week-number gated), `special_event_check` (condition-gated, e.g. `fame >= 10`), `random_event_check` (RNG-based flavor).
- **Ren'Py compilation**: All `.rpy` files are compiled together at build time — no explicit `import` needed between them.

## Ren'Py development commands

The Ren'Py SDK (`renpy.exe` / `renpy.sh`) must be installed separately (not in this repo).

```bash
# Launch the game for testing
./renpy.sh F:/game/galgame/WOTA          # macOS/Linux
renpy.exe F:\game\galgame\WOTA            # Windows

# Lint all scripts (catches missing labels, bad image refs, etc.)
./renpy.sh F:/game/galgame/WOTA lint

# Build distribution
./renpy.sh F:/game/galgame/WOTA distribute
```

## Key game variables (datastore.rpy)

- `week` (int, starts at 1) — current in-game week
- `fame` (int) — campus fame/知名度
- `person_skill` (int, starts at 18) — personal technique level
- `member_count` (int, starts at 2) — club member count
- `skill_pool` (list of dicts) — available skills with id/name/difficulty/mastery/charm
- `weathers` (list of dicts) — weather types with id/factor/name
- `shahe_unlocked`, `yongman_unlocked` (bool) — map location locks
- `has_recruited`, `has_first_stage` (bool) — group route flags

## Notes

- Godot 相关文件已移至 `temp/` 目录，项目完全基于 Ren'Py。
- `剧本讨论/开发指导.docx` 是早期 AI 生成的项目文档，可能过时。README 和 `core/variables.md` 是更好的参考。
- Design docs in `剧本讨论/` are the source of truth for story and character writing.
- Do NOT commit `.rpyc`/`.rpyb` compiled files, `cache/`, `saves/`, `log.txt`, `errors.txt`, or `traceback.txt` (all in `.gitignore`).
- Ren'Py 构建时图标需放在项目根目录；当前在 `assets/icons/`，构建前需复制回根目录。
