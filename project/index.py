"""

    Creating a Simple Website with Python 🐍
    Github :: PCabralSoftware - 2K18 - Twitter :: @pedrogcabral

"""

# Import DOM
from browser import document
from browser import html

# Navigation
nav = html.DIV('Python 🐍', Class="nav")

# Content
cnt = html.DIV('You can do really awesome stuff using a nice slack!', Class="content")

# Footer
ftr = html.DIV('Made with luv by: Cabral', Class="footer")

# Push 
document <= [nav, cnt, ftr]