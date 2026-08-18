---
permalink: "devmtg/2013-11/slides/DebugBOFNotes.html"
---
Debug Info BOF

# Debug Info BOF

### *Eric Christopher*

Optimized debugging is still a big miss with a lof of metadata being lost at various stages, mostly affecting variable tracking, leastly affecting line information.

Suggestion to use dom/dataflow to compute liveness for location lists. Eric not keen on this (expensive?).

Dwarf 4 seems to be the standard that LLVM is being coded to, Dwarf 3 in maintenance mode, Dwarf 2 is dead. Still, would be good to have some mechanism to limit the version of Dwarf symbols, to avoid breaking compatibility with older toolchains for a small feature.

In time, Dwarf 3 will be deprecated, and the story will repeat, and it's clear and accepted by all that this is the natural course of thing.

Debug info for LTO "now works" in 3.4, uniquing all C++ types. This depends on having consistent class descriptions across CUs.

Many debug info size improvements. Non-LTO "smaller than GCC" in 3.4.

Verifier will check debug info, so metadata is supposed to be consistent after validation.

Metadata may lose type information and be left with line, function and scope info. The rest can be inferred from IR.

Debug metadata is widely known to be huge and methods to reduce the size in IR are being considered, including emitting Dwarf directly in IR, converting the most common constructs to text literals (including small numbers, < 4-8 digits), packing (zip) the contents, etc.
