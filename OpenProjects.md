---
layout: "default.html"
permalink: "OpenProjects.html"
---
# Open LLVM Projects

*   Google Summer of Code Ideas & Projects
    *   [Google Summer of Code 2026](#gsoc26)
        *   **LLVM Core**
        *   [**Clang**](http://clang.llvm.org/)
            *   [Expanding API Notes for C++](#expanding-api-notes-for-cpp)
            *   [Participating in Upstreaming -fbounds-safety](#upstreaming-fbounds-safety)
            *   [Incremental build support for the modules driver](#incremental-build-support-modules-driver)
            *   [Improving Clang-Doc](#improving-clang-doc)
            *   [Improving lit](#improving-lit)
        *   [**LLDB**](http://lldb.llvm.org/)
            *   [Add Fortran Debugging Support in LLDB](#fortran-debugging-support-in-lldb)
        *   [**LLVM libc**](http://libc.llvm.org/)
            *   [Enable float80 and float128 math support on unsupported targets for LLVM libc](#enable_float80_float128_for_unsupported_target)
            *   [Use LLVM libc math routines for compiler-rt floating point routines](#use_llvm_libc_math_for_compiler_rt_builtins)
        *   [**ClangIR**](https://llvm.github.io/clangir/)
            *   [Unified Host–Device Compilation in ClangIR (CIR): Enabling Cross-Boundary Analysis and Optimization](#unified-host–device-compilation-in-clangir)
        *   [**Clang Static Analyzer**](https://clang.llvm.org/docs/ClangStaticAnalyzer.html)
            *   [Teach the Clang Static Analyzer to understand lifetime annotations](#csa-lifetime-annotations)
        *   [**Clangd**](http://clangd.llvm.org/)
            *   [Enable Clangd support for HLSL](#enable-clangd-hlsl-support)
        *   [**MLIR**](https://mlir.llvm.org//)
            *   [Static Memory Planner For MLIR](#static_memory_planner_for_mlir)
        <!-- Add other subprojects as necessary -->
    *   [Google Summer of Code 2025](#gsoc25)
        *   **LLVM Core**
            *   [Introduce an ABI lowering library](#llvm-abi-lowering)
            *   [Byte type](#byte-type)
        *   [**Clang**](http://clang.llvm.org/)
            *   [Simple C++20 modules without a build system](#clang-driver-modules)
            *   [Usability Improvements for trapping Undefined Behavior Sanitizer (UBSan)](#clang-improve-trapping-ubsan-2025)
            *   [Improve documentation parsing in Clang](#improve-documentation-parsing-in-clang)
            *   [Advanced symbol resolution and reoptimization for clang-repl](#improve-symbol-discovery-clang-repl)
        *   [**LLDB**](http://lldb.llvm.org/)
            *   [Rich disassembler for LLDB](#rich-disassembler-for-lldb-2025)
        *   [**LLVM libc**](http://libc.llvm.org/)
            *   [Bfloat16 in LLVM libc](#bfloat16-libc)
            *   [Direct I/O from the GPU with io\_uring](#io_uring-libc)
            *   [Profiling and testing the LLVM libc GPU math](#testing-math-libc)
        *   [**ClangIR**](https://clangir.org)
            *   [Validate existing Clang CodeGen test coverage with ClangIR](#clangir-codegen-tests)
            *   [Participate in ClangIR upstreaming](#clangir-upstreaming)
        *   [**Clang Static Analyzer**](https://clang.llvm.org/docs/ClangStaticAnalyzer.html)
            *   [Teach the Clang Static Analyzer to understand lifetime annotations](#csa-lifetime-annotations)
        *   [**Enzyme**](https://enzyme.mit.edu)
            *   [Improve Enzyme reliability and compile times for Rust](#rust-enzyme-improvements)
        *   [**Offload**](https://discourse.llvm.org/t/offload-new-subproject-pending-move-of-libomptarget/78185) (Former [**OpenMP Offloading**](https://openmp.llvm.org/))
            *   [LLVM Compiler Remarks Visualization Tool for Offload Proposal](#offload-remarks-visualization)
    *   [Google Summer of Code 2024](#gsoc24)
        *   **LLVM Core**
            *   [Remove undefined behavior from tests](#remove_ub_tests)
            *   [Automatically generate TableGen file for SPIR-V instruction set](#spirv_tablegen)
            *   [LLVM bitstream integration with CAS (content-addressable storage)](#bitstream_cas)
            *   [Add 3-way comparison intrinsics](#three_way_comparison)
            *   [Improve the LLVM.org Website Look and Feel](#llvm_www)
            *   [The 1001 thresholds in LLVM](#parameter-tuning)
        *   [**Clang**](http://clang.llvm.org/)
            *   [Out-of-process execution for clang-repl](#clang-repl-out-of-process)
            *   [Support clang plugins on Windows](#clang-plugins-windows)
            *   [On Demand Parsing in Clang](#clang-on-demand-parsing)
            *   [Improve Clang-Doc Usability](#clang-doc-improve-usability)
        *   [**LLDB**](http://lldb.llvm.org/)
            *   [Rich disassembler for LLDB](#rich-disassembler-for-lldb)
        *   [**(OpenMP) Offload**](http://openmp.llvm.org/)
            *   [GPU Delta Debugging](#gpu-delta-debugging)
            *   [Offloading libcxx](#offload-libcxx)
            *   [Performance tuning the GPU libc](#gpu-libc)
            *   [Improve GPU First Framework](#gpu-first)
        *   [**ClangIR**](https://clangir.org)
            *   [Compile GPU kernels using ClangIR](#clangir-gpu)
        *   [**LLVM libc**](http://libc.llvm.org/)
            *   [Half precision in LLVM libc](#half-precision-libc)
    *   [Google Summer of Code 2023](#gsoc23)
        *   **LLVM Core**
            *   [Re-optimization using JITLink](#llvm_new_jitlink_reopt)
            *   [JITLink new backends](#llvm_new_jitlink_backends)
            *   [Improving compile times](#llvm_improving_compile_times)
            *   [Addressing Rust optimization failures](#llvm_addressing_rust_optimization_failures)
            *   [Better performance models for MLGO training](#llvm_mlgo_latency_model)
            *   [Machine Learning Guided Ordering of Compiler Optimization Passes](#llvm_mlgo_passes_2023)
            *   [Map LLVM values to corresponding source-level expressions](#llvm_map_value_to_src_expr)
        *   [**Clang**](http://clang.llvm.org/)
            *   [Out-of-process execution for clang-repl](#clang-repl-out-of-process)
            *   [Improve and Stabilize the Clang Static Analyzer's "Taint Analysis" Checks](#clang_analyzer_taint_analysis)
            *   [Implement autocompletion in clang-repl](#clang-repl-autocompletion)
            *   [Modules build daemon: build system agnostic support for explicitly built modules](#clang-modules-build-daemon)
            *   [ExtractAPI Objective-C categories](#clang-extract-api-categories)
            *   [ExtractAPI C++ Support](#clang-extract-api-cpp-support)
            *   [ExtractAPI while building](#clang-extract-api-while-building)
            *   [Improve Clang diagnostics](#clang-improve-diagnostics2)
            *   [Tutorial development with clang-repl](#clang-tutorials-clang-repl)
            *   [Add WebAssembly Support in clang-repl](#clang-repl-wasm)
        *   **LLD**
            *   [LLD Linker Improvements for Embedded Targets](#llvm_lld_embedded)
        *   **MLIR**
            *   [Optimizing MLIR’s Presburger library](#llvm_mlir_presburger_opt)
            *   [Interactively query MLIR IR](#llvm_mlir_query)
        *   **Code Coverage**
            *   [Support a hierarchical directory structure in generated coverage html reports](#llvm_code_coverage)
            *   [Patch based test coverage for quick test feedback](#llvm_patch_coverage)
        *   **ClangIR**
            *   [Build and run SingleSource benchmarks using ClangIR](#clangir)
        *   **[Enzyme](https://enzyme.mit.edu)**
            *   [Move additional Enzyme Rules to Tablegen](#enzyme_tblgen_extension)
    *   [Google Summer of Code 2022](#gsoc22)
        *   **LLVM Core**
            *   [Implement a shared-memory based JITLinkMemoryManager for out-of-process JITting](#llvm_shared_jitlink)
            *   [Modernize the LLVM "Building A JIT" tutorial series](#llvm_build_jit_tutorial)
            *   [Write JITLink support for a new format/architecture](#llvm_jit_new_format)
            *   [Instrumentation of Clang/LLVM for Compile Time](#llvm_instrumentaion_for_compile_time)
            *   [Richer symbol dependency information for LTO](#llvm_lto_dependency_info)
            *   [Machine Learning Guided Ordering of Compiler Optimization Passes](#llvm_mlgo_passes)
            *   [Learning Loop Transformation Heuristics](#llvm_mlgo_loop)
            *   [Evaluate and Expand the Module-Level Inliner](#llvm_module_inliner)
            *   [Remove undef: move uninitialized memory to poison](#llvm_undef_load)
            *   [Add ABI/API export annotations to the LLVM build](#llvm_abi_export)
        *   [**Clang**](http://clang.llvm.org/)
            *   [Extend clang AST to provide information for the type as written in template instantiations](#clang-template-instantiation-sugar)
            *   [Implement support for C++17 structured bindings in the Clang Static Analyzer](#clang-sa-structured-bindings)
            *   [Improve Clang Diagnostics](#clang-improve-diagnostics)
        *   [**Polly**](https://polly.llvm.org)
            *   [Completely switch to new pass manager](#polly_npm)
        *   **[Enzyme](https://enzyme.mit.edu)**
            *   [Move Enzyme Instruction Transformation Rules to Tablegen](#enzyme_tblgen)
            *   [Vector Reverse-Mode Automatic Differentiation](#enzyme_vector)
            *   [Enable The New Pass Manager](#enzyme_pm)
    *   [Google Summer of Code 2021](#gsoc21)
        *   **LLVM Core**
            *   [Distributed lit testing](#llvm_distributing_lit)
            *   [Learning Loop Transformation Heuristics](#llvm_loop_heuristics)
            *   [Fuzzing LLVM-IR Passes](#llvm_ir_fuzzing)
            *   [llvm.assume the missing pieces](#llvm_ir_assume)
            *   [Implement a shared-memory based JITLinkMemoryManager for out-of-process JITting](#llvm_shared_jitlink)
            *   [Modernize the LLVM "Building A JIT" tutorial series](#llvm_build_jit_tutorial)
            *   [Write JITLink support for a new format/architecture](#llvm_jit_new_format)
            *   [Fix fundamental issues in LLVM's IR](#llvm_ir_issues)
            *   [Utilize LoopNest Pass](#llvm_utilize_loopnest)
        *   [**Clang**](http://clang.llvm.org/)
            *   [Extend clang AST to provide information for the type as written in template instantiations](#clang-template-instantiation-sugar)
        *   **OpenMP**
            *   [JIT-ing OpenMP GPU kernels transparently](#openmp_gpu_jit)
        *   **OpenACC**
            *   [OpenACC Diagnostics from the OpenMP Runtime](#openacc_rt_diagnostics)
        *   **[Polly](https://polly.llvm.org)**
            *   [Use official isl C++ bindings](#polly_isl_bindings)
        *   **[Enzyme](https://enzyme.mit.edu)**
            *   [Integrate custom derivatives of BLAS, Eigen, and similar routines into Enzyme](#enzyme_blas)
            *   [Integrate Enzyme into Swift to provide high-performance differentiation in Swift](#enzyme_swift)
            *   [Differentiation of Fixed-Point Arithmetic](#enzyme_fixed)
            *   [Integrate Enzyme into Rust to provide high-performance differentiation in Rust](#enzyme_rust)
        *   **Clang Static Analyzer**
            *   [Clang Static Analyzer performance profiling](#static_analyzer_profling)
            *   [Clang Static Analyzer constraint solver improvements](#static_analyzer_constraint_solver)
        *   **LLDB**
            *   [A structured approach to diagnostics in LLDB](#lldb_diagnostics)
    *   [Google Summer of Code 2020](#gsoc20)
        *   **LLVM Core**
            *   [Improve debugging of optimized code](#llvm_optimized_debugging)
            *   [Improve inter-procedural analyses and optimizations](#llvm_ipo)
            *   [Improve parallelism-aware analyses and optimizations](#llvm_par)
            *   [Make LLVM passes debug info invariant](#llvm_dbg_invariant)
            *   [Improve MergeFunctions to incorporate MergeSimilarFunction patches and ThinLTO Support](#llvm_mergesim)
            *   [Add DWARF support to yaml2obj](#llvm_dwarf_yaml2obj)
            *   [Improve hot cold splitting to aggressively outline small blocks](#llvm_hotcold)
            *   [Advanced Heuristics for Ordering Compiler Optimization Passes](#llvm_pass_order)
            *   [Machine learning and compiler optimizations: using inter-procedural analysis to select optimizations](#llvm_ml_scc)
            *   [Add PostDominatorTree in LoopStandardAnalysisResults](#llvm_postdominators)
            *   [Create loop nest pass](#llvm_loopnest)
            *   [Instruction properties dumper and checker](#llvm_instdump)
            *   [Unify ways to move code or check if code is safe to be moved](#llvm_movecode)
        *   [**Clang**](http://clang.llvm.org/)
            *   [Extend clang AST to provide information for the type as written in template instantiations](#clang-template-instantiation-sugar)
            *   [Find null smart pointer dereferences with the Static Analyzer](#clang-sa-cplusplus-checkers)
        *   [**LLDB**](http://lldb.llvm.org/)

        *   [Support autosuggestions in LLDB's command line](#lldb-autosuggestions)
        *   [Implement the missing tab completions for LLDB's command line](#lldb-more-completions)
        *   [Reimplement LLDB's command-line commands using the public SB API.](#lldb-reimplement-lldb-cmdline)
        *   [Add support for batch-testing to the LLDB testsuite.](#lldb-batch-testing)

        *   **MLIR**
            *   See the [MLIR open project list](https://mlir.llvm.org/getting_started/openprojects/)
    *   [Google Summer of Code 2019](#gsoc19)
        *   **LLVM Core**
            *   [Debug Info should have no effect on codegen](#debuginfo_codegen_mismatch)
            *   [Improve (function) attribute inference](#llvm_function_attributes)
            *   [Improve LLVM binary utilities](#improve_binary_utilities)
        *   [**Clang**](http://clang.llvm.org/)
            *   [Implement an ASTImporter fuzzer](#clang-astimporter-fuzzer)
            *   [Improve shell autocompletion for Clang](#improve-autocompletion)
            *   [Apply the Clang Static Analyzer to LLVM-based Projects](#analyze-llvm)
            *   [Generate annotated sources based on LLVM-IR analyses](#header-generation)
    *   [Google Summer of Code 2018](#gsoc18)
    *   [Google Summer of Code 2017](#gsoc17)
*   [What is this?](#what)
*   [LLVM Subprojects: Clang and more](#subprojects)
*   [Improving the current system](#improving)
    1.  [Factor out target descriptions](#target-desc)
    2.  [Implementing Code Cleanup bugs](#code-cleanups)
    3.  [Compile programs with the LLVM Compiler](#programs)
    4.  [Add programs to the llvm-test suite](#llvmtest)
    5.  [Benchmark the LLVM compiler](#benchmark)
    6.  [Benchmark Statistics and Warning System](#statistics)
    7.  [Improving Coverage Reports](#coverage)
    8.  [Miscellaneous Improvements](#misc_imp)
*   [Adding new capabilities to LLVM](#new)
    1.  [Extend the LLVM intermediate representation](#llvm_ir)
    2.  [Pointer and Alias Analysis](#pointeranalysis)
    3.  [Profile-Guided Optimization](#profileguided)
    4.  [Code Compaction](#compaction)
    5.  [New Transformations and Analyses](#xforms)
    6.  [Code Generator Improvements](#codegen)
    7.  [Miscellaneous Additions](#misc_new)
*   [Project using LLVM](#using)
    1.  [Add a MachineModulePass](#machinemodulepass)
    2.  [Encode Analysis Results in MachineInstr IR](#encodeanalysis)
    3.  [Code Layout in the LLVM JIT](#codelayoutjit)
    4.  [Improved Structure Splitting and Field Reordering](#fieldlayout)
    5.  [Finish the Slimmer Project](#slimmer)

Written by the [LLVM Team](/)

<!-- *********************************************************************** -->

# Google Summer of Code 2026

<!-- *********************************************************************** -->

Welcome prospective Google Summer of Code 2026 Students! This document is your starting point to finding interesting and important projects for LLVM, Clang, and other related sub-projects. This list of projects is not only developed for Google Summer of Code, but open projects that really need developers to work on and are very beneficial for the LLVM community.

We encourage you to look through this list and see which projects excite you and match well with your skill set. We also invite proposals not on this list. More information and discussion about GSoC can be found in [discourse](https://discourse.llvm.org/c/community/gsoc) . If you have questions about a particular project please find the relevant entry in discourse, check previous discussion and ask. If there is no such entry or you would like to propose an idea please create a new entry. Feedback from the community is a requirement for your proposal to be considered and hopefully accepted.

The LLVM project has participated in Google Summer of Code for many years and has had some very successful projects. We hope that this year is no different and look forward to hearing your proposals. For information on how to submit a proposal, please visit the Google Summer of Code main [website.](https://summerofcode.withgoogle.com/)

<!-- *********************************************************************** -->

### Expanding API Notes for C++

<!-- *********************************************************************** -->

**Description**

API notes are a YAML-based "sidecar" file mechanism in Clang that allows users to add attributes to existing headers without modifying the header files themselves. This is particularly useful for Swift developers who want to annotate third-party C/C++ libraries and frameworks for better interoperability. However, API notes have limited support for C++ syntax (e.g., type conversion operators), and cannot annotate specific function overloads or template instantiations.

**Expected Result:** Extend API notes to better support C++ language features.

**Skills:** Intermediate C++, familiarity or experience with compiler development

**Project size:** Small or Medium, depending on scope of the proposal

**Difficulty:** Medium

**Potential Mentors:** [John Hui](https://github.com/j-hui) [Egor Zhdan](https://github.com/egorzhdan) [Gábor Horváth](https://github.com/Xazax-hun)

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2026-expanding-api-notes-for-c/89638)

<!-- *********************************************************************** -->

### Participating in Upstreaming -fbounds-safety

<!-- *********************************************************************** -->

**Description**

The -fbounds-safety extension for C adds bounds annotations and compiler-enforced bounds checking to prevent buffer overflow vulnerabilities. Developed by Apple and maintained in a [downstream fork](https://github.com/swiftlang/llvm-project), the extension is being incrementally upstreamed to mainline Clang. See the [RFC](https://discourse.llvm.org/t/rfc-enforcing-bounds-safety-in-c-fbounds-safety/70854) and [documentation](https://clang.llvm.org/docs/BoundsSafety.html) for details.

The student will contribute to upstreaming by:

*   Taking a subset of features identified by the mentor
*   Extracting a relevant downstream feature and refactoring to meet upstream LLVM standards, writing tests and documentation
*   Backporting to the downstream fork to validate correctness in the full -fbounds-safety context

**Expected results:** Upstreamed patches with tests and documentation; validated backports to downstream.

**Confirmed Mentor:** [Yeoul Na](https://github.com/rapidsna), [Dan Liew](https://github.com/delcypher), [Henrik G. Olsson](https://github.com/hnrklssn)

**Desired skills:** C/C++, compiler concepts, managing patches across branches. Clang/LLVM experience and memory safety knowledge are a plus.

**Project size:** Medium or Large (features can be scoped to match the participant's skill level)

**Difficulty:** Medium or Hard (features can be scoped to match the participant's skill level)

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2026-participating-in-upstreaming-fbounds-safety/89649)

<!-- *********************************************************************** -->

### Incremental build support for the modules driver

<!-- *********************************************************************** -->

**Description**

The newly introduced -fmodules-driver mode enables explicit module builds directly from Clang’s driver, supporting both Clang modules discovered via module map files and C++20 named modules. Currently, these modules are precompiled from scratch on every invocation because the modules driver does not provide any caching. This is especially costly for large modules (e.g., the Standard library modules), adding substantial overhead to each compilation.

This project aims to add compilation-job-level caching across the entire modules-driver build graph to enable incremental compilation. Using the dependency-scan results, the driver should track header and module dependencies for each input and determine which jobs must be rebuilt and which can be safely reused from the cache.

**Expected Result:** On repeated compilations, the modules driver should only execute compile jobs that are affected by changed or newly introduced inputs. All other unaffected jobs should be reused from the cache. If multiple Clang instances run simultaneously, the cache must remain correct and safe under concurrent access.

**Skills:** Intermediate knowledge of C++; familiarity with how C++ code is built. Familiarity with C++20 modules/Clang modules is an asset, but not required.

**Project size:** Large

**Difficulty:** Medium

**Confirmed Mentors:** [Naveen Hanig](https://github.com/naveen-seth) (Primary Mentor), [Michael Spencer](https://github.com/Bigcheese) (Backup Mentor)

**Discourse:** [URL](https://discourse.llvm.org/t/clang-gsoc-2026-incremental-build-support-for-the-modules-driver/89667)

<!-- *********************************************************************** -->

### Improving Clang-Doc

<!-- *********************************************************************** -->

**Description**

Clang-Doc is a modern C/C++ documentation generation tool created as an alternative for Doxygen and built on top of LibTooling. This effort started in 2018 and critical mass has landed in 2019, but the development has been largely stagnant mostly due to a lack of resources until the last two years when the development restarted and made significant progress with two successful Google Summer of Code projects:

*   [GSoC 2024: Improve Clang-Doc](https://blog.llvm.org/posts/2024-12-04-improve-clang-doc/)
*   [GSoC 2025: Improving Core Clang-Doc Functionality](https://blog.llvm.org/posts/2025-gsoc-clang-doc/)

[Clang-Doc: Where We’ve Been and Where We’re Going](https://www.youtube.com/watch?v=vuHF_ZeAPVI) talk presented at 2025 LLVM Developers’ Meeting gives a great overview of Clang-Doc architecture and its biggest strengths such as support for latest C++ features and scalable architecture.

Clang-Doc still has significant room for improvement though. Below are some of the ideas we would like to explore.

*   *Improved Markdown Parsing*: One of the most pressing needs is improved Markdown parsing within Doxygen comments. This enhancement would enable support for richer text formatting, code blocks, and tables directly within code comments, making the documentation more readable and informative. Currently, the lack of full Markdown support limits the expressive power of inline documentation.
*   *Clang AST Support for Group Comments*: Another critical area is the Clang AST support for Doxygen group comments. As highlighted in GitHub issue [#151184](https://github.com/llvm/llvm-project/issues/151184), robust support for Doxygen’s grouping commands (e.g., \\defgroup, \\addtogroup) is crucial for generating accurate and comprehensive API documentation that reflects the intended module structure of large projects.
*   *Making The Output More Indexable*: Most developers navigate to the generated documentation via search engine and more recently LLM agents. Making the generated documentation more optimized for indexers can improve its overall usability.
*   *Optimizing Clang’s Frontend Actions*: Optimizing Clang’s “Frontend Actions” would directly reduce documentation generation time, especially for large codebases. This involves streamlining the processes by which Clang-doc extracts information from the AST, leading to faster build times and a more efficient documentation workflow. As discussed in various LLVM developer forums, performance is a continuous focus for Clang tools.
*   *Arena Allocation for Memory Management*: Arena allocation is a memory management technique that could significantly improve Clang-doc’s execution speed and reduce memory overhead, particularly when processing large ASTs. By allocating objects from a pre-allocated memory block, arena allocation can reduce the overhead associated with individual memory allocations and deallocations, leading to better performance, a common optimization in compilers and static analysis tools.

**Expected Result:** The high-level goal of this project is to implement the missing features in Clang’s documentation parser as well as their handling in Clang-Doc to improve the quality of the generated documentation. The eventual goal is for the LLVM project to start using Clang-Doc for generating its reference documentation, but before we can do that we need to ensure that all required features are implemented.

Note that each of the aforementioned ideas could be a medium-sized project on its own and we expect candidates to select one (or more) that match their interest. Successful proposals should focus not only on addressing the existing limitations, but also draw inspiration for other potential improvements from other documentation tools such as [hdoc](https://hdoc.io/), [standardese](https://github.com/standardese/standardese), [subdoc](https://github.com/chromium/subspace/tree/main/subdoc), [cppdocgen](https://cs.opensource.google/fuchsia/fuchsia/+/main:tools/cppdocgen/), [leafy-green-doc](https://github.com/celerity/leafy-green-doc), or [Mr.Docs](https://www.mrdocs.com/).

Over the course of the project, the candidate will have an opportunity to gain significant experience with LLVM and Clang internals (including lexer and parser) and C/C++ language.

**Skills:** Experience with web technologies (HTML, CSS, JS) and an intermediate knowledge of C++. Previous experience with Clang/LibTooling is a bonus but not required.

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentor:** [Erick Velez](https://github.com/evelez7), [Paul Kirth](https://github.com/ilovepi), [Petr Hosek](https://github.com/petrhosek)

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2026-improving-clang-doc/89662)

<!-- *********************************************************************** -->

### Improving lit

<!-- *********************************************************************** -->

**Description of the project:** LLVM's main test running tool, [`lit`](https://llvm.org/docs/CommandGuide/lit.html) (LLVM's integrated tester), is a key part of LLVM’s testing practices for end-to-end testing of the compiler and related tools. `lit` is a tool that can parse and execute `RUN:` commands added in source file comments. Chiefly, these commands are shell commands that invoke tools that are being tested—like `clang` or `lld`—and whose output can be programmatically checked in conjunction with other tooling, like LLVM’s [`FileCheck`](https://llvm.org/docs/CommandGuide/FileCheck.html) utility.

Over the last couple years, we’ve worked towards improving `lit`’s internal shell enough, so that it could be the default mode for running LLVM tests (see [\[RFC\] Enabling the Lit Internal Shell by Default](https://discourse.llvm.org/t/rfc-enabling-the-lit-internal-shell-by-default/80179)). Today, `lit` already uses the internal shell by default in LLVM’s CI, which has improved test performance and increased consistency across platforms. However, there are still many aspects of the current implementation that could be improved, though.

*   *Modernize the lit Python implementation*: Today, lit’s current implementation is, to a large extent, a direct translation of the old Python 2.7 implementation to Python 3. There are numerous language improvements that would allow us to simplify the code and follow best practices. This would require an audit of the current implementation and subsequent refactoring. Note that we’re not advocating a complete rewrite, but targeted well scoped changes to bring the current implementation into line with more modern Python standards.
*   *Reduced process overhead*: Using `asyncio` for subprocess handling is likely a significant improvement in terms of performance, since `lit` spawns many subprocesses and waits for their results when it could frequently take care of unrelated work. Further, some of the out-of-process builtins should be moved back so that they can run in-process (see [\[RFC\] Reducing process creation overhead in LLVM regression tests](https://discourse.llvm.org/t/rfc-reducing-process-creation-overhead-in-llvm-regression-tests/88612)).
*   *Improve shell utilities*: A few of the internal shell replacements for common programs have some issues with common usage. For instance, the built-in `env` has some problems with pipelines (see [#115578](https://github.com/llvm/llvm-project/issues/115578)), and the ergonomics around `readfile` and environment variables in some compiler-rt tests are problematic.
*   *Performance tuning*: `lit` and the various pieces of its internal shell implementation have never been properly profiled and optimized. For instance, commands like `echo` and `cat`, while functional, employ suboptimal algorithms and data structures. There is a big opportunity here to leverage profiling information, specifically via [Scalene](https://github.com/plasma-umass/scalene), to pinpoint inefficiencies, such as contention on the Global Interpreter Lock (GIL), excessive memory usage, and redundant data copies.

**Expected Result:** The goal of this project is to improve `lit`’s performance, usability, and maintainability. Successful proposals should provide a detailed plan for improving `lit`’s implementation. Applicants are encouraged to look more deeply into these areas, and provide concrete plans for what they propose to change, over only vague descriptions of improvements.

**Skills:** Python

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentor:** [Aiden Grossman](https://github.com/boomanaiden154), [Paul Kirth](https://github.com/ilovepi), [Petr Hosek](https://github.com/petrhosek)

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2026-improving-lit/89663)

<!-- *********************************************************************** -->

### Add Fortran Debugging Support in LLDB

<!-- *********************************************************************** -->

**Description**

Fortran remains widely used in HPC, scientific computing, and numerical simulation. However, LLDB currently provides no meaningful variable inspection support for Fortran programs, resulting in errors such as:

`error: Could not find type system for language fortran95: TypeSystem for language fortran95 doesn't exist`

Currently, LLDB lacks a Fortran type system. While breakpoints, stepping, and backtraces work using DWARF line tables, variable inspection and expression evaluation fail due to the absence of a Fortran TypeSystem, DWARFASTParser, ExpressionParser and language integration layer.

This project aims to add initial Fortran debugging support to LLDB by consuming existing DWARF debug information generated by LLVM Flang. The work will focus entirely on LLDB-side infrastructure. No major changes are expected to LLVM IR, DIBuilder, or the DWARF emission produced by Flang, as current flang compiler already generate sufficient debug information for common Fortran constructs.

Selected candidate will be expected to share an RFC(request for comment) proposal with the proposed architecture and integration of the Fortran language plugin to discuss on LLDB Discourse during the community bonding period.

**Expected Result:** The goal of this project is to implement a minimal but functional Fortran debugging stack inside LLDB that enables:

*   Inspection of scalar variables (integer, real, logical)
*   Inspection of function arguments and return values
*   Static array inspection
*   Character string inspection (character(len=\*))
*   Derived type (struct) inspection
*   Module/global variable visibility
*   Basic expression evaluation (p a, p a+1, p arr(2), p p%x)

*Further reading*  
\[1\] https://lldb.llvm.org/resources/addinglanguagesupport.html  
\[2\] https://github.com/llvm/llvm-project/issues/109119

**Skills:** Intermediate knowledge of C++; Basic Fortran knowledge or desire to learn, Ability to comprehend DWARF debug format and standard.

**Project size:** Large

**Difficulty:** Medium

**Mentors:** [Shivam Gupta](https://github.com/xgupta) [Tarun Prabhu](https://github.com/tarunprabhu)

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2026-add-fortran-debugging-support-in-lldb/89963)

<!-- *********************************************************************** -->

### Enable float80 and float128 math support on unsupported targets for LLVM libc

<!-- *********************************************************************** -->

**Description**

The LLVM libc project aims to provide a complete, correct, and high-performance C23 standard library. A key differentiator is its focus on correctly rounded math functions for all floating-point types, including float, double, long double, and float128 (IEEE 754 quad precision).

However, not all compilers or architectures support these types natively. For example:

*   MSVC on Windows treats long double as 64-bit double and lacks a native \_\_float128 type.
*   AArch64 targets typically use 128-bit long double, but lack the 80-bit extended precision format.
*   Clang on certain non-x86 targets may not enable \_\_float128 by default.

This lack of host compiler support prevents LLVM libc from building and testing its high-precision math routines on these platforms.

**The Goal**

The goal of this project is to implement standalone C++ classes (e.g., within LIBC\_NAMESPACE::fputil) that emulate float80 and float128 semantics in software. These classes should provide the necessary operator overloads and storage (using UInt<128> or similar) to allow the existing templated math implementations to compile and run even when the host compiler does not support the native types.

**Proposed Solution**

*   Type Abstraction: Create wrapper classes that mimic the behavior of native floating-point types.
*   Soft-Float Arithmetic: Implement or connect these classes to soft-float arithmetic routines (add, sub, mul, div) so that math algorithms (like polynomial evaluation) can be executed.
*   Integration: Refactor the math function entry points to instantiate templates with these emulated types when native support is missing.

**Expected Results**

*   A header-only C++ implementation of float80 and float128 types that can be used where native support is missing.
*   Basic arithmetic operations (+, -, \*, /) implemented for these types.
*   Demonstration of LLVM libc math functions compiling and passing tests using these emulated types on a target that lacks native support (e.g., building float80 math on Mac arm64, float128 math with MSVC).

**Project size:** Medium or Large

**Difficulty:** Medium

**Requirements**

*   Basic C++ skills.
*   Interest in understanding the intricacies of floating-point formats (IEEE 754 and extended precision).

**Mentors:** [Tue Ly](mailto:lntue.h@gmail.com), [Nicolas Celik](mailto:its.overmighty@gmail.com), [Krishna Pandey](mailto:kpandey81930@gmail.com),

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2026-libc-enable-float80-and-float128-math-support-on-unsupported-targets-for-llvm-libc/89647)

<!-- *********************************************************************** -->

### Use LLVM libc math routines for compiler-rt floating point routines

<!-- *********************************************************************** -->

**Description**

compiler-rt builtins provide essential floating-point computation routines to support runtime execution when the underlying hardware does not support specific floating-point types natively. Unfortunately, the current implementations are under tested, leaving subtle numerical bugs lying dormant for years. Additionally, they are written in a mix of C and hand-written assembly, which substantially increases the maintenance burden.

In contrast, LLVM libc implements these basic floating-point operations with rigorous testing and formal verification. A recent [effort](https://libc.llvm.org/hand_in_hand.html) (see also [Issue #147386](https://github.com/llvm/llvm-project/issues/147386)) has refactored LLVM libc math routines to be free-standing and header-only. This work has significantly lowered the barrier to use LLVM libc implementations, allowing other LLVM projects to consume LLVM libc logic directly via header inclusions without introducing complex build and link dependencies.

Our goal is to demonstrate the feasibility and benefits of replacing legacy compiler-rt floating-point builtins with the modern, verified equivalents from LLVM libc.

**Expected Results**

*   Infrastructure: Ensure basic floating-point operations in LLVM libc are exposed as shared, free-standing headers suitable for inclusion in compiler-rt.
*   Integration: Add a CMake build option allowing compiler-rt builtins to be compiled using LLVM libc math routines instead of the legacy implementations.
*   Validation & Performance: Benchmark the new implementation on embedded targets. Analyze code size and performance, optimizing the build to achieve parity with the current C or hand-written assembly implementations.

**Project size:** Medium or Large

**Difficulty:** Medium

**Requirements**

*   Basic C++ skills.
*   Interest in understanding the intricacies of floating-point formats (IEEE 754) and the low-level implementation of arithmetic operations.

**Mentors:** [Tue Ly](mailto:lntue.h@gmail.com), [Michael Jones](mailto:michaelrj@google.com), [Muhammad Bassiouni](mailto:muhammad.m.bassiouni@gmail.com),

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2026-libc-use-llvm-libc-math-routines-for-compiler-rt-floating-point-builtins/89648)

<!-- *********************************************************************** -->

### Unified Host–Device Compilation in ClangIR (CIR): Enabling Cross-Boundary Analysis and Optimization

<!-- *********************************************************************** -->

**Description**

Modern heterogeneous applications rely heavily on GPU offloading, yet today’s compilation pipelines strictly separate host and device compilation. This separation prevents whole-program reasoning across host–device boundaries and limits optimization opportunities such as kernel specialization, launch-bound inference, and cross-boundary constant propagation.

This project proposes extending [ClangIR](https://clangir.org) with a combine compilation pipeline that merges host and device CIR modules into a unified representation, enables joint analysis and transformation, and then safely re-splits the code for final target-specific lowering. The work builds directly on an existing work-in-progress implementation and aims to upstream a robust, tested, and documented workflow.

**Background and Motivation**

The Clang compiler today emits separate compilation artifacts for host and device code (e.g., CUDA/HIP). While this model simplifies handling, it introduces fundamental limitations:

*   No cross-boundary analysis: The compiler cannot reason about kernel launches, argument values, or launch configuration at the call site.
*   Missed optimization opportunities: Kernel specialization, dead code elimination, and launch-bound inference require joint host–device visibility.

LLVM’s MLIR-based CIR provides a unique opportunity to address this limitation. Because both host and device code are represented in a structured, high-level IR, it becomes feasible to temporarily merge them, perform joint analyses and transformations, and then re-split them for conventional lowering.

This project directly explores that opportunity.

**Related Work and Current State**

ClangIR is actively being upstreamed and already supports emitting CIR from Clang’s AST and lowering to LLVM IR. Initial experiments have demonstrated that host and device CIR modules can be merged in a controlled way.

A work-in-progress implementation already exists which is capable of merging but there is still work to be done in incorporating the merging with the clang driver

*   A WIP [PR](https://github.com/llvm/clangir/pull/2097) on the incubator project presenting some of the required steps
*   An [issue](https://github.com/llvm/llvm-project/issues/175871) loosely tracking changes regarding the offload support on ClangIR.

**Expected Result**

1.  Clang Driver extensions to optionally enable the capability.
2.  Build the infrastructure to contain within a single translation unit both device and host code
3.  Build the infrastructure to properly split a "combined" translation unit to individual ones representing device and host code
4.  End to End execution of the new driver pipeline on benchmarks from PolyBench.
5.  Reporting on compilation time overheads and execution time overheads.
6.  Bonus Point: Implement an optimization pass that infers launch bounds from the host call site

**Skills:** Intermediate C++ programming skills and familiarity with basic compiler design concepts are required. Prior experience with LLVM IR, MLIR, Clang or ClangIR programming is a big plus, but willingness to learn is also a possibility.

**Project size:** Large

**Difficulty:** Medium

**Potential Mentors:** [Konstantinos (Dinos) Parasyris](https://github.com/koparasy) [Joseph Huber](https://github.com/jhuber6)

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2026-host-device-cir-combine-pipeline-project-idea-discussion/89623)

<!-- *********************************************************************** -->

### Teach the Clang Static Analyzer to understand lifetime annotations

<!-- *********************************************************************** -->

**Description:** The [Clang Static Analyzer](https://clang.llvm.org/docs/ClangStaticAnalyzer.html) (CSA) can already find a wide range of temporal memory errors. These checks often have hardcoded knowledge about the behavior of some APIs. For example, the `cplusplus.InnerPointer` checker knows the semantics of `std::string::data`. The Clang community introduced some lifetime annotations including `[[clang::lifetimebound]]` and `[[clang::lifetime_capture_by(X)]]` and made [many improvements](https://discourse.llvm.org/t/lifetime-analysis-improvements-in-clang/81374) to Clang's default warnings. Unfortunately, the compiler's warnings only do statement local analysis. The CSA is capable of advanced inter-procedural analysis. Generalizing the existing checks like `cplusplus.InnerPointer` could enable the analyzer to find even more errors in annotated code. This can become even more impactful once the standard library [gets annotated](https://github.com/llvm/llvm-project/pull/112751).

**Expected result:**

1.  Identify the checks that can benefit from the `[[clang::lifetimebound]]` and `[[clang::lifetime_capture_by(X)]]` annotations.
2.  Extend those checks to support these annotations.
3.  Make sure the generated bug reports are high quality, the diagnostics properly explain how the analyzer took these annotations into account.
4.  Validate the results on real world projects.
5.  Potentially warn about faulty annotations (stretch goal).

**Skills:** Intermediate C++ programming skills and familiarity with basic compiler design concepts are required. Prior experience with Clang or CSA programming is a big plus, but willingness to learn is also a possibility.

**Project size:** Large

**Difficulty:** Hard

**Potential Mentors:** [Gabor Horvath](https://github.com/Xazax-hun) [Balazs Benics](https://github.com/steakhal) [Daniel Domjan](https://github.com/isuckatcs)

**Discourse:** [URL](https://discourse.llvm.org/t/clang-static-analyzer-gsoc-2025-teach-the-clang-static-analyzer-to-understand-lifetime-annotations/84487)

<!-- *********************************************************************** -->

### Enable Clangd support for HLSL

<!-- *********************************************************************** -->

**Description**

[HLSL](https://microsoft.github.io/hlsl-specs/specs/hlsl.pdf) is a GPU shader programming language and there is an ongoing effort to [add HLSL support into Clang.](https://clang.llvm.org/docs/HLSL/HLSLSupport.html) HLSL is built on the C++11 standard, and as such, clangd already has semi-functional support for HLSL, however, it does not handle all language-specific constructs. The goal for this project is to add holistic support for HLSL into clangd.

**Expected outcomes**

*   Survey the current support gaps when using clangd for HLSL.
*   Create an RFC documenting the gaps and propose the best way to address them.
*   After refining the RFC, generate issues for the groundwork of implementation.
*   Implement these issues to complete HLSL support in clangd.

We do not expect all issues to be resolved and for full support of HLSL to be in clangd. It is however expected that the first 3 steps take ~90 hrs, and the remaining ~90 hrs are dedicated towards implementation.

**Required / desired skills**

Required:

*   Intermediate proficiency of C++.
*   Familiarity of how Language Server Protocols (LSP) work.
*   Interest in learning/knowing the HLSL language specification.

Desired:

*   Previous experience programming with HLSL is a plus.
*   Previous experience developing with LSPs is a plus.

**Size of the project:**

Medium (~180hr).

**Project difficulty:**

Medium.

**Mentors:** [Finn Plummer](mailto:mail@inbelic.dev), [Ashley Coleman](mailto:ascoleman@microsoft.com)

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2026-enable-clangd-support-for-hlsl/89664)

<!-- *********************************************************************** -->

### Static Memory Planner for MLIR

<!-- *********************************************************************** -->

**Description**

Tensors in MLIR are abstract, read-only values without an assigned memory location. Bufferization is the process of allocating/assigning memory buffers to tensor values and rewriting tensor-based operations as memref-based operations. Bufferization is necessary to make IR with tensor types executable. In MLIR, this transformation is performed by the One-Shot-Bufferization infrastructure. This infrastructure allocates new buffers with \`memref.alloc\`. Cleanup / deallocation of memory buffers in the form of \`memref.dealloc\`, is done by the ownership-based buffer deallacation infrastructure.

\`memref.alloc\` and \`memref.dealloc\` model dynamic memory allocation (like C malloc/free), which is not suitable for many accelerators. On such hardware, memory usage must typically be planned before the kernel launch. The goal of this project is to design and implement a static memory planner that turns dynamic allocations into static ones. In essence, instead of relying on a dynamic memory allocator, pre-allocating a large enough buffer and managing it manually. This will require reasoning about alias sets and live ranges of allocations. The focus will be well-structured workloads that typically appear in high-performance computing or machine learning models.

Multiple downstream projects have expressed interest in a static memory planner and several already maintain their own implementations. Providing a uniform solution within MLIR will encourage wider adoption of MLIR components and reduce duplicated effort across the community.

**Expected Results**

An analysis and IR rewriting pass that analyzes allocations and deallocations of input IR and generates new IR where all allocations are turned to memref.subviews of a statically-allocated memref. The subviews take care of the liveness of buffers and at the same time exploits reuse of memory as much as possible.

**Documentation**

*   User-facing documentation explaining the analysis, APIs, and how downstream projects can integrate with it.
*   Design notes describing trade-offs and future extensions.

**Skills:** C++ proficiency, familiarity with MLIR and good understanding of bufferization, memory allocations, lifetimes, alias and dataflow analysis.

**Project size:** 350 hours

**Difficulty:** High

**Mentors:** Javed Absar(https://github.com/javedabsar1), Matthias Springer (https://github.com/matthias-springer)

**Discourse:** [RFC: GSoC Buffer Reuse Pass](https://discourse.llvm.org/t/rfc-gsoc-buffer-reuse-pass-for-non-overlapping-allocations-after-lower-deallocations/89885)

<!-- *********************************************************************** -->

# Google Summer of Code 2025

<!-- *********************************************************************** -->

Welcome prospective Google Summer of Code 2025 Students! This document is your starting point to finding interesting and important projects for LLVM, Clang, and other related sub-projects. This list of projects is not only developed for Google Summer of Code, but open projects that really need developers to work on and are very beneficial for the LLVM community.

We encourage you to look through this list and see which projects excite you and match well with your skill set. We also invite proposals not on this list. More information and discussion about GSoC can be found in [discourse](https://discourse.llvm.org/c/community/gsoc) . If you have questions about a particular project please find the relevant entry in discourse, check previous discussion and ask. If there is no such entry or you would like to propose an idea please create a new entry. Feedback from the community is a requirement for your proposal to be considered and hopefully accepted.

The LLVM project has participated in Google Summer of Code for many years and has had some very successful projects. We hope that this year is no different and look forward to hearing your proposals. For information on how to submit a proposal, please visit the Google Summer of Code main [website.](https://summerofcode.withgoogle.com/)

<!-- *********************************************************************** -->

### Rich Disassembler for LLDB

<!-- *********************************************************************** -->

**Description**

Use the variable location information from the debug info to annotate LLDB’s disassembler (and \`register read\`) output with the location and lifetime of source variables. The rich disassembler output should be exposed as structured data and made available through LLDB’s scripting API so more tooling could be built on top of this. In a terminal, LLDB should render the annotations as text.

**Expected outcomes**

For example, we could augment the disassembly for the following function

```
frame #0: 0x0000000100000f80 a.out`main(argc=1, argv=0x00007ff7bfeff1d8) at demo.c:4:10 [opt]
  1   void puts(const char*);
  2   int main(int argc, char **argv) {
  3    for (int i = 0; i < argc; ++i)
→ 4      puts(argv[i]);
  5    return 0;
  6   }
(lldb) disassemble
a.out`main:
...
  0x100000f71 <+17>: movl  %edi, %r14d
  0x100000f74 <+20>: xorl  %r15d, %r15d
  0x100000f77 <+23>: nopw  (%rax,%rax)
→  0x100000f80 <+32>: movq  (%rbx,%r15,8), %rdi
  0x100000f84 <+36>: callq 0x100000f9e ; symbol stub for: puts
  0x100000f89 <+41>: incq  %r15
  0x100000f8c <+44>: cmpq  %r15, %r14
  0x100000f8f <+47>: jne 0x100000f80 ; <+32> at demo.c:4:10
  0x100000f91 <+49>: addq  $0x8, %rsp
  0x100000f95 <+53>: popq  %rbx
...
```

using the debug information that LLDB also has access to (observe how the source variable i is in r15 from \[0x100000f77+slide))

```
$ dwarfdump demo.dSYM --name  i
demo.dSYM/Contents/Resources/DWARF/demo: file format Mach-O 64-bit x86-64
0x00000076: DW_TAG_variable
 DW_AT_location (0x00000098:
 [0x0000000100000f60, 0x0000000100000f77): DW_OP_consts +0, DW_OP_stack_value
 [0x0000000100000f77, 0x0000000100000f91): DW_OP_reg15 R15)
 DW_AT_name ("i")
 DW_AT_decl_file ("/tmp/t.c")
 DW_AT_decl_line (3)
 DW_AT_type (0x000000b2 "int")
```

to produce output like this, where we annotate when a variable is live and what its location is:

```
(lldb) disassemble
a.out`main:
...                                                               ; i=0
  0x100000f74 <+20>: xorl  %r15d, %r15d                           ; i=r15
  0x100000f77 <+23>: nopw  (%rax,%rax)                            ; |
→  0x100000f80 <+32>: movq  (%rbx,%r15,8), %rdi                   ; |
  0x100000f84 <+36>: callq 0x100000f9e ; symbol stub for: puts    ; |
  0x100000f89 <+41>: incq  %r15                                   ; |
  0x100000f8c <+44>: cmpq  %r15, %r14                             ; |
  0x100000f8f <+47>: jne 0x100000f80 ; <+32> at t.c:4:10          ; |
  0x100000f91 <+49>: addq  $0x8, %rsp                             ; i=undef
  0x100000f95 <+53>: popq  %rbx
```

The goal would be to produce output like this for a subset of unambiguous cases, for example, variables that are constant or fully in registers.

**Confirmed mentors and their contacts**

*   Adrian Prantl aprantl@apple.com (primary contact)
*   Jonas Devlieghere jdevlieghere@apple.com

**Required / desired skills**

Required:

*   Good understanding of C++
*   Familiarity with using a debugger on the terminal
*   Need to be familiar with all the concepts mentioned in the example above
*   Need to have a good understanding of at least one assembler dialect for machine code (x86\_64 or AArch64).

Desired:

*   Compiler knowledge including data flow and control flow analysis is a plus.
*   Being able to navigate debug information (DWARF) is a plus.

**Size of the project:**

medium (~175h)

**Project difficulty:**

hard

**Discourse:** [URL](https://discourse.llvm.org/t/rich-disassembler-for-lldb/76952)

<!-- *********************************************************************** -->

### Bfloat16 in LLVM libc

<!-- *********************************************************************** -->

**Description:**

[Bfloat16](https://en.wikipedia.org/wiki/Bfloat16_floating-point_format) is a recently developed floating point format tailored to machine learning and AI, and in the latest [C++23 standard](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/n4950.pdf), it is officially standardized as std::bfloat16\_t. Its support could be found in many modern hardware, ranging from CPUs of all the major vendors including Intel, AMD, Apple, and Amazon, to GPUs (nVidia and AMD GPUs) and Google TPUs. On the software side, it is supported in all major accelerator libraries, such as CUDA, ROCm, oneAPI, PyTorch, and Tensorflow. The goal for this project is to implement bfloat16 math functions in the LLVM libc library.

**Expected result:**

*   Setup the generated headers properly so that the type and the functions can be used with various compilers (+versions) and architectures.
*   Implement generic basic math operations supporting bfloat16 data types that work on supported architectures: x86\_64, arm (32 + 64), risc-v (32 + 64), and GPUs.
*   Implement specializations using compiler builtins or special hardware instructions to improve their performance whenever possible.
*   If time permits, we can start investigating higher math functions for bfloat16.

**Skills:**

Basic C & C++ skills + Interest in knowing / learning more about the delicacy of floating point formats.

**Project size:** Large

**Difficulty:** Easy/Medium

**Confirmed Mentors:** [Tue Ly](mailto:lntue.h@gmail.com), [Nicolas Celik](mailto:its.overmighty@gmail.com),

**Discourse:** [URL](https://discourse.llvm.org/t/libc-gsoc-2025-bfloat16-in-llvm-libc/84469)

<!-- *********************************************************************** -->

### Direct I/O from the GPU with io\_uring

<!-- *********************************************************************** -->

**Description:**

Modern GPUs are capable of unified addressing with the host. We currently use this to provide I/O support using the [RPC interface](https://libc.llvm.org/gpu/rpc.html). However, this requires a dedicated user thread on the CPU to handle the server code. We want to explore alternatives to providing I/O from the GPU using the Linux [io\_uring](https://en.wikipedia.org/wiki/Io_uring) interface.

This interface is a ring buffer designed to accelerate syscalls. However, it provides a [polling mode](https://unixism.net/loti/tutorial/sq_poll.html#sq-poll) that allows the kernel to flush the ring buffer without the user initiating a system call. We should be able to register `mmap()` memory with the GPU using [AMD](https://github.com/ROCm/ROCR-Runtime/blob/amd-staging/runtime/hsa-runtime/inc/hsa_ext_amd.h#L3022) and [NVIDIA](https://docs.nvidia.com/cuda/cuda-driver-api/group__CUDA__UNIFIED.html) API calls. This interface should allow us to implement a rudimentary read/write interface which can be thought of as the same as the syscall on the CPU. That can then be used to implement a whole file interface.

**Expected result:**

*   An implementation of `pwrite` and `pread` that runs on the GPU.
*   Support for `printf` by forwarding `snprintf` into `pwrite`.
*   If time permits, exploring GPU file APIs.

**Skills:**

Basic C & C++ skills + access to a GPU, Linux kernel knowledge, GPU knowledge.

**Project size:** Small

**Difficulty:** Hard

**Confirmed Mentors:** [Joseph Huber](mailto:joseph.huber@amd.com), [Tian Shilei](mailto:i@tianshilei.me)

**Discourse:** [URL](https://discourse.llvm.org/t/libc-gsoc-2025-direct-i-o-from-the-gpu-with-io-uring/84569)

<!-- *********************************************************************** -->

### Profiling and testing the LLVM libc GPU math

<!-- *********************************************************************** -->

**Description:**

The LLVM C library provides implementations of math functions. We want to profile these against existing implementations, such as CUDA's `libdevice`, ROCm's `device libs`, and OpenCL's `libclc`. Last year we worked on some interfaces to support these tests, now they need to be refined and filled out for the interesting functions.

Additionally, we want to verify the accuracy of these functions when run on the GPU via brute force testing. The goal is to verify that the implementations are correct and at least conformant to the error ranges in the [OpenCL standard](https://registry.khronos.org/OpenCL/specs/3.0-unified/html/OpenCL_C.html#relative-error-as-ulps). This will require a set of unit tests written in the `offload/` project, ideally using the new API that @callumfare is working on.

**Expected result:**

*   Final performance results similar to [Old results](https://dl.acm.org/doi/fullHtml/10.1145/3624062.3624166) but with the more optimized functions and higher accuracy.
*   A test suite that can do brute force testing to confirm that the implementations are conformant.

**Skills:**

Basic C & C++ skills + access to a GPU, some math knowledge

**Project size:** Small

**Difficulty:** Easy / Medium

**Confirmed Mentors:** [Joseph Huber](mailto:joseph.huber@amd.com), [Tue Ly](mailto:lntue.h@gmail.com)

**Discourse:** [URL](https://discourse.llvm.org/t/libc-gsoc-2025-profiling-and-testing-of-the-llvm-libc-gpu-math/84570)

<!-- *********************************************************************** -->

### Validate existing Clang CodeGen test coverage with ClangIR

<!-- *********************************************************************** -->

**Description:** The [ClangIR](https://clangir.org) (CIR) project aims to establish a new intermediate representation (IR) for Clang. Built on top of MLIR, it provides a dialect for C/C++ based languages in Clang, and the necessary infrastructure to emit it from the Clang AST, as well as a lowering path to the LLVM-IR dialect. ClangIR [upstreaming](https://discourse.llvm.org/t/rfc-upstreaming-clangir/76587) is currently in progress.

In order to give community more frequent updates it'd be great if we can report ClangIR progress by measuring the coverage of existing Clang's CodeGen tests in face of a ClangIR enabled pipeline. By collecting information on crashing, passing or failing tests we can come up with a metric that is easier to report and understand, provide entry points for newcomers looking for tasks and help the project by classifying existing issues. Existing Clang CodeGen tests live in clang/test/CodeGen\* and can be found in different states regarding ClangIR support:

*   **FileCheck fails**. LLVM IR builds but FileCheck fails to match output
    *   LLVM IR differs because ClangIR pipeline is emitting different IR (e.g. different instructions are used, missing attributes). Issues need to be created and ClangIR needs to be fixed.
    *   LLVM IR differs because CHECK lines need be made more flexible (LLVM-IR dialect output is different, SSA value names, order of attributes, etc). It's possible a tool like llvm-canon might be of good use here.
*   **Test crash / error**. ClangIR doesn't support some C/C++ construct or LLVM lowering hasn't been implemented.
*   **Test pass**. Yay!

In order to retrieve the information above, the student needs to make changes to Clang's testing infra (LIT configs, scripts, tests, ???) such that it's easier to replay the same invocations with ClangIR enabled, compare against traditional pipeline result or retrieve special directives from tests.

It's not clear what is the best methodology just yet, but it's expected that submitted proposals that want to be taken seriously should present few possible ideas on how to achieve this, prior discussion with other members of the community is encouraged. The student is also expected to interact with the ClangIR community, file github issues, investigate and/or make changes to failing codegen tests.

**Expected result:**

1.  Build the infrastructure to run tests and collect results.
2.  Present the results in a way that can be placed on a webpage.
3.  File issues or change check lines for 50% of the "FileCheck fails" category above. The only subdirectories that need consideration for the moment are:

    ```
    clang/test/CodeGen
        clang/test/CodeGenCXX
        clang/test/CodeGenOpenCL
        clang/test/CodeGenCUDA
    ```

*   Bonus point: find ways to automate/facilitate changes to tests, put PRs to fix problems in ClangIR.

**Skills:** Python, intermediate C++ programming skills and familiarity with basic compiler design concepts are required. Prior experience with LLVM IR, MLIR, Clang or ClangIR programming is a big plus, but willingness to learn is also a possibility.

**Project size:** Large

**Difficulty:** Medium

**Potential Mentors:** [Bruno Cardoso Lopes](https://github.com/bcardosolopes) [Andy Kaylor](https://github.com/andykaylor)

**Discourse:** [URL](https://discourse.llvm.org/t/clangir-gsoc2025-validate-existing-clang-codegen-test-coverage-with-clangir/84481)

<!-- *********************************************************************** -->

### Participate in ClangIR Upstreaming

<!-- *********************************************************************** -->

**Description:** [ClangIR](https://clangir.org) is a new, MLIR\_based intermediate representation of C and C++ code. It has been developed in an LLVM incubator project, but work is now underway to migrate the code from the incubator to the main LLVM repository. As the code is moved, it must be updated to align with LLVM coding standards and quality expectations. The goal for this project is to participate in the ClangIR upstreaming process and help improve both the code and the upstreaming process.

The ClangIR project intends to unlock the possibility of better optimization, analysis, and diagnostics for C and C++ code by adding new abstractions that more closely model the source constructs, preserving more details than are available in standard LLVM IR. The ClangIR dialect is already being used to solve real-world problems using the implementation available in the ClangIR incubator, but we need to move this into the main LLVM repository in order to make this functionality available to a larger audience.

This project will be an opportunity to gain hands-on experience with MLIR development with a focus on day-to-day software engineering discipline. Participants will work side-by-side with other LLVM contributors to achieve a common goal, and in the process will gain a deep understanding of the ClangIR dialect.

**Expected result:**

1.  Migrate ClangIR support for C and C++ language features into the main LLVM repository
2.  Improve the quality of code as it is being migrated
3.  Suggest ways to improve the migration process

**Skills:** Proficiency with modern C++ programming and familiarity with basic compiler design concepts are required. Prior experience with LLVM IR, MLIR, Clang or ClangIR programming is a big plus, but since the goal of this project is to gain such experience, it is not a prerequisite.

**Project size:** Medium to Large

**Difficulty:** Medium

**Potential Mentors:** [Andy Kaylor](https://github.com/andykaylor) [Bruno Cardoso Lopes](https://github.com/bcardosolopes)

**Discourse:** [URL](https://discourse.llvm.org/t/clangir-gsoc-2025-clangir-upstreaming/84766)

<!-- *********************************************************************** -->

### Simple C++20 modules without a build system

<!-- *********************************************************************** -->

**Description**

Currently there is no easy way to take a collection of source files using C++20 modules and build an executable from them. This makes it hard to create simple tests or tiny programs using C++20 modules without first setting up a build system. This project's goal is to extend the extremely simple build system in Clang's driver to handle these cases.

This can be done by using Clang's existing support for scanning for C++20 modules to discover the dependencies between the source files that have been passed in, and then build them in that order, passing in the right PCM files where needed. This may also be extended to support explicitly building Clang modules discovered via module map files too.

**Expected outcomes**

Invoking clang similarly to

```
clang -o program -std=c++20 main.cpp A.cppm B.cppm
```

should compile successfully where each translation-unit only imports modules defined in other source files on the command line, or the standard library. This should add no overhead to cases where modules are not used.

**Confirmed mentors and their contacts**

*   [Michael Spencer](https://github.com/Bigcheese)

**Required skills**

Intermediate knowledge of C++; familiarity with how C++ code is built. Familiarity with C++20 modules is an asset, but not required.

**Size of the project:**

medium (~175h)

**Project difficulty:**

medium

**Discourse:** [URL](https://discourse.llvm.org/t/clang-gsoc-2025-support-simple-c-20-modules-use-from-the-clang-driver-without-a-build-system/84511)

<!-- *********************************************************************** -->

### Usability Improvements for trapping Undefined Behavior Sanitizer (UBSan)

<!-- *********************************************************************** -->

**Description**

Undefined Behavior Sanitizer (UBSan) is a useful compilation mode in Clang for finding uses of undefined behavior (e.g. signed integer overflow) and problematic C/C++ code (e.g. unsigned integer overflow). The default version of UBSan uses a compiler runtime that only works in userspace (e.g. it won’t work in the kernel or for embedded applications) and is not considered secure enough for use in production environments. To handle these other environments UBSan provides a trapping mode that emits trap instructions that immediately halts the application rather than calling into the UBSan runtime which normally diagnoses the problem and then carries on execution.

Unfortunately trapping UBSan has some deficiencies which make it hard to use. In particular:

*   Clang silently ignores the \-fsanitize-trap=undefined flag when it's passed without \-fsanitize=undefined. This project would fix this as a “warm up task” to get familiar with the Clang codebase.
*   When a UBSan trap is hit with the debugger attached it is not convenient to figure out the reason UBSan trapped. For x86\_64 and arm64 some information is encoded in the instruction but decoding this is very inconvenient. While LLDB could be taught to look at the instruction and decode the meaning this is brittle because it depends on undocumented compiler ABI. Instead we can build upon the \_\_builtin\_verbose\_trap work to encode the reason for trapping ("trap reasons") inside the debug information. If time permits we can also investigate emitting more precise trap reasons

**Expected outcomes**

*   When the \-fsanitize-trap=undefined flag is passed on its own the compiler silently ignores it. Currently Clang requires that the \-fsanitize-trap= flag is also passed. Clang should be taught to warn about this.
*   Teach Clang to emit the UBSan trap reasons in debug information on UBSan trap instructions similar to how \_\_builtin\_verbose\_trap works.
*   Confirm LLDB is able to recognize the UBSan trap reasons and add tests for this.
*   If time permits we should investigate emitting more precise trap reasons by using information available in the compiler. We may want to implement a "Sema Diagnostic" like approach where trap reason strings can easily be constructed inside the compiler. This task is more open-ended and has potentially uses outside of UBSan (e.g. \-fbounds-safety).

**Confirmed mentors and their contacts**

*   [Dan Liew](https://github.com/delcypher)
*   [Michael Buch](https://github.com/Michael137)

**Required skills**

Good understanding of C++

**Desirable skills**

*   Familiarity with UBSan
*   Familiarity with LLDB

**Size of the project:**

small (~90h). but can be extended if time allows

**Project difficulty:**

Easy. This project would be good for a beginner to LLVM. Note the "emitting more precise trap reasons" portion is more open ended and so the difficulty of this is entirely down to direction the applicant chooses.

**Discourse:** [URL](https://discourse.llvm.org/t/clang-gsoc-2025-usability-improvements-for-trapping-undefined-behavior-sanitizer/84568)

<!-- *********************************************************************** -->

### Improve documentation parsing in Clang

<!-- *********************************************************************** -->

**Description of the project:** [Clang-Doc](https://clang.llvm.org/extra/clang-doc.html) is a C/C++ documentation generation tool created as an alternative for Doxygen and built on top of LibTooling. This effort started in 2018 and critical mass has landed in 2019, but the development has been largely stagnant mostly due to a lack of resources until last year when the development restarted as a successful Google Summer of Code project.  

The tool is built on top of LibTooling and leverages Clang parsers which supports parsing of Doxygen commands in documentation comments (this support is also used in the implementation of Clang’s

```
-Wdocumentation
```

which can be used to validate the content of documentation comments during compilation).  

Unfortunately, Clang’s documentation parser is incomplete and has several issues:

*   Not all Doxygen commands are supported, limiting the Clang-Doc’s usability.
*   Not all C/C++ constructs are currently handled, most notably C++20 features such as concepts.
*   Markdown support in documentation comments introduced in Doxygen version 1.8.0 is missing.

**Expected result:** The goal of this project is to implement the missing features in Clang’s documentation parser as well as their handling in Clang-Doc to improve the quality of the generated documentation. The eventual goal is for the LLVM project to start using Clang-Doc for generating its reference documentation, but before we can do that we need to ensure that all required features are implemented.  

Successful proposals should focus not only on addressing the existing limitations, but also draw inspiration for other potential improvements from other documentation tools such as [hdoc](https://hdoc.io/), [standardese](https://github.com/standardese/standardese), [subdoc](https://github.com/chromium/subspace/tree/main/subdoc) or [cppdocgen](https://cs.opensource.google/fuchsia/fuchsia/+/main:tools/cppdocgen/).  

Over the course of the project, the candidate will have an opportunity to gain significant experience with LLVM and Clang internals (including lexer and parser) and C/C++ language.

**Skills:** Intermediate knowledge of C++; interest in compilers and parsers. Previous experience with Clang/LibTooling is a bonus but not required.

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentor:** [Petr Hosek](https://github.com/petrhosek), [Paul Kirth](https://github.com/ilovepi)

**Discourse:** [URL](https://discourse.llvm.org/t/improve-documentation-parsing-in-clang/84513)

<!-- *********************************************************************** -->

### Advanced symbol resolution and reoptimization for clang-repl

<!-- *********************************************************************** -->

**Description of the project:** The Clang compiler is part of the LLVM compiler infrastructure and supports various languages such as C, C++, ObjC and ObjC++. The design of LLVM and Clang enables them to be used as libraries, and has led to the creation of an entire compiler-assisted ecosystem of tools. The relatively friendly codebase of Clang and advancements in the JIT infrastructure in LLVM further enable research into different methods for processing C++ by blurring the boundary between compile time and runtime. Challenges include incremental compilation and fitting compile/link time optimizations into a more dynamic environment. Incremental compilation pipelines process code chunk-by-chunk by building an ever-growing translation unit. Code is then lowered into the LLVM IR and subsequently run by the LLVM JIT. Such a pipeline allows creation of efficient interpreters. The interpreter enables interactive exploration and makes the C++ language more user friendly. Clang-Repl is one example.

**Expected result:** The project aims to develop a robust mechanism for resolving missing symbols by dynamically identifying and loading the appropriate shared objects or static archives. Additionally, it will explore use cases where adapting symbols based on execution profiles leads to measurable performance improvements, optimizing the efficiency of just-in-time compilation and dynamic execution environments.

**Skills:** Intermediate knowledge of C++, Understanding of LLVM and the LLVM JIT in particular

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev)

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc2025-advanced-symbol-resolution-and-reoptimization-for-clang-repl)

<!-- *********************************************************************** -->

### Improve Enzyme reliability and compile times for Rust

<!-- *********************************************************************** -->

**Description**

Enzyme requires good information about the memory layout of types. LLVM-IR is intentionally opaque, e.g. \`&f32\` and \`&f64\` both have the LLVM-IR type \`ptr\`. Enzyme is generally able to infer the underlying type (e.g. f32 vs f64) through usage analysis, but that process is slow and can in some cases fail. To make autodiff more robust, we should lower either MIR or THIR type information into LLVM-IR metadata. This analysis is recursive, for example \`&\[T\]\` is a fat pointer and therefore will be represented as a (ptr, int) pair in LLVM-IR. In this case the algorithm should recursively also analyze \`T\` and generate metadata for it.

The function [here](https://github.com/rust-lang/rust/blob/d4bdd1ed551fed0c951eb47b4be2c79d7a02d181/compiler/rustc_monomorphize/src/partitioning/autodiff.rs#L30) can be extended to generate metadata from rusts Mid-level IR (MIR). A prototype of the parser was implemented [here](https://github.com/EnzymeAD/rust/blob/58fee1abf3f2cd0e73ee8b98e53869d6fc3ba604/compiler/rustc_middle/src/ty/mod.rs#L2826) and can be used for inspiration. Various LLVM-IR examples for the metadata which we want to generate can be found in [this](https://github.com/EnzymeAD/Enzyme/blob/main/enzyme/test/TypeAnalysis) test folder. Look for annotations in the style of \` {\[-1\]:Pointer, \[-1,0\]:Float@float}\`.

The online compiler [Explorer](https://enzyme.mit.edu/explorer/) fork can be used to trigger related bugs, starting with "can not deduce type of X".

**Expected outcomes**

The participant should find and select some interesting testcases, in which Enzyme either fails to differentiate an example due to inssuficient Type Information, or takes unreasonable long times (e.g. > 20x slower than compiling the code without autodiff). In the second case, a profiler should be used to verify that Enzyme causes a long compile time due to type analysis. The participant should then write (or later extend) the Type parser to generate the correct metadata, such that Enzyme can handle the new testcases. The LIT testcases should be added to the rust compiler, to avoid further regressions.

Examples for code that currently is not handled correctly can be discussed in the project proposal phase.

**Confirmed mentors and their contacts**

*   [Manuel Drehwald](https://github.com/ZuseZ4)
*   [Oli Scherer](https://github.com/oli-obk)
*   [Johannes Doerfert](https://github.com/jdoerfert)

**Required skills**

Intermediate knowledge of Rust and C++; Familiarity with profilers or LLVM metadata is an asset, but not required.

**Size of the project:**

medium (~175h)

**Project difficulty:**

medium

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc2025-improve-rust-enzyme-reliability-and-compile-times/84523)

<!-- *********************************************************************** -->

### Introduce an ABI lowering library

<!-- *********************************************************************** -->

**Description:** Currently, every LLVM-based frontend that wants to support calling into C code (FFI) needs to re-implement a substantial amount of complex call ABI handling. The goal of this project is to introduce an LLVM ABI library, which can be reused across different frontends, including Clang. More details on the motivation and a broad outline of the design are available in the [corresponding RFC](https://discourse.llvm.org/t/rfc-an-abi-lowering-library-for-llvm/84495/1).

The initial phase of the project will be to implement a prototype that can handle at least the x86\_64 System V ABI. This will involve implementing the ABI type system, mapping of Clang types to ABI types and moving at least part of the X86 ABIInfo implementation from Clang to the new ABI library. This is to demonstrate general feasibility, figure out design questions and analyze compilation-time impact.

Assuming the results from the prototype are positive, the next step would be to upstream the implementation by splitting it into smaller PRs. Finally, the implementation can be expanded to cover additional targets, ultimately removing Clang's ABI handling code entirely.

**Expected result:** The minimum result is a prototype for the x86\_64 ABI. The maximum result is fully upstreamed support for all targets. The expected result is somewhere in the middle between those two.

**Skills:** Intermediate C++. Some familiarity with LLVM is a plus, but not required.

**Project size:** Large

**Difficulty:** Hard

**Confirmed mentors:** [Nikita Popov](https://github.com/nikic)

**Discourse:** [URL](https://discourse.llvm.org/t/llvm-introduce-an-abi-lowering-library/84554)

<!-- *********************************************************************** -->

### Byte type

<!-- *********************************************************************** -->

**Description:** LLVM IR can't represent implementations of memcpy, memcmp, etc correctly due to the lack of a way to represent raw memory. This project aims to add a new 'byte' type to the LLVM IR to represent raw memory.

In addition to adding the new type, the project involves changing clang to lower chars to the new b8 type instead of i8, fixing incorrect lowerings of memory intrinsics, and tracking down the performance regressions.

There is already a [prototype](https://github.com/georgemitenkov/GSoC-2021) implementation of the byte type for an older version of LLVM. More information [here](https://gist.github.com/georgemitenkov/3def898b8845c2cc161bd216cbbdb81f).

**Expected result:** The minimum result is a port of the existing prototype to the current LLVM, fixing all known incorrect optimizations, add support for the byte type to Alive2, and a performance analysis.

**Skills:** Intermediate C++, familiarity with LLVM, profiling.

**Project size:** Large

**Difficulty:** Hard

**Confirmed mentors:** [Nuno Lopes](https://web.ist.utl.pt/nuno.lopes/)

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2025-byte-type/84636)

<!-- *********************************************************************** -->

### LLVM Compiler Remarks Visualization Tool for Offload Proposal

<!-- *********************************************************************** -->

**Description:** LLVM offers different information via remarks, profiling, or runtime debug annotations (e.g., LIBOMPTARGET\_INFO=-1). However, as projects increase, dissecting this information becomes difficult for users. For example, it is difficult to collect all this data, visualize it, and learn from it when building large projects.

Currently, some of this information—for example, compilation remarks—can be exported in JSON format. We want to create a tool to visualize, aggregate, and summarize the information. To aid accelerator development, we will start with the offload project as the primary candidate.

Similar tools, such as opt-viewer, can be used as references and starting points.

**Expected outcomes:** The expected outcome is a tool (e.g., in the form of a compiler wrapper such as ccache) that will allow the dump of all the compiler-generated information in JSON format and organize it in a project structure.

The tool should generate an HTML-based report to help visualize the remarks. We envision a small client-server application using Python to spawn a local server as the visualization's front end. The server will expose the different reports and perform early analysis and aggregation.

Additionally, the tool should be designed so that, in the future, the analysis of the remarks can provide generalized guidelines for the developer (e.g., show the most common remark, use LLM models to explain actions, etc.). The client (HTML viewer) will display the aggregated data, in-line remarks, profile information, etc. We do not expect the project to have all the features at the end of the GSoC but to serve as a placeholder for growth in the future.

In particular, the outcomes of this project should be:

*   Together with the mentors, help the design of the compiler wrapper, data storage layer, and client/server infrastructure. This includes the server API. The outcome of this task is a design document (similar to an RFC).
*   Create a compiler wrapper that will dump different information in JSON format into the data storage layer (e.g., folders).
*   Create a simple server layer that exposes the backend API to the front end. Python is the right way to do this, but we welcome other suggestions that align with the LLVM project. We would like to avoid relying on external projects (e.g., Flask) to avoid adding more dependencies to the LLVM project.
*   Create a simple client-side visualization tool that can be extended in the future to show more reports.

**Mentors:** [@shiltian](https://github.com/shiltian), [@jdoerfert](https://github.com/jdoerfert), [@josemonsalve2](https://github.com/josemonsalve2)

**Required/desired skills:**

*   Basic understanding of the LLVM Compiler to be able to generate compiler remarks, profiling data, and other information from the compiler.
*   Proficiency in Python and C++.
*   Full-stack web development.

**Project size:** Large

**Difficulty:** Easy

**Discourse Link:** [\[GSoC\]\[Offload\]LLVM Compiler Remarks Visualization Tool for Offload Proposal](https://discourse.llvm.org/t/gsoc-offload-llvm-compiler-remarks-visualization-tool-for-offload-proposal/84596)

<!-- *********************************************************************** -->

# Google Summer of Code 2024

<!-- *********************************************************************** -->

Google Summer of Code 2024 was yet another successful one for LLVM project. For the list of accepted and completed projects, please take a look into Google Summer of Code [website](https://summerofcode.withgoogle.com/archive/2024/organizations/llvm-compiler-infrastructure).

Welcome prospective Google Summer of Code 2024 Students! This document is your starting point to finding interesting and important projects for LLVM, Clang, and other related sub-projects. This list of projects is not only developed for Google Summer of Code, but open projects that really need developers to work on and are very beneficial for the LLVM community.

We encourage you to look through this list and see which projects excite you and match well with your skill set. We also invite proposals not on this list. More information and discussion about GSoC can be found in [discourse](https://discourse.llvm.org/c/community/gsoc) . If you have questions about a particular project please find the relevant entry in discourse, check previous discussion and ask. If there is no such entry or you would like to propose an idea please create a new entry. Feedback from the community is a requirement for your proposal to be considered and hopefully accepted.

The LLVM project has participated in Google Summer of Code for several years and has had some very successful projects. We hope that this year is no different and look forward to hearing your proposals. For information on how to submit a proposal, please visit the Google Summer of Code main [website.](https://summerofcode.withgoogle.com/)

<!-- *********************************************************************** -->

### Remove undefined behavior from tests

<!-- *********************************************************************** -->

**Description of the project:** Many of LLVM's unit tests have been reduced automatically from larger tests. Previous-generation reduction tools used undef and poison as placeholders everywhere, as well as introduced undefined behavior (UB). Tests with UB are not desirable because 1) they are fragile since in the future the compiler may start optimizing more aggressively and break the test, and 2) it breaks translation validation tools such as [Alive2](https://github.com/AliveToolkit/alive2/) (since it's correct to translate a fuction that is always UB into anything).  
The major steps include:

1.  Replace known patterns such as branch on undef/poison, memory accesses with invalid pointers, etc with non-UB patterns.
2.  Use Alive2 to detect further patterns (by searching for tests that are always UB).
3.  Report any LLVM bug found by Alive2 that is exposed when removing UB.

**Expected result:** The majority of LLVM's unit tests will be free of UB.

**Skills:** Experience with scripting (Python or PHP) is required. Experience with regular expressions is encouraged.

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentor:** [Nuno Lopes](https://web.ist.utl.pt/nuno.lopes/)

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2004-remove-undefined-behavior-from-tests/77236)

<!-- *********************************************************************** -->

### Automatically generate TableGen file for SPIR-V instruction set

<!-- *********************************************************************** -->

**Description of the project:** The existing file that describes the SPIR-V instruction set in LLVM was manually created and is not always complete or up to date. Whenever new instructions need to be added to the SPIR-V backend, the file must be amended. In addition, since it is not created in a systematic way, there are often slight discrepancies between how an instruction is described in the SPIR-V spec and how it is declared in the TableGen file. Since SPIR-V backend developers often use the spec as a reference when developing new features, having a consistent mapping between the specification and TableGen records will ease development. This project proposes creating a script capable of generating a complete TableGen file that describes the SPIR-V instruction set given the JSON grammar available in the KhronosGroup/SPIRV-Headers repository, and updating SPIR-V backend code to use the new definitions. The specific method used for translating the JSON grammar to TableGen is left up to the discretion of the applicant, however, it should be checked into the LLVM repository with well-documented instructions to replicate the translation process so that future maintainers will be able to regenerate the file when the grammar changes. Note that the grammar itself should remain out-of-tree in its existing separate repository.

**Expected result:**

*   The SPIR-V instruction set's definition in TableGen is replaced with one that is autogenerated.
*   A script and documentation are written that support regenerating the definitions as needed given the JSON grammar of the SPIR-V instruction set.
*   Usage of the SPIR-V instruction set in the SPIR-V backend updated to use the new autogenerated definitions.

**Skills:** Experience with scripting and an intermediate knowledge of C++. Previous experience with LLVM/TableGen is a bonus but not required.

**Project size:** Medium (175 hour)

**Confirmed Mentors:** [Natalie Chouinard](https://github.com/sudonatalie/), [Nathan Gauër](https://github.com/keenuts/)

**Discourse:** [URL](https://discourse.llvm.org/t/clang-automatically-generate-tablegen-file-for-spir-v-instruction-set/76369)

<!-- *********************************************************************** -->

### LLVM bitstream integration with CAS (content-addressable storage)

<!-- *********************************************************************** -->

**Description of the project:** The LLVM bitstream file format is used for serialization of intermediate compiler artifacts, such as LLVM IR or Clang modules. There are situations where multiple bitstream files store identical information, and this duplication leads to increased storage requirements.  

This project aims to integrate the LLVM CAS library into the LLVM bitstream file format. If we factor out the frequently duplicated part of a bitstream file into a separate CAS object, we can replace all copies with a small reference to the canonical CAS object, saving storage.  

The primary motivating use-case for this project is the dependency scanner that's powering "implicitly-discovered, explicitly-built" Clang modules. There are real-world situations where even coarse de-duplication on the block level could halve the size of the scanning module cache.

**Expected result:** There's a way to configure the LLVM bitstream writer/reader to use CAS as the backing storage.

**Skills:** Intermediate knowledge of C++, some familiarity with data serialization, self-motivation.

**Project size:** Medium or large

**Confirmed Mentors:** [Jan Svoboda](https://github.com/jansvoboda11/), [Steven Wu](https://github.com/cachemeifyoucan/)

**Discourse:** [URL](https://discourse.llvm.org/t/llvm-bitstream-integration-with-cas-content-addressable-storage/76757)

<!-- *********************************************************************** -->

### Add 3-way comparison intrinsics

<!-- *********************************************************************** -->

**Description of the project:** [3-way comparisons](https://en.wikipedia.org/wiki/Three-way_comparison) return the values -1, 0 or 1 depending on whether the values compare lower, equal or greater. They are exposed in C++ via the spaceship operator (operator<=>) and in Rust via the PartialOrd and Ord traits. Currently, such comparisons produce sub-optimal codegen and optimization results in some cases.  

The goal of this project is to resolve these optimization issues by implementing new 3-way comparison intrinsics, as described in [\[RFC\] Add 3-way comparison intrinsics](https://discourse.llvm.org/t/rfc-add-3-way-comparison-intrinsics/76685). The implementation steps are broadly:

1.  Add the intrinsics to LLVM IR.
2.  Implement legalization/expansion support in SelectionDAG and GlobalISel.
3.  Implement optimization support in ConstantFolding, InstSimplify, InstCombine, CorrelatedValuePropagation, IndVarSimplify, ConstraintElimination, IPSCCP, and other relevant transforms.
4.  Make use of the intrinsics via InstCombine canonicalization or direct emission in clang/rustc.

Adding new target-independent intrinsics is a good way of becoming familiar with a broad slice of LLVM!

**Expected result:** Support for the intrinsics in the backend and the most important optimization passes. Ideally full integration starting at the frontend.

**Skills:** Intermediate knowledge of C++

**Project size:** Medium or large

**Difficulty:** Medium

**Confirmed Mentors:** [Nikita Popov](https://github.com/nikic), [Dhruv Chawla](https://github.com/dc03)

**Discourse:** [URL](https://discourse.llvm.org/t/llvm-add-3-way-comparison-intrinsics/76807)

<!-- *********************************************************************** -->

### Improve the LLVM.org Website Look and Feel

<!-- *********************************************************************** -->

**Description of the project:** The llvm.org website serves as the central hub for information about the LLVM project, encompassing project details, current events, and relevant resources. Over time, the website has evolved organically, prompting the need for a redesign to enhance its modernity, structure, and ease of maintenance.  

The goal of this project is to create a contemporary and coherent static website that reflects the essence of LLVM.org. This redesign aims to improve navigation, taxonomy, content discoverability, mobile device support, accessibility, and overall usability. Given the critical role of the website in the community, efforts will be made to engage with community members, seeking consensus on the proposed changes.

**Expected result:** A modern, coherent-looking website that attracts new prospect users and empowers the existing community with better navigation, taxonomy, content discoverability, and overall usability. Since the website is a critical infrastructure and most of the community will have an opinion this project should try to engage with the community building community consensus on the steps being taken. Suggested approach:

*   Conduct a comprehensive content audit of the existing website.
*   Select appropriate technologies, preferably static site generators like Hugo or Jekyll.
*   Advocate for a separation of data and visualization, utilizing formats such as YAML and Markdown to facilitate content management without direct HTML coding.
*   Present three design mockups for the new website, fostering open discussions and allowing time for alternative proposals from interested parties.
*   Implement the chosen design, incorporating valuable feedback from the community.
*   Collaborate with content creators to integrate or update content as needed.

The successful candidate should commit to regular participation in weekly meetings, deliver presentations, and contribute blog posts as requested. Additionally, they should demonstrate the ability to navigate the community process with patience and understanding.

**Skills:** Knowledge in the area of web development with static site generators. Knowledge in html, css, bootstrap, and markdown. Patience and self-motivation.

**Difficulty:** Hard

**Project size:** Large

**Confirmed Mentors:** [Tanya Lattner](https://github.com/tlattner), [Vassil Vassilev](https://github.com/vgvassilev)

**Discourse:** [URL](https://discourse.llvm.org/t/improve-the-llvm-org-website-look-and-feel/76864)

<!-- *********************************************************************** -->

### Out-of-process execution for clang-repl

<!-- *********************************************************************** -->

**Description of the project:** The Clang compiler is part of the LLVM compiler infrastructure and supports various languages such as C, C++, ObjC and ObjC++. The design of LLVM and Clang enables them to be used as libraries, and has led to the creation of an entire compiler-assisted ecosystem of tools. The relatively friendly codebase of Clang and advancements in the JIT infrastructure in LLVM further enable research into different methods for processing C++ by blurring the boundary between compile time and runtime. Challenges include incremental compilation and fitting compile/link time optimizations into a more dynamic environment.  

Incremental compilation pipelines process code chunk-by-chunk by building an ever-growing translation unit. Code is then lowered into the LLVM IR and subsequently run by the LLVM JIT. Such a pipeline allows creation of efficient interpreters. The interpreter enables interactive exploration and makes the C++ language more user friendly. Clang-Repl is one example.  

Clang-Repl uses the Orcv2 JIT infrastructure within the same process. That design is efficient and easy to implement however it suffers from two significant drawbacks. First, it cannot be used in devices which do not have sufficient resources to host the entire infrastructure, such as the arduino due (see this [talk](https://compiler-research.org/meetings/#caas_10Mar2022) for more details). Second, crashes in user codes mean that the entire process crashes, hindering overall reliability and ease of use.  

This project aims to move Clang-Repl to an out-of-process execution model in order to address both of these issues.

**Expected result:** Implement an out-of-process execution of statements with Clang-Repl; Demonstrate that Clang-Repl can support some of the ez-clang use-cases; Research into approaches to restart/continue the session upon crash; As a stretch goal design a versatile reliability approach for crash recovery;

**Skills:** Intermediate knowledge of C++, Understanding of LLVM and the LLVM JIT in particular

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev),

**Discourse:** [URL](https://discourse.llvm.org/t/clang-out-of-process-execution-for-clang-repl/68225)

<!-- *********************************************************************** -->

### Support clang plugins on Windows

<!-- *********************************************************************** -->

**Description of the project:** The Clang compiler is part of the LLVM compiler infrastructure and supports various languages such as C, C++, ObjC and ObjC++. The design of LLVM and Clang allows the compiler to be extended with plugins\[1\]. A plugin makes it possible to run extra user defined actions during a compilation. Plugins are supported on unix and darwin but not on windows due to some specifics of the windows platform.  

This project would expose the participant to a broad cross section of the LLVM codebase. It involves exploring the API surface, classifying the interfaces as being public or private, and annotating that information to the API declarations. It would also expose the participant to details and differences of different platforms as this work is cross-platform (Windows, Linux, Darwin, BSD, etc). The resulting changes would improve LLVM on Linux and Windows while enabling new functionality on Windows.

**Expected result:** This project aims to allow make clang -fplugin=windows/plugin.dll work. The implementation approach should extend the working prototype \[3\] and extend the annotation tool \[4\]. The successful candidate should be prepared to attend a weekly meeting, make presentations and prepare blog posts upon request.

*Further reading*  
\[1\] https://clang.llvm.org/docs/ClangPlugins.html  
\[2\] https://discourse.llvm.org/t/clang-plugins-on-windows  
\[3\] https://github.com/llvm/llvm-project/pull/67502  
\[4\] https://github.com/compnerd/ids

**Skills:** Intermediate knowledge of C++, Experience with Windows and its compilation and linking model.

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev), [Saleem Abdulrasool](https://github.com/compnerd)

**Discourse:** [URL](https://discourse.llvm.org/t/support-clang-plugins-on-windows/76408)

<!-- *********************************************************************** -->

### On Demand Parsing in Clang

<!-- *********************************************************************** -->

**Description of the project:** Clang, like any C++ compiler, parses a sequence of characters as they appear, linearly. The linear character sequence is then turned into tokens and AST before lowering to machine code. In many cases the end-user code uses a small portion of the C++ entities from the entire translation unit but the user still pays the price for compiling all of the redundancies.  

This project proposes to process the heavy compiling C++ entities upon using them rather than eagerly. This approach is already adopted in Clang’s CodeGen where it allows Clang to produce code only for what is being used. On demand compilation is expected to significantly reduce the compilation peak memory and improve the compile time for translation units which sparsely use their contents. In addition, that would have a significant impact on interactive C++ where header inclusion essentially becomes a no-op and entities will be only parsed on demand.  

The Cling interpreter implements a very naive but efficient cross-translation unit lazy compilation optimization which scales across hundreds of libraries in the field of high-energy physics.  

```
// A.h
#include &lt;string&gt;
#include &lt;vector&gt;
template &lt;class T, class U = int&gt; struct AStruct {
  void doIt() { /*...*/ }
  const char* data;
  // ...
};

template&lt;class T, class U = AStruct<T&gt;>
inline void freeFunction() { /* ... */ }
inline void doit(unsigned N = 1) { /* ... */ }

// Main.cpp
#include "A.h"
int main() {
  doit();
  return 0;
}
```

This pathological example expands to 37253 lines of code to process. Cling builds an index (it calls it an autoloading map) where it contains only forward declarations of these C++ entities. Their size is 3000 lines of code. The index looks like:

```
// A.h.index
namespace std{inline namespace __1{template &lt;class _Tp, class _Allocator&gt; class __attribute__((annotate("$clingAutoload$vector")))  __attribute__((annotate("$clingAutoload$A.h")))  __vector_base;
  }}
...
template &lt;class T, class U = int&gt; struct __attribute__((annotate("$clingAutoload$A.h"))) AStruct;
```

Upon requiring the complete type of an entity, Cling includes the relevant header file to get it. There are several trivial workarounds to deal with default arguments and default template arguments as they now appear on the forward declaration and then the definition. You can read more in \[1\].  

Although the implementation could not be called a reference implementation, it shows that the Parser and the Preprocessor of Clang are relatively stateless and can be used to process character sequences which are not linear in their nature. In particular namespace-scope definitions are relatively easy to handle and it is not very difficult to return to namespace-scope when we lazily parse something. For other contexts such as local classes we will have lost some essential information such as name lookup tables for local entities. However, these cases are probably not very interesting as the lazy parsing granularity is probably worth doing only for top-level entities.  

Such implementation can help with already existing issues in the standard such as CWG2335, under which the delayed portions of classes get parsed immediately when they're first needed, if that first usage precedes the end of the class. That should give good motivation to upstream all the operations needed to return to an enclosing scope and parse something.  

**Implementation approach**: Upon seeing a tag definition during parsing we could create a forward declaration, record the token sequence and mark it as a lazy definition. Later upon complete type request, we could re-position the parser to parse the definition body. We already skip some of the template specializations in a similar way \[2, 3\].  

Another approach is every lazy parsed entity to record its token stream and change the Toks stored on LateParsedDeclarations to optionally refer to a subsequence of the externally-stored token sequence instead of storing its own sequence (or maybe change CachedTokens so it can do that transparently). One of the challenges would be that we currently modify the cached tokens list to append an "eof" token, but it should be possible to handle that in a different way.  

In some cases, a class definition can affect its surrounding context in a few ways you'll need to be careful about here:  

1) \`struct X\` appearing inside the class can introduce the name \`X\` into the enclosing context.  

2) \`static inline\` declarations can introduce global variables with non-constant initializers that may have arbitrary side-effects.  

For point (2), there's a more general problem: parsing any expression can trigger a template instantiation of a class template that has a static data member with an initializer that has side-effects. Unlike the above two cases, I don't think there's any way we can correctly detect and handle such cases by some simple analysis of the token stream; actual semantic analysis is required to detect such cases. But perhaps if they happen only in code that is itself unused, it wouldn't be terrible for Clang to have a language mode that doesn't guarantee that such instantiations actually happen.  

Alternative and more efficient implementation could be to make the lookup tables range based but we do not have even a prototype proving this could be a feasible approach.

**Expected result:**

*   Design and implementation of on-demand compilation for non-templated functions
*   Support non-templated structs and classes
*   Run performance benchmarks on relevant codebases and prepare report
*   Prepare a community RFC document
*   \[Stretch goal\] Support templates

The successful candidate should commit to regular participation in weekly meetings, deliver presentations, and contribute blog posts as requested. Additionally, they should demonstrate the ability to navigate the community process with patience and understanding.

*Further reading*  
\[1\] https://github.com/root-project/root/blob/master/README/README.CXXMODULES.md#header-parsing-in-root  
\[2\] https://github.com/llvm/llvm-project/commit/b9fa99649bc99  
\[3\] https://github.com/llvm/llvm-project/commit/0f192e89405ce

**Skills:** Knowledge of C++, Deeper understanding of how Clang works, knowledge of Clang AST and Preprocessor.

**Project size:** Large

**Difficulty:** Hard

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev), [Matheus Izvekov](https://github.com/mizvekov)

**Discourse:** [URL](https://discourse.llvm.org/t/on-demand-parsing-in-clang/76912)

<!-- *********************************************************************** -->

### Improve Clang-Doc Usability

<!-- *********************************************************************** -->

**Description of the project:** [Clang-Doc](https://clang.llvm.org/extra/clang-doc.html) is a C/C++ documentation generation tool created as an alternative for Doxygen and built on top of LibTooling. This effort started in 2018 and critical mass has landed in 2019, but the development has been largely dormant since then, mostly due to a lack of resources.  

The tool can currently generate documentation in Markdown and HTML formats, but the tool has some structural issues, is difficult to use, the generated documentation has usability issues and is missing several key features:

*   Not all C/C++ constructs are currently handled by the Markdown and HTML emitter limiting the tool’s usability.
*   The generated HTML output does not scale with the size of the codebase making it unusable for larger C/C++ projects.
*   The implementation does not always use the most efficient or appropriate data structures which leads to correctness and performance issues.
*   There is a lot of duplicated boiler plate code which could be improved with templates and helpers.

**Expected result:** The goal of this project is to address the existing shortcomings and improve the usability of Clang-Doc to the point where it can be used to generate documentation for large scale projects such as LLVM. The ideal outcome is that the LLVM project will use Clang-Doc for generating its [reference documentation](https://llvm.org/doxygen/).  

Successful proposals should focus not only on addressing the existing limitations, but also draw inspiration for other potential improvements from other similar tools such as [hdoc](https://hdoc.io/), [standardese](https://github.com/standardese/standardese), [subdoc](https://github.com/chromium/subspace/tree/main/subdoc) or [cppdocgen](https://cs.opensource.google/fuchsia/fuchsia/+/main:tools/cppdocgen/).

**Skills:** Experience with web technologies (HTML, CSS, JS) and an intermediate knowledge of C++. Previous experience with Clang/LibTooling is a bonus but not required.

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentor:** [Petr Hosek](https://github.com/petrhosek), [Paul Kirth](https://github.com/ilovepi)

**Discourse:** [URL](https://discourse.llvm.org/t/improve-clang-doc-usability/76996)

<!-- *********************************************************************** -->

### Rich Disassembler for LLDB

<!-- *********************************************************************** -->

**Description**

Use the variable location information from the debug info to annotate LLDB’s disassembler (and \`register read\`) output with the location and lifetime of source variables. The rich disassembler output should be exposed as structured data and made available through LLDB’s scripting API so more tooling could be built on top of this. In a terminal, LLDB should render the annotations as text.

**Expected outcomes**

For example, we could augment the disassembly for the following function

```
frame #0: 0x0000000100000f80 a.out`main(argc=1, argv=0x00007ff7bfeff1d8) at demo.c:4:10 [opt]
  1   void puts(const char*);
  2   int main(int argc, char **argv) {
  3    for (int i = 0; i < argc; ++i)
→ 4      puts(argv[i]);
  5    return 0;
  6   }
(lldb) disassemble
a.out`main:
...
  0x100000f71 <+17>: movl  %edi, %r14d
  0x100000f74 <+20>: xorl  %r15d, %r15d
  0x100000f77 <+23>: nopw  (%rax,%rax)
→  0x100000f80 <+32>: movq  (%rbx,%r15,8), %rdi
  0x100000f84 <+36>: callq 0x100000f9e ; symbol stub for: puts
  0x100000f89 <+41>: incq  %r15
  0x100000f8c <+44>: cmpq  %r15, %r14
  0x100000f8f <+47>: jne 0x100000f80 ; <+32> at demo.c:4:10
  0x100000f91 <+49>: addq  $0x8, %rsp
  0x100000f95 <+53>: popq  %rbx
...
```

using the debug information that LLDB also has access to (observe how the source variable i is in r15 from \[0x100000f77+slide))

```
$ dwarfdump demo.dSYM --name  i
demo.dSYM/Contents/Resources/DWARF/demo: file format Mach-O 64-bit x86-64
0x00000076: DW_TAG_variable
 DW_AT_location (0x00000098:
 [0x0000000100000f60, 0x0000000100000f77): DW_OP_consts +0, DW_OP_stack_value
 [0x0000000100000f77, 0x0000000100000f91): DW_OP_reg15 R15)
 DW_AT_name ("i")
 DW_AT_decl_file ("/tmp/t.c")
 DW_AT_decl_line (3)
 DW_AT_type (0x000000b2 "int")
```

to produce output like this, where we annotate when a variable is live and what its location is:

```
(lldb) disassemble
a.out`main:
...                                                               ; i=0
  0x100000f74 <+20>: xorl  %r15d, %r15d                           ; i=r15
  0x100000f77 <+23>: nopw  (%rax,%rax)                            ; |
→  0x100000f80 <+32>: movq  (%rbx,%r15,8), %rdi                   ; |
  0x100000f84 <+36>: callq 0x100000f9e ; symbol stub for: puts    ; |
  0x100000f89 <+41>: incq  %r15                                   ; |
  0x100000f8c <+44>: cmpq  %r15, %r14                             ; |
  0x100000f8f <+47>: jne 0x100000f80 ; <+32> at t.c:4:10          ; |
  0x100000f91 <+49>: addq  $0x8, %rsp                             ; i=undef
  0x100000f95 <+53>: popq  %rbx
```

The goal would be to produce output like this for a subset of unambiguous cases, for example, variables that are constant or fully in registers.

**Confirmed mentors and their contacts**

*   Adrian Prantl aprantl@apple.com (primary contact)
*   Jonas Devlieghere jdevlieghere@apple.com

**Required / desired skills**

Required:

*   Good understanding of C++
*   Familiarity with using a debugger on the terminal
*   Need to be familiar with all the concepts mentioned in the example above
*   Need to have a good understanding of at least one assembler dialect for machine code (x86\_64 or AArch64).

Desired:

*   Compiler knowledge including data flow and control flow analysis is a plus.
*   Being able to navigate debug information (DWARF) is a plus.

**Size of the project.**

medium (~175h)

**An easy, medium or hard rating if possible**

hard

**Discourse:** [URL](https://discourse.llvm.org/t/rich-disassembler-for-lldb/76952)

<!-- *********************************************************************** -->

### GPU Delta Debugging

<!-- *********************************************************************** -->

**Description**

LLVM-reduce, and similar tools perform delta debugging but are less useful if many implicit constraints exist and violation could easily lead to errors similar to the cause that is to be isolated. This project is about developing a GPU-aware version, especially for execution time bugs, that can be used in conjunction with LLVM/OpenMP GPU-record-and-replay, or simply a GPU loader script, to minimize GPU test cases more efficiently and effectively.

**Expected outcomes**

A tool to reduce GPU errors without loosing the original error. Optionally, other properties could be the focus of the reduction, not only errors.

**Confirmed mentors and their contacts**

*   Parasyris, Konstantinos parasyris1@llnl.gov
*   Johannes Doerfert jdoerfert@llnl.gov

**Required / desired skills**

Required:

*   Good understanding of C++
*   Familiarity with GPUs and LLVM-IR

Desired:

*   Compiler knowledge including data flow and control flow analysis is a plus.
*   Experience with debugging and bug reduction techniques (llvm-reduce) is helpful

**Size of the project.**

medium

**An easy, medium or hard rating if possible**

medium

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2024-gpu-delta-debugging/77237)

<!-- *********************************************************************** -->

### Offloading libcxx

<!-- *********************************************************************** -->

**Description**

Modern C++ defines parallel algorithms as part of the standard library, like \`std::transform\_reduce(std::execution::par\_unseq, vec.begin(), vec.end(), 0, std::plus&lt;int&gt;, …)\`. In this project we want to extend an implementation of those that is using OpenMP, including GPU offload, where reasonable. While some algorithms might be amenable to GPU offload via a pure (wrapper) runtime solution, we know others, especially those featuring user provided functors, will also require static program analysis and potentially transformation for additional data management. The goal of the project is to explore different algorithms and the options we have to execute them on the host as well as on accelerator devices, esp. GPUs, automatically via OpenMP.

**Expected outcomes**

Improvements to the prototype support of offloading in libcxx. Evaluations against other offloading approaches and documentation on the missing parts and shortcommings.

**Confirmed mentors and their contacts**

*   Johannes Doerfert jdoerfert@llnl.gov
*   Tom Scogland scogland1@llnl.gov
*   Tom Deakin tom.deakin@bristol.ac.uk

**Required / desired skills**

Required:

*   Good understanding of C++ and C++ standard algorithms
*   Familiarity with GPUs and (OpenMP) offloading

Desired:

*   Experience with libcxx (development).
*   Experience debugging and profiling GPU code.

**Size of the project.**

large

**An easy, medium or hard rating if possible**

medium

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2024-offloading-libcxx/77238)

<!-- *********************************************************************** -->

### The 1001 thresholds in LLVM

<!-- *********************************************************************** -->

**Description**

LLVM has lots of thresholds and flags to avoid "costly cases". However, it is unclear if these thresholds are useful, their value is reasonable, and what impact they really have. Since there are a lot, we cannot do a simple exhaustive search. In some prototype work we introduced a C++ class that can replace hardcoded values and offers control over the threshold, e.g., you can increase the recursion limit via a command line flag from the hardcoded "6" to a different number. In this project we want to explore the thresholds, when they are hit, what it means if they are hit, how we should select their values, and if we need different "profiles".

**Expected outcomes**

Statistical evidence on the impact of various thresholds inside of LLVM's code base, including compile time changes, impact on transformations, and performance measurements.

**Confirmed mentors and their contacts**

*   Jan Hueckelheim jhueckelheim@anl.gov
*   Johannes Doerfert jdoerfert@llnl.gov
*   William Moses wmoses@mit.edu

**Required / desired skills**

Required:

*   Profiling skills and knowledge of statistical reasoning

Desired:

*   Good understanding of the LLVM code base and optimization flow

**Size of the project.**

medium

**An easy, medium or hard rating if possible**

easy

**Discourse:** [URL](https://discourse.llvm.org/t/gsoc-2024-the-1001-thresholds-in-llvm/77235)

<!-- *********************************************************************** -->

### Performance tuning the GPU libc

<!-- *********************************************************************** -->

**Description**

We have begun work on a libc library targeting GPUs. This will allow users to call functions such as malloc or memcpy while executing on the GPU. However, it is important that these implementations be functional and performant. The goal of this project is to benchmark the implementations of certain libc functions on the GPU. Work would include writing benchmarks to test the current implementations as well as writing more optimal implementations.

**Expected outcomes**

In-depth performance for libc functions. Overhead of GPU-to-CPU remote procedure calls. More optimal implementations of 'libc' functions.

**Confirmed mentors and their contacts**

*   Joseph Huber joseph.huber@amd.com
*   Johannes Doerfert jdoerfert@llnl.gov

**Required / desired skills**

Required:

*   Profiling skills and understanding of GPU architecture

Desired:

*   Experience with libc utilities

**Size of the project.**

small

**An easy, medium or hard rating if possible**

easy

**Discourse:** [URL](https://discourse.llvm.org/t/libc-gsoc-2024-performance-and-testing-in-the-gpu-libc/77042)

<!-- *********************************************************************** -->

### Improve GPU First Framework

<!-- *********************************************************************** -->

**Description**

[GPU First](https://arxiv.org/abs/2306.11686) is a methodology and framework that can enable any existing host code to execute the entire program on a GPU without any modification from users. The goal of this project is two folded: 1) Port [host code](https://github.com/shiltian/llvm-project/tree/direct_gpu_compilation) to handle RPC to the new plugin and rewrite it with the host RPC framework introduced in the GPU LibC project. 2) Explore the support for MPI among multiple thread blocks on a single GPU, or even multiple GPUs.

**Expected outcomes**

More efficient GPU First framework that can support both NVIDIA and AMD GPUs. Optionally, upstream the framework.

**Confirmed mentors and their contacts**

*   Shilei Tian i@tianshilei.me
*   Johannes Doerfert jdoerfert@llnl.gov
*   Joseph Huber joseph.huber@amd.com

**Required / desired skills**

Required:

*   Good understanding of C++ and GPU architecture
*   Familiarity with GPUs and LLVM IR

Desired:

*   Good understanding of the LLVM code base and OpenMP target offloading

**Size of the project.**

medium

**An easy, medium or hard rating if possible**

medium

**Discourse:** [URL](https://discourse.llvm.org/t/openmp-gsoc-2024-improve-gpu-first-framework/77048)

<!-- *********************************************************************** -->

### Compile GPU kernels using ClangIR

<!-- *********************************************************************** -->

**Description:** Heterogeneous programming models such as [SYCL](https://sycl.tech), [OpenMP](https://www.openmp.org) and [OpenACC](https://www.openacc.org) help developers to offload computationally intensive kernels to GPUs and other accelerators. [MLIR](https://mlir.llvm.org) is expected to unlock new high-level optimisations and better code generation for the next generation of compilers for heterogeneous programming models. However, the availability of a robust MLIR-emitting C/C++ frontend is a prerequisite for these efforts.

The [ClangIR](https://clangir.org) (CIR) project aims to establish a new intermediate representation (IR) for Clang. Built on top of MLIR, it provides a dialect for C/C++ based languages in Clang, and the necessary infrastructure to emit it from the Clang AST, as well as a lowering path to the LLVM-IR dialect. Over the last year, ClangIR has evolved into a mature incubator project, and a recent [RFC](https://discourse.llvm.org/t/rfc-upstreaming-clangir/76587) on upstreaming it into the LLVM monorepo has seen positive comments and community support.

The overall goal of this GSoC project is to identify and implement missing features in ClangIR to make it possible to compile GPU kernels in the [OpenCL C language](https://registry.khronos.org/OpenCL/specs/3.0-unified/html/OpenCL_C.html) to LLVM-IR for the [SPIR-V](https://registry.khronos.org/SPIR-V) target. The OpenCL to SPIR-V flow is a great environment for this project because a) it is [already supported](https://clang.llvm.org/docs/OpenCLSupport.html) in Clang and b) OpenCL's work-item- and work-group-based programming model still captures modern GPU architectures well. The contributor will extend the AST visitors, the dialect and the LLVM-IR lowering, to add support e.g. for multiple address spaces, vector and custom floating point types, and the `spir_kernel` and `spir_func` calling conventions.

A good starting point for this work is the [Polybench-GPU](https://github.com/sgrauerg/polybenchGpu/tree/master/OpenCL) benchmark suite. It contains self-contained small- to medium sized OpenCL implementations of common algorithms. We expect only the device code (\*.cl files) to be compiled via ClangIR. The existing OpenCL support in Clang can be used to create lit tests with reference LLVM-IR output to guide the development. Optionally, the built-in result verification and time measurements in Polybench could also be used to assess the correctness and quality of the generated code.

**Expected result:** Polybench-GPU's [`2DCONV`](https://github.com/sgrauerg/polybenchGpu/blob/master/OpenCL/2DCONV/2DConvolution.cl), [`GEMM`](https://github.com/sgrauerg/polybenchGpu/blob/master/OpenCL/GEMM/gemm.cl) and [`CORR`](https://github.com/sgrauerg/polybenchGpu/blob/master/OpenCL/CORR/correlation.cl) OpenCL kernels can be compiled with ClangIR to LLVM-IR for SPIR-V.

**Skills:** Intermediate C++ programming skills and familiarity with basic compiler design concepts are required. Prior experience with LLVM IR, MLIR, Clang or GPU programming is a big plus, but willingness to learn is also a possibility.

**Project size:** Large

**Difficulty:** Medium

**Confirmed Mentors:** [Julian Oppermann](https://github.com/jopperm), [Victor Lomüller](https://github.com/Naghasan), [Bruno Cardoso Lopes](https://github.com/bcardosolopes)

**Discourse:** [URL](https://discourse.llvm.org/t/clangir-compile-gpu-kernels-using-clangir/76984)

<!-- *********************************************************************** -->

### Half precision in LLVM libc

<!-- *********************************************************************** -->

**Description:**

Half precision is an IEEE 754 floating point format that has been widely used recently, especially in machine learning and AI. It has been standardized as \_Float16 in the latest C23 standard, bringing its support to the same level as float or double data types. The goal for this project is to implement C23 half precision math functions in the LLVM libc library.

**Expected result:**

*   Setup the generated headers properly so that the type and the functions can be used with various compilers (+versions) and architectures.
*   Implement generic basic math operations supporting half precision data types that work on supported architectures: x86\_64, arm (32 + 64), risc-v (32 + 64), and GPUs.
*   Implement specializations using compiler builtins or special hardware instructions to improve their performance whenever possible.
*   If time permits, we can start investigating higher math functions for half precision.

**Skills:**

Intermediate C++ programming skills and familiarity with basic compiler design concepts are required. Prior experience with LLVM IR, MLIR, Clang or GPU programming is a big plus, but willingness to learn is also a possibility.

**Project size:** Large

**Difficulty:** Easy/Medium

**Confirmed Mentors:** [Tue Ly](mailto:lntue@google.com), [Joseph Huber](mailto:joseph.huber@amd.com),

**Discourse:** [URL](https://discourse.llvm.org/t/libc-gsoc-2024-half-precision-in-llvm-libc/77027)

<!-- *********************************************************************** -->

# Google Summer of Code 2023

<!-- *********************************************************************** -->

Google Summer of Code 2023 was very successful for LLVM project. For the list of accepted and completed projects, please take a look into Google Summer of Code [website](https://summerofcode.withgoogle.com/archive/2023/organizations/llvm-compiler-infrastructure).

<!-- *********************************************************************** -->

## LLVM

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Re-optimization using JITLink

<!-- *********************************************************************** -->

**Description of the project:** In Just-In-Time compilers we often choose a low optimization level to minimize compile time and improve launch times and latencies, however some functions (which we call hot functions) are used very frequently and for these functions it is worth optimizing more heavily. In general hot functions can only be identified at runtime (different inputs will cause different functions to become hot), so the aim of the reoptimization project is to build infrastructure to (1) detect hot functions at runtime and (2) compile them a second time at a higher optimization level, hence the name "re-optimization".  

There are many possible approaches to both parts of this problem. E.g. hot functions could be identified by sampling, or using existing profiling infrastructure, or by implementing custom instrumentation. Reoptimization could be applied to whole functions, or outlining could be used to enable optimization of portions of functions. Re-entry into the JIT infrastructure from JIT’d code might be implemented on top of existing lazy compilation, or via a custom path.  

Whatever design is adopted, the goal is that the infrastructure should be generic so that it can be used by other LLVM API clients, and should support out-of-process JIT-compilation (so some of the solution will be implemented in the ORC runtime).

**Expected result:**

*   Improve ergonomics of indirection – ideally all forms of indirection (for re-optimization, lazy compilation, and procedure-linkage-tables) should be able to share a single stub (and/or binary rewriting metadata) at runtime.
*   Implement basic re-optimization on top of the tidied up indirection.
*   (Stretch goal) Garbage-collect unoptimized code that is no longer needed once the optimized version is available.

**Desirable skills:** Intermediate C++; Understanding of LLVM and the LLVM JIT in particular.

**Project size:** Large.

**Difficulty:** Medium

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev), [Lang Hames](https://github.com/lhames)

**Discourse:** [URL](https://discourse.llvm.org/t/re-optimization-using-jitlink/68260)

<!-- *********************************************************************** -->

### JITLink new backends

<!-- *********************************************************************** -->

**Description of the project:** JITLink is LLVM's new JIT linker API -- the low-level API that transforms compiler output (relocatable object files) into ready-to-execute bytes in memory. To do this JITLink’s generic linker algorithm needs to be specialized to support the target object format (COFF, ELF, MachO), and architecture (arm, arm64, i386, x86-64). LLVM already has mature implementations of JITLink for MachO/arm64, MachO/x86-64, ELF/x86-64, ELF/aarch64 and COFF/x86-64, while the implementations for ELF/riscv, ELF/aarch32 and COFF/i386 are still relatively new.  
You can either work on an entirely new architecture like PowerPC or eBPF, or complete one of the recently added JITLink implementations. In both cases you will likely reuse the existing generic code for one of the target object formats. You will also work on relocation resolution, populate PLTs and GOTs and wire up the ORC runtime for your chosen target.  

**Expected result:** Write a JITLink specialization for a not-yet-supported or incomplete format/architecture such as PowerPC, AArch32 or eBPF.

**Desirable skills:** Intermediate C++; Understanding of LLVM and the LLVM JIT in particular; familiarity with your chosen format/architecture, and basic linker concepts (e.g. sections, symbols, and relocations).

**Project size:** Large.

**Difficulty:** Medium

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev), [Lang Hames](https://github.com/lhames)

[Stefan Gränitz](https://github.com/weliveindetail)

**Discourse:** [URL](https://discourse.llvm.org/t/jitlink-new-backends/68223)

<!-- *********************************************************************** -->

### Improving compile times

<!-- *********************************************************************** -->

**Description of the project:** While the primary job of a compiler is to produce fast code (good run-time performance), it is also important that optimization doesn’t take too much time (good compile-time performance). The goal of this project is to improve compile-time without hurting optimization quality.  
The general approach to this project is:

1.  Pick a workload to optimize. For example, this could be a file from [CTMark](https://github.com/llvm/llvm-test-suite/tree/main/CTMark) compiled in a certain build configuration (e.g. `-O0 -g` or `-O3 -flto=thin`).
2.  Collect profiling information. This could involve compiler options like `-ftime-report` or `-ftime-trace` for a high-level overview, as well as `perf record` or `valgrind --tool=callgrind` for a detailed profile.
3.  Identify places that are unexpectedly slow. This is heavily workload dependent.
4.  Try to optimize an identified hotspot, ideally without impacting generated code. The [compile-time tracker](https://llvm-compile-time-tracker.com/) can be used to quickly evaluate impact on CTMark.

As a disclaimer, it should be noted that outside of pathological cases, compilation doesn’t tend to have a convenient hotspot where 90% of the time is spent, instead it is spread out across many passes. As such, individual improvements also tend to have only small impact on overall compile-time. Expect to do 10 improvements of 0.2% each, rather than one improvement of 2%.

**Expected result:** Substantial improvements on some individual files (multiple percent), and a small improvement on overall geomean compile-time.

**Desirable skills:** Intermediate C++. Familiarity with profiling tools (especially if you are not on Linux, in which case I won’t be able to help).

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentor:** [Nikita Popov](https://github.com/nikic)

**Discourse:** [URL](https://discourse.llvm.org/t/llvm-improving-compile-times/68094)

<!-- *********************************************************************** -->

### Addressing Rust optimization failures

<!-- *********************************************************************** -->

**Description of the project:** The [Rust programming language](https://www.rust-lang.org/) uses LLVM for code generation, and heavily relies on LLVM’s optimization capabilities. However, there are many cases where LLVM fails to optimize typical code patterns that are emitted by rustc. Such issues are reported using the [I-slow](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AI-slow) and/or [A-LLVM](https://github.com/rust-lang/rust/issues?q=is%3Aopen+is%3Aissue+label%3AA-LLVM) labels.  
The usual approach to fixing these issues is:

1.  Inspect the `--emit=llvm-ir` output on [Godbolt](https://rust.godbolt.org/).
2.  Create an LLVM IR test case that is not optimized when run through `opt -O3`.
3.  Identify a minimal missing transform and prove its correctness using [alive2](https://alive2.llvm.org/ce/).
4.  Identify which LLVM pass or passes could perform the transform.
5.  Add necessary test coverage and implement the transform.
6.  (Much later: Check that the issue is really resolved after the next major LLVM version upgrade in Rust.)

The goal of this project is to address some of the less hard optimization failures. This means that in some cases, the process would stop after step 3 or 4 without proceeding to implementation, because it’s unclear how the issue could be addressed, or it would take a large amount of effort. Having an analysis of the problem is still valuable in that case.

**Expected result:** Fixes for a number of easy to medium Rust optimization failures. Preliminary analysis for some failures even if no fix was implemented.

**Desirable skills:** Intermediate C++ for implementation. Some familiarity with LLVM (at least ability to understand LLVM IR) for analysis. Basic Rust knowledge (enough to read, but not write Rust).

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentor:** [Nikita Popov](https://github.com/nikic)

**Discourse:** [URL](https://discourse.llvm.org/t/llvm-addressing-rust-optimization-failures-in-llvm/68096)

<!-- *********************************************************************** -->

### Implement autocompletion in clang-repl

<!-- *********************************************************************** -->

**Description of the project:** The Clang compiler is part of the LLVM compiler infrastructure and supports various languages such as C, C++, ObjC and ObjC++. The design of LLVM and Clang enables them to be used as libraries, and has led to the creation of an entire compiler-assisted ecosystem of tools. The relatively friendly codebase of Clang and advancements in the JIT infrastructure in LLVM further enable research into different methods for processing C++ by blurring the boundary between compile time and runtime. Challenges include incremental compilation and fitting compile/link time optimizations into a more dynamic environment.  

Incremental compilation pipelines process code chunk-by-chunk by building an ever-growing translation unit. Code is then lowered into the LLVM IR and subsequently run by the LLVM JIT. Such a pipeline allows creation of efficient interpreters. The interpreter enables interactive exploration and makes the C++ language more user friendly. The incremental compilation mode is used by the interactive C++ interpreter, Cling, initially developed to enable interactive high-energy physics analysis in a C++ environment.  

[Our group](https://compiler-research.org/) puts efforts to incorporate and possibly redesign parts of Cling in Clang mainline through a new tool, clang-repl. The project aims at the design and implementation of robust autocompletion when users type C++ at the prompt of clang-repl. For example:

```
[clang-repl] class MyLongClassName {};
      [clang-repl] My&lt;tab&gt;
      // list of suggestions.
```

**Expected result:** There are several foreseen tasks:

*   Research the current approaches for autocompletion in clang such as clang -code-completion-at=file:col1:col2.
*   Implement a version of the autocompletion support using the partial translation unit infrastructure in clang’s libInterpreter.
*   Investigate the requirements for semantic autocompletion which takes into account the exact grammar position and semantics of the code. Eg:

    ```
    [clang-repl] struct S {S* operator+(S&) { return nullptr;}};
              [clang-repl] S a, b;
              [clang-repl] v = a + &lt;tab&gt; // shows b as the only acceptable choice here.
    ```

*   Present the work at the relevant meetings and conferences.

**Project size:** Large.

**Difficulty:** Medium

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev)

**Discourse:** [URL](https://discourse.llvm.org/t/clang-repl-implement-autocompletion-in-clang-repl/60364)

<!-- *********************************************************************** -->

### Modules build daemon: build system agnostic support for explicitly built modules

<!-- *********************************************************************** -->

**Description of the project:** Clang currently handles modules independently in each `clang` instance using the filesystem for synchronization of which instance builds a given module. This has many issues with soundness and performance due to tradeoffs made for module reuse and filesystem contention.

Clang has another way of building modules, explicitly built modules, that currently requires build system changes to adopt. Here the build system determines which modules are needed, for example by using [clang-scan-deps](https://github.com/llvm/llvm-project/tree/main/clang/tools/clang-scan-deps), and ensures those modules are built before running the `clang` compile task that needs them.

In order to allow adoption of this new way of building modules without major build system work we need a module build daemon. With a small change to the command line, clang will connect to this daemon and ask for the modules it needs. The module build daemon then either returns an existing valid module, or builds and then returns it.

There is an existing open source dependency scanning daemon that is in a llvm-project fork. This only handles file dependencies, but has an IPC mechanism. This IPC system could be used as a base for the modules build daemon, but does need to be extended to work on Windows.

**Expected result:** A normal project using Clang modules with an existing build system (like Make or CMake) can be built using only explicitly built modules via a modules build daemon.

**Desirable skills:** Intermediate C++ programming skills; familiarity with compilers; familiarity with Clang is an asset, but not required.

**Project size:** 175h or 350h depending on reuse of IPC

**Difficulty:** medium

**Confirmed Mentors:** [Michael Spencer](https://github.com/Bigcheese), [Jan Svoboda](https://github.com/jansvoboda11)

**Discourse:** [URL](https://discourse.llvm.org/t/clang-modules-build-daemon-build-system-agnostic-support-for-explicitly-built-modules/68224)

<!-- *********************************************************************** -->

### ExtractAPI Objective-C categories

<!-- *********************************************************************** -->

**Description of the project:** [Swift-DocC](https://github.com/apple/swift-docc) is the canonical documentation compiler for the Swift OSS project. However Swift-DocC is not Swift specific and uses [SymbolKit](https://github.com/apple/swift-docc-symbolkit/blob/main/openapi.yaml)'s languaguage agnostic JSON-based symbol graph format to understand which symbols are available in the code, this way any language can be supported by Swift-DocC as long as there is a symbol graph generator.

Clang supports symbol graph generation for C and Objective-C as described in [\[RFC\] clang support for API information generation in JSON](https://discourse.llvm.org/t/rfc-clang-support-for-api-information-generation-in-json/58845). Today, support for Objective-C categories is not complete, on one hand if the category extends a type in the current module, the category members are assumed to belong to the extended type itself. On the other hand, if the extended type belongs to another module the category is ignored. Nonetheless, it is common to extend types belonging to other modules in Objective-C as part of the public API of the module. The goal of this project is to extend the symbol graph format to accommodate Objective-C categories and to implement support for generating this information both through clang and through libclang.

**Expected result:** Adding the necessary support to clang's symbol graph generator and in libclang for describing categories of symbols defined in other modules. This might involve additions to SymbolKit that would need to be discussed with that community.

**Desirable skills:** Intermediate C++ programming skills; familiarity with clang and Objective-C are assets but not required.

**Project size:** Medium

**Difficulty:** Medium

**Confirmed Mentors:** [Daniel Grumberg](https://github.com/daniel-grumberg), [Zixu Wang](https://github.com/zixu-w), [Juergen Ributzka](https://github.com/ributzka)

**Discourse:** [URL](https://discourse.llvm.org/t/clang-extractapi-objective-c-categories/68370)

<!-- *********************************************************************** -->

### ExtractAPI C++ Support

<!-- *********************************************************************** -->

**Description of the project:** [Swift-DocC](https://github.com/apple/swift-docc) is the canonical documentation compiler for the Swift OSS project. However Swift-DocC is not Swift specific and uses [SymbolKit](https://github.com/apple/swift-docc-symbolkit/blob/main/openapi.yaml)'s languaguage agnostic JSON-based symbol graph format to understand which symbols are available in the code, this way any language can be supported by Swift-DocC as long as there is a symbol graph generator.

Clang supports symbol graph generation for C and Objective-C as described in [\[RFC\] clang support for API information generation in JSON](https://discourse.llvm.org/t/rfc-clang-support-for-api-information-generation-in-json/58845).

Currently the emitted symbol graph format does not support various C++ constructs such as templates and exceptions and the symbol graph generator does not fully understand C++. This project aims to introduce support for various C++ constructs in the symbol graph format and to implement support for generating this data in clang.

**Expected result:** Adding the necessary support to clang's symbol graph generator and in libclang for describing categories of symbols defined in other modules. This will involve additions to SymbolKit that would need to be discussed with that community.

**Desirable skills:** Intermediate C++ programming skills; familiarity with clang and Objective-C are assets but not required.

**Project size:** Large

**Difficulty:** Medium/Hard

**Confirmed Mentors:** [Daniel Grumberg](https://github.com/daniel-grumberg), [Zixu Wang](https://github.com/zixu-w), [Juergen Ributzka](https://github.com/ributzka)

**Discourse:** [URL](https://discourse.llvm.org/t/extractapi-c-support/68371)

<!-- *********************************************************************** -->

### ExtractAPI while building

<!-- *********************************************************************** -->

**Description of the project:** [Swift-DocC](https://github.com/apple/swift-docc) is the canonical documentation compiler for the Swift OSS project. However Swift-DocC is not Swift specific and uses [SymbolKit](https://github.com/apple/swift-docc-symbolkit/blob/main/openapi.yaml)'s languaguage agnostic JSON-based symbol graph format to understand which symbols are available in the code, this way any language can be supported by Swift-DocC as long as there is a symbol graph generator.

Clang supports symbol graph generation for C and Objective-C as described in [\[RFC\] clang support for API information generation in JSON](https://discourse.llvm.org/t/rfc-clang-support-for-api-information-generation-in-json/58845).

Currently users can use clang to generate symbol graph files using the `clang -extract-api` command line interface or generating symbol graphs for a specific symbol using the libclang interface. This project would entail adding a third mode that would generate the symbol graph output as a side-effect of a regular compilation job. This can enable using the symbol graph format as a light weight alternative to clang Index or clangd for code intelligence services.

**Expected result:** Enable generating symbol graph files during a regular compilation (or module build); provide a tool to merge symbol graph files in the same way a static linker links individual object files; Extend clang Index to support all the information contained by symbol graph files.

**Desirable skills:** Intermediate C++ programming skills; familiarity with clang and Objective-C are assets but not required.

**Project size:** Medium

**Difficulty:** Medium/Hard

**Confirmed Mentors:** [Daniel Grumberg](https://github.com/daniel-grumberg), [Zixu Wang](https://github.com/zixu-w), [Juergen Ributzka](https://github.com/ributzka)

**Discourse:** [URL](https://discourse.llvm.org/t/clang-extractapi-while-building/68372)

<!-- *********************************************************************** -->

### Improve Clang diagnostics

<!-- *********************************************************************** -->

**Description:** The diagnostics clang emits are ultimately its interface to the developer. While the diagnostics are generally good, there are some rough edges that need to be ironed out. Some cases can be improved by special-casing them in the compiler as well.

As one can see from Clang’s issue tracker, there are [lots of issues](https://github.com/llvm/llvm-project/issues?page=2&q=is%3Aopen+is%3Aissue+label%3Aclang%3Adiagnostics) open against clang’s diagnostics.

This project does not aim to implement one big feature but instead focuses on smaller, incremental improvements to Clang’s diagnostics.

Possible example issues to resolve:

*   [Calling nullptr function pointer in a constexpr function results in poor diagnostic](https://github.com/llvm/llvm-project/issues/59872)
*   [Print name of uninitialized subobject (instead of type)](https://github.com/llvm/llvm-project/issues/58601)
*   [https://github.com/llvm/llvm-project/issues/57906](https://github.com/llvm/llvm-project/issues/57906)
*   [clang(++) unhelpful frame-larger-than warning, very small stack frame exceeding very large limit](https://github.com/llvm/llvm-project/issues/57337)
*   Any other diagnostics issue you find interesting or ran into personally.

**Expected outcomes**: At least three fixed smaller diagnostics issues, or one larger implemented diagnostics improvement.

**Confirmed Mentor:**[Timm Bäder](https://github.com/tbaederr)

**Desirable skills:**

*   Intermediate C++ knowledge.
*   Preferably experience in the Clang code base, since the issues mentioned can have their root cause in various parts of it.
*   Preferably an already working local LLVM build

**Project type:** Medium/200 hr

**Discourse** [URL](https://discourse.llvm.org/t/improve-clang-diagnostics-2/68900/3)

<!-- *********************************************************************** -->

### Tutorial development with clang-repl

<!-- *********************************************************************** -->

**Description:** The Clang compiler is part of the LLVM compiler infrastructure and supports various languages such as C, C++, ObjC and ObjC++. The design of LLVM and Clang enables them to be used as libraries, and has led to the creation of an entire compiler-assisted ecosystem of tools. The relatively friendly codebase of Clang and advancements in the JIT infrastructure in LLVM further enable research into different methods for processing C++ by blurring the boundary between compile time and runtime. Challenges include incremental compilation and fitting compile/link time optimizations into a more dynamic environment.

Incremental compilation pipelines process code chunk-by-chunk by building an ever-growing translation unit. Code is then lowered into the LLVM IR and subsequently run by the LLVM JIT. Such a pipeline allows creation of efficient interpreters. The interpreter enables interactive exploration and makes the C++ language more user friendly. The incremental compilation mode is used by the interactive C++ interpreter, Cling, initially developed to enable interactive high-energy physics analysis in a C++ environment.

We invest efforts to incorporate and possibly redesign parts of Cling in Clang mainline through a new tool, clang-repl. The project aims implementing tutorials demonstrating the capabilities of the project and investigating adoption of clang-repl in xeus-clang-repl prototype allowing to write C++ in Jupyter.

**Expected result:** There are several foreseen tasks:

*   Write several tutorials demostrating the current capabilities of clang-repl.
*   Investigate the requirements for adding clang-repl as a backend to xeus-cling.
*   Improve the xeus kernel protocol for clang-repl.
*   Prepare a blog post about clang-repl and possibly Jupyter. Present the work at the relevant meetings and conferences.

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev) [David Lange](https://github.com/davidlange6)

**Desirable skills:** Intermediate C++; Understanding of Clang and the Clang API in particular

**Project type:** Medium

**Discourse** [URL](https://discourse.llvm.org/t/clang-repl-tutorial-development-with-clang-repl/60365)

<!-- *********************************************************************** -->

### Add WebAssembly Support in clang-repl

<!-- *********************************************************************** -->

**Description:** The Clang compiler is part of the LLVM compiler infrastructure and supports various languages such as C, C++, ObjC and ObjC++. The design of LLVM and Clang enables them to be used as libraries, and has led to the creation of an entire compiler-assisted ecosystem of tools. The relatively friendly codebase of Clang and advancements in the JIT infrastructure in LLVM further enable research into different methods for processing C++ by blurring the boundary between compile time and runtime. Challenges include incremental compilation and fitting compile/link time optimizations into a more dynamic environment.

Incremental compilation pipelines process code chunk-by-chunk by building an ever-growing translation unit. Code is then lowered into the LLVM IR and subsequently run by the LLVM JIT. Such a pipeline allows creation of efficient interpreters. The interpreter enables interactive exploration and makes the C++ language more user friendly. The incremental compilation mode is used by the interactive C++ in Jupyter via the xeus kernel protocol. Newer versions of the protocol allow possible in-browser execution allowing further possibilities for clang-repl and Jupyter.

We invest efforts to incorporate and possibly redesign parts of Cling in Clang mainline through a new tool, clang-repl. The project aims to add WebAssembly support in clang-repl and adopt it in xeus-clang-repl to aid Jupyter-based C++.

**Expected result:** There are several foreseen tasks:

*   Investigate feasibility of generating WebAssembly in a similar way to the new [interactive CUDA support](https://reviews.llvm.org/D146389).
*   Enable generating WebAssembly in clang-repl.
*   Adopt the feature in xeus-clang-repl.
*   Prepare a blog post about clang-repl and possibly Jupyter. Present the work at the relevant meetings and conferences.

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev) [Alexander Penev](https://github.com/alexander-penev)

**Desirable skills:** Good C++; Understanding of Clang and the Clang API and the LLVM JIT in particular

**Project type:** Large

**Discourse** [URL](https://discourse.llvm.org/t/clang-repl-add-webassembly-support-in-clang-repl/69419)

<!-- *********************************************************************** -->

### LLD Linker Improvements for Embedded Targets

<!-- *********************************************************************** -->

**Description of the project** GNU toolchain is used widely for building embedded targets. There's a certain momentum in the Clang/LLVM community towards improving the Clang toolchain to support embedded targets. Using the Clang toolchain as an alternative can help us improve code quality, find and fix security bugs, improve developer experience and take advantage of the new ideas and the momentum surrounding the Clang/LLVM community in supporting embedded devices.

**A non-comprehensive list of improvements that can be made to LLD**:

*   **\--print-memory-usage support**

    "--print-memory-usage" in GCC provides a breakdown of the memory used in each memory region defined in the linker file. Embedded developers use this flag to understand the impact on memory. Often embedded systems define multiple memory regions with different space constraints. Supporting this in Clang toolchain will help projects that wish to use Clang toolchain for their projects.

*   **Linkmap**

    Currently, the LLD linker's linkmap output is not as rich as the BFD linker output. Achieving feature parity on linkmap output will be highly useful in analyzing the binaries created by the LLD linker. Further, outputting linkmap in different formats (current LLD output, BFD, and JSON) can help build automation tools for investigating the artifacts produced by the linker.

*   **\--print-gc-sections improvement**

    When the "--print-gc-sections" flag is enabled, LLD prints the sections that were discarded during the linking process. This information currently does not include the mapping between the symbol and the section groups, which is useful for debugging. Preserving this information during the linking process will require modifications to internal linker data structures.

**Project size:** Medium or Large

**Difficulty:** Medium/Hard

**Skills:** C++

**Expected result**:

*   Implementation of "--print-memory-usage" flag.
*   Support for new linkmap output formats 1. BFD and 2. JSON.
*   Improved "--print-gc-sections" output to include information about the surviving symbols.

**Confirmed Mentors:** [Prabhu Rajasekaran](https://github.com/Prabhuk) [Petr Hosek](https://github.com/petrhosek)

**Discourse:** [URL](https://discourse.llvm.org/t/lld-linker-improvements-for-embedded/68129)

<!-- *********************************************************************** -->

### Optimizing MLIR’s Presburger library

<!-- *********************************************************************** -->

**Description**: MLIR’s Presburger Library, FPL ([https://grosser.science/FPL](https://grosser.science/FPL)), provides mathematical abstractions for polyhedral compilation and analysis. The main abstraction that the library provides is a set of integer tuples defined by a system of affine inequality constraints. The library supports standard set operations over such sets. The result will be a set defined by another constraint system, possibly having more constraints. When many set operations are performed in sequence, the constraint system may become very large, negatively impacting performance. There are several potential ways to simplify the constraint system; however, this involves performing additional computations. Thus, spending more time on more aggressive simplifications may make each individual operation slower, but at the same time, insufficient simplifications can make sequences of operations slow due to an explosion in constraint system size. The aim of this project is to find the right balance between the two.

**The goals of this project:**

*   Understand the library's performance in terms of runtime and output size.
*   Optimize the library by finding the best output size and performance tradeoff.

**Expected outcomes**:

*   Benchmarking the performance and output constraint complexity of the primary operations of the library.
*   Implementing simplification heuristics.
*   A better understanding of which simplification heuristics improve overall performance enough to be worth the additional computational cost.

**Desirable skills**: Intermediate C++, Experience in benchmarking

**Project size**: Large

**Difficulty**: Medium

**Confirmed mentors**: [Kunwar Grover](https://github.com/Groverkss)

**Discourse**: [URL](https://discourse.llvm.org/t/mlir-optimizing-mlir-s-presburger-library/68213/1)

<!-- *********************************************************************** -->

### Interactively query MLIR IR

<!-- *********************************************************************** -->

**Description**: The project aims to develop an interactive query language for MLIR that enables developers to query the MLIR IR dynamically. The tool will provide a REPL (or command-line) interface to enable users to query various properties of MLIR code, such as "isConstant" and "resultOf". The proposed tool is intended to be similar to clang-query, which allows developers to match AST expressions in C++ code using a TUI with autocomplete and other features.

**The goals of this project:**

*   Understand the MLIR IR representation and common explorations user do.
*   Implement a REPL to execute queries over MLIR IR.

**Expected outcomes**:

*   Standalone that can be used to interactively explore IR.
*   Implement common matchers that are usable by the tool.
*   (stretch) Enable extracting parts of the IR matched by query into self-contained IR snippets.

**Desirable skills**: Intermediate C++, Experience in writing/debugging peephole optimizations

**Project size**: Either medium or large.

**Difficulty**: Medium

**Confirmed mentors**: [Jacques Pienaar](https://github.com/jpienaar)

**Discourse**: [URL](https://discourse.llvm.org/t/gsoc-proposal-interactive-mlir-query-tool-to-make-exploring-the-ir-easier/69601)

<!-- *********************************************************************** -->

### Better performance models for MLGO training

<!-- *********************************************************************** -->

**Description of the project** We are using machine-guided compiler optimizations ("MLGO") for register allocation eviction and inlining for size, in real-life deployments. The ML models have been trained with reinforcement learning algorithms. Expanding to more performance areas is currently impeded by the poor prediction quality of our performance estimation models. Improving those is critical to the effectiveness of reinforcement learning training algorithms, and therefore to enabling applying MLGO systematically to more optimizations.

**Project size:** either 175 or 350 hr.

**Difficulty:** Medium

**Skills:** C/C++, some compiler experience, some Python. ML experience is a bonus.

**Expected outcomes**: Better modeling of the execution environment by including additional runtime/profiling information, such as additional PMU data, LLC miss probabilities or branch mispredictions. This involves (1) building a data collection pipeline that covers additional runtime information, (2) modifying the ML models to allow processing this data, and (3) modifying the training and inference process for the models to make use this data.

Today, the models are almost pure static analysis; they see the instructions, but they make one-size-fits-all assumptions about the execution environment and the runtime behavior of the code. The goal of this project is to move from static analysis towards more dynamic models that better represent code the way it actually executes.

**Mentors** Ondrej Sykora, Mircea Trofin, Aiden Grossman

**Discourse** [URL](https://discourse.llvm.org/t/better-performance-models-for-mlgo-training/68219)

<!-- *********************************************************************** -->

### Improve and Stabilize the Clang Static Analyzer's "Taint Analysis" Checks

<!-- *********************************************************************** -->

**Description of the project:** The Clang static analyzer comes with an experimental implementation of taint analysis, a security-oriented analysis technique built to warn the user about flow of attacker-controlled ("tainted") data into sensitive functions that may behave in unexpected and dangerous ways if the attacker is able to forge the right input. The programmer can address such warnings by properly "sanitizing" the tainted data in order to eliminate these dangerous inputs. A common example of a problem that can be caught this way is [SQL injections](https://xkcd.com/327/). A much simpler example, which is arguably much more relevant to users of Clang, is buffer overflow vulnerabilities caused by attacker-controlled numbers used as loop bounds while iterating over stack or heap arrays, or passed as arguments to low-level buffer manipulating functions such as memcpy().

Being a static symbolic execution engine, the static analyzer implements taint analysis by simply maintaining a list of "symbols" (named unknown numeric values) that were obtained from known taint sources during the symbolic simulation. Such symbols are then treated as potentially taking arbitrary concrete values, as opposed to the general case of taking an unknown subset of possible values. For example, division by a unchecked unknown value doesn't necessarily warrant a division by zero warning, because it's typically not known whether the value can be zero or not. However, division by an unchecked *tainted* value does immediately warrant a division by zero warning, because the attacker is free to pass zero as an input. Therefore the static analyzer's taint infrastructure consists of several parts: there is a mechanism for keeping track of tainted symbols in the symbolic program state, there is a way to define new sources of taint, and a few path-sensitive checks were taught to consume taint information to emit additional warnings (like the division by zero checker), acting as taint "sinks" and defining checker-specific "sanitization" conditions.

The entire facility is flagged as experimental: it's basically a proof-of-concept implementation. It's likely that it can be made to work really well, but it needs to go through some quality control by running it on real-world source code, and a number of bugs need to be addressed, especially in individual checks, before we can declare it stable. Additionally, the tastiest check of them all – buffer overflow detection based on tainted loop bounds or size parameters – was never implemented. There is also a related check for array access with tainted index – which is, again, experimental; let's see if we can declare this one stable as well!

**Expected result:** A number of taint-related checks either enabled by default for all users of the static analyzer, or available as opt-in for users who care about security. They're confirmed to have low false positive rate on real-world code. Hopefully, the buffer overflow check is one of them.

**Desirable skills:** Intermediate C++ to be able to understand LLVM code. We'll run our analysis on some plain C code as well. Some background in compilers or security is welcome but not strictly necessary.

**Project size:** Either medium or large.

**Difficulty:** Medium

**Confirmed Mentors:** [Artem Dergachev](https://github.com/haoNoQ), [Gábor Horváth](https://github.com/xazax-hun), [Ziqing Luo](https://github.com/ziqingluo-90)

**Discourse:** [URL](https://discourse.llvm.org/t/clang-improve-and-stabilize-the-static-analyzers-taint-analysis-checks/68235)

<!-- *********************************************************************** -->

### Machine Learning Guided Ordering of Compiler Optimization Passes

<!-- *********************************************************************** -->

**Description of the project** This continues the work of GSoC 2020 and [2021](https://summerofcode.withgoogle.com/archive/2021/projects/6411038932598784). Developers generally use standard optimization pipelines like -O2 and -O3 to optimize their code. Manually crafted heuristics are used to determine which optimization passes to select and how to order the execution of those passes. However, this process is not tailored for a particular program, or kind of program, as it is designed to perform “reasonably well” for any input. We want to improve the existing heuristics or replace the heuristics with machine learning-based models so that the LLVM compiler can provide a superior order of the passes customized per program. The last milestone enabled feature extraction, and started investigating training a policy for selecting a more appropriate pass pipeline.

**Project size:** either 175 or 350 hr.

**Difficulty:** Medium

**Skills:** C/C++, some compiler experience. ML experience is a bonus.

**Expected outcomes**: Pre-trained model selecting the most economical optimization pipeline, with no loss in performance; hook-up of model in LLVM; (re-)training tool; come up with new optimization sequences through search or learning.

**Mentors** Tarindu Jayatilaka, Mircea Trofin, Johannes Doerfert

**Discourse** [URL](https://discourse.llvm.org/t/machine-learning-guided-ordering-of-compiler-optimization-passes/60415)

<!-- *********************************************************************** -->

### Support a hierarchical directory structure in generated coverage html reports

<!-- *********************************************************************** -->

**Description of the project:**  
Clang supports source-based coverage that shows which lines of code are covered by the executed tests [\[1\]](https://clang.llvm.org/docs/SourceBasedCodeCoverage.html). It uses llvm-profdata [\[2\]](https://llvm.org/docs/CommandGuide/llvm-profdata.html) and llvm-cov [\[3\]](https://llvm.org/docs/CommandGuide/llvm-cov.html) tools to generate coverage reports. llvm-cov currently generates a single top-level index HTML file. For example, a single top-level directory code coverage report [\[4\]](https://lab.llvm.org/coverage/coverage-reports/index.html) for LLVM repo is published on a coverage bot. Top-level indexing causes rendering scalability issues in large projects, such as Fuchsia [\[5\]](https://fuchsia.dev). The goal of this project is to generate a hierarchical directory structure in generated coverage html reports to match the directory structure and solve scalability issues. Chromium uses its own post-processing tools to show a per-directory hierarchical structure for coverage results [\[6\]](https://analysis.chromium.org/coverage/p/chromium). Similarly, Lcov, which is a graphical front-end Gcov[\[7\]](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html), provides a one-level directory structure to display coverage results [\[8\]](https://llvm.org/reports/coverage/index.html).  
\[1\] [Source-based code coverage](https://clang.llvm.org/docs/SourceBasedCodeCoverage.html)  
\[2\] [llvm-profdata](https://llvm.org/docs/CommandGuide/llvm-profdata.html)  
\[3\] [llvm-cov](https://llvm.org/docs/CommandGuide/llvm-cov.html)  
\[4\] [LLVM coverage reports](https://lab.llvm.org/coverage/coverage-reports/index.html)  
\[5\] [Fuchsia](https://fuchsia.dev)  
\[6\] [Coverage summary for Chromium](https://analysis.chromium.org/coverage/p/chromium)  
\[7\] [Gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html)  
\[8\] [Lcov coverage reports](https://llvm.org/reports/coverage/index.html)  
\[9\] [Issue #54711: Support per-directory index files for HTML coverage report](https://github.com/llvm/llvm-project/issues/54711)

**Expected result:** Implement a support in hierarchical directory structure in generated coverage html reports and show the usage of this feature in LLVM repo code coverage reports.

**Project size:** Medium or Large

**Difficulty:** Medium

**Confirmed Mentors:** [Gulfem Savrun Yeniceri](https://github.com/gulfemsavrun) [Petr Hosek](https://github.com/petrhosek)

**Discourse:** [URL](https://discourse.llvm.org/t/coverage-support-a-hierarchical-directory-structure-in-generated-coverage-html-reports/68239)

<!-- *********************************************************************** -->

### Map LLVM values to corresponding source-level expressions

<!-- *********************************************************************** -->

**Description of the project** Developers often use compiler generated remarks and analysis reports to optimize their code. While compilers in general are good at including source code positions (i.e line and column numbers) in the generated messages, it is useful if these generated messages also include the corresponding source-level expressions. The approach used by the LLVM implementation is to use a small set of intrinsic functions to define a mapping between LLVM program objects and the source-level expressions. The goal of this project is to use the information included within these intrinsic functions to either generate the source expression corresponding to LLVM values or to propose and implement solutions to get the same if the existing information is insufficient. Optimizing memory accesses in a program is important for application performance. We specifically intend to use compiler analysis messages that report source-level memory accesses corresponding to the LLVM load/store instructions that inhibit compiler optimizations. As an example, we can use this information to report memory access dependences that inhibit vectorization.

**Project size:** Medium

**Difficulty:** Medium

**Skills:** Intermediate C++, familiarity with LLVM core or willingness to learn the same.

**Expected result:** Provide an interface which takes an LLVM value and returns a string corresponding to the equivalent source-level expression. We are especially interested in using this interface to map addresses used in load/store instructions to equivalent source-level memory references.

**Confirmed Mentors:** Satish Guggilla (satish.guggilla@intel.com) Karthik Senthil (karthik.senthil@intel.com)

**Discourse:** [URL](https://discourse.llvm.org/t/map-llvm-values-to-corresponding-source-level-expressions/68450)

<!-- *********************************************************************** -->

### Build and run SingleSource benchmarks using ClangIR

<!-- *********************************************************************** -->

**Description of the project:**  
Clang codegen works by emitting LLVM IR using AST visitors. In the [ClangIR](https://llvm.github.io/clangir/) project, we emit ClangIR (CIR) from AST visitors too (CIRGen), and then lower to (a) LLVM IR directly or, alternatively, (b) MLIR in-tree dialects. Lowering to LLVM is still quite immature and lacks many instructions, attributes and metadata support. ClangIR would greatly benefit from some level of parity with Clang AST → LLVM IR codegen quality, in both performance and build time. This is key for incrementally bridging correctness and performance testing, providing a baseline for future higher level optimizations on top of C/C++. A good starting point is to build and run simple benchmarks, measuring both generated code and build time performance. LLVM's llvm-test-suite contains scripts and machinery that easily allows checking correctness and collecting perf related data and its [SingleSource](https://github.com/llvm/llvm-test-suite/tree/main/SingleSource) collection provide a set of simpler programs to build. In a nutshell, while working on this project the student will brigde the gap of CIR → LLVM lowering, and at times fix any lacking Clang AST → CIR support. The work is going to be done incrementally on top of SingleSource benchmarks, while measuring compiler build time and the performance of compiled programs.

**Skills:** Intermediate C++ programming skills; familiarity with compilers, LLVM IR, MLIR or Clang are a big plus, but willingness to learn is also a possibility.

**Expected result:** Build and run programs from the SingleSource subdirectory from the lvm-test-suite, collect and present results (perf and build time) against regular (upstream) clang codegen.

**Project size:** Large

**Difficulty:** Medium

**Confirmed Mentors:** [Bruno Cardoso Lopes](https://github.com/bcardosolopes) [Nathan Lanza](https://github.com/lanza)

**Discourse:** [URL](https://discourse.llvm.org/t/clangir-build-and-run-singlesource-benchmarks-using-clangir/68473)

<!-- *********************************************************************** -->

### Move additional Enzyme Rules to Tablegen

<!-- *********************************************************************** -->

**Description of the project:** Enzyme performs automatic differentiation (in the calculus sense) of LLVM programs. This enables users to use Enzyme to perform various algorithms such as back-propagation in ML or scientific simulation on existing code for any language that lowers to LLVM. The support for an increasing number of LLVM Versions (7-main), AD modes (Reverse, Forward, Forward-Vector, Reverse-Vector, Jacobian), and libraries (BLAS, OpenMP, MPI, CUDA, ROCm, ...) leads to a steadily increasing code base. In order to limit complexity and help new contributors we would like to express more parts of our core logic using LLVM Tablegen. The applicant is free to decide how to best map the program transformation abstractions within Enzyme to Tablegen.

**Expected results:** 1. Extend the tablegen rule generation system within Enzyme to cover a new component beside of the AdjointGenerator  
2\. Moving several existing rules to the new autogenerated system (e.g. LLVM instructions, LLVM intrinsics, MPI calls, ...  

**Confirmed mentor:** [Manuel Drehwald](https://github.com/zuseZ4) [William Moses](mailto:wmoses@mit.edu)

**Desirable skills:** Good knowledge of C++, calculus, and LLVM and/or Clang, and/or MLIR internals. Experience with Tablegen, Enzyme or automatic differentiation would be nice, but can also be learned in the project.

**Project size:** Large

**Difficulty:** Medium

**Discourse** [URL](https://discourse.llvm.org/t/enzyme-move-additional-enzyme-rules-to-tablegen/69738)

<!-- *********************************************************************** -->

### Patch based test coverage for quick test feedback

<!-- *********************************************************************** -->

**Description of the project** Most of the day to day tests in LLVM are regression tests executed by [Lit](https://llvm.org/docs/CommandGuide/lit.html), structured as source code or IR to be passed to some binary, rather than test code directly calling the code to be tested. This has many advantages but can make it difficult to predict which code path is executed when the compiler is invoked with a certain test input, especially for edge cases where error handling is involved. The goal of this project is to help developers create good test coverage for their patch and enable reviewers to verify that they have done so. To accomplish this we would like to introduce a tool that can be fed a patch as input, add coverage instrumentation for the affected source files, runs Lit tests, and records which test cases cause each counter to be executed. For each counter we can then report the number of test cases executing the counter, but perhaps more importantly we can also report the number of test cases executing the counter that are also changed in some way by the patch, since a modified line that results in the same test results isn’t properly tested, unless it’s intended to be a non-functional change. This can be implemented in three separate parts:

1.  Adding an option to llvm-lit to emit the necessary test coverage data, divided per test case (involves setting a unique value to [`LLVM_PROFILE_FILE`](https://clang.llvm.org/docs/SourceBasedCodeCoverage.html#running-the-instrumented-program) for each RUN)
2.  New tool to process the generated coverage data and the relevant git patch, and present the results in a user friendly manner
3.  Adding a way to non-intrusively (without changing build configurations) enable coverage instrumentation to a build. By building the project normally, touching the files changed by the patch, and rebuilding with [`CCC_OVERRIDE_OPTIONS`](https://github.com/llvm/llvm-project/blob/93a1fc2e18b452216be70f534da42f7702adbe1d/clang/tools/driver/driver.cpp#L79-L105) set to [add coverage](https://clang.llvm.org/docs/SourceBasedCodeCoverage.html#compiling-with-coverage-enabled) we can lower the overhead of generating and processing coverage of lines not relevant to the patch.

The tooling in step 2 and 3 can be made completely agnostic of the actual test-runner, lowering the threshold for other test harnesses than Lit to implement the same functionality. If time permits adding this as a step in CI would also be helpful for reviewers.

**Project size:** Small or medium

**Difficulty:** Simple

**Skills:** Python for Lit, data processing and [diff](https://www.gnu.org/software/diffutils/manual/html_node/Unified-Format.html) processing. No compiler experience necessary.

**Expected result:** Implement a new tool for use by the community. Developers get help finding uncovered edge cases during development, while also avoiding paranoid sprinkling of asserts or logs just to check that the code is actually executed. Reviewers can more easily check which parts of the patch are tested by each test.

**Confirmed Mentors:** [Henrik Olsson](https://github.com/hnrklssn)

**Discourse:** [URL](https://discourse.llvm.org/t/coverage-patch-based-test-coverage-for-quick-test-feedback/68628)

<!-- *********************************************************************** -->

# Google Summer of Code 2022

<!-- *********************************************************************** -->

Google Summer of Code 2022 was very successful for LLVM project. For the list of accepted and completed projects, please take a look into Google Summer of Code [website](https://summerofcode.withgoogle.com/archive/2022/organizations/llvm-compiler-infrastructure).

<!-- *********************************************************************** -->

## LLVM

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Implement a shared-memory based JITLinkMemoryManager for out-of-process JITting

<!-- *********************************************************************** -->

**Description of the project:** Write a shared-memory based JITLinkMemoryManager.  
LLVM’s JIT uses the JITLinkMemoryManager interface to allocate both working memory (where the JIT fixes up the relocatable objects produced by the compiler) and target memory (where the JIT’d code will reside in the target). JITLinkMemoryManager instances are also responsible for transporting fixed-up code from working memory to target memory. LLVM has an existing cross-process allocator that uses remote procedure calls (RPC) to allocate and copy bytes to the target process, however a more attractive solution (when the JIT and target process share the same physical memory) would be to use shared memory pages to avoid copies between processes.

**Expected results:**

Implement a shared-memory based JITLinkMemoryManager:*   Write generic LLVM APIs for shared memory allocation.
*   Write a JITLinkMemoryManager that uses these generic APIs to allocate shared working-and-target memory.
*   Make an extensive performance study of the approach.

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev), [Lang Hames](https://github.com/lhames)

**Desirable skills:** Intermediate C++; Understanding of LLVM and the LLVM JIT in particular; Understanding of virtual memory management APIs.

**Project type:** Large

**Discourse** [URL](https://discourse.llvm.org/t/implement-a-shared-memory-based-jitlinkmemorymanager-for-out-of-process-jitting)

<!-- *********************************************************************** -->

### Modernize the LLVM "Building A JIT" tutorial series

<!-- *********************************************************************** -->

**Description of the project:** The LLVM BuildingAJIT tutorial series teaches readers to build their own JIT class from scratch using LLVM’s ORC APIs, however the tutorial chapters have not kept pace with recent API improvements. Bring the existing tutorial chapters up to speed, write up a new chapter on lazy compilation (chapter code already available) or write a new chapter from scratch.

**Expected results:**

*   Update chapter text for Chapters 1-3 -- Easy, but offers a chance to get up-to-speed on the APIs.
*   Write chapter text for Chapter 4 -- Chapter code is already available, but no chapter text exists yet.
*   Write a new chapter from scratch -- E.g. How to write an out-of-process JIT, or how to directly manipulate the JIT'd instruction stream using the ObjectLinkingLayer::Plugin API.

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev), [Lang Hames](https://github.com/lhames)

**Desirable skills:** Intermediate C++; Understanding of LLVM and the LLVM JIT in particular; Familiarity with RST (reStructed Text); Technical writing skills.

**Project type:** Medium

**Discourse** [URL](https://discourse.llvm.org/t/modernize-the-llvm-building-a-jit-tutorial-series)

<!-- *********************************************************************** -->

### Write JITLink support for a new format/architecture

<!-- *********************************************************************** -->

**Description of the project:** JITLink is LLVM’s new JIT linker API -- the low-level API that transforms compiler output (relocatable object files) into ready-to-execute bytes in memory. To do this JITLink’s generic linker algorithm needs to be specialized to support the target object format (COFF, ELF, MachO), and architecture (arm, arm64, i386, x86-64). LLVM already has mature implementations of JITLink for MachO/arm64 and MachO/x86-64, and a relatively new implementation for ELF/x86-64. Write a JITLink implementation for a missing target that interests you. If you choose to implement support for a new architecture using the ELF or MachO formats then you will be able to re-use the existing generic code for these formats. If you want to implement support for a new target using the COFF format then you will need to write both the generic COFF support code and the architecture support code for your chosen architecture.

**Expected results:** Write a JITLink specialization for a not-yet-supported format/architecture.

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev), [Stefan Gränitz](https://github.com/weliveindetail), [Lang Hames](https://github.com/lhames)

**Desirable skills:** Intermediate C++; Understanding of LLVM and the LLVM JIT in particular; familiarity with your chosen format/architecture, and basic linker concepts (e.g. sections, symbols, and relocations).

**Project type:** Large

**Discourse** [URL](https://discourse.llvm.org/t/write-jitlink-support-for-a-new-format-architecture)

<!-- *********************************************************************** -->

### Instrumentation of Clang/LLVM for Compile Time

<!-- *********************************************************************** -->

**Description of the project:** Every developer, at some point (usually while waiting for their program to compile), has asked "Why is it taking so long?" This project is to seek an answer to this question. There exists within LLVM, and by extension CLANG, a timing infrastructure that records events within the compiler. However, its utilization is inconsistent and insufficient. This can be improved by adding more instrumentation throughout LLVM and CLANG but one must be careful. Too much instrumentation, or instrumenting the wrong things, can be confusing and overwhelming, thus making it no more useful than not enough information. The trick is to find the right places to instrument and controlling the instrumentation. Seeking out these key spots will take you through the entire compilation process, from preprocessing through to final code generation, and all phases between. As you instrument the code, you will look at the data as you evolve it, which will further direct your search. You will develop new ways to control and filter the information to allow a better understanding of where the compiler is spending its time. You will seek out and develop example test inputs that illustrate where the compiler can be improved, which will in turn, help direct your instrumenting and search. You will consider and develop ways of controlling the instrumentation to allow better understanding and detailed examination of phases of compilation. Through all of this, you will gain an understanding of how a compiler works, from front end processing, through the LLVM optimization pipeline, through to code generation. You will see, and understand, the big picture of what is required to compile and optimize a C/C++ program, and in particular, how CLANG, LLVM and LLC accomplish these tasks. Your mentors have a combined experience of approximately 25 years of compiler development and around 8 years of experience with LLVM itself to help you on your quest.

**Expected results:**

*   Targetted expansion of the use of the existing timing infrastructure
*   Identification of appropriate test inputs for improving compile time
*   Identification of compile time hotspots
*   New and improved methods of controlling the timing infrastructure

**Confirmed Mentor:** Jamie Schmeiser, Whitney Tsang

**Desirable skills:** C++ programming skills; CLANG/LLVM knowledge an asset but not necessary; self motivated; curiosity; desire to learn

**Project type:** 175 or 350 hour

**Difficulty Rating:** Easy - Medium

**Discourse** [URL](https://discourse.llvm.org/t/instrumentation-of-clang-llvm-for-compile-time)

<!-- *********************************************************************** -->

### Machine Learning Guided Ordering of Compiler Optimization Passes

<!-- *********************************************************************** -->

**Description of the project** This continues the work of GSoC 2020 and [2021](https://summerofcode.withgoogle.com/archive/2021/projects/6411038932598784). Developers generally use standard optimization pipelines like -O2 and -O3 to optimize their code. Manually crafted heuristics are used to determine which optimization passes to select and how to order the execution of those passes. However, this process is not tailored for a particular application, or kind of application, as it is designed to perform “reasonably well” for any input. We want to improve the existing heuristics or replace the heuristics with machine learning-based models so that the LLVM compiler can provide a superior order of the passes customized per application. The last milestone enabled feature extraction, and started investigating training a policy for selecting a more appropriate pass pipeline.

**Project size:** either 175 or 350 hr.

**Difficulty:** Medium

**Skills:** C/C++, some compiler experience. ML experience is a bonus.

**Expected outcomes**: Pre-trained model selecting the most economical optimization pipeline, with no loss in performance; hook-up of model in LLVM; (re-)training tool.

**Mentors** Tarindu Jayatilaka, Mircea Trofin, Johannes Doerfert

**Discourse** [URL](https://discourse.llvm.org/t/machine-learning-guided-ordering-of-compiler-optimization-passes/60415)

<!-- *********************************************************************** -->

### Learning Loop Transformation Policies

<!-- *********************************************************************** -->

**Description of the project** This project is a continuation of last [year’s](https://summerofcode.withgoogle.com/archive/2021/projects/5732097817313280). In 2021, the project achieved its first milestone - separating correctness decisions from policy decisions. This opens up the possibility of replacing the latter with machine-learned ones. Rough milestones: 1) select an initial set of features and use the existing ML Guided Optimizations (MLGO) infra to generate training logs; 2) define a reward signal, computable at compile time, to guide a reinforcement learning training loop; 3) iterate through training and refine reward/feature set

**Project size:** either 175 or 350 hr, ideally 350 hr

**Difficulty:** Medium/Hard

**Skills:** C/C++, some compiler experience. ML experience is a bonus.

**Expected outcomes**: policy ('advisor') interface for loop unrolling, with current heuristic as default implementation; set up feature extraction for reinforcement learning training; set up a reward metric; set up training algorithm, and iterate over policy training

**Mentors** Johannes Doerfert, Mircea Trofin

**Discourse** [URL](https://discourse.llvm.org/t/learning-loop-transformation-policies/60413)

<!-- *********************************************************************** -->

### Evaluate and Expand the Module-Level Inliner

<!-- *********************************************************************** -->

**Description of the project** LLVM's inliner is a bottom-up, strongly-connected component-level pass. This places limits on the order in which call sites are evaluated, which impacts the effectiveness of inlining. We now have a functional Module Inliner, as result of [GSoC2021 work](https://summerofcode.withgoogle.com/archive/2021/projects/5195658885070848). We want to call site priority schemes, effectiveness/frequency of running function passes after successful inlinings, interplay with the ML inline advisor, to name a few areas of exploration.

**Project size:** either 175 or 350 hr, ideally 350 hr, milestones allow for 175hr scoping

**Difficulty:** Medium/Hard

**Skills:** C/C++, some compiler experience.

**Expected outcomes**: Proposal and Evaluation of alternative traversal orders; evaluation of 'clustering' inlining decisions (inline more than one call site at a time); evaluation of effectiveness/frequency of function optimization passes after inlining

**Mentors** Kazu Hirata, Liqiang Tao, Mircea Trofin

**Discourse** [URL](https://discourse.llvm.org/t/evaluate-and-expand-the-module-level-inliner/60525)

<!-- *********************************************************************** -->

### Richer symbol dependency information for LTO

<!-- *********************************************************************** -->

**Description of the project:** C and C++ programs are often composed of various object files produced from separately-compiled source files that are then linked together. When compiling one source file, knowledge that can be derived from the logic contained within the other source files would normally not be available. Link-time optimization, also known as LTO, is a way for optimization to be done using information from more than one source file.

In LLVM, LTO is achieved by using LLVM bitcode objects as the output from the "compile" step and feeding those objects into the link step. LLVM's LTO operates in conjunction with the linker. The linker is invoked by the user and the linker in turn drives LLVM's LTO when it encounters LLVM bitcode files, getting information from LTO about what symbols a bitcode object defines or references. Information about what symbols are defined in or referenced from an object is necessary for the linker to perform symbol resolution, and a linker is normally able to extract such information from regular (non-bitcode) object files.

The implied consequences of LLVM's LTO implementation with respect to linker GC (linker garbage collection) can be improved, especially for aggressive forms of linker GC with lazy inclusion of objects and sections. In particular, the symbols referenced but undefined by an LTO module are, to the linker, monolithic at the module level. At the same time, the symbols referenced but undefined by regular (non-LTO) objects are monolithic to LTO. Together, this means that the inclusion of an LTO module into the overall process potentially leads, in the linker's initial symbol resolution, to all the undefined symbols in that module being considered as referenced; in turn, additional artifacts (e.g., archive members) may be added into the resolution, which further leads to references that may resolve to symbols defined in LTO modules and a premature conclusion that the definition of these symbols are needed. This at least means potentially unnecessary codegen is being done for functions that will be garbage-collected in the end (waste of electricity and time).

We acknowledge that an ideal implementation probably involves a "coroutine" like interaction between the linker and LTO codegen where information flows back and forth; however, such an endeavour is invasive to both linkers and to LLVM.

We believe that by

*   having the linker register, via an API to LTO, symbol reference "nodes" modelling the relationship between a symbol and the symbols that are referenced in turn from (the object file section containing) its linker-selected definition, and
*   using that information in LTO processing,

the LTO processing will be able to effectively identify a more accurate set of LTO symbols that are visible outside of the LTO unit. The linker merely needs to identify only exported symbols and entry points (such as the entry point for an executable and functions involved in initialization and finalization).

Having the LLVM opt/codegen understand the dependency implications from the "outside world" is strictly better than the other direction: the symbols referred to by relocations in non-LTO code are pretty much fixed as compiled (whereas some references in LTO code may disappear with optimization).

**Expected results:**

1.  Modification of the C++ LTO interface used by LLD to implement an interface to record the symbol reference dependency data (incorporating awareness of sections and comdats). This may additionally include a method to add LTO objects provisionally, simulating behaviours where linkers only add objects as needed.
2.  Modification of LTO to use new symbol reference information for definitions in regular objects when visiting definitions in the IR prior to the internalization pass to discover (transitive) symbol references and record the so-referenced symbols as being visible to regular objects. This may additionally include the "late" incorporation of LTO objects added provisionally into the merged LTO module.
3.  Modification of LLD (for ELF) to modify initial resolution to use the new interface as a replacement for setting `VisibleToRegularObj` except for entry point functions (including C++ dynamic initialization and finalization).

**Confirmed Mentors:** Sean Fertile, Hubert Tong, Wael Yehia

**Desirable skills:** Intermediate C++; basic linker concepts (e.g., symbols, sections, and relocations)

**Project size:** 350 hours

**Difficultly:** Medium/Hard

**Discourse** [URL](https://discourse.llvm.org/t/richer-symbol-dependency-information-for-lto/60335)

<!-- *********************************************************************** -->

### Remove undef: move uninitialized memory to poison

<!-- *********************************************************************** -->

**Description of the project** The existence of the undef value in LLVM prevents several optimizations, even in programs where it is not used. Therefore, we have been trying to move all uses of undef to poison so we can eventually remove undef from LLVM.  
This project focuses on uninitialized memory: right now the semantics of LLVM is that loading a value from uninitilized memory yields an undef value. This prevents, for example, SROA/mem2reg from optimizing conditional loads as phi(undef, %x) cannot be replaced with x, as %x might be poison.  
This project consists in devising a consistent semantics for uninitialized (based on existing proposals), an upgrade plan for LLVM, and implementing the changes in LLVM and clang. In clang the changes should be specific to bit-fields.  
For more information see the following [discussion](https://github.com/llvm/llvm-project/issues/52930) and/or contact the mentor.  
Further reading: [introduction to LLVM's memory model](https://web.ist.utl.pt/nuno.lopes/pubs/llvmmem-oopsla18.pdf).

**Project size:** 350 hr

**Difficulty:** Medium/Hard

**Skills:** Intermediate C++

**Expected outcomes**:

*   Semantics for memory operations that removes the need for undef values
*   Upgrade plan for LLVM and frontends
*   Implementation of the proposed semantics in LLVM
*   Implementation of auto-upgrade path for old LLVM IR files
*   Implementation of fixes in clang to use the new IR features
*   Benchmarking to check for regressions and/or perf improvements

**Mentors:** [Nuno Lopes](https://web.ist.utl.pt/nuno.lopes/)

<!-- *********************************************************************** -->

### Add API/ABI export annotations to the LLVM build

<!-- *********************************************************************** -->

**Description of the project**

Currently, all libraries inside LLVM export all their symbols publicly. When linking statically against them, the linker will remove unused symbols and this is not a problem.

When the libraries are built as shared libraries however, the number of exported symbols is very large and symbols that are meant to be internal spill into the public ABI of the shared libLLVM.so.

In this project, we’d like to change the default visibility of library symbols to “hidden”, add an annotation macro to LLVM and use the macro to gradually move the entire library in this direction. This will eventually enable building the shared libLLVM.so on Windows as well.

In practice, this means adding -fvisibility=hidden to individual libraries and annotating exported symbols with the LLVM export annotation.

We would like this work to be as unintrusive into other developer’s workflow as possible, so starting with a small internal library would be beneficial, e.g. one of the LLVM targets or IR passes.

For further reading, there is a Discourse thread avaiable that discusses the idea behind this proposal: [Supporting LLVM\_BUILD\_LLVM\_DYLIB on Windows](https://discourse.llvm.org/t/supporting-llvm-build-llvm-dylib-on-windows/58891) as well as the linked Phabricator review with a patch implementing the functionality: [⚙ D109192 \[WIP/DNM\] Support: introduce public API annotation support](https://reviews.llvm.org/D109192) None of this work has been committed yet but can be used as a starting point for this proposal.

**Project size:** Medium

**Difficulty:** Easy

**Skills:** Build systems, CMake, LLVM

**Expected outcomes**:

*   Export macro implemented and commited to LLVM
*   At least one internal target ported to the new export scheme

**Mentors:** Timm Bäder, Tom Stellard

<!-- *********************************************************************** -->

## Clang

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Extend clang AST to provide information for the type as written in template instantiations.

<!-- *********************************************************************** -->

**Description of the project:** When instantiating a template, the template arguments are canonicalized before being substituted into the template pattern. Clang does not preserve type sugar when subsequently accessing members of the instantiation.

```
std::vector&lt;std::string&gt; vs;
    int n = vs.front(); // bad diagnostic: [...] aka 'std::basic_string&lt;char&gt;' [...]

    template&lt;typename T&gt; struct Id { typedef T type; };
    Id&lt;size_t&gt;::type // just 'unsigned long', 'size_t' sugar has been lost
```

Clang should "re-sugar" the type when performing member access on a class template specialization, based on the type sugar of the accessed specialization. The type of vs.front() should be std::string, not std::basic\_string&lt;char, \[...\]&gt;.  

Suggested design approach: add a new type node to represent template argument sugar, and implicitly create an instance of this node whenever a member of a class template specialization is accessed. When performing a single-step desugar of this node, lazily create the desugared representation by propagating the sugared template arguments onto inner type nodes (and in particular, replacing Subst\*Parm nodes with the corresponding sugar). When printing the type for diagnostic purposes, use the annotated type sugar to print the type as originally written.  

For good results, template argument deduction will also need to be able to deduce type sugar (and reconcile cases where the same type is deduced twice with different sugar).

**Expected results:** Diagnostics preserve type sugar even when accessing members of a template specialization. T&lt;unsigned long&gt; and T&lt;size\_t&gt; are still the same type and the same template instantiation, but T&lt;unsigned long&gt;::type single-step desugars to 'unsigned long' and T&lt;size\_t&gt;::type single-step desugars to 'size\_t'.

**Confirmed Mentor:** [Vassil Vassilev](https://github.com/vgvassilev), [Richard Smith](https://github.com/zygoloid)

**Desirable skills:** Good knowledge of clang API, clang's AST, intermediate knowledge of C++.

**Project type:** Large

**Discourse** [URL](https://discourse.llvm.org/t/clang-extend-clang-ast-to-provide-information-for-the-type-as-written-in-template-instantiations)

<!-- *********************************************************************** -->

### Implement support for C++17 structured bindings in the Clang Static Analyzer

<!-- *********************************************************************** -->

**Description of the project:** Even though a lot of new C++ features are supported by the static analyzer automatically by the virtue of clang AST doing all the work under the hood, the C++17 "structured binding" syntax

```
auto [x, y] = ...;
```

requires some extra work on the Static Analyzer side. The analyzer's transfer functions need to be taught about the new AST nodes, [BindingDecl](https://clang.llvm.org/doxygen/classclang_1_1BindingDecl.html) and [DecompositionDecl](https://clang.llvm.org/doxygen/classclang_1_1DecompositionDecl.html), to work correctly in all [three interpretations](https://en.cppreference.com/w/cpp/language/structured_binding) described by the Standard.  

Incomplete support for structured bindings is a common source of false positives in the uninitialized variable checker on modern C++ code, such as [#42387](https://github.com/llvm/llvm-project/issues/42387).  

It is likely that the Clang CFG also needs to be updated. Such changes in the CFG may improve quality of clang warnings outside of the Static Analyzer.

**Expected results:** The Static Analyzer correctly models structured binding and decomposition declarations. In particular, binding variables no longer appear uninitialized to the Static Analyzer's uninitialized variable checker.

**Confirmed Mentor:** [Artem Dergachev](https://github.com/haoNoQ), [Rashmi Mudduluru](https://github.com/t-rasmud), [Gábor Horváth](https://github.com/xazax-hun), [Kristóf Umann](https://github.com/Szelethus)

**Desirable skills:** Intermediate knowledge of C++. Some familiarity with Clang AST and/or some static analysis background.

**Project size:** 350 hr

**Difficulty:** Medium/Hard

**Discourse** [URL](https://discourse.llvm.org/t/implement-support-for-c-17-structured-bindings-in-the-clang-static-analyzer/60588)

<!-- *********************************************************************** -->

### Improve Clang Diagnostics.

<!-- *********************************************************************** -->

**Description:** Clang Diagnostics, which issues Warnings and Errors to the programmer, are a critical feature of the compiler. Great diagnostics can have a significant impact on the user experience of the compiler and increase their productivity.

Recent improvements in GCC [\[1\]](https://developers.redhat.com/blog/2018/03/15/gcc-8-usability-improvements) [\[2\]](https://developers.redhat.com/blog/2019/03/08/usability-improvements-in-gcc-9/) shows that there is significant headroom to improve diagnostics (and user interactions in general). It would be a very impactful project to survey and identify all the possible improvements to clang on this topic and start redesigning the next generation of our diagnostics.

In addition, we will also make conclusions on issues reported on the LLVM Github Issue page labeled with [clang-diagnostics](https://github.com/llvm/llvm-project/labels/clang%3Adiagnostics) and if they need fixing, we will prepare patches otherwise simply close them.

**Expected outcomes**: Diagnostics will be improved:

*   Improve diagnostic aesthetics
*   Cover missing diagnostics
*   Reduce false positive rate
*   Reword diagnostics

**Confirmed Mentor:** [Aaron Ballman](https://github.com/AaronBallman), [Erich Keane](https://github.com/erichkeane), [Shivam Gupta](https://github.com/xgupta)

**Desirable skills:** C++ coding experience

**Project type:** Large/350 hr

**Discourse** [URL](https://discourse.llvm.org/t/improve-clang-diagnostics/61521)

<!-- *********************************************************************** -->

## Polly

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Complete switch to new pass manager

<!-- *********************************************************************** -->

**Description of the Project:** While the standard Polly-enabled -O1/-O2/-O3 optimization pass pipelines work fine with the [New Pass Manager](https://blog.llvm.org/posts/2021-03-26-the-new-pass-manager/) (NPM), some parts of Polly still only works with the legacy pass manager. This includes some passes such as -polly-export-jscop/-polly-export-jscop, regression testing, Polly-ACC, command line options such as -polly-show, the PassInstrumentation mechanism used by e.g. -print-after-all. LLVM (and Clang) have moved to NPM being the default and support for the legacy pass manager is deprecated, slowly degenerates and features getting removed. That is, all of Polly's functionality should eventually work with the NPM as well, and be prepared for the complete removal of the legacy pass manager. More details about the two pass managers found [here](https://github.com/banach-space/llvm-tutor#about-pass-managers-in-llvm).

**Expected results:** The goal is to make Polly more usable with using only the NPM. Milestones, not necessarily all to be reached in this GSoC, are:  
1\. Make all of Polly's functionality available in the NPM (or decide to deprecate/remove it)  
2\. Better integration into the NPM (such as supporting PassInstrumentation); If the NPM turns out to be inadequate, use only a monolothic function pass.  
3\. Replace the legacy pass manager in regression tests.  
4\. Be ready for complete removal of the legacy pass manager in LLVM.

**Confirmed mentor:** [Michael Kruse](https://github.com/Meinersbur)

**Desirable skills:** Understanding of the C++ template pattern used by the new pass manager ([CRTP](https://en.wikipedia.org/wiki/Curiously_recurring_template_pattern), [Mixins](https://en.wikipedia.org/wiki/Mixin), etc). Familarity with how LLVM can be [linked](https://www.lurklurk.org/linkers/linkers.html) (static, BUILD\_SHARED\_LIBS, and SHLIB/DYLIB) and its [plugin loading machanisms](https://www.llvm.org/docs/WritingAnLLVMPass.html#building-pass-plugins) (static, -load and -load-pass-plugin). Ideally, already worked with LLVM's new pass manager.

**Project size:** Medium

**Difficulty:** Medium/Hard

**Discourse** [URL](https://discourse.llvm.org/t/61174)

<!-- *********************************************************************** -->

## Enzyme

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Move Enzyme Instruction Transformation Rules to Tablegen

<!-- *********************************************************************** -->

**Description of the project:** Enzyme performs automatic differentiation (in the calculus sense) of LLVM programs. This enables users to use Enzyme to perform various algorithms such as back-propagation in ML or scientific simulation on existing code for any language that lowers to LLVM. The support for an increasing number of LLVM Versions (7-main), AD modes (Reverse, Forward, Forward-Vector, Reverse-Vector, Jacobian), and libraries (BLAS, OpenMP, MPI, CUDA, ROCm, ...) leads to a steadily increasing code base. In order to limit complexity and help new contributors we would like to express our core logic using LLVM Tablegen. The applicant is free to decide how to best map the program transformation abstractions within Enzyme to Tablegen.

**Expected results:** 1. A working tablegen rule generation system within Enzyme  
2\. Moving several existing rules to the new autogenerated system (e.g. LLVM instructions, LLVM intrinsics, BLAS calls, MPI calls, ...  

**Confirmed mentor:** [William Moses](mailto:wmoses@mit.edu), Valentin Churavy

**Desirable skills:** Good knowledge of C++, calculus, and LLVM and/or Clang, and/or MLIR internals. Experience with Tablegen, Enzyme or automatic differentiation would be nice, but can also be learned in the project.

**Project size:** Large

**Difficulty:** Medium

**Discourse** [URL](https://discourse.llvm.org/t/enzyme-moving-instruction-rules-to-tablegen/61176)

<!-- *********************************************************************** -->

### Vector Reverse-Mode Automatic Differentiation

<!-- *********************************************************************** -->

**Description of the project:** Enzyme performs automatic differentiation (in the calculus sense) of LLVM programs. This enables users to use Enzyme to perform various algorithms such as back-propagation in ML or scientific simulation on existing code for any language that lowers to LLVM. Enzyme already implements forward and reverse mode automatic differentiation. Enzyme also implements vector forward mode automatic differentiation, which allows Enzyme to batch the derivative computation of several objects in a single call. The goal of this project is too extend this capability in order to perform vector reverse mode. In doing so, multiple sweeps of reverse mode automatic differentiation can be performed at the same time, reducing memory, time, and otherwise generally enabling further optimization.

**Expected results:** Vectorized version of reverse mode automatic differentiation

**Confirmed mentor:** [William Moses](mailto:wmoses@mit.edu), Tim Gymnich

**Desirable skills:** Good knowledge of C++ and some experience with LLVM API's. Experience with Enzyme or automatic differentiation would be nice, but can also be learned in the project.

**Project size:** Medium

**Difficulty:** Medium

**Discourse** [URL](https://discourse.llvm.org/t/enzyme-vector-reverse-mode-automatic-differentiation/61177)

<!-- *********************************************************************** -->

### Enable The New Pass Manager

<!-- *********************************************************************** -->

**Description of the project:** Enzyme is a compiler plugin for LLVM that performs automatic differentiation (in the calculus sense) of LLVM programs. This enables users to use Enzyme to perform various algorithms such as back-propagation in ML or scientific simulation on existing code for any language that lowers to LLVM.  
Enzyme integrates into frontends through the use of an LLVM plugin that can be loaded into Clang, LLVM (opt), the linker (lld), libraries (HIPRtc), directly loaded (Julia), among others (Flang, Rust, etc).  
While using various pieces of machinery from the new pass manager internally, Enzyme does not currently automatically register its transformation passes when using the new pass manager. This creates problems for users on LLVM 13 or above, where the new pass manager is run by default and may not understand why they get linker errors from their code not being differentiated (currently they must add a flag to specify the old pass manager).  
The goal of this project is to enable Enzyme to be called by the new pass manager in LLVM and generally create a coherent user experience.  

**Expected results:** 1. Enzyme can be called by the new pass manager  
2\. \[Optional\] Additional syntactic sugar that makes it easier to use Enzyme.  

**Confirmed mentor:** [William Moses](mailto:wmoses@mit.edu), Valentin Churavy

**Desirable skills:** Good knowledge of C++, and LLVM. Experience with Enzyme would be nice, but can also be learned in the project.

**Project size:** Small

**Difficulty:** Medium

**Discourse** [URL](https://discourse.llvm.org/t/enzyme-enable-the-new-pass-manager/61178)

<!-- *********************************************************************** -->

# Google Summer of Code 2021

<!-- *********************************************************************** -->

Welcome prospective Google Summer of Code 2021 Students! This document is your starting point to finding interesting and important projects for LLVM, Clang, and other related sub-projects. This list of projects is not only developed for Google Summer of Code, but open projects that really need developers to work on and are very beneficial for the LLVM community.

We encourage you to look through this list and see which projects excite you and match well with your skill set. We also invite proposals not on this list. You must propose your idea to the LLVM community through our developers' mailing list (llvm-dev@lists.llvm.org or specific subproject mailing list). Feedback from the community is a requirement for your proposal to be considered and hopefully accepted.

The LLVM project has participated in Google Summer of Code for several years and has had some very successful projects. We hope that this year is no different and look forward to hearing your proposals. For information on how to submit a proposal, please visit the Google Summer of Code main [website.](https://developers.google.com/open-source/gsoc/)

<!-- *********************************************************************** -->

## LLVM

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Distributed lit testing

<!-- *********************************************************************** -->

**Description of the project:** The LLVM lit test suites consist of thousands of small independent tests. Due to the number of tests, it can take a long time to run the full suite, even on a high-spec computer. Builds are already distributable across multiple computers available on the same network, using software such as distcc or icecream, so running tests on a single machine becomes a potential bottleneck. One way to speed up running of the tests could be to distribute test execution across many computers too. Lit provides a test sharding mechanism, which allows multiple computers to run parts of the same testsuite in tandem, but this currently assumes access to a single common filesystem, which may not be possible in all cases and a knowledge of which machines the suite can currently be run on. This project’s goal is to update the existing lit harness (or write a wrapper around it) to allow distribution of the tests in this way, with the idea that developers can write their own interface between the harness and the distribution system of their choice. This harness may need to be able to identify test dependencies such as input files and executables, send the tests to the distribution system (possibly in batches), and receive, collate and report the results to the user, in a similar manner to how lit already does.

**Expected results:** An easy to use harness as described above. Some evidence that given a distributed system, a user can expect to see test suite execution to speed up if they are using that harness.

**Confirmed mentor:** James Henderson

**Desirable skills:** Good knowledge of Python. Familiarity with LLVM lit testing. Some knowledge of distribution systems would also be beneficial.

<!-- *********************************************************************** -->

### Learning Loop Transformation Heuristics

<!-- *********************************************************************** -->

**Description of the project:** This is a short description, please reach out to Johannes (jdoerfert on IRC) and Mircea Trofin if it sounds interesting. We successfully introduced an ML framework for inliner decisions, now we want to expand the scope. In this project we will look at loop transformation heuristics, such as the unroll factor. As a motivational example we can look at a small trip count [dgemm](https://godbolt.org/z/Eeqcvs) which we optimize pretty poorly. With the nounroll pragmas we do a better job but still not close to gcc. The project is open-ended and we could look at various passes/heuristics concurrently.

**Preparation resources:** The ML inliner framework in the LLVM code base as well as the [paper](https://arxiv.org/abs/2101.04808). LLVM transform passes (that are based on heuristics), e.g., loop unroll.

**Expected results:** Measurable better performance with a learned predictor, potentially a set of "classical" heuristics derived from the ML model.

**Confirmed Mentor:** Johannes Doerfert, Mircea Trofin

**Desirable skills:** Intermediate knowledge of ML, C++, self motivation.

<!-- *********************************************************************** -->

### Fuzzing LLVM-IR Passes

<!-- *********************************************************************** -->

**Description of the project:** This is a short description, please reach out to Johannes (jdoerfert on IRC) if it sounds interesting. Fuzzing often reveals a myriad of bugs. CSmith (and others) showed how to do this with C-like languages and we have used [LLVM-IR fuzzing](https://www.youtube.com/watch?v=UBbQ_s6hNgg) in the past successfully. In this project we will apply fuzzing to new passes that are in development, e.g., the Attributor pass. We want to find and fix crashes but also other bugs, including compile time performance problems.

**Preparation resources:** The [LLVM fuzzer infrastructure](https://llvm.org/docs/FuzzingLLVM.html#llvm-opt-fuzzer). LLVM passes that we might want to fuzz, e.g. the Attributor pass. Prior IR-Fuzzing work (https://www.youtube.com/watch?v=UBbQ\_s6hNgg)

**Expected results:** Crashes, maybe also a way to catch non-crash bugs, including performance problems.

**Confirmed Mentor:** Johannes Doerfert

**Desirable skills:** Intermediate knowledge C++, self motivation.

<!-- *********************************************************************** -->

### llvm.assume the missing pieces

<!-- *********************************************************************** -->

**Description of the project:** This is a short description, please reach out to Johannes (jdoerfert on IRC) if it sounds interesting. llvm.assume is a powerful mechanism to retain knowledge. Since it inception it was improved already multiple times but there are major extensions still outstanding which we want to tackled in this project. An incomplete list of topics includes:

*   range-based assumptions, design idea 3) in the [RFC](https://lists.llvm.org/pipermail/llvm-dev/2019-December/137632.html).
*   outline arbitrary assumption/assertion code, design idea 2) in the [RFC](https://lists.llvm.org/pipermail/llvm-dev/2019-December/137632.html).
*   side-effect free assumptions, see [this review](https://reviews.llvm.org/D89054).
*   more knowledge retention usages
*   less interference with optimizations

**Preparation resources:** The llvm.assumption usage, the assumption cache, the "enable-knowledge-retention" option, the [RFC](https://lists.llvm.org/pipermail/llvm-dev/2019-December/137632.html) and [this review](https://reviews.llvm.org/D89054).

**Expected results:** New llvm.assume use cases, improved performance through knowledge retention, optimization based on assertions.

**Confirmed Mentor:** Johannes Doerfert

**Desirable skills:** Intermediate knowledge C++, self motivation.

<!-- *********************************************************************** -->

### Fix fundamental issues in LLVM's IR

<!-- *********************************************************************** -->

**Description of the project:** LLVM's IR has fundamental, long-standing issues. Many are related with undefined behaviors. Others are simply a fallout from underspecification and different interpretations by diffferent people. [Alive2](https://github.com/AliveToolkit/alive2) is a tool that detects bugs in LLVM's optimizations automatically. Using Alive2, we track bugs exposed by the unit tests on a [dashboard](https://web.ist.utl.pt/nuno.lopes/alive2/).

**Expected results:** 1) Report and fix bugs detected by Alive2. 2) Pick one fundamental IR issue and make progress towards fixing it, including proposing fixes for the [semantics](https://llvm.org/docs/LangRef.html), testing fixes to the semantics by running Alive2 over the LLVM unit tests and medium-sized programs, test performance of semantic fixes and fix performance regressions.

**Confirmed Mentor:** Nuno Lopes, Juneyoung Lee

**Desirable skills:** Intermediate C++; willingness to learn about LLVM IR semantics; experience reading papers (preferred).

<!-- *********************************************************************** -->

### Utilize LoopNest Pass

<!-- *********************************************************************** -->

**Description of the project:** The idea of LoopNest pass is recently added, and there are no existing passes utilizing it. Before having LoopNest pass, if you want to write a pass that works on a loop nest, you have to pick from either a function pass or a loop pass. If you chose to write it as a function pass, then you lose the ability to add loops dynamically back to the pipeline. If you decide to write it as a loop pass, then you are wasting compile time to traverse to your pass and return right away when the given loop is not the outermost loop. In this project, we want to utilize the recently introduced LoopNest pass for passes intended for loop nest and have the same ability as the LoopPass to dynamically add loops to the pipeline. In addition, improve the current implementation of LoopNestPass when necessary.

**Expected results (possibilities):** Utilize LoopNest Pass for some existing transformations/analyses.

**Confirmed Mentors:** Whitney Tsang, Ettore Tiotto

**Desirable skills:** Intermediate knowledge of C++, self-motivation.

<!-- *********************************************************************** -->

### JIT-ing OpenMP GPU kernels transparently

<!-- *********************************************************************** -->

**Description of the project:** This is a short description, please reach out to Johannes (jdoerfert on IRC) if it sounds interesting. OpenMP GPU kernels are usually lowered to native binaries, e.g., cubin, and embedded into the host object. At runtime, OpenMP "plugins" will connect with the device driver, e.g., CUDA, to load and run such embedded binary images. In this project we want to develop a new plugin that takes LLVM-IR code, optimizes the IR with kernel parameters known only at runtime, and then generates the GPU binary for consumption by other plugins. Similar to the [remote offload plugin](https://openmp.llvm.org/docs/design/Runtimes.html#remote-offloading-plugin) we can do this transparently to the user. In addition to the JIT infrastructure setup in the plugin we will need to embed the IR into the host object.

**Preparation resources:** OpenMP target offloading infrastructure, LLVM JIT infrastructure.

**Expected results:** A JIT-capable offload plugin which can achieve superior performance when kernel specialization is enabling optimizations.

**Confirmed Mentor:** Johannes Doerfert

**Desirable skills:** Intermediate knowledge C++, JIT compilation, self motivation.

<!-- *********************************************************************** -->

## OpenACC

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### OpenACC Diagnostics from the OpenMP Runtime

<!-- *********************************************************************** -->

**Description of the project:** Clacc and Flacc are projects to introduce OpenACC support to Clang and Flang. For that purpose, OpenACC runtime support is being developed on top of LLVM's OpenMP runtime. However, diagnostics emitted by LLVM's OpenMP runtime are expressed in terms of OpenMP concepts, and so those diagnostics are not always meaningful to OpenACC users. This project should address this issue in two steps:

1.  Develop a mechanism that selects OpenACC versions of diagnostics that are emitted as a result of OpenACC-related calls into the runtime. This mechanism should be general enough that it could be used for programming languages besides OpenMP and OpenACC. One possible approach is to extend internationalization mechanisms already present in some components of the OpenMP runtime.
2.  Provide OpenACC translations for existing OpenMP diagnostics. This step requires an understanding of the relationship between OpenACC and OpenMP as implemented in Clacc and Flacc.

Many components of OpenACC support that will depend upon this project have not yet been upstreamed and are under development. A high-level understanding of those efforts is helpful for this project and can be provided by the mentors. Nevertheless, this project can be completed in upstream LLVM's OpenMP runtime now independently of those efforts.

**Expected results:** A version of upstream LLVM's OpenMP runtime that can emit OpenACC diagnostics as needed.

**Confirmed Mentors:** Valentin Clement, Joel E. Denny

**Desirable skills:** Intermediate C++; Experience with OpenACC or OpenMP

<!-- *********************************************************************** -->

## Polly

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Use official isl C++ bindings

<!-- *********************************************************************** -->

**Description of the project:** Polly use algorithms from the [Integer Set Library (isl)](http://isl.gforge.inria.fr/), which is a library written in C. It uses reference-counting for memory management. Getting reference counting correct is much easier in C++ using RAII, therefore we created a C++ binding for isl: [isl-noexceptions.h](https://github.com/llvm/llvm-project/blob/main/polly/lib/External/isl/include/isl/isl-noexceptions.h). Since then, isl also gained two official C++ bindings, [cpp.h](https://github.com/llvm/llvm-project/blob/main/polly/lib/External/isl/include/isl/cpp.h) and [cpp-checked.h](https://github.com/llvm/llvm-project/blob/main/polly/lib/External/isl/include/isl/cpp-checked.h). We would like to replace the Polly-maintained C++ bindings with the upstream bindings. Unfortunately, this is not an in-place replacement. Differences include how errors are checked, method names, which functions are considered as operator/constructor overloads and the set of exported functions. This will require changing Polly's uses of the C++ bindings and submitting patches to isl to export additional functionality needed by Polly.

**Expected results:** Reduce the differences between the Polly-maintained isl-noexceptions.h bindings and one of the two C++ bindings that isl supports. Due to isl-noexceptions.h exporting more functions and classes than the upstream bindings do, a complete replacement will probably be out of reach, but even reducing the differences will reduce the maintenance cost of Polly's isl-noexceptions.h.

**Confirmed mentor:** Michael Kruse

**Desirable skills:** Deep knowledge of C++, in particular RAII and move-semantics. Interest in API design. Ideally, you already wrote some library's header file. Experience with the isl library would be nice, but can also be learned in the project.

<!-- *********************************************************************** -->

## Enzyme

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Integrate custom derivatives of BLAS, Eigen, and similar routines into Enzyme

<!-- *********************************************************************** -->

**Description of the project:** [Enzyme](https://enzyme.mit.edu/) performs automatic differentiation (in the calculus sense) of LLVM programs. This enables users to use Enzyme to perform various algorithms such as back-propagation in ML or scientific simulation on existing code for any language that lowers to LLVM. Enzyme does so by applying the chain rule to every instruction in every function called by the original function to be differentiated. While functional, this is not necessarily optimal for high-level matrix operations which may have algebraic properties for faster derivative computation. Enzyme also has a mechanism for specifying a custom gradient for a given function. If a custom derivative is available, Enzyme will use that rather than fallback to implementing its own. Many programs use BLAS libraries to efficiently compute matrix and tensor operations. This project would enable high-performance automatic differentiation of BLAS and similar libraries (such as Eigen) by specifying custom derivative rules for their operations.

**Expected results:** Efficient differentiation of BLAS and Eigen codes by writing custom derivative rules for matrix and tensor operations.

**Confirmed mentor:** [William Moses](mailto:wmoses@mit.edu), Johannes Doerfert

**Desirable skills:** Good knowledge of C++, calculus, and linear algebra. Experience with BLAS, Eigen, or Enzyme would be nice, but can also be learned in the project.

<!-- *********************************************************************** -->

### Integrate Enzyme into Swift to provide high-performance differentiation in Swift

<!-- *********************************************************************** -->

**Description of the project:** [Enzyme](https://enzyme.mit.edu/) performs automatic differentiation (in the calculus sense) of LLVM programs. This enables users to use Enzyme to perform various algorithms such as back-propagation in ML or scientific simulation on existing code for any language that lowers to LLVM. While this functions for any frontend that emits LLVM IR, it may be desirable to have closer integration between Enzyme and the frontend for the sake of passing additional information and creating a better user experience. Swift provides automatic differentiation through the use of specifying custom derivative rules in the front-end. Enzyme could be integrated directly with Swift, differentiating the eventual LLVM, but it would lose out on all this additional information about custom derivatives. Moreover, calling into Enzyme naiively would be without Type checking, fine AD-specific debug information, or various other nice tools that Swift provides users of AD. This project would seek to integrate Enzyme and the Swift front end to provide both a nice user-experience for swift programmers who want to use Enzyme to enable high-performance automatic differentiation, and also to allow Enzyme to take advantage of derivative-specific metadata already available in swift.

**Expected results:** Creation of a custom type-checked linguistic construct in Swift for calling Enzyme. Mechanisms for passing Swift's differentiation-specific metadata for use by Enzyme.

**Confirmed mentor:** [William Moses](mailto:wmoses@mit.edu), Vassil Vassilev

**Desirable skills:** Good knowledge of C++ and Swift. Experience with Enzyme or automatic differentiation would be nice, but can also be learned in the project.

<!-- *********************************************************************** -->

### Differentiation of Fixed-Point Arithmetic

<!-- *********************************************************************** -->

**Description of the project:** [Enzyme](https://enzyme.mit.edu/) performs automatic differentiation (in the calculus sense) of LLVM programs. This enables users to use Enzyme to perform various algorithms such as back-propagation in ML or scientific simulation on existing code for any language that lowers to LLVM. In a variety of fields, it is desirable to compute on fixed-point values (e.g. integers) rather than floating point values. This avoid certain truncation errors that may be critical to a given application. Moreover, particular pieces of hardware may simply be more efficient on fixed point rather than floating point values. This project would seek to extend Enzyme to support differentiation of not only floating point base values, but also fixed point base values..

**Expected results:** Implementation of adjoints for LLVM fixed point intrinsics, requisite type analysis rules, and integration into a front-end for an end-to-end test.

**Confirmed mentor:** [William Moses](mailto:wmoses@mit.edu)

**Desirable skills:** Good knowledge of C++, caclulus, and LLVM internals. Experience with Enzyme or automatic differentiation would be nice, but can also be learned in the project.

<!-- *********************************************************************** -->

### Integrate Enzyme into Rust to provide high-performance differentiation in Rust

<!-- *********************************************************************** -->

**Description of the project:** [Enzyme](https://enzyme.mit.edu/) performs automatic differentiation (in the calculus sense) of LLVM programs. This enables users to use Enzyme to perform various algorithms such as back-propagation in ML or scientific simulation on existing code for any language that lowers to LLVM. While this functions for any frontend that emits LLVM IR, it may be desirable to have closer integration between Enzyme and the frontend for the sake of passing additional information and creating a better user experience. This project would seek to integrate Enzyme and the Rust front end to provide a nice user-experience for Rust programmers who want to use Enzyme to enable high-performance automatic differentiation. This also potentially involves integration of LLVM plugin support/custom codegen into rustc.

**Expected results:** Creation of a custom type-checked linguistic construct in Rust for calling Enzyme. Mechanisms for parsing Rust's Type information (represented as debug LLVM debug info) directly into type analysis.

**Confirmed mentor:** [William Moses](mailto:wmoses@mit.edu)

**Desirable skills:** Good knowledge of C++ and Rust. Experience with Enzyme or automatic differentiation would be nice, but can also be learned in the project.

<!-- *********************************************************************** -->

### Clang Static Analyzer performance profiling

<!-- *********************************************************************** -->

**Description of the project:**

*   Chart how much time is spent in transfer functions – including (but not limited to!) checker callbacks.
*   Add llvm Statistics and Timers for quickly obtaining precise and concise dumps without external profilers. Statistics on state splits might be particularly interesting!
*   Measure time spent analyzing specific stack frames. Say, how much time do we spend inlining std::string methods? This time could be saved if we add custom models for these methods instead.

**Confirmed mentor:** Artem Dergachev

<!-- *********************************************************************** -->

### Clang Static Analyzer constraint solver improvements

<!-- *********************************************************************** -->

**Description of the project:** CSA has a small in-house constraint solver, it is pretty trivial, but super fast. The goal is to support range-based logic for some of the symbolic operators, while keeping it linear. Additionally, a unit-test framework can be designed specifically for testing constraint solvers (right now it’s tested rather awkwardly). This project has a couple of interesting properties. It can be segmented into small chunks, and each of these chunks has a non-trivial solution. It might introduce you to a world of solvers (it is a good idea to check your ideas with some heavy-weight solver such as z3). And because the existing solver is simple, there is a myriad of possible extensions to try.

**Confirmed mentor:** Valeriy Savchenko

<!-- *********************************************************************** -->

### A structured approach to diagnostics in LLDB

<!-- *********************************************************************** -->

**Description of the project:**

*   Design and integrate a new diagnostic abstraction (similar to clang::Diagnostic) to report errors, warnings and notes in a structured way.
*   Allow us to differentiate between bugs (unexpected errors) and things the debugger simply doesn’t know (expected errors). Be smart about printing global errors only once. Have the ability of being verbose and have additional metadata (source location, DWARF unit, object file, etc, depending on the type of error and where it originated).
*   Should be compatible and tightly integrated with the existing classes, such as the Status and CommandReturnObject.

**Confirmed mentor:** [Jonas Devlieghere and Raphael Isemann](mailto:teemperor@gmail.com,jonas@devlieghere.com?subject=[GSoC]%20LLDB%20Diagnostics)

<!-- *********************************************************************** -->

# Google Summer of Code 2020

<!-- *********************************************************************** -->

LLVM participation in Google Summer of Code 2020 was very successful and resulted in many interesting projects contributed to LLVM. For the list of accepted and completed projects, please take a look into Google Summer of Code [website.](https://summerofcode.withgoogle.com/archive/2020/organizations/5902726635978752/)

<!-- *********************************************************************** -->

## LLVM

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Improve inter-procedural analyses and optimizations

<!-- *********************************************************************** -->

**Description of the project:** This is a short description, please reach out to Johannes (jdoerfert on IRC) if it sounds interesting. During the GSoC'19 we build the Attributor framework to improve the inter-procedural capabilities of LLVM. This is useful on its own but especially in situations where inlining is impossible or undesirable. In this GSoC project we will look at capabilities not yet available in the Attributor and for the potential to connect the Attributor with existing intra- and inter-procedural optimizations. In this project there is a lot of freedom to determine the actual tasks but we will provide a pool of smaller and medium sized tasks that can be chosen from as well.

**Preparation resources:** The Attributor YouTube videos from the LLVM Developers Meeting 2019 and the recording of the IPO panel from the same meeting. The Attributor framework as well as other existing inter-procedural analyses and optimizations in LLVM.

**Expected results:** Measurable better IPO, especially visible in cases where inlining is not an option or undesirable.

**Confirmed Mentor:** Johannes Doerfert

**Desirable skills:** Intermediate knowledge of C++, self motivation.

<!-- *********************************************************************** -->

### Improve parallelism-aware analyses and optimizations

<!-- *********************************************************************** -->

**Description of the project:** This is a short description, please reach out to Johannes (jdoerfert on IRC) if it sounds interesting. With the OpenMPOpt pass ([under review]('https://reviews.llvm.org/D69930')) we started to teach the LLVM optimization pipeline about OpenMP parallelism encoded as OpenMP runtime calls. In this GSoC project we will look at capabilities not yet available in the OpenMPOpt pass and for the potential to connect existing intra- and inter-procedural optimizations, e.g. the Attributor. In this project there is a lot of freedom to determine the actual tasks but we will provide a pool of smaller and medium sized tasks that can be chosen from as well.

**Preparation resources:** The "Optimizing Indirections, using abstractions without remorse" video on YouTube from the LLVM Developers Meeting 2018. The paper "Compiler Optimizations for OpenMP" and "Compiler Optimizations For Parallel Programs" both by J. Doerfert and H. Finkel (the slides for these are potentially even more useful).

**Expected results:** Measurable better performance or program analysis results for parallel programs with a focus on OpenMP.

**Confirmed Mentor:** Johannes Doerfert

**Desirable skills:** Intermediate knowledge of C++, self motivation.

<!-- *********************************************************************** -->

### Make LLVM passes debug info invariant

<!-- *********************************************************************** -->

**Description of the project:** Generating debug information is one of the fundamental tasks a compiler typically fulfills. It is clear that executable generated code should not depend on the presence of debug information.  

Unfortunately there are known cases in LLVM were code generation differs depending on whether debug information is enabled (\`-g\`) or not. These kind of bugs can lead to bad debug experience ranging from unexpected execution behaviour to the point of programs running fine in debug mode while crashing without debug information.  

The issue has likely not a single cause but is triggered during different passes on different architectures. One such reason is the insertion of Call Frame Information (CFI) in the compiler backend during frame lowering and other later passes. The presence of CFI instructions seems to change instruction scheduling which therefore leads to different generated code.

**Preparation resources:**

*   [PR37728](https://llvm.org/PR37728) is a meta-bug that collects several related issues of differing codegen.
*   [PR37240](https://llvm.org/PR37240) is a bug discussing the CFI issue mentioned above.
*   The following [RFC](http://lists.llvm.org/pipermail/llvm-dev/2019-September/135433.html) discusses some possible mitigation strategies and gives some background information on the CFI issue.

**Expected results:**

*   Write some tooling based on existing scripts to automatically generate examples of differing codegen. This is intended as a starting task to get to know the existing LLVM tools, learn to read LLVM's internal outputs etc.
*   Choose one or more (depending on the difficulty) bugs that cause codegen differences and try to provide patches to fix them. We would be particularly interested in the mentioned CFI issue but working on some of the other related bugs is also absolutely fine.

**Confirmed Mentors:** Paul Robinson and David Tellenbach

**Desirable skills:** Intermediate knowledge of C++, some familarity with general computer architecture, some familarity with the x86 or Arm/AArch64 instruction set.

<!-- *********************************************************************** -->

### Improve MergeFunctions to incorporate MergeSimilarFunction patches and ThinLTO Support

<!-- *********************************************************************** -->

**Description of the project:** MergeSimilarFunctions pass is able to merge not just identical functions, but also functions with small differences in their instructions to reduce code size. It does this by inserting control flow and an additional argument in the merged function to account for the differences. This work was presented at the [LLVM Dev Meeting in 2013](http://llvm.org/devmtg/2013-11/#talk3) A more detailed description was published in a paper at [LCTES 2014](http://dl.acm.org/citation.cfm?id=2597811). The code was released to the community at the time. Meanwhile, the pass has been in production use at QuIC for the past few years and has been actively maintained internally. In order to magnify the impact of MergeSimilarFunctions, it has been ported to ThinLTO and the patches have been upstreamed (see stack of 5 patches mentioned below). But instead of replacing the existing MergeFunctions pass in LLVM-upstream the community suggested we improve the existing one with the ideas from MergeSimilarFunctions. And then leverage the ThinLTO on top of that. The MergeSimilarFunction used in ThinLTO gives impressive code size reduction across a wide range of workloads and the work was presented at [LLVM-dev 2018](https://llvm.org/devmtg/2018-10/talk-abstracts.html#talk2). The LLVM project would greatly benefit from this code size optimization as most embedded systems (think SmartPhones) applications are constrained on code-size.

**Preparation resources:**

*   Stack of patches:
    *   [MergeSimilarFunctions 1/n: a code size pass to merge functions with small differences](https://reviews.llvm.org/D52896)
    *   [\[Porting MergeSimilarFunctions 2/n\] Changes to DataLayout](https://reviews.llvm.org/D52898)
    *   [\[Merge SImilar Function ThinLTO 3/n\] Add hash code to function summary](https://reviews.llvm.org/D52966)
    *   [\[Merge SImilar Function ThinLTO 4/n\] Make merge function decisions before the thin-lto stage](https://reviews.llvm.org/D53253)
    *   [\[Merge SImilar Function ThinLTO 5/n\] Set up similar function to be imported](https://reviews.llvm.org/D53254)The paches can be easily applied to LLVM-trunk and would give a developer a decent head start ;).
*   List of llvm-dev mailing list posts on previous discussions around Merge Functions
    *   [Link1](http://lists.llvm.org/pipermail/llvm-dev/2019-January/129835.html)
    *   [Link2](http://lists.llvm.org/pipermail/llvm-dev/2019-March/131066.html)
    *   [Link3](http://lists.llvm.org/pipermail/llvm-dev/2019-February/129863.html)
    *   [Link4](http://lists.llvm.org/pipermail/llvm-dev/2019-January/129832.html)
*   [The original paper: LCTES 2014](http://dl.acm.org/citation.cfm?id=2597811)
*   [Video and slides of the presentation](https://llvm.org/devmtg/2018-10/talk-abstracts.html#talk2)

**Expected results:**

*   Improve MergeFunctions to have feature parity with MergeSimilarFunctions.
*   Enable MergeFunctions to ThinLTO.

**Confirmed Mentors:** Aditya Kumar (hiraditya on IRC and phabricator), JF Bastien (jfb on phabricator)

**Desirable skills:** Course on compiler design, SSA Representation, Intermediate knowledge of C++, Familiarity with LLVM Core.

<!-- *********************************************************************** -->

### Add DWARF support to yaml2obj

<!-- *********************************************************************** -->

**Description of the project:** LLVM provides a tool called yaml2obj which coverts a YAML document into an object file, for various different file formats such as ELF, COFF and Mach-O, along with obj2yaml which does the inverse. The tool is commonly used to test parts of LLVM, as YAML is often easier to use to describe an object file than raw assembly and more maintainable than a pre-built binary. DWARF is a debugging file format commonly used by LLVM. Many of the tests for LLVM’s DWARF emission are written in assembly, but it would be nicer to write them in YAML. However, yaml2obj does not properly support emission of DWARF sections. This project is to add functionality to yaml2obj to make writing test inputs for DWARF tests simpler, particularly for ELF objects.

**Preparation resources:** Reading up on the DWARF file format will be useful, in particular the standards available at http://dwarfstd.org/Download.php. Also, familiarising yourself with the basics of the ELF file format, as described here https://www.sco.com/developers/gabi/latest/contents.html, may be beneficial.

**Expected results:** The ability to use yaml2obj to generate DWARF sections for object files. Particularly important is ensuring the input YAML can be more easily understood than the equivalent assembly.

**Confirmed Mentors:** James Henderson

**Desirable skills:** Intermediate knowledge of C++.

<!-- *********************************************************************** -->

### Improve hot cold splitting to aggressively outline small blocks

<!-- *********************************************************************** -->

**Description of the project:** Hot Cold Splitting in LLVM is an IR level function splitting transformation. The goal of hot/cold splitting is to improve the memory locality of code and helps reduce startup working set. The splitting pass does this by identifying cold blocks and moving them into separate functions. Because it is implemented at the IR level all the back end target benefit from it. It is a relatively new optimization and it was recently presented at the [LLVM Dev Meeting in 2019](https://llvm.org/devmtg/2019-10/talk-abstracts.html#tech8) and the slides are [here](https://llvm.org/devmtg/2019-10/slides/Kumar-HotColdSplitting.pdf) Because most of the benefit comes from outlining small blocks e.g., \_\_assert\_rtn. The goal of this project is to identify potential blocks via static analysis e.g., exception handling code, optimizing personality functions. Use cost-model to ensure outlining reduces the code size of the caller, use tail call whenever appropriate to save instructions.

**Preparation resources:**

*   [Update on hot cold splitting](http://lists.llvm.org/pipermail/llvm-dev/2019-January/129606.html)
*   The following two papers provide earlier work on hot cold splitting. While these papers are a good start, LLVM's HCS has completely different implementation in two aspects a) It is implemented at IR level and outlines basic blocks as function rather than naked branches. b) It is based on regions and outlines a set of basic blocks.
    *   [Original paper on hot cold splitting by Pettis and Hansen.](http://pages.cs.wisc.edu/~fischer/cs701.f05/code.positioning.pdf)Section 5 on procedure splitting is interesting one. It has nice examples ;) to help understand why HCS works.
    *   [Paper on hot cold splitting](https://www.cs.cmu.edu/afs/cs/academic/class/15745-s07/www/papers/p80-cohn.pdf) The paper provides some details on one approach to split functions. This is helpful to get a different perspective and may help get new ideas.
*   [Video and slides of the presentation](https://llvm.org/devmtg/2019-10/talk-abstracts.html#tech8)

**Expected results:**

*   Improve Hot Cold Splitting to detect and outline cold blocks from program via static analysis or profile information. Use appropriate cost model to weigh benefit of HCS. In case compile time overhead becomes quadratic, come up with a cost model to detect when quadratic behavior gets triggered and bail out based on a compiler flag.

**Confirmed Mentors:** Aditya Kumar (hiraditya on IRC and phabricator)

**Desirable skills:** Course on compiler design, SSA Representation, Intermediate knowledge of C++, Familiarity with LLVM Core.

<!-- *********************************************************************** -->

### Advanced Heuristics for Ordering Compiler Optimization Passes

<!-- *********************************************************************** -->

**Description of the project:** Selecting optimization passes for given application is very important but non-trivial problem because of the huge size of the compiler transformation space (incl. pass ordering). While the existing heuristics can provide high performance code for certain applications, they cannot easily benefit a wide range of application codes. The goal of the project is to learn the interplay between LLVM transformation passes and code structures, then improve the existing heuristics (or replace the heuristics with machine learning-based models) so that the LLVM compiler can provide a superior order of the passes customized per application.

**Expected results (possibilities):**

*   Insights about (implicit) dependences between existing passes.
*   New pass pipelines (think -O3a, -O3b, ...) selectable by the user that tend to perform substantially better on certain kinds of programs.
*   An improved LLVM pass heuristic or new machine learning-based models that can select the best order for LLVM transformation passes based on code structures.

**Preparation resources:**

*   HERCULES: Strong Patterns towards More Intelligent Predictive Modeling, Eunjung Park; Christos Kartsaklis; John Cavazos, IEEE ICPP’14 https://ieeexplore.ieee.org/abstract/document/6957226
*   Predictive Modeling in a Polyhedral Optimization Space, Eunjung Park, John Cavazos, Louis-Noël Pouchet, Cédric Bastoul, Albert Cohen & P. Sadayappan, IJPP’13 https://link.springer.com/article/10.1007/s10766-013-0241-1
*   Machine Learning in Compiler Optimization, Zheng Wang and Michael O’Boyle, IEEE Magazine 2018. https://ieeexplore.ieee.org/document/8357388

**Confirmed Mentors:** EJ Park, Giorgis Georgakoudis, Johannes Doerfert

**Desirable skills:** C++, Python, experience with LLVM and learning-based prediction preferable.

<!-- *********************************************************************** -->

### Machine learning and compiler optimizations: using inter-procedural analysis to select optimizations

<!-- *********************************************************************** -->

**Description of the project:** Current machine learning models for compiler optimization select the best optimization strategies for functions based on isolated per function analysis. In this approach, the constructed models are not aware of any relationships with other functions around it (callers or callees) which can be helpful to decide the best optimization strategies for each function. In this project, we want to explore the SCC (Strongly Connected Components) call graph to add inter-procedural features in constructing machine learning-based models to find the best optimization strategies per function. Moreover, we want to explore the case that it is helpful to group strongly related functions together and optimize them as a group, instead of per function.

**Expected results (possibilities):**

*   Improved heuristics for existing (inter-procedural) passes, e.g. to weight inlining versus function cloning based on code features.
*   Machine learning models to select the best optimizations using code features and inter-procedural analysis. This model can be used for functions in isolation or groups of functions, e.g., CGSCCs.

**Preparation resources:**

*   HERCULES: Strong Patterns towards More Intelligent Predictive Modeling, Eunjung Park; Christos Kartsaklis; John Cavazos, IEEE ICPP’14 https://ieeexplore.ieee.org/abstract/document/6957226
*   Predictive Modeling in a Polyhedral Optimization Space, Eunjung Park, John Cavazos, Louis-Noël Pouchet, Cédric Bastoul, Albert Cohen & P. Sadayappan, IJPP’13 https://link.springer.com/article/10.1007/s10766-013-0241-1
*   Machine Learning in Compiler Optimization, Zheng Wang and Michael O’Boyle, IEEE Magazine 2018. https://ieeexplore.ieee.org/document/8357388

**Confirmed Mentors:** EJ Park, Giorgis Georgakoudis, Johannes Doerfert

**Desirable skills:** C++, Python, experience with LLVM and learning-based prediction preferable.

<!-- *********************************************************************** -->

<!-- *********************************************************************** -->

**Description of the project:** There is currently no easy way to use the result of PostDominatorTreeAnalysis in a loop pass, as PostDominatorTreeAnalysis is a function analysis, and it is not included in LoopStandardAnalysisResults. If one adds PostDominatorTreeAnalysis in LoopStandardAnalysisResults, then all loop passes need to preserve it, meaning that all loop passes need to make sure the result is up to date. In this project, we want to modify some commonly used utilities to generate a list of updates, which can be consume by different updaters, e.g. DomTreeUpdater to update DominatorTree and PostDominatorTree, and MSSAU to update MemorySSA, etc, instead of only updating the DominatorTree. In additional, we want to change existing loop passes to preserve the PostDominatorTree. Finally, adding PostDominatorTree in LoopStandardAnalysisResults.

**Expected results (possibilities):** PostDominatorTree added in LoopStandardAnalysisResults, and can be used by loop passes. More common utilities change to generate list of updates to be easily obtained by different updaters.

**Confirmed Mentors:** Whitney Tsang, Ettore Tiotto, Bardia Mahjour

**Desirable skills:** Intermediate knowledge of C++, self-motivation.

**Preparation resources:**[](https://reviews.llvm.org/rL336163)[](http://llvm.org/doxygen/classllvm_1_1DomTreeUpdater.html)[](https://llvm.org/doxygen/classllvm_1_1PostDominatorTreeAnalysis.html)[](http://llvm.org/doxygen/structllvm_1_1LoopStandardAnalysisResults.html)

<!-- *********************************************************************** -->

### Create LoopNest Pass

<!-- *********************************************************************** -->

**Description of the project:** Currently if you want to write a pass that works on a loop nest, you have to pick from either a function pass or a loop pass. If you chose to write it as a function pass, then you lose the ability to add loops dynamically back to the pipeline. If you decide to write it as a loop pass, then you are wasting compile time to traverse to your pass and return right away when the given loop is not the outermost loop. In this project, we want to create a LoopNestPass, where transformations intended for loop nest can inherit from it, and have the same ability as the LoopPass to dynamically add loops to the pipeline. In addition, create all the adaptors requires to add loop nest passes at different points of the pass builder.

**Expected results (possibilities):** Transformations/Analyses can be written as LoopNestPass, without compromising compile time or usability.

**Confirmed Mentors:** Whitney Tsang, Ettore Tiotto

**Desirable skills:** Intermediate knowledge of C++, self-motivation.

**Preparation resources:** [https://reviews.llvm.org/D68789](https://reviews.llvm.org/D68789) [https://llvm.org/doxygen/classllvm\_1\_1PassBuilder.html](https://llvm.org/doxygen/classllvm_1_1PassBuilder.html)

<!-- *********************************************************************** -->

### Instruction properties dumper and checker

<!-- *********************************************************************** -->

**Description of the project:** TableGen is flexible and allow the end-user to define and set common properties of records (instructions). Every target has dozens or hundreds of such instruction properties. As target code evolve, the td files become more and more complicated, it become harder to see whether the setting of some properties is necessary, even correct or not. eg: whether hasSideEffects property is correctly set on all instructions? One can manually search through the TableGen-generated files; or write some script to run TableGen and matching the output for some specific properties, but a standalone utility that can dump and check instruction properties systematically (eg: also allow target to define some verification rules) might be better from a build-process-management standpoint. This can help to find quite some hidden bugs and hence improve the overall codegen code quality. In addition, the utility can be used to write regression tests for instruction properties, which will increase the quality and precision of LLVM's regression tests.

**Expected results (possibilities):** A standalone llvm tool or utility that can dump and check instruction properties systematically

**Confirmed Mentors:** Hal Finkel, Jinsong Ji , Qingshan Zhang

**Desirable skills:** Intermediate knowledge of C++, self-motivation.

<!-- *********************************************************************** -->

### Unify ways to move code or check if code is safe to be moved

<!-- *********************************************************************** -->

**Description of the project:** Determining whether it is safe to move code around is implemented in several transformations in LLVM (e.g. canSinkOrHoistInst in LICM, or makeLoopInvariant in Loop). Each of these implementations may return different results for a given query, making code motion safety checks inconsistent and duplicated. On the other hand, the mechanism for doing the actual code motion is also different in each transformation. Code duplication causes maintenance problems and increases the time taken to write new transformation. In this project, we want to first identify all the existing ways in loop transformations (could be function or loop pass) to check if code is safe to move, and to move code, and create a standardize way to do so.

**Expected results (possibilities):** A standardize/superset of all the existing ways in loop transformations of checking if code is safe to be moved and to move code

**Confirmed Mentors:** Whitney Tsang, Ettore Tiotto, Bardia Mahjour

**Desirable skills:** Intermediate knowledge of C++, self-motivation.

**Preparation resources:**[](https://github.com/llvm/llvm-project/blob/master/llvm/include/llvm/Transforms/Utils/CodeMoverUtils.h)[](https://llvm.org/doxygen/LICM_8cpp_source.html)[](https://llvm.org/doxygen/classllvm_1_1Loop.html)

<!-- *********************************************************************** -->

## MLIR

<!-- *********************************************************************** -->

All the items in the list of [open projects](https://mlir.llvm.org/getting_started/openprojects/) are opened to GSOC. Feel free to propose your own ideas as well on [Discourse](https://llvm.discourse.group/c/llvm-project/mlir).

<!-- *********************************************************************** -->

### Find null smart pointer dereferences with the Static Analyzer

<!-- *********************************************************************** -->

**Description of the project:** The Clang Static Analyzer already knows how to prevent crashes caused by null pointer dereference in arbitrary code, however it often "gives up" when the code is too complicated. In particular, implementation details of C++ standard classes, even simple ones such as smart pointers or optionals, may be too convoluted for the Analyzer to fully understand. Moreover, the exact behavior depends on which implementation of the Standard Library is used (e.g., GNU libstdc++ or LLVM's own libc++).

We can enable the Analyzer to find more bugs in modern C++ code by teaching it explicitly about the behavior of C++ standard classes, and therefore skipping the whole process in which the Analyzer tries to understand all the implementation details on its own. For example, we could teach it that a default-constructed smart pointer is null, and any attempt to dereference it would result in a crash. The project would therefore consist in manually providing implementations for various methods of standard classes.

**Expected results:** We want the Static Analyzer to emit warnings when a null smart pointer dereference would occur in the code. For example:

```
#include &lt;memory&gt;

    int foo(bool flag) {
      std::unique_ptr&lt;int&gt; x;  // note: Default constructor produces a null unique pointer;

      if (flag)                // note: Assuming 'flag' is false;
        return 0;              // note: Taking false branch

      return *x;               // warning: Dereferenced smart pointer 'x' is null.
    }
```

We should be able to cover at least one class fully, for example, std::unique\_ptr, and then see if we can generalize our results to other classes, such as std::shared\_ptr or the C++17 std::optional.

**Confirmed Mentor:** Artem Dergachev, Gábor Horváth

**Desirable skills:** Intermediate knowledge of C++.

<!-- *********************************************************************** -->

## LLDB

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Support autosuggestions in LLDB's command line

<!-- *********************************************************************** -->

**Description of the project:** LLDB's command line offers several convenience features that are inspired by features of UNIX shells such as tab completions or a command history. One feature that is not implemented yet are 'autosuggestions'. These are suggestions for possible commands that the user might want to type, but unlike tab completions they are displayed directly behind the cursor while the user is typing a command. A good demonstration how this could look like are the autosuggestions implemented in [fish shell](https://fishshell.com).

This project is about implementing autosuggestions in LLDB's editline-based command shell.

**Confirmed Mentor:** [Jonas Devlieghere and Raphael Isemann](mailto:teemperor@gmail.com,jonas@devlieghere.com?subject=[GSoC]%20Autosuggestions)

**Desirable skills:** Intermediate knowledge of C++.

<!-- *********************************************************************** -->

### Implement the missing tab completions for LLDB's command line

<!-- *********************************************************************** -->

**Description of the project:** LLDB's command line offers several convenience features that are inspired by features of UNIX shells such as tab completions for commands. These tab completions are implemented by a completion engine that is not only used by the command line interface of LLDB, but also by graphical interfaces for LLDB such as IDEs. While the tab completions in LLDB are really useful, they are currently not implemented for all commands and their respective arguments. This project is about implementing the remaining completions for the commands in LLDB which will greatly improve the user experience of LLDB. Improving existing completions is also part of the project. Note that the completions are not static list of strings but often require inspecting and understanding the internal state of LLDB. As LLDB commands and their tab completions cover all aspects of LLDB, this project offers a great way to get an overview of all the functionality in LLDB.

**Confirmed Mentor:**[Raphael Isemann](mailto:teemperor@gmail.com?subject=[GSoC]%20Completions)

**Desirable skills:** Intermediate knowledge of C++.

<!-- *********************************************************************** -->

### Reimplement LLDB's command-line commands using the public SB API.

<!-- *********************************************************************** -->

**Description of the project:** Just as LLVM is a library to build compilers, LLDB is a library to build debuggers. LLDB vends a stable, public SB API. Due to historic reasons the LLDB command line interface is currently implemented on top of LLDB's private API and it duplicates a lot of functionality that is already implemented in the public API. Rewriting LLDB's command line interface on top of the public API would simplify the implementation, eliminate duplicate code, and most importantly reduce the testing surface.

This work will also provide an opportunity to clean up the SB API of commands that have accrued too many overloads over time and convert them to make use of option classes to both gather up all the variants and also future-proof the APIs.

**Confirmed Mentor:** Adrian Prantl and Jim Ingham

**Desirable skills:** Intermediate knowledge of C++.

<!-- *********************************************************************** -->

### Add support for batch-testing to the LLDB testsuite.

<!-- *********************************************************************** -->

**Description of the project:** One of the tensions in the testsuite is that spinning up a process and getting it to some point is not a cheap operation, so you'd like to do a bunch of tests when you get there. But the current testsuite bails at the first failure, so you don't want to do many tests since the failure of one fails all the others. On the other hand, there are some individual test assertions where the failure of the assertion *should* cause the whole test to fail. For example, if you fail to stop at a breakpoint where you want to check some variable values, then the whole test should fail. But if your test then wants to check the value of five independent locals, it should be able to do all five, and then report how many of the five variable assertions failed. We could do this by adding *Start* and *End* markers for a batch of tests, do all the tests in the batch without failing the whole test, and then report the error and fail the whole test if appropriate. There might also be a nice way to do this in Python using scoped objects for the test sections.

**Confirmed Mentor:** Jim Ingham

**Desirable skills:** Intermediate knowledge of Python.

<!-- *********************************************************************** -->

# Google Summer of Code 2019

<!-- *********************************************************************** -->

Google Summer of Code 2019 contributed a lot to the LLVM project. For the list of accepted and completed projects, please take a look into Google Summer of Code [website.](https://summerofcode.withgoogle.com/archive/2019/organizations/5682474363912192/)

<!-- *********************************************************************** -->

## LLVM

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Debug Info should have no effect on codegen

<!-- *********************************************************************** -->

**Description of the project:** Adding Debug Info (compiling with \`clang -g\`) shouldn't change the generated code at all. Unfortunately we have bugs. These are usually not too hard to fix and a good way to discover new part of the codebase! We suggest building object files both ways and disassembling the text sections, which will give cleaner diffs than comparing .s files.

**Expected results:** Reduced test cases, bug reports with analysis (e.g., which pass is responsible), possibly patches.

**Confirmed Mentor:** Paul Robinson

**Desirable skills:** Intermediate knowledge of C++, some familiarity with x86 or ARM instruction set.

<!-- *********************************************************************** -->

## Clang

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

### Implement an ASTImporter fuzzer

<!-- *********************************************************************** -->

**Description of the project:** Clang contains an ASTImporter which allows moving declarations and statements from one Clang AST to another. This is for example used for static analysis across translation units and in LLDB's expression evaluator.

The current ASTImporter works as intended when moving simple C code from one AST to another. However, more complicated declarations such as C++'s OOP features and templates are not fully implemented and can cause crashes or invalid AST nodes. The bug reports related to these crashes are often filed against LLDB's expression evaluator and are rarely submited with a minimal reproducer. This makes improving ASTImporter a time-consuming and tedious task.

This project is about writing a fuzzer to proactively discover these ASTImporter bugs and provide minimal reproducers which make understanding and fixing the underlying bug easier.

A possible implementation of such a fuzzer and driver could look like this:

*   Generate some source code that can be imported (either fully randomly or based on existing source code from a user-given code corpus).
*   Import randomly a few declarations from this AST. The AST in which they are imported to can already be populated with declarations.
*   Run Clang's code generator over our imported AST.
*   If we hit an assert during the import or CodeGen steps we probably found an ASTImporter bug.
*   The fuzzer driver should now reduce the size of the source code until it is as small as possible and still reproduces the crash (e.g. by running Creduce with an automatically generated test script).
*   The reproducer should now be stored in a format so that it can just be copied into Clang's regression test suite for the ASTImporter (see the [clang/test/Import/](https://github.com/llvm/llvm-project/tree/master/clang/test/Import) directory). The reproducer must still reproduce the found bug when run as part of the test suite.

This is just one possible approach and students are welcome to submit their own ideas on how the fuzzer should operate. Approaches that allow to automatically verify more aspects of the imported AST (e.g. the source locations of AST nodes, size of RecordDecls) are encouraged. The fuzzer and driver should be implemented in C++ and/or Python.

**Confirmed Mentor:** Raphael Isemann, Shafik Yaghmour

**Desirable skills:** Intermediate knowledge of C++.

<!-- *********************************************************************** -->

### Improve shell autocompletion for Clang

<!-- *********************************************************************** -->

**Description of the project:** Clang has a newly implemented autocompletion feature which details can be found at [LLVM blog](http://blog.llvm.org/2017/09/clang-bash-better-auto-completion-is.html). We would like to improve this by adding more flags to autocompletion, supporting more shells (currently it supports only bash) and exporting this feature to other projects such as llvm-opt. Accepted student will be working on Clang Driver, LLVM Options and shell scripts.

**Expected Results:** Autocompletion working on bash and zsh, support llvm-opt options.

**Confirmed Mentor:** Yuka Takahashi and Vassil Vassilev

**Desirable skills:** Intermediate knowledge of C++ and shell scripting

<!-- *********************************************************************** -->

# Google Summer of Code 2018

<!-- *********************************************************************** -->

Google Summer of Code 2018 contributed a lot to the LLVM project. For the list of accepted and completed projects, please take a look into Google Summer of Code [website.](https://summerofcode.withgoogle.com/archive/2018/organizations/5263452624912384/)

<!-- *********************************************************************** -->

# Google Summer of Code 2017

<!-- *********************************************************************** -->

Google Summer of Code 2017 contributed a lot to the LLVM project. For the list of accepted and completed projects, please take a look into Google Summer of Code [website.](https://summerofcode.withgoogle.com/archive/2017/organizations/6215410651234304/)

<!-- *********************************************************************** -->

* * *
