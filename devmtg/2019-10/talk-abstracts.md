---
layout: "default.html"
permalink: "devmtg/2019-10/talk-abstracts.html"
---
# 2019 Bay Area LLVM Developers' Meeting - Talk Abstracts

<div style="float: left; width: 68%">

# Program with Talk Abstracts

**Keynote Talks**

*   Generating Optimized Code with GlobalISel  
    *Volkan Keles, Daniel Sanders*

    So far, much of the focus of GlobalISel development has been on supporting targets with minimal optimization work. Recently, attention has turned towards optimization and bringing it to the point where it can take over from SelectionDAGISel. In this talk, we'll mainly focus on the combiner which is a key component of producing optimized code with GlobalISel. We'll talk about the overall design of the combiner, the components that support it, how it fits with the rest of GlobalISel, how to test it, and how to debug it. We'll also talk about the current and future work on the combiner to enhance it beyond SelectionDAGISel’s capabilities.

*   Even Better C++ Performance and Productivity: Enhancing Clang to Support Just-in-Time Compilation of Templates  
    *Hal Finkel*

    Just-in-time (JIT) compilation can take advantage of information only known once an application starts running in order to produce very-high-performance code. LLVM is well known for supporting JIT compilation, and moreover, Clang, LLVM's best-in-class C++ frontend, enables the highly-optimized compilation of C++ code. Clang, however, uses purely an ahead-of-time compilation model, and so we leave on the table performance which might come from dynamic specialization.

    In this talk, I'll describe ClangJIT, an enhancement to Clang, and an extension to the C++ language, which brings JIT-compilation capabilities to the C++ ecosystem. Critically, ClangJIT enables the dynamic, incremental creation of new template instantiations. This can provide important performance benefits, and in addition, can decrease overall application compile times. I'll describe how Clang was enhanced to support this feature - what I needed to do to turn Clang into an incremental C++ compilation library - and how LLVM's JIT infrastructure was leveraged. ClangJIT supports Clang's CUDA mode, and how that works will be described. Some application use cases will be highlighted and I'll discuss some future directions.

**Technical Talks**

*   Using LLVM's portable SIMD with Zig  
    *Shawn Landden*

    While not every application that uses SIMD uses only the portable subset that LLVM provides, writing to LLVM instead of assembly (or , , , et cetera) provides more than multiple platforms. It also allows your app to benifit from a rich library of LLVM optimizations. While the portable SIMD features of C (and Rust) are insufficient to write an application, LLVM provides much more. In addition to exporting the full power of LLVM's SIMD functionality, novel Zig features such as comptime are also provided for vector intrinsics.

    We show that LLVM and Zig enable a new single libmvec implementation, instead of the many currently in use and in development.

