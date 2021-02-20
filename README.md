# LBLML
The Line By Line Markup Language

### How Does it Work?
It is a markup language that goes line by line (hence the name).
When you write a program in LBLML, you write *two* things: a command and
a value (like this: command|value). Sometimes a value can be an open or
closed curly brace, this symbolises that that command will cover multiple
lines. Values that are not curly braces will only have their command cover
that line. If you want to understand more of how it works, try the example
project (text.txt) and run it to see the HTML output.

### List of Commands
- bold | Makes text bold
- italic | Makes text italicised
- underline | Makes text underlined
- strike | Makes text have a strike through it
- h1 | Heading one
- h2 | Heading two
- h3 | Heading three
- h4 | Heading four
- h5 | Heading five
- h6 | Heading six
- title | Gives your project a title
- text | Lets you write text
- unorder | Makes an unordered list
- order | Makes an ordered list
- \- | List element
- link | Hyperlink
- ! | Comment (will not be seen in final HTML output)
