# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

《光轨》(Dahuo Light) is a Ren'Py 8.5.3 visual novel — a weekly life-sim about rebuilding a Wota-艺 (otagei/glowstick dance) club at Beihang University (BUAA). The player, a freshman, has 20 in-game weeks to learn skills, build fame, trigger events, and shape the club's fate and personal story endings.

**Git workflow**: `dev` is the active development branch; `main` is stable/playable. All work happens on `dev` and merges to `main` via PR only when verified runnable. Remote: `BUAA-WotaGal` (GitHub: qingchenling/BUAA-WotaGal).

## Build & Run

- **Requires**: Ren'Py 8.5.3 SDK
- The `game/` directory is the Ren'Py game folder. Place it inside a Ren'Py project (the SDK expects a structure where `game/` sits at the project root, next to `log.txt`).
- Launch from the Ren'Py launcher, or run the SDK directly pointing at the project directory.

## Clean before committing

```bash
# Linux/macOS
bash clean.sh

# Windows
clean.bat
```

This removes `cache/`, `saves/`, and all compiled `.rpyc`/`.rpymc` files. Always run before committing — compiled caches should not be checked in.

## Architecture & File Organization

The project follows a strict separation-of-concerns structure:

### `core/` — Backend / game logic
Code that is NOT specific to the galgame/VN framework. Game systems, data models, and logic that could theoretically be reused outside of Ren'Py belong here.
- **`core/userData.rpy`** — All game state as `default` variables (single source of truth for player stats, map flags, club/personal route flags, skill pool). Mutation functions should be written as an API layer so variable changes are traceable via caller.

### `project.rpy` — Project-level configuration
Overall project parameters: `config.name`, `config.version`, `config.window_icon`, and any other top-level Ren'Py config settings. This is the only file that should set `config.*` values.

### `screen/` — UI screens and styles
**One screen per file.** Each `.rpy` file in `screen/` defines exactly one `screen` statement.

**Style file convention:**
- **`screen/style/GLOBAL.rpy`** — Shared/reusable styles, `gui.init()` parameters, and environment-level GUI settings used across multiple screens. Styles that are common to the entire game go here.
- **`screen/style/<ScreenName>-s.rpy`** — Screen-specific styles used only by a single screen. Naming pattern: the screen's filename with `-s` suffix (e.g., `mainMenu.rpy` → `mainMenu-s.rpy`).

### `story/` — Story/plot content
All narrative content: `label` blocks, character definitions (`define`), image declarations, dialogue, branching logic, and plot flow. This is the "script" of the visual novel.

### `assets/` — Static resources
- `background/` — Scene backgrounds
- `characters/char1/`, `characters/char2/` — Character sprite sets (multiple expressions each)
- Fonts: `XiaoLai-Regular.ttf` (default), `SourceHanSansLite.ttf`

## Ren'Py conventions

- Every `label` must end with a corresponding `return` to close the call stack.
- Use `default` (not `define`) for variables that change during gameplay so they participate in save/load.
- Compiled `.rpyc` files are git-ignored; only `.rpy` source files are committed.
- **File placement rules:**
  - `core/` — backend/game-logic code (not galgame-specific)
  - `project.rpy` — only file for `config.*` settings
  - `screen/` — one screen per file; shared styles in `style/GLOBAL.rpy`, screen-specific styles in `style/<name>-s.rpy`
  - `story/` — all plot, dialogue, character definitions, and narrative flow
