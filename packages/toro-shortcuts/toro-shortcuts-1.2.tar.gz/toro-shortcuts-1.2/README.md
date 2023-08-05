#### Introduction
The toro-shortcut converts your keyboard shortcut into a customized tag. The tag will contain three
attributes; linux, macos, and windows. The values in the attributes will be the keyboard shortcut
using the symbols of the corresponding OS.

#### Installation
```
pip install toro-shortcuts
```
#### Usage
The markdown syntax will be the keyboard shortcut between two questions marks. A plus sign will be used
to separate the keys. __MOD__ will be used as a generic symbol for both the __ctrl__ and __command__ key.
```
??MOD+A??
```

The produced HTML of the markdown syntax will be:
```
<p><kdb linux="Ctrl+A" macos="⌘A" winodws="Ctrl+A"></kdb></p>
```

#### Conversion

| Markdown        | Windows/Linux | macOS |
|:---------------:|:-------------:|:-----:|
| ??mod??         | Ctrl          | ⌘     |
| ??alt??         | Alt           | ⌥     |
| ??enter??       | Enter         | ↩     |
| ??shift??       | Shift         | ⇧     |
| ??ctrl??        | Ctrl          | ⌃     |
| ??left arrow??  | Left arrow    | ←     |
| ??right arrow?? | Right arrow   | →     |
| ??up arrow??    | Up arrow      | ↑     |
| ??down arrow??  | Down arrow    | ↓     |
| ??tab??         | Tab           | ⇥     |
| ??esc??         | Esc           | ⎋     |
