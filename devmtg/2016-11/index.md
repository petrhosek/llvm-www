---
layout: "default.html"
permalink: "devmtg/2016-11/index.html"
---
# 2016 US LLVM Developers' Meeting

1.  [About](#about)
2.  [Program](#program)
3.  [Talk Abstracts](#abstracts)
4.  [Contact](#contact)

*   **What**: The tenth meeting of LLVM developers and users
*   **When**: November 3-4, 2016
*   **Where**: San Jose Convention Center - San Jose, CA, USA

A huge thank you to our sponsors!

# Diamond Sponsors:

#      [Apple](http://www.apple.com)

        [Apple](http://www.apple.com)

# Platinum Sponsors:

        ![](logos/Google-logo_420_color_2x.png)  
        [Google](http://google.com)

        ![](logos/psf_pos.jpg)  
        [Sony Computer Entertainment America](http://us.playstation.com/corporate/about/)

# Gold Sponsors:

        ![](logos/Intel-logo.png)  
        [Intel](http://intel.com)

        ![](logos/FB-fLogo-Blue-broadcast-2.png)  
        [Facebook](http://facebook.com/)

# Silver Sponsors:

        ![](logos/HSAFoundation-FINAL.PNG)  
        [HSA Foundation](http://www.hsafoundation.com)

# Bronze Sponsors:

        ![](logos/logo_JetBrains_4.png)  
        [JetBrains](http://www.jetbrains.com/?utm_source=LLVM&utm_medium=sponsorship)

        ![](logos/ARMCompanyLogo.jpg)  
        [ARM](http://www.arm.com)

        ![](logos/Microsoft-logo_rgb_c-gray.png)  
        [Microsoft](http://www.microsoft.com)

# About

The LLVM Foundation announces the tenth annual US LLVM Developers' Meeting will be held November 3rd and 4th in San Jose, California.

The conference will include technical talks, BoFs, hacker's lab, tutorials, and posters.

The meeting serves as a forum for [LLVM](http://llvm.org), [Clang](http://clang.llvm.org), [LLDB](http://lldb.llvm.org) and other LLVM project developers and users to get acquainted, learn how LLVM is used, and exchange ideas about LLVM and its (potential) applications. More broadly, we believe the event will be of particular interest to the following people:

*   Active developers of projects in the LLVM Umbrella (LLVM core, Clang, LLDB, libc++, compiler\_rt, klee, dragonegg, lld, etc).
*   Anyone interested in using these as part of another project.
*   Compiler, programming language, and runtime enthusiasts.
*   Those interested in using compiler and toolchain technology in novel and interesting ways.

Please sign up for the [LLVM Developers' Meeting list](http://lists.llvm.org/mailman/listinfo/llvm-devmeeting) for future announcements and to ask questions.

# Program

The agenda may be found here: [https://llvmdevelopersmeetingbay2016.sched.org](https://llvmdevelopersmeetingbay2016.sched.org)

Please view all videos on the [LLVM YouTube Channel](https://www.youtube.com/channel/UCv2_41bSAa5Y_8BacJUZfjQ).

| Media | Talk |
| --- | --- |
| [Slides](Slides/Hames-ORC.pdf)<br>[Video](https://youtu.be/hILdR8XRvdQ) | **[ORC -- LLVM's Next Generation of JIT API](#talk1)**<br>Lang Hames |
| [Slides](Slides/Ansari-Code-Alignment.pdf)<br>[Video](https://youtu.be/IX16gcX4vDQ) | **[Causes of Performance Instability due to Code Placement in X86](#talk2)**<br>Zia Ansari |
| [Slides](Slides/Finkel-IntrinsicsMetadataAttributes.pdf)<br>[Video](https://youtu.be/jII0AcgU_5c) | **[Intrinsics, Metadata, and Attributes: The story continues!](#talk3)**<br>Hal Finkel |
| [Slides](Slides/Nishanov-LLVMCoroutines.pdf)<br>[Video](https://youtu.be/Ztr8QvMhqmQ) | **[LLVM Coroutines: Bringing resumable functions to LLVM](#talk4)**<br>Gor Nishanov |
| [Slides](Slides/Emerson-ScalableVectorizationinLLVMIR.pdf)<br>[Video](https://youtu.be/0up2hJk7k94) | **[Scalable Vectorization for LLVM](#talk5)**<br>Amara Emerson, Graham Hunter |
| [Slides](Slides/Padlewski-DevirtualizationInLLVM.pdf)<br>[Video](https://youtu.be/qMhV6d3B1Vk) | **[Devirtualization in LLVM](#talk6)**<br>Piotr Padlewski |
| [Slides](Slides/Saito-NextLevelLLVMLoopVectorizer.pdf)<br>[Video](https://youtu.be/XXAvdUwO7kQ) | **[Extending LoopVectorizer towards supporting OpenMP4.5 SIMD and outer loop auto-vectorization](#talk7)**<br>Hideki Saito |
| [Slides](Slides/Zolotukhin-LoopPasses.pdf)<br>[Video](https://youtu.be/AfeUG7f5UA0) | **[Loop Passes: Adding new features while reducing technical debt](#talk8)**<br>Mikhail Zolotukhin |
| [Slides](Slides/DiFederico-rev.ng.pdf)<br>[Video](https://youtu.be/5CbuU4KwBCE) | **[rev.ng: a QEMU- and LLVM-based static binary analysis framework](#talk9)**<br>Alessandro Di Federico |
| [Slides](Slides/Dunbar-NewArchitectureForBuildingSoftware.pdf)<br>[Video](https://youtu.be/b_T-eCToX1I) | **[A New Architecture for Building Software](#talk10)**<br>Daniel Dunbar |
| [Slides](Slides/Kumar-Pop-GVNHoist.pdf)<br>[Video](https://youtu.be/GB3OpqSwuUw) | **[GVN-Hoist: Hoisting Computations from Branches](#talk11)**<br>Aditya Kumar, Sebastian Pop |
| [Slides](Slides/Amini-Johnson-ThinLTO.pdf)<br>[Video](https://youtu.be/9OIEZAj243g) | **[ThinLTO: Scalable and Incremental LTO](#talk12)**<br>Mehdi Amini, Teresa Johnson |
| [Slides](Slides/Lopes-LongLivePoison.pdf)<br>[Video](https://youtu.be/_-3Iiads1EM) | **[Killing poison and undef -- long live poison!](#talk13)**<br>Juneyoung Lee, Nuno Lopes |
| [Slides](Slides/Carlson-LeveragingIntermediateForms.pdf)<br>[Video](https://youtu.be/_xMUP09hmeM) | **[Leveraging Intermediate Forms for Analysis](#talk14)**<br>Jared Carlson, Ayal Spitz |
| [Slides](Slides/Nemet-Compiler-assistedPerformanceAnalysis.pdf)<br>[Video](https://youtu.be/qq0q1hfzidg) | **[Compiler-assisted Performance Analysis](#talk15)**<br>Adam Nemet |
| [Slides](Slides/Colombet-GlobalISel.pdf)<br>[Video](https://youtu.be/6tfb344A7w8) | **[Global Instruction Selection Status](#talk16)**<br>Ahmed Bougacha, Quentin Colombet, Tim Northover |
| [Slides](Slides/Braun-DealingWithRegisterHierarchies.pdf)<br>[Video](https://youtu.be/-TV77T1R7OU) | **[Dealing with Register Hierarchies](#talk17)**<br>Matthias Braun |
| [Slides](Slides/Kleckner-CodeViewInLLVM.pdf)<br>[Video](https://youtu.be/5twzd06NqGU) | **[CodeView, the Microsoft Debug Info Format, in LLVM](#talk18)**<br>Reid Kleckner |
| [Slides](Slides/Sidorin-Summery-Based-Inter-Unit-Analysis.pdf)<br>[Video](https://youtu.be/jbLkZ82mYE4) | **[Summary-based inter-unit analysis for Clang Static Analyzer](#talk19)**<br>Aleksei Sidorin |
| [Slides](Slides/Bieneman-CMake.pdf)<br>[Video](https://youtu.be/StF77Cx7pz8) | **[Developing and Shipping Clang with CMake](#talk20)**<br>Chris Bieneman |
| [Slides](Slides/Paquette-Outliner.pdf)<br>[Video](https://youtu.be/yorld-WSOeU) | **[Reducing Code Size Using Outlining](#talk21)**<br>Jessica Paquette |
| [Slides](Slides/Bowen-Hugett-ToyProgrammingDemo.pdf)<br>[Video](https://youtu.be/-pL94rqyQ6c) | **[Toy programming demo of a repository for statically compiled programs](#talk22)**<br>Paul Bowen-Huggett |
| [Slides](Slides/Cook-LLVM-Program-Integrity.pdf)<br>[Video](https://youtu.be/isHCLMrXPUk) | **[Using LLVM to guarantee program integrity](#talk23)**<br>Simon Cook |

# Talk Abstracts

**ORC -- LLVM's Next Generation of JIT API**  
*Lang Hames*  
[Slides](Slides/Hames-ORC.pdf)  
[Video](https://youtu.be/hILdR8XRvdQ)  
ORC is a modular re-implementation of MCJIT that allows for more flexible configuration, better memory management, more fine-grained testing, and easier addition of new features. Its feature set includes of all MCJIT's current functionality, plus built-in support for lazy and remote compilation. This talk describes ORC's current features and design concepts, and provides demonstrations of how it can be used.

**Causes of Performance Instability due to Code Placement in X86**  
*Zia Ansari*  
[Slides](Slides/Ansari-Code-Alignment.pdf)  
[Video](https://youtu.be/IX16gcX4vDQ)  
Have you ever experienced significant performance swings in your application after seemingly insignificant changes? A random NOP shifting code addresses causing a 20% speedup or regression? This talk will explore some of the common and not so common architectural reasons why code placement/alignment can affect performance on older and newer x86 processors. Even though ideas will be shared on how to avoid/fix some of these issues in compilers, other very low level issues will not have good compiler solutions, but are still important to recognize for knowledge and identification purposes.

**Intrinsics, Metadata, and Attributes: The story continues!**  
*Hal Finkel*  
[Slides](Slides/Finkel-IntrinsicsMetadataAttributes.pdf)  
[Video](https://youtu.be/jII0AcgU_5c)  
This talk is a sequel to my talk at the 2014 LLVM Developers' Meeting, in which I discussed @llvm.assume; scoped-noalias metadata; and parameter attributes that specify pointer alignment, dereferenceability, and more. The past two years have seen changes to the metadata representation itself (e.g. distinct vs. uniqued metadata), as well as new metadata that specify pointer alignment, dereferenceability, control loop optimizations, and more. Several new attributes and intrinsics allow for more-detailed control over pointer-aliasing and control-flow properties, and new intrinsics to support masked and scatter/gather memory accesses have been added. Support for older features, such as fast-math flags and the returned attribute, have been significantly extended. I'll explain the semantics of many of these new features, their intended uses, and a few ways they shouldn't be used. Finally, I'll discuss how Clang exposes and leverages these new features to encourage the generation of higher-performance code.

**LLVM Coroutines: Bringing resumable functions to LLVM**  
*Gor Nishanov*  
[Slides](Slides/Nishanov-LLVMCoroutines.pdf)  
[Video](https://youtu.be/Ztr8QvMhqmQ)  
Though invented long time ago in 1957, coroutines are getting popular in this century. More and more languages adopt them to deal with lazily produced sequences and to simplify asynchronous programming. However, until recently, coroutines in high level languages were distinctly not a zero-overhead abstraction. We are rectifying that by adding coroutine support to LLVM that allows, finally, for high-level language to have efficient coroutines  
In this talk, we will look at coroutine examples in C++ and LLVM IR, at optimization passes that deal with coroutines and at LLVM coroutine representation that C++ and other frontend can use to describe coroutines to LLVM.  
LLVM coroutines are functions that can suspend their execution and return control back to their callers. Suspended coroutines can be resumed to continue execution when desired.  
Though coroutine support in LLVM is motivated primarily by the desire to support C++ Coroutines, the LLVM coroutine representation is language neutral and can be used to support coroutines in other languages as well.

**Scalable Vectorization for LLVM**  
*Amara Emerson, Graham Hunter*  
[Slides](Slides/Emerson-ScalableVectorizationinLLVMIR.pdf)  
[Video](https://youtu.be/0up2hJk7k94)  
SVE is a new vector ISA extension for AArch64 targeted at HPC applications; one major distinguishing feature is that vector registers do not have a fixed size from a compiler perspective. This talk will cover the changes made to LLVM IR to support vectorizing loops in a vector length agnostic manner, as well as improvements in vectorization enabled by the predication and gather/scatter features of the extension. See https://community.arm.com/groups/processors/blog/2016/08/22/technology-update-the-scalable-vector-extension-sve-for-the-armv8-a-architecture for more details on the architecture.

**Devirtualization in LLVM**  
*Piotr Padlewski*  
[Slides](Slides/Padlewski-DevirtualizationInLLVM.pdf)  
[Video](https://youtu.be/qMhV6d3B1Vk)  
Devirtualization - changing indirect virtual calls to direct calls is important C++ optimization. This talk will cover past work on devirtualization including optimizations made by the frontend and by LLVM using !invariant.group and @llvm.assume intrinsic and different LTO tricks. The speaker will also cover interesting problems that he faced and the future work and ideas how to make devirtualization better.

**Extending LoopVectorizer towards supporting OpenMP4.5 SIMD and outer loop auto-vectorization**  
*Hideki Saito*  
[Slides](Slides/Saito-NextLevelLLVMLoopVectorizer.pdf)  
[Video](https://youtu.be/XXAvdUwO7kQ)  
Currently, LoopVectorizer in LLVM is specialized in auto-vectorizing innermost loops. SIMD and DECLARE SIMD constructs introduced in OpenMP4.0 and enhanced in OpenMP4.5 are gaining popularity among performance hungry programmers due to the ability to specify a vectorization region much larger in scope than the traditional inner loop auto-vectorization would handle and also due to several advanced vectorizing compilers delivering impressive performance for such constructs. Hence, there is a growing interest in LLVM developer community in improving LoopVectorizer in order to adequately support OpenMP functionalities such as outer loop vectorization and whole function vectorization. In this Technical Talk, we discuss our approaches in achieving that goal through a series of incremental steps and further extending it for outer loop auto-vectorization.

**Loop Passes: Adding new features while reducing technical debt**  
*Mikhail Zolotukhin*  
[Slides](Slides/Zolotukhin-LoopPasses.pdf)  
[Video](https://youtu.be/AfeUG7f5UA0)  
This year LLVM's loop passes have been greatly improved. Along with enabling new algorithms, such as new advanced loop unrolling heuristics, some long-living problems have been addressed, which resulted in significant compile time improvements and, in general, cleaner pass pipeline. We'll talk about the journey we've done along various loop passes, share our thoughts on how to avoid in future some problems we met, and share the methodology we used to find these problems.

**rev.ng: a QEMU- and LLVM-based static binary analysis framework**  
*Alessandro Di Federico*  
[Slides](Slides/DiFederico-rev.ng.pdf)  
[Video](https://youtu.be/5CbuU4KwBCE)  
rev.ng is an open-source static binary analysis framework based on QEMU and LLVM. Its core component, revamb, is a static binary translator which aims is to translate a Linux program compiled for any of the 17 ISAs supported by QEMU and produce an equivalent binary for a, possibly different, architecture supported by the LLVM compiler framework.  
revamb aims to translate and re-optimize legacy/closed source programs but can also be employed for a number of security-related purposes, such as retrofitting binary hardening techniques (e.g., CFI) or instrumenting existing binaries with good performance figures (e.g., for black box fuzzing purposes).  
More in general, rev.ng can be used to perform binary analysis on a wide range of architectures in the comfortable LLVM environment. As an example, rev.ng can be used to recover high-level information such as an accurate CFG and function boundaries from a binary program.  
At its current status, revamb is able to successfully translate the 105 coreutils binaries compiled for ARM, x86-64 and MIPS and pass over 80% of coreutils's testsuite on all of them. The programs have been linked statically, therefore they include handwritten assembly and their text is in the order of the hundreds of kilobytes.

**A New Architecture for Building Software**  
*Daniel Dunbar*  
[Slides](Slides/Dunbar-NewArchitectureForBuildingSoftware.pdf)  
[Video](https://youtu.be/b_T-eCToX1I)  
Clang was written in part to deliver fast compile times for C & C++ code. However, the traditional way C compilers integrate with build systems places many limitations on how efficiently that can be done. This talk introduces llbuild -- a new framework for building build systems -- which was designed to help solve this problem, and envisions a new architecture for compiling software which would allow us to significantly improve compilation times for large software projects.

**GVN-Hoist: Hoisting Computations from Branches**  
*Aditya Kumar, Sebastian Pop*  
[Slides](Slides/Kumar-Pop-GVNHoist.pdf)  
[Video](https://youtu.be/GB3OpqSwuUw)  
Code-hoisting identifies identical computations across the program and hoists them to a common dominator so as to save code size. Although the main goal of code-hoisting is not to remove redundancies: it effectively exposes redundancies and enables other passes like LICM to remove more redundancies. The main goal of code-hoisting is to reduce code size with the added benefit of exposing more instruction level parallelism and reduced register pressure.  
We present a code hoisting pass that we implemented in llvm. It is based on Global Value Numbering infrastructure available in llvm. The experimental results show an average of 2.5\\% savings in code size, although the code size increases in many cases because it enables more inlining. This is an optimistic algorithm in the sense that we consider all identical computations in a function as potential candidates to be hoisted. We make an extra effort to hoist candidates by partitioning the potential candidates in a way to enable partial hoisting in case common hoisting points for all the candidates cannot be found. We also formalize cases when register pressure will reduce as a result of hoisting.

**ThinLTO: Scalable and Incremental LTO**  
*Mehdi Amini, Teresa Johnson*  
[Slides](Slides/Amini-Johnson-ThinLTO.pdf)  
[Video](https://youtu.be/9OIEZAj243g)  
ThinLTO was first introduced at EuroLLVM 2015 as "A Fine-Grained Demand-Driven Infrastructure". The presentation was based on an early prototype made as a proof-of-concept. Taking this original concept, we redesign it from scratch in LLVM by extending the bitcode format, redesigning the high-level workflow to remove the "demand-driven" iterative part, and adding new capabilities such as the incremental build support. We added supports in two linkers: Gold on Linux and ld64 on Darwin.  
We propose in this presentation to go through the final design and how it is implemented in LLVM.

**Killing poison and undef -- long live poison!**  
*Juneyoung Lee, Nuno Lopes*  
[Slides](Slides/Lopes-LongLivePoison.pdf)  
[Video](https://youtu.be/_-3Iiads1EM)  
The current concept of poison in LLVM is known to be broken, leaving LLVM in a state where certain miscompilation bugs are hard or even impossible to fix. Moreover, the concepts of poison and undef values in LLVM are hard to reason about and are often misunderstood by developers.  
However, we need concepts similar to poison and undef to enable certain important optimizations.  
In this talk, we will present the motivation behind poison and undef and why they are broken. We'll also present a proposal to kill undef and extend poison, while retaining their performance benefits.  
This talk is meant to increase awareness of the issues and motivations behind poison/undef and discuss how to fix it.

**Leveraging Intermediate Forms for Analysis**  
*Jared Carlson, Ayal Spitz*  
[Slides](Slides/Carlson-LeveragingIntermediateForms.pdf)  
[Video](https://youtu.be/_xMUP09hmeM)  
In this presentation we will discuss and demonstrate an approach to build various Formal Methods (FM) tools leveraging LLVM. FM has seen a significant increase in usage in software over the past decade, being used in critical system design, security, and prototyping. We will discuss the benefits and drawbacks of LLVM IR for FM and the need for an Abstract Representation (AR) that allows for the analysis via engineering approximations. In particular we want to talk about our approach and tools that mapped our chosen AR, developed at NASA, and then extending our initial set of analysis into more logical and hierarchal relationship. Lastly we want to present what we feel are the difficulties, future challenges and successes of FM tools integrating with LLVM community.

**Compiler-assisted Performance Analysis**  
*Adam Nemet*  
[Slides](Slides/Nemet-Compiler-assistedPerformanceAnalysis.pdf)  
[Video](https://youtu.be/qq0q1hfzidg)  
Optimization diagnostics have been part of LLVM for years. While important, these diagnostics had a narrow focus on providing user feedback on the success or failure of Auto-vectorization. This work explores the possibility of extending on this foundation in order to build up a full-fledged performance analysis tool set using the compiler. The talk will first lay out the elements of this tool set. Then we will evaluate and refine it through an exploration of real- world use cases.

**Global Instruction Selection Status**  
*Ahmed Bougacha, Quentin Colombet, Tim Northover*  
[Slides](Slides/Colombet-GlobalISel.pdf)  
[Video](https://youtu.be/6tfb344A7w8)  
Last year we presented a proposal to bring up a new instruction selection framework, GlobalISel, in LLVM. This talk will show the progress made with the design and implementation of that proposal as well as pointing out the areas that need to be develop.  
As a backend developer, you will learn what it takes to start using GlobalISel for your target and as a LLVM developer, you will see which aspects of GlobalISel require your contributions.

**Dealing with Register Hierarchies**  
*Matthias Braun*  
[Slides](Slides/Braun-DealingWithRegisterHierarchies.pdf)  
[Video](https://youtu.be/-TV77T1R7OU)  
Many architectures allow addressing parts of a register independently. Be it the infamous high/low 8 bit registers of X86, the 32/64bit addressing modes of X86-64 and AArch64 or GPUs with wide loads and stores where with computation on sub register lanes.  
LLVM recently gained support to track liveness on subregister granularity. In combination with improved heuristics for register classes of varying sizes the average register count decreased for 20% for GPU shader programs.  
This talk gives an introduction to typical situations benefiting from sub register liveness modeling. It shows how a target architecture developer can model them and explains the register allocation techniques employed by llvm.

**CodeView, the Microsoft Debug Info Format, in LLVM**  
*Reid Kleckner*  
[Slides](Slides/Kleckner-CodeViewInLLVM.pdf)  
[Video](https://youtu.be/5twzd06NqGU)  
The number one piece of feedback we've heard from Windows users of Clang is that they want to be able to debug their programs in Visual Studio. More than that, though, there is a world of Windows tools, such as profilers, post-mortem crash analyzers, self-debugging tools (dbghelp), and symbol servers, that makes it really worth implementing CodeView support in LLVM. Since the last dev meeting, we've been hard at work studying the format and slowly adding support for it to LLVM. This talk will give an overview of the format, and then go back and focus on the aspects that most impacted our design decisions in Clang and LLVM. As others in the community have discovered while working on LTO, LLDB, modules, and llvm-dsymutil, type information can often end up being the dominating factor in the performance of the toolchain. CodeView has some interesting design choices for solving that problem that I will share. I will close by talking about where we want to go in the future, and how we will eventually use LLD to package our CodeView into a PDB file.

**Summary-based inter-unit analysis for Clang Static Analyzer**  
*Aleksei Sidorin*  
[Slides](Slides/Sidorin-Summery-Based-Inter-Unit-Analysis.pdf)  
[Video](https://youtu.be/jbLkZ82mYE4)  
The ability to perform interprocedural analysis is one of the most powerful features of Clang Static Analyzer. This talk is devoted to the ongoing improvement of this feature. We will discuss our implementation of summary-based interprocedural analysis as well as cross translation unit analysis. These features allow faster analysis with a greater number of potentially found bugs. We are going to describe our implementation details and approaches and discuss their pros and cons.

**Developing and Shipping Clang with CMake**  
*Chris Bieneman*  
[Slides](Slides/Bieneman-CMake.pdf)  
[Video](https://youtu.be/StF77Cx7pz8)  
In LLVM 3.8 the autoconf build system was deprecated and it was removed in favor of the newer CMake system starting in 3.9. This talk provides a brief introduction to the CMake programming language to ensure everyone basic familiarity. It will include a post-mortem on the LLVM autoconf->CMake transition, and discuss some of the useful features of the LLVM CMake build system which can improve developer productivity. We will explore a case study on packaging and shipping an LLVM toolchain with CMake including an in-depth explanation of many of the new features of the LLVM CMake build system. Lastly it will provide a status report of the current state of the build system as well as presenting some of the future improvements on the horizon.

**Reducing Code Size Using Outlining**  
*Jessica Paquette*  
[Slides](Slides/Paquette-Outliner.pdf)  
[Video](https://youtu.be/yorld-WSOeU)  
Maintaining a low code size overhead is important in computing domains where memory is a scarce resource. Outlining is an optimization which identifies similar regions of code and replaces them with calls to a function. This talk introduces a novel method of compressing code using an interprocedural outliner on LLVM MIR.

**Toy programming demo of a repository for statically compiled programs**  
*Paul Bowen-Huggett*  
[Slides](Slides/Bowen-Hugett-ToyProgrammingDemo.pdf)  
[Video](https://youtu.be/-pL94rqyQ6c)  
This talk will present a proof of concept of an approach which improves compile and link times by replacing the conventional use of object files with an incrementally updated repository without requiring change to existing build infrastructure. It aims to present the idea at a high-level using a live demo of some trivial tools and initiate discussion of a real implementation within the LLVM framework.

**Using LLVM to guarantee program integrity**  
*Simon Cook*  
[Slides](Slides/Cook-LLVM-Program-Integrity.pdf)  
[Video](https://youtu.be/isHCLMrXPUk)  
There are many embedded systems on which we rely heavily in our day to day lives, and for these it is crucial to ensure that these systems are as robust as possible. To this end, it is important to have strong guarantees about the integrity of running code. Achieving this naturally requires close integration between hardware features and compiler toolchain support for these features.  
To achieve this, an NXP architecture uses hardware signing to ensure integrity of a program's control flow from modification. Each instruction's interpretation depends on the preceding instruction in the execution flow (and hence the sequence of all preceding instructions). Basic blocks require a "correction value" to bring the system into a consistent state when arriving from different predecessors. Compiler support is needed for this such that compiled code can receive the benefits of this feature.  
Over the past year we have implemented the infrastructure for this feature which can be enabled on a per-function level in LLVM, for functions written in both C and/or assembly. In this talk we will present this system, and show how it enforces control flow integrity.  
We will explain how we have extended our target's backend with a pass that produces metadata describing a system's control flow. This allows branches and calls to be resolved with appropriate correction values. A particular challenge is dealing with function pointers and hence indirect transfers of control. We will also describe the implementation of user attributes to support such functionality in Clang.  
The encoding of each instruction, and the correction values cannot be finally determined until the final programs is linked. Using the metadata generated by LLVM, we can recreate the control flow graph for the entire program. From this, each instruction can be signed, and the correction values for each basic block inserted into the binary.  
We will finish with a demonstration of this system in action.

# Contact

To contact the organizer please email [Tanya Lattner](mailto:tanyalattner@llvm.org).

<!-- *********************************************************************** -->

* * *
