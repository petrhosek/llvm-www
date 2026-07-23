# Eleventy Static Site Conversion & Migration Script

This document describes the architecture, configuration, and standalone Python script used to convert the 137 Prettier-formatted static HTML files in `llvm-www` into an Eleventy (`@11ty/eleventy`) Markdown-based static site generator setup without altering the resulting HTML output.

---

## 1. Eleventy Configuration (`eleventy.config.js`)

```javascript
module.exports = function (eleventyConfig) {
  // Copy all static assets (CSS, images, slides, SSI includes, PDFs, etc.)
  eleventyConfig.addPassthroughCopy(
    "**/*.{css,png,jpg,PNG,gif,ico,svg,pdf,key,mov,m4v,txt,cgi,incl,js,json,xml,yml,php,ps,eps,ai,cc,py,scale,scss,tbz2,gz,ttf,eot,woff,otf,dir,ppsx,ppt,pptx}"
  );

  return {
    markdownTemplateEngine: false,
    htmlTemplateEngine: false,
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
  };
};
```

### Key Architectural Decisions:
- **`templateEngineOverride: "html"` (`_data/eleventyComputed.js`)**: Tells Eleventy to bypass Markdown-It and Liquid/Nunjucks template evaluation for converted pages so existing HTML blocks, list items, and code snippets are passed through 100% untouched.
- **Dynamic Relative Include Paths (`_includes/default.11ty.js`)**: Calculates the exact relative path (`header.incl`, `../header.incl`, `../../header.incl`) based on `page.filePathStem` so SSI includes resolve identically regardless of directory depth.

---

## 2. Layouts

### `_includes/default.11ty.js`
Used for standard pages that include both `header.incl` at the top and `footer.incl` at the bottom:
```javascript
module.exports = function (data) {
  const stem = data.page.filePathStem || "";
  const parts = stem.split("/").filter((p) => p !== "");
  const depth = Math.max(0, parts.length - 1);
  const prefix = depth === 0 ? "" : "../".repeat(depth);

  return (
    `<!--#include virtual="${prefix}header.incl" -->\n` +
    data.content +
    `<!--#include virtual="${prefix}footer.incl" -->\n`
  );
};
```

### `_includes/header_only.11ty.js`
Used for pages that include only `header.incl`:
```javascript
module.exports = function (data) {
  const stem = data.page.filePathStem || "";
  const parts = stem.split("/").filter((p) => p !== "");
  const depth = Math.max(0, parts.length - 1);
  const prefix = depth === 0 ? "" : "../".repeat(depth);

  return `<!--#include virtual="${prefix}header.incl" -->\n` + data.content;
};
```

---

## 3. Python Conversion Script (`convert_html_to_md.py`)

This standalone script converts all 137 `.html` files to `.md` files, assigns the appropriate layout, preserves exact relative permalinks, and removes the old `.html` source files via `git rm -f`.

```python
#!/usr/bin/env python3
"""
convert_html_to_md.py

Converts all static HTML files to Eleventy Markdown source files (.md)
with YAML front matter while preserving exact output paths and SSI includes.
"""

import glob
import os
import subprocess


def convert_all_html_files():
    html_files = sorted(
        [
            f
            for f in glob.glob("**/*.html", recursive=True)
            if "node_modules" not in f and "_site" not in f
        ]
    )
    print(f"Converting {len(html_files)} HTML files to Markdown...")

    for filepath in html_files:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as fp:
            lines = fp.readlines()

        has_header = any("header.incl" in l for l in lines[:5])
        has_footer = any("footer.incl" in l for l in lines[-5:])

        if has_header and has_footer:
            for i, l in enumerate(lines):
                if "header.incl" in l:
                    del lines[i]
                    break
            for i in range(len(lines) - 1, -1, -1):
                if "footer.incl" in lines[i]:
                    del lines[i]
                    break
            frontmatter = (
                f"---\n"
                f'layout: "default.11ty.js"\n'
                f'permalink: "{filepath}"\n'
                f"---\n"
            )
        elif has_header and not has_footer:
            for i, l in enumerate(lines):
                if "header.incl" in l:
                    del lines[i]
                    break
            frontmatter = (
                f"---\n"
                f'layout: "header_only.11ty.js"\n'
                f'permalink: "{filepath}"\n'
                f"---\n"
            )
        else:
            frontmatter = f'---\npermalink: "{filepath}"\n---\n'

        markdown_path = filepath[:-5] + ".md"
        with open(markdown_path, "w", encoding="utf-8") as fp:
            fp.write(frontmatter + "".join(lines))

        subprocess.run(["git", "rm", "-f", "-q", filepath], check=True)

    # Ensure existing proposals/*.md files specify explicit permalinks
    for md_filepath in sorted(glob.glob("proposals/*.md")):
        with open(md_filepath, "r", encoding="utf-8") as fp:
            content = fp.read()
        if "permalink:" not in content[:100]:
            base_html = md_filepath[:-3] + ".html"
            with open(md_filepath, "w", encoding="utf-8") as fp:
                fp.write(f'---\npermalink: "{base_html}"\n---\n' + content)

    print("Successfully converted all HTML files to Markdown.")


if __name__ == "__main__":
    convert_all_html_files()
```

---

## 4. Build & Verification Commands

```bash
# Build static site into _site/ directory
npm run build

# Verify generated HTML files match existing HTML files exactly
diff -r /path/to/baseline_html/ _site/
```
