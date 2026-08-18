---
layout: "default.html"
permalink: "devmtg/2015-02-07/index.html"
---
# LLVM Workshop at CGO

1.  [Schedule](#schedule)

*   **What**: LLVM at CGO.
*   **When**: February 7, 2015
*   **Where**: San Francisco, CA

A LLVM Workshop will be held at CGO 2015. If you are interested in attending the workshop, please register at the [CGO website](http://cgo.org/cgo2015/).

Topic Overview

*   High-level overview of LLVM & Clang

*   Will include how to get started coding on LLVM & Clang
*   Overview of core design elements, data structures, APIs, and patterns used in the codebase
*   High-level testing strategy for LLVM & Clang using tools like Clang’s ‘-verify’, opt, llc, FileCheck, and GoogleTest
*   Process of submitting a patch, code review, and community interactions

*   How to add an optimization pass to LLVM

*   Tutorial on the LLVM IR both in the abstract and at the level of internal APIs
*   Basic APIs and data structures needed to implement, test, and wire a new pass into the compiler.
*   Overview of the relationship between transform and analysis passes.
*   Overview of the different kinds of transformation passes, how they interact, and what they can and can’t do
*   Actually add a transformation pass and an analysis pass to the compiler that depend on each other and exercise this machinery.
*   Includes authoring relevant tests for each component

*   High-level overview of the architecture of an LLVM backend, with an emphasis on modifying or enhancing existing backends rather than adding a new one

*   Detailed review of where things are: from SelectionDAG to FastISel to the register allocator
*   Detailed review of exactly how a backend’s tablegen works, and how to make changes there and debug things

# Schedule

| Time | Topic |
| --- | --- |
| 8:30 | Introduction to the LLVM Project |
| 9:00 | Getting started hacking on LLVM and Clang |
| 10:00 | BREAK |
| 10:30 | The middle end optimizer |
| 12:00 | LUNCH |
| 2:00 | Diagnosing and fixing bugs in the middle end optimizer |
| 2:45 | Adding optimization passes to the middle end |
| 3:30 | BREAK |
| 4:00 | Overview of the LLVM Code Generator |
| 4:30 | Adding custom legalization, target specific pseudo instructions, and instruction pattern |
| 5:00 | Extended Q&A |

<!-- *********************************************************************** -->

* * *
