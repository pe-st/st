
- ST : Sublime Text
- IJ : IntelliJ
- na : not applicable (feature not available)
- ok : this a default key binding
- w  : has to be configured on Windows
- m  : has to be configured on Mac


Mac OS X    | Windows          | ST  | IJ  | IJ action                      | ST action                   | Remarks
----------- | ---------------- | --- | --- | ------------------------------ | --------------------------- | -------
⌘-D         | Ctrl-D           | mw  | ok  | duplicate line                 |                             |
⌘-up/d      | Ctrl-up/d        | m   | ok  | scroll line up/d               | scroll_lines                |
⌘-⇧-up/d    | Alt-Shift-up/d   | mw  | ok  | swap/move line up/d            | swap_line_up/d              |
ctrl-⇧-up/d | Ctrl-Shift-up/d  |  w  | mw  | clone caret up/d (Multicursor) | select_lines?               |
⌥-up/d      | Alt-up/d         | ??  | m   | next/prev method               |                             |
⌘-end/h     | Ctrl-end/h       | m   | m   | move caret text end/start      | move_to eof/bof             |
            |                  |     |     |                                |                             |
⌥-Lmouse    | Alt-Lmouse       |  w  | ok  | column select (Multicursor)    |                             |
⌥-⇧-Lmouse  | Alt-Shift-Lmouse | mw  | ok  | add caret (Multicursor)        |                             |
            |                  |     |     |                                |                             |
⌘-⌥-L       | Ctrl-Alt-L       | ??  | ok  | reformat code                  |                             |
⌘-⌥-O       | Ctrl-Alt-O       | ??  | ok  | optimize imports               |                             | not included in reformat code
⌥-Shift-D   | Alt-Shift-D      | ??  | mw  | fix doc comment                |                             |
            |                  |     |     |                                |                             |
⌘-⇧-F7      | Ctrl-Shift-F7    | ??  | ok  | highlight usages in file       |                             | navigate: F3/Shift-F3, exit: Esc
            |                  |     |     |                                |                             |
ctrl-H      | Ctrl-H           | ??  | ok  | type hierarchy                 |                             | switch between class/supertype/subtype hierarchy!
            | Gutter Icons     | ??  | ok  | method hierarchy up/d          |                             |
⌘-⌥-U       | Ctrl-Alt-U       | ??  | ok  | diagram popup                  |                             |
            |                  |     |     |                                |                             |
⌥-Enter     | Alt-Enter        |     | ok  | show intention actions         |                             | quick fixes
