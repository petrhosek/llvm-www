---
layout: "default.html"
permalink: "devmtg/2012-11/index.html"
---
# 2012 LLVM Developers' Meeting

1.  [Presentations and Posters](#content)
2.  [Talk Abstracts](#abstracts)
3.  [Poster Abstracts](#poster)

*   **What**: The sixth general meeting of LLVM Developers and Users.
*   **When**: November 7-8, 2012
*   **Where**: Fairmont, 170 South Market Street, San Jose, CA

## **SPONSORED BY: [Apple](http://apple.com), [QuIC](http://www.qualcomm.com/quicinc/), [Google](http://www.google.com)**, [Intel](http://intel.com)

The meeting served as a forum for [LLVM](http://llvm.org), [Clang](http://clang.llvm.org), [LLDB](http://lldb.llvm.org) and other LLVM project developers and users to get acquainted, learn how LLVM is used, and exchange ideas about LLVM and its (potential) applications. More broadly, we believe the event will be of particular interest to the following people:

*   Active developers of projects in the LLVM Umbrella (LLVM core, Clang, LLDB, libc++, compiler\_rt, klee, dragonegg, etc)
*   Anyone interested in using these as part of another project
*   Compiler, programming language, and runtime enthusiasts
*   Those interested in using compiler and toolchain technology in novel and interesting ways

We also invite you to sign up for the [official Developer Meeting mailing list](http://lists.llvm.org/mailman/listinfo/llvm-devmeeting) to be kept informed of updates concerning the meeting.

# Presentations and Posters

| Media | Talk Information |
| --- | --- |
| [Slides](Lattner-Kickoff.pdf) | **Welcome**<br>Chris Lattner, *Apple* |
| [Slides](Finkel-LLVMClangSupercomputer.pdf) [Video](https://youtu.be/8_XYt8rbzRk) | **[LLVM and Clang on the Most Powerful Supercomputer in the World](#talk1)**<br>Hal Finkel, *Argonne National Laboratory* |
| [Slides](Northover-AArch64.pdf) [Video](https://youtu.be/rvrHmrtZz-g) | **[The AArch64 backend: status and plans](#talk2)**<br>Tim Northover, *ARM* |
| [Slides](Gribenko_CommentParsing.pdf) [Video](https://youtu.be/DzRq9Dy0b9c) | **[Parsing Documentation Comments in Clang](#talk3)**<br>Dmitri Gribenko, *HPC Center at National Technical University of Ukraine "Kiev Polytechnic Institute"* |
| [Slides](Serebryany_TSan-MSan.pdf) [Video](https://youtu.be/HDgttiIvMxA) | **[MemorySanitizer, ThreadSanitizer. Scalable run-time detection of uninitialized memory reads and data races with LLVM instrumentation.](#talk4)**<br>Kostya Serebryany, *Google* |
| [Slides](Santosh-Vellvm.pdf) [Video](https://youtu.be/cnwPI07R8Iw) | **[Verified LLVM: Formalizing the semantics of the LLVM Intermediate Representation for Verified Program Transformations](#talk5)**<br>Santosh Nagarakatte, *University of Pennsylvania/Rutgers University* |
| [Slides](Gregor-Modules.pdf)<br>[Video](https://youtu.be/586c_QMXir4) | **[Modules](#talk6)**<br>Doug Gregor, *Apple* |
| [Slides](Carlson-FromSource.pdf) [Video](https://youtu.be/9GSDwFRGuZw) | **[Integrated Security, using LLVM for Dynamic and Static Security Tasks](#talk7)**<br>Jared Carlson, *GoToTheBoard* |
| [Slides](Beaumont-Gay-Diagnostics.pdf) [Video](https://youtu.be/j2e6VkFU_QE) | **[How good are Clang's diagnostics, anyway?](#talk8)**<br>Matt Beaumont-Gay, *Google* |
| [Slides](Gohman-AliasAnalysis.pdf) [Video](https://youtu.be/gxt-uCu7Sxo) | **[Alias Analysis in LLVM](#talk9)**<br>Dan Gohman, *Google* |
| [Slides](Sharlet-ShevlinPark.pdf)<br>[Video](https://youtu.be/W2Fn7ERMJJE) | **[Shevlin Park: A C++ AMP implementation in Clang/LLVM using OpenCL](#talk10)**<br>Dillon Sharlet, *Intel* |
| [Slides](Hongbin-Generating.pdf) [Video](https://youtu.be/jvyh9xKkwKg) | **[Generating Hardware Description with the Target-Independent Code Generator](#talk11)**<br>Hongbin Zheng, *Sun Yat-sen University* |
| [Slides](Carruth-OptimizingAbstractions.pdf)<br>[Video](https://youtu.be/qe-TT3r_ke4) | **[Zero-Cost Abstractions and Future Directions for Modern Optimizing Compilers](#talk12)**<br>Chandler Carruth, *Google* |
| [Slides](Zaks-Rose-Checker24Hours.pdf) [Video](https://youtu.be/kdxlsP5QVPw) | **[Building a Checker in 24 hours](#talk13)**<br>Anna Zaks, *Apple*, Jordan Rose, Apple |

**Lightning Talks:**

| Media | Talk Information |
| --- | --- |
| [Slides](Martinez_ProjectDependencies.pdf)<br>[Video](https://youtu.be/2UxteuA8r6c) | **Project Dependency Impact on Clang’s Build Time**<br>Javier Martinez |
| [Slides](Criswell_AutomatedDefense.pdf)<br>[Video](https://youtu.be/JAR9rFqmn4Y) | **Clang and LLVM for Automated Defense (and Great Justice)**<br>John Criswell |
| [Slides](Weber_TypeAwareMemoryProfiling.pdf)<br>[Video](https://youtu.be/6_snVFhOSJk) | **A Prototype for Fast Type-Aware Memory Profiling**<br>Nico Weber |
| [Slides](Gribenko_MPITypeSafety.pdf)<br>[Video](https://youtu.be/-pxiJpMGm5w) | **Statically Checking MPI Type Safety**<br>Dmitri Gribenko |
| [Slides](Tzannes_ParallelismAnnotations.pdf)<br>[Video](https://youtu.be/wr-BcUGtFQY) | **Annotations for Safe Parallelism**<br>Alexandros Tzannes |
| [Slides](Keryell_SoSlang.pdf)<br>[Video](https://youtu.be/h7aoPWjVxKA) | **SoSlang**<br>Ronan Keryell |
| [Slides](Abbey_Bitcode.pdf)<br>[Video](https://youtu.be/XWR5UHiogmA) | **Bitcode compatibility**<br>Joe Abbey |
| [Slides](Humphreys-LLVMTI.pdf)<br>[Video](https://youtu.be/WVI2JgoRm9U) | **Evaluating LLVM for Texas Instruments DSPs**<br>Jonathan Humphreys |

**BOFs:**

<!-- FIXME: Should use a class tag, not be keyed off "devmtg" id -->

| Media | BOF Information |
| --- | --- |
|  | **BOF: Polly: A loop Nest Optimizer for LLVM**<br>Zino Benaissa, *QuIC* |
|  | **BOF: SelectionDAG & DAGCombiner - how can they be improved?**<br>James Molloy, *ARM* |
| [Slides](Larin-Trick-Scheduling.pdf) | **BOF: Instruction scheduling for Superscalar and VLIW platforms. Temporal perspective**<br>Sergei Larin, *QuIC*, Andy Trick, *Apple* |
|  | **BOF: SPIR - A Standard Portable IR for OpenCL Kernel Language**<br>Boaz Ouriel, *Intel* |
|  | **BOF: Memory Safety, Debugging Tools, and Automated Defenses**<br>Santosh Nagarakatte, *Rutgers University*, John Criswell, *University of Illinois* |
| [Slides](Rotem-VectorizationBOF.pdf) | **BOF: Vectorization in LLVM**<br>Nadav Rotem, *Apple* |

**Posters:**

| Media | Poster Information |
| --- | --- |
| [Poster](Serebryany-ASAN-TSAN-Poster.pdf) | **[MemorySanitizer, ThreadSanitizer](#poster1)**<br>Kostya Serebryany, *Google* |
| [Poster](Strecker-Vuo.pdf) | **[Vuo: Visual programming for multimedia artists](#poster2)**<br>Jaymie Strecker, *Kosada* |
| [Poster](Ahrens-ScoutPoster.pdf) | **[Scout: Using Clang/LLVM to Build A Domain-Specific Language for In Situ Data Analysis and Visualization on Emerging Architectures](#poster3)**<br>Christine Ahrens, *Los Alamos National Laboratory* |

# Talk Abstracts

**LLVM and Clang on the Most Powerful Supercomputer in the World**  
*Hal Finkel - Argonne National Laboratory*  
The IBM Blue Gene/Q (BG/Q) now holds the first and third slots on the Top500 list of the world's most powerful supercomputers, and LLVM with Clang now provides a high-quality autovectorizing C/C++ compiler for the BG/Q. In this talk, I'll describe the process of porting LLVM and Clang to the BG/Q, and how the LLVM IR is mapped to the BG/Q's unique vector instruction set. This process has required enhancements to all levels: From the PowerPC backend through the frontend, including the development of the basic-block autovectorizer. I will demonstrate that, for a large class of codes, LLVM with Clang produces code with superior performance compared to that produced by the vendor-supplied compilers.

**The AArch64 backend: status and plans**  
*Tim Northover - ARM*  
A backend for ARM’s new 64-bit architecture, AArch64, will very soon be added to LLVM. I intend to discuss what we’ve done to make sure it is a good base for future work: correct, extensible and useful. I will talk about areas we’ve found easy to test and the more challenging corners. The MC Hammer suite introduced at the Euro-LLVM conference ensured the completeness and correctness of encoding information, and to a lesser extent, assembly. Difficult corners I will give more details on are the usual suspects: instruction selection, relocations and the constant island pass.  
As well as our testing methodology I will mention some idiosyncrasies of both the architecture and backend, and suggest potentially interesting future projects of varying sizes in optimisation and features for AArch64. I’ll describe some of the facilities already available for those wanting to work on the backend and what they can expect from it already: roughly speaking, correct compilation of standard C and C++ code with Clang. I will also describe some of our own plans for improving the backend and the goals we have for it in the medium term.

**Parsing Documentation Comments in Clang**  
*Dmitri Gribenko - HPC Center at National Technical University of Ukraine "Kiev Polytechnic Institute"*  
The documentation written in comments is usually processed by a third-party tool while the compiler just ignores it, but the compiler could extract some extra information from it. We could use documentation from comments to enhance tools based on Clang libraries. Now Clang does additional semantic checking on documentation and emits warnings to help the programmer ensure that comments don't get stale. Code completion APIs now include documentation associated with each completion result. libclang is enhanced with an API to get the documentation attached to any declaration; this could be used to build a Clang-based Doxygen-like tool.  
In future, when we try to tackle automatic refactoring, we could use this framework to update names referenced in comments so that documentation stays up to date.

**MemorySanitizer, ThreadSanitizer. Scalable run-time detection of uninitialized memory reads and data races with LLVM instrumentation**  
*Kostya Serebryany - Google*  
Following the success of AddressSanitizer (asan), a fast detector of use-after-free and buffer overflow bugs, we have developed two more bug detection tools based on similar ideas. MemorySanitizer (msan, http://code.google.com/p/memory-sanitizer/) detects uninitialized memory reads. It shares many ideas with Valgrind/Memcheck, however it is also different in two important ways: it uses compile-time instrumentation (LLVM) and 1:1 direct shadow memory mapping. Unless the entire program (including libc) is instrumented, msan requires a simple binary instrumentation component (we have an implementation based on DynamoRIO). The slowdown introduced by the tool is typically 2x-3x (compare to Valgrind's 20x). ThreadSanitizer (tsan, http://code.google.com/p/thread-sanitizer/) detects data races. The tool has been briefly mentioned at the 2011 llvm dev meeting but has matured since that time. Similarly to asan and msan, it uses compile-time instrumentation (LLVM), but 95% of the logic is contained in the run-time library. Tsan uses 1:4 direct shadow memory mapping (i.e. uses ~5x more memory). It does not have locks or atomic instructions on the fast path, which makes it scale to large and heavily threaded applications. The slowdown varies between 3x and 10x.

**Verified LLVM: Formalizing the semantics of the LLVM Intermediate Representation for Verified Program Transformations**  
*Santosh Nagarakatte - University of Pennsylvania/Rutgers University*  
This talk will describe our research on building Vellvm (verified LLVM), a framework for reasoning about programs expressed in LLVM’s intermediate representation and transformations that operate on it. Vellvm provides a mechanized formal semantics of LLVM’s intermediate representation, its type system, and properties of its SSA form. The framework is built using the Coq interactive theorem prover. It includes multiple operational semantics and proves relations among them to facilitate different reasoning styles and proof techniques. To validate Vellvm’s design, we extract an interpreter from the Coq formal semantics that can execute programs from LLVM test suite and thus be compared against LLVM reference implementations.  
This talk will also highlight Vellvm’s practicality by demonstrating our efforts in formalizing and verifing a variant of mem2reg optimization within the LLVM compiler suite, and our previoulsy proposed SoftBoundCETS memory safety transformation operating on the LLVM IR. The talk will conclude highlighting the benefits of such formalization efforts to expose compiler bugs and the avenues such a formalizing effort can benefit from compiler developer involvement.  
Joint work with Jianzhou Zhao, Milo M K Martin and Steve Zdancewic at the University of Pennsylvania.

**Modules**  
*Doug Gregor - Apple*  
The C preprocessor has long been a source of problems for programmers and tools alike. Programmers must contend with widespread macro pollution and include-ordering problems due to ill-behaved headers. Developers habitually employ various preprocessor workarounds, such as LONG\_MACRO\_PREFIXES, include guards, and the occasional #undef of a library macro to mitigate these problems. Tools, on the other hand, must cope with the inherent scalability problems associated with parsing the same headers repeatedly, because each different preprocessing context could effect how a header is interpreted---even though the programmer rarely wants it. Modules seeks to solve this problem by isolating the interface of a particular library and compiling it (once) into an efficient, serialized representation that can be efficiently imported whenever that library is used, improving both the programmer's experience and the scalability of the compilation process.

**Integrated Security, using LLVM for Dynamic and Static Security Tasks**  
*Jared Carlson - GoToTheBoard*  
This talk will discuss how to leverage the LLVM and LLDB tools and technologies to create a flexible security infrastructure. The talk discusses incorporating both static and dynamic analysis techniques by using LLVM and LLDB components and that these can easily be integrated back into LLVM development workflow. These tools will help find exploitable bugs within the llvm development environment, illustrate their consequences and are customizable and easily shared within the community.  
Funded by DARPA as a Cyber Fast Track effort, we are currently incorporating LLDB and other open source python libraries along with re-written static analysis scripts so that the tools can be easily integrated and altered into a workflow. It is anticipated that milestone two, an alpha, will be finished in early September and then the project will wrap up in early November with a beta release.  
The talk will discuss how we use the tools to investigate bug severity, utilize artificial intelligence techniques to predispose fuzzing, draw conclusions, and utilize the LLVM technology quite to target various architectures if desired.

**How good are Clang's diagnostics, anyway?**  
*Matt Beaumont-Gay - Google*  
Most of the feedback we get on Clang’s diagnostics is in the form of bug reports (or occasionally people saying nice things about us on the Internet). As developers, we also eat our own proverbial dogfood, and we can assess new diagnostics against various open-source and proprietary codebases, but we don’t have a large-scale view into the diagnostics experience for code that’s under development.  
The build system for Google’s shared codebase keeps all of the output for all of the builds that we do. So, like a good Google engineer, I wrote a MapReduce, using the build result store as input. We now have a daily batch job that crunches through all of the compiler stderr from the last day, parses out detailed, structured information about the diagnostics that Clang produced, and writes the information into a database for later analysis. I’ll discuss the design of the MapReduce, touch on the various pieces of infrastructure that make it work, and present results on the diagnostics seen by Google engineers in their day-to-day work.

**TBAA in LLVM**  
*Dan Gohman - Google*  
LLVM’s Type-Based Alias Analysis framework enables more aggressive optimization for the C family of languages, and it can also be used by other language frontends.

**Shevlin Park: A C++ AMP implementation in Clang/LLVM using OpenCL**  
*Dillon Sharlet - Intel*  
We describe “Shevlin Park”, a prototype implementation of Microsoft’s C++AMP built on CLANG, LLVM, and OpenCL. We fully describe Shevlin Park’s implementation including how CLANG/LLVM can be augmented to easily accommodate C++AMP programming constructs, how C++AMP computation can be expressed as OpenCL compute kernels, and finally how the C++AMP runtime library can be easily implemented on an OpenCL runtime. Using several benchmarks, we evaluate Shevlin Park’s performance, Microsoft’s DirectX based C++AMP, and also conventional OpenCL.

**Generating Hardware Description with the Target-Independent Code Generator**  
*Hongbin Zheng - Sun Yat-sen University*  
Though there exist several projects generating hardware description from LLVM IR (i.e. High-level Synthesis, HLS), they are all working on the LLVM IR layer. However, the LLVM IR layer is not the best layer to perform HLS.  
In this talk, I am going to introduce our open source HLS framework, named Shang. Our HLS framework mainly implements its transformations and analyses in the Target-Independent Code Generator, with the HLS-specific TargetMachine, named VTargetMachine.

**Zero-Cost Abstractions and Future Directions for Modern Optimizing Compilers**  
*Chandler Carruth - Google*  
Today, Clang is a fantastic C++ optimizing compiler. It leverages all of the compiler infrastructure built as part of the LLVM project and produces binaries which have excellent performance. As compiler writers, we have done our jobs very well. So what’s next? Where is the next big opportunity for optimizing compilers, especially in the context of modern C++ code?  
As C++ becomes more popular, and the C++ code bases of the world become larger and more modern, we are faced with some interesting optimization challenges. C++ is popular today due to its excellent performance, but too often certain aspects of this performance rely on hand-tuned code, despite the often elusive promise of C++ providing zero-cost abstractions to programmers. In practice, the abstractions of modern C++ are not in fact zero-cost. This creates a serious danger, as the design of C++, the standard library, and many user libraries, all rely upon the abstractions they introduce having zero cost to allow layering and composing them without a combinatorial explosion of overhead. We are approaching a world where the overheads and costs our compilers fail to remove from abstractions will be magnified into the reality of Wirth’s Law: our software is getting slower more rapidly than hardware becomes faster.  
How do we reverse this trend? We must begin to focus optimizations on decomposing the abstractions formed in modern languages. It is these abstractions, the things which programmers naively expect to be free, which lead to the most surprising and difficult to correct performance problems. These are what must be compiled optimally to allow both idiomatic and common programming patterns to remain efficient and to achieve system wide performance improvements in a world of flat profiles. In this talk, I will walk through what some of these abstractions end up looking like in modern C++ code, explain several ways in which LLVM optimizes away these abstractions, and propose several new optimizations to further address these problems.

**Building a Checker in 24 hours**  
*Anna Zaks - Apple, Jordan Rose - Apple*  
Clang Static Analyzer (http://clang-analyzer.llvm.org/) is a bug finding tool based on path sensitive symbolic execution of user code. We are going to introduce basic concepts behind the analyzer and describe what it takes to write a new check.

# Poster Abstracts

**MemorySanitizer, ThreadSanitizer Poster**  
*Kostya Serebryany - Google*  
Following the success of AddressSanitizer (asan), a fast detector of use-after-free and buffer overflow bugs, we have developed two more bug detection tools based on similar ideas. MemorySanitizer (msan, http://code.google.com/p/memory-sanitizer/) detects uninitialized memory reads. It shares many ideas with Valgrind/Memcheck, however it is also different in two important ways: it uses compile-time instrumentation (LLVM) and 1:1 direct shadow memory mapping. Unless the entire program (including libc) is instrumented, msan requires a simple binary instrumentation component (we have an implementation based on DynamoRIO). The slowdown introduced by the tool is typically 2x-3x (compare to Valgrind's 20x). ThreadSanitizer (tsan, http://code.google.com/p/thread-sanitizer/) detects data races. The tool has been briefly mentioned at the 2011 llvm dev meeting but has matured since that time. Similarly to asan and msan, it uses compile-time instrumentation (LLVM), but 95% of the logic is contained in the run-time library. Tsan uses 1:4 direct shadow memory mapping (i.e. uses ~5x more memory). It does not have locks or atomic instructions on the fast path, which makes it scale to large and heavily threaded applications. The slowdown varies between 3x and 10x.

**Vuo: Visual programming for multimedia artists**  
*Jaymie Strecker - Kosada*  
Vuo is a new programming environment for multimedia artists. We’re building Vuo’s compiler and linker on top of LLVM. We chose LLVM because LLVM makes it easy to add features that multimedia artists enjoy — features that would have taken months or years to write from scratch.  
Why do multimedia artists need a programming environment? Because very often their job is to create software: interactive art and music, animations, visualizations, games, special effects, museum exhibits, and kiosks. Yet their background is in art or music, not programming. Many multimedia artists get around this by using programming environments where, instead of typing a program, they drag-and-drop building blocks onto a canvas and draw lines to connect them. These “node-based” or “visual” programming environments include Max, VVVV, Quartz Composer — and, soon, Vuo.  
LLVM is helping Vuo become more powerful and flexible. Vuo programs are compiled and therefore faster than interpreted programs — thanks to LLVM’s APIs for code generation and optimization. Vuo programs will be able to target Mac, Windows, Linux, iOS, and Android — thanks to LLVM’s support for various targets. Vuo developers will be able to write new building blocks in C and, eventually, other languages (e.g. C#, Python, JavaScript, PHP, Lua) — thanks to LLVM’s many frontends and Mono’s LLVM backend.  
LLVM solves problems of parsing and code generation so we don’t have to. Instead, we can focus on adding features that multimedia artists appreciate, like live coding (the ability to edit a program while it’s running) and easy debugging. LLVM is helping Vuo become flexible, feature-rich, and fun.

**Scout: Using Clang/LLVM to Build A Domain-Specific Language for In Situ Data Analysis and Visualization on Emerging Architectures**  
*Christine Ahrens - Los Alamos National Laboratory*  
As supercomputing architectures change rapidly and larger amounts of data must be processed, it is difficult to create an efficient and versatile workflow for scientific simulations at scale. These large-scale scientific applications require computation, data analysis and visualization. Our approach is to explore building a programming language that can provide appropriate programming abstractions, a development toolchain and runtime layers that support existing scientific applications on emerging architectures without having to significantly rewrite or refactor their code.  
Towards this goal, we have developed Scout, a domain-specific language that provides conservative extensions to C/C++ via the LLVM/Clang compiler  
The poster will provide example Scout programs, a high-level system diagram, visualization support details and architecture support details. It will also contain a discussion of our experiences using LLVM/Clang, Scout design considerations and future goals.

<!-- *********************************************************************** -->

* * *
