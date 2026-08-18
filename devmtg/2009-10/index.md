---
layout: "default.html"
permalink: "devmtg/2009-10/index.html"
---
# 2009 LLVM Developers' Meeting

1.  [Proceedings](#proceedings)
2.  [Attendees](#attendees)

*   **What**: The third general meeting of LLVM Developers and Users.
*   **Why**: To get acquainted, learn how LLVM is used, and exchange ideas.
*   **When**: October 2, 2009

## **SPONSORED BY: [Apple](http://apple.com), [Google](htt
p://google.com), [Adobe](http://www.adobe.com/), [Qualcomm Incorporated](http://ww
w.qualcomm.com/)**

The meeting serves as a forum for both [LLVM](http://llvm.org) and [Clang](http://clang.llvm.org) developers and users to get acquainted, lea rn how LLVM is used, and exchange ideas about LLVM and its (potential) applications. More broadly, we believe the event will be of particular interest to the following people:

*   Active LLVM and Clang developers and users.
*   Anyone interested in using LLVM or Clang.
*   Compiler, programming language, and runtime enthusiasts.
*   Those interested in using compiler technology in novel and interesting ways.

# Proceedings

The day was structured to have general overview/introduction talks about some major LLVM subsystems and talks on applications of LLVM for various specific projects.

This page lists all of the slides and videos for all of the talks of the day. The talks were held in two rooms - in one room we only were able to record a screencast, in the other room we have full video. The 'mobile' versions of the videos are in a generic 'H.264' container, and the 'computer' versions are in QuickTime format.

<!--<p>In addition to being available here, the videos are also available <a  href="http://www.youtube.com/view_play_list?p=E05430D58DF9A720">on youtube</a>.</p> -->

| Media | Who | Description |
| --- | --- | --- |
| \[[Slides](StateOfClang.pdf)\]<br>\[[Video](http://devimages.apple.com/llvm/videos/StateOfClang.mov)\] | Doug Gregor, Chris Lattner, Ted Kremenek | **State of Clang** |
| \[[Slides](Korobeynikov_BackendTutorial.pdf)\] \[[Video](https://youtu.be/mjjbrBUH1KQ)\] | Anton Korobeynikov<br>*Saint Petersburg State University* | **Tutorial: Building backend in 24 hours** - A step by step tutorial to build a backend. |
| \[[Slides](Geoffray_GarbageCollectionVMKit.pdf)\] \[[Video](https://youtu.be/LcB7V9TcNOQ)\] | Nicolas Geoffray<br>*Universite Pierre et Marie Curie* | **Precise and efficient garbage collection in VMKit with MMTk** - This talk will describe how we have added precise garbage collection in VMKit, both in the JVM and .Net runtime. The work continues in the spirit of VMKit, in that the garbage collector is an external library provided by others. We have used MMTk, a garbage collector written in Java to provide efficient and precise garbage collection. The talk will give a step by step explanation on how the new system was implemented and provide a tutorial on how this can be adopted by other kinds of VMs implemented with LLVM. Additionally, I will show the new performance results with the new garbage collector. |
| \[[Slides](Winter_UnladenSwallowLLVM.pdf)\] \[Video\] | Colin Winter<br>*Google* | **Unladen Swallow: Python on LLVM** - This talk will go into detail about Unladen Swallow, a Google-sponsored branch of CPython based on LLVM. The talk will describe the architecture of Python-on-LLVM, why we chose LLVM, how we're exploiting LLVM to increase performance, challenges we face in optimizing Python, and future direction for our work. |
| \[[Slides](Sands_LLVMGCCPlugin.pdf)\] \[[Video](https://youtu.be/EFg7Uj-V1PU)\] | Duncan Sands<br>*Deep Blue Capital* | **Reimplementing llvm-gcc as a gcc plugin** - Mainline gcc is now able to load additional logic and passes at run-time via a plugin mechanism. It may be possible to replace gcc's optimizers and code generators with those of LLVM via a plugin without needing to modify gcc at all. The goal is to obtain an equivalent of llvm-gcc in this way. I will describe the current status of this project. |
| \[[Slides](ScalarEvolutionAndLoopOptimization.pdf)\]<br>\[[Video](http://devimages.apple.com/llvm/videos/ScalarEvolutionLoopOptimizationLLVM.mov)\] | Dan Gohman | **ScalarEvolution and Loop Optimization** - LLVM's ScalarEvolution framework has undergone some major changes and now sports some cool new features. I'll give an overview of what ScalarEvolution can do, illustrate the new features, and discuss the infrastructure behind the functionality. |
| \[[Slides](Lopes_ObjectCodeEmission.pdf)\] \[[Video](https://youtu.be/VPyZBi39Ymw)\] | Bruno Cardoso Lopes<br>*University of Campinas* | **Object Code Emission and llvm-mc** - A high level overview of the LLVM Machine Code Emitter, with a specific focus on the emission of object files: the design and current implementation status. |
| \[[Slides](Greene_180k_Cores.pdf)\] \[[Video](https://youtu.be/_v9uEJx6E30)\] | David Greene<br>*Cray* | **LLVM on 180k Cores** - In this talk we'll see how Cray incorporated LLVM into an existing highly optimizing, vectorizing and parallelizing compiler. Attendees will learn about the pitfalls encountered as well as the benefits of using an Open Source codegen solution. We will also discuss various modifications to LLVM that Cray is currently in the process of integrating back into the community repository. |
| \[[Slides](Cifuentes_ParfaitBugChecker.pdf)\] \[[Video](https://youtu.be/a9v_KR4bdiU)\] | Cristina Cifuentes<br>*Sun Microsystems* | **The Parfait Bug-Checker** - Parfait is a research bug-checking project for C built on top of LLVM. Parfait is being used internally within Sun to find bugs in various applications including the Solaris(TM) operating system. Externally, Parfait is being tested in the OS community with the OpenBSD, Linux and FreeBSD kernels. In this talk we explain Parfait's design for scalability and precision, explain some of the internals of the tool and how it is built on top of LLVM, and give a demo against open source code bases. |
| \[[Slides](Petersen_OptimizingActionScriptBytecode.pdf)\] \[[Video](https://youtu.be/KUQ6yZyzA2o)\] | Scott Petersen<br>*Adobe Systems, Inc.* | **Optimizing ActionScript Bytecode using LLVM** - LLVM has state-of-the-art optimization capabilities that can operate against LLVM bitcode. But many of these optimizations are not intrinsically specific to LLVM's representation of programs. Adobe has built a proof-of-concept implementation of an ActionScript Bytecode optimizer using LLVM. This talk will discuss the implementation of the optimizer and possible future directions for this type of technology. |
| \[[Slides](Osborne_TargetingXCoreResources.pdf)\] \[[Video](https://youtu.be/DF-2gA_0QfU)\] | Richard Osborne<br>*XMOS* | **Targeting XCore resources from LLVM** - The XCore is an event driven multi-threaded processor. It provides direct hardware support for interprocess communication using channels and precise timing of inputs and outputs on I/O pins using ports. This talks looks at using LLVM to compile an version of C extended with support for explicit parallelism and I/O to the XCore. |
| \[[Slides](RegisterAllocationFutureWorks.pdf)\]<br>\[[Video](http://devimages.apple.com/llvm/videos/FutureLLVMRegister.mov)\] | Lang Hames | **Future Works in LLVM Register Allocation** - About the future of register allocation in LLVM. |
| \[[Slides](Zaks_CoVaC.pdf)\] \[[Video](https://youtu.be/iXTliWhYpRs)\] | Anna Zaks<br>*New York University* | **CoVaC: Compiler Validation by Program Analysis of the Cross-Product** - CoVaC is a framework for formal verification of the compiler optimization phase. This talk gives a brief overview of the prototype tool, which has been developed on top of LLVM 2.0. The CoVaC framework checks that optimization passes preserve semantics of the program being compiled by proving that the unoptimized program is equivalent to the optimized one. To leverage existing program analysis techniques, we reduce the equivalence checking problem to analysis of one system - a cross-product of the two input programs. The talk is based on the following paper: Compiler Validation by Program Analysis of the Cross-Product, Anna Zaks and Amir Pnueli, FM'08 |
| \[[Slides](OpenCLWithLLVM.pdf)\]<br>\[[Video](http://devimages.apple.com/llvm/videos/OpenCLandLLVM.mov)\] | Nate Begeman | **OpenCL** |
| \[[Slides](Nagarakatte_SoftBound.pdf)\] \[[Video](https://youtu.be/0nNGS8D5xDg)\] | Santosh Nagarakatte<br>*University of Pennsylvania* | **SoftBound: Highly Compatible and Complete Spatial Memory Safety for C** - SoftBound is a compile-time transformation for enforcing spatial safety of C. SoftBound records base and bound information for every pointer as disjoint metadata. This decoupling enables SoftBound to provide spatial safety without requiring changes to C source code. SoftBound is a software-only approach and performs metadata manipulation only when loading or storing pointer values. This talk provides a brief description of the formal proof and llvm implementation. |
| \[[Slides](Grover_PLANG.pdf)\] \[[Video](https://youtu.be/o-T8Dn8WX9E)\] | Vinod Grover<br>*NVIDIA* | **PLANG: Translating NVIDIA PTX language to LLVM IR Machine** - PTX is an abstract ISA, for NVIDIA GPUs, targeted by CUDA and several other tools. PTX is jitted or compiled to a supported GPU for execution. We describe PLANG, a new front-end for PTX that emits LLVM and leverages its analysis, transformation and code generation infrastructure for PTX. Based on PLANG we have built several analysis and translation tools for PTX, e.g. synchronization analysis, visualization and targeting execution of PTX on x86 processors. In this talk we will describe PLANG, and our experiences in building tools based on LLVM. |
| \[[Slides](Phoenix_AcceleratingRuby.pdf)\] \[[Video](https://youtu.be/J8Q1ljBMFjA)\] | Evan Phoenix<br>*Engine Yard* | **Accelerating Ruby with LLVM** \- Rubinius is a ruby VM that strives to write as much of the system in ruby itself as it can. To make this practical, we're using LLVM to JIT frequently used methods. I'll cover briefly the architecture of Rubinius, spending most of the time discussing the integration points. These include: Background compilation, runtime profile guide optimization, efficient IR generation, etc. |

# Attendees

We had approximately 170 attendees with a huge range of different affiliations.

<!-- *********************************************************************** -->

* * *
