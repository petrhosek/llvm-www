---
layout: "default.html"
permalink: "devmtg/2021-02-28/index.html"
---
<div style="float: left; width: 100%">

# Fifth LLVM Performance Workshop at CGO

The Fifth LLVM Performance Workshop will be held at CGO 2021. The workshop is co-located with CC, HPCA, and PPoPP. If you are interested in attending the workshop, please register at the [CGO website.](https://cgo-conference.github.io/cgo2021) The joint steering committee of CGO/PPoPP/HPCA/CC has decided to make the conference a virtual event this year. Note: The sessions will be delivered and recorded (via zoom) and shared on Youtube for public consumption.

<div style="width: 100%">

1.  [Preliminary Schedule](#schedule)
2.  [Registration](https://conf.researchr.org/attending/cgo-2021/registration)
3.  [Contact](#contact)
4.  [About](#about)

*   **Conference Dates**: Sunday February 28th, 2021 \[9am-1pm (slot1) and 1pm-5pm (slot2) Eastern Time\]
*   **Location**: Virtually

</div>

<!-- BEGIN SCHEDULE -->

# Preliminary Schedule

**Note to presenters: Please plan to leave some time (typically 5 minutes) for questions.** <!-- END SCHEDULE --> <!-- BEGIN ABSTRACT -->

# Abstracts

*   **Patrick Walton:** Rust+LLVM

    The Rust project keeps on top of new developments in LLVM. In this talk I'll go into our new code generation framework, as well as our use of new features like ThinLTO.

*   **Vinay Madhusudan, Ranjith Kumar and Prashantha Nr:** Moving LLVM’s code generator to MLIR framework

    hase ordering is a generic issue in compilation. Separation of concern has been achieved by delegating majority of target independent optimizations to Opt framework. Machine specific optimizations and final code generation is done at MIR level. There are instances of loss of optimization in Translation from LLVM IR to MIR. MLIR is emerging as a new higher level abstraction for LLVM infrastructure. Capability to represent higher language constructs like multi dimensional arrays has made optimizations more natural. Newer machine learning workloads are more suited to pass through MLIR. With an additional layer in compilation, there is more danger of losing optimizations in Translation. To reduce the same we intend to translate from MLIR to MIR using the existing MIR infrastructure to represent targets. On a longer timeframe LLVM IR should be subsumed by MLIR. In this work we have prototyped an MIR dialect in MLIR which can be used to represent the Target specific assembly. We have also ported the required GlobalIsel passes to MLIR through which we could generate X86 assembly from std dialect scalar operations via LLVM dialect. Our aim is to provide a different MLIR Dialect for each of the LLVM Targets and also to port the existing llvm/lib/CodeGen/\* and llvm/lib/Target/\* to MLIR based infrastructure.

*   **Ruijie Fang:** Improving Hot/Cold Splitting Optimization in LLVM

    The hot/cold splitting optimization pass in LLVM is a mid-end optimization pass that aims to improve instruction cache locality by splitting cold blocks into a separate function, using profile and static analysis information. Many incremental improvements have been made since its first inclusion in the LLVM mid-end. The objective of this talk is to summarize our progress on improving the outlining ability of the hot/cold splitting optimization pass in the LLVM compiler on two real-world workloads: qemu (both userspace and full-system emulation) and Firefox. Throughout this presentation, we will discuss several ideas to improve Hot/Cold Splitting on these real-world workloads including section splitting, longjmp outlining, and outlining exception handling blocks, and scheduling hot/cold splitting early in the optimization pipeline. Experimental data, as well as analysis, will be provided to show how these efforts perform on real-world workloads.

*   **Vishal Chebrolu:** Instrumentation to Prevent Programs Buffer-Overflow Attacks

    Memory corruption errors are a serious problem in languages like C and C++. Errors like out-of-bound access to the buffers when explored critically by attackers can lead to security vulnerabilities like buffer-overflow attacks. AddressSanitizer(ASAN) is a fast memory error detector which detects a number of memory bugs. We provide a mechanism for improvising the AddressSanitizer tool to prevent C/C++ programs from halting due to memory corruption errors like out-of-bound accesses to heap memory, use-after-free, invalid free, and double free. The changes are made in the instrumentation module to instrument recovery blocks instead of the error-reporting blocks for each type of accesses and also provide a method for dealing with pointer aliasing within functions. The instrumentation ensures the addressable memory is increased dynamically at runtime according to the execution of the program based on a scale of reallocation, which is used to decide whether to increase the addressable memory or not to consider the specific access. These changes can be employed in cases where system availability is of vital concern or when there is a need to reuse legacy code with increased memory demands, in which case the bounds are expanded safely during runtime.

*   **Arun Rangasamy:** Superblock Scheduler for Code-Size Sensitive Applications

    Load latency and taken branch penalty often limit performance in in-order CPUs. Code size is of paramount significance in many embedded applications. This talk is about an implementation of a super-block scheduler in LLVM, which addresses all three concerns.

*   **Vinay M, Ranjith Kumar H, Siddharth Tiwary and Prashantha Nr:** Classical Loop Nest Transformation Framework on MLIR

    MLIR is fast emerging as a high level program representation for aggressive program transformations. With representations for high level source constructs like multidimensional arrays, it is emerging as a preferred representation for machine learning compiler infrastructure like Tensorflow. In this work, we demonstrate support for classical loop transformation framework in MLIR. Associated analysis like alias analysis, mem2reg have also been supported. We show gain in at least one SPEC 2017 fortran benchmark.

*   **Prashantha Nr and Ranjith Kumar:** LTO and Data Layout Optimisations in MLIR

    Compilation is a process of gradual lowering of source code to target code. LLVM is a well established open source compiler with LLVM and MIR representations. For high level optiimzations, LLVM IR is not suitable. MLIR has been proposed as a higher level IR for high level optimisations. Link time optimisations are not yet proposed for MLIR. In this talk we would like to propose Link Time Optimisations(LTO) for MLIR. Also we would like to present two Data Layout Optimizations(DLO) which utilise the LTO framework. One of the SPEC 2017 benchmark gains ~35% using the proposed framework.

*   **Reshabh Sharma:** Finding the cracks between the analysis

    Compilers are complex. They use various analysis to drive different transformations to reliably generate optimized code. There has been a lot of work for ensuring the correctness of these analysis and transformation. We present an approach inspired from differential testing to find bugs or unexpected behaviors which are caused by the interaction of specific analysis. We focus on finding such behaviors inside LLVM, where the individual analysis seems to do correct at their end. We can classify analysis as fundamental and derived, derived analysis uses the results from fundamental analysis. Post dominator tree is a fundamental analysis while region tree detection analysis which uses post dominator tree will be a derived analysis. Any change made in the result of a fundamental analysis may or may not get reflected in the results of the derived analysis. Though, the result for any derived analysis should remain same if all the fundamental analysis it depends on does not change for a given mutation (given that the analysis itself is inert to that mutation). These unexpected changes are the behaviors we are trying to catch. We will use region tree generation analysis to demonstrate our technique. We will also show a test case where region tree generation analysis misses to detect a region for a mutation that ideally should have had no impact. At last, we will discuss how the region detection analysis is doing the right thing at its end and how its interaction with a fundamental analysis caused this bug.

*   **Gokcen Kestor:** COMET: Domain Specific Compilation for Heterogenous Targets

    The increasing complexity of heterogeneous systems has made it difficult for general-purpose compilers to automatically generate efficient code. Domain-specific languages (DSL) and compilers capture high- level semantic information to successfully generate efficient code for heterogenous targets. COMET introduces DSL and compiler infrastructure which leverages high-level domain-specific optimizations in multi-level Intermediate representations (IR) while progressively lowering of high-level representations to low-level IR to improve performance. Our compiler has been implemented on top of the MLIR framework and currently targeting computational chemistry and graph analytics domains.

*   **Stefanos Baziotis:** Latest Advancements in Automatic Vectorization Research

    In this talk, I want to connect developers the state-of-the-art in automatic vectorization and more specifically, in those advancements that I believe have a potential to be useful to LLVM. Three main topics will be presented: - Outer-Loop Vectorization - Recursive Tree Traversal Vectorization - Dynamic Vectorization My goal is neither just to provide a list of papers nor to present what has already presented in the papers. Rather, it is to provide an intuitive but accurate explanation and overview of the latest research.

*   **Alexis Engelke and Martin Schulz:** Instrew: Fast LLVM-based dynamic Binary Instrumentation and Translation

    Dynamic binary instrumentation and dynamic binary translation are two closely related techniques that can be used to analyze, modify and optimize existing binary code. Binary instrumentation is key to many debugging and performance analysis approaches, allowing for the transparent insertion of debugging or performance probes without requiring recompilation, while binary translation is essential to enable transparent porting of code to new architectures with new and/or modified instruction sets, and is also heavily used in computer architecture research. State-of-the-art tools, like Valgrind, DynamoRIO or PIN for binary instrumentation or QEMU for binary translation, however, typically either have a high performance overhead or allow only minor low-level modifications. To address these performance and functionality limitations, the latter --- QEMU --- has been extended to make use of the LLVM framework (HQEMU, DBILL) in order to take advantage of its optimization potential. However, this approach still uses the existing QEMU intermediate format in the translation process and hence inherits many of the imitations of QEMU. Additionally, it relies on a modified LLVM library, reducing portability and maintainability. In the Instrew project we, therefore, go a step further and solely rely on an unmodified LLVM for code instrumentation and translation, shortcutting the translation process, avoiding the limitations of an additional intermediate language with its own limitations (as in QEMU with its TCG representation) and taking full advantage of code generation features of LLVM. In this talk, we describe the general architecture of Instrew and show results comparing the performance to state-of-the-art tools. Additionally, we identify key problems of LLVM in the context of representing machine code in the high-level LLVM-IR.

*   **Denis Bakhvalov:** Performance Tuning: Future Compiler Improvements

    We live in an increasingly data-centric world, where we generate enormous amounts of data each day. Unfortunately, modern CPUs are not enjoying big improvements in single-core performance as they used to in the past decades. That's why performance tuning is becoming more important than it has been for the last 40 years. According to the popular paper "There’s plenty of room at the top" by Leiserson et al., SW tuning will be one of the key drivers for performance gains in the near future. Obviously, compilers play a big role here. This talk summarizes the key directions of how compilers can help performance tuning in the future.

*   **Aditya Kumar:** Performance improvement opportunities in the open source C++ standard libraries

    The C++ standard library (TC++SL) is a collection of classes and functions. These are written in C++ and are part of the C++ standard itself. All popular compiler toolchains come with a C++ standard library. The popular ones are libstdc++(GNU), libc++(LLVM) also popularly known as libcxx, msvc-stl. Needless to say, the standard library plays a very important role in the runtime performance of many systems. Over a period of time I have collected a list of performance opportunities in the standard C++ libraries. Some of them I found online from the mailing list and bugzilla. Others by reading source code, and previous experience with the performance analysis of libstdc++ and libc++. In this presentation I will share performance improvement opportunities in the open source C++ standard libraries.

<!-- END ABSTRACT -->

# Contact

In case of any queries please reach out to the workshop organizers: "Johannes Doerfert (jdoerfert at anl.gov)", "Sebastian Pop(spop at amazon.com)", "Aditya Kumar (aditya7 at fb.com)", and "Unnikrishnan C (unnikrishnan at iitpkd.ac.in)"

# About

#### Past Attendees

*   Active developers of projects in the LLVM Umbrella (LLVM core, Clang, LLDB, libc++, compiler\_rt, klee, lld, OpenMP, etc).
*   Anyone interested in using these as part of another project.
*   Students and Researchers.
*   Compiler, programming language, and runtime enthusiasts.
*   Those interested in using compiler and toolchain technology in novel and interesting ways.

#### Panels

Panel sessions are guided discussions about a specific topic. The panel consists of ~3 developers who discuss a topic through prepared questions from a moderator. The audience is also given the opportunity to ask questions of the panel.

#### Birds of a Feather (BoF)

A BoF session, an informal meeting at conferences, where the attendees group together based on a shared interest and carry out discussions without any pre-planned agenda.

#### Technical Talks

These 20-30 minute talks cover all topics from core infrastructure talks, to project's using LLVM's infrastructure. Attendees will take away technical information that could be pertinent to their project or general interest.

#### Tutorials

Tutorials are 50-60 minute sessions that dive down deep into a technical topic. Expect in depth examples and explanations. <!-- *********************************************************************** -->

* * *

<!--#include virtual="../../footer.incl" -->

| **Time** | **Speaker** | **Title** |   |   |
| --- | --- | --- | --- | --- |
| 9:00-9:30 | [Johannes Doerfert](https://www.linkedin.com/in/johannes-doerfert-3a0770a2/), [Unnikrishnan C](https://www.linkedin.com/in/unnikrishnan-cheramangalath-52282715/), [Aditya Kumar](https://hiraditya.github.io) | Welcome+Agenda |   |   |
| 9:30-10:00 | [Patrick Walton](https://www.linkedin.com/in/patrick-walton-30a10b16/) | Rust code generation framework. | [\[Abstract\]](#pw) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Patrick-rust-llvm.pdf) \] |
| 10:00-10:30 | [Vinay Madhusudan, Ranjith Kumar and Prashantha Nr (Compiler Tree Technologies Pvt Ltd)](http://www.compilertree.com) | Moving LLVM’s code generator to MLIR framework | [\[Abstract\]](#vm1) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Vinay-MLIR-codegen.pdf) \] |
| 10:30-10:45 | [Ruijie Fang](https://tr5.org/~ruijie/) | Improving Hot/Cold Splitting Optimization in LLVM | [\[Abstract\]](#rj) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Ruijie-hot-cold-split.pdf) \] |
| 10:45-11:00 | [Vishal Chebrolu (NIT Calicut)](https://www.linkedin.com/in/vishal-chebrolu-653816161/) | Instrumentation to Prevent Programs Buffer-Overflow Attacks | [\[Abstract\]](#vc) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Vishal-instrumentation.pdf) \] |
| 11:00-11:30 |   | Break |
| 11:30-12:00 | [Arun Rangasamy (Qualcomm)](https://www.linkedin.com/in/arun-rangasamy-b7b6944a/) | Superblock Scheduler for Code-Size Sensitive Applications | [\[Abstract\]](#ar) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Arun-Superblock-sched.pdf) \] |
| 12:00-12:30 | Vinay M, Ranjith Kumar H, Siddharth Tiwary and Prashantha Nr (Compiler Tree Technologies) | Classical Loop Nest Transformation Framework on MLIR | [\[Abstract\]](#vm2) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Vinay-MLIR-loopnest.pdf) \] |
| 12:30-1:00 | [Prashantha Nr and Ranjith Kumar (Compiler Tree Technologies)](http://www.compilertree.com) | LTO and Data Layout Optimisations in MLIR | [\[Abstract\]](#pn) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Prashantha-MLIR-LTO.pdf) \] |
| 1:00-2:00 |   | Break |
| 2:00-2:30 | [Reshabh Sharma (AMD)](http://linkedin.com/in/reshabh/) | Finding the cracks between the analysis | [\[Abstract\]](#rs) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Reshabh-analysis.pdf) \] |
| 2:30:3:00 | [Gokcen Kestor](https://www.linkedin.com/in/gokcen-kestor-9abb6914/) | COMET: Domain Specific Compilation for Heterogenous Targets | [\[Abstract\]](#gk) |   |
| 3.00-3:45 | [Stefanos Baziotis (NEC Deutschland GmbH)](http://users.uoa.gr/~sdi1600105/) | Latest Advancements in Automatic Vectorization Research | [\[Abstract\]](#sb) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Stefanos-vectorizer.pdf) \] |
| 3:45-4:15 | Alexis Engelke and Martin Schulz (Technical University of Munich) | Instrew: Fast LLVM-based dynamic Binary Instrumentation and Translation | [\[Abstract\]](#ae) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Alexis-instrew.pdf) \] |
| 4:15-4:30 |   | Break |
| 4:30-4:45 | [Denis Bakhvalov (Intel)](http://easyperf.net) | Performance Tuning: Future Compiler Improvements | [\[Abstract\]](#db) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Denis-perf.pdf) \] |
| 4:45-5:20 | [Aditya Kumar (Facebook)](https://hiraditya.github.io/) | Performance improvement opportunities in the open source C++ standard libraries | [\[Abstract\]](#ak) | \[ [Slides](https://llvm.org/devmtg/2021-02-28/slides/Aditya-c++-libraries.pdf) \] |

</div>
