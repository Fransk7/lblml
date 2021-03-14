# LBLML
The Line By Line Markup Language

## How Does it Work?
LBLML is a markup language that goes line by line (hence the name).
When you write a program in LBLML, you write ***two*** things: a command and
a value (like this: command|value) separated by a pipe symbol, no spaces. Sometimes a value 
can be an open or closed curly brace, this symbolises that that command will cover multiple
lines. Values that are not curly braces will only have their command cover
that line. If you want to understand more of how it works, try the example
project (text.txt) and run it in the Python program and then look at the outputed HTML file.

## What Does LBLML Transpile To?
LBLML transpiles to HTML.

## List of Commands
| LBLML | HTML | Description |
| --- | --- | --- |
| bold | `<strong>` | Makes text bold |
| italic | `<em>` | Makes text italicised |
| underline | `<u>` | Makes text underlined |
| strike | `<strike>` | Makes text have a strike through it |
| h1 | `<h1>` | Heading one |
| h2 | `<h2>` | Heading two |
| h3 | `<h3>` | Heading three |
| h4 | `<h4>` | Heading four |
| h5 | `<h5>` | Heading five |
| h6 | `<h6>` | Heading six |
| title | `<title>` | Gives your project a title |
| text | `<p>` | Lets you write text |
| unorder | `<ul>` | Makes an unordered list |
| order | `<ol>` | Makes an ordered list |
| \- | `<li>` | List element |
| link | `<a href="URL">URL</a>` | Hyperlink |
| color | `<script>p { color: value; }</script>` | Colours the text |
| bgcolor | `<script>p { background-color: value; }</script>` | Gives the background a colour |
| ! | N/A | Comment (will not be seen in final HTML output) |
