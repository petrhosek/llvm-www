---
layout: "default.html"
permalink: "devmtg/2014-10/index.html"
---
# 2014 LLVM Developers' Meeting

1.  [About](#about)
2.  [October 28 - Meeting Agenda](#agenda1)
3.  [October 29 - Meeting Agenda](#agenda2)
4.  [Talk Abstracts](#abstracts)
5.  [Lightning Talk Abstracts](#light)
6.  [Tutorial Abstracts](#tutorials)
7.  [BoF Abstracts](#bof)
8.  [Poster Abstracts](#poster)
9.  [Logistics](#logistics)

*   **What**: The eighth meeting of LLVM Developers and Users.
*   **When**: October 28-29, 2014
*   **Where**: DoubleTree by Hilton - San Jose, CA

A huge thank you to our sponsors!

# Diamond Sponsors:

#      [Apple](http://www.apple.com)

        ![](quic_web_logo.jpg)  
        [QuIC](http://www.quicinc.com)

# Platinum Sponsors:

        ![](Google-logo_420_color_2x.png)  
        [Google](http://google.com)

        ![](SCE_C_pos.jpg)  
        [Sony Computer Entertainment America](http://us.playstation.com/corporate/about/)

# Gold Sponsors:

        Interested in being a Gold Level Sponsor? See [below.](#sponsor)

# Silver Sponsors:

        ![](HSAFoundation-FINAL.PNG)  
        [HSA Foundation](http://www.hsafoundation.com)

        ![](MentorEmbedded_brand_legal.png)  
        [Mentor Embedded](http://www.mentor.com/embedded)

# Bronze Sponsors:

        ![](ARMCompanyLogo.jpg)  
        [ARM](http://www.arm.com)

# About

The LLVM Foundation announces the eighth annual bay area LLVM Developers' Meeting will be held October 28th and 29th in San Jose, CA.

This year the conference will be 2 full days that include technical talks, BoFs, hacker’s lab, tutorials, and a poster session. Attendance will be capped at 300.

The meeting serves as a forum for [LLVM](http://llvm.org), [Clang](http://clang.llvm.org), [LLDB](http://lldb.llvm.org) and other LLVM project developers and users to get acquainted, learn how LLVM is used, and exchange ideas about LLVM and its (potential) applications. More broadly, we believe the event will be of particular interest to the following people:

*   Active developers of projects in the LLVM Umbrella (LLVM core, Clang, LLDB, libc++, compiler\_rt, klee, dragonegg, lld, etc).
*   Anyone interested in using these as part of another project.
*   Compiler, programming language, and runtime enthusiasts.
*   Those interested in using compiler and toolchain technology in novel and interesting ways.

# October 28 - Meeting Agenda

| Media | Talk |
| --- | --- |
| [Slides](Slides/2014WelcomeTalk.pdf)<br>[Video](https://youtu.be/DEd95Zwqbtw) | **Welcome**<br>Tanya Lattner, *LLVM Foundation* |
| [Slides](Slides/Bataev-OpenMP.pdf)<br>[Video](https://youtu.be/OI2Ccucy73Q) | **[OpenMP Support in Clang/LLVM: Status Update and Future Directions](#talk1)**<br>Alexey Bataev, *Intel* |
| [Slides](Slides/Menendez-Alive.pdf)<br>[Video](https://youtu.be/iV5jBtE35r4) | **[Alive: Provably Correct InstCombine Optimizations](#talk2)**<br>David Menendez, *Rutgers University* |
| [Slides](Slides/Stellard-llvm-stable-releases2014.pdf)<br>[Video](https://youtu.be/9h5Zx_mO2tI) | **[LLVM Stable Releases](#talk3)**<br>Tom Stellard, *Advanced Micro Devices* |
| [Slides](Slides/Reames-GarbageCollection.pdf)<br>[Video](https://youtu.be/mdVR0RYJQ9w) | **[Supporting Precise Relocating Garbage Collection in LLVM](#talk4)**<br>Philip Reames, *Azul Systems*<br>Sanjoy Das, *Azul Systems* |
| [Slides](Slides/Zhao-SourceCodeAnalysisforSecurity.pdf)<br>[Video](https://youtu.be/xSN0J_JV06E) | **[Source Code Analysis for Security through LLVM](#talk5)**<br>Lu Zhao, *HP Fortify* |
| [Slides](Slides/Trick-FTL.pdf)<br>[Video](https://youtu.be/bnY5FVxHUVc) | **[FTL: WebKit’s LLVM based JIT](#talk6)**<br>Andrew Trick, *Apple*<br>Juergen Ributzka, *Apple* |
| [Slides](Slides/Criswell-VirtualGhost.pdf)<br>[Video](https://youtu.be/iVwShAxImHE) | **[Virtual Ghost: Using LLVM to Protect Applications from a Compromised Operating System](#talk7)**<br>John Criswell, *University of Rochester* |
| [Slides](Slides/Cormack-BuildingAnLLVMBackend.pdf)<br>[Video](https://youtu.be/b53WqCbLEYg) | **[Building an LLVM Backend](#tutorial1)**<br>Fraser Cormack, *Codeplay Software*<br>Pierre-André Saulais, *Codeplay Software* |
| [Slides](Slides/Estes-MISchedulerTutorial.pdf)<br>[Video](https://youtu.be/Uge_whHVmtM) | **[Adding and Optimizing a Subtarget for MIScheduler](#tutorial2)**<br>Dave Estes, *QuIC* |
| [Slides](Slides/Christopher-DebugInfoTutorial.pdf)<br>[Video](https://youtu.be/_wqX9H2A66M) | **[Debug Info Tutorial](#tutorial3)**<br>Eric Christopher, *Google*<br>David Blaikie, *Google* |

# October 29 - Meeting Agenda

| Media | Talk |
| --- | --- |
| [Slides](Slides/Carruth-TheLLVMPassManagerPart2.pdf)<br>[Video](https://youtu.be/6NDQl544yEg) | **[The LLVM Pass Manager, Part 2](#talk11)**<br>Chandler Carruth, *Google* |
| [Slides](Slides/Molloy-LLVM-Performant-As-GCC-llvm-dev-2014.pdf)<br>[Video](https://youtu.be/EsNMa9nxLOk) | **[What does it take to get LLVM as performant as GCC](#talk9)**<br>James Molloy, *ARM*<br>Ana Pazos, *QuIC* |
| [Slides](Slides/Morisset-AtomicsPresentation.pdf)<br>[Video](https://youtu.be/cDM6Gr_XzGI) | **[Blowing up the Atomic Barrier](#talk10)**<br>Robin Morisset, *Google* |
| [Slides](&lt;Slides/Skip the FFI.pdf&gt;)<br>[Video](https://youtu.be/_xAqf-VwaOM) | **[Skip the FFI: Embedding Clang for C Interoperability](#talk18)**<br>Jordan Rose, *Apple*<br>John McCall, *Apple* |
| [Slides](Slides/Schmidt-SupportingVectorProgramming.pdf)<br>[Video](https://youtu.be/y_YU5CxrxNo) | **[Supporting Vector Programming on a Bi-Endian Processor Architecture](#talk12)**<br>Bill Schmidt, *IBM* |
| [Slides](Slides/Finkel-IntrinsicsMetadataAttributes.pdf)<br>[Video](https://youtu.be/Zyeey4gkIg8) | **[Intrinsics, Metadata and Attributes: Now, more than ever!](#talk13)**<br>Hal Finkel, *Argonne National Laboratory* |
| [Slides](Slides/Prashanth-DLO.pdf)<br>[Video](https://youtu.be/Ckzole3hArc) | **[Implementing Data Layout Optimizations in LLVM Framework](#talk14)**<br>Prashantha NR, *Compiler Tree Technologies* |
| [Slides](Slides/Majnemer-FuzzingClang.pdf)<br>[Video](https://youtu.be/0yUzo-pBkFk) | **[Fuzzing Clang to Find ABI Bugs](#talk15)**<br>David Majnemer, *Google* |
| [Slides](Slides/Scheller-ARMCodeQuality.pdf)<br>[Video](https://youtu.be/1DM2Q75qDSU) | **[A closer look at ARM code quality](#talk16)**<br>Tilmann Scheller, *Samsung Electronics* |
| [Slides](Slides/Larin-GlobalInstructionScheduling.pdf)<br>[Video](https://youtu.be/A88vO_lP5b8) | **[Implementation of global instruction scheduling in LLVM infrastructure](#talk17)**<br>Sergei Larin, *QuIC*<br>Aditya Kumar, *QuIC* |
| [Slides](#light)<br>[Video](https://youtu.be/sNZD7qFA2nY) | **[Lightning Talks](#light)** |
| [Slides](Slides/Baker-CustomHardwareStateMachines.pdf)<br>[Video](https://youtu.be/DGWFQXK_EU4) | **[Custom Hardware State-Machines and Datapaths: Using LLVM to Generate FPGA Accelerators](#talk19)**<br>Alan Baker, *Altera Corporation* |
| [Slides](Slides/Baev-Controlling_VRP.pdf)<br>[Video](https://youtu.be/lJmXiwJo2ZQ) | **[Controlling Virtual Register Pressure in LLVM Middle-End](#talk20)**<br>Ivan Baev, *QuIC* |
| [Slides](Slides/Zarko-IndexingLargeMixedLang.pdf)<br>[Video](https://youtu.be/KDiXo5GwQ-U) | **[Indexing Large, Mixed-Language Codebases](#talk21)**<br>Luke Zarko, *Google* |
| [Slides](&lt;Slides/Christopher-Function Multiversioning Talk.pdf&gt;)<br>[Video](https://youtu.be/iAaoGsCVeCI) | **[Architecture Specific Code Generation and Function Multiversioning](#talk22)**<br>Eric Christopher, *Google* |
| [Slides](Slides/Hawes-Frappe.pdf)<br>[Video](https://youtu.be/xelhxXfqngc) | **[Frappé: Using Clang to Query and Visualize Large Codebases](#talk23)**<br>Nathan Hawes, *Oracle*<br>Ben Barham, *Oracle* |

# Talk Abstracts

**OpenMP Support in Clang/LLVM: Status Update and Future Directions**  
*Alexey Bataev (Speaker) - Intel, Zinovy Nis (Speaker) - Intel*  
[Slides](Slides/Bataev-OpenMP.pdf)  
[Video](https://youtu.be/OI2Ccucy73Q)  
OpenMP is a well-known and widely used API for shared-memory parallelism. Support for OpenMP in Clang/LLVM compiler is currently under development. In this talk, we will present current status of OpenMP support, what is done and what remains to be done, technical details behind OpenMP implementation. Also, we will elaborate on accelerators and pragma-assisted SIMD vectorization, introduced in the latest 4.0 edition of the OpenMP standard.

**Alive: Provably Correct InstCombine Optimizations**  
*Nuno Lopes - Microsoft Research, David Menendez (Speaker) - Rutgers University, Santosh Nagarakatte - Rutgers University John Regehr - University of Utah*  
[Slides](Slides/Menendez-Alive.pdf)  
[Video](https://youtu.be/iV5jBtE35r4)  
Optimizations are hard to get right. Even seemingly innocuous transformations in InstCombine can miss important corner cases. With Alive, you can specify peephole optimizations in a friendly, LLVM-like language, automatically determine their correctness, and generate the corresponding C++ code. 

**LLVM Stable Releases**  
*Tom Stellard - Advanced Micro Devices*  
[Slides](Slides/Stellard-llvm-stable-releases2014.pdf)  
[Video](https://youtu.be/9h5Zx_mO2tI)  
This talk will cover LLVM stable releases, how they work, who uses them, and how we can make them better.

**Supporting Precise Relocating Garbage Collection in LLVM**  
*Philip Reames (Speaker) - Azul Systems, Sanjoy Das - Azul Systems (Speaker)*  
[Slides](Slides/Reames-GarbageCollection.pdf)  
[Video](https://youtu.be/mdVR0RYJQ9w)  
Generating efficient code that is compatible with common high performance garbage collector implementations will strengthen LLVM's ability to support languages with managed runtime environments. To support this common use case, we have built and are in the process of contributing a safepoint insertion pass which can rewrite optimized IR into a form which respects the invariants required by a fully relocating garbage collector, and a set of intrinsics which enable work towards efficient lowering of safepoints. We'll cover the motivation, high level design, and show off some examples.

**Source Code Analysis for Security through LLVM**  
*Lu Zhao - HP Fortify*  
[Slides](Slides/Zhao-SourceCodeAnalysisforSecurity.pdf)  
[Video](https://youtu.be/xSN0J_JV06E)  
We added a new debug mode for the Clang compiler which emits extra metadata in the LLVM bitcode. The metadata has turned the bitcode into a useful vehicle from which an intermediate representation for secure source code analysis can be derived. We have used this approach to find security vulnerabilities in the Objective-C source code.

**FTL: WebKit’s LLVM based JIT**  
*Andrew Trick (Speaker) - Apple, Juergen Ributzka (Speaker) - Apple*  
[Slides](Slides/Trick-FTL.pdf)  
[Video](https://youtu.be/bnY5FVxHUVc)  
FTL is the fourth-tier LLVM JIT that powers JavaScript in WebKit. We will talk about our experiences using LLVM to build this high-performance JIT. We will explain the motivation for new LLVM features, including patchpoints and a new form of stack maps, and will share our vision on future work and the direction we would like LLVM move to become a better platform for JIT clients.

**Virtual Ghost: Using LLVM to Protect Applications from a Compromised Operating System**  
*John Criswell - University of Rochester*  
[Slides](Slides/Criswell-VirtualGhost.pdf)  
[Video](https://youtu.be/iVwShAxImHE)  
This talk presents an LLVM-based system named Virtual Ghost that protects applications from a compromised operating system kernel.  Virtual Ghost uses compiler instrumentation to protect application data from spying and corruption from the operating system kernel.  It also uses an extended version of the LLVM instruction set to restrict how the operating system kernel can interact with the hardware, preventing the operating system kernel from using hardware configuration to corrupt application control-flow or to bypass the application data protection guarantees.

**What does it take to make LLVM as performant as GCC**  
*James Molloy (Speaker) - ARM, Ana Pazos (Speaker) - QuIC, Yin Ma - QuIC*  
[Slides](Slides/Molloy-LLVM-Performant-As-GCC-llvm-dev-2014.pdf)  
[Video](https://youtu.be/EsNMa9nxLOk)  
For the past 7 months Qualcomm and ARM have jointly been analyzing and improving performance for the AArch64 architecture in LLVM, based on a differential analysis against GCC. This talk aims to provide information on the areas that we're currently lacking compared to GCC, along with the progress that we've made so far.

**Blowing up the Atomic Barrier**  
*Robin Morisset (Speaker) - Google, JF Bastien - Google*  
[Slides](Slides/Morisset-AtomicsPresentation.pdf)  
[Video](https://youtu.be/cDM6Gr_XzGI)  
Atomics in C11 and C++11 let the programmer express the guarantees needed for racy accesses in lock-free code, in theory bringing a zero-cost abstraction for parallelism to the language. This talk will showcase how you can use atomics today and where the abstraction breaks down. We’ll focus on LLVM’s recent improvements for atomics that provide significant performance gains on ARMv7, Power and x86. Finally we’ll discuss some extremely non-intuitive behaviors of atomics, how atomics in C++ may evolve, and how it may impact LLVM.

**The LLVM Pass Manager, Part 2**  
*Chandler Carruth - Google*  
[Slides](Slides/Carruth-TheLLVMPassManagerPart2.pdf)  
[Video](https://youtu.be/6NDQl544yEg)  
I will present a new design and implementation of the LLVM pass manager that is currently being developed in the tree. I will cover how it differs from the previous implementation and how those differences allow it to solve many of the long-standing limitations of the current implementation. I will discuss in depth how the new system supports richer analysis dependencies, flexible composition of function-level analyses and module- or call-graph-level transformations. The new pass manager also introduces a caching-based scheduling model which is substantially different from the prior ones and critical to understanding the impact of transitioning. And as I go through these topics I will introduce how to write a pass suitable for the new infrastructure and how to port an existing pass to live happily in both.  
Finally, I will show a specific new call-graph analysis used by the new pass manager and discuss how these two components can be used to parallelize the entire LLVM compilation pipeline. I will mention some of the basic correctness and efficiency challenges faced when running in parallel and detail the specific challenges and constraints pursuing this path would impose on analysis and optimization passes.

**Supporting Vector Programming on a Bi-Endian Processor Architecture**  
*Bill Schmidt (Speaker) - IBM, Michael Gschwind - IBM*  
[Slides](Slides/Schmidt-SupportingVectorProgramming.pdf)  
[Video](https://youtu.be/y_YU5CxrxNo)  
The POWER instruction set architecture is designed to support both big-endian and little-endian memory models.  However, many of the instructions designed for vector support assume that vector elements in registers appear in big endian order, that is, with the lowest-numbered vector element in the most significant portion of the register.  This talk will outline some of the issues faced in designing a sensible vector programming model on a bi-endian architecture with a big-endian bias, and how we've addressed them.  We will also discuss the current status of implementation in the GCC and Clang/LLVM compilers.

**Intrinsics, Metadata and Attributes: Now, more than ever!**  
*Hal Finkel - Argonne National Laboratory*  
[Slides](Slides/Finkel-IntrinsicsMetadataAttributes.pdf)  
[Video](https://youtu.be/Zyeey4gkIg8)  
Over the past year, LLVM has grown several new ways to communicate important information to the optimizer: An @llvm.assume intrinsic function to provided additional truths, scoped-noalias metadata to provided explicit pointer aliasing sets, and parameter attributes that specify pointer alignment, dereferenceability, and more. I'll explain the semantics of many of these new features, their intended uses, and a few ways they shouldn't be used. Finally, I'll discuss how Clang exposes and leverages these new features to encourage the generation of higher-performance code.

**Implementing Data Layout Optimizations in LLVM Framework**  
*Prashantha NR (Speaker) - Compiler Tree Technologies, Vikram TV - Compiler Tree Technologies,    Vaivaswatha N - Compiler Tree Technologies*  
[Slides](Slides/Prashanth-DLO.pdf)  
[Video](https://youtu.be/Ckzole3hArc)  
Modern server workloads are limited by memory bandwidth. For regular accesses like loops, people change the loop iterations to change the access pattern; thereby gaining locality. Another way to alleviate the memory bottleneck is to change the data layout organization for better locality. In this talk we will speak about memory layout optimizations like Structure Splitting, Instance Interleaving, Struct Array copy, Array Remapping in LLVM compiler framework.

**Fuzzing Clang to Find ABI Bugs**  
*David Majnemer - Google*  
[Slides](Slides/Majnemer-FuzzingClang.pdf)  
[Video](https://youtu.be/0yUzo-pBkFk)  
Correctly implementing C++ is very hard, bugs can arise from incredibly subtle interactions of different language features. In this talk, we will discuss how we used fuzzing to dramatically increase the reliability of Clang's ABI-specific code.

**A closer look at ARM code quality**  
*Tilmann Scheller - Samsung Electronics*  
[Slides](Slides/Scheller-ARMCodeQuality.pdf)  
[Video](https://youtu.be/1DM2Q75qDSU)  
This talk presents current performance numbers for the SPEC CPU benchmark suites on ARM, comparing the performance of LLVM and GCC, with the main focus on the SPEC CPU integer benchmarks. To dive a little bit deeper, we will also have a closer look at the generated assembly code of selected benchmarks where LLVM is performing worse than GCC. We will use the results of this performance analysis to point out potential code generation opportunities for LLVM.

**Implementation of global instruction scheduling in LLVM infrastructure**  
*Sergei Larin (Speaker) - QuIC,  Aditya Kumar (Speaker) - QuIC*  
[Slides](Slides/Larin-GlobalInstructionScheduling.pdf)  
[Video](https://youtu.be/A88vO_lP5b8)  
Discuss perspectives and tradeoffs in implementation of global instruction scheduling and support for it in the LLVM infrastructure. Present and discuss relative QuIC experience.

**Skip the FFI: Embedding Clang for C Interoperability**  
*Jordan Rose (Speaker) - Apple, John McCall (Speaker) - Apple*  
[Slides](&lt;Slides/Skip the FFI.pdf&gt;)  
[Video](https://youtu.be/_xAqf-VwaOM)  
Most languages that aren't a superset of C provide a Foreign Function Interface (FFI) that allows one to interface with existing C libraries. FFIs are often an afterthought, requiring manual or source-to-source translation from C header files to a subset of the target language, resulting in complicated build processes, frequent manual tweaking, and numerous implementation challenges.   
This talk will discuss an alternative approach that embeds Clang into an LLVM-based compiler front end to provide C compatibility without the traditional FFI. Embedding Clang provides seamless access to C APIs, moving the translation of APIs from external tools into the compiler itself. Moreover, one can leverage Clang's deep knowledge of C record layout and calling conventions to simplify the C interface and make both bring up and porting of a new compiler front end simpler.

**Custom Hardware State-Machines and Datapaths: Using LLVM to Generate FPGA Accelerators**  
*Alan Baker - Altera Corporation*  
[Slides](Slides/Baker-CustomHardwareStateMachines.pdf)  
[Video](https://youtu.be/DGWFQXK_EU4)  
Altera Corporation’s OpenCL compiler uses LLVM to generate FPGA accelerators. In order to generate efficient hardware, many transformations were implemented. The key transformations will be discussed, emphasizing the FPGA vs CPU architectural differences that motivate them.

**Controlling Virtual Register Pressure in LLVM Middle-End**  
*Ivan Baev - QuIC*  
[Slides](Slides/Baev-Controlling_VRP.pdf)  
[Video](https://youtu.be/lJmXiwJo2ZQ)  
Enabling new compiler optimizations or compiling at higher optimization levels do not necessarily improve performance. One common reason is the increased register pressure that results in an increased amount of spill code. We analyze several LLVM target-independent optimizations with respect to register pressure. We then describe algorithms for controlling register pressure in LICM and GVN and report their positive impact on run-time performance. A discussion on how to control register pressure in the inliner concludes the talk.

**Indexing Large, Mixed-Language Codebases**  
*James Dennett - Google, Luke Zarko (Speaker) - Google*  
[Slides](Slides/Zarko-IndexingLargeMixedLang.pdf)  
[Video](https://youtu.be/KDiXo5GwQ-U)  
The Kythe project aims to establish open data formats and protocols for interoperable developer tools. In this talk, we will introduce the Kythe model as it applies to C++14, concentrating on features required for generating cross-references. In the process, we will discuss how the Clang front-end was instrumental in developing an indexing tool that produces Kythe data describing C++ source code.

**Architecture Specific Code Generation and Function Multiversioning**  
*Eric Christopher - Google*  
[Slides](&lt;Slides/Christopher-Function Multiversioning Talk.pdf&gt;)  
[Video](https://youtu.be/iAaoGsCVeCI)  
A talk on microarchitecture dependent optimization and code generation for individual functions, the changes that have been necessary to enable it, and function multiversioning as the next step.

**Frappé: Using Clang to Query and Visualize Large Codebases**  
*Nathan Hawes (Speaker) - Oracle, Ben Barham (Speaker) - Oracle*  
[Slides](Slides/Hawes-Frappe.pdf)  
[Video](https://youtu.be/xelhxXfqngc)  
Frappé is a new tool to support developers with a range of code comprehension queries in multi-million line codebases, from "Does function X or something it calls write to global variable Y?" to "How much code could be affected if I change this macro?".  Results are overlaid on a visualisation of the code based on a cartographic map, where the continent/country/state hierarchy corresponds to the code equivalent: high-level architectural components down to individual files and functions. This allows users to visually filter results based on their location and more immediately guage their number and locality.

# Lightning Talk Abstracts

**Automatic Loop Diagonalization with LLVM**  
*Vedant Kumar - UC Berkeley*  
[Slides](Slides/Kumar-LoopDiagonalization.pdf)  
The effects of some loops can be captured by matrices. This talk shows how to take advantage of this fact to optimize away entire loops.

**PBQP register allocation**  
*Arnaud de Grandmaison - ARM,  Lang Hames - Apple*  
[Slides](Slides/PBQP-update-and-in-the-wild.pdf)  
The PBQP register allocator has been part of the LLVM source code for a long time. This talk will present a high level overview of the PBQP allocator principles, as well as its status and future work.

**PBQP register allocation in the wild**  
*Arnaud de Grandmaison - ARM,  Lang Hames - Apple*  
[Slides](Slides/PBQP-update-and-in-the-wild.pdf)  
This talk will present how the PBQP is used with 2 real world processors and report some performance numbers.

**Link-Time Optimization on PlayStation(R)4**  
*Yunzhong Gao - Sony Computer Entertainment America*  
[Slides](Slides/Gao-LTO-lightning-talk.pdf)  
As a follow-up to last year's presentation, this is a talk on our experience implementing LTO on PlayStation(R)4’s proprietary linker, including some of the challenges and results we see in the games.

**Software Visualizer (SWViz): A tool for visually exploring Linux kernel with Clang**  
*Harsh Vardhan Dwivedi - QuIC*  
[Slides](Slides/Dwivedi-SWViz.pdf)  
What is SWviz and why should I care about it anyway? SWViz is a tool to explore the call graph of a program. It’s chief advantage being able to leverage the linker and compiler (Clang) to generate accurate call-graphs. Through use of Swviz one can quickly gain an understanding of how a program is working. This leads to a massive cutdown in number of hours spent understanding the call-flow of any mature codebase. We’ll demonstrate use of SWViz with Linux Kernel.

**LLVM for Interactive Modeling and High Performance Simulation**  
*Peng Cheng - The MathWorks, Inc.*  
[Slides](Slides/Cheng-InteractiveModeling.pdf)  
At MathWorks, LLVM has been used to create multi-thread JIT engines for interactive modeling and high performance simulation.  This talk will present why and how LLVM is used to implement the JIT engines as well as some challenges.

**AddressSanitizer for Windows**  
*Timur Iskhodzhanov - Google*  
[Slides](&lt;Slides/ASan for Windows.pdf&gt;)  
A fast memory error detector, now available to try on Windows. Brief overview of the internals and some initial deployment results.

# Tutorial Abstracts

**Building an LLVM Backend**  
*Fraser Cormack (Speaker) - Codeplay Software, Pierre-André Saulais (Speaker) - Codeplay Software*  
[Slides](Slides/Cormack-BuildingAnLLVMBackend.pdf)  
[Video](https://youtu.be/b53WqCbLEYg)  
This talk explains how to get started with building a LLVM backend for a new architecture. It shows how LLVM transforms programs through the back-end compilation pipeline and what needs implementing for a new target. Practical debugging tips, as well as solutions to common issues are given. No LLVM backend experience is needed, but experience with LLVM IR is recommended.

**Adding and Optimizing a Subtarget for MIScheduler**  
*Dave Estes (Tutorial) - QuIC*  
[Slides](Slides/Estes-MISchedulerTutorial.pdf)  
[Video](https://youtu.be/Uge_whHVmtM)  
Tutorial for adding a subtarget to an existing backend for use with the MIScheduler. Will cover TableGen basics insofar as understanding the records used for the MachineSchedModel. Will provide strategies on how to best model some basic machine architectures.

**Debug Info Tutorial**  
*Eric Christopher (Speaker) - Google, David Blaikie (Speaker) - Google*  
[Slides](Slides/Christopher-DebugInfoTutorial.pdf)  
[Video](https://youtu.be/_wqX9H2A66M)  
Take a walk through the DWARF debug information format and the llvm APIs that serve as an interface to emitting debug information for your language.

# BoF Abstracts

**JIT Support in LLVM**  
*Lang Hames - Apple*  
A forum for clients and developers of LLVM's JIT infrastructure to discuss APIs, features, and intrinsic support (the stackmap and patchpoint intrinsics).

**Performance tracking & benchmarking infrastructure**  
*Kristof Beyls - ARM, Chad Rosier - QuIC, Chris Matthew - Apple, Tobias Grosser - ETH, Renato Golin - Linaro*  
Having at least some public performance tracking that the majority of the community cares about would make it easier to collaborate for all developers improving the quality of LLVM-generated code. During last year’s BoF, we identified some key shortcomings in LNT to be able to produce low-noise performance numbers on the test-suite and most of them have been fixed recently. In this BoF, we wish to mainly talk about what is needed and missing for the produced compile and execution time numbers to be quickly and easily interpreted and acted upon.

**Debug Info BOF**  
*Eric Christopher, Google*  
There's been quite a bit of interest in a Debug Info BOF following the one we had last year at the 2013 Developer Conference. This BOF will cover everything from scaling our current handling of debug information, to ongoing work on debug information correctness, and future proposals for DWARF standardization.

**Improving LLVM for remote test execution**  
*Brian Rzycki - Samsung Austin R&D Center*  
Today's LLVM testing frameworks focus on testing native compilers on the same host where the test is compiled. The goal of this BoF is to examine the components necessary for change and to discuss potential solutions that allow for running tests on remote hosts in a way that best benefits the overall community.

**Future directions and features for LLDB**  
*Deepak Mathews Panickal - Codeplay Software*  
I propose to organize a BoF to discuss mainly the following topics:

*   As a variety of new targets are being added that form parts of widely used heterogeneous devices, LLDB should develop a system to allow for Simultaneous Multiple Target Debugging. This would allow for the definition of behaviours for how heterogeneous systems are debugged in a single instance.
*   Future advances of LLDB tools such as the MI interface and lldb-gdbserver, NativeProcess, NativeThread etc.

**GPU Implementers BoF**  
*Tom Stellard - AMD, Owen Anderson - Apple*  
LLVM is rapidly gaining popularity as a compilation framework for graphics processors.  This Birds of a Feather session will focus on issues of interest to implementers of GPU targets in LLVM.  Topics of discussion may include:

*   Techniques for overcoming common challenges in adapting LLVM to GPU targets
*   Future directions in LLVM to benefit GPU targets
*   Opportunities for different GPU targets to share infrastructure and/or optimizations

Audience participation is encouraged.  Bring your own questions and ideas!

**LLVM Inliner Improvements**  
*Yin Ma - QuIC, Ana Pazos - QuIC, Jiangling Liu - ARM*  
Discuss the opportunities to extend the LLVM inliner and our work greedy inliner.

**LTO**  
*Tony Linthicum - QuIC, Dan Palermo - QuIC*  
Discuss LTO’s current state and potential future improvements.  Potential topics include, but are not limited to, the following:   passing command line arguments to LTO,  profile driven LTO optimizations,  compile time improvements and  performance improvements.

**Lld**  
*Shankar Easwaran - QuIC, Daniel Stewart - QuIC*  
The lld linker is a solid foundation for a general-purpose linker, as well as a set of libraries for creating linker-like tools. We will talk about the current status of lld, what the shortcomings are for a production linker, and what major areas need to be implemented, such as LTO support, diagnostics, extensibility. We will also discuss the feasibility of targeting an initial set of features so that lld can be made the default linker for linking the LLVM tools

# Poster Abstracts

**LLVM for Interactive Modeling and High Performance Simulation**  
*Peng Cheng, Nathan Brewton, Dale Martin - The MathWorks, Inc.*  
[Poster](Slides/Cheng-InteractiveModelingPoster.pdf)  
To enable inter-module optimization during interactive modeling for high performance simulation of Simulink models, LLVM based JIT compilers have been developed at MathWorks.  These JIT compilers support multiple threads on major platforms, including win32, win64, glnax64, and maci64, and achieve superior running time performance compared with previous shared library based compilers. This talk will present why and how LLVM is used to implement the JIT compilers as well as some challenges.

**ISPC: clang-based front-end**  
*Dmitry Babokin - Intel Corporation James Brodman - Intel Corporation*  
[Poster](Slides/Babokin-ISPC_clang.pdf)  
ISPC is a C-based language based on the SPMD (single program, multiple data) programming model that generates efficient SIMD code for modern processors without the need for complex analysis and autovectorization. The project uses the LLVM infrastructure for optimization and code generation but originally used a custom front-end. The poster describes our experience with building a clang-based front-end and the engineering problems we have encountered introducing the concept of “varying” types to clang.

**A C++ ABI Test Suite**  
*Sunil Srivastava - Sony Computer Entertainment*  
[Poster](Slides/Srivastava-ABI-testsuite_poster.pdf)  
This poster describes the design of an Itanium C++ ABI Test Suite that verifies a compiler’s compliance against the ABI specification to ensure link compatibility.

**Software Visualizer (SWViz): A tool for visually exploring Linux kernel with Clang**  
*Harsh Vardhan Dwivedi - QuIC*  
[Poster](Slides/Dwivdei-SWVizPoster.pdf)  
What is SWviz and why should I care about it anyway? SWViz is a tool to explore the call graph of a program. It’s chief advantage being able to leverage the linker and compiler (Clang) to generate accurate call-graphs. Through use of Swviz one can quickly gain an understanding of how a program is working. This leads to a massive cutdown in number of hours spent understanding the call-flow of any mature codebase. We’ll demonstrate use of SWViz with Linux Kernel.

**Machine Guided Compilation and Compiling to Minimize Energy Usage**  
*Simon Cook - Embecosm, Ed Jones - Embecosm*  
[Poster](Slides/Cook-mageecPoster.pdf)  
Today we need compilers to optimize for energy rather than just size or speed. In this poster we present the results of integrating machine learning with LLVM, so the compiler can be trained on which optimizations minimize energy. As a side effect of energy optimization we also see significant performance benefits - nearly doubling performance compared to -O3 in some cases.

**Translating Java into LLVM IR to Detect Security Vulnerabilities**  
*Cristina Cifuentes - Oracle Labs Australia, Oracle, Nathan Keynes - Parfait, Oracle, John Gough - Oracle Labs Australia, Oracle, Diane Corney - Oracle Labs Australia, Oracle, Lin Gao - Parfait, Oracle, Manuel Valdiviezo - Parfait, Oracle, Andrew Gross - Java Security, Oracle*  
[Poster](Slides/Cifuentes-TranslatingJava.pdf)  
This poster describes one of several new Java security vulnerabilities and how we reused and extended LLVM’s IR in order to detect such vulnerability.  One year later, full support for Java 7 and 8 are in place, along with various analyses that detect Java platform vulnerabilities.

**Intel® AVX-512 architecture evolution and support in Clang/LLVM**  
*Zinovy Nis - Intel Corporation, Robert Khasanov - Intel Corporation*  
[Poster](Slides/Nis-AVX-512ArchPoster.pdf) Intel® AVX-512 vector ISA continues to evolve. It has recently been enriched with new groups of instructions operating on different vector lengths and different vector element sizes. We’ll present the current status of new AVX-512 features enabling in CLANG/LLVM  and show how these features can be exploited for performance improvements particularly by vectorizer.

**mcsema**  
*Artem Dinaburg - Trail of Bits, Inc. Andrew Ruef - Trail of Bits, Inc. Jay Little - Trail of Bits, Inc.*  
[Poster](Slides/McSemaPoster.pdf)  
mcsema is a framework for analyzing and transforming machine-code programs to LLVM bitcode. It supports translation of x86 machine code, including integer, floating point, and SSE instructions.

**Carte++: A LLVM-Based Compiler Targeting FPGAs**  
*Jeffrey Hammes, Lisa Krause , Matthew O’Connor, Jon Steidel - SRC Computers, LLC*  
[Poster](Slides/Krause-CartePoster.pdf)  
SRC Computers, LLC is presenting a poster on its upcoming Carte++ compiler release showing how the Clang/LLVM infrastructure has provided full language support and a rich set of compiler optimizations upon which to build the Carte++ code generator. The poster will illustrate specific optimizations and compiler challenges unique to SRC's FPGA-based hardware.

# Logistics

[DoubleTree by Hilton San Jose](http://doubletree3.hilton.com/en/hotels/california/doubletree-by-hilton-hotel-san-jose-JOSE-DT/index.html)  
2050 Gateway Place  
San Jose, CA 95110

You may book their hotel stay by using this [link](https://resweb.passkey.com/go/LLVM2014).

Rate: $209 plus local taxes for superior double queen or superior king rooms

Self Parking is $19 per day.

<!-- *********************************************************************** -->

* * *
