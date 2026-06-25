# markdown-to-html

Fast Markdown to HTML converter with syntax highlighting and theming.

## Features
- CommonMark compliant
- Syntax highlighting for 50+ languages
- Table and task list support
- Custom CSS themes
- CLI and Python API

## CLI Usage
```bash
md2html input.md -o output.html --theme github
md2html input.md --theme dark --highlight
```

## Python API
```python
from md2html import convert, Theme

html = convert("# Hello World\n\nThis is **bold**.")
html = convert(markdown_text, theme=Theme.GITHUB_DARK)
```

## License
MIT
