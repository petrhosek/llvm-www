#!/usr/bin/env python3
"""
fix_syntax_errors.py

Corrects HTML syntax errors across the repository so files can be parsed
by Prettier's HTML5 parser.
"""

import glob
import os
import re


def fix_file(path: str, transformer):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        original = f.read()
    updated = transformer(original)
    if updated != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(updated)


def universal_syntax_fixes(content: str) -> str:
    # 1. Normalize void </br> end tags to <br>
    content = re.sub(r"</br\s*>", "<br>", content, flags=re.IGNORECASE)

    # 2. Fix unquoted URLs in href attributes (e.g., <a href=http://example.com>)
    content = re.sub(
        r'<a\s+href=http([^>\s]+)>',
        r'<a href="http\1">',
        content,
        flags=re.IGNORECASE,
    )

    # 3. Fix unclosed quotes in href values
    content = re.sub(
        r'href=""?([^\s>"\']+)>',
        r'href="\1">',
        content,
    )
    return content


# Apply universal regex fixes across all HTML files
for filepath in glob.glob("**/*.html", recursive=True):
    if "node_modules" in filepath:
        continue
    fix_file(filepath, universal_syntax_fixes)

# Specific mismatched tag case fixes (<A> -> <a>, <Li> -> <li>, <P> -> <p>)
fix_file("Users.html", lambda c: re.sub(r"<A\b", "<a", c, flags=re.I))
fix_file("devmtg/2007-05/index.html", lambda c: re.sub(r"<A\b", "<a", c))
fix_file("devmtg/2010-11/index.html", lambda c: re.sub(r"<A\b", "<a", c))
fix_file("devmtg/2012-11/index.html", lambda c: re.sub(r"<A\b", "<a", c))
fix_file(
    "devmtg/2018-10/talk-abstracts.html",
    lambda c: c.replace("<Li>", "<li>").replace("<P>", "<p>"),
)

# Specific misnested or unclosed tag corrections
fix_file(
    "devmtg/2011-11/index.html",
    lambda c: c.replace(
        "LunarGLASS: A LLVM-based shader compiler stack</b>",
        "LunarGLASS: A LLVM-based shader compiler stack</a></b>",
    ).replace(
        "Symbolic Testing of OpenCL Code</b>",
        "Symbolic Testing of OpenCL Code</a></b>",
    ),
)
fix_file(
    "devmtg/2013-04/index.html",
    lambda c: c.replace("<h3></div>", "</h3></div>").replace(
        "  <t\n    <td>Victoria Caparros</td>",
        "  <tr>\n    <td>Victoria Caparros</td>",
    ),
)
fix_file(
    "devmtg/2013-11/index.html",
    lambda c: c.replace("</td></td></tr>", "</td></tr>")
    .replace(
        '<td><a href="#talk14"><b>PGO in LLVM: Status and Current Work</a></b>',
        '<td><b><a href="#talk14">PGO in LLVM: Status and Current Work</a></b>',
    )
    .replace(
        '<td><a href="#bof7"><b>BOF: JIT & MCJIT</a></b>',
        '<td><b><a href="#bof7">BOF: JIT & MCJIT</a></b>',
    ),
)
fix_file(
    "devmtg/2015-10/index.html",
    lambda c: c.replace(
        '<a href="http://www.quicinc.com">QuIC</a></h1>',
        '<a href="http://www.quicinc.com">QuIC</a>',
    )
    .replace(
        "<i>Serge Guelton, <i>Quarkslab</i>",
        "Serge Guelton, <i>Quarkslab</i>",
    )
    .replace(
        "Adam Nemet - Apple Inc.</i><br>", "Adam Nemet - Apple Inc.<br>"
    ),
)
fix_file(
    "devmtg/2017-10/index.html",
    lambda c: c.replace(
        "Ramakrishna Upadrasta</i><br>", "<i>Ramakrishna Upadrasta</i><br>"
    ).replace(
        '<p>To contact the organizer please email <a'
        ' href="mailto:tanyalattner@llvm.org">Tanya Lattner</a>.</p>\n</div>',
        '<p>To contact the organizer please email <a'
        ' href="mailto:tanyalattner@llvm.org">Tanya Lattner</a>.</p>',
    ),
)
fix_file(
    "devmtg/2021-11/index.html",
    lambda c: c.replace("Registration</b></a>", "Registration</a></b>"),
)
fix_file(
    "GitHubMigrationStatus.html",
    lambda c: c.replace(
        '<a href="https://reviews.llvm.org/D67772">D67772</td>',
        '<a href="https://reviews.llvm.org/D67772">D67772</a></td>',
    ),
)
fix_file(
    "RandomBoxes/002-LLVM-TV.html",
    lambda c: c.replace('height=129">', 'height="129">'),
)
fix_file(
    "RandomBoxes/007-Bugpoint.html",
    lambda c: c.replace('height=120">', 'height="120">').replace(
        'height=119">', 'height="119">'
    ),
)