*   Code-Generation for the Arm M-profile Vector Extension \[ [Video](https://youtu.be/TUDWpAhLjBU) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Meijer-Parker-CodeGenForTheArmM-ProfileVectorExt.pdf) \]  
    *Sjoerd Meijer, Sam Parker*

    In this talk we share design and implementation details how the code-generation techniques auto-vectorisation, hardware-loops, and predication are combined to enable efficient code-generation for tail-predicated hardware loops that are introduced in Arm's new M-Profile Vector Extension.

*   Alive2: Verifying Existing Optimizations \[ [Video](https://youtu.be/paJhdBp_iA4) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Lopes-Regehr-Alive2.pdf) \]  
    *Nuno Lopes, John Regehr*

    Alive is regularly used to verify InstCombine optimizations. However, it is limited mostly to InstCombine-style optimizations, and it can only verify optimizations written in Alive's own IR-like DSL.

    Alive2 is a re-implementation of Alive that removes several limitations of the previous tool. It supports floating point operations and has better support for memory and loops. It handles optimizations beyond those found in InstCombine. It includes a standalone tool that can prove equivalence / refinement between two bitcode functions as well as an \`opt\` plugin that can prove that an LLVM optimization is correct. Neither of these new tools requires optimizations to be rewritten in the Alive DSL.

    In this talk, we will give an overview on Alive2 and show how you can use it to 1) ensure your optimization is correct, and 2) to find that bug that is triggering a miscompilation.

*   The clang constexpr interpreter \[ [Videos](https://youtu.be/LgrgYD4aibg) \] \[ Slides \]  
    *Nandor Licker*

    Constexpr enables C++ to implement NP-complete solutions in constant time at execution time. In order to ensure that programmers do not grow old while such sources compile, C++ frontends should provide effective constexpr evaluators. In order to improve on the performance of the existing tree-walking evaluator and provide a mechanism which scales as the complexity of constexpr use cases increases, we present an interpreter which we are upstreaming, aimed to completely replace the existing evaluator.

*   Souper-Charging Peepholes with Target Machine Info \[ [Video](https://youtu.be/5eSOWM0upN8) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Hsu-Souper-ChargingPeepholes.pdf) \]  
    *Min-Yih Hsu*

    Souper, a LLVM-based superoptimization framework, has seen adoption in both academic research and industry projects. Given an LLVM IR as an input, Souper tries to generate peephole patterns by synthesizing semantically equivalent but shorter instruction sequences. However, as a platform-independent framework, it lacks a model of the actual cost of an instruction sequence on the target machine. This leads to missing optimizations opportunities or generation of peephole patterns which degrade performance.

    In this talk, we’re going to demonstrate how Souper can benefit from target machine information. Then, we will explore some possible approaches to providing Souper with target machine info to steer the superoptimizer to find more patterns with improvements than regressions. This will enable Souper to be used in a more automated way and reduce the manual intervention required.

*   Transitioning the Networking Software Toolchain to Clang/LLVM \[ [Video](https://youtu.be/0rICCQb_mRg) \] \[ Slides \]  
    *Ivan Baev, Jeremy Stenglein, Bharathi Seshadri*

    In this talk we will share our experience in the journey of transitioning Cisco Enterprise Networking software with a high market share to Clang/LLVM as the primary compiler. For performance and business reasons, our software stack should run on many different processors. We will describe several contributions to the MIPS and PPC backends to make LLVM on parity with gcc compiler for these processors. We will summarize our contributions to debugging optimized code and enabling LLVM on Cisco data plane component where code must be highly optimized with LTO to forward network packets in the correct byte order.

*   Link Time Optimization For Swift \[ [Video](https://youtu.be/Si-fWILpORA) \] \[ Slides \]  
    *Jin Lin*

    The code size of iOS apps is critical due to the size limit of apple store. More and more iOS apps are written in Swift. The Swift programming language provides many new language features such as protocol to facilitate software development. In order to support the implementation of these new features, the existing Swift compiler has to generate the protocol related code and data. However, these generated code and data may not be used in the whole project. For example, some protocol definition is used one module as public and not really consumed by any other modules. Preliminary experiment shows the size of some commercial iOS app can be potentially reduced by 9% through aggressive dead code elimination. Those unused code and data cannot be eliminated easily by the compiler optimizations since they are recorded in llvm.used data structure. In addition, the generated code and data might be implicitly used by Swift runtime library. This calls for a smarter, much more advanced static analysis and novel additions to the classic dead code elimination technique.

    We introduce a novel building pipeline that eliminates the protocol from swift class by leveraging the link time optimization in existing LLVM compiler. In this framework, the swift files are first compiled as LLVM bitcode files and the llvm-link is used to merge all the LLVM bitcode files as one bitcode file. A new LLVM optimization is proposed to eliminate the protocol conformance related variables from the LLVM.used array in this bitcode file. It enables more opportunities for link time optimization to transform global variables into local variables and then identify the dead local variables. The following dead code elimination is extended to update the protocol conformance tables as well as LLVM.used array. The experiment shows that this novel approach reduces the code size of some commercial iOS app by 2%.

*   Hot Cold Splitting Optimization Pass In LLVM \[ [Videos](https://youtu.be/Q8rqGg6vHAE) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Kumar-HotColdSplitting.pdf) \]  
    *Aditya Kumar*

    Hot Cold splitting is an optimization to improve instruction locality. It is used to outline basic blocks which execute less frequently. The hot/cold splitting pass identifies cold basic blocks and moves them into separate functions. The linker can then put newly-created cold functions away from the rest of the program . The idea here is to have these cold pages faulted in relatively infrequently, and to improve the memory locality of code outside of the cold area.

    The algorithm is novel in the sense it is based on region and implemented at the IR level. Because it is implemented at the IR level, all the backend targets benefit from this implementation. Other implementations of hot-cold splitting outline each basic block separately and are implemented at the RTL level.

*   Making UB hurt less: security mitigations through automatic variable initialization  
    *JF Bastien*

    clang recently started supporting automatic variable initialization, where it unconditionally initializes stack variables. It addresses concrete issues in security-related C and C++ applications, and serves as a last-defense guardrail against some stack use-after-free and memory disclosures. We’ll dive into how this removes sharp edges in C-based languages, what optimizations are required to make this option palatable, and what current overheads look like.

*   Propeller: Profile Guided Large Scale Performance Enhancing Relinker \[ [Video](https://youtu.be/DySuXFGmB40) \] \[ Slides \]  
    *Sriraman Tallam*

    We discuss the design of Propeller which is a framework for Post Link Optimizations and we show how Propeller can optimize binaries beyond PGO and ThinLTO via basic block layout.

*   From C++ for OpenCL to C++ for accelerator devices \[ [Video](https://youtu.be/9a5gQ4wJoxs) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Stulova-Haastregt-FromCPlusPlusforOpenCL.pdf) \]  
    *Anastasia Stulova*

    In this talk we will describe the new language mode that has been added into Clang for using functionality of C++17 in the OpenCL kernel language - C++ for OpenCL. As this language mode is fully backwards compatible with OpenCL C 2.0, existing OpenCL applications can gradually switch to using C++ features without any major modifications.

    During the implementation the strategy was chosen to generalize features that exist in a range of accelerator devices to C++. For example, address space support was improved in C++ to be used as a language extension and OpenCL functionality was built on top of it. This was done to take advantage of common logic in some language features among multiple C++ dialects and extensions that are available in Clang.

    At the end of the talk we will describe the future roadmap. Some [documentation](https://clang.llvm.org/docs/LanguageExtensions.html#opencl-features) has been started in Clang. There is also discussion with the Khronos Group about wider adoption of this language mode and possibly more formal documentation to appear in the future. Additionally we would like to highlight our positive experience of community engagement and the help we have received with early testing and feature evaluation from the users of Clang.

*   LLVM-Canon: Shooting for Clear Diffs \[ [Video](https://youtu.be/c9WMijSOEUg) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Paszkowski-LLVMCanon.pdf) \]  
    *Michal Paszkowski*

    Comparing intermediate representation dumps after various transformations can be extremely laborious. This is especially true when reasoning through differences in shaders or compute modules which have undergone several optimization passes. Most of these differences tend to be semantically equivalent and are just a consequence of irregular instruction ordering and naming. In the need to save time we have developed a tool called llvm-canon which transforms the code into a canonical form. Thereby in ideal conditions, canonicalized semantically identical code should result in a clear diff, making important semantic differences stand out.

    The challenges we faced during the development of this project gave us many sleepless nights. Puzzling over the right point of reference for canonicalization, calculating the odds of similarity, and finding the golden mean between precision and being human-friendly resulted in a very useful tool. A tool with broad possibilities for further expansion and improvements.

    In this talk I will go through countless ideas for what is known today as llvm-canon (including ditched ones). Discuss the algorithms behind all the transformations, including instruction reordering and all the magic behind naming values. Yet more importantly I will demonstrate the benefits of diffing canonical code and what we have learned from this interesting experiment.

*   Better C++ debugging using Clang Modules in LLDB  
    *Raphael Isemann*

    Expression evaluators in the C++ debuggers we use today still struggle to consistently support many language features. In this talk we show by using Clang‘s C++ Modules, LLDB can support most of the previously unsupported language features in its expression evaluator.

*   Ownership SSA and Semantic SIL  
    *Michael Gottesman*

    Reference-counted memory management is used by a number of programming languages, including Swift, Python, PHP, Perl, and Objective-C. Reference counting operations are usually introduced as part of lowering to the compiler's IR as, e.g., calls to builtins or library functions, but this approach leads to both missed optimization opportunities (if the presence of these calls inhibit optimizations) and correctness bugs (if optimizations reason about reference-counting incorrectly). In Swift, we have mitigated these problems by changing the Swift Intermediate Language (SIL) to express statically verifiable ownership constraints on def-use chains defining an augmented form of SSA called Ownership SSA (OSSA). OSSA has yielded many benefits such as improved frontend correctness/verification and the implementation of safer, more aggressive reference counting optimizations. The improvements allowed by OSSA may be of interest to other developers of high level languages that use reference counting memory management.

*   arm64e: An ABI for Pointer Authentication  
    *Ahmed Bougacha, John McCall*

    arm64e is a variant of Apple's arm64 ABI which supports pointer authentication using the ARMv8.3 PAC instructions. All code pointers and some data pointers are signed using a cryptographic hash, improving the security of the system by making Return-Oriented Programming and Jump-Oriented Programming attacks harder to carry out. In this talk, we go over the pointer authentication mechanisms, how they're represented at each level in the compiler, and how arm64e takes advantage of them in programming languages.

*   Porting by a 1000 Patches: Bringing Swift to Windows \[ [Video](https://youtu.be/Zjlxa1NIfJc)\] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Abdulrasool-BringingSwiftToWindows.pdf) \]  
    *Saleem Abdulrasool*

    Swift is a modern language based upon the LLVM compiler framework. It takes advantage of Clang to provide seamless interoperability with C/C++. The Swift compiler and language are designed to take advantage of modern Unix facilities to the fullest, and this made porting to Windows a particularly interesting task. This talk covers the story of bringing Swift to Windows from the ground up through an unusual route: cross-compilation on Linux. The talk will cover interesting challenges in porting the Swift compiler, standard library, and core libraries that were overcome in the process of bringing Swift to a platform that challenges the Unix design assumptions.

*   The Penultimate Challange: Constructing bug reports in the Clang Static Analyzer \[ [Video](https://youtu.be/yh2qdnJjizE) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Umann-ThePenultimateChallenge.pdf) \]  
    *Kristóf Umann*

    Static analysis is used to find errors or code smells statically. As the highest cost factor regarding static analysis is the human effort the expert makes evaluating whether a report is a true positive, presenting our findings in an easy-to-understand manner is of the utmost importance.

    This talk will explore the techniques and data structures used by the Clang Static Analyzer to construct bug reports. It will briefly explain the construction of the ExplodedGraph during symbolic execution, and how it will be processed after the analysis. Using a combination of data and control dependency analysis with the help of the inspection of the ExplodedGraph, the analyzer tries to construct user friendly diagnostics. Since symbolic execution is a kind of path sensitive analysis, the idea behind the solution the analyzer employs is general enough to create diagnostics for other kinds of analyses. We will also discuss the challenges the analyzer faces and future development possibilities.

*   Address Spaces in LLVM \[ [Video](https://youtu.be/Oj1BNoL1jpM) \] \[ Slides \]  
    *Matt Arsenault*

    Address spaces have various uses in different languages and targets, but are commonly misunderstood. The rules for address spaces have not always been clear and there are differing interpretations. I will describe features address spaces currently have, rules surrounding casting, aliasing, bit-representation/non-integral pointers, dereferencability and intended uses.

*   An MLIR Dialect for High-Level Optimization of Fortran \[ [Video](https://youtu.be/ff3ngdvUang) \] \[ Slides \]  
    *Eric Schweitz*

    The LLVM-based Flang project is actively developing a standards-compliant compiler for Fortran—the world’s first high-level programming language and still an important language for science and engineering today. While Fortran’s core strength of writing computations on arrays remains, the standard language continues to add new facilities such as object-oriented programming. The Flang project has been exploring the use of MLIR, specifically the definition of Flang’s Fortran IR (FIR) as a framework upon which to build a more comprehensive and regular set of optimizations for both better performance and overall reliability of Flang. This talk will explore what the FIR dialect is, how it is built upon and uses other aspects of MLIR, as well as some of the high-level optimizations achieved.

*   Loop-transformation #pragmas in the front-end \[ [Video](https://youtu.be/RhwjZS9PSI8) \] \[ Slides \]  
    *Michael Kruse*

    Code-transformation directives allow the programmer to specify which trans- formation the compiler should apply and in which order (e.g. tile the loop nest, then parallelize the outermost and vectorize the inner most loop) with- out impacting the source’s maintainability. Currently, Clang only supports the "#pragma clang loop directives" which do not reliably take a sequence of trans- formations into account.

    We present the "#pragma clang transform" directive that specifically supports chaining transformations. These directives must be parsed, represented in the AST, instantiated for templates, (de-)serialized, dumped, semantically verified, and its LLVM-IR generated.

*   Optimizing builds on Windows: some practical considerations \[ [Video](https://youtu.be/usPL_DROn4k) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Ganea-OptimizingBuildesOnWindows.pdf) \]  
    *Alexandre Ganea*

    We will share our experience on using Clang & LLD on large (50M LoC) video game codebases, and we will show some pitfalls and considerations for improving build times on Windows 10. Profile traces based on practical scenarios will be used to demonstrate our changes. Finally we intend to present new ways for compiling code with Clang to ultimately increase iteration times.

*   LLVM-Reduce for testcase reduction \[ [Video](https://youtu.be/n1jDj7J9N8c) \] \[ Slides \]  
    *Diego Treviño Ferrer*

    LLVM-Reduce is a new and powerful tool that can reduce IR testcases in new and interesting ways; reducing IR code to almost a fraction of the original size.

    In this talk I will demonstrate how to use the tool and how to build a proper interesting-ness test - a key element used by llvm-reduce in order to minimize testcases. The more powerful the test is, the better testcase it will produce.

*   Memoro: Scaling an LLVM-based Heap profiler \[ [Video](https://youtu.be/fm47XsATelI) \] \[ Slides \]  
    *Thierry Treyer*

    Memoro is a heap profiler built using the LLVM Sanitizer infrastructure. It instruments your program during the compilation and its visualiser helps you navigate the collected profile by highlighting bad patterns, such as frequent allocation and waste of memory. Collecting data proved to be a challenge: instrumented programs don‘t meet our expectations and the run-time overhead makes Memoro impractical to use on larger services. This talk presents our work to overcome those constraints, understand the source of the overhead and reduce it, so Memoro can be applied more easily on Facebook services.

*   The Attributor: A Versatile Inter-procedural Fixpoint Iteration Framework \[ [Video](https://youtu.be/CzWkc_JcfS0) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Doerfert-Attributor.pdf) \]  
    *Johannes Doerfert*

    The Attributor fixpoint iteration framework is a new addition to LLVM that, first and foremost, offers powerful inter-procedural attribute deduction. While it was initially designed as a replacement for the existing ’function attribute deduction“ pass, the Attributor framework is already more than that. The framework, as well as the deduced information which does not directly translate to LLVM-IR attributes, can be used for various other purposes where information about the code is required.

    In this talk we will give an overview about the design, showcase current and future use cases, discuss the interplay with other (inter-procedural) passes, highlight ongoing and future extensions, and finally present an evolution. Actual deduction (and use) of attributes will be described but also discussed in our lighting talk presentations and poster.

*   LLVM Tutorials: How to write Beginner-Friendly, Inclusive Tutorials \[ [Videos](https://youtu.be/F_q50Th1t3A) \] \[ Slides \]  
    *Meike Baumgärtner, Dmitri Gribenko*

    As a beginner with no connection to the LLVM community, getting into contributing to LLVM is hard. To keep the LLVM developer community healthy with a steady stream of new developers coming in, we need tutorials that explain how to accomplish basic tasks in the real LLVM code base. Examples include writing/improving a Clang warning, and adding/improving an optimization pass. Those tutorials are not only helpful for unaffiliated beginners, but can also help onboard new employees as well as provide insights for experienced LLVM developers into parts of the project we are not familiar with.

    To start this effort, we wrote three new tutorials with supporting documentation: ’My First Typo Fix“ (explaining the end-to-end development workflow), ’My First Clang Warning“ , and ’My First Clang/LLVM Tutorial“ (showcasing the contents of this talk), with more tutorials to come. To scale this effort of creating new tutorials and cover most parts of the LLVM project, we need to engage more members of the LLVM community to join us.

    We will share our experience of writing and testing the tutorials we created and give recommendations on how to write beginner-friendly, inclusive tutorials for the LLVM project.

*   Maturing an LLVM backend: Lessons learned from the RISC-V target \[[Video](https://youtu.be/hT_0HaXW_Io) \] \[ Slides \]  
    *Alex Bradbury*

    The RISC-V backend will ship as an official target in the 9.0 release, due the end of August. This talk will give a brief overview of the current status, but primarily focus on elaborating on the development and testing process, picking out lessons to be learned for other backends and for the LLVM community as a whole. Which aspects of our methodology should others adopt? Are there opportunities to improve LLVM to make it easier to bring up new backends? Or opportunities to better share tests? How can we make it easier for language frontends like Rust to support new targets?

**Tutorials**

*   Getting Started With LLVM: Basics  
    *Jessica Paquette, Florian Hahn*

    This tutorial serves as a tour of LLVM, geared towards beginners interested in implementing LLVM passes. Both LLVM middle-end (IR) and back-end (MIR) passes are covered. At the end of this tutorial, newcomers will be armed with the tools necessary to create their own passes, and improve upon existing passes.

    This tutorial contains

    *   A brief, high-level explanation of LLVM’s pass-based architecture.
    *   An explanation of analysis and tranformation passes, and how they interact.
    *   Examples of important analysis passes, such as Dominator Trees and Target Transform Information.
    *   An introduction to fundamental data structures and APIs for LLVM pass development.
    *   A sample project which ties together the tutorial material, for use as a reference.

*   ASTImporter: Merging Clang ASTs \[ [Videos](https://youtu.be/M9hSCNC4w2U) \] \[ Slides \]  
    *Gábor Márton*

    ASTImporter is part of Clang's core library, the AST library. There are cases when we have to work with more than one AST contexts, but we would like to view the set of the ASTs as if they were one big AST resulting from the parsing of all files together. ASTImporter imports nodes of an AST context into another AST context.

    Existing clients of the ASTImporter library are Cross Translation Unit (CTU) static analysis and the LLDB expression parser. CTU static analysis imports a definition of a function if its definition is found in another translation unit (TU). This way the analysis can breach out from the single TU limitation. LLDB’s "expr" command parses a user-defined expression, creates an ASTContext for that and then imports the missing definitions from the AST what we got from the debug information (DWARF, etc).

*   Developing the Clang Static Analyzer  
    *Artem Dergachev*

    This tutorial is about getting around the internals of the static analyzer. You'll learn how to figure out what exactly is the static analyzer thinking when it analyzes any particular code. You'll learn how to debug false positives and other bugs in a methodical, principled manner. We'll show how the analyzer represents program behavior as a graph and walk through a few such graphs step-by-step and then see how to debug it further when we believe that anything about these graphs is incorrect.

    This tutorial will be useful to anybody who wants to get involved in the development of the static analyzer, sub-project of LLVM that is both complex and also friendly to newcomers. The tutorial is a complement to the talk “How to Write a Checker in 24 Hours” from LLVM DevMtg'2012; here we will focus on getting started contributing to the analyzer core.

*   Writing an LLVM Pass: 101 \[ [Video](https://youtu.be/ar7cJl2aBuU) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Warzynski-WritingAnLLVMPass.pdf) \]  
    *Andrzej Warzynski*

    This tutorial will introduce you to the intricacies of writing, building and testing an LLVM pass. It is based on the latest release of LLVM. It aims to provide a reference starting point for those wanting to understand better how LLVM works and those who want to learn how to write LLVM plugins or LLVM based tools. It will cover common gotchas when building a pass and ways of debugging them (with and without a debugger). It will walk you through sample transformation and analysis passes (and explain the difference). It will cover pass registration using the new and the legacy pass managers. We will also try the new, Polly-inspired plugin registration mechanism (based on a patch not yet merged upstream at the point of writing this abstract). Finally, you’ll see how to write and configure LIT tests for the sample passes as well and how to use the typical LLVM testing tools (e.g. FileCheck, not, count).

*   Writing Loop Optimizations in LLVM \[ [Video](https://youtu.be/3pRhvQi7Z10) \] \[ Slides \]  
    *Kit Barton, Ettore Tiotto, Hal Finkel, Michael Kruse, Johannes Doerfert*

    LLVM contains an evolving set of classes and tools specifically designed to interact with loops. The Loop and LoopInfo classes are being continually improved, as are supporting data structures such as the Data Dependence Graph (DDG) and Program Dependence Graph (PDG). The pass manager infrastructure (both New and Legacy pass managers) provide infrastructure to write both function passes and loop passes. However, putting all of these concepts together to write a functioning loop optimization pass can still be a somewhat daunting task.

    This tutorial will start by introducing basic terminology that is used within LLVM to describe loops (for example, many of the concepts introduced in https://reviews.llvm.org/D65164). It will then look at the Loop and LoopInfo classes, and go over the interfaces they have to work with loops. It will provide examples of how these classes can be used to implement different types of loop optimizations, using examples from both the Loop Fusion and Loop Distribution passes. It will discuss the differences between a function pass and a loop pass, including a discussion of the advantages and disadvantages of each one when writing loop optimizations. It will also provide guidance on when each type of pass should be used. Finally, it will go through many of the useful utility functions that need to be used in order to write a loop optimization efficiently (e.g., updating the dominator tree, updating Scalar Evolution, etc.).

*   The Attributor: A Versatile Inter-procedural Fixpoint Iteration Framework \[ [Video](https://youtu.be/HVvvCSSLiTw) \]  
    *Johannes Doerfert*

    The Attributor fixpoint iteration framework is a new addition to LLVM that, first and foremost, offers powerful inter-procedural attribute deduction. While it was initially designed as a replacement for the existing “function attribute deduction” pass, the Attributor framework is already more than that. The framework, as well as the deduced information which does not directly translate to LLVM-IR attributes, can be used for various other purposes where information about the code is required.

    In this talk we will give an overview about the design, showcase current and future use cases, discuss the interplay with other (inter-procedural) passes, highlight ongoing and future extensions, and finally present an evolution. Actual deduction (and use) of attributes will be described but also discussed in our lighting talk presentations and poster.

*   Getting Started with the LLVM Testing Infrastructure \[ [Video](https://youtu.be/isVQ8kYqaSA) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Homerding-Kruse-LLVMTestingInfrastructureTutorial.pdf) \]  
    *Brian Homerding, Michael Kruse*

    A strong testing infrastructure is critical for compilers to maintain a high quality of correctness and performance. This tutorial will cover the various elements of the LLVM testing infrastructure. The focus will be to for newcomers to learn to write and run the unit, regression and whole program tests in the LLVM infrastructure as well as the integration of external suites into the LLVM test suite. We will additionally cover the various frameworks and tools used within the test suites, including using LNT to track performance data.

*   An overview of Clang \[ [Video](https://youtu.be/5kkMpJpIGYU) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/ClangTutorial-Stulova-vanHaastregt.pdf) \]  
    *Sven van Haastregt, Anastasia Stulova*

    This tutorial will give an overview of Clang. We will cover the distinction between the Clang compiler driver and the Clang language frontend, with an emphasis on the latter. We will examine the different Clang components that a C program goes through when being compiled, i.e., lexing, parsing, semantic analysis, and LLVM IR generation. This includes some of the Clang Abstract Syntax Tree (AST), Type, and the Diagnostics infrastructure. We will conclude by explaining the various ways in which Clang is tested.

    The tutorial is aimed at newcomers who have a basic understanding of compiler concepts and wish to learn about the architecture of Clang or start contributing to Clang.

*   An overview of LLVM \[ [Video](https://youtu.be/J5xExRGaIIY) \] \[ Slides \]  
    *Eric Christopher, Sanjoy Das, Johannes Doerfert*

    Details coming soon.

*   How to Contribute to LLVM  
    *Chris Bieneman, Kit Barton*

    Details coming soon.

*   My First Clang Warning \[ [Video](https://youtu.be/FNnKMSkaLkY) \] \[ Slides \]  
    *Dmitri Gribenko, Meike Baumgärtner*

    This tutorial will walk you through adding a new warning to Clang. We will test the new warning on real code, analyze the results, and discuss how certain aspects of C++ affect design of warnings and static analysis tooling. This workshop is aimed at newcomers who have a basic understanding of compiler concepts and wish to learn about the architecture of Clang or implement static analysis tooling based on Clang. We will not be covering ClangTidy due to time constraints, but want to emphasize that understanding concepts described in this workshop is essential for writing ClangTidy checkers.

**Panels**

*   Panel: Inter-procedural Optimization (IPO) \[ [Video](https://youtu.be/cC2cspQgSxM) \]  

    Interprocedural optimizations (IPOs) have been historically weak in LLVM. The strong reliance on inlining can be seen as a consequence or cause. Since inlining is not always possible (recursion, parallel programs, ...) or beneficial (large functions), the effort to improve IPO has recently seen an upswing again. In order to capitalize this momentum, we would like to talk about the current situation in LLVM, and goals for the immediate, but also distant, future.

    We will ask our expert panel questions as follows:

    *   What are the current and potential problems with IPO?
    *   How does the new pass manager impact IPO?
    *   Is function cloning & IPO as an alternative to inlining?
    *   How does the desired (new PM) pipeline differ from what we have right now?
    *   How is, and how should, IPO interact with (thin-)LTO and PGO?
    *   What are the most desirable IPO analyses and optimizations we are lacking today?

    This guided panel discussion is a follow-up to the BoF at EuroLLVM'19. Both experts and newcomers are welcome to attend. Questions can be send to the organizers prior to the conference to allow consideration.

*   The Loop Optimization Working Group \[ [Video](https://youtu.be/CEVznqrzVVI) \]  
    *Kit Barton, Michael Kruse, TBD*

    The Loop Optimization Working Group has been meeting bi-weekly since June 5, 2019. The primary focus of the group is to discuss loop optimizations within LLVM. This panel will contain several active members of the workgroup. It will begin with an overview of the working group and describe the topics that are currently being pursued by the workgroup, including status updates for loop optimizations that are currently under active development. It will then open up the discussion to more general topics of loop optimizations and the loop optimization pipeline. These discussions may include:

    *   Specific loop optimizations that are missing, or need improvement
    *   General infrastructure for loop optimizations
    *   Organization of loop optimizations in the loop optimization pipeline (e.g., the loop optimization strategy)
    *   The advantage/necessity of a LoopPass in the NewPassManager

**Birds of a Feather**

*   LLDB  
    *Jonas Devlieghere*

    LLDB has seen an influx of contributions over the past year, with the highest level of activity we've seen in the past 4 years. Let's use this BoF to discuss everybody's goals and identify places where we can synchronize our efforts. Some potential topics include breaking up dependencies in LLDB, support cross-module references, upstreaming of language supports (swift, rust), and improving Windows support.

*   Towards Better Code Generator Design and Unification for a Stack Machine  
    *Leonid Kholodov, Dmitry Borisenkov*

    By design, LLVM backend infrastructure is geared towards classical register-based architectures. Thus, adapting it to a stack machine implies additional LLVM passes that are likely to vary depending on a target. For instance, the Selection DAG cannot produce instructions that directly handle the stack. Instead, it selects a relevant instruction version designed to work with registers. Then, MIR passes are performed to insert stack manipulations (pushes, pops, exchanges) and to convert instructions handling virtual registers into those handling stack slots. The suggested logic seems quite generic and not limited to a specific stack-based virtual machine. It is similar to other optimizations and analytical approaches that can be applied to stack machines regardless of the specific instruction set.

    Previously, WebAssembly was the only implementation that needed a comprehensive stackification logic, now we created an option for the TON virtual machine (TVM). Given that stack machines are great for binary size minimization, stackification solutions are likely to face demand from other domains. So, we would love to discuss whether or not the community needs generic algorithms that can be integrated with various backends and if stack-machine support might benefit the target-independent code generator.

*   Debug Info  
    *Adrian Prantl*

    As evidenced by the debug info quality metrics introduced at last year's Debug Info BoF session, there have been significant improvements to LLVM's handling of debug info in optimized code throughout 2019. With a growing number of debug info contributors in the LLVM community, this session provides a forum to highlight recent improvements and areas that need attention. We will use the opportunity to summarize the current state of LLVM debug info quality and then open the floor to a discussion about future directions.

**Lightning Talks**

*   GWP-ASan: Zero-Cost Detection of Memory Safety Bugs in Production \[ [Video](https://youtu.be/RQGWMLkwrKc) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Morehouse-GWP-ASan.pdf) \]  
    *Matt Morehouse*

    GWP-ASan is a negligible-overhead sampling-based utility for finding heap-use-after-frees and heap-buffer-overflows in production. It combines the capabilities of the Electric Fence Malloc Debugger with the power of sampling to provide probabilistic bug detection with arbitrarily low CPU and RAM overhead. This low overhead allows GWP-ASan to be widely deployed in production, where it finds bugs that have evaded all other forms of testing, including fuzz testing with sanitizers.

    This talk provides a quick introduction to how GWP-ASan works, the impact it has had at Google, and how you can use GWP-ASan for your own production applications.
*   When 3 Memory Models Aren’t Enough – OpenVMS on x86 \[ [Videos](https://youtu.be/fiZwCLbJNSI) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/ThreeMemoryModelsNotEnough.pdf) \]  
    *John Reagan*

    Over the past two years, we have ported OpenVMS to x86 using LLVM. OpenVMS has some unique features such as ’ code in 64-bit space“ , ’stack and static data in 32-bit space“, and ’procedure values must be representable in 32-bits“. This talk will describe some of the interesting aspects of these requirements and how we modified LLVM and our linker to solve them.

*   FileCheck: learning arithmetic \[ [Video](https://youtu.be/mcrQ5f-mASw) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Preudhomme-FileCheck.pdf) \]  
    *Thomas Preud'homme*

    This talk introduces the numeric expression matching in FileCheck, feature recently upstreamed by the speaker, which allows to check that two numeric values in the input are linked by a numeric relation. This is useful for testing memory layout or register allocation among other things. The feature also allows the values to be expressed in different radix, thus allowing to relate an address expressed in hex number to an offset expressed in decimal notation.

*   \-Wall Found Programming Errors and Engineering Effort to Enable Across a Large Codebase \[ [Video](https://youtu.be/Fc4Br0eNUa4) \] \[ [Slides](http://llvm.org/devmtg/2019-10/slides/Kumar-WallFoundCompilationErrors.pdf) \]  
    *Aditya Kumar*

    \-Wall tells the compiler to enable a lot of (~9000) warning checks. And after we enable -Werror (which tells the compiler to treat warnings as errors), the build fails and good things happen. We found real bugs by enabling the warnings and hopefully, this will prevent bugs in future. Compiler warnings are one of the best static-analysis tools we could have, so we would like to use it to the fullest.

    I’ll share some interesting bugs that were found as a result of enabling ‘-Wall’ in a large codebase. While some of them were funny and benign, some were really critical bugs hidden in the codebase. I’ll share strategies that worked and that didn’t for example: enabling compiler warning per module doesn’t scale well in a monorepo.

*   Handling 1000s of OpenCL builtin functions in Clang \[ [Video](https://youtu.be/LU_2aOn3Wpg) \] \[ Slides \]  
    *Sven van Haastregt*

    OpenCL provides about 13000 different function overloads that can be used by OpenCL code. Clang provides a header file containing all declarations, but unfortunately parsing this header file takes several seconds per OpenCL program. Ameliorating the parsing time by precompiling the header file has several drawbacks: the resulting PCH file is several megabytes large and requires special handling for macros and conditional compilation.

    We present a new TableGen driven approach to support all OpenCL builtins in a fast and compact manner. TableGen generates a trie and tables for recognising and constructing function declarations. From this, Clang constructs the necessary builtin function declarations when a regular name lookup fails and retries the lookup. This approach avoids the need to parse the opencl-c.h header or populate the symbol table with 1000s of declarations. The generated tables and functions together take less than 250 kilobytes which is significantly smaller than the PCH approach. The initial patches of this work have been committed (e.g. r362371) and the remainder of the implementation is currently being upstreamed and reviewed.

*   NEC SX-Aurora as a Scalable Vector Playground \[ [Video](https://youtu.be/SW60DrfOuGw) \] \[ [Slides](http://llvm.org/devmtg/2019-10/slides/Moll-NEC-SX-AuroraAsScalableVectorPlayground.pdf) \]  
    *Simon Moll, Kazuhisa Ishizaka*

    Supporting scalable vector ISA such as ARM SVE, RISC-V Vector is a hot topic in LLVM. In this talk, we will introduce the scalable vector ISA in "SX-Aurora TSUBASA" vector computer that is only one market available computer on which the LLVM developers can play with scalable vector. The scalar LLVM backend for SX-Aurora is available, and developers can immediately try interesting topics such as design of IR and auto vectorization. We will also describe design of vector IR based on LLVM-VP and code generation technique for it.

*   Implementing Machine Code Optimizations for RISC-V \[ [Videos](https://youtu.be/4_raNLEq2j0) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Revill-ImplementingMachineCodeOpts-RISCV.pdf) \]  
    *Lewis Revill*

    LLVM's CodeGen library contains support for various optimizations at the machine code level. I have recently been investigating a few ways in which the RISC-V backend could make use of this support to improve code size and speed. The optimizations implemented were: saving and restoring callee saved registers via libcalls; utilizing shrink wrapping to modify prologue/epilogue insertion points; and utilizing the machine outliner to deduplicate common machine code sequences.

    In this talk I will discuss the process of enabling these optimizations for RISC-V, and explain the various decisions that were made. I will show benchmarking results for each technique, and talk about potential changes that could improve the results.

*   Optimization Remarks Update \[ [Videos](https://youtu.be/AbgYN3tPaB8) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Mistrih-OptimizationRemarksUpdate.pdf) \]  
    *Francis Visoiu Mistrih*

    This lightning talk will give a brief overview of the new remark format, and will discuss the integration with the toolchain to provide a better user experience. We will quickly go over the impact of enabling optimization remarks for a project and talk about our future plans.

*   Supporting Regular and Thin LTO with a Single LTO Bitcode Format \[ [Video](https://youtu.be/uH0-e4xayNc) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Voss-SupportingRegularandThinLTO.pdf) \]  
    *Matthew Voss*

    LTO bitcode files are currently specialized to either Thin or Regular LTO. As a user or middleware library provider, this increases the complexity. A user must recompile all files for the type of LTO and library providers must ship two versions of their bitcode. This talk outlines Sony’s solution: a single LTO bitcode format that can be used with both Thin and Regular LTO backends.

*   Transitioning Apple’s Downstream llvm-project Repositories to the Monorepo  
    *Alex Lorenz*

    This talk describes how Apple transitioned to the new llvm-project monorepo from the split downstream {llvm/clang/...} Git repositories that were used for Swift and internal clients. We also briefly go over the tools and processes that are used to continuously merge from the upstream monorepo to the newly created downstream ones.

*   A Unified Debug Server For Deeply Embedded Systems and LLDB \[ [Video](https://youtu.be/IMq3a_SSzFw) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Cook-UnifiedDebugServerforDeeplyEmbeddedSystemsandLLDB.pdf) \]  
    *Simon Cook*

    When debugging applications, whilst LLDB handles high level operations, it abstracts and offloads lower level operations to a debug server which is responsible for controlling the process or hardware. The debug server is capable of very simple operations, such as reading/writing registers and memory, starting and single-stepping the processor and reporting back when the processor halts. The two communicate with each other using a very simple text based serial protocol.

    The GNU debugger has long been served by a number of debug server options, including the gdbserver program for Linux class embedded systems and tools such as OpenOCD for deeply embedded systems. LLDB is not so well served, even though it uses an almost identical protocol to talk to the debug server. In most cases, the built in lldb-server program is used for this purpose, but this is ill suited for bare metal applications on embedded platforms.

    We present a new free and open source debug server for deeply embedded systems which fully supports LLDB. It is capable of controlling the simplest hardware, through to complex multicore heterogenous architectures. In particular, it can also run in lockstep mode, where two targets (for example an architectural model and a hardware implementation) are controlled together, to identify any points where behavior diverges.

*   State of LLDB and Deeply Embedded RISC-V \[ [Videos](https://youtu.be/37ce7gVpgIE) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Cook-StateofLLD-RISCV.pdf) \]  
    *Simon Cook*

    RISC-V is one of the newest targets to be supported with LLVM, having gained non-experimental status in LLVM 9.0, and has both a Clang and LLD port. In this talk I discuss the state of support for various RISC-V architectures in LLDB, focusing on debugging deeply embedded applications.

*   Supporting a Vendor ABI Variant in Clang \[ [Video](https://youtu.be/ATOfCfM9hSg) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Robinson-SupportingVendorABIinClang.pdf) \]  
    *Paul Robinson*

    Clang and LLVM implement a variety of ABIs, both at the language level ("C++ ABI" e.g., struct layout) and hardware level (e.g., calling conventions). These ABIs are subject to bug fixes and evolution; they are software conventions, after all, even with a strong intent to keep them stable. This can be a problem for a vendor with extremely strict backward-compatibility guarantees; sometimes an ABI bug "fix" is actually a breakage. I describe tactics Sony has used to preserve ABI compatibility with the original PS4(r) release in 2013, despite the good intentions of subsequent upstream development.

*   Speculative Compilation in ORC JIT \[ [Videos](https://youtu.be/MUyf2466PbI) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Velliengiri-SpeculativeCompilationinORC.pdf) \]  
    *Praveen Velliengiri*

    Using the ORC JIT APIs we have developed support for speculative compilation. This feature aims to use early compilation on dedicated additional threads to hide compilation latency in the JIT'd program without interfering with execution. Speculative decisions are made based on the branch probability of control flow graphs which is derived from static heuristics and IR instrumentation based profiling of JIT'd code. We have seen a consistent reduction in compilation overhead experienced by the execution thread. Finally, we will show our results for selected applications.

*   Optimization Remarks for Human Beings  
    *William Bundy*

    This talk dives into the development of a Visual Studio extension for displaying optimization remarks at Sony PlayStation, discussing both the possibilities for remarks as a teaching and code analysis tool if they're seamlessly integrated into everyday programming, and some of the issues faced in making that possible for massive projects.

*   Improving the Optimized Debugging Experience \[ [Video](https://youtu.be/nZmHD9yiRz4) \] \[ [Slides](http://llvm.org/devmtg/2019-10/slides/Cazalet-Hyams-ImprovingOptimizedDebuggingExperience.pdf) \]  
    *Orlando Cazalet-Hyams*

    Sometimes it is impractical to debug unoptimized code (-g -O0). However, the optimized debugging experience (-g -O2) can be frustrating and occasionally misleading. This is not ideal, especially when printf-debugging won't cut it. But it doesn't have to be this way!

    Over the last year, using DExTer and other tools, we have found many debug-info bugs that occur when compiling with optimizations. Some remain unfixed and there are certainly more to be found.

    In this talk I'll outline some examples of these bugs, how we found them, and what we're doing to improve the optimized debugging experience.

*   Improving your TableGen Descriptions \[ [Video](https://youtu.be/dIEVUlsiktQ) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Absar-ImprovingYourTableGenDescription.pdf) \]  
    *Javed Absar*

    TableGen is a DSL used extensively in LLVM for describing instructions, attributes, scheduler models, amongst other things. This talk will walk through TableGen language features, including new ones, that help write concise and better TableGen files.

*   Loom: Weaving Instrumentation for Program Analysis \[ [Video](https://youtu.be/T8qGbze3apo) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Kidney-Loom.pdf) \]  
    *Brian Kidney*

    Instrumentation tools often focus on single tasks, such as gathering performance numbers or detecting race conditions. While gathering important information for the user, these tools are not often designed to allow the end-user a more general code exploration as executed. Loom is a framework for general-purpose instrumentation and transformation of software in the LLVM intermediate representation. Loom provides both a standalone tool and a library with an API designed to allow for the implementation of custom instrumentation passes.

    Loom's current functionality is presented, including real-world applications for Loom in a recent research project. We present comparisons of both performance and functionality of Loom to existing instrumentation tools, including X-Ray, CSI, D-Trace and Intel Pin. Finally, we will present security use cases that are not addressed by any of these instrumentation tools and are the motivation for new Loom developments.

*   Clang Interface Stubs: Syntax Directed Stub Library Generation. \[ [Video](https://youtu.be/Z7aHpWsFfSM) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Lotfi-ClangInterfaceStubs.pdf) \]  
    *Puyan Lotfi*

    Stub libraries, like import libraries on Windows and TAPI on Darwin, are useful for reducing link time and for constraining the API surface of an SDK. Stub libraries are limited to the API surface the library author intends to expose to users and do not contain runtime code. We believe that source driven API annotation is the best way to encourage library writers to lock down an API.

    In this talk we will discuss the various proof of concept attempts and improvements to clang that have been done in the process of building this feature, how this information is derived using visibility attributes provided by the developer in their code, and ways clang Interface Stubs can be used by a library author to control and track an API.

*   Flang Update \[ [Video](https://youtu.be/MqQk5VsPar4) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Scalpone-FlangUpdate.pdf) \]  
    *Steve Scalpone*

    Flang development update touching on current status, experience with MLIR, and an overview of compiler performance.

*   Lowering tale: Supporting 64 bit pointers in RISCV 32 bit LLVM backend \[ [Video](https://youtu.be/Vb4wj8aR1xI) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Sharma-Supporting64BitPointersinRISCV.pdf) \]  
    *Reshabh Sharma*

    We are working on a RISCV 32 bit GPU ISA, which is an unofficial extension over RV32 having custom instructions specifically designed for GPGPU. This will help in improving programmability of the second generation design of open source RISC-V manycore processor (bjump.org/manycore).

    Addressable memory has greatly exceeded 32 bits, we extend the support to 64 bit addressable memory at address space 1 using custom load and store instructions. In this talk, we will describe our implementation in chronological order with respect to different phases in the backend supported with details about all the approaches considered with their pros and cons.
*   Virtual Function Elimination in LLVM \[ [Videos](https://youtu.be/PtfF0BixmWA) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Stannard-DeadVirtualFunctionElimintation.pdf) \]  
    *Oliver Stannard*

    I am currently working on a patch to LLVM and Clang to allow unused C++ virtual functions to be removed by LTO. I will explain what virtual functions and calls to them look like in LLVM IR, and why they can't be removed by existing optimisations. Then I will describe the changes I have made to LLVM and Clang to make this optimisation possible.

*   Making a Language Cross Platform: Libraries and Tooling \[ [Video](https://youtu.be/bdiQM0IPMio) \] \[ [Slides](http://llvm.org/devmtg/2019-10/slides/Mittertreiner-MakingALanguageCrossPlatform.pdf) \]  
    *Gwen Mittertreiner*

    A look back (and forwards) on what works well when writing cross platform system level libraries and what becomes difficult, especially in regards to supporting Windows and Android, and how you can design your tools and libraries to make this easier.

*   Grafter - A use case to implement an embedded DSL in C++ and perform source to source traversal fusion transformation using Clang \[ [Video](https://youtu.be/x0u92t_seas) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Sakka-Grafter.pdf) \]  
    *Laith Sakka*

    Grafter is a tool that performs fusion for general imperative traversals that traverse the same tree achieving significant performance benefits.

    In this talk, we will discuss how Grafter utilizes Clang to implement its language, captures different information that is needed for its static analysis, and finally writes back the new fused traversals.

**Posters**

*   TON Labs Backend for TON Blockchain  
    *Dmitry Borisenkov, Dmitry Shtukenberg, Leonid Kholodov*

    TON Labs initiative to deliver a comprehensive ecosystem for the TON blockchain was announced in July 2019. Ultimately, it will be offered as an open-source solution. The compiler toolchain is an essential part of it designed to enable developers using general-purpose languages they know to develop smart contracts and to run them on a virtual machine that is not bound to WebAssembly.

    A beta version of the C compiler has been recently released and the source code is supposed to become public by the time of this event, or soon. The poster is to demonstrate the overall scope of work related to the compiler, as well as all the challenges we faced while adapting the LLVM framework and the C language to a domain where neither is initially supposed to work.
*   LLVM Build Times Using a Program Repository  
    *Rusell Gallop, Phil Camp*

    The Program Repository is a project studying the benefits of changing the build workflow, storing object data in a database instead of object files, structured to eliminate duplicated work from the compilation process, enable incremental compilation, and to minimize the work that must be performed by the linker. This poster will present the current compile time gains building LLVM and Clang.

    The Program Repository identifies duplicate code and data across compile units and avoids repeated work during both compilation and linkage. For example, if a function is present in multiple compile units then it will only be optimised and stored once. With duplicates identified at compile time, a program repository linker will not need to process any code or data that it would otherwise discard.

*   RISC-V Bit Manipulation Support in the Clang/LLVM Toolchain  
    *Scott Egerton, Paolo Savini*

    This poster presents details of the Clang/LLVM implementation to add support for the RISC-V bit manipulation instruction set extension.

*   Attributor, a Framework for Interprocedural Information Deduction  
    *Johannes Doerfert, Hideto Ueno, Stefan Stipanovic*

    Over the summer, the “Attributor” fixpoint iteration framework was developed and committed into LLVM. The first goal of this framework is to improve the current attribute inference system with consistency. The framework simplifies module-wide attribute deduction and also fosters generic interprocedural information propagation. Because of abstracted interfaces and the provided infrastructure, it is now much easier to add and deduce new attributes. In this poster, we will outline the Attributor framework as well as our work on attribute deduction. We detail how deduction of exciting attributes improved, including but not limited to nonnull, noalias, dereferenceable, and describe the new attributes we introduced and derive now: nosync, nofree, and willreturn.

*   Overflows Be Gone: Checked C for Memory Safety  
    *Mandeep Singh Grang*

    Buffer overflows and out-of-bounds memory accesses are common programming anomalies. They are a major security exploit which can allow an attacker to compromise spatial safety thus resulting in unintended program behavior. In this poster, we present Checked C, an extension to C designed to guarantee spatial safety. Checked C is implemented in LLVM and Clang. Checked C adds static and dynamic checking to C to detect or prevent memory access violations. The goal of Checked C is to improve systems programming by making fundamental improvements to C.

**Student Research Competition**

*   Cross-Translation Unit Optimization via Annotated Headers  
    *William S. Moses*

    LLVM automatically derives facts that are only used while the respective translation unit, or LLVM module, is processed (i.e. constant function, error-throwing, etc). This is true both in standard compilation but also link-time-optimization (LTO) in which the module is (partially) merged with others in the same project at link time. LTO is able to take advantage of this to optimize functions calls to outside the translation unit. However, LTO doesn't solve the problem for two reasons of practicality: LTO comes with a nontrivial compile-time investment; and many libraries upon which a program could depend, do not ship with LTO information, simply headers and binaries. In this extended abstract, we solve the problem by generating annotated versions of the source code that also include this derived information. Such an approach has the benefits of both worlds: allowing optimizations previously limited to LTO without running LTO and only providing headers. Such headers are created by modifying Clang to understand three custom attributes to represent arbitrary LLVM function attributes and modifying LLVM to emit C-compatible headers with the aforementioned attribute. Finally, we test the approach experimentally on the DOE RSBench proxy application and verify that it provides the expected speedups.

*   Quantifying Dataflow Analysis with Gradients in LLVM  
    *Abhishek Shah*

    TBD

*   Floating Point Consistency in the Wild: A practical evaluation of how compiler optimizations affect high performance floating point code  
    *Jack J Garzella*

    Using the FLiT compilation tool, we evaluate Physics-related high-performance codebases, by recompiling each one with LLVM, GCC, and Intel, at every optimization level and all sorts of FP-related flags.

*   Static Analysis of OpenMP Data Mapping for Target Offloading \[ [Video](https://youtu.be/9ZPQpo8QuyI) \] \[ [Slides](https://llvm.org/devmtg/2019-10/slides/Barua-StaticAnalysisofOpenMPPrograms.pdf) \]  
    *Prithayan Barua*

    TBD

# Contact

To contact the organizer, [email Tanya Lattner](mailto:tanyalattner@llvm.org)

<!-- *********************************************************************** -->

* * *

</div>
