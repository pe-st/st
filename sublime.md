Sublime Text
============

## Projects and Workspaces

- Projects can have multiple workspaces
- Only Projects should be added to version control
- Projects show the configured folders in the sidebar

### Add new projects to Project Manager (Plugin)

- Use Project / Project Manager / Add Project


## Build Systems

See http://docs.sublimetext.info/en/latest/reference/build_systems.html

- Difference between `cmd` and `shell_cmd`: `cmd` is an array, `shell_cmd` a string. Use whatever is easier to get the quotes right ;-)

### Some regexes for file_regex

Match `filename:line:column:message` and `filename:line:message` :

    ^([^ ]+?):([0-9]+):([0-9]+(?=[:]))?:? *(.*)

Match `filename(line:column):message` and `filename(line):message` :

    ^([^ ]+?)\(([0-9]+):?((?<=[:])[0-9]+)?\) *: *(.*)

Match `"filename", line` (e.g. `"C:\Daten\src\FO\trunk\fo\ep2\raffl\testclient\RafFlClient.cpp", line 199: error(225)`)

    ^\"([^ ]+?)\", line ([0-9]+)


## Settings

See also http://docs.sublimetext.info/en/latest/customization/settings.html

### Fonts

- Packages/User/Preferences.sublime-settings is not platform specific, so no
  differences between Mac and Windows possible without a plugin
- Platform specific font can be configured with SyntaxMgr, but it's not always picked up upon start
- Default Font on Mac: Menlo (good); best equivalent on PC: Meslo LG S DZ


## Syntax and Colours

### Scopes

- Display the current Scope with <kbd>Cmd</kbd>-<kbd>Alt</kbd>-<kbd>P</kbd>
- http://sublime-text-unofficial-documentation.readthedocs.org/en/latest/extensibility/syntaxdefs.html
- (Textmate docu): http://manual.macromates.com/en/scope_selectors

### Colour Themes

- Inherited from Textmate
- Reference: http://sublime-text-unofficial-documentation.readthedocs.org/en/latest/reference/color_schemes.html
- Use the *Color Highlighter* package to display the colors inline

## Unicode and UTF-8

- Default is UTF-8
- set preference "show_encoding" to true to have the current encoding displayed in the status bar
- change the encoding with "Save with encoding..." or "Reopen with encoding"


## Regex

### Perl (PCRE) Regex

- According to http://docs.sublimetext.info/en/latest/search_and_replace/search_and_replace_overview.html,
  **Sublime Text** uses the Perl Compatible Regular Expressions (PCRE) engine from the Boost library:
  http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/boost_regex/syntax/perl_syntax.html
- Useful! : http://www.regexplanet.com/advanced/perl/index.html

### Ruby (Oniguruma) Regex

- According to https://www.sublimetext.com/docs/3/syntax.html,
  **Sublime Syntax Files** use Ruby regexes (more precisely the Oniguruma Engine):
  https://github.com/kkos/oniguruma/blob/master/doc/RE
- http://www.regular-expressions.info/ruby.html
- Useful: http://rubular.com/

### Multiline Regex

For multiline regexes use the *dotall* modifier `(?s)` to make the dot match newline characters, e.g.

    (?s)^ +88 .*?\.

matches multiline "88 Cobol value definitions"


## Find/Replace in Files

*Where* field examples:

- <project> (not available from the button...)
- <current file>
- <open files>
- <open folders>
- -*.doc
- *.txt


## Console

- Default key mapping is ctrl+backquote
- with Swiss German keyboard I prefer ctrl-<

Show settings:

    s = sublime.load_settings("Preferences.sublime-settings")
    s.get("font_face")


## Plugins

- Managed by Package Control
- Listed in alphabetic order


### Advanced New File

- Bound to <kbd>Cmd</kbd>-<kbd>Alt</kbd>-<kbd>N</kbd> (as opposed to <kbd>Cmd</kbd>-<kbd>N</kbd>)
- Let's define a name (with a smart default path) before editing


### GitGutter

- Seems to slow down ST (at least on Windows?)


### Highlight Build Errors

- Does work, but do you get rid of the highlighting?


### Indent JSON

- not only indent, but also reorders (alphabetically). For this reason I prefer Pretty JSON


### Indent XML

Uses <kbd>Cmd</kbd>-<kbd>K</kbd>, <kbd>Cmd</kbd>-<kbd>F</kbd>


### MarkdownEditing

- Default Markdown Syntax doesn't support Github Flavored Markdown
- MarkdownEditing is better than knockdown

### Markdown Preview

- Use it with Command Palette
- Github Parser doesn't work through proxy


### Pretty JSON

- Format (Pretty Print) just pretty prints (good thing! 'Indent JSON' also reorder, which I hate...)


### Trailing Spaces

- Use it via *Edit / Trailing Spaces* menu


## Exploration needed

Indent/format code?
Snippets
Toggle wrapping ("command": "toggle_setting", "args": {"setting": "word_wrap"} ? Menu View/Word wrap)
Expand Selection commands (super+shift+space, super+shift+j, super+shift+a) similar to IJ Extend Selection?
