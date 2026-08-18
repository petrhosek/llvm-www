---
layout: "default.html"
permalink: "devmtg/2024-03/index.html"
---
# Eighth LLVM Performance Workshop at CGO

*   **What:** Eighth LLVM Performance Workshop at CGO
*   **When:** March 2nd, 2024 (Saturday)
*   **Where:** [Venue The Exchange, 150 Morrison St, EH3 8EE, Edinburgh, United Kingdom)](https://conf.researchr.org/venue/cgo-2024/cgo-2024-venue) \[In person\]
*   **Proposals should be submitted to:** [Easychair Submission](&lt;https://easychair.org/conferences/?conf=llvmcgo2024
            &gt;)
*   **The deadline for receiving submissions is:** : January 25th, 2024
*   **Speakers will be notified of acceptance or rejection by:** February 1st, 2024
*   Note: Travel grants are available to eligible candidates upon request. Please reach out to the program committee if you need travel grant for the workshop.
*   Note: Invitation letters for visa application are available upon request. Please reach out to the program committee if you need invitation letter for visa application.

The Eighth LLVM Performance Workshop will be held at ([CGO 2024](https://conf.researchr.org/track/cgo-2024/cgo-2024-workshops-and-tutorials)). The workshop is co-located with CC, HPCA, and PPoPP. If you are interested in attending the workshop, please register at the ([CGO website](https://conf.researchr.org/home/cgo-2024)). The LLVM workshop at CGO will be in-person.

Program Committee:

*   Johannes Doerfert (jdoerfert at llnl.gov)
*   Aditya (hiraditya at msn.com)
*   Jose M Monsalve Diaz (jmonsalvediaz at anl.gov)
*   Shilei Tian (i at tianshilei.me)
*   Rafael A Herrera Guaitero (rafaelhg at udel.edu)

# Schedule \[WIP\]

<!-- Opening remarks --> <!-- Talk 0 --> <!-- Talk 1 --> <!-- Talk 2 --> <!-- Talk 3 --> <!-- Break --> <!-- Talk 4 --> <!-- Talk 5 --> <!-- Talk 6 --> <!-- Talk 7 --> <!-- Lunch Break --> <!-- Keynote --> <!-- Talk 8 --> <!-- Open Discussion --> <!-- Closing remarks -->

| Time (EDT) | Speaker | Title | Topic |
| --- | --- | --- | --- |
| 8:30 - 8:35 (5 min) | [Jose M Monsalve Diaz](https://www.linkedin.com/in/josemonsalve2/)<br>[Shilei Tian](https://www.linkedin.com/in/shiltian/)<br>[Johannes Doerfert](https://www.linkedin.com/in/johannes-doerfert-3a0770a2)<br>[Aditya](https://twitter.com/_hiraditya_)<br>[Rafael A Herrera Guaitero](https://www.linkedin.com/in/randres-herrera/) | Opening Remarks | Welcome and Introduction |
| 8:35 - 9:00 (25 min) | Guray Ozen | [Targeting NVIDIA Hopper using MLIR](#talk0)<br>\[[slides](slides/nvidia-hopper-in-mlir.pdf)\] | Code generation<br>MLIR<br>GPU |
| 9:00 - 9:30 (30 min) | Shivam Kunwar | [Map LLVM Values to corresponding source-level expression](#talk1) <!-- <br/><span style="font-family: monospace;">[<a href="slides/RL4ReAl.pdf">slides</a>]</span> --> | LLVM<br>C++<br>Loop Vectorization<br>Debug Info |
| 9:30 - 10:00 (30 min) | Tomaz Canabrava | [Using LLVM to inspect, and fix, the Physical Structure of a Large Scale Software - The Codevis Project](#talk2) <!-- <br/><span style="font-family: monospace;">[<a href="slides/RL4ReAl.pdf">slides</a>]</span> --> | Software Visualization<br>Large Scale<br>LLVM<br>Clang<br>Flang |
| 10:00 - 10:30 (30 min) | Amir Ayupov | [Practical Use of BOLT](#talk3)<br>\[[slides](slides/practical-use-of-bolt.pdf)\] | LLVM<br>BOLT<br>PGO<br>Profile-guided optimizations<br>Profiling |
| 10:30 - 10:50 (20 min) | \- | Coffee break | \- |
| 10:50 - 11:20 (30 min) | Venkatakeerthy S,<br>Siddharth Jain,<br>Umesh Kalvakuntla,<br>Pranav Sai Gorantla,<br>Rajiv Shailesh Chitale,<br>Eugene Brevdo,<br>Albert Cohen,<br>Mircea Trofin,<br>Ramakrishna Upadrasta | [The Next 700 ML-Enabled Compiler Optimizations](#talk4)<br>\[[slides](slides/ML-Compiler-Bridge.pdf)\] | ML driven Compiler Optimizations<br>Infrastructure<br>Library<br>LLVM<br>MLIR<br>Pluto |
| 11:20 - 11:50 (30 min) | Rafael Andres Herrera Guaitero,<br>Rodrigo Ceccato de Freitas,<br>Rémy Neveu,<br>Jose Manuel Monsalve Diaz | [Unveiling the Power of Heterogeneous Computing: A Brief Dive into Host and Target Tasks with OpenMP LLVM](#talk5)<br>\[[slides](slides/power-of-heterogeneous-computing.pdf)\] | Heterogeneous Computing<br>Device Offloading<br>OpenMP<br>LLVM<br>Accelerators |
| 11:50 - 12:20 (30 min) | Tobias Schwarz,<br>Alexis Engelke | [Building a Fast Back-end for LLVM-IR](#talk6)<br>\[[slides](slides/llvm-fast-backend.pdf)\] | LLVM<br>Back-end<br>Fast compilation |
| 12:20 - 12:50 (30 min) | George Stelle,<br>Tarun Prabhu,<br>Pat McCormick | [Dominance is not a Tree: Towards More Precise Dominance Relations](#talk7)<br>\[[slides](slides/dominance-is-not-a-tree.pdf)\] | Dominance<br>Single Static Assignment<br>Concurrency<br>Optimizations |
| 12:50 - 13:40 (50 min) | \- | Lunch break | \- |
| 13:40 - 14:30 (50 min) | Saman Amarasinghe | [Keynote: "Arrays 2.0: Extending the Scope of the Array Abstraction"](#keynote)<br>\[[slides](slides/Arrays-2.0-LLVM-CGO-2024-Keynote.pdf)\] | Arrays<br>Loops<br>Structured Data<br>Finch, TACO |
| 14:30 - 15:00 (30 min) | Ivan Ivanov,<br>Jens Domke,<br>Toshio Endo,<br>Johannes Doerfert | [Automatic Parallelization and OpenMP Offloading of Fortran](#talk8) <!-- <br/><span style="font-family: monospace;">[<a href="slides/RL4ReAl.pdf">slides</a>]</span> --> | Fortran<br>OpenMP<br>Offloading |
| 15:00 - 15:30 (30 min) | \- | Open Discussion | \- |
| 15:30 - 15:40 (10 min) | [Jose M Monsalve Diaz](https://www.linkedin.com/in/josemonsalve2/)<br>[Shilei Tian](https://www.linkedin.com/in/shiltian/)<br>[Johannes Doerfert](https://www.linkedin.com/in/johannes-doerfert-3a0770a2)<br>[Aditya Kumar](https://twitter.com/_hiraditya_)<br>[Rafael A Herrera Guaitero](https://www.linkedin.com/in/randres-herrera/) | Closing Remarks | Getting feedback |

# Abstracts

### Targeting NVIDIA Hopper using MLIR  
[▲ back to schedule](#workshop-schedule)

#### Guray Ozen1

##### 1Google Research

This talk explores how to make the most of the NVIDIA Hopper Tensor Core by using its new hardware features effectively. Even with these advanced features, the challenge lies in efficiently using them, especially when creating fast General Matrix Multiply (GEMM) kernels. The ongoing research focuses on integrating the features of the NVIDIA Hopper Architecture GPU into the MLIR compiler. The main goal is to turn MLIR into a strong compiler that can unlock the best performance from GPUs. The talk discusses how to implement important elements, such as the Tensor Memory Accelerator (TMA), warp-group level tensor core instructions, and transactional barriers. Several features have been implemented to GPU, NVGPU, and NVVM dialects. The GPU dialect is where we launch the kernel, NVVM dialect is where we generate PTX assembly, and NVGPU dialect is where we can create efficient kernels at a higher level. The talk covers a detailed discussion of these dialects and how they contribute to optimizing the performance of the NVIDIA Hopper Architecture.

### Map LLVM Values to corresponding source level expression  
[▲ back to schedule](#workshop-schedule)

#### Shivam Kunwar

<!-- <h5><sup>1</sup>Pacific Northwest National Laboratory</h5> -->

The primary objective of this project is to enhance the effectiveness of compiler-generated remarks and analysis reports for code optimization. These messages, while often comprehensive, lack direct connections to the corresponding source-level expressions. The goal is to bridge this gap by utilizing LLVM's intrinsic functions, which establish mappings between LLVM program entities and source-level expressions. The project specifically focuses on utilizing these intrinsic functions to generate or derive source expressions from LLVM values. This functionality is particularly important for enhancing memory access optimizations, including the reporting of memory access dependences that hinder vectorization.

### Using LLVM to inspect, and fix, the Physical Structure of a Large Scale Software - The Codevis Project  
[▲ back to schedule](#workshop-schedule)

#### Joachim Meyer1, 2

##### 1KDE, 2Codethink

Codevis is an open source tool that enables the user to study, analyse, and fix large scale software architecture flaws. The software currently understands C, c++ and Fortran. Codevis' main use case is to display relationship graphs between libraries, structures (such as classes or pure "c" structures), functions (including traits, functions or methods), and files. Codevis offers several tools that help find problems on large scale designs, such as a \`Knowledge Island\` (a visualisation that showcases who originates the source code per file, module, class) to \`Find Cycles\`. We know old software usually grows organically, and without the knowledge we have today, cycles probably exist that make this an even more tangled ball of yarn. Codevis aims to help corporations visualise all their software architecture in one single tool. This ensures faster action can be taken during development, or faster action can be taken during architecture decision-making. LLVM is a core part of this project for the C++ and Fortran parser. It has been proven to work. It fixes architectural issues within the KDE Frameworks Libraries - a collection of 80+ libraries combinning millions of lines of code.

### Practical Use of BOLT  
[▲ back to schedule](#workshop-schedule)

#### Amir Ayupov1

##### 1Meta

BOLT is a binary optimizer for ELF binaries and is a part of LLVM project. Utilizing sample-based profiling, BOLT boosts the performance even for highly optimized binaries built with both profile-guided optimizations (PGO) and link-time optimizations (LTO). BOLT has been demonstrated to be effective for a number of workloads spanning from HHVM to Clang, Python, Rust, MySQL, and Chromium, and has features enabling its use in various environments. This talk focuses on practical aspects of BOLT application through profile collection, use of BOLT optimizations and flags for specific use cases, interaction with compiler PGO, and usage in continuous profiling scenarios.

### The Next 700 ML-Enabled Compiler Optimizations  
[▲ back to schedule](#workshop-schedule)

#### Venkatakeerthy S1, Siddharth Jain1, Umesh Kalvakuntla1, Pranav Sai Gorantla1, Rajiv Shailesh Chitale1, Eugene Brevdo2, Albert Cohen2, Mircea Trofin2 and Ramakrishna Upadrasta1

##### 1IIT Hyderabad, 2Google DeepMind

There is a growing interest in enhancing compiler optimizations with ML models, yet interactions between compilers and ML frameworks remain challenging. Some optimizations require tightly coupled models and compiler internals, raising issues with modularity, performance and framework independence. Practical deployment and transparency for the end-user are also important concerns. We propose MLCompiler-Bridge to enable ML model development within a traditional Python framework while making end-to-end integration with an optimizing compiler possible and efficient. We evaluate it on both research and production use cases, for training and inference, over several optimization problems, multiple compilers and its versions, and gym infrastructures.

### Unveiling the Power of Heterogeneous Computing: A Brief Dive into Host and Target Tasks with OpenMP LLVM  
[▲ back to schedule](#workshop-schedule)

#### Rafael Andres Herrera Guaitero1, Rodrigo Ceccato de Freitas2, Rémy Neveu3 and Jose Manuel Monsalve Diaz3

##### 1University of Delaware, 2UNICAMP, 3Argonne National Lab

This session offers a concise overview of achieving heterogeneous computing through OpenMP. This presentation aims to explain the current state of the implementation and provide guidance to other developers, especially those who are new, on how to get started and contribute to LLVM's OpenMP host and target task support. We look at the role of the runtime system interface and its implementation, providing insights into the essential components that drive heterogeneous computing. We also discuss the current RFC of the offloading runtime project and the plans to use it universally. To help a practical understanding, we finish the session with a simple example that shows how to compile and execute heterogeneous code using the LLVM framework.

### Building a Fast Back-end for LLVM-IR  
[▲ back to schedule](#workshop-schedule)

#### Tobias Schwarz1 and Alexis Engelke1

##### 1Technical University of Munich

Low compilation times of unoptimized builds are important for developer productivity and especially for fast start-up just-in-time compilation. LLVM's back-end is an often-cited problem for these use cases, with a substantial portion of the compile-time being spent for rewriting the program code multiple times. We develop a completely new LLVM back-end for a commonly used subset of LLVM-IR (e.g., typical output of Clang) targeting x86-64 without using the existing back-end infrastructure. Instead, we generate machine code with just two passes over the input IR without any further IR. This way, on the SPECint 2017 benchmarks, we achieve a ~10x compile-time speed-up over the LLVM -O0 back-end with a run-time slowdown in the range of 0-30%. Instead of building a custom IR, we start from LLVM-IR as this allows adopting our compiler as fast baseline without code changes while still providing an easy path to optimized compilation. In this talk, we describe our approach and related challenges and experiences when building an entirely new, performance-focused LLVM back-end from scratch.

### Dominance is not a Tree: Towards More Precise Dominance Relations  
[▲ back to schedule](#workshop-schedule)

#### George Stelle1, Tarun Prabhu1, Pat McCormick1

##### 1Los Alamos National Laboratory

In LLVM and other modern compilers, single static assignment (SSA) is a crucial theory for internal representations, enabling optimizations in the presence of imperative code. A fundamental function of SSA is calculating and using dominance relations to determine where immutable variables can be referenced. Dominator trees have historically been a good approximation of the dominator relation and efficiently computable. However, there are programs for which the dominator tree fails to capture precise dominance relations, preventing optimizations. In this work, we give examples of these kinds of programs, and show how removing the restriction to tree relations enables more precise dominance relations, therefore enabling more optimization. We discuss how one can use properties of SSA to implement a more general dominance relation using a small set of trees corresponding to shared branches, which we call a dominator grove. We present a work-in-progress implementation of a dominator grove in LLVM, along with some of the current hurdles in modifying the existing analyses and transformations to be sound in the presence of non-tree dominance relations. Using the implementation, we collect empirical data on the frequency of non-tree dominance relations in real code. We present some basic formal properties of the approach, and end with a discussion of future work, including concurrent extensions to SSA theory.

### Arrays 2.0: Extending the Scope of the Array Abstraction  
[▲ back to schedule](#workshop-schedule)

#### Saman Amarasinghe1

##### 1 Massachusetts Institute of Technology

FORTRAN, the first programming language introduced over a half a century ago, ushered in multi-dimensional arrays to store data and FOR loops to iterate over them. Since then, the programming world has evolved to introduce a plethora of data structures ranging from lists and sets to trees and graphs. Yet, when it comes to handling immense data sets, arrays and loops remain a practical mainstay. Every imperative programming language has implemented arrays and loops and most programmers learn to use them early on. Many important features in modern hardware from caches to prefetchers were created to efficiently execute array accesses by loops. Even in LLVM, many optimizations including loop invariant code motion, vectorization and polyhedral optimizations were dedicated to optimizing loopy codes with array accesses.  
The scope of the array data structure, a multi-dimensional, dense, integer grid of points in a rectilinear space, first introduced in FOTRAN, haven't expanded beyond this definition. However, a significant portion of real-world data, either originating from sensors, computational processes, or human input, embodies innate structures such as sparsity, repeated value sequences, symmetry and continuous real-valued indices. These characteristics are evident in diverse fields like scientific computing, data analytics, graph processing, and machine learning.  
In this talk, I will attempt to expand the familiar arrays and loops abstraction beyond the original scope of FORTRAN with the TACO and Finch compilers. TACO pioneered auto-generating of kernels for any sparse tensor algebra operation across prevalent formats. Finch, on the other hand, has seamlessly integrated the management of structured data, capturing nuances like sparsity, repeated values, symmetry and arrays where indices are real values.  
I will demonstrate how to compile complex loopy programs with structured data into efficient loops in a systematic way and how our compiler's output rivals the performance of best-of-class handcrafted codes. I hope to convince you that we can finally put structured array programming on the same compiler transformation and code generation footing as dense array codes.  

Saman Amarasinghe is a Professor in the Department of Electrical Engineering and Computer Science at Massachusetts Institute of Technology and a member of its Computer Science and Artificial Intelligence Laboratory (CSAIL) where he leads the Commit compiler group. Under Saman's guidance, the Commit group has developed a myriad of pioneering programming languages and compilers including the StreamIt, StreamJIT, PetaBricks, Halide, Simit, MILK, Cimple, TACO, GraphIt, BioStream, CoLa and Seq programming languages and compilers, DynamoRIO, Helium, Tiramisu, Codon and BuildIt compiler/runtime frameworks, Superword Level Parallelism (SLP), goSLP and VeGen for vectorization, Ithemal machine learning based performance predictor, Program Shepherding to protect programs against external attacks, the OpenTuner extendable autotuner, and the Kendo deterministic execution system. He was the co-leader of the Raw architecture project. Beyond academia, Saman was a co-founder of Determina, Lanka Internet Services Ltd., Venti Technologies, DataCebo and Exaloop corporations. Saman received his BS in Electrical Engineering and Computer Science from Cornell University in 1988, and his MSEE and Ph.D. from Stanford University in 1990 and 1997, respectively. He is an ACM Fellow.

### Automatic Parallelization and OpenMP Offloading of Fortran  
[▲ back to schedule](#workshop-schedule)

#### Iva Ivanov1, 2, Jens Domke3, Toshio Endo1, Johannes Doerfert2

##### 1Tokyo Institute of Technology, 2Lawrence Livermore National Laboratory, 3RIKEN Center for Computational Science (R-CCS)

The most substantial compute power found in most modern HPC systems is in their accelerators, namely GPUs. Thus, it is extremely important to utilize them in order to maximize performance of scientific computing applications. Fortran is still prevalent in the scientific community and there are vast amounts of important existing applications written in it, however, legacy Fortran code was not written with accelerators in mind, so enabling scientists to easily make use of modern hardware with minimal effort is an important goal. OpenMP has been widely used as a way to accelerate these programs, and the 6.0 version of the standard which is scheduled to be released in late 2024 introduces a new directive with this goal in mind, called coexecute. It allows the programmer to instruct the compiler to automatically parallelize and offload a sequence of array operations and calls to intrinsic functions. This requires extensive compiler transformations such as splitting device kernels and parallelization of loops, which we implement in LLVM's MLIR based compiler, Flang. We show how automatic parallelization and offloading of existing fortran code to accelerators is possible with just simple annotations from the programmer.

# Call for Speakers

We invite speakers from academia and industry to present their work on the following list of topics (including and not limited to:)

*   Improving performance and code-size of applications built by LLVM toolchains
*   Improving performance of LLVM's runtime libraries
*   Improving the security of generated code
*   Any tools or products developed by using one of the libraries in LLVM infrastructure
*   Performance tracking over time
*   Compiler flags, annotations and remarks to understand and improve performance
*   Any other topic related to improving and maintaining the performance and quality of LLVM generated code

While the primary focus of the workshop is on these topics, we welcome any submission related to the LLVM-project, its sub-projects (clang, mlir, lldb, Polly, lld, openmp, pstl, compiler-rt, etc.), as well as their use in industry and academia.

We are looking for:

*   keynote speakers (30-60minutes),
*   technical presentations (30 minutes plus questions and discussion),
*   tutorials (30-60minutes),
*   panels (30-60minutes),
*   BOFs (30-60minutes)

Proposals should provide sufficient information for the review committee to be able to judge the quality of the submission. Proposals can be submitted under the form of an extended abstract, full paper, or slides. Accepted presentations will be presented online. The presentations will be publicly available on [https://llvm.org/devmtg/](https://llvm.org/devmtg/)

In case of any queries please reach out to the workshop organizers: Johannes Doerfert (jdoerfert at llnl.gov), Aditya (hiraditya at msn.com), Jose M Monsalve Diaz (jmonsalvediaz at anl.gov), Shilei Tian (i at tianshilei.me), or Rafael (rafaelhg at udel.edu).

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

Tutorials are 30-60 minute sessions that dive down deep into a technical topic. Expect in depth examples and explanations.

# Code of Conduct

The LLVM Foundation is dedicated to providing an inclusive and safe experience for everyone. We do not tolerate harassment of participants in any form. By registering for this event, we expect you to have read and agree to the [LLVM Code of Conduct](http://llvm.org/docs/CodeOfConduct.html).

We also adhere to the [Code of Conduct use by CGO](https://conf.researchr.org/attending/cgo-2024/code-of-conduct)

<!-- *********************************************************************** -->

* * *
