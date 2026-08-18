---
layout: "default.html"
permalink: "ProjectsWithLLVM/index.html"
---
# Projects built with LLVM

This page is an incomplete list of the projects built with LLVM, sorted in reverse chronological order. The idea of this list is to show some of the things that have been done with LLVM for various course projects or for other purposes, which can be used as a source of ideas for future projects. Another good place to look is the list of [published papers and theses that use LLVM](../pubs).

Note that this page is not intended to reflect that current state of LLVM or show endorsement of any particular project over another. This is just a showcase of the hard work various people have done. It also shows a bit about how the capabilities of LLVM have evolved over time.

We are always looking for new contributions to this page. If you work on a project that uses LLVM for a course or a publication, we would definitely like to hear about it, and would like to include your work here as well. Please just send email to [the LLVM-dev mailing list](mailto:llvm-dev@lists.llvm.org) with an entry like those below. We're not particularly looking for source code (though we welcome source-code contributions through the normal channels), but instead would like to put up the "polished results" of your work, including reports, papers, presentations, posters, or anything else you have.

<!--=========================================================================-->

## Table of Contents

<!--=========================================================================-->

*   [dragonegg](#dragonegg)
*   [vmkit](#vmkit)
*   [DawnCC](#dawncc)
*   [Terra Lang](#terralang)
*   [Codasip Studio](#codasip)
*   [Pony Programming Language](#pony)
*   [SMACK Software Verifier](#smack)
*   [DiscoPoP: A Parallelism Discovery Tool](#discopop)
*   [Just-in-time Adaptive Decoder Engine (Jade)](#jade)
*   [The Crack Programming Language](#crack)
*   [Rubinius: a Ruby implementation](#rubinius)
*   [MacRuby](#macruby)
*   [pocl: Portable Computing Language](#pocl)
*   [TTA-based Codesign Environment (TCE)](#tta-tce)
*   [The IcedTea Version of Sun's OpenJDK](#icedtea)
*   [The Pure Programming Language Compiler](#pure)
*   [LDC - the LLVM-based D Compiler](#LDC)
*   [How to Write Your Own Compiler](#compilerwrite)
*   [Register Allocation by Puzzle Solving](#puzzles)
*   [Faust Real-Time Signal Processing System](#faust)
*   [Adobe "Hydra" Language](#adobe-hydra)
*   [Calysto Static Checker](#Calysto)
*   [Improvements on SSA-Based Register Allocation](#ssa_ra)
*   [LENS Project](#LENS)
*   [Trident Compiler](#trident)
*   [Ascenium Reconfigurable Processor Compiler](#ascenium)
*   [Scheme to LLVM Translator](#scheme)
*   [LLVM Visualization Tool](#llvmtv)
*   [Improvements to Linear Scan register allocation](#linearscan)
*   [LLVA-emu project](#llvaemu)
*   [SPEDI: Static Patch Extraction and Dynamic Insertion](#spedi)
*   [An LLVM Implementation of SSAPRE](#ssapre)
*   [Jello: a retargetable **J**ust-In-Time compil**e**r for **LL**VM bytec**o**de](#jello)
*   [Emscripten: An LLVM to JavaScript Compiler](#emscripten)
*   [Rust: a safe, concurrent, practical language](#rust)
*   [ESL: Embedded Systems Language](#ESL)
*   [RTSC: The Real-Time Systems Compiler](#RTSC)
*   [Vuo: A modern visual programming language for multimedia artists](#vuo)

<!--=========================================================================-->

## dragonegg

Dragonegg integrates the LLVM optimizers and code generator with the GCC parsers. This allows LLVM to compile Ada, Fortran, and other languages supported by the GCC compiler frontends, and access to C features not supported by Clang. See [dragonegg webpage](http://dragonegg.llvm.org).

## VMKit: a substrate for virtual machines

Current MREs are monolithic. Extending them to propose new features or reusing them to execute new languages is difficult. VMKit is a library that eases the development of new MREs and the process of experimenting with new mechanisms inside MREs. VMKit provides the basic components of MREs: a JIT compiler, a GC, and a thread manager. See [vmkit webpage](http://vmkit.llvm.org/).

## Automatic Insertion of Copy Annotation in Data-Parallel Programs

### By Gleison Mendonca, Breno Campos Ferreira Guimaraes, Péricles Alves, Marcio Machado Pereira, Guido Araéujo, and Fernando Magno Quintao Pereira. See Dawn project webpage.

Directive-based programming models, such as OpenACC and OpenMP arise today as promising techniques to support the development of parallel applications. These systems allow developers to convert a sequential program into a parallel one with minimum human intervention. However, inserting pragmas into production code is a difficult and error-prone task, often requiring familiarity with the target program. This difficulty restricts the ability of developers to annotate code that they have not written themselves. This paper provides one fundamental component in the solution of this problem. We introduce a static program analysis that infers the bounds of memory regions referenced in source code. Such bounds allow us to automatically insert data-transfer primitives, which are needed when the parallelized code is meant to be executed in an accelerator device, such as a GPU. To validate our ideas, we have applied them onto Polybench, using two different architectures: Nvidia and Qualcomm-based. We have successfully analyzed 98% of all the memory accesses in Polybench. This result has enabled us to insert automatic annotations into those benchmarks leading to speedups of over 100x.

<!--=========================================================================-->

## Terra: A low-level counterpart to Lua

### By Zach DeVito

[Terra](http://terralang.org/) is a system programming language that is embedded in and meta-programmed by Lua, which handles details like conditional compilation, type systems, namespaces, and templating/function specialization that are normally special constructs in other languages. Terra code shares Lua's syntax and control-flow constructs, and it can easily call Lua functions and vice versa. Since the JIT compiler is available at runtime, libraries and embedded domain specific languages can use it to dynamically generate or auto-tune arbitrary high performance code with custom optimizations.

Terra is backwards compatible with (and embeddable in) existing C code and is likewise a small, monomorphic, statically-typed, compiled language with manual memory management. There is also built-in support for SIMD operations and other low-level features like non-temporal writes and prefetches. Terra can optionally run independently from LuaJIT and LLVM. In fact, if your final program doesn’t need Lua, you can save Terra code into an object file, shared library, or executable.

<!--=========================================================================-->

## Codasip Studio

### By Codasip Ltd.

Codasip Studio is a highly automated development environment that covers all aspects of Application Specific Instruction-set Processor (ASIP) design including LLVM-based C/C++ compiler generation.

Starting with a high-level description of a processor written in CodAL (Codasip's processor description language), users are able to generate the design implementation, verification environment, virtual system prototype, and complete redistributable programming environment.

Codasip Studio includes a compiler backend generator that analyzes the CodAL description and then automatically generates sources for an LLVM backend with support of numerous extensions for ASIP programming. This way, users are able to generate a working C/C++ compiler for their specific architecture within several days.

<!--=========================================================================-->

## Pony Programming Language

### By the Pony Development Team

Pony is an object-oriented, actor-model, capabilities-secure, high performance programming language. It emphasizes a concurrent mindset by extending the class model with the actor model such that actors are first-class citizens. The language is statically typed, type- and memory-safe and comes with a collection of powerful guarantees: no data races, no uncaught exceptions, and no deadlocks. Pony implements a mark-and-don’t-sweep garbage collector without requiring generations or read and write barriers. There is no “stop-the-world” step required. All message passing between actors is causal.

<!--=========================================================================-->

## SMACK Software Verifier

### By smackers

[SMACK](https://github.com/smackers/smack) is an automated software verifier, verifying assertions given in its input LLVM intermediate representation (IR) programs. Under the hood, SMACK is a translator from the LLVM IR into the Boogie intermediate verification language (IVL). Targeting Boogie exploits a canonical platform which simplifies the implementation of algorithms for verification, model checking, and abstract interpretation.

<!--=========================================================================-->

## DiscoPoP: A Parallelism Discovery Tool

### By the DiscoPoP Development Team

[DiscoPoP (Discovery of Potential Parallelism)](http://www.grs-sim.de/discopop) is a tool that assists in identifying potential parallelism in sequential C/C++ programs. It instruments the code for finding both control and data dependences. A series of analyses are built on top of dependence to explore potential parallelism and parallel patterns. The instrumentation is done with the help of LLVM. A modified version of Clang with a new option "-dp" is also provided to invoke DiscoPoP.

<!--=========================================================================-->

## Just-in-time Adaptive Decoder Engine (Jade)

### By Jérôme Gorin (ARTEMIS/Institut Telecom/Telecom SudParis), Mickaël Raulet, Matthieu Wipliez (IETR/INSA Rennes)

[Jade](https://github.com/orcc/jade) (Just-in-time Adaptive Decoder Engine) is a generic video decoder engine using LLVM for just-in-time compilation of video decoder configurations. Those configurations are designed by MPEG Reconfigurable Video Coding (RVC) committee. MPEG RVC standard is built on a stream-based dataflow representation of decoders. It is composed of a standard library of coding tools written in RVC-CAL language and a dataflow configuration — block diagram — of a decoder.

Jade project is hosted as part of the Open RVC-CAL Compiler ([Orcc](http://orcc.sf.net)) and requires it to translate the RVC-CAL standard library of video coding tools into an LLVM assembly code.

<!--=========================================================================-->

## The Crack Programming Language

<!--=========================================================================-->

[Crack](http://code.google.com/p/crack-language/) aims to provide the ease of development of a scripting language with the performance of a compiled language. The language derives concepts from C++, Java and Python, incorporating object-oriented programming, operator overloading and strong typing.

<!--=========================================================================-->

## Rubinius

<!--=========================================================================-->

### By Evan Phoenix and the Rubinius team

[Rubinius](http://github.com/evanphx/rubinius) is a new virtual machine for Ruby. It leverages LLVM to dynamically compile Ruby code down to machine code using LLVM's JIT.

<!--=========================================================================-->

## MacRuby

### By the MacRuby Project Team

[MacRuby](http://macruby.org) is an implementation of Ruby on top of core Mac OS X technologies, such as the Objective-C common runtime and garbage collector, and the CoreFoundation framework. It is principally developed by Apple and aims at enabling the creation of full-fledged Mac OS X applications.

MacRuby uses LLVM for optimization passes, JIT and AOT compilation of Ruby expressions. It also uses zero-cost DWARF exceptions to implement Ruby exception handling.

<!--=========================================================================-->

## pocl: Portable Computing Language

### By various contributors.

In addition to producing an easily portable open source OpenCL implementation, another major goal of [pocl](http://portablecl.org) is improving performance portability of OpenCL programs with compiler optimizations, reducing the need for target-dependent manual optimizations.

An important part of pocl is a set of LLVM passes used to statically parallelize multiple work-items with the kernel compiler, even in the presence of work-group barriers. This enables static parallelization of the fine-grained static concurrency in the work groups in multiple ways.

<!--=========================================================================-->

## TTA-based Codesign Environment (TCE)

### By Customized Parallel Computing group of Tampere University of Technology

[TCE](http://tce.cs.tut.fi) is a toolset for designing customized exposed datapath processors based on the Transport triggered architecture (TTA).

The toolset provides a complete co-design flow from C/C++ programs down to synthesizable VHDL/Verilog and parallel program binaries. Processor customization points include the register files, function units, supported operations, and the interconnection network.

TCE uses Clang and LLVM for C/C++/OpenCL C language support, target independent optimizations and also for parts of code generation. It generates new LLVM-based code generators "on the fly" for the designed processors and loads them in to the compiler backend as runtime libraries to avoid per-target recompilation of larger parts of the compiler chain.

<!--=========================================================================-->

## The IcedTea Version of Sun's OpenJDK

### By Gary Benson (Red Hat, USA)

The [IcedTea](http://icedtea.classpath.org/) project was formed to provide a harness to build OpenJDK using only free software build tools and to provide replacements for the not-yet free parts of OpenJDK. Over time, various extensions to OpenJDK have been included in IcedTea.

One of these extensions is [Zero.](http://openjdk.java.net/projects/zero/) OpenJDK only supports x86 and SPARC processors; Zero is a processor-independent layer that allows OpenJDK to build and run using any processor. Zero contains a JIT compiler called [Shark](http://icedtea.classpath.org/wiki/ZeroSharkFaq) which uses LLVM to provide native code generation without introducing processor-dependent code.

The development of Zero and Shark were funded by Red Hat.

<!--=========================================================================-->

## The Pure Programming Language Compiler

### By Albert Graef, Johannes Gutenberg University Mainz (Germany)

[Pure](http://pure-lang.googlecode.com/) is an algebraic / functional programming language based on term rewriting. Programs are collections of equations which are used to evaluate expressions in a symbolic fashion. Pure offers dynamic typing, eager and lazy evaluation, lexical closures, a hygienic macro system (also based on term rewriting), built-in list and matrix support (including list and matrix comprehensions) and an easy-to-use C interface. The interpreter uses LLVM as a backend to JIT-compile Pure programs to fast native code.

In addition to the usual algebraic data structures, Pure also has MATLAB-style matrices in order to support numeric computations and signal processing in an efficient way. Pure is mainly aimed at mathematical applications right now, but it has been designed as a general purpose language. The dynamic interpreter environment and the C interface make it possible to use it as a kind of functional scripting language for many application areas.

<!--=========================================================================-->

## LDC - the LLVM-based D Compiler

### By the LDC developers

[D](http://dlang.org/) is a language with C-like syntax and static typing. It pragmatically combines efficiency, control, and modeling power, with safety and programmer productivity. D supports powerful concepts like Compile-Time Function Execution (CTFE) and Template Meta-Programming, provides an innovative approach to concurrency and offers many classical paradigms.

The [LDC](http://wiki.dlang.org/LDC) compiler uses the frontend from the reference compiler combined with LLVM as backend to produce efficient native code.

<!--=========================================================================-->

## How to Write Your Own Compiler

### By Silvano Rivoira, Politecnico di Torino

[This project](http://staff.polito.it/silvano.rivoira/HowToWriteYourOwnCompiler.htm) describes the development of a compiler front end producing LLVM Assembly Code for a Java-like programming language. It is used in a course on Compilers to show how to incrementally design and implement the successive phases of the translation process by means of common tools such as JFlex and Cup. The source code developed at each step is made available.

<!--=========================================================================-->

## Register Allocation by Puzzle Solving

### By Fernando Pereira and Jens Palsberg, UCLA.

In this project, we have shown that register allocation can be viewed as solving a collection of puzzles. We model the register file as a puzzle board and the program variables as puzzle pieces; pre-coloring and register aliasing fit in naturally. For architectures such as x86, SPARC V8, and StrongARM, we can solve the puzzles in polynomial time, and we have augmented the puzzle solver with a simple heuristic for spilling. For SPEC CPU2000, our implementation is as fast as the extended version of linear scan used by LLVM. Our implementation produces Pentium code that is of similar quality to the code produced by the slower, state-of-the-art iterated register coalescing algorithm of George and Appel augmented with extensions by Smith, Ramsey, and Holloway.

[Project page](http://compilers.cs.ucla.edu/fernando/projects/puzzles/) with a link to a tool that verifies the output of LLVM's register allocator.

<!--=========================================================================-->

## Faust Real-Time Signal Processing System

<!--=========================================================================-->

### By Grame, National Center of Music Creation

FAUST is a compiled language for real-time audio signal processing. The name FAUST stands for Functional AUdio STream. Its programming model combines two approaches: functional programming and block diagram composition. You can think of FAUST as a structured block diagram language with a textual syntax. The project aims at developing a new backend for Faust that will directly produce LLVM IR instead of the C++ class Faust currently produces. With a (yet to come) library version of the Faust compiler, it will allow developers to embed Faust + LLVM JIT to dynamically define, compile on the fly and execute Faust plug-ins. LLVM IR and tools also allows some nice bytecode manipulations like "partial evaluation/specialization" that will also be investigated.

<!--=========================================================================-->

## Adobe "Hydra" Language

<!--=========================================================================-->

### By Adobe Systems Incorporated

Efficient use of the computational resources available for image processing is a goal of the [Adobe Image Foundation](http://labs.adobe.com/wiki/index.php/AIF_Toolkit) project. Our language, "Hydra", is used to describe single- and multi-stage image processing kernels, which are then compiled and run on a target machine within a larger application. Similarly to how its namesake had many heads, our Hydra can be run on the GPU or alternately on the host CPU(s). AIF uses LLVM for our CPU path.

The first Adobe application to use our system is the soon-to-ship After Effects CS3. We welcome you to try out our public beta found at [labs.adobe.com](http://labs.adobe.com/technologies/aftereffectscs3/).

<!--=========================================================================-->

## Calysto Static Checker

<!--=========================================================================-->

### By Domagoj Babic, UBC.

[Calysto](http://www.cs.ubc.ca/~babic/index_calysto.htm) is a scalable context- and path-sensitive SSA-based static assertion checker. Unlike other static checkers, Calysto analyzes SSA directly, which means that it not only checks the original code, but also the front-end (including SSA-optimizations) of the compiler which was used to compile the code. The advantage of doing static checking on the SSA is language independency and the fact that the checked code is much closer to the generated assembly than the source code.

Several main factors contribute to Calysto's scalability:

*   A novel SSA symbolic execution algorithm that exploits the structure of the control flow graph to minimize the number of paths that need to be considered.
*   Lazy interprocedural analysis.
*   Tight integration with the [Spear](http://www.cs.ubc.ca/~babic/index_spear.htm) automated theorem prover, designed for software static checking.
*   And, of course, fast implementations of the basic algorithms in LLVM (dominator trees, postdominance, etc.).

Currently, Calysto is still in the development phase, and the first results are encouraging. Most likely, the first public release will happen some time in the fall 2007. [Spear](http://www.cs.ubc.ca/~babic/index_spear.htm) and Calysto generated [benchmarks](http://www.cs.ubc.ca/~babic/index_benchmarks.htm) are available.

<!--=========================================================================-->

## Improvements on SSA-Based Register Allocation.

### By Fernando Pereira, UCLA.

The register allocation problem has an exact polynomial solution when restricted to programs in the Single Static Assignment (SSA) form. Although striking, this major theoretical accomplishment has yet to be endorsed empirically. This project consists in the implementation of a complete SSA-based register allocator using the [LLVM](http://llvm.org/) compiler framework. We have implemented a static transformation of the target program that simplifies the implementation of the register allocator and improves the quality of the code that it generates. We also describe novel techniques to perform register coalescing and SSA-elimination. In order to validate our allocation technique, we extensively compare different flavors of our method against a modern and heavily tuned extension of the linear-scan register allocator described [here](2004-Fall-CS426-LS.pdf). The proposed algorithm consistently produces faster code when the target architecture provides a small number of registers. For instance, we have achieved an average speed-up of 9.2% when limiting the number of registers to four general purpose and three reserved register. By augmenting the algorithm with an aggressive coalescing technique, we have been able to raise the speed improvement up to 13.0%.

This project was supported by the google's [Summer of Code](http://code.google.com/soc/) initiative. Fernando Pereira is funded by [CAPES](http://www.capes.gov.br/capes/portal/) under process number 218603-9.

[Project page.](http://compilers.cs.ucla.edu/fernando/projects/soc/)

<!--=========================================================================-->

## LENS Project

<!--=========================================================================-->

### By Michael O. McCracken, UCSD.

The [LENS Project](http://www.cs.ucsd.edu/~mmccrack/lens/) is intended to improve the task of measuring programs and investigating their behavior. LENS defines an external representation of a program in XML to store useful information that is accessible based on program structure, including loop structure information.

Lens defines a flexible naming scheme for program components based on XPath and the LENS XML document structure. This allows users and tools to selectively query program behavior from a uniform interface, allowing users or tools to ask a variety of questions about program components, which can be answered by any tool that understands the query. Queries, metrics and program structure are all stored in the LENS file, and are annotated with version names that support historical comparison and scientific record-keeping.

Compiler writers can use LENS to expose results of transformations and analyses for a program easily, without worrying about display or handling information overload. This functionality has been demonstrated using LLVM. LENS uses LLVM for two purposes: first, to generate the initial program structure file in XML using an LLVM pass, and second, as a demonstration of the advantages of selective querying for compiler information, with an interface built into LLVM that allows LLVM passes to easily respond to queries in a LENS file.

<!--=========================================================================-->

## Trident Compiler

<!--=========================================================================-->

### By Los Alamos National Laboratory

[Trident](http://trident.sf.net/) is a compiler for floating point algorithms written in C, producing Register Transfer Level VHDL descriptions of circuits targeted for reconfigurable logic devices. Trident automatically extracts parallelism and pipelines loop bodies using conventional compiler optimizations and scheduling techniques. Trident also provides an open framework for experimentation, analysis, and optimization of floating point algorithms on FPGAs and the flexibility to easily integrate custom floating point libraries.

Trident uses the LLVM C/C++ front-end to parse input languages and produce low-level platform independent code.

<!--=========================================================================-->

## Ascenium Reconfigurable Processor Compiler

<!--=========================================================================-->

### By Ascenium Corporation

Ascenium is a fine-grained continuously reconfigurable processor that handles most instructions at hard-wired speeds while retaining the ability to be targeted by conventional high level languages, giving users "all the performance of hardware, all the ease of software."

The Ascenium team prefers LLVM bytecodes as input to its code generator for several reasons:

*   LLVM's all inclusive format makes global optimizations and consolidations such as global data dependency analysis easy.
*   LLVM's rich and strictly typed format generally make subtle and sophisticated optimizations easy.
*   LLVM's great ancillary tools and documentation make it easy to work with — even hardware geeks can understand it!

Ascenium's [HOT CHIPS 17](http://www.hotchips.org/archives/hc17/) [presentation](Ascenium.pdf) describes the architecture and compiler in more detail.

<!--=========================================================================-->

## Scheme to LLVM Translator

<!--=========================================================================-->

### By Tobias Nurmiranta

This is a [small scheme compiler](http://www.ida.liu.se/~tobnu/scheme2llvm/) for LLVM, written in scheme. It is good enough to compile itself and work.

The code is quite similar to the code in the book SICP (Structure and Interpretation of Computer Programs), chapter five, with the difference that it implements the extra functionality that SICP assumes that the explicit control evaluator (virtual machine) already have. Much functionality of the compiler is implemented in a subset of scheme, llvm-defines, which are compiled to llvm functions.

<!--=========================================================================-->

## LLVM Visualization Tool

<!--=========================================================================--> <!-- CS497rej: Object-Oriented Programming and Design (Spring 2004) Project --> <!-- _______________________________________________________________________ -->

### By Misha Brukman, Tanya Brethour, and Brian Gaeke

The LLVM Visualization Tool (LLVM-TV) can be used to visualize the effects of transformations written in the LLVM framework. Our visualizations reflect the state of a compilation unit at a single instant in time, between transformations; we call these saved states "snapshots". A user can visualize a sequence of snapshots of the same module—for example, as a program is being optimized—or snapshots of different modules, for comparison purposes.

Our target audience consists of developers working within the LLVM framework, who are trying to understand the LLVM representation and its analyses and transformations. In addition, LLVM-TV has been designed to make it easy to add new kinds of program visualization modules. LLVM-TV is based on the [wxWidgets](http://www.wxwindows.org) cross-platform GUI framework, and uses AT&T Research's [GraphViz](http://www.research.att.com/sw/tools/graphviz) to draw graphs.

[Wiki page](http://wiki.cs.uiuc.edu/cs497rej/LLVM+Visualization+Tool) with overview; design doc, and user manual. You can download llvm-tv from LLVM SVN (http://llvm.org/svn/llvm-project/television/trunk).

<!--=========================================================================-->

## Improvements to Linear Scan register allocation

<!--=========================================================================--> <!-- CS426: Advanced Compilers (Fall 2003) Project<br>--> <!-- _______________________________________________________________________ -->

### By Alkis Evlogimenos

Linear scan register allocation is a fast global register allocation first presented in [Linear Scan Register Allocation](http://citeseer.ist.psu.edu/poletto99linear.html) as an alternative to the more widely used graph coloring approach. In this paper, I apply the linear scan register allocation algorithm in a system with SSA form and show how to improve the algorithm by taking advantage of lifetime holes and memory operands, and also eliminate the need for reserving registers for spill code.

Project report: [PS](2004-Fall-CS426-LS.ps), [PDF](2004-Fall-CS426-LS.pdf)

<!--=========================================================================-->

## LLVA-emu project

<!--=========================================================================--> <!-- CS497YYZ: Hot Topics in Operating Systems (Fall 2003) --> <!-- _______________________________________________________________________ -->

### By Misha Brukman and Brian Gaeke

Traditional architectures use the hardware instruction set for dual purposes: first, as a language in which to express the semantics of software programs, and second, as a means for controlling the hardware. The thesis of the [Low-Level Virtual Architecture](/pubs/2003-10-01-LLVA.html) project is to decouple these two uses from one another, allowing software to be expressed in a semantically richer, more easily-manipulated format, and allowing for more powerful optimizations and whole-program analyses directly on compiled code.

The semantically rich format we use in LLVA, which is based on the LLVM compiler infrastructure's intermediate representation, can best be understood as a "virtual instruction set". This means that while its instructions are closely matched to those available in the underlying hardware, they may not correspond exactly to the instructions understood by the underlying hardware. These underlying instructions we call the "implementation instruction set." Between the two layers lives the translation layer, typically implemented in software.

In this project, we have taken our next logical steps in this effort by (1) porting the entire Linux kernel to LLVA, and (2) engineering an environment in which a kernel can be run directly from its LLVM bytecode representation — essentially, a minimal, but complete, emulated computer system with LLVA as its native instruction set. The emulator we have invented, llva-emu, executes kernel code by translating programs "just-in-time" from the LLVM bytecode format to the processor's native instruction set.

Project report: [PS](2003-Fall-CS497YYZ-LLVA-emu.ps), [PDF](2003-Fall-CS497YYZ-LLVA-emu.pdf)

<!--=========================================================================-->

## SPEDI: Static Patch Extraction and Dynamic Insertion

<!--=========================================================================--> <!-- _______________________________________________________________________ -->

### By Brian Fahs

As every modern computer user has experienced, software updates and upgrades frequently require programs and sometimes the entire operating system to be restarted. This can be a painful and annoying experience. What if this common annoyance could be avoided completely or at least significantly reduced? Imagine only rebooting your system when you wanted to shut your computer down or only closing an application when you wanted rather than when an update occurs. The purpose of this project is to investigate the potential of performing dynamic patching of executables and create a patching tool capable of automatically generating patches and applying them to applications that are already running. This project should answer questions like: How can dynamic updating be performed? What type of analysis is required? Can this analysis be effectively automated? What can be updated in the running executable (e.g., algorithms, organization, data, etc.)?

Project report: [PS](2003-Fall-CS497YYZ-SPEDI.ps), [PDF](2003-Fall-CS497YYZ-SPEDI.pdf)

<!--=========================================================================-->

## An LLVM Implementation of SSAPRE

<!--=========================================================================--> <!--CS426: Advanced Compilers (Fall 2002)--> <!-- _______________________________________________________________________ -->

### By Tanya Brethour, Joel Stanley, and Bill Wendling

In this report we present implementation details, empirical performance data, and notable modifications to an algorithm for PRE based on \[the 1999 TOPLAS SSAPRE paper\]. In \[the 1999 TOPLAS SSAPRE paper\], a particular realization of PRE, known as SSAPRE, is described, which is more efficient than traditional PRE implementations because it relies on useful properties of Static Single-Assignment (SSA) form to perform dataflow analysis in a much more sparse manner than the traditional bit-vector-based approach. Our implementation is specific to a SSA-based compiler infrastructure known as LLVM (Low-Level Virtual Machine).

Project report: [PS](2002-Fall-CS426-SSAPRE.ps), [PDF](2002-Fall-CS426-SSAPRE.pdf)

<!--=========================================================================-->

## Jello: a retargetable Just-In-Time compiler for LLVM bytecode

<!--=========================================================================--> <!-- CS497CZ: Dynamic Translation and Optimization (Spring 2002)--> <!-- _______________________________________________________________________ -->

### By Chris Lattner, Misha Brukman, and Brian Gaeke

We present the design and implementation of Jello, a *retargetable* Just-In-Time (JIT) compiler for the Intel IA32 architecture. The input to Jello is a C program statically compiled to Low-Level Virtual Machine (LLVM) bytecode. Jello takes advantage of the features of the LLVM bytecode representation to permit efficient run-time code generation, while emphasizing retargetability. Our approach uses an abstract machine code representation in Static Single Assignment form that is machine-independent, but can handle machine-specific features such as implicit and explicit register references. Because this representation is target-independent, many phases of code generation can be target-independent, making the JIT easily retargetable to new platforms without changing the code generator. Jello's ultimate goal is to provide a flexible host for future research in runtime optimization for programs written in languages which are traditionally compiled statically.

Note that Jello eventually evolved into the current LLVM JIT, which is part of the tool **lli**.

Project report: [PS](2002-Spring-CS497CZ-Jello.ps), [PDF](2002-Spring-CS497CZ-Jello.pdf)

<!--=========================================================================-->

## Emscripten: An LLVM to JavaScript Compiler

### By Alon Zakai and the rest of the Emscripten contributors

[Emscripten](http://emscripten.org) compiles LLVM bitcode into JavaScript, which makes it possible to compile C and C++ source code to JavaScript (by first compiling it into LLVM bitcode using Clang), which can be run on the web. Emscripten has been used to port large existing C and C++ codebases, for example Python (the standard CPython implementation), the Bullet physics engine, and the eSpeak speech synthesizer, among many others.

Emscripten itself is written in JavaScript. Significant components include the [Relooper Algorithm](https://github.com/kripken/emscripten/blob/master/docs/paper.pdf?raw=true) which generates high-level JavaScript control flow structures ("if", "while", etc.) from the low-level basic block information present in LLVM bitcode, as well as a JavaScript parser for LLVM assembly.

<!--=========================================================================-->

## Rust: a safe, concurrent, practical language

### The rust contributors

[rust](http://www.rust-lang.org/) is a curly-brace, block-structured expression language. It visually resembles the C language family, but differs significantly in syntactic and semantic details. Its design is oriented toward concerns of "programming in the large", that is, of creating and maintaining *boundaries* - both abstract and operational - that preserve large-system *integrity*, *availability* and *concurrency*.

It supports a mixture of imperative procedural, concurrent actor, object-oriented and pure functional styles. Rust also supports generic programming and metaprogramming, in both static and dynamic styles.

The static/native compilation is using LLVM.

<!--=========================================================================-->

## Embedded Systems Language

[ESL (Embedded Systems Language)](https://github.com/bagel99/esl) is a new programming language designed for efficient implementation of embedded systems and other low-level system programming projects. ESL is a typed compiled language with features that allow the programmer to dictate the concrete representation of data values; useful when dealing, for example, with communication protocols or device registers.

Novel features are: no reserved words, procedures can return multiple values, automatic endian conversion, methods on types (but no classes). The syntax is more Pascal-like than C-like, but with C bracketing. The compiler bootstraps from LL IR.

<!--=========================================================================-->

## RTSC: The Real-Time Systems Compiler

[The Real-Time Systems Compiler (RTSC)](http://www4.cs.fau.de/Research/RTSC/) is an operating-system–aware compiler that allows for a generic manipulation of the real-time system architecture of a given real-time application.

Currently, its most interesting application is the automatic migration of an event-triggered (i.e. based on OSEK OS) system to a time-triggered (i.e. based on OSEKTime) one. To achieve this, the RTSC derives an abstract global dependency graph from the source code of the application formed by so called "Atomic Basic Blocks" (ABBs). This "ABB-graph" is free of any dependency to the original operating system but includes all control and data dependencies of the application. Thus this graph can be mapped to another target operating system. Currently input applications can be written for OSEK OS and then be migrated to OSEKTime or POSIX systems.

The LLVM-framework is used throughout the whole process. At first the static analysis of the application needed to construct the ABB-graph is performed using the LLVM-framework. Additionally the manipulation and final generation of the target system are also based on the LLVM.

<!--=========================================================================-->

## Vuo: A modern visual programming language for multimedia artists

[Vuo](http://vuo.org) is a modern visual programming language for multimedia artists. The Vuo Compiler takes modular components written in various languages, and a graph of dataflow between components. [Using the LLVM code generation API](http://vuo.org/node/31), the Vuo Compiler turns the graph into a native, multithreaded executable.
