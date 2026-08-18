---
layout: "default.html"
permalink: "devmtg/2018-04/talks.html"
---
# 2018 European LLVM Developers Meeting

<div style="float: left; width: 68%">

<div style="width: 100%">

*   [Conference main page](index.html)
*   **Conference Dates**: April 16-17, 2018
*   **Location**: [Bristol Marriott Hotel City Centre](http://www.marriott.com/hotels/travel/brsdt-bristol-marriott-hotel-city-centre/), Bristol UK

</div>

# About

The meeting serves as a forum for LLVM, Clang, LLDB and other LLVM project developers and users to get acquainted, learn how LLVM is used, and exchange ideas about LLVM and its (potential) applications.

The conference includes:

*   [Keynotes](#Keynotes)
*   [Tutorials](#Tutorials)
*   [Technical talks](#Talks)
*   [Lightning talks](#Lightning_Talks)
*   [BoFs](#BoFs)
*   [Poster session](#Posters)
*   hacker’s lab
*   and a reception.

# Keynotes

**The Cerberus Memory Object Semantics for ISO and De Facto C**  
*P. Sewell* The semantics of pointers and memory objects in C has been a vexed question for many years. C values cannot be treated as simple abstract or concrete entities: the language exposes their representations, but compiler optimisations rely on analyses that reason about provenance and initialisation status, not just runtime representations. The ISO standard leaves much of this unclear, and in some aspects differs with de facto standard usage - which itself is difficult to investigate. This talk will describe our candidate source-language semantics for memory objects and pointers in C, as it is used and implemented in practice. Focussing on provenance and uninitialised values, we propose a coherent set of choices for a host of design questions, based on discussion with the ISO WG14 C standards committee and previous surveys of C experts. This should also inform design of the LLVM internal language semantics, and it seems that our source-language proposal and the LLVM proposal by Lopes, Hur, et al. can be made compatible. Our semantics is integrated with the Cerberus semantics for much of the rest of C, with a clean translation of C into a Core intermediate language. Together, the two make C undefined behaviours explicit. Cerberus has a web-interface GUI in which one can explore all the allowed behaviours of small test programs, and which also identifies the clauses of the C standard relevant to typechecking and translating each test. Work-in-progress URL: [http://svr-pes20-cerberus.cl.cam.ac.uk/](http://svr-pes20-cerberus.cl.cam.ac.uk/) We also describe detailed proposals to WG14, showing how the semantics can be incorporated into the ISO standard.

* * *

**LLVM x Blockchains = A new Ecosystem of Decentralized Applications**  
*R. Zhong* Recently, blockchains are showing more and more power as application platforms besides transaction-trading platforms. Running applications on decentralized platforms totally differs from the way we did before. And we can foresee, developers will redefine existing centralized applications and create different decentralized applications. However, the foundations are not ready yet. Both academia and industry are exploring how to enpower the decentralized applications. We, Nebulas, call on the LLVM community to bring LLVM to the blockchain community. We propose several open problems needing to be addressed with the target of leveraging LLVM in blockchains. Besides, we also share our work on using LLVM to build a smart contract execution engine.

# Tutorials

**Pointers, Alias & ModRef Analyses**  
*A. Sbirlea, N. Lopes* Alias analysis is widely used in many LLVM transformations. In this tutorial, we will give an overview of pointers, Alias and ModRef analyses. We will first present the concepts around pointers and memory models, including the representation of the different types of pointers in LLVM IR, then discuss the semantics of ptrtoint, inttoptr and getelementptr and how they, along with pointer comparison, are used to determine memory overlaps. We will then show how to efficiently and correctly use LLVM’s alias analysis infrastructure, introduce the new API changes, as well as the highlight common pitfalls in the usage of these APIs.

* * *

**Scalar Evolution - Demystified**  
*J. Absar* This is a tutorial/technical-talk proposal for an illustrative and in-depth exposition of Scalar Evolution in LLVM. Scalar Evolution is an LLVM analysis that is used to analyse, categorize and simplify expressions in loops. Many optimizations such as - generalized loop-strength-reduction, parallelisation by induction variable (vectorization), and loop-invariant expression elimination - rely on SCEV analysis. However, SCEV is also a complex topic. This tutorial delves into how exactly LLVM performs the SCEV magic and how it can be used effectively to implement and analyse different optimisations. This tutorial will cover the following topics:

1.  What is SCEV? How does it help improve performance? SCEV in action (using simple clear examples).
2.  hain of Recurrences - which forms the mathematical basis of SCEV.
3.  Simplifying/rewriting rules in CR that SCEV uses to simplify expressions evolving out of induction variables. Terminology and SCEV Expression Types (e.g. AddRec) that is common currency that one should get familiar with when trying to understand and use SCEV in any context.
4.  LLVM SCEV implementation of CR - what's present and what's missing?
5.  How to use SCEV analysis to write your own optimisation pass? Usage of SCEV by LSR (Loop Strength Reduce) and others.
6.  How to generate analysis info out of SCEV and how to interpret them.

The last talk on SCEV was in LLVM-Dev 2009. This tutorial will be complementary to that and go further with examples, discussions and evolution of scalar-evolution in llvm since then. The author has previously given a talk on machine scheduler in llvm - [https://www.youtube.com/watch?v=brpomKUynEA&t=310s](https://www.youtube.com/watch?v=brpomKUynEA&t=310s)

# BoFs (Birds of a Feather)

\[[top](#top)\]

**Towards implementing #pragma STDC FENV\_ACCESS**  
*U. Weigand* When generating floating-point code, clang and LLVM will currently assume that the program always operates under default floating-point control modes, i.e. using the default rounding mode and with floating-point exceptions disabled, and never checks the floating-point status flags. This means that code that does attempt to make use of these IEEE features will not work reliably. The C standard defines a pragma FENV\_ACCESS that is intended to instruct the compiler to switch to a method of generating code that will allow these features to be used, but this pragma and the associated infrastructure is not yet implemented in clang and LLVM. The purpose of this BoF is to bring together all parties interested in this feature, whether as potential users, or as experts in any of the parts of the compiler that will need to be modified to implement it, from the clang front end, through the optimizers, to the various back ends that need to emit appropriate code for their platform. We will discuss the current status of the partial infrastructure that is already present, identify the pieces that are still missing, and hopefully agree on next steps to move towards a full implementation of pragma FENV\_ACCESS in clang and LLVM.

* * *

**Build system integration for interactive tools**  
*I. Biryukov, H. Wu, E. Liu, S. McCall* The current approach for integrating clang tools with build systems (CompilationDatabase, compile\_commands.json) was designed for running command line tools and it lacks some important features that would be nice to have for interactive tools like clangd, e.g. tracking updates to the compilation commands for existing files or propagating information like file renames back to the build system. The current approach also requires interference from the users of the tools to generate compile\_commands.json even for the build systems that support it. On the other hand, there are existing tools like CLion and Visual Studio that integrate seamlessly with their supported build systems and “just work” for the users without extra configuration. Arguably, this approach provides a better user experience. It would be interesting to explore existing build systems and approaches for integrating them with interactive clang-based tools and improving user experience in that area.

* * *

**Clang Static Analyzer BoF**  
*Devin Coughlin* BoF for the users and implementors of the Clang Static Analyzer. Suggested agenda: 1. Quick presentation of the ongoing development activities in the Static Analyzer community 2. Discussion of the main annoyances using the Static Analyzer (e.g. sources of false positives) 3. Discussion of the most wanted checks for the Static Analyzer 4. Discussion of missing capabilities of the Analyzer (statistical checks, pointer analysis, ...) 5. Discussion of the constraint solver limitations and proposed solutions 6. Discussion of future directions

* * *

**LLVM Foundation BoF**  
*LLVM Foundation Board of Directors*

# Technical Talks

\[[top](#top)\]

**A Parallel IR in Real Life: Optimizing OpenMP**  
*H. Finkel, J. Doerfert, X. Tian, G. Stelle* Exploiting parallelism is a key challenge in programming modern systems across a wide range of application domains and platforms. From the world's largest supercomputers, to embedded DSPs, OpenMP provides a programming model for parallel programming that a compiler can understand and optimize. While LLVM's optimizer has not traditionally been involved in OpenMP's implementation, with all of the outlining logic and translation into runtime-library calls residing in Clang, several groups have been experimenting with implementation techniques that push some of this translation process into LLVM itself. This allows the optimizer to simplify these parallel constructs before they're transformed into runtime calls and outlined functions. We've experimented with several techniques for implementing a parallel IR in LLVM, including adding intrinsics to represent OpenMP constructs (as proposed by Intel and others) and using Tapir (an experimental extension to LLVM originally developed at MIT), and have used these to lower both parallel loops and tasks. Nearly all parallel IR techniques allow for analysis information to flow into the parallel code from the surrounding serial code, thus enabling further optimization, and on top of that, we've implemented optimizations such as fusion of parallel regions and the removal of redundant barriers. In this talk, we'll report on these results and other aspects of our experiences working with parallel extensions to LLVM's IR.

* * *

**An Introduction to AMD Optimizing C/C++ Compiler**  
*A. Team* In this paper we introduce some of the optimizations that are a part of AMD C/C++ Optimizing Compiler 1.0 (AOCC 1.0) which was released in May 2017 and is based on LLVM Compiler release 4.0.0. AOCC is AMD’s CPU performance compiler which is aimed at optimizing the performance of programs running on AMD processors. In particular, AOCC 1.0 is tuned to deliver high performance on AMD’s EPYC(TM) server processors. The performance results for SPECrate®2017\_int\_base, SPECrate®2017\_int\_peak \[1\], SPECrate®2017\_fp\_base and SPECrate®2017\_fp\_peak \[2\] that we include in the paper show that AOCC delivers excellent performance thereby enhancing the power of the AMD EPYC(TM) processor. The optimizations fall into the categories of loop vectorization, SLP vectorization, data layout optimizations and loop optimizations. We shall introduce and provide some details of each optimization. \[1\] [https://www.spec.org/cpu2017/results/res2017q4/cpu2017-20171031-00334.html](https://www.spec.org/cpu2017/results/res2017q4/cpu2017-20171031-00334.html)  
\[2\] [https://www.spec.org/cpu2017/results/res2017q4/cpu2017-20171031-00366.html](https://www.spec.org/cpu2017/results/res2017q4/cpu2017-20171031-00366.html)

* * *

**Analysis of Executable Size Reduction by LLVM passes**  
*V. Sinha, P. Kumar, S. Jain, U. Bora, S. Purini, R. Upadrasta* Increase in the number of embedded devices and the demand to run resource intensive programs on these limited memory systems has necessitated the reduction of executable size of programs. LLVM offers an out-of-box -Oz optimization that is specifically targeted for the reduction of generated executable size. However, the formidable increase in the interest of making smaller and smarter devices has compelled programmers to develop more complicated programs for embedded systems. In this work, we aim to cater to the specific need of compiler driven reduction of executable size for such memory critical devices. We go beyond the traditional series of passes executed by -Oz; we try to break this series into logical groups and study their effect, as well as the effect of their combinations, on size of the executable. Our preliminary study over SPEC 2017 benchmarks gives an insight into the comparative effect of the groups of passes on executable size. Our work has potential to enable the developer to tailor a custom series of passes so as to obtain the desired executable size. To further aid such a customization, we create a prediction model (based on simple linear regression) that is correctly able to predict the executable size obtained by a combination of groups when given only the sizes obtained by the individual groups.

* * *

**Developing Kotlin/Native infrastructure with LLVM/Clang, travel notes.**  
*N. Igotti* In September of 2016 JetBrains started development of LLVM-based Kotlin compiler and runtime. Since then, we have reached version 0.5, which compiles to most LLVM targets (Linux, Windows and macOS as OS; x86, ARM and MIPS as CPU architectures, along with more exotic WebAssembly) and supports smooth interop with arbitrary C and Objective-C libraries. This talk will give some highlights on challenges we faced during development of this backend, with emphasis on LLVM-related topics.

* * *

**Extending LoopVectorize to Support Outer Loop Vectorization Using VPlan**  
*D. Caballero, S. Guggilla* The introduction of the VPlan model in Loop Vectorizer (LV) started as a refactoring effort to overcome LV’s existing limitations and extend its vectorization capabilities to outer loops. So far, progress has been made on the refactoring part by introducing the VPlan model to record the vectorization and unrolling decisions for candidate loops and generate code out of them. This talk focuses on the strategy to bring outer loop vectorization capabilities to Loop Vectorizer by introducing an alternative vectorization path in LV that builds VPlan upfront in the Loop Vectorizer pipeline. We discuss how this approach, in the short term, will add support for vectorizing a subset of simple outer loops annotated with vectorization directives (#pragma omp simd and #pragma clang loop vectorize). We also talk about the plan to extend the support towards generic outer and inner loop auto-vectorization through the convergence of both vectorization paths, the new alternative vectorization path and the existing inner loop vectorizer path, into a single one with advanced VPlan-based vectorization capabilities. We conclude the talk by describing potential opportunities for the LLVM community to collaborate in the development of this effort.

* * *

**Finding Iterator-related Errors with Clang Static Analyzer**  
*Á. Balogh* The Clang Static Analyzer is a sub-project of Clang that performs source code analysis on C, C++, and Objective-C programs. It is able to find deep bugs by symbolically executing the code. However, this far finding C++ iterator related bugs was a white spot in the analysis. In this work we present a set of checkers that detects three different bugs of this kind: out-of-range iterator dereference, mismatch between iterator and container or two iterators and access of invalidated iterators. Our combined checker solution is capable finding all these errors even in in less straightforward cases. It is generic so it do not only work on STL containers, but also on iterators of custom container types. During the development of the checker we also had to overcome some infrastructure limitations from which also other (existing and future) checkers can benefit. The checker is already deployed inside Ericsson and is under review by the community.

* * *

**Finding Missed Optimizations in LLVM (and other compilers)**  
*G. Barany* Randomized differential testing of compilers has had great success in finding compiler crashes and silent miscompilations. In this talk I explain how I used the same approach to find missed optimizations in LLVM and other open source compilers (GCC and CompCert). I compile C code generated by standard random program generators and use a custom binary analysis tool to compare the output programs. Depending on the optimization of interest, the tool can be configured to compare features such as the number of total instructions, multiply or divide instructions, function calls, stack accesses, and more. A standard test case reduction tool produces minimal examples once an interesting difference has been found. I have used these tools to compare the code generated by GCC, Clang, and CompCert. I found previously unreported missing arithmetic optimizations in all three compilers, as well as individual cases of unnecessary register spilling, missed opportunities for register coalescing, dead stores, redundant computations, and missing instruction selection patterns. In this talk I will show examples of optimizations missed by LLVM in particular, both target-independent mid-end issues and ones in the ARM back-end.

* * *

**Global code completion and architecture of clangd**  
*E. Liu, H. Wu, I. Biryukov, S. McCall* Clangd is an implementation of the Language Server Protocol (LSP) server based on clang’s frontend and developed as part of LLVM in the clang-tools-extra repository. LSP is the relatively new initiative to standardize the protocol for providing intelligent semantic code editing features independent of a particular text editor. Clangd aims to support very large codebases and provide intelligent IDE features like code completion on a project-wide scale. In this talk, we’ll cover the architecture of clangd and talk in-depth about the feature we’ve been working on in the last few months: the global code completion.

* * *

**Hardening the Standard Library**  
*M. Clow* Every C++ program depends on a standard library implementation. For LLVM users, this means that libc++ is at the bottom of their dependency graph. It is vital that this library be correct and performant. In this talk, I will discuss some of the principles and tools that we use to make libc++ as "solid" as possible. I'll talk about preconditions, postconditions, reading specifications, finding problems, ensuring that bugs stay fixed, as well as several tools that we use to achieve our goal of making libc++ as robust as possible. Some of the topics I'll discuss are:

*   Precondition checking - when practical.
*   Warning eradication
*   The importance of a comprehensive test suite for both correctness and ensuring that bugs don't reappear.
*   Static analysis
*   Dynamic analysis
*   Fuzzing

* * *

**Implementing an LLVM based Dynamic Binary Instrumentation framework**  
*C. Hubain, C. Tessier* This talk will go over our efforts to implement a new open-source DBI framework based on LLVM. We have been using DBI frameworks in our work for a few years now: to gather coverage information for fuzzing, to break whitebox cryptography implementations used in DRM or to simply assist reverse engineering. However we were dissatisfied with the state of existing DBI frameworks: they were either not supporting mobile architectures, too focused on a very specific use cases or very hard to use. This prompted the idea of developing QBDI ([https://qbdi.quarkslab.com](https://qbdi.quarkslab.com)), a new framework which has been in development for two years and a half. With QBDI we wanted to try a modern take on DBI framework design and build a tool crafted to support mobile architectures from the start, adopting a modular design enabling its integration with other tools and that was easy to use by abstracting all the low-level details from the users. During the talk, we will review the motivation behind the usage of a DBI. We will explain its core principle and the main implementation challenges we faced. We will share some lessons learned in the process and how it changed the way we think about dynamic instrumentation tools.

* * *

**LLVM Greedy Register Allocator – Improving Region Split Decisions**  
*M. Yatsina* LLVM Code Generation provides several alternative passes for performing register allocation. Most of the LLVM in-tree targets use the Greedy Register Allocator, which was introduced in 2011. An overview of this allocator was presented by Jakob Olesen at the LLVM Developers' Meeting of that year (\*). This allocator relies on splitting live ranges of variables in order to cope with excessive co-existing registers. In this technique a live range is split into two or more smaller subranges, where each subrange can be assigned a different register or be spilled. This talk revisits the Greedy Register Allocator available in current LLVM, focusing on its live range region splitting mechanism. We show how this mechanism chooses to split live ranges, examine a couple of cases exposing suboptimal split decisions, and present recent contributions along with their performance impact.

* * *

**MIR-Canon: Improving Code Diff Through Canonical Transformation.**  
*P. Lotfi* Comparing IR and assembly through diff-tools is common but can involve tediously reasoning through differences that are semantically equivalent. The development of GlobalISel presented problems of correctness verification between two programs compiled from identical IR using two different instruction selectors (SelectionDAG versus GlobalISel) where outcomes of each selector should ideally be reducible to identical programs. It is in this context that transforming the post-ISel Machine IR (MIR) to a more canonical form shows promise. To address said verification challenges we have developed a MIR Canonicalization pass in the LLVM open source tree to perform a host of transformations that help to reduce non-semantic differences in MIR. These techniques include canonical virtual register renaming (based on the order operands are walked in the def-use graph), canonical code motion of defs in relation to their uses, and hoisting of idempotent instructions. In this talk we will discuss these algorithms and demonstrate the benefits of using the tool to canonicalize code prior to diffing MIR. The tool is available for the whole LLVM community to try.

* * *

**New PM: taming a custom pipeline of Falcon JIT**  
*F. Sergeev* Over the few last months we at Azul were teaching Falcon, our LLVM based optimizing JIT compiler, to leverage the new pass manager framework. This talk will focus on our motivation as well as practical experience in getting an extensive custom LLVM pipeline to production under the new pass manager. I will cover the current state of LLVM pass manager as viewed from our "downstream" side, issues we met while converting, as well as our expectations and how well they were met at the end.

* * *

**Organising benchmarking LLVM-based compiler: Arm experience**  
*E. Astigeevich* The ARM Compiler 6 is a product based on Clang/LLVM projects. Basing your product on Clang/LLVM sources brings challenges in organizing the product development lifecycle. You need to decide how to synchronize downstream and upstream repositories. The decision impacts ways of testing and benchmarking. The Arm compiler team does development of the compiler on the upstream trunk keeping a downstream repository synchronized with the upstream trunk. Upstream public build bots guard us from commits which can break our builds. We also have infrastructure to do additional testing. There are a few public performance tracking bots which run the LLVM test-suite benchmarks. Although the LLVM test-suite covers many use cases, products often have to care about a wider variety of use cases. So you will have to track quality of code generation on other programs too. In this presentation we will explain how we protect the Arm compiler product from code generation quality issues that the public bots don’t catch. We will cover topics like continuous regression tracking, process of fixing regressions, a benchmarking infrastructure. We will show that the most important part of protecting the quality of a LLVM-based product is to be closely involved into development of the upstream LLVM which means detect issues in the upstream LLVM as early as possible and report them as soon as possible. We hope our experience will enable both better LLVM-derived products to be made and for product teams of other companies to contribute to LLVM itself more effectively.

* * *

**Performance Analysis of Clang on DOE Proxy Apps**  
*H. Finkel, B. Homerding* The US Department of Energy has released nearly 50 proxy applications ([http://proxyapps.exascaleproject.org/](http://proxyapps.exascaleproject.org/)). These are simplified applications that represent key characteristics of a wide class of scientific computing workloads. We've conducted in-depth performance analysis of Clang-generated code for these proxy applications, comparing to GCC-compiled code and, in some cases, code generated by vendor compilers, and have found some interesting places where Clang could do better. In this talk, we'll walk through several interesting examples and present some data on overall trends which, in some cases, are surprising.

* * *

**Point-Free Templates**  
*A. Gozillon, P. Keir* Template metaprogramming is similar to many functional languages; it's pure with immutable variables. This encourages a similar programming style; which begs the question: what functional features can be leveraged to make template metaprogramming more powerful? Currying is just such a technique, with increasing use cases. For example the ability to make concise point-free metafunctions using partially applied combinators and higher-order functions. Such point-free template metafunctions can be leveraged as a stand-in for the lack of type-level lambda abstractions in C++. Currently there exist tools for converting pointful functions to point-free functions in certain functional languages. These can be used for quickly creating point-free variations of a metafunction or finding reusable patterns. As part of our research we have made a point-free template conversion tool using Clang LibTooling that takes pointful metafunctions and converts them to point-free metafunctions that can be used in lieu of type-level lambdas.

* * *

**Protecting the code: Control Flow Enforcement Technology**  
*O. Simhon* Return-Oriented Programming (ROP), and similarly Call/Jump-Oriented Programming (COP/JOP), have been the prevalent attack methodology for stealth exploit writers targeting vulnerabilities in programs. Intel introduces Control-flow Enforcement Technology (CET) \[1\] which is a HW-based solution for protecting from gadget-based ROP/COP/JOP attacks. The new architecture deals with such attacks using Indirect Branch Tracking and Shadow Stack. The required support is implemented in LLVM and includes optimized lightweight instrumentation. This talk targets LLVM developers who are interested in new security architecture and methodology implemented in LLVM. Attendees will get familiar with basic control flow attacks, CET architecture and its LLVM compiler aspects.  
\[1\] [https://software.intel.com/sites/default/files/managed/4d/2a/control-flow-enforcement-technology-preview.pdf](https://software.intel.com/sites/default/files/managed/4d/2a/control-flow-enforcement-technology-preview.pdf)

# Lightning talks

\[[top](#top)\]

**C++ Parallel Standard Template LIbrary support in LLVM**  
*M. Dvorskiy, J. Cownie, A. Kukanov* The C++17 standard has introduced extensions to the Standard Template Library (STL) to allow the expression of parallelism through the Parallel STL. In this talk we describe the extensions, how to use them, and how we are intending to support them in Clang/LLVM.

* * *

**Can reviews become less of a bottleneck?**  
*K. Beyls* Many contributors to LLVM have experienced that sometimes the hardest part of making a contribution is to get reviews for changes you propose. To put it another way, one of the main limiting factors of the speed at which the LLVM project improves is review bandwidth. In an attempt to gain some insights on this and go beyond anecdotal evidence, I analysed the patterns of code review interactions over the past 3 years, as they happened on reviews.llvm.org. A few examples of statistics and insights I'll share are: - A small number of people do the bulk of the code reviews. The distribution of reviews done per reviewer seems to follow a power law. - On average, every patch for which you request review needs 2.5 review comments from someone outside your direct team before it can be committed. - One consequence of the above data is that for every review you request, you should aim to do at least 2.5 useful review comments for people outside your direct team, to pay your fair share in reviews. Many developers want to pay back their "review debt". However, with over 200 changes to open reviews every day, it is difficult and time consuming to find a review that you can help with. I will share a few ideas and experiments on how to make it easier to find the open reviews that you can help with. Overall, I hope this lightning talk can help towards making review slightly less of a bottleneck for the LLVM project.

* * *

**Clacc: OpenACC Support for Clang and LLVM**  
*J. Denny, S. Lee, J. Vetter* We are working on a new project, clacc, to contribute production-quality OpenACC compiler support to upstream clang and LLVM. A key feature of the clacc design is to translate OpenACC to OpenMP in order to build on clang’s existing OpenMP compiler and runtime support. The purpose of this talk is to describe the clacc goals, design decisions, and challenges that we have encountered so far in our prototyping efforts. We have begun preliminary design discussions on the clang developers mailing list and plan to continue these discussions throughout the development process to ensure the final clacc design is acceptable by the community.

* * *

**DragonFFI: Foreign Function Interface and JIT using Clang/LLVM**  
*A. Guinet* DragonFFI is a Clang/LLVM-based library that allows calling C functions and using C structures from any languages. It will show how Clang and LLVM are used to make this happen, and the pros/cons against similar libraries (like (c)ffi). In 2014, Jordan Rose and John McCall from Apple presented a talk about using Clang to call C functions from foreign languages. They showed issues they had doing it, especially about dealing with various ABI. DragonFFI provides a way to easily call C functions and manipulate C structures from any language. Its purpose is to parse C libraries headers without any modifications and transparently use them in a foreign language, like Python or Ruby. In order to deal with ABI issues previously demonstrated, it uses Clang to generate scalar-only wrappers of C functions. It also uses generated debug metadata to have introspection on structures. This talk will present the tool, how Clang and LLVM are used to provide these functionalities, and the pros and cons against what other similar libraries like (c)ffi \[0\] \[1\] are doing. It will show the actual limitations of Clang we had to circumvent, and the overall internal working of DragonFFI. In an effort to try and get help from the community, we will also present a list of tasks of various difficulties that can be done to participle in the project. This library is in active development and is still in an alpha/beta stage. Source code of the whole project is available here: [https://github.com/aguinet/dragonffi](https://github.com/aguinet/dragonffi). Python packages can be installed using pip under Linux 32/64 bits and OSX 32/64 bits (pip install pydffi).

* * *

**Easy::Jit: Compiler-assisted library to enable Just-In-Time compilation for C++ codes**  
*J. Fernandez, S. Guelton* Compiled languages like C++ generally don't have access to Just-in-Time facilities, which limits the range of possible optimizations. We introduce a framework to enable dynamic recompilation of some functions, using runtime information to improve the compiled code. This framework gives the user a clean abstraction and does not need to rely on specific compiler knowledge.

* * *

**Flang -- Project Update**  
*S. Scalpone* Lightning talk with current status of Flang, a Fortran front-end for LLVM. Cover current status of community, software, and short-term roadmap. **Look-Ahead SLP: Auto-vectorization in the Presence of Commutative Operations**  
*V. Porpodas, R. Rocha, L. Góes* Auto-vectorizing compilers automatically generate vector (SIMD) instructions out of scalar code. The state-of-the-art algorithm for straight-line code vectorization is Superword-Level Parallelism (SLP). In this work, we identify a major limitation at the core of the SLP algorithm, in the performance-critical step of collecting the vectorization candidate instructions that form the SLP-graph data structure. SLP lacks global knowledge when building its vectorization graph, which negatively affects its local decisions when it encounters commutative instructions. We propose LSLP, an improved algorithm that can plug-in to existing SLP implementations, and can effectively vectorize code with arbitrarily long chains of commutative operations. LSLP relies on short-depth look-ahead for better-informed local decisions. Our evaluation on a real machine shows that LSLP can significantly improve the performance of real-world code with little compilation-time overhead.

* * *

**Low Cost Commercial Deployment of LLVM**  
*J. Bennett* Deployment of a full new port of LLVM for general commercial use typically requires several engineer years of effort. With a large and diverse community of users, there are demanding requirements for features, reliability and performance if the compiler is to be successful. This cost is perfectly reasonable in supporting a major processor design, whose development will have been an order of magnitude more expensive. However there are many other processors which do not fall into this category, particularly custom DSPs and other specialist processors. Such devices are often only used by the company which designed them and are typically programmed in assembly language by an in-house team. Assembly programmers are rare and expensive to hire. Using assembly language is inherently less productive than high level coding. Being able to program in C would boost productivity and reduce costs, but with such a small user base, spending years on developing a full LLVM compiler tool chain cannot be justified. But a full C/C++ compiler tool chain is not needed. C is sufficient, and the well defined user base means only a limited feature set is required. In this talk I will describe the development of a LLVM tool chain for C for a 16-bit word-addressed Harvard architecture DSP. The work required 120 days of engineering effort in 2016/17, and also included the implementation of a CGEN-based assembler/disassembler, GDB and newlib C library. The LLVM work included adding support for 16-bit integers and the whole tool chain was regression tested using both the LLVM lit tests and GCC C regression test suite. The tool chain has been in production use for the past 12 months.

* * *

**Measuring the User Debugging Experience**  
*G. Bedwell* As compiler engineers, we (hopefully) think a lot about the the quality of the debug data that our compiler produces whether that be DWARF, Codeview or something else entirely. In general, we'd expect that producing more accurate debug data will lead to a better quality of debugging experience for the user, but how can we measure that quality of debugging experience beyond more general strategies such as dogfooding the tools ourselves? We'll present the Debugging Experience Tester tool (DExTer) and how we can use it in conjunction with various heuristics to assign a score to the overall quality of debugging. Using this, we can start answering some interesting questions. How does clang at -O0 -g compare to clang at -O2 -g? How does clang-cl compare against MSVC when debugging optimized code in Visual Studio? How has the clang debugging experience changed over the years? We'll suggest how can we use this information to improve the quality of the debugging experience we provide and how this could be used to inform the implementation of the long talked about -Og optimization level.

* * *

**Measuring x86 instruction latencies with LLVM**  
*G. Chatelet, C. Courbet, B. De Backer, O. Sykora* Instruction latencies are at the core of the instruction scheduling process of the LLVM backend. This information is usually provided by CPU vendors in the form of reference manuals or as direct contributions to the LLVM code base. Validating and correcting this information is hard. Dr. Agner Fog has been maintaining a database of latencies and decompositions for several years; his approach is to carefully craft pieces of assembly and use PMUs (Performance Monitoring Units). We present a tool based on LLVM and inspired by Fog that automates the process of measuring instruction latencies and infers the assignment of micro-operations to ports. Our goal is to feed this information back into LLVM configuration files.

* * *

**OpenMP Accelerator Offloading with OpenCL using SPIR-V**  
*D. Schürmann, J. Lucas, B. Juurlink* For many applications modern GPUs could potentially offer a high efficieny and performance. However, due to the requirement to use specialized languages like CUDA or OpenCL, it is complex and error- prone to convert existing applications to target GPUs. OpenMP is a well known API to ease parallel programming in C, C++ and Fortran, mainly by using compiler directives. In this work, we design and implement an extension for the Clang compiler and a runtime to offload OpenMP programs onto GPUs using a SPIR-V enabled OpenCL driver.

* * *

**Parallware, LLVM and supercomputing**  
*M. Arenaz* The HPC market is racing to build the next breakthrough exascale technologies by 2024. The high potential of HPC is being hindered by software issues, and porting software to new parallel hardware is one of the most significant costs in the adoption of breakthrough hardware technologies. Parallware technology innovation hinges on its different approach to dependence and data-flow analyses. LLVM uses the classical mathematical approach to dependence analysis, applying dependence tests and the polyhedral model mainly to vectorization of inner loops. In contrast Parallware uses a semantic analysis engine powered by a fast, extensible, hierarchical classification scheme to find parallel patterns in the LLVM-IR. The technical talk proposed for EuroLLVM will present the key challenges being addressed at Appentra: (1) Pros and cons of developing Parallware’s classification scheme on top of the LLVM-IR; (2) Parallware use of Clang and Flang to map the semantic information collected in the LLVM-IR back to the source code; (3) Parallware mechanisms to annotate and refactor the source code in order to produce OpenMP/OpenACC-enabled parallel code.

* * *

**Returning data-flow to asynchronous programming through static analysis**  
*M. Gilbert* Asynchronous event driven simulation is an efficient mechanism to model hardware devices. However, this programming style leads to a callback nightmare which impairs understanding of a program’s (hw model’s) data-flow. I will present a combination of runtime library and libtooling based static analysis tool which returns a data-flow view to a decoupled call graph. This significantly aids in program understanding and is a crucial tool for understanding behavior of a large, complicated system.

* * *

**RFC: A new divergence analysis for LLVM**  
*S. Moll, T. Klössner, S. Hack* This RFC is a joint effort by Intel and Saarland University to bring the divergence analysis of the Region Vectorizer (RV) to LLVM. This is part of the VPlan+RV proposal that we presented at the US LLVM Developers’ Meeting 2017. The divergence analysis is an essential building block in loop vectorization and the optimization of SPMD kernels. This effort is complementary to the VPlan proposal brought forward by Intel. The Region Vectorizer is an analysis and transformation framework for outer-loop and whole-function vectorization. RV vectorizes arbitrary reducible control flow including nested divergent loops. RV is being used by the Impala \[1\] and the PACXX \[6\] high performance programming frameworks.

* * *

**Static Performance Analysis with LLVM**  
*C. Courbet, O. Sykora, G. Chatelet, B. De Backer* Static performance analysis tools are instrumental in helping developers understand and tune the performance of their computation kernels. They are typically used in addition to benchmarking. This includes, for example, statically evaluating the throughput/latency of a basic block or identifying the critical path or limiting resources. These tools are typically provided by vendors in the form of closed-source, closed-data binaries (e.g. Intel® Architecture Code Analyzer \[1\]). Based on the data already present in LLVM for instruction scheduling (such as uops, execution ports/units, and latencies), we automatically generate subtarget performance simulators with a unified API. This allows building generic static performance analysis tools in an open and maintainable way. Beyond tools to analyze code, we’ll show applications to automatic performance tuning. \[1\] [https://software.intel.com/en-us/articles/intel-architecture-code-analyzer](https://software.intel.com/en-us/articles/intel-architecture-code-analyzer)

* * *

**Supporting the RISC-V Vector Extensions in LLVM**  
*R. Kruppe, J. Oppermann, A. Koch* RISC-V is an open and free instruction set architecture (ISA) used in numerous domains in industry and research. The (in-development) vector extensions supplement the basic ISA with support for data parallel computations. Software using them is vector length agnostic and therefore works with a variable vector length determined by the hardware as opposed to fixed-size SIMD registers, making software portable across a range of implementations. The vector length can also vary during execution depending on the requirements of the kernel being executed. The highly variable vector length raises unique challenges for supporting this instruction set in compilers. This talk gives an overview of the ongoing work to support it in LLVM, covering the overall implementation strategy, proposed extensions to LLVM IR, relation to the work for the similar Scalable Vector Extensions by Arm, and the current implementation status.

* * *

**Using Clang Static Analyzer to detect Critical Control Flow**  
*S. Cook* As part of the SECURE project ([http://gtr.rcuk.ac.uk/projects?ref=132799](http://gtr.rcuk.ac.uk/projects?ref=132799)), we are implementing transformations and analyses in open-source compilers which reduce programmer effort and error when implementing secure applications. This talk will discuss our work on extending the clang static analyzer to detect when "critical" variables are used to affect control flow. Critical variables are sensitive pieces of information that a programmer wishes to keep secret (such as cryptographic keys), and their use in the control flow graph can cause them to leak through side channel attacks. Our checker searches for branches that depend on critical variables and values derived from such critical variables and generates reports informing a user where the value became critical in their program. We discuss our experience in extending the checker to detect cases where it is the type itself that is of interest rather than a particular value, as we are interested in whether a variable is critical, irrespective of the value it holds at any given time.

# Posters

\[[top](#top)\]

**Automatic Profiling for Climate Modeling**  
*A. Gerbes, N. Jumah, J. Kunkel* Some applications are time consuming like climate modeling, which include lengthy simulations. Hence, the coding of such applications is sensitive in terms of performance. Most of the execution time of such applications is spent to execute specific parts of the code. Thus, giving more time to the optimization of those code parts can improve the application's performance. To identify the performance aspects of the code parts, profiling the application is a well-known technique. There are many tools and options for application developers to profile their applications. However, generally the profiling process provides performance information for an application or parts of it. To get such information for different parts of an application, some tools -e.g. LIKWID- allow the developer to tell the tool which parts are intended to be profiled. Developers mark the parts that they need performance information about. In this poster, we present an effort to profile climate modeling codes with two alternative methods. In the first method, we use the GGDML translation tool to mark the computational kernels of an application for profiling. In the second, we use Clang to mark some code parts. The same application code is written with the C language and the higher-level language extensions of GGDML. This source code is translated into a code that is ready for profiling in the first case. For the second method, the source code is translated into a C code without profiling markers. The resulting code is marked with a Clang instrumentation tool. Both of the code versions that are marked are then profiled. Both methods successfully generated the profiling markers. The GGDML translation tool was able to generate the profiling markers for the computational kernels according to the higher semantics of the language. The Clang-generated markers were driven by the Clang node types. The tested Clang annotations generated in the experiments give similar results for those generated by the GGDML translation tool.

* * *

**Cross Translation Unit Analysis in Clang Static Analyzer: Qualitative Evaluation on C/C++ projects**  
*G. Horvath, P. Szecsi, Z. Gera, D. Krupp* The Clang Static Analyzer cannot reason about errors that span across multiple translation units. We implemented Cross Translation Unit analysis and presented the performance properties of our implementation in the last year's EuroLLVM conference. In the CTU analysis mode we usually find 1.5-2 times more potential bugs. It is of paramount importance to study what are the quality (true/false positive rate, path length, ...) of these reports. This year we present a poster about the advancements since last year and a qualitative analysis of the reports on popular open source projects using CTU.

* * *

**Effortless Differential Analysis of Clang Static Analyzer Changes**  
*G. Horváth, R. Kovács, P. Szécsi* The proposition of a new patch to the Clang Static Analyzer engine includes information about the possible effects of the change. This normally consists of analysis results on a few software projects before and after applying the patch. This common practice has a few shortcomings. First, patch authors often have a bias towards a set of projects they are familiar with. Indeed, finding a set of test projects that truly show the effects of the patch can be a challenging task. Not to mention that a reviewer's request to extend the number of test projects might result in a significant amount of extra work for the patch author. Ideally, the reproduction and the extension of an analysis should be painless, and it should be possible to display results in an easily shareable format. We present a set of scripts for Clang-Tidy and the Clang Static Analyzer to address the above described issues in the hope that they will be beneficial not only to analyzer patch authors, but to a wide range of developers within the community.

* * *

**Offloading OpenMP Target Regions to FPGA Accelerators Using LLVM**  
*L. Sommer, J. Oppermann, J. Korinth, A. Koch* In recent versions, the OpenMP standard has been extended to support heterogeneous systems. Using the new OpenMP device constructs, regions of code can be offloaded to specialized accelerators. Besides GPUs, FPGAs have received increasing attention as dedicated accelerators in heterogeneous systems. The goal of this work is to develop a compile-flow to map OpenMP target regions to FPGA accelerators based on LLVM and the Clang frontend. We explain our custom Clang-based compilation-flow as well as our extensions to the LLVM OpenMP runtime implementation, responsible for data-transfer and device execution, and describe their integration into the existing LLVM offloading infrastructure.

* * *

**Using clang as a Frontend on a Formal Verification Tool**  
*M. Gadelha, J. Morse, L. Cordeiro, D. Nicole* We will introduce ESBMC's new clang-based frontend; ESBMC is an SMT-based context-bounded model checker that aims to provide bit-precise verification of both C and C++ programs. Using clang as a frontend not only eases the burden of supporting the ever evolving C/C++ standards (now being released every 3 years), but also brings a series of advantages, e.g., warning and compilation messages as expected from a compiler, expression simplifications, etc. The frontend was developed using libTooling and we will also present the challenges faced during development, including bugs found in clang (and patches submitted to fix them). Finally, we will present a short summary of ESBMC's features, and our future goal of fully supporting the C++ language, and the remaining work for attaining that goal.

# Student research competition

\[[top](#top)\]

**Compile-Time Function Call Interception to Mock Functions in C/C++**  
*G. Márton, Z. Porkoláb* In C/C++, test code is often interwoven with the production code we want to test. During the test development process we often have to modify the public interface of a class to replace existing dependencies; e.g. a supplementary setter or constructor function is added for dependency injection. In many cases, extra template parameters are used for the same purpose. These solutions may have serious detrimental effects on code structure and sometimes on run-time performance as well. We introduce a new technique that makes dependency replacement possible without the modification of the production code, thus it provides an alternative way to add unit tests. Our new compile-time instrumentation technique modifies LLVM IR, thus enables us to intercept function calls and replace them in runtime. Contrary to existing function call interception (FCI) methods, we instrument the call expression instead of the callee, thus we can avoid the modification and recompilation of the function in order to intercept the call. This has a clear advantage in case of system libraries and third party shared libraries, thus it provides an alternative way to automatize tests for legacy software. We created a prototype implementation based on the LLVM compiler infrastructure which is publicly available for testing.

* * *

\[[top](#top)\] **Improved Loop Execution Modeling in the Clang Static Analyzer**  
*P. Szécsi* The LLVM Clang Static Analyzer is a source code analysis tool which aims to find bugs in C, C++, and Objective-C programs using symbolic execution, i.e. it simulates the possible execution paths of the code. Currently, the simulation of the loops is somewhat naive (but efficient), unrolling the loops a predefined constant number of times. However, this approach can result in a loss of coverage in various cases. This study aims to introduce two alternative approaches which can extend the current method and can be applied simultaneously: (1) determining loops worth to fully unroll with applied heuristics, and (2) using a widening mechanism to simulate an arbitrary number of iteration steps. These methods were evaluated on numerous open source projects and proved to increase coverage in most of the cases. This work also laid the infrastructure for future loop modeling improvements.

* * *

**Using LLVM in a Model Checking Workflow**  
*G. Sallai* Formal verification can be used to show the presence or absence of specific type of errors in a computer program. Formal verification is usually done by transforming the already implemented source code into a formal model, then mathematically proving certain properties of that model (e.g. an erroneous state in the model cannot be reached). The theta verification framework provides a well-defined formal model suitable for checking imperative programs. In this talk, we present an LLVM IR frontend for theta, which bridges the gap between formal verification frameworks and the LLVM IR representation. Leveraging the LLVM IR as the frontend language of the verification workflow simplifies the transformation and allows us to easily add new supported languages. However, these transformations often yield impractically large models, which cannot be checked within a reasonable time. Therefore size reduction techniques need to be used on the program, which can be done by utilizing LLVM's optimization infrastructure (optimizing for size and simplicity rather than execution time) and extending it with other reduction algorithms (such as program slicing).

* * *

\[[top](#top)\] <!-- *********************************************************************** -->

<div style="float: left; width: 30%; padding-left: 20px">

## Diamond Sponsors:

[

# Apple

Apple](http://www.apple.com)  
[![](logos/quic-stack-version.jpg)  
QuIC](http://www.quicinc.com/)  

## Platinum Sponsors:

[![](logos/Google-logo_420_color_2x.png)  
Google](http://google.com)  
[![](logos/Mozilla.png)  
Mozilla](http://www.mozilla.org)  
[![](logos/psf_pos.jpg)  
Sony Interactive Entertainment](http://us.playstation.com/corporate/about/)

## Gold Sponsors:

[![](logos/Arm_logo_blue_150LG.png)  
Arm](http://www.arm.com/)  
[![](logos/Mentor-ASB-Logo-Black-Hires.png)  
Mentor](https://www.mentor.com)  
[![](logos/Intel-logo.png)  
Intel](http://intel.com)  
[![](logos/FB-fLogo-Blue-broadcast-2.png)  
Facebook](http://facebook.com/)  
[![](logos/HSAFoundation-FINAL.PNG)  
HSA Foundation](http://www.hsafoundation.com)  

*Thank you to our sponsors!*

</div>

<!-- *********************************************************************** -->

* * *

</div>
