Sublime keymaps
===============

## Notation

⌘ : Cmd (sublime-settings: 'super')
⌥ : Option (sublime-settings: 'alt')
S : Shift
C : Ctrl


## Debug Bindings

Set `sublime.log_input(True)` in the Console


## Umbelegungen für Schweizerdeutsche Tastatur

C-<     Show Console (Ctrl-`)
⌘-ä     Indent (⌘-])   [eigentlich ⌘-¨, wegen dead key aber nicht möglich]
⌘-ö     Unindent (⌘-[) [eigentlich ⌘-ü siehe oben]


## Unterschiede zu IntelliJ

| Sublime    | IntelliJ   | action            | original sublime action for IntelliJ key  |
| ---------- | ---------- | ----------------- | ----------------------------------------- |
| ⌘-S-D      | ⌘-D        | duplicate line    | find_under_expand                         |
| ⌘-C-up     | ⌘-S-up     | swap line up      | -                                         |
| ⌘-C-down   | ⌘-S-down   | swap line down    | -                                         |
| ⌥-C-up     | ⌘-up       | scroll line up    | -                                         |
| ⌥-C-down   | ⌘-down     | scroll line down  | -                                         |


## Not to miss

⌘-S-P   Command Palette (e.g. for git commands)
⌘-+     Increase font size
⌘--     Decrease font size

⌘-K, ⌘-U   Uppercase
⌘-K, ⌘-L   Lowercase


### Goto...

⌘-R     Outline view (Goto Symbol)
⌘-P     Show/Filter open files (Goto Anything)
        - without symbol: files
        - @ : symbol (= outline view)
        - # : words

### Multiple Selections

C-S-down/up  Columnar insert (similar to Ctrl-Enter in Emacs)
⌘-S-D        Select current word repeatedly! (⌘-D in Original-Binding)
⌘-C-G        Select all instances of current word (Alt-F3 on Windows)

⌘ + Mouse    Select multiple with the mouse
⌘-⌥ + Mouse  Columnar selection with the mouse


⌘-U          Undo last selection
Esc          Cancel multiple selections
