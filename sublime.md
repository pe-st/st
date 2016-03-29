Sublime Text
============

## Projects and Workspaces

- Projects can have multiple workspaces
- Only Projects should be added to version control
- Projects show the configured folders in the sidebar


## Build Systems

See http://docs.sublimetext.info/en/latest/reference/build_systems.html

- Difference between `cmd` and `shell_cmd`: `cmd` is an array, `shell_cmd` a string. Use whatever is easier to get the quotes right ;-)
- 

## Syntax and Colours

### Scopes

- Display the current Scope with <kbd>Cmd</kbd>-<kbd>Alt</kbd>-<kbd>P</kbd>
- http://sublime-text-unofficial-documentation.readthedocs.org/en/latest/extensibility/syntaxdefs.html
- (Textmate docu): http://manual.macromates.com/en/scope_selectors

### Colour Themes

- Inherited from Textmate
- Reference: http://sublime-text-unofficial-documentation.readthedocs.org/en/latest/reference/color_schemes.html
- Use the *Color Highlighter* package to display the colors inline

## Plugins

- Managed by Package Control
- Listed in alphabetic order


### Advanced New File

- Bound to <kbd>Cmd</kbd>-<kbd>Alt</kbd>-<kbd>N</kbd> (as opposed to <kbd>Cmd</kbd>-<kbd>N</kbd>)
- Let's define a name (with a smart default path) before editing


### GitGutter

- Seems to slow down ST (at least on Windows?)


### Indent XML

Uses <kbd>Cmd</kbd>-<kbd>K</kbd>, <kbd>Cmd</kbd>-<kbd>F</kbd>


### MarkdownEditing

- Default Markdown Syntax doesn't support Github Flavored Markdown
- MarkdownEditing is better than knockdown

### Markdown Preview

- Use it with Command Palette
- Github Parser doesn't work through proxy


### Trailing Spaces

- Use it via *Edit / Trailing Spaces* menu


## Exploration needed

Indent/format code?
Snippets
Build System or Command line...?
Toggle wrapping ("command": "toggle_setting", "args": {"setting": "word_wrap"} ? Menu View/Word wrap)
Expand Selection commands (super+shift+space, super+shift+j, super+shift+a) similar to IJ Extend Selection?
