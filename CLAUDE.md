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

## Ren'Py Documentation Quick Reference

Based on [Ren'Py 8.5 Documentation](https://www.renpy.org/doc/html/). Key sections organized by usage frequency.

### 1. Screen Language — `screen` statement syntax

```renpy
screen name(param1, param2="default"):
    tag tag_name          # same tag → replaces previous screen
    modal True            # blocks interaction below
    zorder 100            # layering (higher = on top)
    style_prefix "prefix" # prepended to child style names
    variant "touch"       # platform-specific variant

    default var = value   # screen-local variable
    on "show" action ...  # lifecycle: show/hide/replace/replaced
    use other_screen(param) # embed another screen
```

**Key layout containers**: `fixed`, `frame`, `hbox`, `vbox`, `grid cols rows`, `viewport`, `vpgrid`, `side`

**Key UI elements**: `text`, `textbutton`, `button`, `imagebutton`, `label`, `input`, `bar`, `vbar`, `null`, `timer`, `key`, `drag`, `mousearea`, `nearrect`

**Control flow**: `if/elif/else`, `for i in list`, `python:` (avoid side effects!), `showif` (with ATL appear/show/hide events), `use screen_name:` + `transclude` (slot for caller's children)

**`has` statement**: sets container inside single-child parents (button, frame, window)
```renpy
button:
    has vbox
    text "Line 1"
    text "Line 2"
```

**`use` + `transclude`**: reusable layout pattern
```renpy
screen wrapper():
    frame:
        transclude   # <-- caller's children render here
# Usage:
use wrapper():
    text "I appear inside the frame"
```

**Screen show/hide/call**:
- `show screen name(args)` — persistent until hidden
- `hide screen name` — explicit removal
- `call screen name(args)` — shows, waits for Return(), hides → result in `_return`

### 2. Screen Actions — most commonly used

| Category | Key Actions |
|---|---|
| **Flow** | `Jump(label)`, `Call(label, *args)`, `Return(value)`, `Start(label)`, `MainMenu(confirm=True)`, `Quit(confirm=None)`, `ShowMenu(screen)` |
| **Show/Hide** | `Show(screen)`, `Hide(screen)`, `ShowTransient(screen)`, `ToggleScreen(screen)` |
| **Data** | `SetVariable(name, value)`, `ToggleVariable(name)`, `IncrementVariable(name)`, `SetScreenVariable`, `SetLocalVariable` |
| **File** | `FileAction(slot)`, `FileSave(slot)`, `FileLoad(slot)`, `FileDelete(slot)`, `FilePage(n)`, `QuickSave()`, `QuickLoad()` |
| **Audio** | `Play(channel, file)`, `Stop(channel)`, `SetMixer(mixer, vol)`, `ToggleMute(mixer)` |
| **Focus** | `CaptureFocus(name)`, `ClearFocus(name)`, `GetFocusRect(name)` |
| **Utility** | `Function(callable, *args)`, `Confirm(prompt, yes, no)`, `If(expr, true, false)`, `Notify(msg)`, `OpenURL(url)`, `Screenshot()`, `Scroll(id, dir)` |

**Preference dispatch**: `Preference(name, value)` — one function handles ALL preferences
```renpy
Preference("display", "fullscreen")     # display mode
Preference("text speed", 30)            # CPS
Preference("music volume", 0.5)         # mixer levels
Preference("all mute", "toggle")        # mute toggle
Preference("skip", "seen")              # skip mode
Preference("font size", 1.2)            # accessibility
```

### 3. Style Properties — quick lookup by category

| Category | Key Properties |
|---|---|
| **Position** | `xpos/ypos`, `xalign/yalign` (0.0–1.0 float), `xanchor/yanchor`, `xoffset/yoffset`, `xsize/ysize`, `xmaximum/ymaximum`, `xminimum/yminimum`, `xfill/yfill` (boolean), `area` (x,y,w,h tuple) |
| **Text** | `color`, `size`, `font`, `bold`, `italic`, `underline`, `strikethrough`, `textalign` (0.0 left, 0.5 center, 1.0 right), `line_spacing`, `line_leading`, `first_indent`, `rest_indent`, `outlines` (list of tuples), `kerning`, `slow_cps`, `vertical` |
| **Window** | `background` (displayable or None), `foreground`, `padding` (2 or 4 tuple), `left/right/top/bottom_padding`, `xpadding/ypadding`, `size_group`, `modal` |
| **Button** | `hover_sound`, `activate_sound`, `mouse`, `focus_mask`, `keyboard_focus`, `key_events` |
| **Bar** | `bar_vertical`, `bar_invert`, `bar_resizing`, `left/right/top/bottom_bar`, `base_bar`, `thumb`, `thumb_align`, `thumb_shadow` |
| **Box** | `spacing`, `first_spacing`, `box_reverse`, `box_wrap`, `box_align`, `order_reverse`, `box_justify` |
| **Margin** | `left/right/top/bottom_margin`, `xmargin/ymargin`, `margin` |

**Style application**: `style_prefix "foo"` on container → auto-looks-up `foo_button`, `foo_label`, etc. Override: `style "exact_name"`.

### 4. Special Screen Names — Ren'Py built-ins

| Screen | Parameters | When Shown |
|---|---|---|
| `main_menu` | (none) | Game launch, first screen |
| `say` | `who`, `what` | Every `say` statement — **requires ids**: `"who"`, `"what"`, `"window"` |
| `choice` | `items` (list of MenuEntry) | `menu:` statement |
| `input` | `prompt` | `renpy.input()` — **requires id**: `"input"` on an Input widget |
| `nvl` | `dialogue` (list) | NVL-mode dialogue |
| `notify` | `message` | `renpy.notify()` |
| `confirm` | `message`, `yes_action`, `no_action` | Quit/overwrite/delete confirmations |
| `save` | (none, uses `tag menu`) | Save file selection |
| `load` | (none, uses `tag menu`) | Load file selection |
| `preferences` | (none, uses `tag menu`) | Settings/options |
| `skip_indicator` | (none) | During skip mode |
| `ctc` | `arg` + keywords | Click-to-continue indicator |

### 5. Custom Displayables (Creator-Defined)

```python
init python:
    class MyDisplayable(renpy.Displayable):
        def __init__(self, ...):
            super().__init__()
            # store params
        def render(self, width, height, st, at):
            rv = renpy.Render(width, height)
            canvas = rv.canvas()
            # draw: canvas.rect(color, rect), canvas.polygon(color, points)
            # event handling: canvas.event() for mouse/key bindings
            return rv
        def visit(self):
            return []  # sub-displayables for prediction
```

**Canvas methods** (Ren'Py 8.5): `rect(color, (x,y,w,h))`, `polygon(color, points_list)`, `line(color, start, end, width)`, `circle(color, center, radius)` — NOTE: `border_radius` kwarg is NOT supported; Use polygon-based corner approximation for rounded rects.

### 6. Text Input

`renpy.input(prompt, default="", allow=None, exclude="{}", length=None, pixel_width=None, mask=None)` — shows the `input` screen. The screen must contain an `input` widget with `id "input"`.

**Input widget properties**: `value` (InputValue), `default`, `length`, `pixel_width`, `allow`, `exclude`, `copypaste`, `prefix/suffix`, `changed`, `mask`, `caret_blink`, `multiline`, `action`, `arrowkeys`

### 7. Useful Config Variables (`config.*` — set in `project.rpy`)

| Config | Purpose |
|---|---|
| `config.name`, `config.version` | Project identity |
| `config.window_icon` | Window icon |
| `config.screen_width/height` | Usually set via `gui.init(w, h)` |
| `config.has_autosave` | Enable auto-save (default True) |
| `config.has_quicksave` | Enable quick-save (default False) |
| `config.default_fullscreen` | Start fullscreen |
| `config.window_title` | Window title text |
| `config.main_menu_music` | Music on main menu |

### 8. Python / Ren'Py Integration

- **`default` vs `define`**: `default` vars participate in save/load; `define` is static
- **`init python:`** blocks run at init time (before game starts)
- **`$ python_statement`** — single-line Python in script
- **`python:`** block — multi-line Python
- **Screen scope**: params > `default` > screen-local > global store
- **Data actions**: Use `SetScreenVariable`/`SetLocalVariable` inside screens, `SetVariable` for global store
- **Avoid side effects in screens** — Ren'Py may run screen code multiple times (prediction)

### 9. Full Documentation Map

| Section | Key Topics |
|---|---|
| **Getting Started** | Quickstart, GUI Customization Guide |
| **Ren'Py Language** | Language Basics, Labels & Control Flow, Dialogue, Images, Menus, Python/Conditionals, Audio/Movie/Voice |
| **Text, Displayables, Transforms** | Text, Translation, Displayables, Transforms & Properties, Transitions, Matrixcolor, Layered Images, 3D Stage, Live2D |
| **Customizing Ren'Py** | Styles & Style Properties, Screens/Screen Language, Screen Actions/Values/Functions, Special Screen Names, Config/Preference/Store Variables, Mouse Cursors, Text Shaders |
| **Tools** | Launcher, Developer Tools, Interactive Director, Automated Testing |
| **Other Functionality** | NVL-Mode, Speech Bubbles, Text Input, Side Images, Gallery/Music Room, Drag/Drop, Sprites, Keymap, Achievements, Dialogue History, Splashscreen, Game Lifecycle |
| **Python & Ren'Py** | Statement Equivalents, Save/Load/Rollback, Persistent Data, Advanced GUI, Creator-Defined Displayables/Statements, Custom Text Tags, Character Callbacks, File Access, HTTP Fetch |
| **Building & Platforms** | Building Distributions, Android/iOS/Web/ChromeOS/Raspberry Pi, In-App Purchase, Updater, Gestures |
| **Indices** | Style Property Index, Transform Property Index, Function/Class Index, Reserved Names |
