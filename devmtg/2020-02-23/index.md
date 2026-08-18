---
layout: "default.html"
permalink: "devmtg/2020-02-23/index.html"
---
# Fourth LLVM Performance Workshop at CGO

An LLVM Performance Workshop will be held at CGO 2020. The workshop is co-located with CC, HPCA, and PPoPP. It takes place at [Hilton San Diego Resort and Spa](https://cgo-conference.github.io/cgo2020/venue/) in San Diego, CA. If you are interested in attending the workshop, please register at the [CGO website.](https://cgo-conference.github.io/cgo2020/)

<div style="float: left; width: 68%">

<div style="width: 100%">

1.  [Preliminary Schedule](#schedule)
2.  [Registration](#register)
3.  [Contact](#contact)
4.  [About](#about)

*   **Conference Dates**: Sunday February 23rd, 2020
*   **Location**: Hilton San Diego Resort and Spa, San Diego, CA, USA
*   **Conference Room**: Portofino

</div>

# Preliminary Schedule

| **Time** | **Speaker** | **Title** |   |
| --- | --- | --- | --- |
| 9:15-9:50 | Simon Moll | An Overview of the Region Vectorizer | [\[Abstract\]](#sm) |
| 9:50-10:15 | Prithayan Barua | Optimized Memory Movement for OpenMp target offloading | [\[Abstract\]](#pb) |
| 10:15-10:30 |   | Break |
| 10:30-11:05 | Utpal Bora, Santanu Das, Pankaj Kureja, Saurabh Joshi, Ramakrishna Upadrasta and Sanjay Rajopadhye | LLOV: A Fast Static Data-Race Checker for OpenMP Programs | [\[Abstract\]](#ub) | \[ [Slides](https://llvm.org/devmtg/2020-02-23/slides/Utpal-LLOV.pdf) \] |
| 11:05-11:30 | Johannes Doerfert | OpenMP in LLVM --- A Design and Implementation Overview | [\[Abstract\]](#jd1) |
| 11:30-12:00 | \- | Discussion Round --- Participating in LLVM - GSoC and other opportunities |  |
| 12:00-13:30 |   | Lunch |
| 13:30-14:30 | William Moses and Johannes Doerfert | Keynote: "Header Time Optimization": Cross-Translation Unit Optimization via Annotated Headers | [\[Abstract\]](#wm) |
| 14:30-15:00 | Shilei Tian, Johannes Doerfert and Barbara Chapman | Asynchronous OpenMP Offloading on NVIDIA GPUs | [\[Abstract\]](#st) | \[ [Slides](https://llvm.org/devmtg/2020-02-23/slides/Shilei-multistreams.pdf) \] |
| 15:00-15:15 |   | Break |
| 15:15-15:45 | Kyungwoo Lee and Nikolai Tillmann | Global Machine Outliner for ThinLTO | [\[Abstract\]](#kl) | \[ [Slides](https://llvm.org/devmtg/2020-02-23/slides/Kyungwoo-GlobalMachineOutlinerForThinLTO.pdf) \] |
| 15:45-16:15 | Aditya Kumar, Ian Levesque, Sam Todd | Cheap function entry instrumentation to collect runtime metrics | [\[Abstract\]](#ak) | \[ [Slides](https://llvm.org/devmtg/2020-02-23/slides/Aditya-FunctionEntryInstrumentationLLVM.pdf) \] |
| 16:15-16:45 | Johannes Doerfert | Interactive introduction: The Attributor: A Versatile Inter-procedural Fixpoint Iteration Framework |   |
| 16:45- |   | Open Discussion Round |

# Abstracts

*   **Simon Mall:** An Overview of the Region Vectorizer

    The Region Vectorizer (RV) is a data-parallel vecorizer for LLVM IR. This talk gives an overview of the RV vectorization system, its main features and future directions.

*   **Prithayan Barua:** Optimized Memory Movement for OpenMp target offloading

    OpenMP offers directives for offloading computations from CPU hosts to accelerator devices such as GPUs. A key underlying challenge is in efficiently managing the movement of data across the host and the accelerator. Since the cost of data movement is high due to data volume and the delay of interconnection, how to efficiently manage the data movement operations to avoid redundancy is the challenge faced by the compilers. In this talk, we introduce an optimization framework that runs analysis and transformation on a novel intermediate representation: location-aware heap SSA (LASSA) that models the memory accesses and data movement across tasks running on different devices that have private storage. This framework casts the problem of removal of redundant data movements into a partial redundancy elimination (PRE) problem and applies the lazy code motion technique to optimize it. This is a work in progress, and we have a prototype LLVM implementation. We evaluated it with 10 benchmarks and got a Geo-mean speedup of 2.3X, and saved a Geo-mean 3480 MB of redundant data transfers.

*   **Utpal Bora, Santanu Das, Pankaj Kureja, Saurabh Joshi, Ramakrishna Upadrasta and Sanjay Rajopadhye:** LLOV: A Fast Static Data-Race Checker for OpenMP Programs

    In the era of Exascale computing, writing efficient parallel programs is indispensable and at the same time, writing sound parallel programs is highly difficult. While parallel programming is easier with frameworks such as OpenMP, the possibility of data races in these programs still persists. In this paper, we propose a fast, lightweight, language agnostic, and static data race checker for OpenMP programs based on the LLVM compiler framework. We compare our tool with other state-of-the-art data race checkers on a variety of well-established benchmarks. We show that the precision, accuracy, and the F1 score of our tool is comparable to other checkers while being orders of magnitude faster. To the best of our knowledge, this work is the only tool among the state-of-the-art data race checkers that can verify a FORTRAN program to be data race free.

*   **Johannes Doerfert:** OpenMP in LLVM --- A Design and Implementation Overview

    OpenMP support in LLVM is changing, fast and in many places. This talk will provide an overview of the changes, their status and goals, the rational behind them, as well as ways to contribute. A summary of the content is given below. Please note that the talk presents the work done by many people across the entire community. Due to relative frequent releases of new features, OpenMP was always a moving target when it comes to implementation. In addition, we currently working on increasing the hardware and language support: The second offloading target, namely AMDGPU, is advancing rapidly and with it the need to redesign/generalize the offloading code path in Clang and in the OpenMP device runtime library. On the language side, Flang, the Fortran compiler front-end, will require full support for OpenMP similar to the current implementation in Clang. To provide this support in a maintainable way, the code generation is transitioning out of Clang into LLVM-Core. In tandem with these changes, optimizations for OpenMP programs are developed. Utilizing abstract call sites, the Attributor performs scalar optimizations, e.g., constant propagation, across the boundaries of outlined OpenMP regions. Finally, explicit OpenMP aware optimizations are developed as part of the OpenMPOpt pass.

*   **William Moses and Johannes Doerfert:** Keynote II: "Header Time Optimization": Cross-Translation Unit Optimization via Annotated Headers

    LLVM automatically derives facts that are only used while the respective translation unit, or LLVM module, is processed (i.e. constant function, error-throwing, etc). This is true both in standard compilation but also link-time-optimization (LTO) in which the module is (partially) merged with others in the same project at link time. LTO is able to take advantage of this to optimize functions calls to outside the translation unit. However, LTO doesn't solve the problem for two reasons of practicality: LTO comes with a nontrivial compile-time investment; and many libraries upon which a program could depend, do not ship with LTO information, simply headers and binaries. In this extended abstract, we solve the problem by generating annotated versions of the source code that also include this derived information. Such an approach has the benefits of both worlds: allowing optimizations previously limited to LTO without running LTO and only requiring C/C++-compatible headers. Our modified Clang understands three custom attributes that encode arbitrary LLVM-IR attributes and it can emit C/C++-compatible headers with the aforementioned attribute embedded based on the information available in the LLVM-IR. We test the approach experimentally on the LLVM multisource application test suite and find that annotated headers find up to a 30\\% speedup, and represent half of the speedups found by full LTO.

*   **Shilei Tian, Johannes Doerfert and Barbara Chapman:** Asynchronous OpenMP Offloading on NVIDIA GPUs

    In the current implementation of LLVM OpenMP offloading, the runtime submits all kernels to the default stream and blocks the issuing thread until device execution is done. Since the default stream serializes all submitted kernel and lunches them sequentially, even in parallel issued kernels are not executed on a device concurrently. This is problematic especially if single kernels do not utilize the entire device consistently, a situation not uncommon on modern GPUs. In this work, we present a design and prototype to use multiple streams to offload OpenMP target regions in order for concurrent execution on the device. Our prototype infrastructure shows speedups of up to 1.33x on micro benchmarks and we expect further improvements from hardware-based dependence resolution.

*   **Kyungwoo Lee and Nikolai Tillmann:** Global Machine Outliner for ThinLTO

    The existing machine-outliner in LLVM already provides a lot of value to reduce code size but also has significant shortcomings: In the context of ThinLTO, the machine-outliner operates on only one module at a time, and doesn’t reap outlining opportunities that only pay off when considering all modules together. Furthermore, identical outlined functions in different modules do not get deduplicated because of misaligned names. We propose to address these shortcomings: We run machine-level codegen (but not the IR-level optimizations) twice: The first time, the purpose is purely to gather statistics on outlining opportunities. The second time, the gathered knowledge is applied during machine outlining to do more. The core idea is to track information about outlined instruction sequences via a new kind of stable machine instruction hashes that are meaningful and quite exact across modules. In this way, the machine-outliner may outline many identical functions in separate modules. Furthermore, we introduce unique names for outlined functions across modules, and then enable link-once ODR to let the linker deduplicate functions. We also observed that frame-layout code tends to not get outlined: the generated frame-layout code tends to be irregular as it is optimized for performance, using the return address register in unique ways which are not easily outlinable. We change the machine-specific layout code generation to be homogenous, and we synthesize outlined prologue and epilogue helper functions on-demand in way that can be fitted to actually occurring frequent patterns across all modules. Again, we can gather statistics in the first codegen, and apply them in the second one. Fortunately, it turns out that the time spent in codegen is not dominating the overall compilation, and our approach to run codegen twice represents an acceptable cost. Also, codegen tends to be very deterministic, and the information gathered during the first codegen is highly applicable to the second one. In any case, our optimizations are sound. In our experience, this often significantly increases the effectiveness of outlining with ThinLTO in terms of size and even performance of the generated code. We have observed an improvement in the code size reduction of outlining by a factor of two in some large applications.

*   **Aditya Kumar, Ian Levesque, Sam Todd:** Cheap function entry instrumentation to collect runtime metrics

    Compiler instrumentation technique that is extremely cheap, lock free (in some cases) and extensible. This can be used for dead code detection, detecting null pointers, value profiling of function arguments etc.

# Contact

In case of any queries please reach out to the workshop organizers: Johannes Doerfert (jdoerfert at anl.gov), Sebastian Pop(spop at amazon.com), Aditya Kumar (aditya7 at fb.com)

# About

What can you can expect at an LLVM Developers' Meeting?

#### Panels

Panel sessions are guided discussions about a specific topic. The panel consists of ~3 developers who discuss a topic through prepared questions from a moderator. The audience is also given the opportunity to ask questions of the panel.

#### Birds of a Feather (BoF)

A BoF session, an informal meeting at conferences, where the attendees group together based on a shared interest and carry out discussions without any pre-planned agenda.

#### Technical Talks

These 20-30 minute talks cover all topics from core infrastructure talks, to project's using LLVM's infrastructure. Attendees will take away technical information that could be pertinent to their project or general interest.

#### Tutorials

Tutorials are 50-60 minute sessions that dive down deep into a technical topic. Expect in depth examples and explanations. <!-- *********************************************************************** -->

* * *

</div>
