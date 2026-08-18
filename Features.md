---
layout: "default.html"
permalink: "Features.html"
---
# LLVM Features

The [LLVM compiler system](releases/) for C and C++ includes the following:

*   Front-ends for C, C++, Objective-C, Fortran, etc. They support the ANSI-standard C and C++ languages. Additionally, many GCC extensions are supported.
*   A stable implementation of the LLVM instruction set, which serves as both the online and offline code representation, together with assembly (ASCII) and bytecode (binary) readers and writers, and a verifier.
*   A powerful pass-management system that automatically sequences passes (including analysis, transformation, and code-generation passes) based on their dependences, and pipelines them for efficiency.
*   A wide range of global scalar optimizations.
*   A link-time interprocedural optimization framework with a rich set of analyses and transformations, including sophisticated whole-program pointer analysis, call graph construction, and support for profile-guided optimizations.
*   An easily retargetable code generator, which currently supports X86, X86-64, PowerPC, PowerPC-64, ARM, Thumb, SPARC, Alpha, CellSPU, MIPS, MSP430, SystemZ, WebAssembly and XCore.
*   A Just-In-Time (JIT) code generation system, which currently supports X86, X86-64, ARM, AArch64, Mips, SystemZ, PowerPC, and PowerPC-64.
*   Support for generating DWARF debugging information.
*   A profiling system similar to gprof.
*   A test framework with a number of benchmark codes and applications.
*   APIs and debugging tools to simplify rapid development of LLVM components.

# Strengths of the LLVM System

1.  LLVM uses a simple [low-level language](docs/LangRef.html) with strictly defined semantics.
2.  It includes front-ends for [C](docs/CommandGuide/html/llvmgcc.html) and [C++](docs/CommandGuide/html/llvmgxx.html). Front-ends for Java, Scheme, and other languages are in development.
3.  It includes an aggressive optimizer, including scalar, interprocedural, profile-driven, and some simple loop optimizations.
4.  It supports a [life-long compilation model](/pubs/2004-01-30-CGO-LLVM.html), including link-time, install-time, run-time, and offline optimization.
5.  LLVM has full support for [accurate garbage collection](docs/GarbageCollection.html).
6.  The LLVM code generator is relatively easy to retarget, and makes use of a powerful target description language.
7.  LLVM has extensive [documentation](docs/) and has hosted many [projects](ProjectsWithLLVM/) of various sorts.
8.  Many third-party users have claimed that LLVM is easy to work with and develop for. For example, the (now removed) Stacker front-end was written in 4 days by someone who started knowing nothing about LLVM. Additionally, LLVM has tools to make [development easier](docs/Bugpoint.html).
9.  LLVM is under active development and is constantly being extended, enhanced and improved. See the status updates on the left bar to see the rate of development.
10.  LLVM is freely available under an OSI-approved "Apache License Version 2.0" license.
11.  LLVM is currently used by many commercial, non-profit or academic entities, who contribute many extensions and new features.

# LLVM Audience

LLVM can be used in many different kinds of projects. You might be interested in LLVM if you are:

*   A compiler researcher interested in compile-time, link-time (interprocedural), and runtime transformations for C and C++ programs.
*   A virtual machine researcher/developer interested in a portable, language-independent instruction set and compilation framework.
*   An architecture researcher interested in compiler/hardware techniques.
*   A security researcher interested in static analysis or instrumentation.
*   An instructor or developer interested in a system for quick prototyping of compiler transformations.
*   An end-user who wants to get better performance out of your code.

# Want to Know More?

You can [browse the documentation online](docs/), try [LLVM in your web browser](/demo/index.cgi), or [download the source code.](/releases/index.html)
