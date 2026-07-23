# HTML Prettier Cleanup & Layout-Preserving Scripts

This document details the Python scripts used to clean up HTML syntax errors and preserve layout when preparing the `llvm-www` repository for formatting with `npx prettier --write '**/*.html'`.

Prettier uses an HTML5 parser (`angular/html5`) which enforces strict HTML5 rules:
1. **Case-Matching Tags:** Opening and closing tags must use matching case (e.g., `<A>...</a>` is treated as a syntax error).
2. **Block Elements Inside `<p>`:** In HTML5, `<p>` cannot contain block-level elements (`<ul>`, `<table>`, `<h2>`, `<div>`, `<section>`, etc.). When an HTML5 parser encounters a block element inside `<p>`, it automatically closes the `<p>` tag before the block element starts. A trailing `</p>` after the block element then triggers `SyntaxError: Unexpected closing tag "p"`.

To fix these issues **without deleting closing tags or changing visual layout**, we used two scripts:

1. **Syntax & Case Correction Script (`fix_syntax_errors.py`):** This script resolves mismatched tag case, unquoted URLs in attribute values, void element syntax (`</br>` -> `<br>`), and specific unclosed/misnested tags across the repository.
2. **Layout-Preserving Paragraph Container Script (`convert_p_wrappers.py`):** Rather than removing closing `</p>` tags around nested block elements (which removes matching tags and can alter margins), this script converts invalid `<p ...> ... </p>` wrappers around block-level elements into matching `<div ...> ... </div>` containers. All attributes (`align="center"`, `class="..."`, `style="..."`) and closing tags remain matched.

To execute the full cleanup and reformat the repository:

```bash
# 1. Correct syntax errors and mismatched case tags
python3 fix_syntax_errors.py

# 2. Convert invalid <p> containers around block elements to <div> containers
python3 convert_p_wrappers.py

# 3. Verify all 137 HTML files pass Prettier check with zero syntax errors
npx prettier --check '**/*.html'

# 4. Reformat all HTML files in-place
npx prettier --write '**/*.html'
```
