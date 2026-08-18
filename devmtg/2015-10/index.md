---
layout: "default.html"
permalink: "devmtg/2015-10/index.html"
---
# 2015 LLVM Developers' Meeting

1.  [About](#about)
2.  [October 29 - Meeting Agenda](#agenda1)
3.  [October 30 - Meeting Agenda](#agenda2)
4.  [Talk Abstracts](#abstracts)
5.  [Lightning Talk Abstracts](#light)
6.  [Tutorial Abstracts](#tutorials)
7.  [BoF Abstracts](#bof)
8.  [Poster Abstracts](#poster)
9.  [Hotel](#hotel)
10.  [Reception](#reception)

*   **What**: The ninth meeting of LLVM Developers and Users.
*   **When**: October 29-30, 2015
*   **Where**: Marriott - San Jose, CA

A huge thank you to our sponsors!

# Diamond Sponsors:

#      [Apple](http://www.apple.com)

        [Apple](http://www.apple.com)

        ![](logos/quic-stack-version.jpg)  
        [QuIC](http://www.quicinc.com)

# Platinum Sponsors:

        ![](logos/Google-logo_420_color_2x.png)  
        [Google](http://google.com)

        ![](logos/psf_pos.jpg)  
        [Sony Computer Entertainment America](http://us.playstation.com/corporate/about/)

# Silver Sponsors:

        ![](logos/HSAFoundation-FINAL.PNG)  
        [HSA Foundation](http://www.hsafoundation.com)

# Bronze Sponsors:

        ![](logos/Microsoft-logo_rgb_c-gray.png)  
        [Microsoft](http://www.microsoft.com)

# About

The LLVM Foundation announces the ninth annual bay area LLVM Developers' Meeting will be held October 29th and 30th in San Jose, CA.

This year the conference will be 2 full days that include technical talks, BoFs, hacker’s lab, tutorials, and a poster session. Attendance will be capped at 350.

The meeting serves as a forum for [LLVM](http://llvm.org), [Clang](http://clang.llvm.org), [LLDB](http://lldb.llvm.org) and other LLVM project developers and users to get acquainted, learn how LLVM is used, and exchange ideas about LLVM and its (potential) applications. More broadly, we believe the event will be of particular interest to the following people:

*   Active developers of projects in the LLVM Umbrella (LLVM core, Clang, LLDB, libc++, compiler\_rt, klee, dragonegg, lld, etc).
*   Anyone interested in using these as part of another project.
*   Compiler, programming language, and runtime enthusiasts.
*   Those interested in using compiler and toolchain technology in novel and interesting ways.

Please sign up for the LLVM Developers' Meeting list for future announcements and to ask questions.  
[http://lists.llvm.org/mailman/listinfo/llvm-devmeeting](http://lists.llvm.org/mailman/listinfo/llvm-devmeeting)

You may also contact the organizer: [Tanya Lattner](mailto:tanyalattner@llvm.org)

# October 29 - Meeting Agenda

The schedule may be viewed here: [http://devmtg15.llvm.org](http://devmtg15.llvm.org).

| Media | Talk |
| --- | --- |
| Slides | **Welcome**<br>Tanya Lattner, *LLVM Foundation* |
| [Slides](slides/BastienGohman-WebAssembly-HereBeDragons.pdf)<br>[Video](https://www.youtube.com/watch?v=5W7NkofUtAw&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21&index=1) | **[WebAssembly: Here Be Dragons](#talk1)**<br>Jf Bastien, *Google*<br>Dan Gohman, *Mozilla* |
| [Slides](slides/Colombet-GlobalInstructionSelection.pdf)<br>[Video](https://www.youtube.com/watch?v=F6GGbYtae3g&index=2&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[A Proposal for Global Instruction Selection](#talk)**<br>Quentin Colombet, *Apple* |
| [Slides](slides/Doerfert-InputSpaceSplittingForOpenCL.pdf)<br>[Video](https://www.youtube.com/watch?v=py3pUnvQ7cY&index=3&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Input Space Splitting for OpenCL](#talk2)**<br>Johannes Doerfert, *Saarland University* |
| [Slides](slides/Baev-IndirectCallPromotion.pdf)<br>[Video](https://www.youtube.com/watch?v=ZeuEMLG3gVI&index=5&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Profile-based Indirect Call Promotion](#talk3)**<br>Ivan Baev, *QuIC* |
| [Slides](slides/SerebryanyCollingbourne-BeyondSanitizers.pdf)<br>[Video](https://www.youtube.com/watch?v=5K_uIda0tZU&index=4&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Beyond Sanitizers: guided fuzzing and security hardening](#talk4)**<br>Kostya Serebryany, *Google* |
| [Slides](slides/Beyls-AutomatedPerformanceTrackingOfLlvmGeneratedCode.pdf)<br>[Video](https://www.youtube.com/watch?v=9UliHoRYjZI&index=6&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Automated performance-tracking of LLVM-generated code](#talk5)**<br>Kristof Beyls, *ARM* |
| [Slides](slides/Margiolas-HeterogeneousExecutionEngineForLLVM.pdf)<br>[Video](https://www.youtube.com/watch?v=utpD3Kv7h88&index=7&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[A Heterogeneous Execution Engine for LLVM](#talk6)**<br>Christos Margiolas, *University of Edinburgh* |
| [Slides](slides/GueltonGuinet-BuildingTestingDebuggingASimpleOutOfTreePass.pdf)<br>[Video](https://www.youtube.com/watch?v=BnlG-owSVTk&index=8&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Tutorial: Building, Testing and Debugging a Simple out-of-tree LLVM Pass](#tutorial1)**<br>Serge Guelton, *Quarkslab*<br>Adrien Guinet, *Quarkslab* |
| [Slides](slides/Saulais-CreatingSPMDVectorizerOpenCL.pdf)<br>[Video](https://www.youtube.com/watch?v=ePu6c4FLc9I&index=9&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Tutorial: Creating an SPMD Vectorizer for OpenCL with LLVM](#tutorial2)**<br>Pierre-Andre Saulais, *Codeplay Software* |
| [Slides](slides/DoerfertGrosser-OptimisticAssumptionsInPolly.pdf)<br>[Video](https://www.youtube.com/watch?v=mIBUY20d8c8&index=10&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Tutorial: Polly - Optimistic Loop Nest Optimizations with Schedule Trees](#tutorial3)**<br>Tobias Grosser, *ETH Zurich*<br>Johannes Doerfert, *Saarland University* |
| [Slides](slides/RobinsonEdwards-LivingDownstreamWithoutDrowning.pdf)<br>[Video](https://www.youtube.com/watch?v=INCi9gOVMug&index=11&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Tutorial/BoF: Living Downstream Without Drowning](#tutorial4)**<br>Paul Robinson, *Sony Computer Entertainment*<br>Michael Edwards, *Sony Computer Entertainment* |

# October 30 - Meeting Agenda

The schedule may be viewed here: [http://devmtg15.llvm.org](http://devmtg15.llvm.org).

| Media | Talk |
| --- | --- |
| [Slides](slides/GroffLattner-SILHighLevelIR.pdf)<br>[Video](https://www.youtube.com/watch?v=Ntj8ab-5cvE&index=12&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Swift's High-Level IR: A Case Study of Complementing LLVM IR with Language-Specific Optimization](#talk7)**<br>Joseph Groff, *Apple Inc.*<br>Chris Lattner, *Apple Inc.* |
| [Slides](slides/Blaikie-OpaquePointerTypes.pdf)<br>[Video](https://www.youtube.com/watch?v=OWgWDx_gB1I&index=13&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Typeless Pointers in LLVM IR](#talk8)**<br>David Blaikie, *Google Inc.* |
| [Slides](slides/Gerolf-PerformanceImprovementsAndHeadroom.pdf)<br>[Video](https://www.youtube.com/watch?v=mLhDzqKdUCQ&index=14&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[LLVM Performance Improvements and Headroom](#talk9)**<br>Gerolf Hoflehner, *Apple* |
| [Slides](slides/Wu-OptimizingLLVMforGPGPU.pdf)<br>[Video](https://www.youtube.com/watch?v=9TlR9hNZbck&index=15&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Optimizing LLVM for GPGPU](#talk10)**<br>Jingyue Wu, *Google Inc.* |
| [Slides](slides/KlecknerMajnemer-ExceptionHandling.pdf)<br>[Video](https://www.youtube.com/watch?v=JHfb8z-iSYk&index=16&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Exception handling in LLVM, from Itanium to MSVC](#talk11)**<br>Reid Kleckner, *Google*<br>David Majnemer, *Google* |
| [Slides](slides/WongBataev-OpenMPGPUAcceleratorsComingOfAgeInClang.pdf)<br>[Video](https://www.youtube.com/watch?v=1S2A0VWGOws&index=17&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[OpenMP GPU/Accelerator support Coming of Age in Clang](#talk12)**<br>Michael Wong, *IBM*<br>Alexey Bataev, *Intel* |
| [Slides](slides/JasperKlimek-UpdateOnClangBasedTooling.pdf)<br>[Video](https://www.youtube.com/watch?v=1S2A0VWGOws&index=17&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[An update on Clang-based C++ Tooling](#talk13)**<br>Daniel Jasper, *Google*<br>Manuel Klimek, *Google* |
| [Slides](slides/DasReames-LLVMForAManagedLanguage.pdf)<br>[Video](https://www.youtube.com/watch?v=3G2Rg6GBXqA&index=19&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[LLVM for a managed language: what we've learned](#talk14)**<br>Sanjoy Das, *Azul Systems*<br>Philip Reames, *Azul Systems* |
| [Slides](slides/Porpodas-ThrottlingAutomaticVectorization.pdf)<br>[Video](https://www.youtube.com/watch?v=xxtA2XPmIug&index=20&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Throttling Automatic Vectorization: When Less Is More](#talk15)**<br>Vasileios Porpodas, *University of Cambridge* |
| [Slides](slides/SimmersPanchenko-LLVMBackendForHHVM.pdf)<br>[Video](https://www.youtube.com/watch?v=VZ7A7t5LcR8&index=21&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[LLVM back end for HHVM/PHP](#talk16)**<br>Brett Simmers, *Facebook, Inc.*<br>Maksim Panchenko, *Facebook, Inc.* |
| [Slides](slides/Nema-LoopVersioningLICM.pdf)<br>[Video](https://www.youtube.com/watch?v=VxRjJmkFsgM&index=22&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[LoopVersioning LICM](#talk17)**<br>Ashutosh Nema, *AMD* |
| [Slides](https://docs.google.com/presentation/d/1oxNHaVjA9Gn_rTzX6HIpJHP7nXRua_0URXxxJ3oYRq0/edit#slide=id.p)<br>[Video](https://www.youtube.com/watch?v=rXi065XC6zY&index=23&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Compiling large, real-world codebases with clang on Windows](#talk18)**<br>Hans Wennborg, *Google Inc.*<br>Nico Weber, *Google Inc.* |
| [Slides](slides/Prantl-ExonSmith-DebugInfoMetadataToModules.pdf)<br>[Video](https://www.youtube.com/watch?v=EgkZ8PTNSHQ&index=24&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Debug Info: From Metadata to Modules](#talk19)**<br>Duncan Exon Smith, *Apple*<br>Adrian Prantl, *Apple* |
| [Slides](slides/NemetZolotukhin-AdvancesInLoopAnalysisFrameworksAndOptimizations.pdf)<br>[Video](https://www.youtube.com/watch?v=XvkLHIASlp8&index=25&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21) | **[Advances in Loop Analysis Frameworks and Optimizations](#talk20)**<br>Adam Nemet - Apple Inc.<br>Michael Zolotukhin, *Apple Inc.* |

# Talk Abstracts

**WebAssembly: Here Be Dragons**  
*Jf Bastien - Google*  
*Dan Gohman - Mozilla*  
[Slides](slides/BastienGohman-WebAssembly-HereBeDragons.pdf)  
[Video](https://www.youtube.com/watch?v=5W7NkofUtAw&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21&index=1)  
WebAssembly is a tale of four browser vendors, seeking new languages and capabilities while staying fast, secure and portable. The old JavaScript wizard still has many spells under its belt, but it seeks a companion on its quest to reach VM utopia. WebAssembly is that companion.  
In this quest, mad alchemist Dan and jester JF will detail their exploration of LLVM-land. You’ll get to witness firsthand their exploration of ISel and MI, hear of their wondrous encounter with MC, and gasp at the Spell of Restructuring wherein SSA+CFG is transmuted into regs+AST. Will our adventurers conquer the Target and capture the virtual ISA?  
Join us in this exciting tale to which \*you\* are the hero!

**A Proposal for Global Instruction Selection**  
*Quentin Colombet - Apple*  
[Slides](slides/Colombet-GlobalInstructionSelection.pdf)  
[Video](https://www.youtube.com/watch?v=F6GGbYtae3g&index=2&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  
Our existing instruction selection framework, SelectionDAGISel (SDISel), has some fundamental limitations, including, but not limited to, slow compile time, basic block only scope, and monolithic approach. Over the years, we spent a lot of effort to workaround these limitations with more target hooks and more optimizations passes (e.g., CodeGenPrepare, ConstantHoisting) with their own problems (inaccurate heuristic, have to predict what the instruction selector will do, etc.) and limitations. We believe that it is time to come up with a new instruction selection framework, global-isel, that will solve these problems while offering new opportunities to improve our code generation. In this talk, we will present our plan to bring global-isel to LLVM.

**Input Space Splitting for OpenCL**  
*Johannes Doerfert - Saarland University*  
[Slides](slides/Doerfert-InputSpaceSplittingForOpenCL.pdf)  
[Video](https://www.youtube.com/watch?v=py3pUnvQ7cY&index=3&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

OpenCL programs are prone to memory and control flow divergence. When  implementing OpenCL for machines with explicit SIMD instructions,  compilers can usually generate more efficient code if they can prove  non-divergence of memory and branch instructions. To this end, they  leverage a so-called divergence analysis. However, in practice  divergence is often input-dependent and exhibited for some, but not  all inputs. Hence, static analyses fail to prove non-divergence. To  obtain good performance, developers can manually split the input  space, however this is a tedious and error prone task.  
 In this talk we present a new OpenCL to CPU compiler pipeline that  addresses this problem by automatically ensuring divergence free  control flow through program specialization.  To this end we represent  the full kernel as well as the implicit work item dimensions in the  polyhedral model. For data dependent control flow and non-affine  expression overapproximation is used. From the polyhedral iteration  domains and memory access functions we can then derive conditions for  the absence of memory as well as control divergence.  Based one these  conditions the input space is split in order to generate specialized  kernel versions with beneficial divergence characteristics.  Commonly  large parts of the input exhibit regular access and control patterns  and only a fixed size boundary of the input space does not. In such  cases we can achieve speedups almost as high as the used vectorization  with. However, also for non-diverging kernels our technique can  improve the performance due to simplifications in the polyhedral  model.

**Profile-based Indirect Call Promotion**  
*Ivan Baev - QuIC*  
[Slides](slides/Baev-IndirectCallPromotion.pdf)  
[Video](https://www.youtube.com/watch?v=ZeuEMLG3gVI&index=5&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

Indirect call promotion (ICP) is the second most profitable profile-based optimization according to a recent study. This talk will present LLVM ICP pass that iterates over all indirect call sites in the module and selectively transforms them. We will discuss how subsequent optimizations in the compiler pipeline may benefit from ICP.

**Beyond Sanitizers: guided fuzzing and security hardening**  
*Kostya Serebryany - Google*  
[Slides](slides/SerebryanyCollingbourne-BeyondSanitizers.pdf)  
[Video](https://www.youtube.com/watch?v=5K_uIda0tZU&index=4&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

The Sanitizers (AddressSanitizer and friends) allow you to find many stability and security bugs in C++ code, but they are only as good as your tests are. In this talk we will show how to improve your test coverage with guided fuzzing (libFuzzer) and how to protect your applications in production even if some bugs are still there (Control Flow Integrity and SafeStack).

**Automated performance-tracking of LLVM-generated code**  
*Kristof Beyls - ARM*  
[Slides](slides/Beyls-AutomatedPerformanceTrackingOfLlvmGeneratedCode.pdf)  
[Video](https://www.youtube.com/watch?v=9UliHoRYjZI&index=6&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

Ensuring that top-of-trunk consistently generates high-quality code remains harder than it should be. Continuous integration (CI) setups that track correctness of top-of-trunk work pretty well today since they automatically report correctness regressions with low false positive rate to committers. In comparison, the output generated by CI setups that track performance require far more human effort to interpret.  
In this talk, I’ll describe why I think effective performance tracking is hard and what problems need solving, with a focus on our real world experiences and observations.  
As part of the bring-up of one of the public performance tracking bots, I’ve done an in-depth analysis of its performance and noise characteristics. The insights gained from this analysis drove a number of improvements to LNT and the test-suite in the past year. I hope that sharing these insights will help others in setting up low-noise performance-tracking bots.  
I’ll conclude by summarizing what seem to be the most important missing pieces of CI functionality to make the performance-tracking infrastructure as effective as the correctness-tracking infrastructure.

**A Heterogeneous Execution Engine for LLVM**  
*Christos Margiolas - University of Edinburgh*  
[Slides](slides/Margiolas-HeterogeneousExecutionEngineForLLVM.pdf)  
[Video](https://www.youtube.com/watch?v=utpD3Kv7h88&index=7&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

Hexe, which stands for Heterogeneous Execution Engine, is an new compiler component that integrates with the LLVM infrastructure. It targets efficient computation on heterogeneous platforms by allowing the automatic offloading of workloads on computational accelerators, such as Graphics Processing Units (GPUs) or Digital Signal Processors(DSPs).  
The workloads we consider for offloading are either explicitly annotated by the programmer or automatically detected by static compiler analysis and runtime checks. Our infrastructure operates at the level of LLVM intermediate representation and effectively supports multiple source languages.  
Hexe consists of a set of compiler passes and a runtime environment. The compiler passes perform the required code analysis and transformations to enable workload offloading. The runtime environment manages data transfers and synchronization operations, and performs dynamic workload scheduling.  
We consider a diverse set of heterogeneous systems ranging from mobile devices equipped with arm based multi-core CPUs, embedded GPUs and DSPs to data center nodes consisting of x86 multi-cores and high-end GPUs. Hexe has a modular design where new accelerator types and programming environments can be supported via a plugin interface. We also consider interoperability between Hexe and modern JIT technologies, such as LLVM MCJIT.

**Swift's High-Level IR: A Case Study of Complementing LLVM IR with Language-Specific Optimization**  
*Joseph Groff - Apple Inc.*  
*Chris Lattner - Apple Inc.*  
[Slides](slides/GroffLattner-SILHighLevelIR.pdf)  
[Video](https://www.youtube.com/watch?v=Ntj8ab-5cvE&index=12&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

The Swift programming language is built on LLVM and uses LLVM IR and the LLVM backend for code generation, but it also contains a new high-level IR called SIL to model the semantics of the language (and perform optimizations) at a higher level. In this talk, we discuss the motivations and applications of SIL, including high-level semantic analyses and transformations such as flow-dependent diagnostics, devirtualization, specialization, reference counting optimization, and TBAA, and we compare SIL's design with that of LLVM IR.

**Typeless Pointers in LLVM IR**  
*David Blaikie - Google Inc.*  
[Slides](Blaikie-OpaquePointerTypes.pdf)  
[Video](https://www.youtube.com/watch?v=OWgWDx_gB1I&index=13&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

In an effort to simplify and canonicalize LLVM IR surrounding pointer expressions, the type information from pointers is being removed. Hear about the current changes, utilities for updating your test cases, as well as current open questions and future work.

**LLVM Performance Improvements and Headroom**  
*Gerolf Hoflehner - Apple*  
[Slides](slides/Gerolf-PerformanceImprovementsAndHeadroom.pdf)  
[Video](https://www.youtube.com/watch?v=mLhDzqKdUCQ&index=14&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

While LLVM is known for very fast compile-time, many developers in the community also push for improving run-time performance of generated code. This talk highlights this year’s performance gains on AArch64 in key benchmarks like SPEC2006, Kernels and also the llvm test suite. While progress has been impressive more work needs to be done. Therefore we will discuss future performance headroom which involves both expanding existing and architecting new optimizations.

**Optimizing LLVM for GPGPU**  
*Jingyue Wu - Google Inc.*  
Slides  
[Video](https://www.youtube.com/watch?v=JHfb8z-iSYk&index=16&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

This talk presents Google’s effort of optimizing LLVM for CUDA. When we started this effort, LLVM was well-tuned for CPUs but there had been little public work on improving its GPU performance. We developed, tuned, and augmented several general and CUDA-specific optimization passes. As a result, our LLVM-based compiler generates better code than nvcc on key end-to-end internal benchmarks and is on par with nvcc on a variety of open-source benchmarks.

**Exception handling in LLVM, from Itanium to MSVC**  
*Reid Kleckner - Google*  
*David Majnemer - Google*  
[Slides](slides/KlecknerMajnemer-ExceptionHandling.pdf)  
[Video](https://www.youtube.com/watch?v=9TlR9hNZbck&index=15&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

This talk covers the design and implementation of MSVC-compatible exception handling in Clang and LLVM. Unlike the Itanium C++ exception handling model, the Windows exception handling model is not designed around successive unwinding. As a result, the existing LLVM landingpad instruction is insufficient for expressing how Windows exceptions should be handled. To support Windows exceptions, we added the new token type and a family of new EH pad instructions to LLVM. This talk describes the final design of the new representation and the tradeoffs we made along the way.

**OpenMP GPU/Accelerator support Coming of Age in Clang**  
*Michael Wong - IBM*  
*Alexey Bataev - Intel*  
[Slides](slides/WongBataev-OpenMPGPUAcceleratorsComingOfAgeInClang.pdf)  
[Video](https://www.youtube.com/watch?v=dCdOaL3asx8&index=18&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

GPU/Accelerator computing will be the basis for the future of Exacale computing through the DOE's CORAL project. It is also the basis for future features for C++ Std's SG14's Games Development/Low Latency/Real Time/Graphics Study Group. However, llvm currently lacks a unified platform-neutral infrastructure for offloading to GPUs/Accelerators, which severely limits clang/llvm usage in these hugely important application domains.  
For the past several years, a number of contributors from AMD, Argonne National Lab., IBM, Intel, Texas Instruments, University of Houston and many others have come together to deliver OpenMP support to clang. OpenMP 3.1 is now officially in clang 3.7 and work continues to completion of OpenMP 4 aiming for clang 3.8. One of the most important features of OpenMP 4 standard is a vendor- and platform-neutral support for Accelerators.  
The main presenters will be the OpenMP CEO and Chair of ISO C++'s SG5/SG14 along with the main developer who has been delivering OpenMP implementation in clang (with the help of many others). This talk will describe how GPU and Accelerators will be supported in clang. It offers an overview of the OpenMP 4 syntax, and a description of the upstreaming progress in both clang and llvm through this continued collaboration, as well as the offloading interface design that will describe target independent support across many hardware targets including Nvidia, Xeon Phi, ARM, and AMD devices.

**An update on Clang-based C++ Tooling**  
*Daniel Jasper - Google*  
*Manuel Klimek - Googl*  
[Slides](slides/JasperKlimek-UpdateOnClangBasedTooling.pdf)  
[Video](https://www.youtube.com/watch?v=1S2A0VWGOws&index=17&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

This talk is going to give an update of the C++ tooling we are building on top of clang. Among others, it will focus on clang-tidy, a tool to statically analyze source code to diagnose and fix typical programming errors like style violations, interface misuse, or bugs. We'll give an update on the direction this project is taking, new checks that are being integrated and challenges we are facing. In a live demo, we'll show how we can fix specific problems throughout LLVM's own codebase. We'll also show how a new check can be added in a matter of minutes and how other Clang-based tools can help with its development.

**LLVM for a managed language: what we've learned**  
*Sanjoy Das - Azul Systems*  
*Philip Reames - Azul Systems*  
[Slides](slides/DasReames-LLVMForAManagedLanguage.pdf)  
[Video](https://www.youtube.com/watch?v=3G2Rg6GBXqA&index=19&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

For a little over a year we have been working towards a production quality, state of the art LLVM based JIT compiler for Java. This talk focuses on what we've learned about LLVM's strengths and weaknesses as an optimization framework for Java-like languages. We will discuss interesting challenges in efficiently implementing Java's semantics within LLVM IR, and how we've been growing LLVM towards being a more effective compiler for managed languages.

**Throttling Automatic Vectorization: When Less Is More**  
*Vasileios Porpodas - University of Cambridge*  
[Slides](slides/Porpodas-ThrottlingAutomaticVectorization.pdf)  
[Video](https://www.youtube.com/watch?v=xxtA2XPmIug&index=20&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

SIMD vectors are widely adopted in modern general purpose processors as they can boost performance and energy efficiency for certain applications.  
Compiler-based automatic vectorization is one approach for generating code that makes efficient use of the SIMD units, and has the benefit of avoiding hand development and platform-specific optimizations.  
The Superword-Level Parallelism (SLP) vectorization algorithm is the most well-known implementation of automatic vectorization when starting from straight-line scalar code, and is implemented in several major compilers.  
The existing SLP algorithm greedily packs scalar instructions into vectors starting from stores and traversing the data dependence graph upwards until it reaches loads or non-vectorizable instructions.  
Choosing whether to vectorize is a one-off decision for the whole graph that has been generated.  
This, however, is suboptimal because the graph may contain code that is harmful to vectorization due to the need to move data from scalar registers into vectors. The decision does not consider the potential benefits of throttling the graph by removing this harmful code.  
In this work we propose a solution to overcome this limitation by introducing Throttled SLP (TSLP), a novel vectorization algorithm that finds the optimal graph to vectorize, forcing vectorization to stop earlier whenever this is beneficial.  
Our experiments show that TSLP improves performance across a number of kernels extracted from widely-used benchmark suites, decreasing execution time compared to SLP by 9% on average and up to 14% in the best case.

**LLVM back end for HHVM/PHP**  
*Brett Simmers - Facebook, Inc.*  
*Maksim Panchenko - Facebook, Inc.*  
[Slides](slides/SimmersPanchenko-LLVMBackendForHHVM.pdf)  
[Video](https://www.youtube.com/watch?v=VZ7A7t5LcR8&index=21&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

The Hip-Hop Virtual Machine (HHVM) is a JIT compiler for executing PHP programs. It is used by some of the world’s largest websites such as facebook.com and wikipedia.org, among many others. At Facebook we have frequently been asked why we don't use LLVM as a back end for HHVM. Inspired by the success of Apple’s FTL we implemented an alternative back end using LLVM.  
In this talk we will share what it took to hook LLVM in to HHVM from conception to running limited production traffic. We will cover changes to our internal IR and modifications we had to make to LLVM. We will discuss performance challenges we faced, peculiar bugs, and finally will discuss why we are not yet at the point of enabling the LLVM back end for production Facebook traffic.

**LoopVersioning LICM**  
*Ashutosh Nema - AMD*  
[Slides](slides/Nema-LoopVersioningLICM.pdf)  
[Video](https://www.youtube.com/watch?v=VxRjJmkFsgM&index=22&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

Loop invariant code motion is an important compiler optimization and it moves invariant instructions out of a loop without affecting the semantics of a program. For safety it ensures the alias dependencies before moving invariant out of loop. In some cases memory aliasing may make this optimization ineffective. This results in possible missed opportunities in speeding up applications.  
LoopVersioning LICM is a step to exploit those missed opportunities where memory aliasing may make LICM optimization ineffective.

**Compiling large, real-world codebases with clang on Windows**  
*Hans Wennborg - Google Inc.*  
*Nico Weber - Google Inc.*  
[Slides](https://docs.google.com/presentation/d/1oxNHaVjA9Gn_rTzX6HIpJHP7nXRua_0URXxxJ3oYRq0/edit#slide=id.p)  
[Video](https://www.youtube.com/watch?v=rXi065XC6zY&index=23&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

llvm 3.7 is the first release that can build large projects such as Chromium on Windows without having to fall back to Visual Studio's compiler for a single translation unit. This talk gives an overview of the work done to get to this state: It covers language extensions clang needed to learn to parse Microsoft's headers and dark corners of the Microsoft ABI, with a focus on work done in the last year. Much of the Windows support was developed in tight collaboration between the Chromium and LLVM projects. The talk also touches on how this collaboration works and why it’s successful. Finally, the talk also gives an overview of how to get projects building with clang that build with Visual Studio.

**Debug Info: From Metadata to Modules**  
*Duncan Exon Smith - Apple*  
*Adrian Prantl - Apple*  
[Slides](slides/Prantl-ExonSmith-DebugInfoMetadataToModules.pdf)  
[Video](https://www.youtube.com/watch?v=EgkZ8PTNSHQ&index=24&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

The efficiency of debug info in LLVM and Clang improved dramatically this year.  This talk is about what it took to get here and what work remains.  
We'll talk about how Metadata was redesigned to make the debug info IR memory-efficient (with a human-readable assembly syntax).  We'll go into the implications for other Metadata graphs, and what a more expressive Metadata future could look like.  We'll also include an overview of what's left to scale debug info for LTO.  
We'll also talk about Clang's new module debugging feature, which reduces the size of debug info on disk, improves compile time, and makes full type information available to debuggers.  We'll highlight how Clang-based debuggers like LLDB can use module debug information to enhance expression evaluation.

**Advances in Loop Analysis Frameworks and Optimizations**  
*Adam Nemet - Apple Inc.  
*Michael Zolotukhin - Apple Inc.*  
[Slides](slides/NemetZolotukhin-AdvancesInLoopAnalysisFrameworksAndOptimizations.pdf)  
[Video](https://www.youtube.com/watch?v=Y0c8rPf9ihU&index=33&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

The talk will survey recent advances in loop analysis frameworks to support optimizations like unrolling, distribution, loop-aware load-elimination and multi-versioning. A significant part of our contribution was to rethink and re-design existing analysis frameworks to make them both more powerful and more widely accessible. The major part of this talk will focus on introducing these analysis frameworks and how they are used by optimizations. We will also discuss how they integrate with other analysis passes and outline ideas for their future evolution.*

# Tutorial Abstracts

*

**Tutorial: Building, Testing and Debugging a Simple out-of-tree LLVM Pass**  
*Serge Guelton - Quarkslab*  
*Adrien Guinet - Quarkslab*  
[Slides](slides/GueltonGuinet-BuildingTestingDebuggingASimpleOutOfTreePass.pdf)  
[Video](https://www.youtube.com/watch?v=BnlG-owSVTk&index=8&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

This tutorial aims at providing solid ground to develop out-of-tree LLVM passes. It presents all the required building blocks, starting from scratch: cmake integration, llvm pass management, opt / clang integration. It presents the core IR concepts through two simple obfuscating passes: the SSA form, the CFG, PHI nodes, IRBuilder etc. We also take a quick tour on analysis integration through dominators. Finally, it showcases how to use cl and lit to parametrize and test the toy passes developed in the tutorial.

**Tutorial: Creating an SPMD Vectorizer for OpenCL with LLVM**  
*Pierre-Andre Saulais - Codeplay Software*  
[Slides](slides/Saulais-CreatingSPMDVectorizerOpenCL.pdf)  
[Video](https://www.youtube.com/watch?v=ePu6c4FLc9I&index=9&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

Processors such as CPUs or DSPs often feature SIMD instructions, but are not designed to efficiently support Single Program Multiple Data (SPMD) execution models such as OpenCL. The design of a compiler for such a target therefore needs some form of vectorization to generate the most optimal code for this kind of data-parallel execution model. This is because SPMD programs are most often written in scalar form with the implicit assumption that many instances of the program are executed in parallel. On CPU-like architectures, SIMD vector units can be leveraged for parallelism, such that each SIMD lane is loosely mapped to a program instance.  
This tutorial looks at how to create an SPMD vectorizer that targets CPU-like architectures for use with heterogeneous compute frameworks. OpenCL is used as an example but the concepts should translate to other frameworks such as CUDA, RenderScript or Vulkan Compute. While there are other possible approaches, we have chosen to present one that works at the LLVM IR level and that is essentially an IR pass that creates vectorized functions from the original scalar SPMD function. This allows targetting multiple architectures with very little architecture-specific code.  
We will start by briefly introducing the SPMD execution model, describing how it is used in OpenCL and giving an overview of what a SPMD vectorizer should do and how it differs from other kinds such as LLVM's loop vectorizer and SLP vectorizer. Then we will look at a possible vectorizer design, including the different vectorization stages (analysis, control-flow to data-flow, scalarization, packetization/instantiation and optimization/cleanup). Finally, we will look at some possible optimizations as well as other aspects that do not fit the 'stage-by-stage' presentation (e.g. vectorizing and scalarizing calls to builtin functions, SIMD width detection, interleaved memory access optimizations, SoA to AoS conversions, etc).

**Tutorial: Polly - Optimistic Loop Nest Optimizations with Schedule Trees**  
*Tobias Grosser - ETH Zurich*  
*Johannes Doerfert - Saarland University*  
[Slides](slides/DoerfertGrosser-OptimisticAssumptionsInPolly.pdf)  
[Video](https://www.youtube.com/watch?v=mIBUY20d8c8&index=10&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

Polly is an advanced LLVM loop nest optimizer that provides precise memory access analyses and implements on top of them advanced loop optimizations based on a memory-access focused program model.  
In the first part of this tutorial we introduce the audience to  integer set based schedule trees as a way to model loop programs. We explain how we statically model program behavior on the granularity of individual dynamic computations and discuss different program analyses (memory accesses, data-dependences, computational complexity).  
We then learn how to perform complex loop transformations using simple per-node operations on an abstract program schedule tree. Such transformations include most classical loop transformations, but also full/partial tile separation, outer-loop vectorization and other more complex transformations. At the end of the first part of this tutorial, the audience understands the general concepts used in Polly.  
The second part of this tutorial is focused on Polly's new optimistic optimization infrastructure that enables non-statically provable transformations to be performed optimistically. Discussing optimization blocking issues such as exception handling code, infinite loops, integer wrapping or out-of-bound memory accesses we introduce the concept of optimistic assumptions. We then discuss how such assumptions can be described in general, how Polly can collect assumptions, how redundant assumptions are eliminated and how a (close to) minimal run-time check to verifying them are generated. At the end of the second part of this tutorial the audience will be able to create optimistic loop optimizations even for cases that lack sufficient static information.

**Tutorial/BoF: Living Downstream Without Drowning**  
*Paul Robinson - Sony Computer Entertainment*  
*Michael Edwards - Sony Computer Entertainment*  
[Slides](slides/RobinsonEdwards-LivingDownstreamWithoutDrowning.pdf)  
[Video](https://www.youtube.com/watch?v=INCi9gOVMug&index=11&list=PL_R5A0lGi1AA4Lv2bBFSwhgDaHvvpVU21)  

Have you made changes to your copy of an llvm.org project? Not planning to contribute them back to the open-source project right away? Then you are LIVING DOWNSTREAM.  
Have you noticed that there are actually quite a lot of changes made to the upstream projects? Clang + LLVM together see an average of 50 commits every day. This is a FLOOD.  
Are you seeing lots of conflicts or test failures when you merge from upstream? Spending too much time patching things back together before you can make any progress on your project? Then you are DROWNING!  
On a project with lots of local changes, managing the flood can be a half-time job all by itself. It's not \_exactly\_ unproductive time, but it's time you do not spend on your unique project and customizations.  
At Sony Computer Entertainment, we were drowning... but we've learned to swim with the current, and we are building a lifeboat. In this combined tech-talk/BOF session, Paul and Mike will talk about SCE's practices and plans for reducing our merge overhead, including source-patch practices and merge/build/test automation. Then, it becomes a BOF where everyone can share their ideas, suggestions and practices for Living Downstream Without Drowning!

# Lightning Talk Abstracts

# BoF Abstracts

# Poster Abstracts

# Reception

The reception will be held on Thursday, October 29 from 6PM-10PM at [SP2 Communal Bar & Restaurant](http://www.sp2sanjose.com) A reception ticket is required to attend this event. Drinks and food will be provided.

SP2 Communal Bar & Restaurant  
72 N Almaden Ave.  
San Jose, CA 95110  

# Hotel

[San Jose Marriott](http://www.marriott.com/hotels/travel/sjcsj-san-jose-marriott/)  
301 South Market Street  
San Jose, CA 95113

We have negotiated a room block for our attendees:

LLVM Foundation Developers Meeting  

Start date: 10/28/15  
End date: 10/31/15  
Last day to book: 10/7/15  
Marriott hotel(s) offering your special group rate:  

San Jose Marriott for 229.00 USD per night  
[Book your group rate for LLVM Foundation Developers Meeting](http://www.marriott.com/meeting-event-hotels/group-corporate-travel/groupCorp.mi?resLinkData=LLVM%20Foundation%20Developers%20Meeting%5Esjcsj%60llvllva%60229.00%60USD%60false%604%6010/28/15%6010/31/15%6010/7/15&app=resvlink&stop_mobi=yes)

# Parking

You can find parking at the San Jose Marriott (valet only) and the San Jose Convention Center.

Rates:  
San Jose Marriott Valet parking:

*   First 30 Minutes $8
*   Up to 1 hour $14
*   1 to 2 hours $20
*   2 to 4 hours $26
*   4-5 hours $32
*   5-24 hours $34

San Jose Convention Center Parking: $1 per 20 min, $20 daily maximum Monday - Sunday, special rates as posted at facility may apply during special event ([http://www.sanjose.org/maps-more/parking/](http://www.sanjose.org/maps-more/parking/)).

<!-- *********************************************************************** -->

* * *

*
