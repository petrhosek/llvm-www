---
layout: "default.html"
permalink: "devmtg/2026-01/index.html"
---
# Tenth LLVM Performance Workshop at CGO

*   **What:** Tenth LLVM Performance Workshop at CGO
*   **When:** January 31st, 2026 (Saturday)
*   **Where:** Sydney, Australia
[International Convention Centre Sydney, Sydney, Australia](https://2026.cgo.org/track/cgo-2026-workshops-and-tutorials) \[In person\]*   **Proposals should be submitted to:** [Easychair](https://easychair.org/conferences?conf=llvmcgo2026)
*   **The deadline for receiving submissions is:** December 23rd, 2025 ~December 16th, 2025~
*   **Speakers will be notified of acceptance or rejection by:** December 24th, 2025 ~December 23rd, 2025~
*   Note: Travel grants are available to eligible candidates upon request. Please reach out to the program committee if you need a travel grant.
*   Note: Invitation letters for visa application are available upon request. Please reach out to the program committee if you need invitation letter for visa application.

The Tenth LLVM Performance Workshop will be held at ([CGO 2026](https://2026.cgo.org/track/cgo-2026-workshops-and-tutorials)). The workshop is co-located with CC, HPCA, and PPoPP. If you are interested in attending the workshop, please register at the ([CGO website](https://conf.researchr.org/home/cgo-2026)). The LLVM workshop at CGO will be in-person.

Program Committee:

*   Aditya (hiraditya at msn.com)
*   Jose M Monsalve Diaz (josem.monsalvediaz at amd.com)
*   Shilei Tian (i at tianshilei.me)
*   Rafael Andres Herrera Guaitero (rafaelhg at udel.edu)
*   Kevin Sala (salapenades1 at llnl.gov)

# Schedule

<!-- Opening Remarks --> <!-- Keynote --> <!-- Talk 1 --> <!-- Coffee Break --> <!-- Talk 2 --> <!-- Talk 3 --> <!-- Talk 4 --> <!-- Lunch Break --> <!-- Talk 5 --> <!-- Talk 6 --> <!-- Talk 7 --> <!-- Closing Remarks -->

| Time (AEDT) | Title | Speaker | Topic |
| --- | --- | --- | --- |
| 8:45 - 9:00 (15 min) | Welcome and Opening Remarks | [Jose M Monsalve Diaz](https://www.linkedin.com/in/josemonsalve2/)<br>[Shilei Tian](https://www.linkedin.com/in/shiltian/)<br>[Aditya](https://twitter.com/_hiraditya_)<br>[Rafael A Herrera Guaitero](https://www.linkedin.com/in/randres-herrera/)<br>[Kevin Sala](https://www.linkedin.com/in/kevinsalapenades/) |  |
| 9:00 - 10:00 (60 min) | Keynote: [ML Optimizations in Production LLVM: The Next Research Challenges (an engineer's opinion)](#keynote)<br>\[[slides](slides/ml-optimizations-in-production-llvm.pdf)\] | Mircea Trofin | ML, Optimization, Industry |
| 10:00 - 10:30 (30 min) | [Compiling Agentic AI Programs for Dataflow Execution: An MLIR Approach](#talk1)<br>\[[slides](slides/compiling-agentic-ai-dataflow-mlir.pdf)\] | Miguel Andrés Cárdenas Sierra, Rafael A Herrera Guaitero, Isaac David Bermudez Lara, Jose M Monsalve Diaz | MLIR, Dataflow Compilation, Agentic AI, Compiler Optimization, Concurrency |
| 10:30 - 11:00 (30 min) | Coffee Break | \- | \- |
| 11:00 - 11:30 (30 min) | [Polymer: An explainable database execution engine based on MLIR](#talk2)<br>\[[slides](slides/polymer.pdf)\] | Yizhe Zhang, Bocheng Han, Zhengyi Yang | MLIR, Database Execution Engine, JIT Compilation, Query Optimization, Pipeline Execution |
| 11:30 - 12:00 (30 min) | [Profile Once, Optimize Anywhere: Architecture-agnostic Profile-Guided Optimization](#talk3)<br>\[[slides](slides/apgo_cgo_workshop.pdf)\] | Lei Qiu, Yikang Fan, Yanxia Wu, Fang Lyu | Profile-Guided Optimization, Cross-Architecture Optimization, Compiler Optimization, HPC |
| 12:00 - 12:30 (30 min) | [Practice on Optimizing SPEC CPU 2017 for Sunway Architecture](#talk4)<br>\[[slides](slides/spec-cpu-sunway-optimization.pdf)\] | Yingchi Long, Jun Jiang, Yanhe Zhai, Yaohui Han, Ying Liu, Zheng Lin, Yuyang Zhang, Zhongcheng Zhang, Jiahao Shan, Zhenchuan Chen, Xiaobing Feng, Huimin Cui | Sunway Architecture, LLVM Compiler, Vectorization, Partial Redundancy Elimination, Constant Propagation |
| 12:30 - 13:45 (75 min) | Lunch Break | \- | \- |
| 13:45 - 14:15 (30 min) | [Nugget: Portable Program Snippets](#talk5)<br>\[[slides](slides/nugget-portable-program-snippets.pdf)\] | Zhantong Qiu, Mahyar Samani, Jason Lowe-Power | Computer Architecture, Simulation, Workload Reduction, Sampling Methodology, Portable Program Snippets |
| 14:15 - 14:45 (30 min) | [An End-to-End Workflow for Data-Driven GPU Optimization with LLVM](#talk6) | Konstantinos Parasyris | LLVM, GPU, Data Collection, Performance Optimization |
| 14:45 - 15:15 (30 min) | [Equipping LLVM/OpenMP with Advanced OpenMP GPU Offloading Features](#talk7)<br>\[[slides](slides/equipping-llvm-openmp-gpu-offloading.pdf)\] | Kevin Sala, Krishna Chaitanya Sankisa, Krzysztof Parzyszek, Michael Klemm | OpenMP, GPU, Accelerator, Target, LLVM, Clang |
| 15:15 - 15:30 (15 min) | Closing Remarks | [Jose M Monsalve Diaz](https://www.linkedin.com/in/josemonsalve2/)<br>[Shilei Tian](https://www.linkedin.com/in/shiltian/)<br>[Aditya](https://twitter.com/_hiraditya_)<br>[Rafael A Herrera Guaitero](https://www.linkedin.com/in/randres-herrera/)<br>[Kevin Sala](https://www.linkedin.com/in/kevinsalapenades/) |  |

# Abstracts

<!-- Abstract for Keynote -->

### ML Optimizations in Production LLVM: The Next Research Challenges (an engineer's opinion)  
[▲ back to schedule](#workshop-schedule) \[[slides](slides/ml-optimizations-in-production-llvm.pdf)\]

#### Mircea Trofin

LLVM has had support for ML-Guided Optimizations for the last 5 years, applied first to a size problem (via the inliner), and then for a performance problem (via the register allocator). At Google, we've been using both in production workloads: the former, for Chrome on Android; Fuchsia OS; and for cloud infrastructure. The latter, for our instrumented profiling binaries, including search; and for the Android compiler toolchain and within AOSP. This talk is about open problems from the challenges we encountered. Specifically, it is a call for collaboration between academia and industry on addressing what we learned to be the key challenging compiler problems which, once solved, can unlock the wide-spread replacement of optimization decisions with policies trained via automatic techniques (ML or AI), at large scale in the industry.

<!-- Abstract for Talk 1 -->

### Compiling Agentic AI Programs for Dataflow Execution: An MLIR Approach  
[▲ back to schedule](#workshop-schedule) \[[slides](slides/compiling-agentic-ai-dataflow-mlir.pdf)\]

#### Miguel Andrés Cárdenas Sierra, Rafael A Herrera Guaitero, Isaac David Bermudez Lara, Jose M Monsalve Diaz

Agentic AI programs orchestrate inference, memory, and external tools to accomplish complex tasks. Compiling these programs presents distinct challenges: individual operations may take seconds to complete, execution depends on remote services, and the primary opportunity for optimization lies in exploiting concurrency among independent operations rather than traditional instruction-level techniques. We introduce an MLIR dialect for agentic AI that represents data dependencies explicitly through dataflow semantics. The dialect defines 18 operations covering inference, three-tier memory, tool invocation, and synchronization. Three optimization passes exploit the structure of agent programs: reasoning fusion reduces inference round-trips by merging sequential operations, context deduplication eliminates redundant inputs across operations, and capability scheduling enables cost-aware execution ordering through operation classification. The compiler performs dependency analysis to identify concurrent execution opportunities and lowers programs to dataflow graphs where execution is driven by data availability rather than program order. This work demonstrates that domain-specific MLIR dialects enable effective compiler optimization for AI workloads where latency dominates execution time.

<!-- Abstract for Talk 2 -->

### Polymer: An explainable database execution engine based on MLIR  
[▲ back to schedule](#workshop-schedule) \[[slides](slides/polymer.pdf)\]

#### Yizhe Zhang, Bocheng Han, Zhengyi Yang

Despite significant advances in database execution engine performance through Just-in-Time (JIT) compilation and optimized execution strategies, database systems continue to suffer from limited explainability and extensibility. Evaluating individual operator implementations typically requires modifying source code, and database operation reuse remains constrained by language boundaries. We present Polymer, a framework that leverages MLIR's hierarchical intermediate representation to model database execution engines. Polymer treats database operations as composable MLIR operators, enabling fine-grained debugging and systematic optimization across operator boundaries. By representing query execution plans as MLIR modules and lowering them to LLVM IR for execution via LLVM's ORC JIT runtime, Polymer provides a unified platform for evaluating query optimizers, comparing data format I/O performance, and identifying performance bottlenecks at the operator level. Our approach transforms database execution into a compiler-centric problem, enabling the application of mature compiler optimization techniques to database systems while preserving explainability through MLIR's multi-level representation.

<!-- Abstract for Talk 3 -->

### Profile Once, Optimize Anywhere: Architecture-agnostic Profile-Guided Optimization  
[▲ back to schedule](#workshop-schedule) \[[slides](slides/apgo_cgo_workshop.pdf)\]

#### Lei Qiu, Yikang Fan, Yanxia Wu, Fang Lyu

Profile-Guided Optimization (PGO) is a widely used technique for guiding compiler optimizations with runtime behavior. However, its adoption is limited by the high cost of collecting architecture-specific profiles, especially on resource-constrained devices or slow simulation platforms. We propose APGO, an architecture-agnostic PGO framework that enables "profile once, optimize anywhere". APGO treats profile transfer as a region-level alignment problem: APGO directly reuses matched profile regions and employs an AI-Guided Synthesizer to reconstruct missing profile data through architecture-aware layout adaptation and profile mapping. This approach removes the requirement for native profiling on divergent targets, enabling efficient profile reuse. Experimental results show that APGO reduces up to 32.78x profiling time compared to native architecture profiling, while achieving comparable performance on the majority of workloads (34/54 single-core and 11/20 multi-threaded) across RISC-V and ARM. Notably, APGO even surpasses native PGO on 14 single-core and 6 multi-threaded workloads, with peak improvements of 13%.

<!-- Abstract for Talk 4 -->

### Practice on Optimizing SPEC CPU 2017 for Sunway Architecture  
[▲ back to schedule](#workshop-schedule) \[[slides](slides/spec-cpu-sunway-optimization.pdf)\]

#### Yingchi Long, Jun Jiang, Yanhe Zhai, Yaohui Han, Ying Liu, Zheng Lin, Yuyang Zhang, Zhongcheng Zhang, Jiahao Shan, Zhenchuan Chen, Xiaobing Feng, Huimin Cui

Sunway architecture requires tailored compiler optimizations to be performed to achieve peak performance on Sunway CPUs. In the practice of optimizing SPECCPU 2017 benchmark suite, a few compiler optimizations targeting Sunway architecture have been implemented, involving both approaches dedicated for Sunway instruction set and micro-architecture, and common methods that may also benefit other architectures (e.g., X86, ARM, RISC-V) but not included in mainstream LLVM yet. This work introduces four such optimizations integrated into the LLVM: 1) customized instruction selection for vectorized zero-extending load and truncating store, 2) vectorization factor calculation based on bit-width in vector register, 3) loop-carried partial redundancy elimination and 4) constant propagation of fortran arguments. Evaluated on the SPEC CPU 2017 benchmark suite across two 64-core Sunway CPUs (SW3231 and WX-H8000), the enhanced compiler achieves ratio increases of 20.62% for integer and 28.28% for floating-point workloads, compared to a non-vectorized baseline.

<!-- Abstract for Talk 5 -->

### Nugget: Portable Program Snippets  
[▲ back to schedule](#workshop-schedule) \[[slides](slides/nugget-portable-program-snippets.pdf)\]

#### Zhantong Qiu, Mahyar Samani, Jason Lowe-Power

Evaluating architectural ideas on realistic workloads is increasingly challenging due to the prohibitive cost of detailed simulation and the lack of portable sampling tools. Existing targeted sampling techniques are often tied to specific binaries, incur significant overhead, and make rapid validation across systems infeasible. To address these limitations, we introduce Nugget, a flexible framework that enables portable sampling across simulators, hardware, architectural differences, and libraries. Nugget leverages LLVM IR to perform binary-independent interval analysis, then generates lightweight, cross-platform executable snippets (nuggets), that can be validated natively on real hardware before use in simulation. This approach decouples samples from specific binaries, dramatically reduces analysis overhead, and allows researchers to iterate on sampling methodologies while efficiently validating samples across diverse systems.

<!-- Abstract for Talk 6 -->

### An End-to-End Workflow for Data-Driven GPU Optimization with LLVM  
[▲ back to schedule](#workshop-schedule)

#### Konstantinos Parasyris

Collecting representative GPU benchmarks remains a fundamental challenge for compiler and performance researchers: real applications are complex, dynamic, and difficult to extract into reproducible kernels without losing important optimization context. Reasoning about how modern compilers optimize such workloads—and how individual optimization decisions impact performance, code size, compilation time, or register pressure—is even harder. As a result, automating performance optimization and enabling data-driven approaches often requires substantial manual effort and deep compiler expertise. LLVM provides powerful analysis and transformation capabilities, but its steep learning curve and compiler-centric tooling make it difficult for data scientists and ML researchers to engage effectively. These communities need realistic datasets, controllable optimization knobs, and programmatic access to compiler behavior—not ad-hoc benchmarks or handcrafted microkernels. Mneme addresses this gap by providing an end-to-end framework for GPU performance experimentation built on LLVM. Mneme records kernels directly from real GPU applications, enabling the collection of representative workloads without modifying application source code. It supports automated replay and autotuning across multiple optimization parameters, while exposing rich metrics including execution time, compilation time, executable size, and register pressure. Through Python bindings, Mneme integrates naturally with the broader data science and ML ecosystem, enabling large-scale dataset construction and data-driven optimization studies. By lowering the barrier to collecting, analyzing, and optimizing realistic GPU workloads, Mneme can make LLVM-based GPU research more accessible, reproducible, and data-centric.

<!-- Abstract for Talk 7 -->

### Equipping LLVM/OpenMP with Advanced OpenMP GPU Offloading Features  
[▲ back to schedule](#workshop-schedule) \[[slides](slides/equipping-llvm-openmp-gpu-offloading.pdf)\]

#### Kevin Sala, Krishna Chaitanya Sankisa, Krzysztof Parzyszek, Michael Klemm

OpenMP is the de facto standard parallel programming model for shared-memory systems. With the introduction of OpenMP 4.0 over a decade ago, the specification was extended to support accelerators, including GPUs, through the target offloading model. This model provides a portable approach to accelerating code regions in C, C++, and Fortran across multiple GPU vendors and other state-of-the-art accelerators. Despite these advantages, some performance overheads and the lack of essential GPU-specific features have limited widespread adoption. Consequently, many HPC developers continue to rely on vendor-specific programming models such as CUDA and HIP to achieve peak application performance. To address these challenges, the OpenMP language committee is actively working on extending the specification to better expose GPU-oriented capabilities. In this talk, we cover several of these upcoming OpenMP features, discuss their work-in-progress implementation in Clang and LLVM/OpenMP, and provide a preliminary performance comparison against native GPU APIs on a few C/C++ benchmarks.

# Call for Speakers

We invite speakers from academia and industry to present their work on the following list of topics (including and not limited to:):

*   Improving performance and code-size of applications built by LLVM toolchains
*   Improving performance of LLVM's runtime libraries
*   Improving the security of generated code
*   Any tools or products developed by using one of the libraries in LLVM infrastructure
*   Performance tracking over time
*   Compiler flags, annotations and remarks to understand and improve performance
*   Any other topic related to improving and maintaining the performance and quality of LLVM generated code

While the primary focus of the workshop is on these topics, we welcome any submission related to the LLVM project, its sub-projects (clang, mlir, lldb, Polly, lld, openmp, pstl, compiler-rt, etc.), as well as their use in industry and academia.

We are looking for:

*   keynote speakers (30-60 minutes),
*   technical presentations (25 minutes plus questions and discussion),
*   tutorials (30-60 minutes),
*   panels (30-60 minutes),
*   BOFs (30-60 minutes)

Proposals should provide sufficient information for the review committee to be able to judge the quality of the submission. Proposals can be submitted under the form of an extended abstract, full paper, or slides. Accepted presentations can be presented in-person or online. The presentations will be publicly available on [https://llvm.org/devmtg/](https://llvm.org/devmtg/), and recordings will be available on LLVM's YouTube channel ([https://www.youtube.com/channel/UCv2\_41bSAa5Y\_8BacJUZfjQ](https://www.youtube.com/channel/UCv2_41bSAa5Y_8BacJUZfjQ))

In case of any queries please reach out to the workshop organizers: Aditya (hiraditya at msn.com), Jose M Monsalve Diaz (josem.monsalvediaz at amd.com), Shilei Tian (i at tianshilei.me), Rafael Andres Herrera Guaitero (rafaelhg at udel.edu), or Kevin Sala (salapenades1 at llnl.gov).

#### What types of people attend?

*   Active developers of projects in the LLVM Umbrella (LLVM core, Clang, LLDB, libc++, compiler\_rt, klee, lld, OpenMP, MLIR etc).
*   Anyone interested in using these as part of another project.
*   Students and Researchers.
*   Compiler, programming language, and runtime enthusiasts.
*   Those interested in using compiler and toolchain technology in novel and interesting ways.

#### Panels

Panel sessions are guided discussions about a specific topic. The panel consists of ~3 developers who discuss a topic through prepared questions from a moderator. The audience is also given the opportunity to ask questions of the panel.

#### Birds of a Feather (BoF)

A BoF session, an informal meeting at conferences, where the attendees group together based on a shared interest and carry out discussions without any pre-planned agenda.

#### Technical Talks

These 25 minute talks cover all topics from core infrastructure talks, to project's using LLVM's infrastructure. Attendees will take away technical information that could be pertinent to their project or general interest.

#### Tutorials

Tutorials are 30-60 minute sessions that dive down deep into a technical topic. Expect in depth examples and explanations.

# Code of Conduct

The LLVM Foundation is dedicated to providing an inclusive and safe experience for everyone. We do not tolerate harassment of participants in any form. By registering for this event, we expect you to have read and agree to the [LLVM Code of Conduct](http://llvm.org/docs/CodeOfConduct.html). We also adhere to the [CGO Code of Conduct](https://conf.researchr.org/attending/cgo-2026/code-of-conduct).

<!-- *********************************************************************** -->

* * *
