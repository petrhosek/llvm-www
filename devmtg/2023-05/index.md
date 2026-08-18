---
layout: "default.html"
permalink: "devmtg/2023-05/index.html"
---
# 2023 European LLVM Developers' Meeting

<div style="float: left; width: 68%">

<div style="width: 100%">

# About

The LLVM Developers' Meeting is a bi-annual gathering of the entire LLVM Project community. The conference is organized by the LLVM Foundation and many volunteers within the LLVM community. Developers and users of LLVM, Clang, and related subprojects will enjoy attending interesting talks, impromptu discussions, and networking with the many members of our community. Whether you are a new to the LLVM project or a long time member, there is something for each attendee.

To see the agenda, speakers, and register, please visit the Event Site here: [https://llvm.swoogo.com/2023eurollvm/](https://llvm.swoogo.com/2023eurollvm/)

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

For future announcements or questions: Please visit the LLVM Discourse forums. Most posts are in the Announcements or Community categories and tagged with EuroLLVM.

# Program

**Keynotes**

Order out of Chaos, The LLVM Release Process \[ [Video](https://youtu.be/onaNb2U1Od8) \] \[ [Slides](&lt;slides/TechnicalTalks-May10/01-Tobias Hieta-LLVM-Release-Process.pdf&gt;) \]  
*Tobias Hieta, Ubisoft*  

In this Talk, I will explain how the LLVM release process works. How fixes are created, staged, tested, and reviewed to be included in a release and how community members can get involved and help improve future releases of LLVM.  

“-fbounds-safety”: Enforcing bounds safety for production C code \[ [Video](https://youtu.be/RK9bfrsMdAM) \] \[ [Slides](slides/TechnicalTalks-May11/01-Na-fbounds-safety.pdf) \]  
*Yeoul Na, Apple*  

In this talk we will describe “-fbounds-safety”, a new language extension implemented in Clang that brings bounds safety to the C language. The language extension addresses multiple of the practical challenges that have made existing approaches to safer C dialects difficult to adopt. Our approach facilitates incremental adoption by preserving source compatibility with standard C and preserving ABI-compatibility with C binaries. It also minimizes adoption effort by reconciling wide pointers (a.k.a. “fat” pointers) with ABI-preserving bounds annotations. “-fbounds-safety” has been adopted on millions of lines of production C code and proven to work in an industrial setting.  

**Technical Talks**

Extensible and Composable Dataflow Analysis in MLIR \[ [Video](https://www.youtube.com/watch?v=5BijBv2TDnU) \] \[ [Slides](slides/TechnicalTalks-May10/07-TomEccles-JeffNiu-MLIRDataflowAnalysis.pdf) \]  
*Tom Eccles, Arm & Jeff Niu, Modular*  

Designing a dataflow analysis framework requires understanding the peculiarities of the compiler's IR: analyses need to run in a reasonable time and without algorithmic explosion, analyses need to compose, and the framework must be extensible to allow building a library of analyses. MLIR does not have fixed IR semantics. The IR is user-extensible, and this reflects the primary challenge of building core infrastructure in MLIR. It is not possible to build a dataflow analysis framework for MLIR the same way as they have been built for other compilers. We proposed (and upstreamed) a general-purpose dataflow analysis framework to MLIR designed according to MLIR's core principles: extensible, composable, and debuggable. Our framework is unique in that it separates the states of lattice elements from the logic that produces them: we allow users to define new kinds of state but also inject transfer functions for existing states. Our framework also has a dynamic dependency graph that is lazily instantiated according to the shape of the IR, reducing the number of iterations to converge. In our talk, we will present the mathematical formulation for transparently composable dataflow analyses. We will discuss the implementation in upstream MLIR and how core analyses like dead code analysis, constant propagation, and integer range analysis can be composed together with out-of-tree dialects and analyses. As an in-depth example, we will give an overview of Flang's stack arrays pass, which operates on Flang's MLIR dialects, It moves compiler-added array temporaries from the heap to the stack and uses data-flow analysis to ensure that pointer lifetimes do not escape the current stack frame. We show how this analysis is composed with in-tree analyses to achieve better results. If there is time, we will show how data flow analysis can be used in a wider context by reviewing the whole Flang stack arrays pass.  

MLIR-based offline memory planning and other graph-level optimizations for xcore.ai \[ [Video](https://youtu.be/zjDllpl8RVc) \] \[ [Slides](slides/TechnicalTalks-May10/06-Panickal-MLIROfflineMemoryPlanning.pdf) \]  
*Deepak Panickal, XMOS*  

In this talk, we will give a walk-through of our MLIR-based graph compiler optimizing TensorFlow Lite models to be deployed on the xcore.ai microcontroller. We focus specifically on MLIR passes for memory usage reduction, such as offline memory planning, operator splitting, and streaming constants from flash, along with other passes. We leverage open-source projects such as MLIR, Tensorflow, and tflite-micro-compiler to create a small executable within various resource constraints. In contrast to other compilers in the LLVM world, we do not lower to LLVM IR. Instead, we produce C++ source code using tflite-micro-compiler, which is compiled and executed by our toolchain. We will go through some of the challenges in our journey and future plans. All code for the graph compiler and runtime is available publically on GitHub.  

A Rusty CHERI: The path to hardware capabilities in Rust \[ [Video](https://youtu.be/6vCh3WSLMvo) \] \[ Slides \]  
*Lewis Revill, Embecosm*  

Can we make unsafe Rust code safer with hardware capabilities? This talk presents the motivation behind our effort to support CHERI (Capability Hardware Enhanced RISC Instructions) in Rust, the challenges involved in modifying the Rust compiler to achieve this, and the current state of Rust/CHERI (hopefully with a demo).  

Extending the AArch32 JITLink backend \[ [Video](https://youtu.be/9jFXNRzDSf0) \] \[ [Slides](&lt;slides/TechnicalTalks-May10/04-Granitz-ExtendingtheAArch32 -JITLinkBackend.pdf&gt;) \]  
*Stefan Gränitz, echtzeit.dev*  

Practical advice on llvm-jitlink-executor, JITLink development and debugging of JITed ARM/Thumb code  

Using MLIR to Optimize Basic Linear Algebraic Subprograms \[ [Video](https://youtu.be/x8IIMeFH7sk) \] \[ [Slides](slides/TechnicalTalks-May10/08-Varoumas-UsingMLIR-to-OptimizeBasicLinearAlgebraicSubprograms.pdf) \]  
*Steven Varoumas, Huawei Technologies Research & Development*  

The powerful framework provided by MLIR has the potential to allow library developers to express and optimize standard linear algebra functions without having to write daunting assembly code. In this presentation, we will describe how we have leveraged and extended the capabilities of MLIR to generate an optimized subset of BLAS functions, with performance comparable to hand-written assembly implementations.  

Buddy Compiler: An MLIR-based Compilation Framework for Deep Learning Co-design \[ [Video](https://youtu.be/EELBpBA-XCE) \] \[ [Slides](&lt;slides/TechnicalTalks-May10/09-Zhang-Buddy Compiler_An MLIR-BasedCompilationFramework-for-DeepLearningCo-Design.pdf&gt;) \]  
*Hongbin Zhang, Institute of Software Chinese Academy of Sciences*  

Buddy Compiler is a compiler framework for software and hardware co-design. We are committed to building an extensible co-design ecosystem based on MLIR and RISC-V. This talk will share our co-design process in deep learning inference, including preprocessing, optimization, and backend support. Furthermore, we will also present our plans and current progress on DSL (Domain-Specific Language) to DSA (Domain-Specific Architecture) co-design.  

MachineScheduler - fine grain resource allocation using resource intervals \[ [Video](https://youtu.be/XWBVLcdzmFg) \] \[ [Slides](slides/TechnicalTalks-May11/03-Petrogalli-StartAtCycle.pdf) \]  
*Francesco Petrogalli, Apple*  

In this talk we will describe an optimisation introduced in the MachineScheduler that allows to allocate more resources in a smaller number of cycles. To achieve this, we introduced the concept of resource interval and look for empty slots when tracking resource usage at a schedule boundary.  

Inliner in MLIR \[ [Video](https://youtu.be/Ldxu8MJZY-I) \] \[ [Slides](slides/TechnicalTalks-May11/10-Absar-Inliner_in_MLIR.pdf) \]  
*Javed Absar, Qualcomm*  

We give an overview of the Inliner in MLIR. The Inliner strikes a balance by defining interfaces that define the expectations and can handle recursive functions using a history-based scheme. This talk will cover Inlining in MLIR, and touch upon optimizations in general in MLIR.  

How to use llvm-debuginfo-analyzer tool \[ [Video](https://youtu.be/V8pW0Wr9pSg) \] \[ [Slides](slides/TechnicalTalks-May11/09-Ensico-llvm-debuginfo-analyzer.pdf) \]  
*Carlos Alberto Enciso, SN Systems (Sony Interactive Entertainment)*  

Developed at Sony, llvm-debuginfo-analyzer is a command-line tool added recently to LLVM. This talk will present a more detailed information on how to use the tool, with specific test cases that cover the most common options. In addition, it will enumerate current limitations and future work.  

Practical Global Merge Function with ThinLTO \[ [Video](https://youtu.be/rh2ApiBQQks) \] \[ [Slides](slides/TechnicalTalks-May10/03-Lee-PracticalGlobalMergeFunction-with-ThinLTO.pdf) \]  
*Kyungwoo Lee, Meta*  

Function merging is an important technique for reducing code size by combining identical or similar functions into a single function. This technique has been extensively researched in both industry and academia. However, the existing methodologies have not been evaluated with -Oz, which includes aggressive outlinings, and the linker's identical code folding, which can already fold identical pieces of code. Additionally, none of these methodologies suggest a sound approach that works globally with ThinLTO, which is crucial when building large apps. In this talk, we propose our global merge function (GMF), which utilizes global merge information obtained from a prior codegen run and optimistically creates merging instances within each module context independently. Our evaluation showed that GMF can reduce code size in real-world iOS apps by up to 3.5% on top of state-of-the-art outliners that are fully enabled with ThinLTO.  

Prototyping MLIR in Python \[ [Video](https://youtu.be/YJIKr1DoUCQ) \] \[ [Slides](slides/TechnicalTalks-May11/05-Fehr-PrototypeMLIRinPython.pdf) \]  
*Sasha Lopoukhine, University of Edinburgh & Mathieu Fehr, University of Edinburgh*  

We present xDSL, a reimplementation of MLIR core features in pure Python with a focus on accessibility. xDSL aims at bridging the Python DSL community with the MLIR one, by being fully compatible with MLIR through the textual format. Dialects can as well be translated from one framework to the other through IRDL. Since xDSL is written in pure Python, it lowers the barrier of entry for newcomers, and allows them to learn about MLIR concepts without having the struggle of installing MLIR, and can even do so directly on a Jupyter notebook hosted on the web. It is also a good option for prototyping dialects, since no recompilation is required in between changes, resulting in faster iteration time.  

What would it take to remove debug intrinsics? \[ [Video](https://youtu.be/fZgFTOuhEzc) \] \[ [Slides](slides/TechnicalTalks-May11/08-Morse-RemoveDebugIntrinsics.pdf) \]  
*Jeremy Morse, SN Systems (Sony Interactive Entertainment)*  

It is a truth universally acknowledged that representing LLVMs debug-info with intrinsics is a poor design, slowing compile-time performance and creating new categories of bugs. However, removing them is not easy as our APIs lack a way of describing instruction positions from outside of the instruction list. In this talk I'll illustrate what's bad about the current design and explore the design space of possible solutions. I'll also suggest what information a new instruction-movement API would need to maintain debug-info if we didn't use intrinsics. Having a more precise API for describing instruction movement will ease the work of pass authors in getting debug-info correct, and rid optimisation passes of many footguns.  

Compiling Ruby (with MLIR) \[ [Video](https://youtu.be/NfMX-dFMSr0) \] \[ [Slides](slides/TechnicalTalks-May11/06-Denisov-CompilingRubyWithMLIR.pdf) \]  
*Alex Denisov*  

Ever wondered how to build an ahead-of-time (AOT) compiler for a dynamic, interpreted language? Then this talk is a good starting point. In this presentation, you'll learn how a typical interpreter works, how to map it onto an intermediate representation (MLIR in this case), and how to produce an executable at the end of the compilation pipeline. By the end of this talk, we hope to inspire you to take on the challenge of building a compiler for your favorite interpreted language.  

What’s new in MLIR? \[ [Video](https://youtu.be/LPlRLt9w4b0) \] \[ Slides \]  
*Mehdi Amini*  

MLIR has evolved significantly since it was introduced at EuroLLVM 2019. The last tutorial was at the US Dev Mtg in 2020. In this talk, we'll survey new components and provide a quick intro into how to take advantage of the new MLIR features from the last two years.  

Structured Bindings and How to Analyze Them \[ [Video](https://youtu.be/ZPcf7w-Tk3Y) \] \[ [Slides](slides/TechnicalTalks-May11/02-Domjan-StructuredBindingsCombined.pdf) \]  
*Domján Dániel, Company*  

A deeper dive into how structured bindings are handled inside the Clang Static Analyzer. The process involves multiple parts of the analyzer throughout the static analysis pipeline. This speech will give an insight into all the steps and tricks used in the implementation.  

MLIR Dialect Design and Composition for Front-End Compilers \[ [Video](https://youtu.be/hIt6J1_E21c) \] \[ Slides \]  
*Jeff Niu, Modular*  

MLIR dialect design is often more an art than a science. MLIR provides powerful infrastructure for building IR and a vast ecosystem of dialects to use, but lacks guidelines on how to actually do so. This talk is a deep dive on principles for MLIR dialect design and composition. We will focus on criteria for dialect design, such as concise and powerful representation and transparent composability, dialect design principles and techniques, such as preserving high-level information and distinguishing between “structural” and “computation” dialects, and challenges with integrating with upstream dialects. We will study how good dialect design allows us efficiently and easily write powerful optimizations on our IR and how to write generic IR transformations with MLIR interfaces. We will present our findings through the lens of building a general-purpose programming language with MLIR.  

ML-LLVM-Tools: Towards Seamless Integration of Machine Learning in Compiler Optimizations \[ [Video](https://youtu.be/3RYPv27Tp6s) \] \[ [Slides](slides/TechnicalTalks-May10/10-Venkat-ML-LLVM-Tools.pdf) \]  
*S. VenkataKeerthy, IIT Hyderabad*  

With the growth in usage of Machine Learning (ML) to support compiler optimization decisions, there is a need for robust tools to support both training and inference. Such tools should be scalable and independent of the underlying model, and the ML framework upon which the model is built. We propose a unified infrastructure to aid ML based compiler optimizations in LLVM at each of training and inference stages by using: (1) LLVM-gRPC, a gRPC based framework to support training, (2) LLVM-InferenceEngine, a novel ONNX based infrastructure to support ML inference within LLVM. Our infrastructure allows seamless integration of both the approaches with ML based compiler optimization passes. When our LLVM-InferenceEngine is integrated with a recently proposed approach that uses Reinforcement Learning for performing Register Allocation, it results in a 12.5x speedup in compile time.  

Optimizing the Linux Kernel with LLVM BOLT \[ [Video](https://youtu.be/ivTCCTSMGZg) \] \[ [Slides](&lt;slides/TechnicalTalks-May10/11-Panchenko-Optimizing-the-LinuxKernel-with-LLVM BOLT.pdf&gt;) \]  
*Maksim Panchenko, Meta*  

This technical talk explores the challenges and benefits of applying LLVM BOLT optimizations to the Linux Kernel, given its unique binary structure and compiled code. Early performance results are shared, and attendees gain insights into kernel-specific code patterns and improvements that can be achieved with post-link optimizations.  

mlir-meminfo : A Memory Model for MLIR \[ [Video](https://youtu.be/7p3Vg3yZ29s) \] \[ Slides \]  
*Kunwar Grover, IIIT Hyderabad & Arjun Pitchanathan, University of Edinburgh*  

A number of transformations in high-level MLIR dialects like Linalg, SCF and Affine focus on building transformations for optimizing the cache behavior of programs. While building models for the cost of computation for these transformations are easy as it is a local property, data movement on cached architectures depends on the global state and is very hard to predict. Current approaches for memory models for these transformations use transformation-specific cost models, which do not compose from one transformation to another due to the global properties of data movement. We introduce mlir-meminfo, a lightweight, analytical memory model for MLIR. mlir-meminfo accurately predicts the cache behavior of a program, with a particular focus on transformations, updating the cache information almost instantly for modern neural networks like BERT, containing hundreds of memory accesses. With the introduction of mlir-meminfo, we aim to revolutionize transformation memory models for MLIR and improve developer productivity for performance programming.  

**Tutorials**

Developing BOLT pass \[ [Video](https://youtu.be/kPKPkg5ugMg) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Tutorial-May10/02-Ayupov-BOLTPass.pdf) \]  
*Amir Ayupov, Meta*  

The tutorial covering the basics of BOLT pass development and debugging techniques, with examples of adding a simple peephole rule and a standalone pass. Debugging examples cover narrowing down a misoptimized function, producing an assembly test and visualizing the CFG.  

A whirlwind tour of the LLVM optimizer \[ [Video](https://youtu.be/7GHXDEIMGIY) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Tutorial-May10/01-Popov-AWhirlwindTour-oftheLLVMOptimizer.pdf) \]  
*Nikita Popov, Red Hat*  

This is a tour of LLVM's optimization pipeline: It provides an overview of all important optimization passes and analyses, as well as how they work together and fit into the overall optimization pipeline.  

Tutorial: Controllable Transformations in MLIR \[ [Video](https://youtu.be/P4gUj3QtH_Y) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Tutorial-May11/02-Zinenko-TransformDialectTutorial.pdf) \]  
*Alex Zinenko, Google*  

MLIR has recently introduced support for declaratively specifying and controlling compiler transformations via the transform dialect. It allows one to request compiler transformations using compiler IR itself, which can be embedded into the original IR that is being transformed (similarly to pragmas) or supplied separately (similarly to scheduling languages). This tutorial presents the concepts of the MLIR transform dialect and related infrastructure. It will be accompanied by a practical demonstration of three use scenarios.

*   Composing transform dialect operations available in (upstream) MLIR to perform a sequence of optimizing transformations that results in efficient code for an MLIR linear algebra operation.
*   Defining new transform dialect operations and adapting existing transformation code to work with the transform dialect infrastructure.
*   Setting up and using the transform dialect infrastructure in a downstream out-of-tree project with custom dialects, transformations and passes.

After following the tutorial, the attendees will be able to apply the transform dialect in their work and extend it when necessary. Basic familiarity with MLIR is a prerequisite.  

GlobalISel by example \[ [Video](https://youtu.be/PEP0DfAT_N8) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Tutorial-May11/01-Bradbury-GlobalISelTutorial.pdf) \]  
*Alex Bradbury, Igalia*  

The GlobalISel framework was introduced with the intention of replacing SelectionDAG, aiming to provide advantages in terms of performance, granularity, and modularity. This tutorial will provide everything you need to know about using this framework for a new target, focusing on RISC-V as an example and working through some specific examples of challenging cases.  

**Quick Talks**

Iterative Compilation - Give the compiler a second chance \[ [Video](https://youtu.be/XMuS2PGyWms) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May10/06-Zion-Iterative%20Compilation%20-%20EuroLLVM.pdf) \]  
*Ziv Ben Zion, Mobileye*  

Compiler heuristics play a crucial role in improving the performance of generated code. Revisiting some of the decisions taken by the compiler is possible using different compilation flags, and can sometimes overcome wrong compiler decisions. This talk introduces a different approach, where the compiler itself triggers new compiler runs with different heuristics. I will briefly outline how we implemented this new approach in our LLVM-based compiler.  

Another level of indirection - Compiler Fallback of load/store into gather/scatter enhance compiler robustness by overcoming analysis and hardware limitations \[ [Video](https://youtu.be/85VX3CQTFt8) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May11/06%20-Aviram-PDF%20EuroLLVM%20presentation%20-%20Fallback.pdf) \]  
*Omer Aviram, Mobileye*  

I'll introduce a recently developed LLVM-IR utility that can improve compilers robustness, by converting ("fallback") memory accesses (load/store) with a constant stride, into indirect accesses (scatter/gather); Discuss interesting cost decisions raised by such transformations; as well as the technical challenges faced in transforming load/store instructions with a single pointer into gather/scatter instructions with a vector of pointers.  

Switch per function in LLVM \[ [Video](https://youtu.be/-cPmbtw9dlQ) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May11/05-Schneider-SwitchPerFunction_FINAL.pdf) \]  
*Tomer Nissim Schneider, CEVA*  

At CEVA, we have found that more optimizations and compiler hints are extremely essential for optimizing code of our customers.​ We added support for clang switches as function attributes.  

Tensor Evolution - An ML Graph Optimization Technique \[ [Video](https://youtu.be/T1yPnrVgISo) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May10/03-Absar-Tensor_Evolution_Final_Slides.pdf) \]  
*Javed Absar, Qualcomm & Muthu Baskaran, Qualcomm*  

We present ‘Tensor Evolution (TEV)’, a new analysis for tensors such as those found in loops of ML Graphs. It is an extension of the well-known Scalar Evolution (SCEV) for tensors and tensor expressions. In an ML Graph, tensors can be added, multiplied, sliced, reshaped, and concatenated. We describe how each of these tensor-ops could be handled to generate TEV-expressions and rewrite rules. TEV is an analysis that enables optimizations such as loop-invariant code motion.  

ML-on-CPU: should vectorization happen in the LLVM backend or higher up the stack? \[ [Video](https://youtu.be/hyi1rtSHI6g) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May10/02-Kalda-euroLLVM_ML_on_CPU.pdf) \]  
*Elen Kalda, Arm*  

This talk is about how TVM, one of the most mature machine learning compilation stacks in ML space, interacts with LLVM. TVM is a domain specific compiler that consumes a machine learning model expressed in high level ML framework like TensorFlow or PyTorch and compiles it for a chosen target, such as Arm(R) architecture. For CPU targets, it does this by using LLVM as a backend, directly translating TVM's IR into LLVM IR.  

In TVM, just like in other Machine Learning stacks using LLVM as a backend for CPU code generation, one needs to make a decision about where optimizations like vectorization should happen: in the LLVM backend, or in the ML stack higher up. This is further complicated by the emergence of scalable vectors, like the Scalable Vector Extension (SVE). While generating code for fixed length vectors can mostly be left to LLVM, there is a case to be made for the presence of variable length vectors in TVM stack, to be able to more effectively use the capabilities of SVE. In this talk, we're going to present our experiences and insights on the trade-offs targeting SVE in the TVM+LLVM stack.  

CORE-V LLVM: Adding eight vendor extensions to standard RISC-V LLVM \[ [Video](https://youtu.be/Sjg6xW6bQuM) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May11/04-Charlie-Keaney-Presentation.pdf) \]  
*Charlie Keaney & Chunyu Liao, Embecosm*  

CORE-V is a family of open source commercially rust RISC-V designs from the Open Hardware Group, with a set of 8 custom instruction set extensions. This talk will look at the practical challenges we have encountered in supporting vendor specific extensions to RISC-V in LLVM. This has been a collaborative project across several organizations on two continents, and with an additional objective of training a new generation of LLVM developers in China and Europe.  

Advanced Bug Reports: Choose Your Own Adventure \[ [Video](https://youtu.be/XAXFimqCCwI) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May11/03%20-arseniy-zaostrovnykh-path-sensitive-bug-reports-choose-your-own-adventure-slides.pdf) \]  
*Arseniy Zaostrovnykh, SonarSource SA*  

Finding actual bugs using the Clang Static Analyzer (CSA) is only half of the story. Getting bugs fixed also requires convincing developers that those bugs are real. Traditional bug reports, however, are typically either too short and miss important details, or too long such that they overwhelm developers with information. This talk presents a novel approach to make CSA-bug-reports interactive to confront developers with exactly the amount of information they need to understand and confirm a bug.  

Multiple-Entry, Multiple-Exit MLIR Regions \[ [Video](https://youtu.be/TM-97iiozDY) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May10/01%20-Multiple-Exit%20MLIR%20Blocks-EuroLLVM%202023.pdf) \]  
*Jeff Niu, Modular*  

MLIR regions provide a natural representation of structured control-flow found in many applications, with implicit SSA value captures and automatic memory scopes, but they have been limited to single-entry, single-exit regions. In this talk, we present a new MLIR region-based control-flow representation for single-entry, multiple-exit regions and how this provides a faithful IR model of control-flow in source languages. We also integrated LLVM coroutine intrinsics in our compiler, and we will discuss how they interact with our control-flow representation and how the latter enables trivial implementations of coroutine frame optimizations.  

Target-Independent Integer Arithmetic \[ [Video](https://youtu.be/PBA_iHGc6Zg) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May11/01%20-Target-Independent%20Integer%20Arithmetic.pdf) \]  
*Jeff Niu, Modular*  

How can you fold address arithmetic without knowing the maximum machine integer size? How about C integer types with variable widths? What about range analysis? Folding target-independent IR is important in producing target-agnostic serialization, where introducing a target can cause invalid arithmetic semantics. This talk will present a formulation for target-independent integer arithmetic, its limitations, and how it was implemented in MLIR.  

Improving Vectorization for Loops with Control Flow \[ [Video](https://youtu.be/mKG0NmGtpbE) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May10/05-EuroLLVM23%20-%20Improving%20Vectorization%20for%20Loops%20with%20Control%20Flow.pdf) \]  
*Ashutosh Nema, AMD*  

Auto-vectorization is an essential compiler optimization. In the presence of control flow, it gets challenging. We introduce the implementation of Branch-On-Super-Word-Conditional-Codes (BOSCC) way of vectorization in the presence of conditional statements. BOSCC introduces a branch instruction that can be conditionally taken based on the comparison result of two vector variables. BOSCC encloses the vector instructions guarded by vector predicate inside an if-statement.  

How to run the LLVM-Test Suite on GPUs and what you’ll find \[ [Video](https://youtu.be/_IYG_aMjsfs) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May11/02%20-EuroLLVM%2023%20-%20LLVM%20TS%20on%20GPU.pdf) \]  
*Johannes Doerfert, LLNL*  

Running codes on GPUs is nowadays pretty easy. However, testing GPU compilation on a large, well-understood selection of codes is not. We present an automated approach that allows running (most) existing codes on the GPU in order to test the optimizations and backends. We present our findings from running (most of) the LLVM Test Suite on modern GPUs and show how we combine existing functionality to create concise GPU reducers for bugs.  

OpenMP as GPU Kernel Language \[ [Video](https://youtu.be/16cedvl2Ly4) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/QuickTalks-May10/04%20-%20EuroLLVM%2023%20-%20OpenMP%20Kernel%20Language.pdf) \]  
*Johannes Doerfert, LLNL*  

In this talk, we discuss the use of OpenMP as a kernel language (think CUDA or HIP). While OpenMP comes with offloading capabilities, the execution model was different and generally associated with overheads. Further, the user did not have the same level of control, at least not without target-specific builtins. With our new OpenMP extensions, we can match native CUDA (and HIP) codes while retaining the portability of OpenMP as well as interoperability with the existing capabilities.  

**Lightning Talks**

LLVM IR as an Embedded Domain-Specific Language \[ Video \] \[ Slides \]  
*Nikita Baksalyar*  

This lightning talk will demonstrate an alternative way of using the LLVM API. We will develop a simple domain-specific language using metaprogramming techniques and see how it simplifies code and reduces boilerplate.  

Using MLIR for Dalvik Bytecode Analysis \[ [Video](https://youtu.be/hfqOivYdD40) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Lightning-Talks/01-Eduardo-EuroLLVM2023.pdf) \]  
*Eduardo Blázquez, University Carlos III of Madrid*  

Using intermediate representations allows analysts to write optimizations and code analysis passes easier than parsing binary or bytecode directly. Kunai is a library intended for static analysis of dalvik bytecode, in a newer version of the library, the idea is to use the capabilities and possibilities offered by MLIR, writing a new dialect centered on Dalvik instructions.  

Spot the Difference with LLVM-FLOW: an open-source interactive visualization tool for comparing IR CFGs \[ [Video](https://youtu.be/bCwteA-9mSs) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Lightning-Talks/08-Lee-LLVMFlow.pdf) \]  
*Jinmyoung Lee, KC Machine Learning Lab*  

One way to understand and debug IR optimization process is to visualize Control Flow Graphs (CFGs) before and after optimization and compare them. However, since the CFGs can be drastically different, comparing these two graphs is a challenging task. LLVM-FLOW (https://llvmflow.kc-ml2.com/), an open-source interactive CFG visualization web app, is developed to ease the difficulty by highlighting the same components in two graphs. By clicking the highlighted node, you can easily find the corresponding node in another graph. LLVM-FLOW is a useful tool for LLVM experts to understand the IR flow when writing a custom pass, as well as for LLVM newcomers to study the IR pattern's behavior.  

Leveraging MLIR for Better SYCL Compilation \[ [Video](https://youtu.be/UOOPFpojGN8) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Lightning-Talks/02-Lomuller-SYCL-MLIR.pdf) \]  
*Victor Lomüller, Codeplay Software*  

SYCL is an open standard programming model for heterogeneous device programming, based on C++. Similar to optimizing C++ compilers, SYCL compilers would therefore also profit from a more suitable high-level representation for optimization. This talk presents first results on our investigation on how MLIR can be leveraged to improve SYCL compilation flows and optimizations.  

Arm/AArch64 Embedded Development with LLD : What’s New \[ [Video](https://youtu.be/cJCr4XqFmFY) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Lightning-Talks/03-Amilendra-Arm-AArch64-EmbeddedDevelopment-with-LLD.pdf) \]  
*Amilendra Kodithuwakku, Arm Limited*  

Arm Limited has been continuously adding LLD support for embedded development on Arm/AArch64 targets. This lightning talk will be a short explanation of recently added features. 1) Armv8-M Security Extensions, also known as, Cortex-M Security Extensions (CMSE) 2) AArch64 Big Endian Support  

Using automated tests to tune the -Og pipeline \[ [Video](https://youtu.be/f1uHy-ukucc) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Lightning-Talks/04-Tozer-UsingAutomatedTestsToTuneOgSlides.pdf) \]  
*Stephen Livermore-Tozer, SN Systems (Sony Interactive Entertainment)*  

In clang, the -Og flag is intended to run optimizations that will not significantly reduce the quality of the program's debug information. Rather than making informed decisions about which optimizations will preserve debug info, this flag currently uses the -O1 pipeline, to run a few optimizations and hope that debug info will not be significantly affected. This is due to the lack of useful data about how well the various optimization passes in LLVM preserve debug info. In this talk I explain how we at Sony have attempted to solve this problem using Dexter, a tool for testing debug info quality, in an automated test pipeline to empirically explore different pipeline designs to find a fast and debuggable -Og pipeline.  

Buddy-CAAS: Compiler As A Service for MLIR \[ [Video](https://youtu.be/f7USv-oAtvI) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Lightning-Talks/05-Zhang-Buddy-CAAS-CompilerAs-AService-forMLIR.pdf) \]  
*Hongbin Zhang, Institute of Software Chinese Academy of Sciences*  

This talk will introduce the Buddy-CAAS, Buddy Compiler As A Service for MLIR. In practice, debugging and configuring an MLIR pass pipeline is always time-consuming, and there are no good aid tools. In order to improve the efficiency of compiler developers, we implemented an online platform called Buddy-CAAS (https://buddy.isrc.ac.cn/). Our platform allows MLIR developers to configure the pass pipeline, view the intermediate products, and execute on a specific backend through an emulator. We are also integrating more features on our platform to power the MLIR ecosystem.  

llvm-buildmark - observations, tips, and tricks on reducing LLVM build times \[ [Video](https://youtu.be/ka1wehtGQ-4) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Lightning-Talks/06-Bradbury-llvm-buildmark.pdf) \]  
*Alex Bradbury, Igalia*  

This talk provides a series of statistics on LLVM build times (both incremental and in a simulation of common edit-compile-test cycles) using a simple script that aims to provide a common baseline statistic. We'll look at some figures across real-world hardware, how LLVM build performance has changed over time, and the impact of various options (e.g. -DBUILD\_SHARED\_LIBS=True, -DLLVM\_USE\_SPLIT\_DWARF=True, GCC vs Clang, lld vs ld.{bfd,gold} and so on).  

Lock Coarsening optimizations for loops in Java \[ [Video](https://youtu.be/IpGqTq8cVKw) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/Lightning-Talks/07-Thomas-LockOpts.pdf) \]  
*Anna Thomas, Azul Systems*  

This talk will focus on lock optimizations done for loops in Java by Falcon, Azul’s LLVM based JIT compiler. Synchronization is one the basic techniques that guarantee correctness in parallel execution. This is implemented using monitors in Java. Monitor acquires are expensive CPU operations, which also block various loop and reordering compiler optimizations. We will talk about two specific loop optimizations done for lock coarsening and the benefits it brings. For both these techniques, we introduced loop chunking in LLVM as a mechanism to coarsen locks over. We will go over the legality and cost model aspects as well.  

**Student Technical Talks**

Cost Modelling for Register Allocation and Beyond \[ [Video](https://youtu.be/1yWCbYlcdd4) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/StudentTalks-May10/03-Grossman-cost-modelling.pdf) \]  
*Aiden Grossman, University of California, Davis*  

Accurate and fast cost modeling is essential for training ML models to replace certain key heuristics within LLVM when looking for performance gains. For eviction in the LLVM greedy register allocator, we use a linear model with some domain specific features which has successfully trained highly performant ML replacements, but leaves a lot to be desired in terms of absolute accuracy. In this talk we present results on the application of more generic basic block specific cost models to this problem as well as future directions and current work to push accurate cost modeling beyond basic blocks for the application of training ML models.  

A Template-Based Code Generation Approach for MLIR \[ [Video](https://youtu.be/0z1uEgVwfDo) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/StudentTalks-May11/01-Florian-TemplatedBasedCodeGenerationApproach-for-MLIR.pdf) \]  
*Florian Drescher, Technical University of Munich (TUM)*  

In the talk, we introduce a template-based compilation approach for MLIR dialects. It derives code templates ahead-of-time for MLIR instructions using the already implemented lowerings. During run-time compilation of a program, it stitches together the created templates and patches missing constants to quickly derive native. We apply our compiler on database queries (LingoDB) as well as ONNX models and achieve compile-time speed-ups between 60x and 1000x at the cost of slower execution by the factor two to three compared to the existing LLVM compilation back-end. In this presentation, we describe our approach for fast, template-based compilation and outline our vision on how to improve on the idea and establish template-based compilation as a new code generation approach for MLIR as an alternative to the currently used LLVM back-end.  

MLIR Query Tool for easier exploration of the IR \[ [Video](https://youtu.be/3ELHZARBmYs) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/StudentTalks-May11/04-Sreeramaswamy-MLIRQueryTool.pdf) \]  
*Devajith Valaparambil Sreeramaswamy*  

This talk will introduce mlir-query, a query language tool designed to simplify the exploration of the Intermediate Representation (IR) of code in MLIR. mlir-query aims to provide a more efficient means of understanding and debugging the IR, which can be challenging without a query language. The presentation will showcase the tool's basic queries, such as operation, hasName, resultOf, and constant queries, along with a demo of its usefulness.  

mlirSynth: Synthesis of Domain-Specific Programs in MLIR \[ [Video](https://youtu.be/Ak24vvCatkc) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/StudentTalks-May11/03-Brauckmann-mlirSynth.pdf) \]  
*Alexander Brauckmann, University of Edinburgh*  

mlirSynth is a tool that automatically raises programs to high-level MLIR dialects, using MLIR's dialect definitions, instead of relying on manually-defined rules that are difficult to maintain. Our experiments show that mlirSynth achieves higher coverage than existing rule-based approaches on the PolyBench benchmark and enables high performance through domain-specific compilation.  

Image Processing Ops as first class citizens in MLIR: write once, vectorise everywhere! \[ [Video](https://youtu.be/0xQ2lDY9RCw) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/StudentTalks-May10/04-Tagore-ImageProcessingOp.pdf) \]  
*Prathamesh Tagore, Veermata Jijabai Technological Institute*  

We present an MLIR dialect for Image Processing named Digital Image Processing (DIP). DIP dialect solves the problem of dependence on external tools and libraries for image pre-processing in deep learning models at the MLIR IR level. This dialect is capable of processing an image input at the IR level in the form of memrefs. We utilise MLIR’s vector dialect abstraction to generate optimal vectorisable code using a single lowering pipeline for different architectures. Additionally, we also present these operations in the form a C++ library for their higher level use. As of now, the DIP dialect supports 1D as well as 2D convolutions, resizing, rotation, FFT, IFFT and morphological transformations for images.  

Using the Clang data-flow framework for null-pointer analysis \[ [Video](https://youtu.be/TPEQ3vg16iA) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/StudentTalks-May10/02-Cesh-Dataflow_RC1_finalized.pdf) \]  
*Viktor Cseh, Eötvös Loránd University*  

In late 2021 a new data-flow analysis framework was introduced into the Clang analysis tooling, enabling reasoning about program states the symbolic execution engine of the Clang Static Analyzer had difficulty deducing. In this talk, we summarize our experience with the data-flow framework through the lens of implementing a Clang-Tidy checker using null-pointer analysis. We discuss various approaches we tested to encode pointer values within the framework, their performance and limitations, and best practices and common pitfalls we encountered while implementing checkers using the framework.  

Fast pivot Function for MLIR’s Presburger Library Through Vectorization and Integer Arithmetic in FPU \[ [Video](https://youtu.be/-TQAy6WWBJ0) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/StudentTalks-May10/01-Zhou-pivotfpu.pdf) \]  
*Qi Zhou*  

This talk presents a fast implementation of the core function pivot for the Presburger library in MLIR by performing vectorized integer arithmetics in FPU. The hot loop of the pivot function performs overflow-checked multiplication and addition on each element of an input matrix of low dimension and mostly small-value items. MLIR’s upstream uses element-wise transprecision computing, where the data type of each element starts with int64\_t and will be switched to LargeInteger in case of overflow. Compilers cannot automatically vectorize this approach, and int64\_t has a much larger bit width than what is typically needed for most items in the matrix. Additionally, extra arithmetics are required to perform overflow checking for integers, resulting in significant overhead. These issues can be addressed by taking advantage of SIMD and reducing the bit width for every element. This report also introduces the int24\_t data type, a 24-bit integer data type created from the sign bit, plus the 23-bit mantissa of a 32-bit floating point. int24\_t overflow can be captured as floating point imprecision by a status register, making overflow awareness almost free. On a representative 30-row by 19-column input matrix, the runtime is reduced from 550 ns to 26 ns, achieving 20 times speedup.  

RISC-V Vector Extension Support in MLIR: Motivation, Abstraction, and Application \[ [Video](https://youtu.be/i9dsjzVOvy8) \] \[ [Slides](https://llvm.org/devmtg/2023-05/slides/StudentTalks-May11/02-Zhang-RISC-V-VectorExtensionSupport-in-MLIR.pdf) \]  
*Hongbin Zhang, Institute of Software Chinese Academy of Sciences*  

This talk will share our work on supporting the RISC-V Vector (RVV) extension in MLIR. The RVV extension provides high-performance vector instructions, and the parallelism model is different from other SIMD architectures. However, MLIR vector abstractions cannot support some RVV features, especially the dynamic vector length and register group configuration. To address this issue, we add custom MLIR abstractions to support RVV parallelism model, and our design balances generic and specialized parts to avoid introducing fragmentation. As a demonstration case, we use our abstractions to implement a vectorization optimization for the matrix multiplication operation.  

**Posters**

Automatic Translation of C++ to Rust \[ [Poster](https://llvm.org/devmtg/2023-05/slides/Posters/02-Preto-AutomaticTranslationCPlusPlus-Rust.pdf) \]  
*Henrique Preto, ULisboa - Instituto Superior Técnico*  

Memory safety bugs account for 70% of the security vulnerabilities found in major Microsoft and Google projects. C++, while not memory safe, is an efficient language commonly used to implement critical systems software. However, Rust is a memory-safe programming language that offers comparable performance to C++. Still, manually rewriting existing C++ codebases in Rust is not practical. This work presents a source-to-source compiler built with Clang that translates C++ code to safe Rust, automatically making the software safer without losing performance and efficiency.  

A sustainable approach to have vector predication in the Loop Vectorizer \[ [Poster](https://llvm.org/devmtg/2023-05/slides/Posters/01-Albano-VectorPredictionPoster.pdf) \]  
*Lorenzo Albano, Barcelona Supercomputing Center*  

A number of vector ISAs, like the RISC-V Vector Extension, have support for vector length and predication. Vector Predication provides us intrinscis to express operations that map well to these ISAs. However, the Loop Vectorizer still does not make use of them. At BSC we extended the Loop Vectorizer so it can use Vector Predication intrinsics but the amount of duplication makes us reluctant to upstream it. In this poster we present an alternative that has less impact to the Loop Vectorizer and a new pass that propagates the vector length and mask to the vectorised code.  

Performance Analysis of Undefined Behavior Optimizations \[ [Poster](https://llvm.org/devmtg/2023-05/slides/Posters/05-Popescu-PerformanceImpactOfExploitingUndefinedBehavior.pdf) \]  
*Lucian Popescu, Politehnica University of Bucharest*  

State-of-the-art compilers, such as Clang/LLVM, use undefined behavior (UB) to issue optimizations. We present the impact of UB optimizations for a diverse set of application categories to discover what are UBs that are most performance critical.  

Static Analysis for C++ Rust-Like Lifetime Annotations \[ [Poster](https://llvm.org/devmtg/2023-05/slides/Posters/06-Monteiro-StaticAnalysisForCPlusPlus-Rust-Like-LifetimeAnnotations.pdf) \]  
*Susana Monteiro, INESC-ID, IST ULisboa*  

Memory safety vulnerabilities can be addressed by incrementally migrating from memory-unsafe languages like C++ to memory-safe languages, namely Rust. However, this involves some challenges, in particular regarding Rust’s concept of lifetimes, which does not exist in C++. Recently, Clang introduced Rust-like lifetime annotations to approach this challenge, but it is essential to ensure their correctness. Our work focuses on developing a static analyzer to verify the correctness of C++ lifetime annotations, consequently addressing memory-safety vulnerabilities.  

Leveraging MLIR for Better SYCL Compilation \[ [Poster](https://llvm.org/devmtg/2023-05/slides/Posters/04-Lomuller-LeveragingMLIR-forBetterSYCLCompilation.pdf) \]  
*Victor Lomüller, Codeplay Software*  

SYCL is an open standard programming model for heterogeneous device programming, based on C++. Similar to optimizing C++ compilers, SYCL compilers would therefore also profit from a more suitable high-level representation for optimization. This poster presents first results on our investigation on how MLIR can be leveraged to improve SYCL compilation flows and optimizations.  

Forcefully Embedding MLIR into Python \[ [Poster](https://llvm.org/devmtg/2023-05/slides/Posters/03-Mitenkov-ForcefullyEmbedding%20MLIR-intoPython.pdf) \]  
*George Mitenkov, ETH Zurich*  

While MLIR provides its users with the infrastructure to create new dialects, lowerings and rewrites to support efficient domain-specific and ML workload compilation, the front-ends that generate MLIR have not been fully explored. In particular, it is common to either write SSA-based MLIR code in high-level dialects, or re-implement the code generation flow from the source language to MLIR. Both approaches are not developer-friendly because they require maintenance and significant development effort. In this poster session, we present how MLIR can be embedded into Python, allowing one to generate non-SSA Pythonic front-ends based on the dialect specifications. Moreover, we discuss how the front-ends can be statically compiled to SSA-based MLIR or even dynamically executed. We evaluate our work by presenting examples of front-ends for zero-knowledge proof or RISC-V compilers.  

# Code of Conduct

The LLVM Foundation is dedicated to providing an inclusive and safe experience for everyone. We do not tolerate harassment of participants in any form. By registering for this event, we expect you to have read and agree to the [LLVM Code of Conduct](http://llvm.org/docs/CodeOfConduct.html).

# Contact

To contact the organizer, [email eurollvm@llvm.orgr](mailto:eurollvm@llvm.org)

<!-- *********************************************************************** --> <!--#include virtual="sponsors.incl" -->

* * *

<!--#include virtual="../../footer.incl" -->

1.  [About](#about)
2.  [Program](#program)
3.  [Code of Conduct](#coc)
4.  [Contact](#contact)

*   **Conference Dates**: May 10-11, 2023
*   **Location**: [DoubleTree By Hilton, Glasgow, Scotland](https://www.hilton.com/en/hotels/glagwdi-doubletree-glasgow-central/)
*   [**Event Site**](https://llvm.swoogo.com/2023eurollvm/)

</div>

</div>
