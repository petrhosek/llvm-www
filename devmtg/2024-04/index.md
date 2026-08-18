---
layout: "default.html"
permalink: "devmtg/2024-04/index.html"
---
# 2024 EuroLLVM Developers' Meeting

<div style="float: left; width: 68%">

<div style="width: 100%">

<div style="display: flex; gap: 20px;">

<div style="flex: 1;">

1.  [About](#about)
2.  [Program](#program)
3.  [Code of Conduct](#coc)
4.  [Contact](#contact)

</div>

<div style="flex: 1;">

*   **Conference Dates**: April 10-11, 2024 (Pre-Conference workshops April 9)
*   **Location**: [Vienna Marriott, Vienna, Austria](https://www.marriott.com/en-us/hotels/vieat-vienna-marriott-hotel/overview/)
*   **Event Site: Coming Soon [https://llvm.swoogo.com/2024eurollvm](https://llvm.swoogo.com/2024eurollvm)

    # About

    The Euro LLVM Developers' Meeting is a bi-annual gathering of the entire LLVM Project community. The conference is organized by the LLVM Foundation and many volunteers within the LLVM community. Developers and users of LLVM, Clang, and related subprojects will enjoy attending interesting talks, impromptu discussions, and networking with the many members of our community. Whether you are a new to the LLVM project or a long time member, there is something for each attendee.

    To see the agenda, speakers, and register, please visit the Event Site here: [https://llvm.swoogo.com/2024eurollvm](https://llvm.swoogo.com/2024eurollvm)

    What can you can expect at an LLVM Developers' Meeting?

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

    What types of people attend?

    *   Active developers of projects in the LLVM Umbrella (LLVM core, Clang, LLDB, libc++, compiler\_rt, flang, lld, MLIR, etc).
    *   Anyone interested in using these as part of another project.
    *   Students and Researchers
    *   Compiler, programming language, and runtime enthusiasts.
    *   Those interested in using compiler and toolchain technology in novel and interesting ways.

    The LLVM Developers' Meeting strives to be the *best conference* to meet other LLVM developers and users.

    For future announcements or questions: Please visit the LLVM Discourse forums. Most posts are in the Announcements or Community categories and tagged with usllvmdevmtg.

    # Program

    **Keynotes:**

    Does LLVM implement security hardenings correctly? A BOLT-based static analyzer to the rescue?  
    *Kristof Beyls* \[ [Video](https://youtu.be/Sn_Fxa0tdpY) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/Keynote/Beyls_EuroLLVM2024_security_hardening_keynote.pdf) \]  
    In the past decade, security has become one of the 3 key areas in compiler design and implementation, next to correctly translating to assembly and optimization. In comparison to general correctness and optimization, we're lacking tools to test correct code generation of security hardening features. This presentation shows the results of an experiment to build a prototype binary static analyzer for 2 security hardening features (pac-ret, stack clash) using BOLT. The results are promising and I propose to integrate this into the upstream BOLT project to enable us to implement higher-quality security mitigations in LLVM and other compilers.

    How Slow is MLIR  
    *Mehdi Amini, Jeff Niu*  
    \[ [Video](https://youtu.be/7qvVMUSxqz4) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/Keynote/Amini-Niu-HowSlowIsMLIR.pdf) \] This talk will dig into the performance aspects involved in implementing a compiler with MLIR. We're interested here in the compile-time performance (the efficiency of the compiler implementation) instead of the generated code. We will go through implementation details of MLIR and quantify the cost of common operations (traversing or mutating the IR). We will then expose some anti-patterns that we unfortunately commonly see in MLIR-based compilers. Finally we will go through a few elements that are impacting the performance of the IR: for example the threading model of MLIR, how to use resources for zero-overhead management of large constants, taking advantage of the Properties custom storage on operations, or the aspect related to Type/Attribute intrinsic to the storage in the MLIRContext.

    **Tutorials:**

    Zero to Hero: Programming Nvidia Hopper Tensor Core with MLIR's NVGPU Dialect  
    *Guray Ozen* \[ [Video](https://youtu.be/V3Q9IjsgXvA) \] \[ Slides \]  
    NVIDIA Hopper Tensor Core brings groundbreaking performance, requiring the utilization of new hardware features like TMA, Warpgroup level MMA, asynchronous barriers (mbarriers), Thread Block Cluster, and more. Despite having a compiler with these features, crafting a fast GEMM kernel remains challenging. In this talk, we will initially discuss the NVGPU and NVVM dialects, where the Hopper features have been implemented. Following that, we will delve into the implementation of multistage GEMM and warp-specialized GEMM, as used by libraries like Cutlass. Here, we will leverage MLIR's Python bindings to meta-program the IR.

    **Technical Talks:**

    Revamping Sampling-Based PGO with Context-Sensitivity and Pseudo-Instrumentation  
    Wenlei He \[ [Video](https://youtu.be/HYJne9WjSd0) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/He-Yu-Wang-Oh-RevampingSamplingBasedPGO.pdf) \]  
    This talk describes CSSPGO, a context-sensitive sampling-based PGO framework with pseudo-instrumentation. It leverages pseudo instrumentation to improve profile quality without incurring the overhead of traditional instrumentation. It also enriches profile with context-sensitivity to aid more effective optimizations through a novel profiling methodology using synchronized LBR and stack sampling. We will also share how CSSPGO is used to lift performance of Meta's server workloads.

    Deep Dive on MLIR Interfaces  
    Mehdi Amini \[ [Video](https://youtu.be/VCJAmOFvnh4) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Amini-DeepDiveOnMLIRInternals.pdf) \]  
    This talk will walk through the details of implementation of interfaces in MLIR. The interfaces (OpInterfaces, DialectInterfaces, TypeInterfaces, and AttributeInterfaces) are key components of MLIR extensibility. They are composed of a convenient user API through ODS (TableGen) as well as C++ wrappers. However there are many layers of indirection underlying their implementation, which are quite difficult to grasp with. It is a common complaint that it is impossible to debug or trace the code and understand how everything is fitting together.

    Temporal Profiling and Orderfile Optimization for Mobile Apps  
    Ellis Hoag \[ [Video](https://youtu.be/yd4pbSTjwuA) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Hoag-TemporalProfiling-and-OrderfileOptimization-forMobileApps.pdf) \]  
    Traditional PGO can improve CPU-bound applications, but it doesn't work well for some mobile applications which are more concerned with startup time and binary size. We recently extended LLVM's IRPGO framework to support Temporal Profiling to measure an app's startup behavior. We've also created a new algorithm to generate orderfiles called Balanced Partitioning which uses temporal profiles to reduce .text section page faults during startup and can even reduce compressed binary size. And finally, we have a tool to measure an iOS app's page faults on a device to showcase our results. This talk will be useful to anyone interested in understanding how IRPGO can order functions to improve start performance and compressed size.

    Enable Hardware PGO for both Windows and Linux  
    Wei Xiao \[ [Video](https://youtu.be/l-pauXcCz5k) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Xiao-EnablingHW-BasedPGO.pdf) \]  
    In this talk, we will discuss how to enable hardware PGO by extending sampling-based PGO with enriched profiles. We will postmortem some real cases to demonstrate hardware PGO can expose more optimization opportunities than instrumentation-based PGO and thus provide better performance. Moreover, we will discuss how to enable hardware PGO on Windows based on the latest Intel VTune SEP.

    Swift/C++ Interoperability  
    Egor Zhdan \[ [Video](https://youtu.be/2g-fQd_OYUU) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Zhdan-SwiftCPlusPus-Interoperability.pdf) \]  
    Swift/C++ interoperability enables incrementally incorporating Swift - a memory safe language - into existing C++ codebases and has been used to gradually adopt Swift in large C++ projects, including the Swift compiler itself.

    Leveraging LLVM Optimizations to Speed up Constraint Solving  
    Benjamin Mikek \[ [Video](https://youtu.be/MHnScvWl67U) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Mikek-LeveragingLLVMOptimizations-toSpeedUp-ConstraintSolving.pdf) \]  
    SLOT is a new tool which uses existing LLVM optimization passes to speed up SMT constraint solvers like Z3. While existing work has used SMT solving to verify LLVM’s peephole optimizations or in symbolic execution engines like KLEE, we flip the script and use LLVM optimizations to improve constraint solving. Our strategy is to translate SMT constraints into LLVM IR, apply the optimizer, and then translate back, alleviating manual developer effort in understanding both solver and LLVM internals. We find that SLOT speeds up average solving times by up to 2x for floating-point and bitvector constraints, and increases the number of constraints solved at fixed timeouts by up to 80%.

    Structured Code Generation From the Ground Up  
    Alex Zinenko \[ [Video](https://youtu.be/E1QWiJUvw7I) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Zinenko-Vasilache-StructuredCodeGeneration.pdf) \]  
    Native high-level code generation support in MLIR is largely based on the idea of structured code generation, which is often mistaken for being synonymous with the linear algebra (Linalg) dialect. Instead, the structure code generation approach evolved hand-in-hand with the progressive lowering philosophy of MLIR and permeates most of its dialects involved in code generation. This talk attempts to demystify the structured code generation in MLIR by introducing the relevant concepts bottom-up from individual arithmetic operations on scalars, to single instruction multiple data (SIMD) operations on vectors, to manipulations on multi-dimensional tensors. Using small examples and illustrations, it demonstrates that this approach boils down to a handful of concepts largely present in modern hardware though with a slightly different terminology. It does not require deep understanding of MLIR or any specific dialect.

    Contextual Instrumented-Based Profiling for Datacenter Applications  
    Mircea Trofin \[ [Video](https://youtu.be/jwkcmS52btI) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Trofin-ContextualInstrumented-Based%20ProfilingforDatacenter.pdf) \]  
    We present an Instrumentation - Based Profile Guided Optimization (PGO) technique that produces contextual profiles. When applied to a real production binary, it proves competitive when compared to tip-of-tree instrumented PGO in: binary size, runtime and memory overhead, and resulting profile size. We conclude with challenges and possible approaches to incorporating contextual profiles "wholeheartedly" in LLVM.

    C++ Modules: Build 'Em All with CMake and Clang  
    Alexy Pellegrini \[ [Video](https://youtu.be/9OwQZ-LRb0c) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Pellegrini-BuildEmAll-WithCMake.pdf) \]  
    CMake now supports building C++ modules with Clang. We will briefly present what C++ modules are, how to build them and integrate them in your projects, and what are the main challenges and limitations.

    Mojo debugging: extending MLIR and LLDB  
    Walter Erquinigo, Billy Zhu \[ [Video](https://youtu.be/9jfukpjCPIg) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/MojoDebugging.pdf) \]  
    Modular has made great strides towards bringing full-fledged debugging support for the Mojo programming language in LLDB. Our commitment goes beyond making basic debugging work; we aspire to place debugging in a first-class status for Mojo. We'll dive into the unique technical challenges we've faced in this journey, and how we extended MLIR and LLDB for proper language debugging using DWARF, highlighting our open-source contributions. We'll also explore the approach we are taking to create a great user-centric debugging experience, focusing first on VS Code.

    Faster Compilation with GlobalISel: Skipping LLVM-IR  
    Tobias Stadler \[ [Video](https://youtu.be/UYPBVel_OLg) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Stadler-FasterCompilation-With-GlobalISel.pdf) \]  
    In a GlobalISel-based back-end, LLVM-IR is first translated to generic Machine IR (gMIR), which is then selected into target instructions. Instead of generating LLVM-IR, we emit gMIR directly and skip the first part of the code generation pipeline. For our application, this improved compile-times by ~20%. In this talk, we present how to work with gMIR, show how common IR constructs are lowered for GlobalISel, and discuss the performance of LLVM's instruction selectors.

    Experiences building a JVM using LLVM ORC JIT  
    Markus Böck \[ [Video](https://youtu.be/g9b_G4ao3PY) \] \[ [Slides](&lt;https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Bock-Experiences-Building-a-JVM-withLLVMOrc.pdf &gt;) \]  
    JLLVM is a Java virtual machine built with LLVM, featuring a multi-tier system with an interpreter and JIT compiler, a relocating garbage collector and On-Stack replacement. The focus of this talk is to show how LLVM is used to implement JLLVM and these features with the goal of inspiring other LLVM-based virtual machine implementations. Topics covered include presenting the system architecture utilizing ORC JIT and JITLink, the use of statepoints to support relocating garbage collectors, the use of deoptimization operands to enable On-Stack replacement and the tradeoffs of using LLVM as a JIT.

    Teaching MLIR concepts to undergraduate students  
    Mathieu Fehr, Sasha Lopoukhine \[ [Video](https://youtu.be/XnRZA1pz7iw) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Fehr-Lopoukhine-TeachingMLIRConceptsToUndergraduateStudents.pdf) \]  
    We present a compiler from a simple programming language to RISC-V, implemented entirely in MLIR. We use this course to teach undergraduate students at the University of Edinburgh modern compilation concepts and tools. Our course guides students through the whole compilation pipeline, from parsing to assembly generation, with all intermediate representations represented as MLIR IR. We provide the students with dialects for each intermediate representation (AST, ChocoPy, RISC-V SSA, RISC-V), and ask them to implement parsing, verification, lowering, and optimization passes. We talk in detail about the structure of this course.

    Simplifying, Consolidating & Documenting LLDB's Scripting Functionalities  
    Mohamed Ismail Bennani \[ [Video](https://youtu.be/hNvFmZ1iB78) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Bennani-LLDBScriptingImprovements.pdf) \]  
    This presentation explores current challenges in LLDB's scripting capabilities, emphasizing opportunities for improvement such as enhanced discoverability, updated documentation, and minimized maintenance costs. It delves into advancements in the LLDB Python module, as well as in LLDB Scripted Interface Dispatch method, ensuring a seamless conversion from private types to their scripting counterpart.

    Incremental Symbolic Execution for the Clang Static Analyzer  
    Balázs Benics \[ [Video](https://youtu.be/bCr2Rw7UpBI) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Benics-IncrementalCSA.pdf) \]  
    I will present a technique to speed up subsequent Clang Static Analyzer (CSA) runs on mostly unchanged code. CSA takes a lot more time to complete than simply compiling the source code. This imposes challenges for quick developer feedback, for pull requests, or even within your IDE. For incremental and localized changes, we could reuse the bulk of the previous analysis and only re-analyze the changed parts that actually matter. In this talk, besides presenting this novel technique for incremental analysis, I will summarize how CSA currently selects and analyzes functions and elaborate on how this technique could fit into the current architecture.

    Accurate Coverage Metrics for Compiler-Generated Debugging Information  
    J. Ryan Stinnett \[ [Video](https://youtu.be/LePAdLTRa4Q) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Stinnett-Kell-AccurateCoverageMetrics.pdf) \]  
    Many debugging tools rely on compiler-produced metadata to present a source-language view of program states, such as variable values and source line numbers. While this tends to work for unoptimised programs, current compilers often generate only partial debugging information in optimised programs. Current approaches for measuring the extent of coverage of local variables are based on crude assumptions (for example, assuming variables could cover their whole parent scope) and are not comparable from one compilation to another. In this talk, we propose some new metrics, computable by our tools, which could serve as motivation for language implementations to improve debugging quality.

    Optimizing RISC-V code size: Zcmt and Zcmi extensions  
    Gábor Márton \[ [Video](https://youtu.be/SmMAIyjXowM) \]  
    The presentation discovers how linker relaxations optimize executable binaries in the RISC-V architecture, focusing on reducing code size and possibly boosting execution efficiency. We delve into the Zcmt and Zcmi extensions, showcasing their roles in compressing function calls and instruction sequences. We will illuminate how RISC-V linker relaxations complement broader optimization strategies like LTO and post-link optimizations.

    Computing Bounds of SSA Values in MLIR  
    Matthias Springer \[ [Video](https://youtu.be/SI3q-aNkrQ4) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Springer-ComputingBoundsOfSSAValues-In-MLIR.pdf) \]  
    We present the MLIR \`ValueBoundsConstraintSet\` infrastructure, which can compute lower/upper/equality bounds of index-typed SSA values or dynamic dimension sizes of shaped values, in terms of other SSA values or as a constant. For example, this infrastructure has been used to enable vectorization of tensor IR with dynamic dimension sizes and to hoist dynamic memory allocations from loops. In this talk, we present the infrastructure's API, how to extend it with custom ops and touch upon current limitations.

    MLIR Vector Distribution  
    Kunwar Grover, Harsh Menon \[ [Video](https://youtu.be/ueYi9NnK4Pw) \]  
    We present a vector distribution framework for MLIR based on a customizable layout dataflow analysis, signature attributes, and a distribution pattern rewriter. This framework allows us to lower computation over n-D vector types to lower-level code tailored to the constraints of the target hardware like tensor cores or virtual ISAs like SPIR-V. Based on the experience with the implementation in the IREE compiler, we discuss possible future directions for moving parts of the work upstream to MLIR, and influencing the future direction of the MLIR vector abstractions.

    Lifting CFGs to structured control flow in MLIR  
    Markus Böck \[ [Video](https://youtu.be/UqO3o4rXJes) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Bock-LiftingCFGs.pdf) \]  
    A major feature of MLIR is modeling higher-level control flow operation. By treating 'if's and loops as first-class citizens the implementation of transformation passes is simplified and further analysis of loops made easier and incremental. However, depending on the input language, lowering to structured control flow is non-trivial compared to CFGs. This talk therefore presents the recent upstream implementation of lifting control flow graphs to structured control flow. After elaborating what structured control flow is and showing use-cases for lifting from a CFG, the talk further goes into how the upstream implementation works, how it can be used with custom dialects, and any input constraints and guarantees given by the algorithm.

    MLIR Linalg Op Fusion - Theory & Practice  
    Javed Absar \[ [Video](https://youtu.be/7-xAzlda0F8) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Absar-MLIR-LinalgOpFusion.pdf) \]  
    Linalg is an important dialect in MLIR. Many external projects also use Linalg as key dialect to enter the MLIR world. It is an instantiation of what is called - StructuredOps i.e. structured types and structured iterators working coherently together. This talk will first cover some essential concepts of Linalg to give the audience an understanding of linalg ops and transformations. Then it will focus on op fusion in linalg. At end of the talk the audience will have a better understanding on Linalg Op Fusion and adjacent topics.

    Efficient Data-Flow Analysis on Region-Based Control Flow in MLIR  
    Weiwei Chen \[ [Video](https://youtu.be/vvVR3FyU9TE) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Chen-Efficient-Data-Flow-Analysis-on-Region-based-Control-Flow-in-MLIR.pdf) \]  
    Sparse Conditional Constant Propagation (SCCP) is a data-flow analysis based optimization that simultaneously removes dead code while propagating constants along the control-flow graph of a program. In this talk, we present an efficient SCCP algorithm based on a structured region-based control flow model in MLIR for the Mojo programming language. The new algorithm can guarantee the best case of runtime, easy to debug, and can be equally applied to other types of data-flow analyses.

    LLVM-IR-Dataset-Utils - Scalable Tooling for IR Datasets  
    Aiden Grossman, Ludger Paehler \[ [Video](https://youtu.be/_SOWTuWyx1Q) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/TechnicalTalks/Grossman-LLVMIR-DatasetUtils.pdf) \]  
    In this talk we will present how LLVM-IR-Dataset-Utils can be leveraged to build LLVM IR-based datasets, how these datasets can be leveraged for the development of data-intensive machine-learned heuristics, and how readily extensible our utilities are to new data-driven use-cases inside of the LLVM ecosystem to inform the design of future optimization heuristics. We anticipate the datasets constructed with this tooling, and expansions thereof, to have the potential to drive future heuristics validation, correctness testing, machine learning for compilers, and compile-time performance tracking.

    **Panels:**

    Carbon: An experiment in different tradeoffs  
    *Chandler Carruth, Jon Ross-Perkins, Richard Smith* \[ [Video](https://youtu.be/Za_KWj5RMR8) \]  
    This panel is an opportunity to ask the team working on Carbon about any and all of the tradeoffs and experiments that they're undertaking, how the project and experiment are progressing, and more. A group of active members of the Carbon project will share what we've learned so far, including both things we're excited about and would recommend LLVM and other projects to look at, as well as things that haven't gone so well. We'll also be able to talk about what we have left to do, how we plan to approach it, and places where we likely need help.

    **Student Technical Talks:**

    Better Performance Models for MLGO Training  
    Viraj Shah \[ [Video](https://youtu.be/ZI9ytBkHwKg) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/StudentTechnicalTalks/Shah-BetterPerformanceModelsForMLGOTraining.pdf) \]  
    The systematic application of MLGO models to more optimizations is impeded by existing models' insufficient ability to account for many of the dynamic effects associated with runtime as a result of assumptions made about the execution environment and runtime behavior of code. In this talk, we present our work focusing on developing a performance model capable of accurately modeling longest latency cache misses and including resulting overhead into the throughput, and consequently, reward signal calculation. Further, experimenting with different ways to supplement such models with additional features so as to strike a balance between how accurately the model can estimate performance, and how feasible it is to build/train and use.

    Transform-dialect schedules: writing MLIR-lowering pipelines in MLIR  
    Rolf Morel \[ [Video](https://youtu.be/YOWAhrh_qxs) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/StudentTechnicalTalks/Morel-Transform-DialectSchedules.pdf) \]  
    The Transform dialect exposes transformations of MLIR as ops in MLIR. These fine-grained operations can be sequenced to express more involved transformations. When such a sequence expresses a coherent lowering step we refer to it as a schedule. By recent additions to the Transform dialect, we can name these schedules and call them from other sequences. Leveraging this feature, we show how Transform ops compose into reusable schedules and how schedules compose into larger schedules. We show that entire MLIR-lowering pipelines can be declaratively specified in MLIR with large parts being shared among pipelines.

    How expensive is it? Big data for ML cost modeling  
    Aiden Grossman \[ [Video](https://youtu.be/T3-clIqsF3s) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/StudentTechnicalTalks/Grossman-MLCostModeling.pdf) \]  
    Within this talk, we present tooling and processes to create extremely accurate learned cost models. We take a large set of basic blocks from ComPile, benchmark them using llvm-exegesis, and then train a learned cost model based on that data. In contrast to previous approaches, we were able to train on a significantly more representative set of basic blocks than previous approaches due to our use of a large dataset like ComPile on top of the production-grade benchmarking infrastructure

    Sign Extension Optimizations inside LLVM  
    Panagiotis Karouzakis \[ [Video](https://youtu.be/HeIDxixC-VM) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/StudentTechnicalTalks/Karouzakis-SignExtOpts.pdf) \]  
    In certain programs not all the expressions need to use all available bits of precision by the target machine. Also, there are many 32 bit programs that now run in 64-bit targets. Usually, in integer arithmetic and in floating-point arithmetic not all the expressions of a program need all the width of the register, but due to the switch from 32 to 64-bit architectures the registers are usually 64 bits. The compiler has to perform sign extensions in the narrow operations to preserve meaning. However, we can eliminate some sign extensions because not all of them are needed. The key is to know what each operator accepts and produces in their upper bits. Doing it in the LLVM Frontend only adds support for this optimization for one language. In this approach, we performed this optimization inside the LLVM IR. One problem is that if we find an optimal solution for one Node, it might not result in an optimal overall solution. If we had an abstract syntax tree, this problem is completely solvable using Dynamic Programming. This not the case with SSA-form in LLVM IR, because we have a DAG with many users. In this work we explore how to apply the dynamic programming optimization from syntax trees where each node occurs once to LLVM IR where each instruction may be involved in multiple chains.

    High Performance FFT Code Generation through MLIR Linalg Dialect and Micro-kernel  
    Yifei He \[ [Video](https://youtu.be/0K93UdgplTo) \]\[ Slides \]  
    Fast Fourier Transform (FFT) libraries are one of the most critical HPC software components. We've built a compilation framework that can automatically generate high-performance FFT code.

    **Quick Talks**

    Implementing MIR Pattern Matching & Rewriting for GlobalISel Combiners  
    Pierre van Houtryve \[ [Video](https://youtu.be/gQDBrN2uPMk) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Houtryve-MIRPatternsForGlobalISelCombiners.pdf) \]  
    GlobalISel combiners long relied on ad-hoc C++ code to do most of the work despite using TableGen to define their combiner rules. I have recently worked on adding in/out MIR patterns support (complete with a PatFrag-like system and type inference) to the GlobalISel combiners infrastructure which allows us to write many combiner rules directly in TableGen. In this talk, I will be giving an overview of my work on this project and some ideas for what could come next.

    Enhancing clang-linker-wrapper to support SYCL/DPC++  
    Alexey Sachkov \[ [Video](https://youtu.be/uhNHlytKX4c) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Sachkov-EnchancingClang-linker-wrapper-to-supportSYCL.pdf) \]  
    Driven by Intel, SYCL/DPC++ compiler is an LLVM-based project that implements support for the SYCL Language. We (Intel) have made several changes to the clang-linker-wrapper tool to support SYCL device code linking and wrapping. This talk provides an overview of key features we have introduced to the tool in our downstream implementation. The talk will focus on our approach of device code handling, novel mechanism for propagating various metadata from the compiler to the runtime and few other changes.

    Parallelizing applications with indirect memory writes in MLIR  
    Pablo Antonio Martinez, Hugo Trachino \[ [Video](https://youtu.be/mGSu5zdYHpg) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Martinez-ParallelizingApplicationsWithMLIR.pdf) \]  
    Indirect memory writes are present in many AI and HPC applications. However, automatic parallelization of such applications is hard due to data races. In this work we propose a new method to automatically parallelize loops with indirect memory writes in MLIR, showing up to 4.9x speedup across several benchmark suites.

    Arcilator for ages five and up: flexible self-contained hardware simulation made easy  
    Théo Degioanni \[ [Video](https://youtu.be/lE7ynoMstQA) \] \[ [Slides](Degioanni-Arcilator.pdf) \]  
    Arcilator is a simulator for hardware specified in CIRCT dialects (the MLIR hardware modelling subproject). We introduce a new dialect-based interface for Arcilator, which eliminates the need to build heavy C++ wrapper hand-crafted for each hardware model needing simulation. We explain how it is built internally and showcase interesting use cases.

    3 years of experience with the LLVM security group -- successes and remaining challenges  
    Kristof Beyls \[ [Video](https://youtu.be/vbBOumh8iSo) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Belys-LLVMSecurityGroup-3YearExperiences.pdf) \]  
    The LLVM security group was established 3 years ago to enable responsible coordinated disclosure of LLVM security issues. This presentation will briefly summarize what the group is doing; what it has achieved in the past 3 years; and which areas for improvements become clear after analyzing the kinds of issues that were reported. Those include areas such as threat modeling, improving quality of mitigation features, supply chain attacks and how to communicate public security issues that are not CVE-worthy.

    LLDB: What's in a Register?  
    David Spickett \[ [Video](https://youtu.be/Hb7DbdIr3Rk) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Spickett-lldb-Whats-in-a-register.pdf) \]  
    Every tool can disassemble instructions. So why do we not do the same for the contents of registers? Tired of using a manual and a calculator to find out what mode you’re in, where you’re going to branch, what your rounding mode is? Learn about a new feature in LLDB 18 that solves this problem by leveraging the power of Clang’s Abstract Syntax Tree.

    Practical fuzzing for C/C++ compilers  
    Oliver Stannard \[ [Videos](https://youtu.be/3ewJPWW2A00) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Stannard-PracticalFuzzing.pdf) \]  
    In this talk, I will give an overview of the fuzzers which I use to test Clang and GCC. These include open-source fuzzers like csmith, as well as some custom code-generators I have written to target specific parts of the compiler. I'll also talk about how I run these fuzzers, testing a large number of compiler options. In particular, I have found this to be very useful for finding bugs caused by the interaction of seemingly unrelated compiler features. Finally, I'll talk about some useful techniques for turning fuzzer failures into good bug reports, and how to continue running fuzzers before the bugs they find have been fixed.

    Repurposing LLVM analyses in MLIR: Also there and back again across the tower of IRs  
    Henrich Lauko \[ [Video](https://youtu.be/pfViYCignjY) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Lauko-RepurposingLLVMAnalysesInMLIR.pdf) \]  
    LLVM IR boasts a rich history of tools and analyses, but with the emerging rise of MLIR, there is a challenge of transitioning these valuable legacy analyses to the new representation. Ideally, we would not have to touch them at all and repurpose them in MLIR seamlessly. Imagine being able to relate your analysis outcomes from LLVM IR directly to your MLIR dialect – pretty cool, right? In this talk, I will walk you through a solution that allows us to achieve precisely that using what we call a "tower of IRs," connecting LLVM representation to the desired MLIR dialect.

    Life with Opaque Pointers from a Frontend Perspective  
    Sebastian Neubauer \[ [Video](https://youtu.be/lEf4xVrtaxU) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Neubauer-LifeWithOpaquePointers.pdf) \]  
    Many frontends downstream of the LLVM project used to rely on semantically meaningful pointer element type information. The opaque pointer transition forced an end to this practice, creating a difficulty that keeps prompting questions on Discourse to this day. We present our experience moving SPIR-V and DXIL frontends to opaque pointers and a collection of solution patterns.

    Debug information for macros  
    Adrian Prantl \[ [Video](https://youtu.be/WOkoAHTbsbM) \]\[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Prantl-DebugInfoForMacros.pdf) \]  
    When we were adding macros to the Swift language in Swift 5.9, we faced a challenge for how to represent them in debug info and surface them in consumers like LLDB. Like C preprocessor macros, Swift macro expansions can be nested. But unlike C preprocessor macros, Swift macros are AST transformations written in Swift that can either be standalone executables or compiler plugins. In this talk we will explain how we use inline debug information to allow LLDB and other debuggers to selectively step in or over macro expansions, and how we use an LLVM DWARF extension to capture the expanded macro source code in DWARF itself to make it available to debug info consumers that don't have access to the original project.

    From C++ ranges to shorter template names: A C++ Debugging journey  
    Michael Buch \[ [Video](https://youtu.be/VT6-fL2hiN8) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Buch-FromSTDRanges.pdf) \]  
    LLDB’s expression evaluator permits execution of arbitrary C++ expressions. It relies on an interplay between a wide range of LLVM components - the Clang frontend, LLVM’s JIT APIs, DebugInfo, clang modules and more. This quick talk outlines how all of these components fit together by showcasing some recent work we have done on LLDB to improve C++ debugging experience. Namely we describe the process of how we added support for default template arguments and Clang's preferred\_name attribute in the variable view.

    Target-aware vectorization for irregular loops or instruction patterns  
    Wei Wei, Mindong Chen \[ [Video](https://youtu.be/zoff-riWPP8) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Wei-TargetAwareVectorization.pdf) \]  
    This talk will introduce a target-aware vectorization approach for irregular loops or instruction patterns, with a focus on how to generate irregular or complicated vector instructions such as COMPACT, DOT-PRODUCT, HISTCNT, etc. In addition, some clever vectorization schemes are introduced, such as lowering some math library function calls into target-dependent vector instructions, or vectorizing interleaved memory accesses by structure load stores instructions. Finally, we will discuss the choice of implementation, whether based on the Vplan framework or relying on some target-dependent passes, such as loop idiom or inst-combine pass at the backend, which require cost trade-offs.

    Mitigating lifetime issues for C++20 coroutines  
    Utkarsh Saxena \[ [Video](https://youtu.be/SEFaC0wkaVE) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Saxena-MitigatingLifetimeIssues.pdf) \]  
    C++20 coroutines offer an elegant approach to asynchronous programming, streamlining code structure and avoiding callback complexity. However, subtle errors in handling reference parameters can lead to dangling references and use-after-free issues. A key requirement is ensuring the lifetime of reference parameters extends throughout the entire coroutine execution, not merely the first suspension point. We explore common lifetime pitfalls in coroutines, particularly when integrated with constructs like \`std::function\`. We introduce the \[\[clang::coro\_lifetimebound\]\] attribute, extending Clang's lifetime bound analysis to identify these issues at compile time, significantly improving coroutine code safety.

    Loop Iteration Space Splitting  
    Ashutosh Nema \[ [Video](https://youtu.be/iEs4icJcGrI) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Nema-LoopIterationSpaceSplitting.pdf) \]  
    Loop splitting as a general framework to enable various needs ! Loop iteration space splitting is the process of dividing a loop into several smaller loops, each handling a portion of the original loop's iterations. LLVM currently includes a pass called InductiveRangeCheckElimination that performs loop splitting to eliminate range checks. Beyond the current method of eliminating induction range checks, there are additional scenarios where employing loop splitting could facilitate further optimizations.

    A Wishlist for Faster LLVM Back-ends  
    Alexis Engelke \[ [Video](https://youtu.be/i0T_9wTvrbk) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/QuickTalks/Engelke-AWishList-ForFasterLLVM-Backends.pdf) \]  
    LLVM's back-end is often associated with high performance but long compilation times, even for unoptimized builds. This talk shows where compile-time within the LLVM back-end is spent and outlines some ideas for future improvements.

    **Lightning Talks:**

    The Road to Github Actions: Migrating LLVM’s CI  
    Aiden Grossman \[ [Video](https://youtu.be/rqS3kFtCHW8) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/LightningTalks/Grossman-TheRoadToGitHubActions.pdf) \]  
    Continuous integration is an incredibly useful tool for development, especially for a project on the scale of LLVM. Last year, LLVM migrated from precommit review using Phabricator to precommit review using Github Pull Requests. This has sparked significant interest around moving the precommit CI to Github Actions. Within this talk, we cover the recent efforts to move the existing precommit CI over to Github Actions, the engineering challenges involved, future directions, and how the community can get involved to help improve and adapt the CI infrastructure.

    Multilib Configuration Files  
    Peter Smith \[ [Video](https://youtu.be/sEP4qlN_sAU) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/LightningTalks/Smith-MultilibConfigurationFiles.pdf) \]  
    A description of the configuration file based multilib implementation and clang and our experience using it in an embedded toolchain.

    Carbon's high-level semantic IR  
    Richard Smith \[ [Video](https://youtu.be/vIWT4RhUcyw) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/LightningTalks/Smith-Carbons-high-level-semanticIR.pdf) \]  
    An introduction to the Carbon toolchain's Semantics IR. This talk will describe some of the challenges and benefits that come from using a linear execution-based model for the program representation during initial type-checking rather than a traditional tree-based approach as used by Clang.

    Enabling Loop Vectorization for Compressing Store Pattern  
    Tejas Joshi \[ [Video](https://youtu.be/HVQ5mG3lExs) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/LightningTalks/Joshi-EnablingLoopVectorizer-for-CompressingStorePattern.pdf) \]  
    LLVM currently does not vectorize loops with compressing store patterns. We enable this vectorization which give performance improvements in several applications.

    Automatic Proxy App Generation through Input Capture and Generation  
    Johannes Doerfert, Ivan R. Ivanov \[ [Video](https://youtu.be/RUaW1jOQyAo) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/LightningTalks/Ivanov-AutomaticProxyAppGeneration.pdf) \]  
    Benchmarks and proxy apps are extremely important for machine learning applications in compilers and for exploration of new hardware architectures. We introduce a new framework that can capture LLVM IR function inputs from an existing run or generate synthetic input from IR only. Bundled with a simple driver, this allows for easily relocatable and reproducible runs on a variety of systems.

    How we use MLIR to test ReRAM cells  
    Maximilian Bartel \[ [Video](https://youtu.be/Ym9WQHg9k6U) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/LightningTalks/Bartel-HowWeUseMLIR-To-TestReRAMCells.pdf) \]  
    Devices for neuromorphic computing are still prone to defects and limitations. However the impact those have on neural networks is not clear. In this talk I show how I used the linalg and transform dialect together with the Python execution engine in MLIR to test real devices on our lab equipment.

    Automatic Retuning of Floating-Point Precision  
    Ivan R. Ivanov, William S. Moses \[ [Videos](https://youtu.be/QOjgIzEsmzQ) \] \[ Slides \]  
    The choice of a floating point representation is often key to the success of an algorithm's implementation. Using too large of a floating-point type can limit performance, whereas using too small a floating-point type reduces accuracy. This has been especially critical in machine learning applications, where manually tuning floating point type is required to ensure large language models do not overwhelm the available memory bandwidth. Typically, a programmer makes a choice of the floating operation in their application, and any changes require require extensive rewrites of the code. This both limits the ability of changing representation for any large codebases, and is especially restrictive if one wants to search over the space of available floating point sizes. Integrated as part of the Enzyme framework, we introduce a pass to automatically change the floating point precision in existing applications. This can be applied at both a whole-application level, as well as planned support for individual operations. A motivation for building this within an AD framework is to leverage the floating-point error results that can be generated by AD to automatically select which floating point computations can be changed without substantially changing the accuracy of the end program.

    OpenSSF Scorecard - Do we need to improve our security practices?  
    Marius Brehler \[ [Video](https://youtu.be/X9igMS_CR4o) \] \[ [Slides](https://llvm.org/devmtg/2024-04/slides/LightningTalks/Brehler-OpenSSFScorecard-Do-we-need-to-improve.pdf) \]  
    Scorecard is an automated tool created by OpenSSF to help maintainers of open source software to improve their security best practices and to help consumers of open source software to assess whether their dependencies are safe. The scores can be used to identify areas that need to be improved in order to enhance the security of a project. With https://github.com/llvm/llvm-project/pull/69933 a OpenSSF Scorecard action and badge were added to the LLVM repository. This presentation gives a brief analysis of the current OpenSSF Scorecard report and points out which actions were and still can be taken to improve the score.

    **Posters:**

    Developing an LLVM Backend for VLIW RISC-V Vector Extension Architectures  
    Hao-Chun Chang \[ [Poster](https://llvm.org/devmtg/2024-04/slides/Posters/Chang-VLIW-RISC-V-VectorExt-Poster.pdf) \]  
    In this poster, an experimental VLIW RISC-V target with Vector extension is presented. We summarize the process of LLVM compiler implementation for this experimental target. In addition, we also enable Swing Modulo Scheduling for our target to enhance performance with software pipelining. There are issues related to LMUL issues. We incorporate LMUL design in RVV into Swing Modulo Scheduling. We will discuss the problem encountered and the approach to handle it. Eventually, we show the experimental result of performance improvement.

    Hybrid Execution: Combining Ahead-of-Time and Just-in-Time Compilation of LLVM Bitcode  
    Christoph Pichler \[ [Poster](https://llvm.org/devmtg/2024-04/slides/Posters/Pichler-Poster-CombiningExecutionModes-of-LLVMBitCodeOn-GraalVM.pdf) \]  
    Compiler research has been putting high effort into statically generating efficient native code ahead of time (AOT), as it can be seen in the LLVM project and clang, for example. In contrast, GraalVM is a polyglot execution engine that can also execute LLVM bitcode, and comes with an aggressively optimizing just-in-time (JIT) compiler. We present an approach that combines together the advantages of both AOT and JIT compilation, where the overhead of JIT compilation is avoided by utilizing natively executed methods and improving the warm-up performance. The goal of our current follow-up work is to more automatically determine which code candidates are suitable for native execution. We would like to be able to traverse certain parts in the call graph of the code and be able to identify whether the execution of a certain function should happen natively or through the GraalVM JIT compiler.

    Dynamic Evolution of Instruction Set Simulators: A Practical Approach with "ALPACA"  
    Nicholas Fry \[ [Poster](https://llvm.org/devmtg/2024-04/slides/Posters/Fry-Poster-GeneratingInstructionSetSimulatorsFromHardwareDescription-WithCIRCTMLIR.pdf) \]  
    We present ALPACA, a work-in-progress CIRCT MLIR approach to generating an ISS for emerging accelerator architectures from their RTL/HLS description. ALPACA facilitates the automatic generation of state update functions, enabling the ISS to dynamically evolve with hardware implementations.

    PoTATo: Points-to analysis via domain specific MLIR dialect  
    Robert Konicar \[ [Poster](https://llvm.org/devmtg/2024-04/slides/Posters/Konicar-Lauko-PotatoPoster.pdf) \]  
    Addressing the diverse needs of points-to analysis in various use-cases requires a flexible approach. In this talk you can learn about a new unifying framework, PoTATo, designed to allow users to select an algorithm that suits their specific needs. PoTATo employs a novel approach, representing memory effects as a simplified dialect generated from a source IR. This simplified representation abstracts away unnecessary IR details, unifying the analysis process. Furthermore, leveraging general MLIR tooling, the representation can be optimised, significantly reducing the points-to analysis problem. This talk showcases how PoTATo has successfully transformed the complexity of points-to analysis into a streamlined dialect transition.

    VAST: MLIR compiler for C/C++  
    Henrich Lauko \[ [Poster](https://llvm.org/devmtg/2024-04/slides/Posters/Lauko-Poster-VAST.pdf) \]  
    This poster will introduce the distinctive architecture of VAST, an MLIR-based compiler specifically designed for program analysis of C/C++. At the heart of VAST lies a versatile stack of intermediate representations (tower of IRs), empowering users to select the most suitable representations for program analysis or subsequent abstraction. Emphasizing its core infrastructure built around the IR stack, we will demonstrate its practical applications in diverse compilation scenarios, including static analysis, language transpilation, and decompilation.

    IR Around the World: Statistical Analysis of a Massive Multi-Language Corpus of IR  
    Khoi Nguyen, Andrew Kallai \[ [Poster](https://llvm.org/devmtg/2024-04/slides/Posters/Grossman-IRAroundTheWorld) \]  
    Within this walk, we present statistical analyses of the properties of the generated IR, and the optimization pipeline itself. We quantify a number of factors related to the optimization pipeline including which optimizations are run, how long they take, and perform an analysis of the code at the end on a massive corpus of multi-language IR. We anticipate our results to be a starting point for deeper specific investigations on issues like the optimality of the current pass pipelines and help to better understand where compile time is spent. Initial results are presented here but the talk will focus on knowledge filtered out of this data and more we will gather in the meantime.

    Solving Phase Ordering with Off-Policy Deep Reinforcement Learning Algorithms  
    Oliver Chang \[ [Poster](https://llvm.org/devmtg/2024-04/slides/Posters/Chang-Poster-SolvingPhaseOrdering-WithOffPolicyDeepReinforcement.pdf) \]  
    We address the phase ordering problem in an LLVM compiler, using off-policy deep reinforcement learning (DRL). Previous work applying DRL in the phase ordering problem have mainly used policy optimization techniques which is sample inefficient compared to off-policy approaches or Deep Q-learning which has been surpassed by novel algorithms. In particular, we use Double Deep Q-learning as our algorithm and the Compiler Gym framework to facilitate the reinforcement learning environment (LLVM), program inputs, reward function, and action space. We show success in reducing intermediate representation (IR) instruction count while using a light-weight neural network and small memory buffer.

    # Code of Conduct

    The LLVM Foundation is dedicated to providing an inclusive and safe experience for everyone. We do not tolerate harassment of participants in any form. By registering for this event, we expect you to have read and agree to the [LLVM Code of Conduct](http://llvm.org/docs/CodeOfConduct.html).

    # Contact

    To contact the organizer, [email events@llvm.org](mailto:events@llvm.org)

    <!-- *********************************************************************** --> <!--#include virtual="sponsors.incl" -->

    * * *

    <!--#include virtual="../../footer.incl" -->

    **

</div>

</div>

</div>

</div>
