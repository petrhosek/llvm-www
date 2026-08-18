---
layout: "default.html"
permalink: "devmtg/2014-02/index.html"
---
# LLVM devroom at FOSDEM

1.  [Call for "Papers"](#call)
2.  [Logistics](#logistics)
3.  [Registration](#register)

*   **What**: LLVM at FOSDEM.
*   **When**: February 2, 2014
*   **Where**: Brussels, Belgium

At FOSDEM 2014, LLVM will for the first time participate with a dedicated devroom. Complementing the upcoming Euro LLVM 2014, the devroom at FOSDEM provides a great opportunity for core LLVM developers and the wider open source community to get together to connect and discuss.

As possibly the largest European Open Source Conference, FOSDEM takes place in Brussels and attracts with more than 400 lectures every year over 5000 hackers - many core contributors of the worlds leading open source projects.

We also invite you to sign up for the [official Developer Meeting mailing list](http://lists.llvm.org/mailman/listinfo/llvm-devmeeting) to be kept informed of updates concerning the meeting.

# Schedule

| Talk | Slides/videos |
| --- | --- |
| **Welcome**<br>Tobias Grosser & Sylvestre Ledru |  |
| [**Clang: Re-inventing the Compiler**](#talk1)<br>Alp Toker | [Slides](slides/toker-clang-reinventing.pdf) |
| [**Auto-Vectorization in LLVM**](#talk2)<br>Renato Golin | [Slides](slides/golin-AutoVectorizationLLVM.pdf) |
| [**The Avatar project - improving embedded security with S2E, KLEE and Qemu**](#talk3)<br>Luca Bruno | [Slides](slides/bruno-avatar.pdf) |
| [**The LLVMLinux project**](#talk4)<br>Jan-Simon Möller | [Slides](slides/moller-llvmlinux.pdf) |
| [**How to contribute to LLVM**](#talk5)<br>Sylvestre Ledru | [Slides](slides/ledru-how-to-contribute-to-llvm.pdf) |
| [**Two uses cases for the clang C++ parser: Online Code Browser and Qt moc Replacement.**](#talk6)<br>Olivier Goffart |  |
| [**Statically compiling Ruby with LLVM**](#talk7)<br>Laurent Sansonetti |  |
| [**LDC - the LLVM-based D compiler**](#talk8)<br>Kai Nacke |  |
| [**Introduction on KLEE**](#talk9)<br>Daniel Liew |  |
| [**An approach for energy consumption analysis of programs using LLVM**](#talk10)<br>Neville Grech |  |
| [**High Level Loop Optimizations in LLVM**](#talk11)<br>Tobias Grosser |  |

# Talk Abstracts

**Clang: Re-inventing the Compiler**  
*Alp Toker*  
The LLVM clang C++ compiler has exceeded all expectations in the last year, gaining unprecedented new features that let you explore, rewrite and rediscover your source code.  
This is a talk about the human story of a compiler: What can we achieve going beyond compilation? Why are we compelled to invent a better wheel? How can we make everyday life better for coders, and could the compiler itself become an instrument for wider social change?  
Developed by an eclectic team of academics, supercomputer hobbyists and vendors including Apple and Google, the LLVM project has proven itself as a hotbed of innovation leading the renaissance in C-family programming languages, recently receiving the coveted ACM Software System Award.  
Whether you're a kernel hacker, app developer or front-end designer, clang is different to other compilers, it's coming to a machine near you in 2014 and may well impact your work: Here's what you need to know.

**Auto-Vectorization in LLVM**  
*Renato Golin*  
Auto-Vectorization has come a long way since the early vector-processing CPUs, and compilers generally take a long time to implement it, prioritizing other more generic features instead. But with all recent high-end chips containing some form of SIMD operations, auto-vectorization became a necessary feature on any modern compiler. LLVM was perhaps the latest of the big compilers to have a decent vectorization engine, but it has grown considerably for the last year, and the investment on SIMD code generation will not diminish. This presentation outlines the past implementations, what we currently have available and peeks into the engineering pipeline to see what else we are working on.

**The Avatar project - improving embedded security with S2E, KLEE and Qemu**  
*Luca Bruno*  
Avatar is a research framework that enables complex dynamic analysis of embedded devices by orchestrating the execution of an emulator together with the real hardware.  
It is built on top of S2E/Qemu, KLEE and LLVM and its main goal is to enable advanced security analysis of pristine ARM source-less firmware, eg. through dynamic tracing or symbolic execution.  
This talk will show the key-features of S2E in enabling runtime binary analysis (using Qemu virtualization and KLEE/LLVM symbolic execution) and how Avatar uses it to orchestrate analysis and execution at the emulator<->device edge.  
To address the growing concerns about the security of embedded systems, it is important to perform accurate analysis of firmware binaries, even when the source code or the hardware documentation are not available. Unlike static analysis, dynamic analysis relies on the ability to execute software in a controlled environment, which is however difficult due the lack of documentation and the large variety of subtly different hardware on the market.  
In this talk we present Avatar, a framework that enables such complex analysis of embedded devices. In particular we will introduce S2E, a C++ project which leverages several components to do binary emulation, including:

*   Qemu for machine virtualization
*   LLVM as the IR of choice
*   KLEE for symbolic execution of LLVM IR
*   S2E plugins for hooking into data and control flow

Then we show the Avatar framework, which acts as an analysis driver, context switcher and memory forwarder. Avatar is currently written in Python and on top of basic features, it includes several techniques to improve the system's performance as well as heuristics to help in vulnerability discovery.  
Both project are FLOSS. S2E is a research project from EPFL, while Avatar is under development at Eurecom.

**The LLVMLinux project**  
*Jan-Simon Möller*  
Jan-Simon Möller will introduce the audience to the LLVMLinux project which goal it is to compile the Linux Kernel with the compiler tools provided by the LLVM project (clang). He will talk about the steps needed to compile the Kernel itself, the issues found during this endeavour and the status of upstreaming patches to the Kernel and the LLVM project.

**How to contribute to LLVM**  
*Sylvestre Ledru*  
When starting to contribute to LLVM knowing the technical steps and especially the community habits can make the first (and upcoming) contribution a lot easier and the contribution process will become a more positive experience. This talk will discuss technical points such as your first patch into LLVM, how to get +w permissions, the various workflow, but also more soft skills such as 'how can I find a reviewer for my patch', 'should I review patches myself' or 'what is the right strategy to add a larger feature to LLVM'?

**Two uses cases for the clang C++ parser: Online Code Browser and Qt moc Replacement.**  
*Olivier Goffart*  
In this talk we will see how one can use the clang libraries to build two practical tools. The first tool is an online C/C++ online code browser that uses clang to parse the AST in order to provide information about each token and build a cross reference database. \[[http://code.woboq.org](http://code.woboq.org)\] The second tool is a replacement for Qt's moc (meta-object compiler) which is used by Qt to provide introspection and enable signals and slots and the QML language, both as a stand alone executable or as a clang plugin. [http://https://github.com/woboq/moc-ng](http://https://github.com/woboq/moc-ng)  
The talk goes over implementation details and challenges encountered while developing.

**Statically compiling Ruby with LLVM - ... or how RubyMotion works internally**  
*Laurent Sansonetti*  
RubyMotion is a commercial implementation of the Ruby language for iOS and OS X development. RubyMotion makes intensive use of LLVM in order to statically compile Ruby. In this session we will focus on how RubyMotion uses LLVM also a bit of history with the MacRuby project (which uses LLVM as a JIT).  
RubyMotion is a commercial implementation of the Ruby language for iOS and OS X development. The RubyMotion toolchain lets Ruby developers write full-fledged native applications for iPhone, iPad and the Mac. RubyMotion apps are statically compiled into optimized machine code.  
RubyMotion makes intensive use of LLVM in order to statically compile Ruby and target various architectures. In this session we will focus on how RubyMotion uses LLVM, the challenges that we had to solve in order to compile Ruby, some of the various codegen optimizations we implemented and how we integrate with profiling/debugging tools. We will also cover the mistakes we learned from the MacRuby project, which uses LLVM a bit differently.  
(This presentation will only focus on the internals of RubyMotion. We will not cover Ruby, RubyMotion or iOS/OS X development.)

**LDC - the LLVM-based D compiler**  
*Kai Nacke*  
D is a language with C-like syntax and static typing. It pragmatically combines efficiency, control, and modeling power, with safety and programmer productivity. Because of its features major companies start to adopt D.  
LDC is a fully open source, portable D compiler. It uses the frontend from the reference compiler combined with LLVM as backend to produce efficient native code. LDC targets x86/x86\_64 systems like Linux, OS X and Windows and also Linux/PPC64. Ports to other architectures like ARM are underway. Currently, LDC can be built with LLVM 3.1 and all later LLVM releases.  
In my talk, I introduce the overall architecture of LDC first. Using the frontend AST as starting point I show how types, statements and expression are mapped to LLVM IR and which LLVM features are required. Experiences with LLVM in general, porting to other LLVM backends than x86 and integrating features like the AddressSanitizer are highlighted. At last, areas of improvement for LLVM are shown from the perspective of a D compiler (ABI, vararg, exception handling).

**Introduction on Klee**  
*Daniel Liew*  

**An approach for energy consumption analysis of programs using LLVM**  
*Neville Grech*  
Energy models can be constructed by characterizing the energy consumed by executing each instruction in a processor's instruction set. This can be used to determine how much energy is required to execute a sequence of assembly instructions. However, statically analysing low level program structures is hard, and the gap between the high-level program structure and the low-level energy models needs to be bridged. We have developed a tool for performing a static analysis on the intermediate compiler representations of a program. Specifically, we target LLVM IR, a representation used by most modern compilers including Clang.  
One of the challenges in doing so is that of determining an energy cost of executing LLVM IR program segments, for which we have developed a mapping tool. This tool associates LLVM IR program segments with assembly program segments, producing a mapping. Mapping information is useful when performing an analysis at one layer using energy models defined at a lower layer. Essentially, this propagates the energy model defined at the instruction set level up to the LLVM IR level, at which the analysis is performed. When this is used with our analysis tool, we are able to infer energy formulae that characterize the energy consumption for a particular program. This approach can be applied to any languages targeting the LLVM toolchain or architectures supported by LLVM.  
Static energy estimation has applications in program optimization, and enables energy-aware software development.

**High Level Loop Optimizations in LLVM**  
*Tobias Grosser*  
For several important program classes (image processing, scientific computing, ...) High Level Loop Optimizations are essential to reach top performance. With Polly, we present a high-level loop optimization framework for LLVM, that provides a flexible infrastructure to develop and describe such high-level loop optimizations. We present Polly as a classical optimizer for a C compiler, but focus on its use as an infrastructure to develop optimizations for domain specific languages and specialized hardware such as GPUs. This talks gives an overview of the overall structure of Polly itself and also insights into the components and tools essential when working with Polly (isl, ppcg, islpy, islplot).

# Logistics

The mailing list [llvm-devroom@lists.fosdem.org](mailo:llvm-devroom@lists.fosdem.org) can be used to discuss issues of general interest related to the conference organization.

# Registration

FOSDEM does not require any registration and is free of charge. However, we advise to arrive early in the devroom in case of important crowd.

<!-- *********************************************************************** -->

* * *
