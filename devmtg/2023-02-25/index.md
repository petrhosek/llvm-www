---
layout: "default.html"
permalink: "devmtg/2023-02-25/index.html"
---
# Seventh LLVM Performance Workshop at CGO

*   **What:** Seventh LLVM Performance Workshop at CGO
*   **When:** February 25th (Saturday), 2023
*   **Where:** [Hotel Bonaventure, Montreal, Canada](https://conf.researchr.org/venue/cgo-2023/cgo-2023-venue) \[In person\]
*   **Proposals should be submitted to:** [Easychair Submission Link](https://easychair.org/conferences/?conf=llvmcgo2023)
*   **The deadline for receiving submissions is:** February 1st, 2023.
*   **Speakers will be notified of acceptance or rejection by:** February 3rd, 2023
*   Note: Travel grants are available upon request. Please reach out to the program committee if you need travel grant for the workshop.

The Seventh LLVM Performance Workshop will be held at ([CGO 2023](https://conf.researchr.org/track/cgo-2023/cgo-2023-workshops-and-tutorials)). The workshop is co-located with CC, HPCA, and PPoPP. If you are interested in attending the workshop, please register at the ([CGO website](https://conf.researchr.org/home/cgo-2023)). The organizing committee of CGO/PPoPP/HPCA/CC has decided to make the conference in-person this year. The LLVM workshop at CGO will be in-person.

Program Committee:

*   Johannes Doerfert (jdoerfert at llnl.gov)
*   Aditya (hiraditya at msn.com)
*   Jose M Monsalve Diaz (jmonsalvediaz at anl.gov)
*   Shilei Tian (i at tianshilei.me)

# Schedule \[WIP\]

<!-- <tr> <td> <p>8:10 - 8:50 (40 min)</p> </td> <td> <p>Keynote</a></p> </td> <td> <p>TBD</p> </td> <td> Keynote </td> </tr> -->

| Time (EDT) | Speaker | Title | Topic |
| --- | --- | --- | --- |
| 8:00 - 8:10 (10 min) | [Jose M Monsalve Diaz](https://www.linkedin.com/in/josemonsalve2/)<br>[Shilei Tian](https://www.linkedin.com/in/shiltian/)<br>[Johannes Doerfert](https://www.linkedin.com/in/johannes-doerfert-3a0770a2)<br>[Aditya](https://twitter.com/_hiraditya_) | Opening Remarks | Welcome and Introduction |
| 8:10 - 8:50 (40 min) | S. Venkatakeerthy<br>Siddharth Jain<br>Anilava Kundu<br>Rohit Aggarwal<br>Albert Cohen<br>Ramakrishna Upadrasta | [RL4ReAl: Reinforcement Learning for Register Allocation](#rl4real)<br>\[[slides](slides/RL4ReAl.pdf)\] | Machine Learning |
| 8:50 - 9:30 (40 min) | Rizwan A. Ashraf<br>Zhen Peng<br>Luanzheng Guo<br>Gokcen Kestor | [Automatic Code Generation for High-performance Graph Algorithms](#auto-code-gen-for-graph)<br>\[[slides](slides/codegen-graph-algo.pdf)\] | Codegen |
| 9:30 - 10:00 (30 min) | \- | Coffee Break | \- |
| 10:00 - 10:40 (40 min) | Marco Gelmi<br>Danila Kutenin<br>Daniel Mankowitz<br>Andrea Michi<br>Marco Selvi<br>Nilay Vaish<br>MinJae Hwang | [A New Implementation for std::sort](#std-sort)<br>\[[slides](slides/A-New-Implementation-for-std-sort.pdf)\] | Algorithms |
| 10:40 - 11:20 (40 min) | Gunnar Kudrjavets<br>Aditya Kumar | [Optimizing the Compiler's Memory Usage? Let Us Implement a BasicProfiler First!](#optimize-compiler-memory-usage)<br>\[[slides](slides/basic-memory-profiler.pdf)\] |  |
| 11:20 - 12:00 (40 min) | Joachim Meyer<br>Aksel Alpay<br>Sebastian Hack<br>Holger Fröning<br>Vincent Heuveline | [Solid Work-Group Synchronization on CPUs](#work-group-sync-cpu)<br>\[[slides](slides/work-group-sync-on-cpu-LLVM.pdf)\] | Heterogeneous Computing |
| 12:00 - 12:10 (10 min) | [Jose M Monsalve Diaz](https://www.linkedin.com/in/josemonsalve2/)<br>[Shilei Tian](https://www.linkedin.com/in/shiltian/)<br>[Johannes Doerfert](https://www.linkedin.com/in/johannes-doerfert-3a0770a2)<br>[Aditya](https://twitter.com/_hiraditya_) | Closing Remarks | Getting feedback |

# Abstracts

### Automatic Code Generation for High-Performance Graph Algorithms  
[▲ back to schedule](#workshop-schedule)

#### Rizwan A. Ashraf1, Zhen Peng1, Luanzheng Guo1, Gokcen Kestor1

##### 1Pacific Northwest National Laboratory

Graph algorithms have broad applicability in many domains, such as scientific computing, social sciences, and many more. A well-performing implementation of these algorithms on computing systems however requires significant programmer effort, and portability across various heterogeneous computing devices does not come for free. In this paper, we describe the support of optimizations in the MLIR-based COMET compiler of graph algorithms for portable and faster implementation as compared to a library-based approach. We discuss the needed extensions to our compiler front-end, intermediate representation, and the workspace and masking optimizations. Our experimental results demonstrate speedup of up to 3.7X for the sparse matrix - sparse matrix operation over various semirings, as compared to a library-based implementation of the GraphBLAS standard.

### A New Implementation for `std::sort`  
[▲ back to schedule](#workshop-schedule)

#### Marco Gelmi1, MinJae Hwang2, Danila Kutenin1, Daniel J. Mankowitz1, Andrea Michi1, Marco Selvi2, Nilay Vaish2

##### 1DeepMind, 2Google LLC

`std::sort` is one of the most used algorithms from the C++ Standard Library. In this writeup, we talk about our recent changes to the `libc++` implementation of the algorithm for improving its performance. Before our changes, the core of the implementation was the Quicksort algorithm. The implementation handled a few particular cases specially. Collections of length 5 or less are sorted using sorting networks. Depending on the data type being sorted, collections of lengths up to 30 are sorted using insertion sort. There was special handling for collections where most items are equal and for collections that are almost sorted.

### Optimizing the Compiler's Memory Usage? Let Us Implement a Basic Profiler First!  
[▲ back to schedule](#workshop-schedule)

#### Gunnar Kudrjavets1, Aditya Kumar2

##### 1University of Groningen, 2ACM Distinguished Speaker

The number of files and source lines of code in popular industrial code bases is significant. As of 2017, the Microsoft Windows code base contained 3.5 million files. The Linux kernel contained 27.8 million lines of code in 2020. Compiling code fast is essential to developer productivity for thousands of engineers. Compiler performance requirements, such as CPU and I/O usage, are high. One of the application's standard performance criteria is memory usage and memory allocator churn. Lower memory usage implies a higher capacity to run more compiler instances in parallel. Deceptively easy solutions to reduce memory usage, such as custom memory allocators (e.g., `jemalloc`), are available. However, in our industry experience, nothing replaces context-dependent targeted optimizations. To optimize memory usage, we need to be able to conduct reliable and valid measurements. This talk describes the challenges associated with designing and implementing a performant and scalable mechanism to intercept calls to a memory allocator. We can use that intercept mechanism as an essential profiling tool. A critical requirement for this type of profiler is low-performance overhead, enabling us to run the profiling functionality in a production environment. Attributing and quantifying memory usage in production is a complex problem. The inspiration for this presentation is our experience at Meta (Facebook), where we worked on the performance engineering of various applications. We discuss the problems related to (a) different methods of intercepting allocator calls, such as malloc and free, (b) enabling and disabling the allocator intercept mechanism, (c) keeping track of the count and size of allocations that multiple threads request, (d) the concept of "safe" APIs that are available during the execution of the intercept mechanism, and (e) avoiding reentrancy. We finish our talk by discussing various problems and solutions related to extending the profiling mechanism. If the in-memory data structures are insufficient to keep track of performance-related data, it must be stored somewhere. Interacting with a storage mechanism, such as a hard disk, will add complexity in the case of multiple readers and writers. As a concrete example for our discussion, we use publicly accessible information about Mac OS X and reference the source code from Apple.

### Solid Work-Group Synchronization on CPUs  
[▲ back to schedule](#workshop-schedule)

#### Joachim Meyer1, Aksel Alpay2, Sebastian Hack1, Holger Fröning2, Vincent Heuveline3

##### 1Compiler Design Lab, Saarland Informatics Campus, Saarland University, 2University of Heidelberg, 3Heidelberg University

More and more frameworks and simulations are developed using heterogeneous programming models such as CUDA, HIP, SYCL, or OpenCL. Their hierarchical kernel models are easily mapped to the GPU's resource hierarchy, their massive number of threads, and lightweight synchronization. For compatibility with CPU-only high-performance computing facilities (e.g. Fugaku) or for splitting work across GPUs and CPUs, it is beneficial if the kernels written for those programming models can also be executed on CPUs. A significant hurdle to achieving this in a performance-portable manner is that implementing barriers for such kernels on CPUs requires providing forward-progress guarantees. These guarantees can only be provided by using sufficient concurrency (by means of threads or fibers) or compiler transformations that split the kernels at the barriers. While new variants and improvements are still being proposed, the compiler transformations are similar in spirit. This means that the base transformations are regularly re-implemented in research and production runtimes of the heterogeneous programming models. We propose to have one of these implementations upstream in LLVM, to allow for reusing a mature and optimized implementation.

### RL4ReAl: Reinforcement Learning for Register Allocation  
[▲ back to schedule](#workshop-schedule)

#### S. Venkatakeerthy1, Siddharth Jain1, Anilava Kundu1, Rohit Aggarwal1, Albert Cohen2 and Ramakrishna Upadrasta1

##### 1IIT Hyderabad, 2Google

We aim to automate decades of research and experience in register allocation, leveraging machine learning. We tackle this problem by embedding a multi-agent reinforcement learning algorithm within LLVM, training it with state of the art techniques. We formalize the constraints that precisely define the problem for a given instruction-set architecture, while ensuring that the generated code preserves semantic correctness. We also develop a gRPC based framework providing a modular and efficient compiler interface for training and inference. Our approach is architecture independent: we show experimental results targeting Intel x86 and ARM AArch64. Our results match or out-perform the heavily tuned, production-grade register allocators of LLVM.

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

Proposals should provide sufficient information for the review committee to be able to judge the quality of the submission. Proposals can be submitted under the form of an extended abstract, full paper, or slides. Accepted presentations will be presented online. The presentations will be publicly available on [https://llvm.org/devmtg/](https://llvm.org/devmtg/), and recordings will be available on [LLVM's youtube channel](https://www.youtube.com/channel/UCv2_41bSAa5Y_8BacJUZfjQ)

In case of any queries please reach out to the workshop organizers: Johannes Doerfert (jdoerfert at llnl.gov), Aditya (hiraditya at msn.com), Jose M Monsalve Diaz (jmonsalvediaz at anl.gov), Shilei Tian (i at tianshilei.me),

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

We also adhere to the [Code of Conduct use by CGO](https://conf.researchr.org/attending/cgo-2023/code-of-conduct)

<!-- *********************************************************************** -->

* * *
