---
layout: "default.html"
permalink: "devmtg/2022-04-03/index.html"
---
# Sixth LLVM Performance Workshop at CGO

*   **What:** Sixth LLVM Performance Workshop at CGO
*   **When:** Sunday April 03, 2022
*   **Where:** Virtual
*   **Proposals should be submitted to:** [Easychair Submission Link](https://easychair.org/conferences/?conf=llvmcgo2022)
*   **The deadline for receiving submissions is:** March 01, 2022
*   **Speakers will be notified of acceptance or rejection by:** March 07, 2022

The Sixth LLVM Performance Workshop will be held at ([CGO 2022](https://conf.researchr.org/track/cgo-2022/cgo-2022-workshops-and-tutorials)). The workshop is co-located with CC, HPCA, and PPoPP. If you are interested in attending the workshop, please register at the ([CGO website](https://conf.researchr.org/home/cgo-2022)). The organizing committee of CGO/PPoPP/HPCA/CC has decided to make the conference virtual this year.

Program Committee:

*   Johannes Doerfert (jdoerfert at anl.gov)
*   Aditya Kumar (adityak at snap.com)
*   Jose M Monsalve Diaz (jmonsalvediaz@anl.gov)
*   Shilei Tian (i@tianshilei.me)

# Schedule

| Time (EDT) | Speaker | Title | Topic |
| --- | --- | --- | --- |
| 13:00 - 13:15 (15 min) | [Jose M Monsalve Diaz](https://www.linkedin.com/in/josemonsalve2/)<br>[Johannes Doerfert](https://www.google.com/url?q=https://www.linkedin.com/in/johannes-doerfert-3a0770a2/&sa=D&source=editors&ust=1647549339251666&usg=AOvVaw2O1D9myHz5uLu0_NLPCVO0)<br>[Aditya Kumar](https://www.google.com/url?q=https://hiraditya.github.io/&sa=D&source=editors&ust=1647549339251913&usg=AOvVaw0Jon2xtUE-YxYLqfoxI9YR) | Opening remarks | Welcome and introduction |
| 13:15 - 14:00 (45 min) | [Nikita Popov](https://www.npopov.com/aboutMe.html) | [Keynote: Opaque Pointers Are Coming](#keynote)<br>\[[slides](slides/keynote.Opaque.Pointers.Are.Coming.pdf)\] | Keynote |
| 14:00 - 14:30 (30 min) | Mohd. Muzzammil<br>Abhay Mishra<br>Sumit Lahiri<br>Awanish Pandey<br>Subhajit Roy | [The Hot Path SSA Form in LLVM](#hot-path)<br>\[[slides](slides/The.Hot.Path.SSA.Form.in.LLVM.pdf)\] | OPT Analysis, MLIR |
| 14:30 - 15:00 (30 min) | Shalini Jain<br>Yashas Andaluri<br>Venkatakeerthy S.<br>Ramakrishna Upadrasta | [POSET-RL: Phase ordering for Optimizing Size and Execution Time using Reinforcement Learning](#poset-rl)<br>\[[slides](slides/POSET-RL.Phase.ordering.for.Optimizing.Size.and.Execution.Time.using.Reinforcement.Learning.pdf)\] | Opt, Code size, ML |
| 15:00 - 15:30 (30 min) | Sandya Mannarswamy<br>Dibyendu Das | [Learning to combine Instructions in LLVM Compiler](#learning-combine)<br>\[[slides](slides/Learning.to.Combine.Instructions.in.LLVM.Compiler.pdf)\] | ML, Development |
| 15:30 - 16:00 (30 min) | Break |
| 16:00 - 16:45 (45 min) | William Moses<br>Johannes Doerfert | [\[Tutorial\] An Guide to Performance Debugging LLVM-based Programs](#tutorial-guide) | Tutorial, Debugging, Performance |
| 16:45 - 17:15 (30 min) | Mats Petersson | [Compiling, running and benchmarking SNAP with LLVM Flang - experiences with a new compiler](#compiling-running)<br>\[[slides](slides/Building.and.running.SNAP.using.LLVM.Flang.pdf)\] | Flang, Application, OpenMP |
| 17:15 - 17:45 (30 min) | Haochen Wang<br>Tomasz Czajkowski<br>Ehsan Amiri | [An Anatomy of Optimized Matrix Multiplication on AArch64](#anatomy-optimized)<br>\[[slides](slides/An.Anatomy.of.Optimized.Matrix.Multiplication.in.AArch64.pdf)\] | DSL, IR |
| 17:45 - 18:05 (20 min) | Break |
| 18:05 - 18:35 (30 min) | Joseph Huber | [Improving the OpenMP Offloading Driver: LTO, libraries, and toolchains](#improving-openmp)<br>\[[slides](slides/Improving.the.OpenMP.Offloading.Driver.LTO.libraries.and.toolchains.pdf)\] | OpenMP, LTO |
| 18:35 - 19:15 40 min) | Djordje Todorovic<br>Bharathi Seshadri<br>Ananthakrishna Sowda<br>Nikola Tesic<br>Ivan Baev | [Crash-Analyzer: An LLVM-based Tool for Triaging and Analyzing Crashes](#crash-analyzer)<br>\[[slides](slides/llvm-crash-analyzer.pdf)\] | Tools, MachineIR Analysis |
| 19:15 - 19:45 (30 min) | Juneyoung Lee<br>Woosung Song | [Prototyping a compiler for homomorphic encryption using MLIR](#prototyping-compiler)<br>\[[slides](slides/Prototyping.a.compiler.for.homomorphic.encryption.in.MLIR.pdf)\] | MLIR, DSL |
| 19:45 - 20:30 (45 min) | Arnamoy Bhattacharyya<br>Peixin Qiao<br>Bryan Chan | [\[Tutorial\] A walk through Flang OpenMP lowering: From FIR to LLVMIR](#tutorial-flang)<br>\[[slides](slides/A.walk.through.Flang.OpenMP.lowering.From.FIR.to.LLVMIR.pdf)\] | Tutorial, Flang, OpenMP |
| 20:30 - 20:45 (15 min) | [Jose M Monsalve Diaz](https://www.linkedin.com/in/josemonsalve2/)<br>[Johannes Doerfert](https://www.google.com/url?q=https://www.linkedin.com/in/johannes-doerfert-3a0770a2/&sa=D&source=editors&ust=1647549339251666&usg=AOvVaw2O1D9myHz5uLu0_NLPCVO0)<br>[Aditya Kumar](https://www.google.com/url?q=https://hiraditya.github.io/&sa=D&source=editors&ust=1647549339251913&usg=AOvVaw0Jon2xtUE-YxYLqfoxI9YR) | Closing remarks | Getting feedback |

# Abstracts

### Opaque Pointers Are Coming  
[▲ back to schedule](#workshop-schedule)

TLLVM is currently finalizing the migration from typed pointers (i32\*) to opaque pointers (ptr) -- the likely largest intermediate representation change in LLVM's history. In this talk, we'll discuss the motivations for the change, how it will affect developers working on/with LLVM in practice, and why this migration took such a long time. We'll also briefly cover possible future IR changes based on opaque pointers.

### The Hot Path SSA Form in LLVM  
[▲ back to schedule](#workshop-schedule)

The Static Single Assignment (SSA) form is the most popular representation used in the LLVM compiler system. The SSA form has been affable to the design of simpler algorithms for existing optimizations and has facilitated the development of new ones. However, speculative optimizations—optimizations targeted towards speeding up the “common cases” of a program—have not been fortunate enough to savor an SSA-like intermediate form.

We build the Hot Path SSA (HPSSA) Form within the LLVM infrastructure to facilitate the design of speculative analyses and optimizations by allowing only hot reaching definitions (definitions along frequent acyclic paths in the program profile) to reach their respective uses. We also demonstrate how the HPSSA form can be effective in easily building speculative variants of existing "standard" analyses by building a SpecSCCP pass —a speculative variant of Wegman and Zadeck’s Sparse Conditional Constant Propagation algorithm.

### POSET-RL: Phase ordering for Optimizing Size and Execution Time using Reinforcement Learning  
[▲ back to schedule](#workshop-schedule)

The ever increasing memory requirements of several applications has led to increased demands which might not be met by embedded devices. Constraining the usage of memory in such cases is of paramount importance. It is important that such code size improvements should not have a negative impact on the runtime. Improving the execution time while optimizing for code size is a non-trivial but a significant task.

The ordering of standard optimization sequences in modern compilers is fixed, and are heuristically created by the compiler domain experts based on their expertise. However, this ordering is sub-optimal, and does not generalize well across all the cases.

We present a reinforcement learning based solution to the phase ordering problem, where the ordering improves both the execution time and code size. We propose two different approaches to model the sequences: one by manual ordering, and other derived from Oz sequences by creating a graph called Oz Dependence Graph (ODG). Our approach uses minimal data as training set, and is integrated with LLVM.

We show results on X86 and AArch64 architectures using the benchmarks from SPEC-CPU 2006, SPEC-CPU 2017 and MiBench. We observe that the proposed model based on ODG outperforms the Oz sequence both in terms of size and execution time by 6.19% and 11.99% in SPEC 2017 benchmarks, on an average.

### Learning to combine Instructions in LLVM Compiler  
[▲ back to schedule](#workshop-schedule)

Instruction combiner (IC) is a critical compiler optimization pass, which replaces a sequence of instructions with an equivalent and optimized instruction sequence at basic block level. There can be thousands of instruction-combining patterns which need to be frequently updated as new coding idioms/applications and novel hardware evolve over time. This results in frequent updates to the IC optimization pass thereby incurring considerable human effort and high software maintenance costs. To mitigate these challenges associated with the traditional IC, we design and implement a Neural Instruction Combiner (NIC) and demonstrate its feasibility by integrating it into the standard LLVM compiler optimization pipeline.

NIC leverages neural sequence-to-sequence (Seq2Seq) models for generating optimized encoded IR sequence from the unoptimized encoded IR sequence. To the best of our knowledge, ours is the first work demonstrating the feasibility of a neural instruction combiner built into a full-fledged compiler pipeline. Given the novelty of this task, we built a new dataset for training our NIC neural model. We show that NIC achieves exact match results percentage of 72\\% for optimized sequences as compared to traditional IC and neural machine translation metric Bleu precision score of 0.94, demonstrating its feasibility in a production compiler pipeline.

### \[Tutorial\] An Guide to Performance Debugging LLVM-based Programs  
[▲ back to schedule](#workshop-schedule)

LLVM is a compiler infrastructure that has become the foundation of a variety of compilers and languages including C/C++, Fortran, Rust, Swift, Julia, and more. When a user of an LLVM-based compiler is writing a program, it is unfortunately and surprisingly easy to shoot one self in the foot and inadvertently write code that prevents optimization.

This talk will provide viewers with an introduction to performance debugging in LLVM, covering a variety of common tools and techniques such as profilers and optimization remarks. This talk will also provide users with the the necessary tools to solve advanced performance engineering mysteries including LLVM optimizations inadvertently not applying to programs. The talk will conclude by discussing two recent performance engineering mysteries that arose on LLVM main: a change to phase ordering that accidentally resulted in LICM needless removing alias and range information (https://github.com/llvm/llvm-project/issues/53794), and the increasing importance and ubiquity of hardcoded compiler flags.

### Compiling, running and benchmarking SNAP with LLVM Flang - experiences with a new compiler  
[▲ back to schedule](#workshop-schedule)

LLVM Flang is a new Fortran frontend and a compiler driver in LLVM, using MLIR as an intermediate step before generating LLVM-IR. SNAP is a physics application of medium size, written in Fortran 95 and using OpenMP and MPI for parallelism. This talk will discuss the trials and tribulations of compiling some thousands of lines of Fortran source code (SNAP) with a new compiler (LLVM Flang).

LLVM Flang is still work-in-progress. This is the first time that a large Fortran application is compiled with LLVM Flang in a way that allows to benchmark it against other Fortran compilers. I will discuss my approach for measuring the performance and compare the results with GFortran and the Classic Flang. This initial study has revealed a number of areas for improvement to LLVM Flang code generation that would show better performance on SNAP, and beyond!

### An Anatomy of Optimized Matrix Multiplication on AArch64  
[▲ back to schedule](#workshop-schedule)

This proposal presents our work in optimizing double-precision floating-point General Matrix Multiply (GEMM), which computes a matrix fma (fused multiply add) between three source matrices C+=A\*B. For double precision GEMM, we were able to achieve 9.7 GFLOPs, which is close to the theoretical maximum of 10.4 GFLOPs under the conditions of our testing machine. In addition, we also achieved a cache miss rate of only 0.2%. This GEMM IR will be shipped together with Huawei's BiSheng compiler, a compiler based on the open source LLVM project. The presentation will focus on how to best use the techniques for high-performance GEMM.

There are many well-established optimization techniques for GEMM, but their effectiveness doesn't scale well over a wide range of matrix sizes. To obtain an optimized MM for a general size, from the small to the large, the challenge is to choose the appropriate techniques for different matrix sizes, and how to best combine the techniques and sizes together. For example, on AArch64, a 4-by-4 MM micro-kernel is small enough to be fitted into the available NEON vector registers for vectorization, but as the matrix size increases, register pressure starts to appear, and vectorization loses effectiveness as reloads of the source matrix elements into the vector registers become necessary. As another example of a technique whose effectiveness degrades with size, the technique of outer product expansion in MM inherently supports loop invariant code motion and gives very good performance for 128-by-128 MM, but as the matrix size increases into the thousands and cache locality decreases, the performance gain from outer products quickly degrades, and tiling and packing are needed to improve caching.

We will demonstrate how to best choose the matrix sizes for the micro- and macro-kernels based on the platform. We present optimized GEMM on AArch64 for the small, medium and large sizes: a 4-by-4 MM micro-kernel hand-vectorized with the NEON vector infrastructure, a 128-by-128 macro-kernel optimized with outer product expansion, and the thousand-sized GEMM optimized with tiling and packing. Alongside a tutorial of these techniques themselves, we will demonstrate how to best use the MM kernel of a smaller size in the MM of a larger size, and provide a deeper understanding of why each technique is most effective on its corresponding matrix size.

### Improving the OpenMP Offloading Driver: LTO, libraries, and toolchains  
[▲ back to schedule](#workshop-schedule)

This technical talk will describe the work done to improve the clang driver for generating OpenMP offloading applications. The talk will detail the motivations behind this change, the implementation and function of the new driver, and the features and performance this new approach provides. Features such as device link time optimization, static libraries, and tool-chain unification greatly improve both the performance and usability of LLVM's OpenMP offloading support. I will mention the performance improvements found for some applications that make heavy use of split compilation, something that is notoriously slow for regular CUDA codes.

### Crash-Analyzer: An LLVM-based Tool for Triaging and Analyzing Crashes  
[▲ back to schedule](#workshop-schedule)

Crash-Analyzer is an LLVM-based tool that bridges the gap between triaging and fixing a bug. We introduce compiler technology and analyses to discover and reason about semantics of crashing program. The Crash-Analyzer consists of Corefile Reader, Decompiler, and Analyzer. It takes a corefile and the corresponding executable binary and attempts to identify the function that is responsible for the crash. Crash-Analyzer also outputs a backward taint data flow graph which can be helpful for developers.

### Prototyping a compiler for homomorphic encryption using MLIR  
[▲ back to schedule](#workshop-schedule)

Homomorphic encryption is an encryption scheme in cryptography that provides a set of operations on encrypted data. Among homomorphic encryption schemes, CKKS provides efficient but approximate operations on real numbers. CKKS encrypts a plaintext as a pair of large integer polynomials, and its homomorphic operations are defined as a series of polynomial operations on them. Thus, the implementations of CKKS operations typically contain many loops on large arrays representing polynomials. Successfully applying loop optimizations can significantly boost the performance of the operations.

In this talk, we introduce a prototype of a compiler for homomorphic encryption using MLIR.

It takes a program that describes polynomial operations and compiles it into LLVM IR.

Our prototype can compile decryption/encryption, and the generated code is at most 40% faster when run in 32 threads than the C++ implementation written using Intel HEXL.

### A walk through Flang OpenMP lowering: From FIR to LLVMIR  
[▲ back to schedule](#workshop-schedule)

In this talk, we show the details of the lowering process from Source Fortran code to LLVMIR, through the Fortran Dialect of MLIR e.g FIR. We walk the listeners through an example OpenMP construct (SIMD) and showcase how to design the lowering pipeline. This talk will immensely be helpful to future contributors to the LLVM-Flang OpenMP project.

# Call for Speakers

We invite speakers from academia and industry to present their work on the following list of topics (including and not limited to:)

*   Compilation and interpretation techniques benefitting from LLVM,
*   Performance optimizations, code-size optimizations and binary instrumentation techniques using LLVM,
*   Improvements to runtime libraries developed under llvm-infrastructure e.g., libc++, libc++-abi, OpenMP, etc.
*   Improving the security of generated code using compilation techniques,
*   Any tools developed with LLVM (or subprojects) for performance analysis,
*   compiler flags, annotations and remarks to understand and improve performance,
*   any other topic related to improving and maintaining the performance and quality of LLVM generated code.

While the primary focus of the workshop is on these topics, we welcome any submission related to the LLVM-project, its sub-projects (clang, mlir, lldb, Polly, lld, openmp, pstl, compiler-rt, etc.), as well as their use in industry and academia.

We are looking for:

*   keynote speakers(30-60minutes),
*   technical presentations: 30 minutes plus questions and discussion,
*   tutorials(30-60minutes),
*   panels(30-60minutes),
*   BOFs(30-60minutes)

Proposals should provide sufficient information for the review committee to be able to judge the quality of the submission. Proposals can be submitted under the form of an extended abstract, full paper, or slides. Accepted presentations will be presented online. The presentations will be publicly available on https://llvm.org/devmtg/, and recordings will be available on [LLVM's youtube channel](https://www.youtube.com/channel/UCv2_41bSAa5Y_8BacJUZfjQ)

In case of any queries please reach out to the workshop organizers: Johannes Doerfert (jdoerfert at anl.gov), Aditya Kumar (adityak at snap.com), Jose M Monsalve Diaz (jmonsalvediaz@anl.gov), Shilei Tian (i@tianshilei.me), Vaibhav Kurhe (vaibhav.kurhe@gmail.com)

#### What types of people attend?

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

Tutorials are 30-60 minute sessions that dive down deep into a technical topic. Expect in depth examples and explanations. <!-- *********************************************************************** -->

* * *
