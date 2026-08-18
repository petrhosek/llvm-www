---
layout: "default.html"
permalink: "devmtg/2025-06/index.html"
---
# 2025 AsiaLLVM Developers' Meeting

<div style="float: left; width: 68%">

<div style="width: 100%">

1.  [About](#about)
2.  [Program](#program)
3.  [Code of Conduct](#coc)
4.  [Contact](#contact)

*   **Conference Date**: June 10, 2025
*   **Location**: [The Westin Hotel](https://www.marriott.com/en-us/hotels/tyowi-the-westin-tokyo/overview/), Tokyo, Japan

</div>

# About

The Asia LLVM Developers' Meeting is a tri-annual gathering of the entire LLVM Project community. The conference is organized by the LLVM Foundation and many volunteers within the LLVM community. Developers and users of LLVM, Clang, and related subprojects will enjoy attending interesting talks, impromptu discussions, and networking with the many members of our community. Whether you are a new to the LLVM project or a long time member, there is something for each attendee.

### What can you can expect at an LLVM Developers' Meeting?

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

Who attends?

*   Active developers of projects in the LLVM Umbrella (LLVM core, Clang, LLDB, libc++, compiler\_rt, flang, lld, MLIR, etc).
*   Anyone interested in using these as part of another project.
*   Students and Researchers
*   Compiler, programming language, and runtime enthusiasts.
*   Those interested in using compiler and toolchain technology in novel and interesting ways.
*   Sponsors and partners utilizing LLVM technology in their products.

The LLVM Developers' Meeting strives to be the *best conference* to meet other LLVM developers and users.

For future announcements or questions: Please visit the [LLVM Discourse forums](https://discourse.llvm.org). Most posts are in the Announcements or Community categories and tagged with [asia-devmtg](https://discourse.llvm.org/tag/asia-devmtg).

# Program

**Keynote**

LLVM's First 25 Years and the Road Ahead \[ [Video](https://youtu.be/crmqvh4Z7YI) \] \[ [Slides](slides/keynote/lattner-keynote.pdf) \]  
Speaker: Chris Lattner  

The creator of LLVM, Swift, Clang, MLIR, co-founder and CEO of Modular on the history and future of the LLVM Project.

**Technical Talks**

ONNX-MLIR: An MLIR-based Compiler for ONNX AI models \[ [Video](https://youtu.be/cXHTu2wI5Ps) \] \[ [Slides](slides/technical-talk/le-onnx.pdf) \]  
Speaker: Tung D. Le  

Open Neural Network Exchange (ONNX) is an open standard for representing deep neural networks, and MLIR is emerging as a flexible compiler infrastructure. In this talk, we present a technical report on our open-source compiler, namely ONNX-MLIR, which uses MLIR to compile ONNX models into native code on different architectures e.g., x86, IBM Power, IBM Z. We will discuss the core design of ONNX-MLIR, the optimizations it deploys, and how it supports custom AI accelerators. ONNX-MLIR has been developed since 2019, shortly after MLIR was introduced. Thus, we would also like to discuss some lessons learned when building ONNX-MLIR in parallel with the growth of MLIR compiler infrastructure.

Sanitizing MLIR Programs with Runtime Operation Verification \[ [Video](https://youtu.be/O1nGbW6hKBU) \] \[[Slides](slides/technical-talk/springer-sanitizing.pdf) \]  
Speaker: Matthias Springer  

Operation verification is a core MLIR feature and a powerful tool for building robust compilers. MLIR verifies all operations between pass boundaries, but only static invariants based on compile-time information can be verified. This talk shows how to additionally verify operations at runtime, ranging from low-level properties such as out-of-bounds accesses into tensors/memrefs to high-level properties such as mismatching tensor shapes on linalg structured operations. This talk will also show how to build a memory leak sanitizer based on runtime operation verification.

Data-Tiling in IREE: Achieving High Performance Through Compiler Design \[ [Video](https://youtu.be/iANJWUL_SOo) \] \[ [Slides](slides/technical-talk/wang-data-tilling.pdf) \]  
Speaker: Han-Chung Wang  

This talk explores how IREE, a retargetable MLIR-based compiler for tensor programs, achieves high performance through data-tiling. By rearranging input data into target-specific layouts and utilizing tensor encodings, IREE bridges the gap between host and device. These encodings enable efficient data handling and unlock optimizations like folding, fusion, and propagation, which reduce the cost of relayouting operations. Learn how IREE integrates data-tiling to optimize performance in a compiler context.

Safety at Scale: Advancing Safety with hundreds of millions of lines of C++ \[ [Video](https://youtu.be/BUhYJtAq1n8) \] \[ [Slides](slides/technical-talk/yasuda-safety.pdf) \]  
Speaker: Kinuko Yasuda  

Memory safety is increasingly recognized as a top priority in the industry, and the adoption of memory-safe languages for new code has become a key common methodology. However, significantly improving the safety of large existing C++ codebases remains a major challenge. In this talk, I will share our recent experience deploying several safety improvements across our C++ codebase at Google. Specifically, I will talk about the deployment of hardened libc++, and explain a series of improvements and extensions we made to Clang’s compile-time pointer lifetime analysis around lifetimebound annotations. By enabling hardened libc++ in all of our products, and adopting the annotations in our key core libraries, we have been able to reduce a significant number of safety violations, and improve the reliability and correctness of our code. I will also touch on ongoing efforts and future work in this area.

LLVM vs. GCC on RISC-V Using SPEC CPU Benchmarks: Methods, Gaps, and Optimizations \[ [Video](https://youtu.be/T30hxDUqfVY) \] \[ [Slides](slides/technical-talk/li-risc.pdf) \]  
Speaker: Yongtai Li  

This work details a systematic approach for comparing LLVM and GCC compilers on RISC-V using SPEC CPU 2006 and 2017 benchmarks, with full results disclosed for the 2017 suite. We expose critical performance gaps through code size, dynamic instruction counts (DIC), and vectorization efficiency, while proposing actionable fixes for compiler-specific inefficiencies.

Breaking std::vector's ABI for performance gains: A Horror Story \[ [Video](https://youtu.be/RKdkHwbgXfY) \] \[ [Slides](slides/technical-talk/di-bella-vector.pdf) \]  
Speaker: Christopher Di Bella  

This talk chronicles the story of modifying std::vector to directly track its size instead of its allocated buffer, and the associated performance improvements we gained as a result. We’ll also tell the story of applying these changes to libc++ so that it can be upstreamed, and the far more terrifying story of addressing any and all downstream reliance on the previous implementation quirks of vector to see this optimisation deployed internally.

Understanding Tablegen generated files in LLVM Backend \[ [Video](https://youtu.be/vkVjIAlzdMw) \] \[ [Slides](slides/technical-talk/chaudhuri-tablegen.pdf) \]  
Speaker: Prerona Chaudhuri  

While working with LLVM, one needs to deal with tablegen generated files which are quite tricky to understand, especially for beginners. And its important to understand these files so that one can debug failures for eg: while building a new backend or adding a new feature in the backend. In this short technical talk, I would like to summarize the common and important tablegen generated files that we can encounter in the llvm backend, what is the semantics of the C++ generated code etc.

Reducing Code Size with Speculative Inlining \[ [Video](https://youtu.be/lmpBcKu7teo) \] \[ [Slides](slides/technical-talk/lee-inlining.pdf) \]  
Speaker: Vincent Lee  

Inlining has generally been seen as a critical optimization for performance at the cost of size. But, it can also be used for size optimizations in the mobile space. In this talk, we discuss a new inlining technique that explores the full set of inlining candidates to uncover cases where inlining will generate size improvements due to downstream simplifications. It uncovers beneficial inlining that the traditional cost modeling overlooks resulting in non-trivial app size and performance improvements.

LLVM in the Automotive Industry: Bringing Functional Safety to Open Source \[ [Video](https://youtu.be/wAQ1XBjXfog) \] \[ [Slides](slides/technical-talk/urribarri-automotive.pdf) \]  
Speaker: Wendi Urribarri  

This talk explores the importance of functional safety in automotive software and the need to qualify compilers under ISO 26262 to prevent undetected errors. It looks into the challenges of ensuring compilers don’t introduce undetected errors and propose a collaborative, open-source approach to qualifying LLVM. Attendees will gain insights into the qualification process, key challenges, and the benefits of making safety compliance more accessible. Let’s discuss how we can align LLVM with industry standards and enable its broader adoption in safety-critical systems.

**Quick Talks**

ClangIR’s Footprint: Compile Time Impact \[ [Video](https://youtu.be/Dh_RObp5SUE) \] \[ [Slides](slides/quick-talk/lopes-compile-time.pdf) \]  
Speaker: Bruno Cardoso Lopes  

This presentation explores recent measurements of ClangIR’s impact on compile time. It addresses community concerns from the upstreaming RFC about compilation performance while providing updates on ClangIR’s status.

The Data Inspection Language: Fast & Simple Expression Evaluation in LLDB \[ [Video](https://youtu.be/tgsDbrQga_w) \] \[ [Slides](slides/quick-talk/lebedev-lldb.pdf) \]  
Speaker: Andrei Lebedev  

LLDB often spends a substantial amount of time evaluating expressions needed for displaying certain debug information in an IDE. Currently, this work must be done by LLDB’s full expression evaluator, a very powerful but somewhat slow and heavyweight mechanism. However, these expressions tend to be small and simple, so most of them could be evaluated much faster. The approach of a fast limited expression evaluator was leveraged in lldb-eval for a limited C++ subset proving that the approach is viable. In this talk we introduce the Data Inspection Language (DIL) – a new LLVM mainline effort based partly on lldb-eval that aims to expand its capabilities, make it more robust and language-agnostic. The goal of DIL is to eventually replace the existing frame variable mechanism in LLDB, permitting it to be used for simple expression evaluation. This new implementation will greatly increase the capabilities of ‘frame variable’, allowing it to quickly and directly evaluate simple expressions, in turn allowing to bypass the full expression evaluator in many common cases.

A technology for lifting machine code to high-performance LLVM IR \[ [Video](https://youtu.be/oXQ6b2wZWpU) \] \[ [Slides](slides/quick-talk/yoshimura-ir.pdf)\]  
Speaker: Masashi Yoshimura  

Introducing a technology for lifting machine code to high-performance LLVM IR. This approach transforms Linux/ELF binaries into executables for various target platforms through ahead-of-time compilation. It converts code sections into LLVM IR using a tool that translates machine instructions into equivalent IR, then applies a sophisticated optimization that leverages virtual registers to enhance performance. In this session, we’ll explore the underlying architecture, key optimization strategies, and discuss future challenges and opportunities for advancing cross-platform binary translation.

Improving LLVM Backend Development with a New TableGen Language Server \[ [Video](https://youtu.be/XrF9HWCBkBE) \] \[ [Slides](slides/quick-talk/ando-backend.pdf) \]  
Speaker: Shin Ando  

TableGen is essential for LLVM backend development, but the current development experience leaves much to be desired. This talk presents a new language server tailored for TableGen, with improved performance, stability, and dedicated support for backend development. Through robust parsing, advanced analysis, and a rich set of LSP features, we show how the development experience can be significantly improved.

Improvements to LoopInterchange to accelerate vectorization \[ [Video](https://youtu.be/VV5nFm1ByY0) \] \[ [Slides](slides/quick-talk/kasuga-loopinterchange.pdf) \]  
Speaker: Ryotaro Kasuga  

LoopInterchange is a transform pass that exchanges the order of loops within a nested loop. It accelerates loop vectorization in some cases, especially the vectorization of the innermost loop. This talk is about how LoopInterchange affects vectorization and improvements to LoopInterchange to boost vectorization.

**Lightning Talks**

Fujitsu Compiler Test Suite: New Test Suite for Fortran/C/C++ \[ [Video](https://youtu.be/_k2zKR5xVoQ) \] \[ [Slides](slides/lightning-talk/kawashima-fujitsu.pdf) \]  
Speaker: Takahiro Kawashima  

Fujitsu released Fujitsu Compiler Test Suite [https://github.com/fujitsu/compiler-test-suite](https://github.com/fujitsu/compiler-test-suite), a test suite for Fortran/C/C++ compilers, at the end of 2023. It is used in the Flang CI [https://linaro.atlassian.net/wiki/spaces/FLANGCI/overview](https://linaro.atlassian.net/wiki/spaces/FLANGCI/overview), one of unofficial CI (continuous integration) systems in the LLVM community, to detect regressions of LLVM. This talk explains what the Fujitsu Compiler Test Suite and the Flang CI are and how the LLVM community can leverage them.

Complex Number Division Calculation Methods and Our Work in MLIR \[ [Video](https://youtu.be/0QR-EtoYIlI) \] \[ [Slides](slides/lightning-talk/watanabe-division.pdf) \]  
Speaker: Shunsuke Watanabe  

Our investigation revealed that the optimization of loops involving complex number division in Flang performs worse than Gfortran. This performance difference was confirmed in SPEC CPU 2017’s cam4 benchmark. The reason for this is that the current Flang can only lower complex number division to scalar runtime functions (such as “\_\_divdc3”), preventing vectorization and inlining. Therefore, we considered using the MLIR’s complex dialect to compute complex number division. This talk will explain the calculation methods for complex number division and our work in MLIR.

Wanco: WebAssembly AOT Compiler That Supports Live Migration \[ [Video](https://youtu.be/gVvgSn7dyts) \] \[ [Slides](slides/lightning-talk/tamura-webassembly.pdf) \]  
Speaker: Raiki Tamura  

We introduce Wanco, an AOT compiler for WebAssembly that enables migration across platforms, making it ideal for edge computing and IoT devices. Leveraging LLVM, Wanco introduces up to 50% overhead while storing snapshots in a CPU- and OS-independent format, enhancing the portability of WebAssembly programs.

Toward a Practical Double-Fetch Checker for Clang Static Analyzer: Early Results and Future Directions for OS Security \[ [Video](https://youtu.be/LcYdysH5CQs) \] \[ [Slides](slides/lightning-talk/shigemitsu-tiling.pdf) \]  
Speaker: Fumiya Shigemitsu  

Double-fetch vulnerabilities - a form of TOCTOU (Time-of-Check to Time-of-Use) bugs - pose a significant risk in kernels and embedded systems when user-space memory is accessed multiple times without proper copy semantics. In this talk, we present our newly developed double-fetch checker for the Clang Static Analyzer, which builds on research prototypes (e.g., DFTracker) and uses memory-access provenance, alias relationships, and control-flow analysis to detect repeated reads from user memory. We’ll share how we reduce false positives through tailored heuristics, explore extensions for RTOS-specific environments, and outline future directions aimed at improving kernel and embedded security.

Nanpanjiang Project: Helping Female Engineers Succeed in Compilers and Tools \[ [Video](https://youtu.be/faRR-Y8e00g) \] \[ [Slides](slides/lightning-talk/qiu-nanpangjiang.pdf) \]  
Speaker: Ji Qiu  

The Nanpanjiang Project, established in 2023 by technology enthusiasts in the HelloLLVM community in mainland China, aims to support female engineers in achieving career goals in compilers and virtual machines. Originating from the first “Women in Compilers and Tools Workshop” (WiCT) by the LLVM Foundation, it offers lectures, tutorials, and mentorship. So far, over 20 seminars have been held, with projections indicating outreach will grow from 200 to 20,000 by 2036, mentorship participants from 20 to 5,000, and active maintainers from 2 to 200. The project will continue to promote gender diversity and contribute to the technology community’s prosperity.

Leverage AArch64 SME/SVE instructions to support clang matrix\_type \[ [Video](https://youtu.be/EC0oPWoXDnY) \] \[ [Slides](slides/lightning-talk/zheng-matrix.pdf) \]  
Speaker: Zheng Chen  

AArch64 has SME instructions to operate on the ZA register which works great for Clang matrix\_type operations. I would like to share what we did in Huawei to leverage AArch64 SME instructions to support fast Clang matrix\_type operations.

Bolting the Linux kernel with profile instrumentation \[ [Video](https://youtu.be/5ympgoV_Uqo) \] \[ [Slides](slides/lightning-talk/wei-instrumentation.pdf) \]  
Speaker: Wei Wei  

This presentation focuses on several enhancements to BOLT for Linux kernel, including support for AArch64, relocation mode and instrumentation. We will talk about the motivations, the challenges, and what we have achieved including early performance results, and further work, with an emphasis on instrumentation.

Reflection of standard attributes in Clang \[ [Video](https://youtu.be/VyaV5sCcbyk) \] \[ [Slides](slides/lightning-talk/cassagnes-clang.pdf) \]  
Speaker: Aurelien Cassagnes  

This talk will discuss the implementation experience when adding “attributes reflection” to Clang, from the perspective of a first time contributor.

# Code of Conduct

The LLVM Foundation is dedicated to providing an inclusive and safe experience for everyone. We do not tolerate harassment of participants in any form. By registering for this event, we expect you to have read and agree to the [LLVM Code of Conduct](http://llvm.org/docs/CodeOfConduct.html).

# Contact

To contact the organizer, [email events@llvm.org](mailto:events@llvm.org)

</div>

<!-- *********************************************************************** --> <!--#include virtual="sponsors.incl" -->

* * *
