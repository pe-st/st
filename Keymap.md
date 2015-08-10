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


## Debug Bindings

Set `sublime.log_input(True)` in the Console


## Umbelegungen für Schweizerdeutsche Tastatur

C-<     Show Console (Ctrl-`)
⌘-ä     Indent (⌘-])   [eigentlich ⌘-¨, wegen dead key aber nicht möglich]
⌘-ö     Unindent (⌘-[) [eigentlich ⌘-ü siehe oben]


## Differences to IntelliJ

Sublime keymap has been adapted to match closely IntelliJ

| Sublime    | IntelliJ   | IJ Windows | action                   | original sublime action for IntelliJ key  |
| ---------- | ---------- | ---------- | ------------------------ | ----------------------------------------- |
| ⌘-S-D      | ⌘-D        | C-D        | duplicate line           | find_under_expand                         |
| ⌥-C-up/d   | ⌘-up/d     | C-up/d     | scroll line up/d         | -                                         |
| ⌘-C-up/d   | ⌘-S-up     | A-S-up/d   | swap/move line up/d      | -                                         |
|            | ⌘-⌥-S-up   | C-S-up/d   | swap/move statement up/d | -                                         |
|            | ⌥-up/d     | A-up/d     | next/prev method         | -                                         |
|            | C-⌥-up/d   | C-A-up/d   | next/prev occurrence     | -                                         |
|            | C-⌥-S-up/d | C-A-S-up/d | next/prev change         | -                                         |


## Not to miss

⌘-S-P   Command Palette (e.g. for git commands)
⌘-+     Increase font size
⌘--     Decrease font size

⌘-K, ⌘-U    Uppercase
⌘-K, ⌘-L    Lowercase
            Titlecase? (Edit / Convert Case / Titlecase)

⌘-⌥-  2     Split vertical in panes 
⌘-⌥-S-2     Split horizontal in panes 
⌘-⌥-1       Remove vertical split 

Indent/format code?
Snippets
Markdown preview?
Insert Mode


### Find / Replace

⌘-F         Find
⌘-G         Next
⌘-H         Replace
⌘-S-F       grep (Find in Files)


### Goto...

⌘-R     Outline view (Goto Symbol)
⌘-P     Show/Filter open files (Goto Anything)
        - without symbol: files
        - @ : symbol (= outline view)
        - # : words
        - : : lines


### Multiple Selections

C-S-down/up  Columnar insert (similar to Ctrl-Enter in Emacs)
⌘-S-D        Select current word repeatedly! (⌘-D in Original-Binding)
⌘-C-G        Select all instances of current word (Alt-F3 on Windows)

⌘ + Mouse    Select multiple with the mouse
⌘-⌥ + Mouse  Columnar selection with the mouse


⌘-U          Undo last selection
Esc          Cancel multiple selections
