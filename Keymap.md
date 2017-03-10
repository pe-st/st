Sublime keymap
==============

## Notation

⌘ : Cmd (sublime-settings: 'super', on Windows often Ctrl)
⌥ : Option (sublime-settings: 'alt')
S : Shift
C : Ctrl
A : Alt (Windows)

### Differences Mac - Windows

- ⌘ is on Windows Ctrl if not noted otherwise
- toggle_overwrite is 'insert' on Windows and ⌘-⌥-O on OSX


## How to Debug Bindings

- Set `sublime.log_input(True)` in the Console to see the key
- Set `sublime.log_commands(True)` to see the command


## Function Keys

F2  : bookmarks
F3  : find next (Windows)
F4  : next/prev result
F5  : sorting (Mac)
F6  : spell checking
F7  : build
F9  : sorting (Windows)
F11 : Fullscreen / Distraction Free (Windows)
F12 : lookup definition


## Umbelegungen für Schweizerdeutsche Tastatur

⌘-7     Comment
C-<     Show Console (Ctrl-`)
⌘-ä     Indent (⌘-])   [eigentlich ⌘-¨, wegen dead key aber nicht möglich]
⌘-ö     Unindent (⌘-[) [eigentlich ⌘-ü siehe oben]
⌘-S-1   increase_font_size (⌘-+)


## Differences to IntelliJ

Sublime keymap has been adapted to match closely IntelliJ

| Sublime    | IntelliJ   | Subl Win   | IJ Windows | action                   | conflicting sublime action  | resolution                   |
| ---------- | ---------- | ---------- | ---------- | ------------------------ | --------------------------- | ---------------------------- |
| ⌘-S-D      | ⌘-D        | C-S-D      | C-D        | duplicate line           | find_under_expand           | use IJ                       |
| ⌥-C-up/d   | ⌘-up/d     | C-up/d     | C-up/d     | scroll line up/d         | move_to bof/eof             |                              |
| ⌘-C-up/d   | ⌘-S-up/d   | C-S-up/d   | A-S-up/d   | swap/move line up/d      | -                           | use IJ                       |
|            | ⌘-⌥-S-up/d |            | C-S-up/d   | swap/move statement up/d | select_lines (clone caret)  | clone caret                  |
|            | ⌥-up/d     |            | A-up/d     | next/prev method         | -                           |                              |
|            | C-⌥-up/d   |            | C-A-up/d   | next/prev occurrence     | scroll_lines                |                              |
|            | C-⌥-S-up/d |            | C-A-S-up/d | next/prev change         | -                           |                              |
| ⌘-up/d     | ⌘-end/h    |            |            | end/start of text        | -                           | use IJ                       |
| ⌥-Lmouse   | ⌥-Lmouse   |            |            | column select            | -                           |                              |
| ⌘-⌥-Lmouse | ⌥-S-Lmouse |            |            | add caret                | -                           | use IJ                       |
| C-S-up/d   | -          |            |            | clone caret up/d         | -                           | use Sublime                  |
| Cmd-i      | n/a        | C-i        | n/a        | incr find                |                             | just use find                |
| Cmd-S-i    | n/a        | C-S-i      | n/a        | incr find reverse        |                             | just use find                |
| Cmd-f      | Cmd-f      | C-f        | C-f        | find                     |                             |                              |
|            | Cmd-S-F7   |            | C-S-F7     | highlight                |                             | 'find under' is close        |
| Cmd-g      | F3         | F3         | F3         | find next                |                             |                              |
| Cmd-S-g    | S-F3       | S-F3       | S-F3       | find pref                |                             |                              |
| Cmd-Alt-g  |            | C-F3       |            | find under               |                             |                              |
| Cmd-A-S-g  |            | C-S-F3     |            | find under prev          |                             |                              |
| Cmd-ctrl-g |            | A-F3       |            | find under all           |                             |                              |
| Cmd-S-f    | ctrl-S-f   | C-S-f      | C-S-f      | find in files            |                             |                              |
| Cmd-e      |            | C-e        |            | slurp find               |                             |                              |
| Cmd-S-e    |            | C-S-e      |            | slurp replace            |                             |                              |
| Cmd-Alt-f  | Cmd-r      | C-h        | C-r        | replace                  | goto @ (symbol, outline)    | use IJ, C-F12 instead of C-r |
| Cmd-Alt-e  |            | C-S-h      |            | replace next             |                             |                              |
| Cmd-S-a    |            | C-S-a      |            | find action (palette)    | expand_selection to tag     |                              |
| Cmd-r      | Cmd-F12    | C-r        | C-F12      | file structure           |                             | use IJ                       |

https://www.jetbrains.com/idea/help/multicursor.html

Go Class (Ctrl-N in Jetbrains) : C-S-R (goto_symbol_in_project)
Go File (C-S-N in Jetbrains) : C-P ({"overlay": "goto", "show_files": true})
Go Declaration (C-B in Jetbrains) : F12 (goto_definition)


## Not to miss

⌘-S-P   Command Palette (e.g. for git commands)
⌘-+     Increase font size

⌘-K, ⌘-U    Uppercase
⌘-K, ⌘-L    Lowercase
            Titlecase? (Edit / Convert Case / Titlecase)


### Windows and Panes

⌘-⌥-  2     Split vertical in panes
⌘-⌥-S-2     Split horizontal in panes
⌘-⌥-1       Remove vertical split

⌘-K, ⌘-down Split vertical (Origami)
⌘-K, ⌥-down Clone File (new view) to lower pane


### Goto...

⌘-R     Outline view (Goto Symbol)
⌘-P     Show/Filter open files (Goto Anything)
        - without symbol: files
        - @ : symbol (= outline view)
        - # : words
        - : : lines


### Multiple Selections

C-S-down/up  Columnar insert (similar to Ctrl-Enter in Emacs)(C-A-up/d on Windows)
⌘-S-D        Select current word repeatedly! (⌘-D in Original-Binding)
⌘-C-G        Select all instances of current word (Alt-F3 on Windows)

⌘ + Mouse    Select multiple with the mouse
⌘-⌥ + Mouse  Columnar selection with the mouse


⌘-U          Undo last selection
Esc          Cancel multiple selections
