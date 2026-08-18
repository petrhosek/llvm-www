---
layout: "default.html"
permalink: "devmtg/2019-02-16/index.html"
---
# Third LLVM Performance Workshop at CGO

*   **What**: Third LLVM Performance Workshop at CGO
*   **When**: **Sunday February 17th**, 2019
*   **Where**: **Georgetown University Room**, Washington DC, USA

An LLVM Performance Workshop will be held at CGO 2019. The workshop is co-located with CC, HPCA, and PPoPP. It takes place at [Marriott Marquis](http://cgo.org/cgo2019/venue/) in Washington DC. If you are interested in attending the workshop, please register at the [CGO website.](http://cgo.org/cgo2019/workshops.html)

# Preliminary Schedule

| **Time** | **Room** | **Speaker** | **Title** |   |
| --- | --- | --- | --- | --- |
| 9:00 | tba | Joel E. Denny | Clacc: Translating OpenACC to OpenMP in Clang | [\[Abstract\]](#jed) |
| 9:40 | tba | Ayal Zaks | Tiling Loops for Scratch-Pad Memories | [\[Abstract\]](#az) |
| 10:20-10:40 |   | Break |
| 10:40 | tba | Brian Homerding | Enabling math function call optimization for DOE proxy applications | [\[Abstract\]](#bh) |
| 11:20 | tba | Alexandru Susu | Emulating Arithmetic Operations with LLVM's Instruction Selection Pass | [\[Abstract\]](#as) |
| 12:00-13:30 |   | Lunch |
| 13:40 | tba | Simon Moll | Multi-dimensional Vectorization in LLVM | [\[Abstract\]](#sm) |
| 14:20 | tba | Johannes Doerfert | Performance Gap Exploration with LLVM | [\[Abstract\]](#jd) |
| 15:00-15:20 |   | Break |
| 15:20 | tba |   | LLVM Q&A Panel: **Questions Welcome** |   |
| 16:00 |   | Workshop ends. |

# Abstracts

*   **Joel E. Denny, Seyong Lee, and Jeffrey S. Vetter**: Clacc: Translating OpenACC to OpenMP in Clang

    OpenACC was launched in 2010 as a portable programming model for heterogeneous accelerators. Although various implementations already exist, no extensible, open-source, production-quality compiler support is available to the community. This deficiency poses a serious risk for HPC application developers targeting GPUs and other accelerators, and it limits experimentation and progress for the OpenACC specification. To address this deficiency, Clacc is a recent effort funded by the US Exascale Computing Project to develop production OpenACC compiler support for Clang and LLVM. A key feature of the Clacc design is to translate OpenACC to OpenMP to build on Clang's existing OpenMP compiler and runtime support. In this talk, we describe the Clacc goals and design. We also describe the challenges that we have encountered so far in our prototyping efforts, and we present some early performance results.

*   **Ayal Zaks, Michael Zuckerman, and Dorit Nuzman**: Tiling Loops for Scratch-Pad Memories

    Tiling a loop is a well-known code transformation that helps optimize temporal locality. Tiling is important for systems that have caches in order to achieve high performance. For systems that are based on scratch-pad memories or software-managed caches, tiling is vital in order for code to be functional. Furthermore, due to the high overhead of transferring data between main memory and scratch-pad memory, it is desirable to tile several loops together. Lastly, if such data transfers can be executed asynchronously and in parallel to processing the data in the scratch-pad memories, careful scheduling of the transfers and double-buffering of the data are desired in order to hide data transfer overheads. In this work we show how multiple loops can be tiled together in order to execute them efficiently on systems with scratch-pad memories.

*   **Brian Homerding**: Enabling math function call optimization for DOE proxy applications

    The US Department of Energy proxy applications are simplified applications that are representative of the important code for various scientific computing workloads. Our performance analysis work on these proxy applications have revealed some areas where Clang can improve when compared to GCC and vendor compilers. Among these is the limited ability to apply optimizations to math function calls when we care about errno. This talk will discuss modeling the memory behavior of math functions using function attributes in order to enable these optimizations. Along with a discussion of our subsequent work to extend the attributes’ coverage and use.

*   **Alexandru Susu**: Emulating Arithmetic Operations with LLVM's Instruction Selection Pass

    The Connex-S wide research vector processor has a simple design with 16-bit integer lanes since many embedded applications can make good use of narrow integer types. For completeness, however, our back end for Connex-S needs to lower code to emulate efficiently arithmetic operations for non-native types such as 32-bit integer and 16-bit floating point. To simplify the work of the compiler writer we conceive a method to code generate how we lower these operations inside LLVM's instruction selection pass. We also implement in the Connex-S processor simple lane gating techniques to minimize energy consumption for vector code with a high degree of control divergence, as it is the case for routines emulating floating point operations.

*   **Simon Moll, Shrey Sharma, Matthias Kurtenacker, and Sebastian Hack**: Multi-dimensional Vectorization in LLVM

    Loop vectorization is a classic technique to exploit SIMD instructions in a productive way. In multi-dimensional vectorization, multiple loops of a loop nest are vectorized at once. This exposes opportunities for data reuse, register tiling and more efficient memory accesses. In this work, we present TensorRV, a multi-dimensional vectorization framework for LLVM IR. TensorRV is a generalization of the Region Vectorizer, a general purpose outer-loop and whole-function vectorizer, to the multi-dimensional setting. We evaluate TensorRV on a set of stencil codes and matrix transpose. We find that stencil codes benefit from the reduction of load instructions with a speedup of x1.45 on NEC SX-Aurora TSUBASA. Multi-loop vectorized matrix transpose leverages efficient SIMD shuffle instructions on AVX512, for which we report a speedup of x3.27.

*   **Johannes Doerfert, Brian Homerding and Hal Finkel**: Performance Gap Exploration with LLVM

    Compilers are limited by the static information directly or indirectly encoded in the program. Especially low-level languages, such as C and C++, are therefore considered problematic as their weak type system and relaxed memory semantic allows for various, sometimes non-obvious, behaviors. Since compilers have to preserve the program semantic for all program executions, the existence of exceptional behavior can prevent optimizations that the developer would consider valid and might even expect. Analyses to guarantee the absence of such disruptive and unlikely situations are consequently an indispensable part of an optimizing compiler. However, these analyses have to be approximative and limited in scope. Global and exact static analysis, under consideration of all potential inputs to the program, is simply an infeasible task for any non-trivial program. Even if a user knows the structure of all inputs ever passed to the program, it is not easy to encode such information. The conservatively correct compiler can consequently not match the expectations a developer with superior knowledge has. In this talk, we present a method to automatically measure the effect missing static information has on the optimizations applied to a given program. As a result, we generate an optimistically optimized program version which, compared to the original, defines a performance gap that can be closed by better analyses and programmer annotations. Our evaluation of six, already optimized, proxy kernels for high-performance applications exposed a compiler flaw that caused a ≈6x fold slowdown, as well as opportunities to achieve speedups of up to 20.6%. This clearly indicates that static uncertainty can result in poor performance, but also that compilers need to more effectively utilize available information.

Workshop organization: Johannes Doerfert, Sebastian Pop, Aditya Kumar.

<!-- *********************************************************************** -->

* * *
