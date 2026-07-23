#!/usr/bin/env python3
"""
convert_p_wrappers.py

Iteratively identifies Prettier HTML5 `Unexpected closing tag "p"` errors
and converts the surrounding `<p ...>` and `</p>` wrapper around block
elements into matching `<div ...>` and `</div>` tags.
"""

import glob
from multiprocessing import Pool
import os
import re
import subprocess

BLOCK_TAGS = {
    "<ul",
    "<ol",
    "<table",
    "<h1",
    "<h2",
    "<h3",
    "<h4",
    "<div",
    "<dl",
    "<pre",
    "<hr",
    "<blockquote",
    "<section",
}


def convert_invalid_p_wrappers(filepath: str):
    while True:
        # Check formatting with Prettier
        res = subprocess.run(
            ["npx", "prettier", filepath], capture_output=True, text=True
        )
        if res.returncode == 0:
            break

        line_num = None
        for err_line in res.stderr.splitlines():
            if 'Unexpected closing tag "p"' in err_line:
                pos = err_line.split("(")[:-1]
                pos_str = err_line.split("(")[-1].rstrip(")")
                line_num = int(pos_str.split(":")[0])
                break

        if not line_num:
            break

        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        if not (0 <= line_num - 1 < len(lines)):
            break

        # Search upward from the unexpected </p> line for the matching opening <p ...>
        found_block_p = False
        has_block_child = False
        for up in range(line_num - 1, -1, -1):
            if any(block in lines[up].lower() for block in BLOCK_TAGS):
                has_block_child = True

            if re.search(r"<p\b", lines[up], flags=re.IGNORECASE):
                if has_block_child:
                    # Convert opening <p ...> to <div ...> and closing </p> to </div>
                    lines[up] = re.sub(
                        r"<p\b", "<div", lines[up], count=1, flags=re.IGNORECASE
                    )
                    lines[line_num - 1] = re.sub(
                        r"</p\b[^>]*>",
                        "</div>",
                        lines[line_num - 1],
                        count=1,
                        flags=re.IGNORECASE,
                    )
                    found_block_p = True
                break

        # If </p> has no opening <p> anywhere above it, remove the orphan duplicate tag
        if not found_block_p:
            lines[line_num - 1] = re.sub(
                r"</p\b[^>]*>",
                "",
                lines[line_num - 1],
                count=1,
                flags=re.IGNORECASE,
            )

        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(lines)


html_files = sorted(
    [
        f
        for f in glob.glob("**/*.html", recursive=True)
        if "node_modules" not in f
    ]
)
with Pool(processes=16) as pool:
    pool.map(convert_invalid_p_wrappers, html_files)
