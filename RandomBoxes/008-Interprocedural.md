---
permalink: "RandomBoxes/008-Interprocedural.html"
---
LLVM has great support for interprocedural analysis and optimization. It provides standard classes like call graphs, and provides a mature [Alias Analysis Infrastructure](docs/AliasAnalysis.html) as well. LLVM includes several interprocedural optimizations, including inlining, IP constant propagation, dead argument elimination, dead global elimination, global variable constantization, by-ref to by-value argument promotion, etc.
