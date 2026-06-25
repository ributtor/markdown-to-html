"""Core Markdown to HTML conversion."""
import re
from enum import Enum
from typing import Optional

class Theme(Enum):
    DEFAULT = "default"
    GITHUB = "github"
    GITHUB_DARK = "github-dark"
    MINIMAL = "minimal"

def _convert_headers(text: str) -> str:
    for i in range(6, 0, -1):
        pattern = r"^" + "#" * i + r"\s+(.+)$"
        text = re.sub(pattern, f"<h{i}>\\1</h{i}>", text, flags=re.MULTILINE)
    return text

def _convert_emphasis(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text

def _convert_links(text: str) -> str:
    text = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', text)
    return text

def _convert_lists(text: str) -> str:
    lines = text.split("\n")
    result = []
    in_list = False
    for line in lines:
        if re.match(r"^[\-\*]\s+", line):
            if not in_list:
                result.append("<ul>")
                in_list = True
            content = re.sub(r"^[\-\*]\s+", "", line)
            result.append(f"  <li>{content}</li>")
        else:
            if in_list:
                result.append("</ul>")
                in_list = False
            result.append(line)
    if in_list:
        result.append("</ul>")
    return "\n".join(result)

def _wrap_html(body: str, theme: Theme) -> str:
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Document</title></head>
<body class="theme-{theme.value}">{body}</body>
</html>"""

def convert(markdown: str, theme: Theme = Theme.DEFAULT, full_page: bool = False) -> str:
    html = markdown
    html = _convert_headers(html)
    html = _convert_emphasis(html)
    html = _convert_links(html)
    html = _convert_lists(html)
    html = html.replace("\n\n", "</p><p>")
    if full_page:
        html = _wrap_html(html, theme)
    return html
