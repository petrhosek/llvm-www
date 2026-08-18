---
layout: "default.html"
permalink: "devmtg/2025-10/index.html"
---
# 2025 US LLVM Developers' Meeting

<div style="float: left; width: 68%">

<div style="width: 100%">

1.  [About](#about)
2.  [Program](#program)
3.  [Code of Conduct](#coc)
4.  [Contact](#contact)

*   **Conference Date**: October 28-29, 2025
*   **Location**: [Santa Clara Marriott](https://www.marriott.com/en-us/hotels/sjcga-santa-clara-marriott/overview/), Santa Clara, California

</div>

# About

The US LLVM Developers' Meeting is a tri-annual gathering of the entire LLVM Project community. The conference is organized by the LLVM Foundation and many volunteers within the LLVM community. Developers and users of LLVM, Clang, and related subprojects will enjoy attending interesting talks, impromptu discussions, and networking with the many members of our community. Whether you are a new to the LLVM project or a long time member, there is something for each attendee.

### What can you can expect at an LLVM Developers' Meeting?

**Keynotes**

Keynotes are 40-45 minute talks that provide an overview of a topic or project and often capture the history and impact of choices made and what that means for current and future development.

**Technical Talks**

These 20-30 minute talks cover all topics from core infrastructure talks, to project's using LLVM's infrastructure. Attendees will take away technical information that could be pertinent to their project or general interest.

**Tutorials**

Tutorials are 50-60 minute sessions that dive down deep into a technical topic. Expect in depth examples and explanations.

**Lightning Talks**

These are fast 5 minute talks that give you a taste of a project or topic. Attendees will hear a wide range of topics and probably leave wanting to learn more.

**Quick Talks**

Quick 10 minute talks that dive a bit deeper into a topic, but not as deep as a Technical Talk.

**Student Technical Talks**

Graduate or Undergraduate students present their work using LLVM.

**Panels**

Panel sessions are guided discussions about a specific topic. The panel consists of ~3 developers who discuss a topic through prepared questions from a moderator. The audience is also given the opportunity to ask questions of the panel.

### Who attends?

*   Active developers of projects in the LLVM Umbrella (LLVM core, Clang, LLDB, libc++, compiler\_rt, flang, lld, MLIR, etc).
*   Anyone interested in using these as part of another project.
*   Students and Researchers
*   Compiler, programming language, and runtime enthusiasts.
*   Those interested in using compiler and toolchain technology in novel and interesting ways.
*   Sponsors and partners utilizing LLVM technology in their products.

The LLVM Developers' Meeting strives to be the *best conference* to meet other LLVM developers and users.

For future announcements or questions: Please visit the [LLVM Discourse forums](https://discourse.llvm.org). Most posts are in the Announcements or Community categories and tagged with [usdevmtg](https://discourse.llvm.org/tag/usdevmtg)

# Program

**Keynotes**

*ClangIR: Upstreaming an Incubator Project* \[ [Video](https://youtu.be/mQXE_y1T6H0) \] \[ [Slides](slides/keynotes/kaylor_lopes.pdf) \]  
Speakers: Andy Kaylor, Bruno Cardoso Lopes  

The presenters will share their experience transitioning ClangIR from an incubator project to an upstream feature within the LLVM community. The talk will focus on the development process, the technical challenges encountered, and the lessons learned while integrating a new high-level IR into Clang. This provides a case study on managing significant changes and community collaboration in a large-scale open-source project like LLVM.

*From proprietary to fully open-source: Arm Toolchain's adoption of LLVM technology* \[ [Video](https://youtu.be/I7S_Vsnkecg) \] \[ [Slides](slides/keynotes/smith.pdf) \]  
Speaker: Peter Smith  

Arm's embedded toolchain has existed since the establishment of the company 35 years ago. For the first 20 years, the toolchain was entirely proprietary. Over the last 15 years, Arm has incrementally replaced the proprietary parts of the toolchain with LLVM technology, with the latest incarnation providing an option for a fully open-source LLVM-based toolchain using LLVM libc. Throughout the process, we have kept our toolchain in sync with the LLVM main branch. This presentation covers the toolchain's adoption of LLVM technology, including: \* Early experiments to bridge the EDG front-end used by the proprietary compiler with an LLVM backend. \* Replacement of the compiler with a derivative of clang. \* Testing the correctness of the combined toolchain. \* Adoption of libc++ as the C++ library. \* How our strategy of managing downstream changes evolved. \* Replacement of all remaining proprietary tools with LLVM equivalents and removal of downstream patches. \* Our plans for integrating LLVM libc. The intended audience includes those interested in: \* Assembling a toolchain using a mixture of LLVM and proprietary technology. \* Managing downstream changes across a full toolchain, including merging and testing. \* Migrating customers through technology changes.

**Technical Talks**

*Building Modern Language Frontends with MLIR: Lessons from Mojo's Compile-Time Meta-Programming* \[ [Video](https://youtu.be/5RpOF-F0Gps) \] \[ [Slides](slides/technical_talks/lattner_zhu.pdf) \]  
Speakers: Chris Lattner, Billy Zhu  

This talk explains how Mojo, a new programming language, leverages MLIR to create a powerful compile-time metaprogramming system designed for heterogeneous computing. The language uses high-level features like traits and dependent types to build robust, type-safe abstractions that can target diverse hardware from a single programming model. The core of the implementation involves a parametric IR built on MLIR, where MLIR's attribute system is used to represent the parameters in Mojo's polymorphic system. This design, which makes both operations and types parameterizable, allows for the efficient specialization of generic code while ensuring type safety throughout the compilation process. The presentation will share practical insights and patterns learned during development to help other language implementers working with MLIR.

*Magellan: Autonomous Discovery of Novel Compiler Optimization Heuristics with AlphaEvolve* \[ [Video](https://youtu.be/D8lcsfOjEOs) \] \[ [Slides](slides/technical_talks/chen.pdf) \]  
Speaker: Hongzheng Chen  

This talk proposes a shift toward 'evolvable compilers' by using AlphaEvolve, a Gemini-powered agent, to automatically generate and refine compiler optimization heuristics for LLVM and XLA. By applying this method to challenges like function inlining and register allocation in LLVM, the project aims to reduce manual tuning efforts and create more performant, concise optimization policies. The results demonstrate that these automatically generated heuristics can outperform human-designed ones, with plans to upstream the solutions to the LLVM and XLA communities.

*Mind the Gap: Key Missing Features in the LLVM Toolchain for Windows on Arm* \[ [Video](https://youtu.be/7ISlHzJs2ks) \] \[ [Slides](slides/technical_talks/javaid.pdf) \]  
Speaker: Muhammad Omair Javaid  

This talk discusses the current state of LLVM-based toolchains for Windows on Arm, highlighting key missing features compared to other platforms. While Clang has made significant progress in supporting this target, several gaps remain that impact both user experience and performance. These include incomplete support for Structured Exception Handling (SEH) which is critical for robust error handling, lack of a native linker (ldd), and missing features in LLDB for debugging. The talk will provide an overview of these issues, their implications for developers, and the ongoing work to address them. By the end of this talk, the audience will have a better understanding of the challenges and opportunities for improving the LLVM toolchain on Windows on Arm.

*Climbing the ladder of complete: LLVM-libc past and future* \[ [Video](https://youtu.be/HtCMCL13Grg) \] \[ [Slides](slides/technical_talks/jones.pdf) \]  
Speaker: Michael Jones  

LLVM-libc has been in progress for almost 6 years. One of the questions I get fairly frequently is when it will be complete. The answer is that it depends on how you define "complete", but generally people mean "when can I build X piece of software with LLVM-libc?" In this talk I'll take you through what you can build with LLVM-libc now, what still needs to be finished to build the things you care about, and how you can help. This talk is suitable for anyone interested in LLVM-libc, either as a developer or a user. There will be some technical discussion, but it's mostly focused on the higher level status. Ideally this talk will provide the strategy for LLVM-libc for the next year.

*State of Clang 2025* \[ [Video](https://youtu.be/dROeqPmgZJg) \] \[ [Slides](slides/technical_talks/ballman.pdf) \]  
Speaker: Aaron Ballman  

As a follow-up to last year's State of Clang report, come along with Clang's lead maintainer to hear about what the Clang community has been up to. The talk will cover what new features have been added to Clang 21 and beyond, as well as data about the Clang community and how it compares to the overall LLVM project.

*Through the Compiler's Keyhole: Migrating to Clang Without Seeing the Source* \[ [Video](https://youtu.be/CHbyo0Ux60o) \] \[ [Slides](slides/technical_talks/hosek.pdf) \]  
Speaker: Petr Hosek  

This talk recounts the experience of migrating a proprietary, closed-source vendor codebase to the standard Clang toolchain, a significant departure from previous projects where full source code was available. The lack of source access necessitated a heavy reliance on automated solutions and the development of new features within the LLVM ecosystem. Key strategies included building minimal baremetal ports of the \*\*UBSan\*\* and \*\*PGO\*\* runtimes to detect undefined behavior and guide performance optimizations, respectively. The team also utilized \*\*FatLTO\*\* for aggressive optimizations under tight resource constraints, implemented the \`-fseparate-named-section\` option to manage memory layout, and proposed a \*\*DWARF CFI validation\*\* feature to aid in debugging hand-written assembly. The presentation will cover the lessons learned, the new features developed during this process, and ideas to simplify similar migrations in the future.

*Automating the search aspects of compiler engineering: IR for auto-tuning & beyond* \[ [Video](https://youtu.be/UgKvsIz0Jhs) \] \[ [Slides](slides/technical_talks/morel.pdf) \]  
Speaker: Rolf Morel  

This talk is about automating the mechanical bits of your job. The main ingredients:

1.  Encoding plans for pipeline/schedule-manipulations into an IR for pipelines/schedules, and
2.  Having tools automatically perform the optimization-through-considering-alternatives loop.

Consider an average compiler engineer's plan for an average day:

*   Out of all possible optimizations, first try optimization F. Evaluate. If perf isn't there...
*   Then tweak F's knobs. Evaluating each time.
*   Try optimization G next. Evaluate.
*   Then tweak G's knobs. Evaluate.
*   Now try F;G. Tweak knobs. Evaluate.
*   Then G;F. Tweak knobs. Evaluate.

Most of this is pretty repetitive and hence mechanizable. Except for formulating the plan—this is where you as an engineer are essential.

We build on MLIR's Transform-dialect \[0\], which exposes fine-grained transformations as operations which compose into schedules. (SSA-values fed into and produced by ops control transform ordering; parameters, i.e. attributes, are tweakable knobs.) We introduce transform ops with non-deterministic choice semantics. For example, an op's parameter can be the result of our new op which represents non-det selection among valid options. We go further: an op which chooses among regions to represent a choice between alternative sub-schedules. Further still: we employ SSA to encode that choices are tied together. E.g., we can encode that a sub-schedule later on should only be selected if a particular sub-schedule was chosen early on.

We demonstrate one approach to dealing with the non-determinism: a driver that obtains all choices—and their dependencies and constraints—and throws them to a solver. The solver selects a viable overall configuration which we use to rewrite the schedule so it no longer has non-determinism (to our knowledge, the first instance of a useful schedule IR rewrite). Thus obtained deterministic schedules are then automatically applied to payloads to obtain perf numbers, which we feed back into the solver for it to learn about the parameter space. The driver runs in a loop until a stopping criteria has been reached (e.g. until you come back into work in the morning).

Finally, we emphasize we go beyond:

*   **Auto-tuning**, as we "reify" choices into (transform) IR and tune more than just parameters,
*   **Auto-scheduling** (systems which automatically compose transforms), as we allow the engineer to effectively specify templates with composition choices at just the places they would have considered in the course of the day.

In short, our approach enables both expressiveness and controllable tractability.

*Enhancing MLGO Inlining with IR2Vec Embeddings* \[ [Video](https://youtu.be/ywe1-lI9H4k) \] \[ [Slides](slides/technical_talks/venkatakeerthy.pdf) \]  
Speaker: S. VenkataKeerthy  

Our initial experiments on internal binaries demonstrate that combining existing MLGO features with IR2Vec embeddings yields additional code size reductions of up to 5% in comparison to \`-Os\` and 4% in comparison to \`-Os\` with MLGO Inliner. This talk will outline the design of IR2Vec, the plan for upstreaming its support into LLVM, and discuss experimental results validating its effectiveness and scalability on real-world datacenter binaries. Specifically, we will describe how IR2Vec embeddings are used for driving ML-Guided Compiler Optimizations, focusing on our efforts to enhance current MLGO infrastructure and its possible extensions.

*A Faster and Simpler Dialect Conversion Driver without Pattern Rollback* \[ [Video](https://youtu.be/m-wAe80rMPs) \] \[ [Slides](slides/technical_talks/boeck_springer.pdf) \]  
Speakers: Markus Böck, Matthias Springer  

This talk presents a new "One-Shot Dialect Conversion" driver for MLIR, designed to address long-standing performance, usability, and maintenance issues with the existing dialect conversion infrastructure. The talk will give an overview of the design of the new driver, describe how to migrate existing passes/patterns to the new infrastructure, and report some first performance numbers.

*Specializing MLIR Data Structures: an Experiment* \[ [Video](https://youtu.be/EHq4iT-3htw) \] \[ [Slides](slides/technical_talks/fehr_stefanesco.pdf) \]  
Speakers: Mathieu Fehr, Leo Stefanesco  

MLIR's extensible type system is a powerful tool for building custom dialects. However, it can be challenging to specialize data structures for a given dialect without modifying the core MLIR infrastructure. In this talk, we will present an experiment in which we specialized MLIR data structures for a custom dialect. We will discuss the challenges we faced, the solutions we came up with, and the lessons we learned. We will also discuss how this work could be generalized to other dialects, and how it could be used to improve the performance of MLIR-based compilers.

*Normal forms for MLIR* \[ [Video](https://youtu.be/Esw84hH1Ed0) \] \[ Slides \]  
Speaker: Alex Zinenko  

MLIR's powerful rewrite system is a key component of its success. However, the lack of a canonical representation for MLIR operations can make it difficult to write robust and efficient rewrite patterns. In this talk, we will discuss the concept of normal forms for MLIR operations, and how they can be used to simplify the process of writing rewrite patterns. We will present a new framework for defining and working with normal forms in MLIR, and we will show how it can be used to improve the quality of MLIR-based compilers.

*Automatically generating pattern rewrites in MLIR* \[ [Video](https://youtu.be/MkYgNpWlvD8) \] \[ [Slides](slides/technical_talks/fehr.pdf) \]  
Speaker: Mathieu Fehr  

MLIR's declarative rewrite rule system is a powerful tool for writing compiler optimizations. However, it can be tedious and error-prone to write these rules by hand. In this talk, we will present a new system for automatically generating pattern rewrites in MLIR. We will discuss how this system can be used to automatically generate rewrite rules from a high-level specification, and we will show how it can be used to improve the quality of MLIR-based compilers.

*Lightweight Fault Isolation: LLVM Support for Efficient Native Code Sandboxing* \[ [Video](https://youtu.be/S0apBhyZklg) \] \[ [Slides](slides/technical_talks/garkinfel_yedidia.pdf) \]  
Speakers: Tal Garfinkel, Zachary Yedidia  

This talk presents a new approach to lightweight fault isolation in LLVM. We will discuss how we can use LLVM's existing infrastructure to build a system that can efficiently sandbox native code. We will also discuss the challenges we faced, the solutions we came up with, and the lessons we learned. We will show how this work can be used to improve the security of a wide range of applications, from web browsers to operating systems.

*Hardening the Core: Challenges in Mitigating Hardware Vulnerabilities with LLVM* \[ [Video](https://youtu.be/rOH9rCAaJJA) \] \[ [Slides](slides/technical_talks/sharma.pdf) \]  
Speaker: Reshabh K Sharma  

In this talk, we will explore the challenges faced by compiler developers using LLVM to mitigate hardware vulnerabilities and the potential need to evolve the LLVM compiler to effectively integrate security-focused transformations alongside its powerful optimization capabilities. As microarchitectural side-channel attacks like Spectre continue to evolve, it is crucial to address the challenges faced by mitigation developers at various levels of LLVM. These compiler-based defenses provide a flexible and timely response to emerging threats. They also enhance the overall security posture by layering defenses, protecting systems even when hardware-based solutions fall short or are not feasible. We will examine common defense patterns, the complexities of implementing mitigations, and the critical differences between these and traditional compiler transformations. Furthermore, we will discuss potential enhancements to LLVM that could increase the reliability of security measures and argue why compilers are the optimal platform for these defenses. We aim to underscore the necessity of a two-step mitigation infrastructure and highlight how tools like Bolt could help in addressing current limitations, paving the way for a more secure code transformation landscape.

*Using and Improving Optimization Remarks* \[ [Video](https://youtu.be/i7O62-2qxpU) \] \[ [Slides](slides/technical_talks/stadler.pdf) \]  
Speaker: Tobias Stadler  

Optimization remarks are a powerful yet underutilized tool for gaining insight into compiler heuristics and transformations. Remarks can inform the user on which optimizations applied successfully, which failed to apply, and which heuristics led to those decisions. We want to provide users with actionable, low-noise remarks about possible performance oversights in their code, and compiler developers with fine-grained per-function telemetry to qualify optimizer changes on large codebases and track down regressions. Our goal is to provide a unified remarks framework to cover both use-cases. In this talk, we will provide an overview of the state of optimization remarks, how to use them, and how to further extend them. We will show examples for applying remarks to different use-cases (e.g. improved vectorization failure hints, inlining summaries, regression analysis).

*Byte Type: Supporting Raw Data Copies in the LLVM IR* \[ [Video](https://youtu.be/eQF-hDmlLog) \] \[ [Slides](slides/technical_talks/lobo.pdf) \]  
Speaker: Pedro Lobo  

In this talk, we will discuss the challenges of supporting raw data copies in the LLVM IR. We will present a new \`byte\` type for the LLVM IR, and we will show how it can be used to represent raw data copies in a way that is both efficient and easy to work with. We will also discuss how this new type can be used to improve the performance of a wide range of applications, from image processing to scientific computing.

*Optimizing Flang's optimizer* \[ [Video](https://youtu.be/H4Desa4PG3s) \] \[ [Slides](slides/technical_talks/lupori.pdf) \]  
Speaker: Leandro Lupori  

Flang is a new Fortran front-end for LLVM. In this talk, we will discuss the challenges of optimizing Flang's optimizer. We will present a new approach to optimizing Flang's optimizer, and we will show how it can be used to improve the performance of Flang-compiled code. We will also discuss how this work can be generalized to other front-ends, and how it can be used to improve the performance of LLVM-based compilers.

*LT-Uh-Oh: Adventures using LTO with libc* \[ [Video](https://youtu.be/cG278WjmIFs) \] \[ [Slides](slides/technical_talks/kirth_thornburgh.pdf) \]  
Speakers: Paul Kirth, Daniel Thornburgh  

Link-Time Optimization (LTO) can be a powerful tool for improving the performance of C and C++ code. However, it can also be a source of subtle and hard-to-debug bugs. In this talk, we will discuss our adventures using LTO with libc. We will discuss the challenges we faced, the solutions we came up with, and the lessons we learned. We will also discuss how this work can be used to improve the quality of LTO in LLVM.

*An Undefined Behavior Annex for C++* \[ [Video](https://youtu.be/aTKv5xVg2Kw) \] \[ [Slides](slides/technical_talks/yaghmour.pdf) \]  
Speaker: Shafik Yaghmour  

Undefined behavior is a major source of bugs in C and C++ programs. In this talk, we will present a new Undefined Behavior Annex for C++. We will discuss how this annex can be used to detect and diagnose undefined behavior in C and C++ programs. We will also discuss how this work can be used to improve the quality of C and C++ compilers.

*LLVM Foundation Updates* \[ [Video](https://youtu.be/UVF2EhGS2pY) \] \[ Slides \]  
Speakers: LLVM Foundation Board of Directors  

This talk will provide an update on the latest activities of the LLVM Foundation. We will discuss the foundation's recent work, and we will provide a look at what's in store for the future. We will also discuss how you can get involved with the LLVM Foundation, and how you can help support the LLVM project.

*JIT-loading Arbitrary Programs - Powering Xcode Previews with LLVM's JIT* \[ [Video](https://youtu.be/AKfwEZVm2PE) \] \[ [Slides](slides/technical_talks/hames.pdf) \]  
Speaker: Lang Hames  

Xcode Previews is a new feature in Xcode that allows developers to see the results of their code changes in real time. In this talk, we will discuss how we use LLVM's JIT to power Xcode Previews. We will discuss the challenges we faced, the solutions we came up with, and the lessons we learned. We will also discuss how this work can be used to improve the quality of JIT compilers in LLVM.

*Iago: AI Driven Superoptimization for LLVM* \[ [Video](https://youtu.be/x4TFaweVJQ4) \] \[ [Slides](slides/technical_talks/mukherjee.pdf) \]  
Speaker: Manasij Mukherjee  

We designed Iago to be a drop-in replacement for Souper—a state-of-the-art superoptimizer for LLVM IR—we can perform a direct comparison between Iago's synthesis by LLM and Souper's synthesis by enumeration. We evaluated both Iago and Souper on a random sample of the synthesis problems encountered when optimizing the SPEC CPU 2017 benchmark suite. We found that while Iago finds 7.4% fewer optimizations than Souper does, 35.7% of the optimizations found by Iago were not found by Souper: most of these required synthesizing two or more new instructions and multiple fresh constants.

*CUTLASS Python DSL Infrastructure* \[ [Video](https://youtu.be/5NXd6MbKYNQ) \] \[ [Slides](slides/technical_talks/ozen.pdf) \]  
Speaker: Guray Ozen  

CUTLASS is a new Python DSL for writing high-performance GPU kernels. In this talk, we will discuss the CUTLASS Python DSL infrastructure. We will discuss the challenges we faced, the solutions we came up with, and the lessons we learned. We will also discuss how this work can be used to improve the quality of GPU support in LLVM.

*Synthesizing Practical Transfer Functions in Data-flow Analysis* \[ [Video](https://youtu.be/jv4Oob2vpeA) \] \[ [Slides](slides/technical_talks/fan.pdf) \]  
Speakers: Yuyou Fan  

Data-flow analysis is a key component of many compiler optimizations. In this talk, we will discuss the challenges of synthesizing practical transfer functions in data-flow analysis. We will present a new approach to synthesizing transfer functions, and we will show how it can be used to improve the quality of data-flow analysis in LLVM. We will also discuss how this work can be generalized to other compilers, and how it can be used to improve the quality of compiler optimizations.

*Instruction Cost-Modelling: Can We Do Better?* \[ [Video](https://youtu.be/uvOiF0RtaGs) \] \[ [Slides](slides/technical_talks/hickey.pdf) \]  
Speaker: Neil Hickey  

Instruction cost-modelling is a key component of many compiler optimizations. In this talk, we will discuss the challenges of instruction cost-modelling. We will present a new approach to instruction cost-modelling, and we will show how it can be used to improve the quality of compiler optimizations in LLVM. We will also discuss how this work can be generalized to other compilers, and how it can be used to improve the quality of compiler optimizations.

*The LLVM Offloading Infrastructure* \[ [Video](https://youtu.be/pndPwVMouPg) \] \[ [Slides](slides/technical_talks/huber.pdf) \]  
Speaker: Joseph Huber  

The LLVM offloading infrastructure is a new feature in LLVM that allows developers to offload computations to a remote device. In this talk, we will discuss the LLVM offloading infrastructure. We will discuss the challenges we faced, the solutions we came up with, and the lessons we learned. We will also discuss how this work can be used to improve the quality of offloading support in LLVM.

*Clang-Doc: Where We've Been and Where We're Going* \[ [Video](https://youtu.be/vuHF_ZeAPVI) \] \[ [Slides](slides/technical_talks/velez.pdf) \]  
Speaker: Erick Velez  

Clang-Doc is a LibTooling-based documentation generator that has been a part of LLVM for almost 10 years. In that timeframe, it has experienced long periods of neglect. However, over the last two years, the project has seen steady improvement. In this talk, we’ll give a historical overview of its development, evolution, improvements to performance, C++ support, and a redesign of its core architecture leveraging Mustache templates.

*Loop Optimisations in LLVM: Mission Impossible?* \[ [Video](https://youtu.be/87UUMVpBAOU) \] \[ Slides \]  
Speaker: Sjoerd Meijer  

At last year’s LLVM Developer Conference, we presented our work on loop vectorization and highlighted the lack of certain loop optimisations as a key factor limiting Clang/LLVM’s ability to generate competitive code for scientific applications compared to other compilers. After another year of effort—and following in the footsteps of many before us— we still don't have any of the loop optimisations running by default, so it’s fair to ask whether loop optimisations in LLVM are a mission impossible. In this follow-up talk, we’ll share what we’ve learned this year, what we’ve achieved, and what’s next, as we explore whether this challenge can truly be overcome.

*Triton-San: Toward Precise Debugging of Triton Kernels via LLVM Sanitizers* \[ [Video](https://youtu.be/Ncvjewv6hZ0) \] \[ [Slides](slides/technical_talks/lu.pdf) \]  
Speaker: Tim Lu  

We evaluated Triton-San on both synthetic micro-benchmarks and real-world kernels from the official Triton tutorial and TritonBench. Our results show that Triton-San detected all known bugs with no false positives and introduced acceptable runtime and memory overhead. This talk will present the motivation, design, and implementation of Triton-San, along with key findings from our evaluation. We will also provide guidance on how to use Triton-San and share details about its public release on GitHub.

*Building an LLVM-based Compiler Toolchain for Distributed Quantum Computing* \[ [Video](https://youtu.be/TukHhQnFRXE) \] \[ [Slides](slides/technical_talks/levytskyy.pdf) \]  
Speaker: Vyacheslav Levytskyy  

As quantum computing is approaching a phase of quantum utility, a need for new compiler toolchains arises to support recent hardware breakthroughs. This talk will present an overview of our MLIR-based compiler infrastructure for quantum photonic networks and explore its design aimed at overcoming the limitations of current quantum devices and support distributed quantum processing. We also aim to provide insights into the specifics of compiler development for quantum computing, guided by non-obvious user priorities and the nuanced behavior of quantum hardware and control devices. The discussion spans from the challenges of adoption of a programming model adequate for extending heterogeneous computing and distributed systems with quantum devices to interfacing with different categories of quantum computing users, via well-established in the field frontends and with the prospect of adopting smoother ways of leveraging quantum MLIR-based compilers and tools. We are exploring the LLVM-based compiler toolchain for quantum computing from low-level details to high-level concepts, from code generation for quantum experiments in real-time setup and for multiple hardware designs and system generations to architectural concerns of supporting resource-efficient scalable quantum computing platform.

*Modular MAX’s JIT Graph Compiler* \[ [Video](https://youtu.be/NQb-Q0g6Pw4) \] \[ [Slides](slides/technical_talks/boulala.pdf) \]  
Speaker: Feras Boulala  

This talk introduces Modular MAX’s \*\*MLIR-based Graph Compiler\*\*, a system designed to overcome the difficulty of extending operator sets in traditional deep learning compilers. Rather than requiring complex rebuilds or separate DSLs, MAX's framework uses a pragmatic, "kernel-first" approach built for extensibility. At its core is a JIT compiler that optimizes model graphs for specific hardware. The key innovation is its use of \*\*Mojo primitives\*\*—such as decorators, parameters, and traits—that empower developers to easily register custom, high-performance kernels directly, without needing to modify and rebuild the underlying compiler infrastructure. The presentation will walk through the compiler's phases, focusing on this extensibility and demonstrating how Mojo-authored kernels interact with the system.

*Building C++ compiler runtimes on demand: Why and how* \[ [Video](https://youtu.be/4oKegT4TWV0) \] \[ [Slides](slides/technical_talks/moses.pdf) \]  
Speaker: Brooks Moses  

TIn Google's internal C++ toolchain, we build the compiler runtimes such as libc++ and llvm-libc "on demand" from source for each user build command (with caching, of course!), rather than using pre-compiled libraries. Doing so allows us to support a much wider range of target systems and sanitizer configurations, while also providing performance improvements and improving the toolchain development and release experience. This talk discusses the build-system mechanisms we use to do this, the practical benefits and costs that we've seen when deploying this, and unique challenges we are facing when using the LLVM runtime-library sources in this manner. The talk should be of interest to attendees who design and maintain toolchain deployments, as well as helping LLVM library maintainers gain insight into this use-case for their code.

*What’s New in VPlan* \[ [Video](https://youtu.be/GYusDQ0tSoY) \] \[ [Slides](slides/technical_talks/hahn.pdf) \]  
Speaker: Florian Hahn  

Since the last presentation focusing on VPlan in 2023, there has been quite a bit of progress along the proposed roadmap, including work on the VPlan-based cost model, improvements to VPlan construction and lowering, and a number of new VPlan transformations. In this talk, we will highlight recent major improvements to the VPlan infrastructure and show a number of examples of new VPlan-based transformations and vectorization features, as well as examples of legacy code replaced by VPlan features. To wrap up, we will revisit the roadmap from 2023 and discuss next steps.

*Taming GPU programming in safe Rust* \[ [Video](https://youtu.be/ASUek97s5P0) \] \[ [Slides](slides/technical_talks/drehwald.pdf) \]  
Speaker: Manuel Drehwald  

This presentation explores a method for safe GPU programming in Rust by leveraging Rust's compiler guarantees, such as ownership and alias analysis, to improve runtime performance for HPC and machine learning applications. The research focuses on how these safety features can be used to optimize code for GPUs, aiming to provide both high performance and memory safety without the typical pitfalls of GPU programming. This work is relevant for developers looking to use Rust for high-performance computing on GPU hardware within the LLVM ecosystem.

*A Better HLSL Compiler: Using the offload-test-suite to improve quality* \[ [Video](https://youtu.be/umTaqZYYBlU) \] \[ [Slides](slides/technical_talks/bieneman.pdf) \]  
Speaker: Chris Bieneman  

Microsoft, and Google have been partnering to add HLSL support to Clang which includes full code generation support for DirectX's DXIL intermediate format and Vulkan's SPIR-V. In this effort we've invested significantly in a new testing infrastructure to enable our project goals. This talk will discuss the project goals, provide an overview of the testing infrastructure, and some early data and real world results demonstrating the value we're already seeing from the infrastructure.

*An overview of recent performance work in libc++* \[ [Video](https://youtu.be/D2P3_G8ZCpU) \] \[ Slides \]  
Speaker: Louis Dionne  

Libc++ has recently been focusing on improving the performance of many Standard APIs. We have also streamlined and improved our benchmarks suite, and made it much easier for contributors to just jump into the code and implement new optimizations. This talk will go over the workflow for contributing performance optimizations to libc++ and showcase some of the most interesting and impactful optimizations contributed in the last few releases.

*Lifetime Safety in Clang* \[ [Video](https://youtu.be/3zWK7Lx96vI) \] \[ [Slides](slides/technical_talks/saxena.pdf) \]  
Speaker: Utkarsh Saxena  

This talk introduces a new, powerful \*\*intra-procedural, flow-sensitive lifetime analysis in Clang\*\* designed to detect complex use-after-scope and use-after-return bugs in C++. Moving beyond simple statement-local checks, this analysis tracks pointer and reference origins across entire function bodies and control-flow paths. It employs a sophisticated dataflow analysis model inspired by \*\*Rust's borrow checker (Polonius)\*\*, using symbolic "Origins" and "Loans" to reason about object lifetimes. The feature is integrated as a native Clang warning, is highly configurable, and is designed for safe default enablement in large codebases. While not a full borrow checker, this analysis lays the crucial infrastructure for potentially introducing Rust-like lifetime annotations into C++ in the future, promising stronger correctness guarantees.

*Area Team Updates* \[ [Video](https://youtu.be/RVImySA_e6A) \] \[ Slides \]  

Updates from the LLVM Area Teams.

**Tutorials**

*Understanding MLIR Crash Reproducers: Debugging, Application, and Best Practices* \[ [Video](https://youtu.be/joTDLdiJpmo) \] \[ [Slides](slides/tutorials/bulavin.pdf) \]  
Speaker: Artemiy Bulavin  

This talk offers a comprehensive guide to the MLIR crash reproducer ecosystem, aimed at developers building and maintaining MLIR-based compilers. We will begin with the fundamentals, demonstrating how to generate and use reproducers with mlir-opt for rapid debugging. We will then cover practical integration strategies, showing how to enable this functionality in a programmatic and user-friendly way via the PassManager, using Triton as an example downstream project. The session will explore best practices for effectively using reproducers, including strategies for minimizing them and the critical distinction between standard and local reproducers for pinpointing the exact point of failure.

*So you want to change the LLVM-IR?* \[ [Video](https://youtu.be/TyOIQ8BaDXc) \] \[ Slides \]  
Speaker: Jeremy Morse  

The LLVM IR is a powerful and flexible intermediate representation. However, it can be challenging to change the LLVM IR without breaking things. In this talk, we will discuss the process of changing the LLVM IR. We will discuss the challenges we faced, the solutions we came up with, and the lessons we learned. We will also discuss how this work can be used to improve the quality of the LLVM IR.

*Scheduling Model in LLVM: Past, Present, and Future* \[ [Video](https://youtu.be/YZHhlmOTG0g) \] \[ [Slides](slides/tutorials/hsu.pdf) \]  
Speaker: Min Hsu  

The LLVM scheduling model is a key component of LLVM's code generation pipeline. In this talk, we will discuss the LLVM scheduling model. We will discuss the challenges we faced, the solutions we came up with, and the lessons we learned. We will also discuss how this work can be used to improve the quality of code generation in LLVM.

*BOLT tutorial on AArch64 and how it competes or complements other PGOs* \[ [Video](https://youtu.be/KdHtOMc5_c8) \] \[ [Slides](slides/tutorials/mpeis.pdf) \]  
Speaker: Paschalis Mpeis  

Many people experiment with BOLT and other Profile-Guided Optimization (PGO) methods because of the performance gains they promise. We often see developers struggle to get BOLT running smoothly or get confused by the variety of PGO methods. This tutorial aims to help with that by building understanding through: \* Break down of the code-layout challenges BOLT solves, visualize them in binaries, and explain why traditional compilers struggle. \* Describe the main profiling techniques and their trade-offs between performance and quality, relative to user's environment or other constraints. \* Briefly compare BOLT, a Post-Link Optimizer (PLO), with other PLOs, as well compile-time or link-time PGOs it competes with or complements, such as Propeller, FE-, IR-, AFDO/S-, CS-, CSS-, HW-, and Temporal-PGO. To wrap up we will demonstrate the flow on a particular binary: 1. Use Arm's latest Performance Analysis tools to predict whether BOLT can improve performance. 2. Capture a profile and optimize the binary with BOLT. 3. Validate results with metrics and visuals. Attendees will learn when to choose BOLT, what problem it solves, how to apply it effectively, and when to combine it with other PGOs.

**Quick Talks**

*Generating efficient CPU code with MLIR for scalable vector extensions in an end-to-end case study* \[ [Video](https://youtu.be/kBOW0tp_6tw) \] \[ [Slides](slides/quick_talks/beysel_warzynski.pdf) \]  
Speakers: Ege Beysel, Andrzej Warzyński  

This talk demonstrates how to generate efficient CPU code for AI workloads using IREE's MLIR-based compiler infrastructure with emphasis on ARM's Scalable Vector and Matrix Extensions (SVE and SME). We explore the integration of SVE and SME code generation into IREE, covering compilation strategies, vectorization techniques, and targeting two AI centric architecture features, namely FEAT\_BF16 and FEAT\_I8MM.

*Accelerating ML on Hexagon: A Glimpse into Qualcomm's MLIR-Based Compiler* \[ [Video](https://youtu.be/ozpJD2u_1ng) \] \[ [Slides](slides/quick_talks/baskaran_slama.pdf) \]  
Speakers: Muthu Baskaran, Franck Slama  

In this talk, I'll present an overview of Qualcomm's MLIR-based compiler for machine learning models, designed to target the Hexagon™ DSP via the Hexagon™ LLVM backend. I'll outline the high-level architecture of the compiler stack, which lowers Torch models to Hexagon assembly, highlighting how MLIR enables modular and extensible compilation for embedded ML workloads. I'll also touch on some of the key technical challenges the team has been addressing, such as memory management on constrained devices. This session aims to give attendees a quick but insightful look into the practical application of MLIR in a production-grade compiler.

*Where We're Legalizing, We Don't Need Validators: Generating valid DXIL for the DirectX Backend* \[ [Video](https://youtu.be/BvkWLJJjiL8) \] \[ [Slides](slides/quick_talks/lotfi.pdf) \]  
Speaker: Farzon Lotfi  

In this talk, we present a plan for a validator-free pipeline for targeting DXIL directly from LLVM. By reimagining the classic LLVM-to-DXIL flow, we've developed a suite of legalizations and transformations that make DXIL generation predictable, robust, and compliant from the outset. We'll cover our approach to data scalarization, leveraging and adapting the existing LLVM Scalarizer. We'll also dive into our array flattening work, which transforms nested and multidimensional arrays into forms acceptable by the DXIL backend. By carefully reusing and extending LLVM infrastructure, we've built a system that emits DXIL-ready code which will eventually no longer require a post-hoc validator step.

*An investigation of missed devirtualization opportunities* \[ [Video](https://youtu.be/l7dTGVsaf6w) \] \[ [Slides](slides/quick_talks/amiri.pdf) \]  
Speaker: Ehsan Amiri  

We will present two groups of missed opportunities in whole program devirtualization (WPD). Currently we have statistics that shows catching one the two cases will increase the number of devirtualized callsites in some popular C++ open source programs by thousands or hundreds (0.5% to 3.5% of all virtual calls that are not devirtualized by WPD). In both groups of missed opportunities there is enough information to devirtualize the call in the source code and in the same function as the virtual callsite. Unfortunately catching these missed cases does not seem easy. We will discuss why currently devirtualization misses these opportunities and what are the challenges to make it happen. One notable issue that is highlighted during the discussion is the existing tension between WPD and non-strict-aliasing. After reminding this issue using an example, we will discuss why we think a language level improvement is needed to address this issue.

*Understanding linalg.pack and linalg.unpack* \[ [Video](https://youtu.be/Q6ryij-nJrM) \] \[ [Slides](slides/quick_talks/bartel.pdf) \]  
Speaker: Maximilian Bartel  

The linalg.pack and linalg.unpack operations enable critical data layout transformations for tensor computations in MLIR. This talk examines their design, implementation challenges, and production deployment insights. We begin by demonstrating how these operations facilitate efficient mapping to hardware-specific kernels, particularly for matrix multiplication workloads. Through visual examples, we illustrate the transformation patterns and their impact on memory access efficiency. Drawing from production AI compiler development, we present concrete examples of semantic ambiguities encountered during implementation—cases where operation behavior was undefined or inconsistent. We detail how these issues were identified, their implications for correctness, and the solutions adopted by the MLIR community. The talk concludes with practical guidance on when and how to employ these operations effectively. We share performance considerations for both isolated kernels and full network compilation and discuss the trade-offs between transformation overhead and execution efficiency. Attendees will gain actionable knowledge for integrating linalg.pack/unpack into their compilation flows while avoiding common implementation pitfalls.

*Optimizing IREE to Match llama.cpp: An Introduction to IREE optimization for newbies through a benchmark journey* \[ [Video](https://youtu.be/yLZW-xWVDT8) \] \[ [Slides](slides/quick_talks/eom.pdf) \]  
Speaker: Uiseop Eom  

Deploying efficient machine learning inference engines often involves rigorous benchmark comparisons to achieve optimal performance. In this talk, we present a benchmark analysis comparing the inference performance of IREE against llama.cpp, focusing specifically on executing open-source llama3 model. Attendees will learn about the performance gaps initially observed between IREE and llama.cpp, and the targeted optimizations we implemented within the iree-compiler to bridge these gaps. The session will introduce common performance bottlenecks faced by new users of iree-compiler and iree-runtime, including typical profiling tips. We will demonstrate practical MLIR optimizations and how to implement them. This talk aims to be especially valuable for newcomers looking to understand and enhance performance when leveraging IREE for model inference tasks.

*Optimizing generic code lowering to LLVM-IR through function equivalence coalescing* \[ [Video](https://youtu.be/0mH_024cHUw) \] \[ [Slides](slides/quick_talks/sbirlea.pdf) \]  
Speaker: Alina Sbirlea  

This talk describes a solution for the problem of duplicate LLVM IR functions being emitted when lowering generic code such as C++ templates, and generics in Rust, Swift, or Carbon. The aim is to tackle the issue of code size and high compile-times, originally impacting C++ templates, for which a front end approach is expected to be more efficient than LLVM's function merging pass. We present an algorithm for coalescing different front-end level functions into a single LLVM IR function when such functions are equivalent in LLVM IR. For this, we use LLVM types for building a canonical fingerprint for functions, even when such types are distinct in the language's front end. We implement this proof of concept in Carbon's front end during the lowering to LLVM-IR stage. The algorithm determines if two functions are equivalent by considering their SemIR (Carbon's IR) representation and their lowered LLVM type information, handling recursion through strongly-connected components (SCCs) call graph analysis, and using two types of fingerprints in order to identify potential equivalences. We also discuss alternatives and future improvements.

*Project Widen Your Char-izons: Adding wchar support to LLVM-libc* \[ [Video](https://youtu.be/YjI9dum74uM) \] \[ [Slides](slides/quick_talks/nawaz_pratipati.pdf) \]  
Speakers: Uzair Nawaz, Sriya Pratipati  

Project Widen Your Char-izons adds wide character functionality to LLVM-libc. This includes implementing parallels to standard string utilities (e.g., concatenation, length) and facilitating conversions between multibyte and wide characters, currently supporting UTF-8 and UTF-32 encodings. There were many interesting implementation details and design choices that had to be made when implementing these functions, such as "how do we handle someone partially converting a character" or "should we consider multiple wide character sizes" (we wanted the answer to be no). This talk aims to elaborate on the design decisions and challenges encountered during the implementation of these libc functions. It is primarily targeted at runtime developers interested in character encodings. The content is moderately technical, focusing on our design rationale and the trade-offs involved in decisions that were not pursued. The ultimate goal is to explain the established framework and demonstrate its potential for future expansion to UTF-16.

*Extending ThinLTO Support for AMDGPU* \[ [Video](https://youtu.be/hEnUlpTWnHk) \] \[ [Slides](slides/quick_talks/tian.pdf) \]  
Speaker: Shilei Tian  

In this talk, we'll briefly introduce the ongoing effort to support ThinLTO for AMDGPU. We'll start by discussing the motivation for enabling ThinLTO and the current limitations in the AMDGPU ABI that prevent us from using it out of the box. By default, ThinLTO compiles modules from each translation unit in parallel, effectively following a split scheme based on translation units. To work around some of the limitations, we've made targeted modifications to the existing ThinLTO infrastructure. However, not all limitations can be addressed with workarounds. To properly support ThinLTO, we'll introduce a new split scheme that divides the program based on a graph constructed from the module summary. The remaining ThinLTO infrastructure will then compile the resulting splits in parallel, instead of compiling modules per translation unit as ThinLTO does by default. We also expect this new scheme to benefit other GPU targets that don't share the same ABI constraints as AMDGPU.

*TangoLLVM: An LLVM Backend for the Go compiler* \[ [Video](https://youtu.be/5uSGRZAIaVg) \] \[ [Slides](slides/quick_talks/gu.pdf) \]  
Speaker: Tianxiao Gu  

We add LLVM as an alternative backend for the Go compiler. The LLVM backend can be used to generate code for selected functions only. Different from TinyGo or GOLLVM, we do not aim at building everything using LLVM. Instead, we still use the Go compiler to parse and compile the source code to obtain an object file. Before lowering the Go SSA into platform dependent format, we translate the generic Go SSA into LLVM bitcode, compile the bitcode and generate the necessary auxiliary data (e.g., GC stack maps), and patch the code and auxiliary data into the object file generated by the Go compiler. In this way, we can first reuse many optimizations that have been applied before lowering (e.g., escape analysis, nil check elimination). Second, we have no need to deal with the Go ABI internal to lower every call instruction to LLVM IR. We do not need to generate type descriptors and other module data at LLVM. Third, we can reuse many optimizations released in LLVM. For example, we do additional inlining at LLVM side to further improve performance. We have implemented TangoLLVM on top of Go 1.19/1.24 and LLVM19. We have evaluated TangoLLVM on go1 benchmark suite. The geomean improvement is 10.41%.

*MLIR based graph compiler for in-memory inference computing* \[ [Video](https://youtu.be/vtE_3xit044) \] \[ [Slides](slides/quick_talks/jain_srivastava.pdf) \]  
Speakers: Kshitij Jain, Satyam Srivastava  

Inference for LLMs has brought newer challenges to be addressed in compute space like KV-cache. d-matrix has designed an accelerator which is suited for llm inference. In this talk we would like to address the design challenges faced while designing a compiler for the hierarchical distributed shared memory inference chip. An MLIR based compiler tool chain was designed from ground up to tackle the native code generation issues. Novel bottom up based fine grained scale out solution was designed at affine dialect level to address the inference scale out. The talk will also address the integration of subset of triton language to the PyTorch compiler tool chain.

*Building an MLIR Compiler for Real-Time AI on Existing 5G Infrastructure* \[ [Video](https://youtu.be/UGHJV2bUhW8) \] \[ [Slides](slides/quick_talks/nudelman_tyagi.pdf) \]  
Speakers: Isaac Nudelman, Ankush Tyagi  

This talk explores how we developed a MLIR based compiler for Ericsson's many-core architecture to enable real-time AI inference for 5G baseband infrastructure. While recent improvements in compiler optimization and model compression have enabled efficient deployment of models on embedded systems, there are still gaps, especially for real-time applications. We will discuss the specific challenges we encountered, such as optimizations that hurt latency and upstream assumptions about hardware. We will also discuss the strategies we used to overcome these hurdles, including the different approaches available to develop hardware specific optimizations, as well as making effective use of quantization and model architecture adjustments to reduce latency.

*Are we fully leveraging TableGen in MLIR?* \[ [Video](https://youtu.be/bo5krmvbS9c) \] \[ [Slides](slides/quick_talks/jain.pdf) \]  
Speaker: Kshitij Jain  

While TableGen descriptions in MLIR greatly reduce boilerplate in creating new IR entities (dialects, types, ops etc.), their utility is sometimes underestimated beyond this narrow role. TableGen descriptions, should and can be more. As such, the goal of this talk is to demonstrate why Tablegen descriptions should —— and how they can —— serve as a single source of truth, for a given IR entity, encoding all information required to effectively interface with said IR entity. Rich TableGen descriptions can: 1) Make a compiler's domain and feature-set clearer. 2) Make a compiler's behavior more apparent and robust. 3) Reduce the mental overhead on compiler developers. 4) Lower the barrier to entry for new contributors. Audience can expect this talk to help them realize the above-mentioned benefits of richer TableGen descriptions through existing utilities, concepts, and often underappreciated software engineering pragmatisms.

*MLIR Testing Guide – What and Why?* \[ [Video](https://youtu.be/_6stF7fjfXY) \] \[ [Slides](slides/quick_talks/warzynski.pdf) \]  
Speaker: Andrzej Warzyński  

MLIR includes a dedicated Testing Guide that prescribes how to write minimal, consistent, and discoverable tests. Unlike other testing guides in LLVM that leave formatting choices to contributors, the MLIR guide takes an extra step - it discusses in detail how to structure and document tests effectively. This talk will highlight the core principles of the formatting guide ("what") and explain the reasoning behind them ("why"). It will demonstrate how to write self-documenting tests that make it easier to spot edge cases being exercised - and those that are missing. Real-world examples will show how adopting the guide helped identify duplicated tests and reduce redundancy. The presentation is both an encouragement and a call to action to adopt the guide more broadly. It will also touch on potential future directions for improving MLIR's test ecosystem.

*LLM Schedule Primitive Generator with MLIR based Polyhedral Engine* \[ [Video](https://youtu.be/LXQqdqJGXWU) \] \[ [Slides](slides/quick_talks/wang.pdf) \]  
Speaker: Kai-Ting Amy Wang  

Using the open-sourced and MLIR-based Polymorphous project \[1\], we explore using LLM agents to generate schedule primitives that result in competitive performance for Polybench. Our method consists of two stages: first, a planning agent proposes a high level transformation strategy and second, a coding agent realizes the strategy in syntactically correct MLIR. The coding agent iteratively attempts to produce correctly labeled payload IR and transform IR as guided by feedbacks from mlir-opt. Initial experiments show that 29 out of 30 Polybench testcases compile and run successfully with competitive performance, highlighting the potential of LLMs for optimization and code generation. Ongoing performance tuning includes multi-agent LLM techniques to improve the generated transformation sequences.

*New & Improved LLVM Premerge Testing: Status Update* \[ [Video](https://youtu.be/A_IY7qgyM6s) \] \[ [Slides](slides/quick_talks/grossman_tice.pdf) \]  
Speakers: Aiden Grossman, Caroline Tice  

In this talk we will give an update on the new premerge testing system, including all the improvements that we have made (and are continuing to make): We have eliminated a major pain point for libc++ developers, by migrating libc++ premerge testing to a set of more powerful, dedicated (non-preemptible) machines; we have made testing both faster and more reliable, by improving start up and build performance and reducing the flakiness of test results; we have made it easier to see and track the performance improvements over time, by overhauling our new dashboard(s) that show the performance and build latencies for the premerge tests. If there is time we will also present our plans for future improvements to the premerge testing system.

*Timing-Resistant Coding Support in LLVM* \[ [Video](https://youtu.be/zLBEXGTdd6o) \] \[ [Slides](slides/quick_talks/alexandre.pdf) \]  
Speaker: Julius Alexandre  

There is a fundamental tension between cryptographic coding and compiler optimizations. When cryptographers write C and C++ code that needs to be constant-time, they tend to follow bitwise arithmetic recipes that unfortunately do not always stand up to the optimization pipeline, or they write raw inline assembly. WYSIWYG compiler-level support for constant-time coding will prevent attackers from learning useful information from timing conditional branches, jumps, and memory accesses, and will make it simpler for cryptographers to build the functionality that we all rely on in TLS libraries, hash functions, and more. This talk will cover the technical challenges of constant-time coding support in Clang and LLVM, and how optimization passes can inadvertently introduce timing vulnerabilities.

*Impossible Perspectives in Data Layout* \[ [Video](https://youtu.be/GkDhot6I8ec) \] \[ [Slides](slides/quick_talks/bogner.pdf) \]  
Speaker: Justin Bogner  

In this talk, we'll discuss the challenges we faced representing constructs in HLSL that are somewhat odd compared to the usual rules of C and C++, and consider the tradeoffs of various approaches along the way. There are several contexts where HLSL doesn't match C++ in terms of layout. "CBuffers" have rules that grew out of the history of shading languages, DirectX APIs, and weird GPU hardware that result in odd alignment and padding requirements, especially for arrays. The packoffset feature of CBuffers and the vk::offset attribute which can inject arbitrary amounts of padding into a structure. Small vector types are aligned based on their element type instead of their total size. All of these need some care in how they're handled throughout the compiler. This talk will discuss the implementation, present lessons learned, and consider where these techniques are useful in other contexts.

*Towards Automatic Reduction of Module Bugs* \[ [Video](https://youtu.be/8dLPQLwSe_U) \] \[ [Slides](slides/quick_talks/ivanov.pdf) \]  
Speaker: Maksim Ivanov  

Tools that automatically reduce compiler bugs have been known for a long time (C-Reduce, C-Vise, etc.) and have been used effectively to get small reproducers from tens or even hundreds of megabytes of code. However, reducing C++ module bugs specifically presents unique challenges that rendered the tools virtually unusable for that use-case. In this talk, we discuss how we automated module bug reduction at Google by adding necessary support to C-Vise, as well as other improvements we made in the process.

*Save Our Source-Locations* \[ [Video](https://youtu.be/OJMToFlxqog) \] \[ [Slides](slides/quick_talks/livermore-tozer.pdf) \]  
Speaker: Stephen Livermore-Tozer  

Keeping an accurate record of source locations for instructions is necessary for both debugging and sample-based PGO, but LLVM can often fail to do so, in part due to the unnecessary dropping of source location information during optimizations, which has led to degradation of source location quality over the course of LLVM's development. To counteract this, we at Sony have added a new feature to LLVM to better track and describe missing source locations, in order to permanently fix this class of problem: this talk will explain how this feature works and what it means for LLVM developers going forwards.

**Lightning Talks**

*Mojo GPU Compilation* \[ [Video](https://youtu.be/aY6I76b8rLY) \] \[ [Slides](slides/lightning_talks/chen_dakkak.pdf) \]  
Speakers: Weiwei Chen  

Mojo is a heterogeneous programming language in the python family which unifies CPU+GPU programming. It's the cornerstone of the Modular MAX inference engine — and is used extensively to unlock high performance on heterogenous platforms while ensuring maintainability. This talk is aimed at people who are interested in the GPU kernel programming in Mojo along with how Mojo's unique compilation flow enables it to offload work to the accelerator from the library.

*PyDSL: A MLIR DSL for Python developers* \[ [Video](https://youtu.be/7_dB2QolUkc) \] \[ [Slides](slides/lightning_talks/wang.pdf) \]  
Speaker: Kai-Ting Amy Wang  

Since its December 2023 debut, PyDSL has enabled Python-based prototyping language with a clean, developer-friendly syntax to access MLIR's powerful compiler infrastructure. PyDSL bridges this gap by offering a programming model that imitates native Python semantics while compiling to efficient MLIR code. We review PyDSL's core design and introduce key enhancements in the latest edition: a lightweight autotuning system for dynamic kernel specialization, seamless Triton interoperability, and more Pythonic programming styles to write MLIR programs. These improvements add expressive power, reduce boilerplates, and empower developers to write optimized high-performance MLIR kernels entirely within a subset of Python.

*Continuous Integration System for Global ISel* \[ [Video](https://youtu.be/SImisNPSNpM) \] \[ [Slides](slides/lightning_talks/hickey.pdf) \]  
Speaker: Neil Hickey  

The Global ISel (GISel) framework in LLVM has gained traction as a modern alternative for instruction selection and is also the default selector at O0 for AArch64. Unlike the traditional SelectionDAG approach, GISel works directly on a linear intermediate representation, aiming to improve compile-time performance by bypassing DAG construction. However, GISel's adoption across all backends is limited by its incomplete coverage of instruction selection cases, which necessitates fallbacks to SelectionDAG. To address and monitor these limitations, we developed a specialized continuous integration (CI) system that automatically builds the latest LLVM daily, compiles a broad set of benchmarks (like RajaPerf, TSVC, SPEC 2017, and the LLVM test suite), and reports every fallback event with detailed phase and instruction data. This CI system provides a visualization dashboard for real-time tracking, fostering transparency and enabling the LLVM community to systematically close GISel's gaps. While significant progress has been made—such as achieving fallback-free runs for TSVC—fallbacks still occur in other benchmarks like RajaPerf, underscoring the ongoing need for comprehensive monitoring and targeted improvements.

*LLDB MCP* \[ [Video](https://youtu.be/OJas4nknp0o) \] \[ [Slides](slides/lightning_talks/devlieghere.pdf) \]  
Speaker: Jonas Devlieghere  

This talk introduces the new support for the Model Context Protocol (MCP) in LLDB, enabling agent-driven debugging workflows. MCP provides a standardized way for AI models to access external tools, bridging the gap between large language models and LLDB. Users can interact with the debugger using natural language, which the model translates into LLDB commands executed over MCP. Key benefits include reduced context switching between debugging tools and AI assistants, more intuitive debugging for novice developers, and the ability to leverage AI's pattern recognition capabilities for tedious or repetitive debugging tasks.

*Shared Representation across Languages* \[ [Video](https://youtu.be/N2Qv_o5lhCE) \] \[ [Slides](slides/lightning_talks/mcmichen.pdf) \]  
Speaker: Tommy McMichen  

The LLVM compiler has a low-level view of memory, permitting fine-grained control over memory in source languages. This low level representation hinders analysis and optimization, and the freedoms it grants are not always needed. We find that most memory used in performance-critical C/C++ applications implement data collections with high-level properties that can be leveraged in the compiler. In this talk, we describe MEMOIR, an extension to the LLVM IR that provides a first-class representation for common data collection types and operations. We will demonstrate how our extension improves conventional compiler analysis and transformation, and enables new optimizations on memory layout and collection implementation. We conclude by presenting ongoing work on front-end support for C/C++ and Rust that pave the way towards collection-oriented compilers in both LLVM and MLIR.

*LLVM Advisor* \[ [Video](https://youtu.be/AR4t4azfKL8) \] \[ [Slides](slides/lightning_talks/sala.pdf) \]  
Speaker: Kevin Sala  

LLVM Advisor addresses the challenge of processing overwhelming compiler output by providing a unified visualization tool for LLVM remarks, profiling data, and other compilation artifacts. This talk demonstrates how developers can transform scattered compiler diagnostics into actionable insights through an intuitive local web-based interface, making offloading optimization information more accessible to both newcomers and experienced developers.

*llvm-exegesis on AArch64: What Works and What Doesn't?* \[ [Video](https://youtu.be/YIgWZihk85s) \] \[ [Slides](slides/lightning_talks/meijer.pdf) \]  
Speaker: Sjoerd Meijer  

This talk provides an update on the effort to improve AArch64 support for llvm-exegesis, a benchmarking tool that measures instruction characteristics. Initially, the tool was largely dysfunctional on AArch64, with the vast majority of its ~6,000 generated tests failing due to issues like uninitialized operands, pseudo-instructions, and segmentation faults. Through systematic improvements—including expanding register class support, disabling unsupported instructions, and adding basic load/store functionality—the team has dramatically increased the number of cleanly-running test cases from just over 100 to more than 4,300. The presentation will detail these fixes and outline future work, which will focus on enhancing support for load/store instructions and improving the accuracy of latency measurements.

*How to test and evaluate LLVM-libc on embedded applications* \[ [Video](https://youtu.be/Dta6nQLmCOY) \] \[ [Slides](slides/lightning_talks/huynh.pdf) \]  
Speaker: William Huynh  

For years, Arm has been building an embedded toolchain with picolibc as the default C library. Recently, a promising new C library, LLVM-libc, has emerged. How do we know when is the right time to switch over? What are the challenges of testing libraries on embedded applications? The intended audience includes those looking for an introduction to LLVM-libc on embedded and beginners interested in learning how to test embedded applications.

*Non-attribute property improvements in MLIR* \[ [Video](https://youtu.be/aqbeDB3xf9o) \] \[ [Slides](slides/lightning_talks/drewniak.pdf) \]  
Speaker: Krzysztof Drewniak  

Over the past year, many improvements have been made to the infrastructure for using non-attribute properties in MLIR. Such properties allow constants and other data to be stored inline in the operation struct without potentially-expensive attribute uniquing. This presentation will showcase these improvements, such as new support for such properties in TableGen-based builder/parser/printer generation, operation verification, improved generic builders, and declarative rewrite rules. It will also present future directions for non-attribute properties.

*Can Vectorization Slow Down Performance? Addressing the Challenges of Vectorizing Stride Access* \[ [Video](https://youtu.be/xHzVLvWmF0U) \] \[ [Slides](slides/lightning_talks/kinoshita.pdf) \]  
Speaker: Kotaro Kinoshita  

TSVC is a benchmark designed to measure the vectorization capabilities of compilers. In one of its test cases, s128, it has been discovered that vectorization in LLVM can cause performance degradation under certain conditions. We found that this degradation is caused by vectorizing strided access, and such issues occur even in simple cases. This talk will present potential LLVM improvements for vectorizing strided access and discuss future directions for enhancing its performance.

**Student Technical Talks**

*MARCO - Modelica Advanced Research COmpiler* \[ [Video](https://youtu.be/u3wvGOYXAaI) \] \[ [Slides](slides/student_talks/scuttari.pdf) \]  
Speaker: Michele Scuttari  

Modelica is a high-level, equation-based language used for modeling complex physical systems. MARCO (Modelica Advanced Research Compiler) is a novel compiler that leverages MLIR to bring modern compiler infrastructure to the Modelica ecosystem. This talk introduces MARCO's architecture and its MLIR-based lowering strategy for Modelica's Differential-Algebraic Equation (DAE) systems. The talk is aimed at developers interested in domain-specific language compilation, and attendees will take away insights on integrating MLIR for descriptive, non-traditional, languages like Modelica. The project has been first and only presented at the Modelica conference in 2023, but it has never been proposed to a compiler-oriented audience.

*Translation Validation for LLVM's RISC-V Backend* \[ [Video](https://youtu.be/znMGXxQC12A) \] \[ [Slides](slides/student_talks/briles.pdf) \]  
Speaker: Mitch Briles  

With algorithms such as instruction selection, instruction folding, and register allocation, LLVM's backends have the job of lowering IR to assembly or object code while being mindful of the semantics of each language. Starting with AArch64, we're leveraging Alive2 to validate these target-dependent optimizations and translations. After using our tool to find 44 miscompiles in the AArch64 backend, the natural progression is to branch out to other architectures. Our next focus is a much smaller ISA: RISC-V. The new tool, RISCV-TV, is early in development, but has already detected 2 miscompiles! Bugs can be found in existing tests, but these tools are most effective when paired with a fuzzer. We anticipate more results by the time of the meeting.

*Leveraging MLIR to Compile a Basis-Oriented Quantum Programming Language* \[ [Video](https://youtu.be/gcpe6SGCH4I) \] \[ [Slides](slides/student_talks/adams.pdf) \]  
Speaker: Austin Adams  

Quantum computing has leaped from the theoretical realm into a competitive commercial race, but programming quantum computers remains challenging. Quantum programming languages today require programmers to master both physics notation and quantum gate engineering. The Qwerty quantum programming language was recently proposed (arXiv:2404.12603) as a higher-level abstraction providing primitives rooted in quantum bases rather than low-level quantum circuitry. The semantic gap between Qwerty's novel basis-oriented constructs and traditional quantum circuits renders existing quantum compilers unsuitable for compiling Qwerty code. This talk describes how MLIR is used in our Qwerty compiler to compile Qwerty code embedded in Python into quantum assembly or LLVM IR. The full architecture of our compiler is described, including custom MLIR dialects, interfaces, analyses, and passes. A brief comparison between all known quantum MLIR dialects will also be presented.

**Panels**

*Contributing to Clang* \[ [Video](https://youtu.be/a5QorEEk8Js) \] \[ Slides \]  
Speakers: Aaron Ballman, Corentin Jabot, Erich Keane  

You want to start contributing to Clang, but aren't sure where to start? You are wondering what it takes to maintain Clang, and how we prioritize features, triage bugs? Or maybe you just want to ask us some burning questions. Come join a group of long-term Clang maintainers to talk about the challenges of community building, onboarding, and maintaining a large open-source project. How does Clang balance the needs of our users, the other parts of LLVM, and multiple committees, while fostering a welcoming community? What can we improve, and how can you help?

**Posters**

*Optimizing IREE to Match llama.cpp: An Introduction to IREE optimization for newbies through a benchmark journey* \[ Slides \]  
Speaker: Uiseop Eom  

Deploying efficient machine learning inference engines often involves rigorous benchmark comparisons to achieve optimal performance. In this talk, we present a benchmark analysis comparing the inference performance of IREE against llama.cpp, focusing specifically on executing open-source llama3 model. Attendees will learn about the performance gaps initially observed between IREE and llama.cpp, and the targeted optimizations we implemented within the iree-compiler to bridge these gaps. The session will introduce common performance bottlenecks faced by new users of iree-compiler and iree-runtime, including typical profiling tips. We will demonstrate practical MLIR optimizations and how to implement them. This talk aims to be especially valuable for newcomers looking to understand and enhance performance when leveraging IREE for model inference tasks.

*Better multithreading with LLVM* \[ Slides \]  
Speaker: Jameson Nash  

While no sane compiler would optimize atomics, we aren't always particularly sane. We'll look at three ways that llvm could do more to interact with threads better: thread static analysis warnings, new code optimizations for atomic update loops, and a work-stealing runtime for the llvm backend.

*XeGPU: A High-Performance MLIR Dialect for Intel GPU Programming* \[ Slides \]  
Speakers: Chao Chen, Jianhui Li  

We present XeGPU, the official MLIR dialect for programming Intel GPUs. Built on experience from the XeTile prototype introduced last year, XeGPU brings a simplified, layout-guided programming model tailored for tile-based GPU kernel development. By representing tile decomposition through layout annotations instead of multiple explicit tiled loops, XeGPU produces IR that is both more concise and easier to reason about and optimize. In contrast to Triton and CUTE, which employ general-purpose layout algebra, XeGPU introduces a straightforward nested block layout abstraction. This design effectively captures common patterns such as transpose, broadcast, reduction, and matrix-matrix multiply (MMA), enabling concise and performant kernel construction. XeGPU allows developers to define high-level workgroup operations using layout-annotated types, which guide hierarchical lowering using upstream MLIR infrastructure. The lowering process includes workgroup-to-subgroup distribution, blocking, and subgroup-to-workitem decomposition, all expressed through MLIR's transformation pipelines. The dialect lowers to Intel GPU ISA through LLVM-based code generation and enables mapping to hardware features such as shared local memory and matrix instructions. We evaluate XeGPU on a range of matrix multiplication (GEMM) workloads and compare it against hand-written reference kernels. XeGPU achieves competitive performance while maintaining a compact and composable intermediate representation. This work demonstrates how a domain-specific layout abstraction can simplify GPU programming without compromising performance, and how MLIR can serve as a foundation for building production-grade AI compilers.

*Mojo GPU Compilation* \[ Slides \]  
Speakers: Weiwei Chen, Abdul Dakkak  

Mojo is a heterogeneous programming language in the python family which unifies CPU+GPU programming. It's the cornerstone of the Modular MAX inference engine — and is used extensively to unlock high performance on heterogenous platforms while ensuring maintainability. This talk is aimed at people who are interested in the GPU kernel programming in Mojo along with how Mojo's unique compilation flow enables it to offload work to the accelerator from the library.

*Towards Collection-Oriented Compilation in LLVM* \[ Slides \]  
Speaker: Tommy McMichen  

The LLVM compiler has a low-level view of memory, permitting fine-grained control over memory in source languages. This low level representation hinders analysis and optimization, and the freedoms it grants are not always needed. We find that most memory used in performance-critical C/C++ applications implement data collections with high-level properties that can be leveraged in the compiler. In this talk, we describe MEMOIR, an extension to the LLVM IR that provides a first-class representation for common data collection types and operations. We will demonstrate how our extension improves conventional compiler analysis and transformation, and enables new optimizations on memory layout and collection implementation. We conclude by presenting ongoing work on front-end support for C/C++ and Rust that pave the way towards collection-oriented compilers in both LLVM and MLIR.

*LLVM Advisor* \[ Slides \]  
Speaker: Kevin Sala  

LLVM Advisor addresses the challenge of processing overwhelming compiler output by providing a unified visualization tool for LLVM remarks, profiling data, and other compilation artifacts. This talk demonstrates how developers can transform scattered compiler diagnostics into actionable insights through an intuitive local web-based interface, making offloading optimization information more accessible to both newcomers and experienced developers.

# Code of Conduct

The LLVM Foundation is dedicated to providing an inclusive and safe experience for everyone. We do not tolerate harassment of participants in any form. By registering for this event, we expect you to have read and agree to the [LLVM Code of Conduct](http://llvm.org/docs/CodeOfConduct.html).

# Contact

To contact the organizer, [email events@llvm.org](mailto:events@llvm.org)

</div>

<!-- *********************************************************************** --> <!--#include virtual="sponsors.incl" -->

* * *
