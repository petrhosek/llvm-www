---
layout: "default.html"
permalink: "devmtg/2013-04/index.html"
---
# 2013 European LLVM Conference

### **SPONSORED BY:** [ARM](http://www.arm.com/), [ENS](http://www.ens.fr/), [Google](http://www.google.com/), [IRILL](http://www.irill.org)/[INRIA](http://www.inria.fr), [Intel](http://www.intel.com), [Parrot](http://www.parrot.com), [QuIC](http://www.qualcomm.com/quicinc/), [Samsung](http://www.samsung.com)

1.  [Announcement](#announcements)
<!-- <li><a href="#callfor">Call for Speakers, Posters, Demos</a></li> -->2.  [Content](#content)
3.  [Questionnaire Results](#questionnaire)
4.  [Talk abstracts](#talkabstract)
5.  [Tutorial abstracts](#tutoabstract)
6.  [Poster abstracts](#posterabstract)
7.  [Lightning talk abstract](#ltalkabstract)

*   **What**: The third European LLVM meeting
*   **Why**: To get acquainted, learn how LLVM is used, and exchange ideas.
*   **When**: 29/30 April 2013
*   **Where**: Paris, France

## Announcement

The conference already took place. Here the original announcement:

"We are pleased to announce the third European LLVM conference on April 29-30 2013 in Paris, France. This will be a two day conference which aims to present the latest developments in the LLVM world and help strengthen the network of LLVM developers. The format will be similar to that of the previous meetings held in London but with more time for presentations and networking. The meeting is open to anyone whether from business or academia, professional or enthusiast and is not restricted to those from Europe - attendees from all regions are welcome."

The [After Conference Blog Post](http://blog.llvm.org/2013/05/eurollvm-2013-paris-france.html) gives an impression of the event.  

Videos are also available on the [IRILL website](http://www.irill.org/videos/euro-llvm-2013). <!-- <h2 id="callfor">Call for Speakers, Posters, Demos</h2> We invite academic, industrial and hobbyist speakers to present their work on developing or using LLVM, Clang, etc.  Proposals for technical presentations, posters, workshops, demonstrations and BoFs are welcome.  Material will be chosen to cover a broad spectrum of themes and topics at various depths, some technical deep-diving, some surface-scratching. <p>We are looking for: <ol> <li>Keynote speakers.</li> <li>Technical presentations (30 minutes plus questions and discussion) related to development of LLVM, Clang etc.</li> <li>Presentations relating to academic or commercial use of LLVM, Clang etc.</li> <li>Lightning talks (5 minutes, no questions, no discussion).</li> <li>Workshops and in-depth tutorials (1-2 hours - please specify in your submission).</li> </ol></p> <p>The deadline for receiving submissions is March 1st, 2013.  Speakers will be notified of acceptance or rejection by the 15th of March.  Proposals that are not sufficiently detailed (talks lacking a comprehensive abstract for example) are likely to be rejected.  Slides and posters must be in PDF format. Submissions should be done by email at <a href="mailto:euro-llvm-2013-technical-committee@googlegroups.com"> euro-llvm-2013-technical-committee@googlegroups.com</a>.</p> <p>Please note that presentation materials and videos for the technical sessions will be posted on llvm.org after the conference. We have reserved additional spots for speakers, such that they can attend the conference even though we have reached our registration limit.</p> <h3 id="submissions">Submission Style</h3> <p>We are looking for: <ul> <li>A title and an extended abstract, <i>OR</i></li> <li>A title, abstract and some slides</li> </ul> <p>Please make clear the status of the slides: Are they a skeleton of your presentation with the detail missing? Or, perhaps a section of detail that lacks introduction and conclusions? The more you can give us and tell us the easier it will be for us to be positive about your submission.</p> <p>For examples of abstracts and introductions please look at papers from any compiler conference such as Code Generation and Optimization. A typical abstract is from one paragraph to half of a column on a 2-column A4 page. A typical introduction is between 0.5 and 2 A4 pages. An A4 page would suffice for an extended abstract. The more slides you give us in near final form the less we need by way of abstract and introduction.</p> --> <!-- *********************************************************************** -->

## Content

### Keynotes

| Speaker | Subject | Media |
| --- | --- | --- |
| Chandler Carruth (Google) | [Optimization in LLVM - Numbers, A Case Study, and Looking Forward](#talk3) | [Video](https://youtu.be/hmTi_FDe9pY) |
| Jakob Olesen (Apple) | [How Computers Work](#talk7) | [Slides](olesen-slides.pdf), no video available |

### Talks

| Speaker | Subject | Media |
| --- | --- | --- |
| Andrey Bokhanko & Alexey Bataev (Intel) | [Towards OpenMP Support in LLVM](#talk2) | [Slides](bokhanko-bataev-slides.pdf), [Video](https://youtu.be/9SkYb8YWRA8) |
| Ahmed Bougacha | [Dagger: decompilation to LLVM IR](#talk1) | [Slides](bougacha-slides.pdf), [Video](https://youtu.be/JoOC3vqnh-s) |
| Eric Christopher (Google) | [Debug Info - Status and Directions](#talk5) | [Slides](christopher-slides.pdf), [Video](https://youtu.be/EpFel-1mpK0) |
| Daniel Jasper (Google) | [clang-format - Automatic formatting for C++](#talk4) | [Slides](jasper-slides.pdf), [Video](https://youtu.be/5eplO4qpxCY) |
| Olaf Krzikalla (TU Dresden) | [Performing Source-to-Source Transformations with Clang](#talk9) | [Slides](krzikalla-slides.pdf), [Video](https://youtu.be/IKDROD29Sz4) |
| Oleg Maslov (Intel) | [LLVM Interpreter, a key component in validation of OpenCL compilers](#talk10) | [Slides](maslov-slides.pdf), [Video](https://youtu.be/XPi-74rHo9U) |
| Simone Pellegrini (U Innsbruck) | [An experimental framework for Pragma Handling in Clang](#talk13) | [Slides](pellegrini-slides.pdf), [Video](https://youtu.be/wH4bP0p9qdc) |
| Michael Spencer (Sony) | [lld - Solving the Linking Performance Problem](#talk8) | [Slides](spencer-slides.pdf), [Video](https://youtu.be/ONGVraXbJOo) |
| Evgeniy Stepanov (Google) | [Run-time tracking of uninitialized data with MemorySanitizer](#talk6) | [Slides](stepanov-slides.pdf), [Video](https://youtu.be/2Y0T-1AB-gY) |
| Ulrich Weigand (IBM) | [LLVM on IBM POWER processors: a progress report](#talk14) | [Slides](weigand-slides.pdf), [Video](https://youtu.be/eSIk4FPH7O0) |

### Tutorials

| Speaker | Subject | Media |
| --- | --- | --- |
| Simon Cook (Embecosm) | [How to implement an LLVM Assembler - a tutorial](#talk12) | [Slides](cook-slides.pdf), [Video](https://youtu.be/caKpPIzqWig) |
| Manuel Klimek (Google) | [The Clang AST - a tutorial](#tuto1) | [Slides](klimek-slides.pdf), [Video](https://youtu.be/b8JTwPz5dSw) |

### [Lightning talks](#ltalkabstract)

| Speaker | Subject | Media |
| --- | --- | --- |
| Diana Chen | MCLinker: Design and Implementation of a Fragments-based Target-independent Linker | [Slides](chen-slides.pdf), [Video](https://youtu.be/gISMoK3fGFg) |
| Clemens Hammacher | Sambamba: A Runtime System for Online Adaptive Parallelization | [Slides](hammacher-slides.pdf), [Video](https://youtu.be/GclQAaP8J-0) |
| Ralf Karrenberg | Noise: A Clang Extension for User-Defined Optimization Strategies | [Slides](karrenberg-slides.pdf), [Video](https://youtu.be/zAUxHBs3iVs) |
| David Lacey | Integrating fine-grained timing constraints into LLVM | [Slides](lacey-slides.pdf), [Video](https://youtu.be/eA-tpkYpZR8) |
| Sylvestre Ledru | Rebuild of all Debian packages using Clang instead of gcc | [Slides](ledru-slides.pdf), [Video](https://youtu.be/IcLnlyyjY_M) |
| Diego Novillo | FDO-based whole program optimization in LLVM | [Slides](novillo-slides.pdf), [Video](https://youtu.be/vnL4rqE0XtQ) |
| Henning Thielemann | Efficient audio signal processing using LLVM and Haskell | [Slides](thielemann-slides.pdf), [Video](https://youtu.be/0KPuzXoAwfQ) |

### [Posters](#posterabstract)

| Presenter | Subject | Media |
| --- | --- | --- |
| Ryan Baird | Improving Machine Code Generation Quality by Interfacing VPO with LLVM | [Poster](baird-poster.pdf) |
| Victoria Caparros | Using the LLVM Interpreter to Quantify Applications Inherent Properties | [Poster](caparros-poster.pdf) |
| Diana Chen | MCLinker: Design and Implementation of a Fragments-based Target-independent Linker | [Poster](chen-poster.pdf) |
| Peter Conn | Code Editing in Local Style | [Poster](conn-poster.pdf) |
| Dustin Feld | ENHANCE - Enabling heterogeneous hardware acceleration using novel programming and scheduling models | [Poster](feld-poster.pdf) |
| Clemens Hammacher | Sambamba: A Runtime System for Online Adaptive Parallelization | [Poster](hammacher-poster.pdf) |
| Muhammad Hataba | OJIT: A novel secure remote execution technology by obfuscated Just-In-Time compilation | [Poster](hataba-poster.pdf) |
| Dávid Juhász | LLVM backend for TILE64 | [Poster](juhasz-poster.pdf) |
| Ralf Karrenberg | Noise: A Clang Extension for User-Defined Optimization Strategies | [Poster](karrenberg-poster.pdf) |
| Ayal Zaks | LLVM IR editor plugin for Eclipse | [Poster](zaks-poster.pdf) |

<!-- *********************************************************************** -->

## Questionnaire Results

At the end of the event we had 91 questionnaires returned and the results were pretty good. Below are some overall results, but each presenter will receive the results of their own talks by personal email.

Each question had a range of four possible results (excellent-poor, very useful-waste of time, etc), and below are the percentage of the results that were 1 or 2 (excellent+good, very useful+useful, etc). We're not considering "average" as a positive result, for obvious reasons.

At the end, there's a table with the percentages of a geometric mean of all talks and another for the lightning talks, so you can get a feel of the response without going in too much detail.

**Overall event questions**

| Question | % of positive results |
| --- | --- |
| Overall event | 98% |
|   |   |
| Venue Quality | 96% |
| Venue Food & Drinks | 77% |
| Venue Rooms & Equipment | 73% |
| Venue Location | 99% |
|   |   |
| Quality of Lectures/Papers | 100% |
| Quality of Tutorials | 93% |
| Lightning Talks & Posters | 94% |
|   |   |
| Overall networking usefulness | 94% |
| Created 5+ new connections | 65% |
| Reinforced 5+ existing connections | 44% |
|   |   |
| Dinner Cruise Overall | 100% |
| Dinner Cruise Food & Drinks | 100% |
| Dinner Cruise Location | 100% |

**Regarding the Content, they wanted:**

| Topic | More | Same | Less |
| --- | --- | --- | --- |
| Formal Presentations | 19% | 67% | 14% |
| Deeper, Specific Sessions | 42% | 39% | 19% |
| Technical (Soft. Eng.) Sessions | 43% | 48% | 9% |
| Narrowing Towards a Major Theme | 4% | 81% | 15% |

**Location and Transport**

Where should we hold EuroLLVM 2014?

*   **Paris** 18%
*   **London** 16%
*   **Any Major EU city** 66%

**Geometric Mean of All Talks**

| Question | % of positive results |
| --- | --- |
| Material clearly presented | 86% |
| Interesting topic to me | 84% |
| Too much knowledge required(\*) | 78% |
| Importance to the Community | 90% |
| Would like to hear more | 84% |

**Lightning Talks**

| Question | % of positive results |
| --- | --- |
| Material clearly presented | 90% |
| Interesting topic to me | 93% |
| Too much knowledge required(\*) | 93% |
| Importance the Community | 94% |
| Would like to hear more | 90% |

(\*) Positive results for this question are those that answered "disagree" and "strongly disagree", since we expected that the talks shouldn't required too much detailed knowledge to understand, specially from a crowd as specialized as ours.

<!-- *********************************************************************** -->

## Talk abstracts

**Dagger: decompilation to LLVM IR**  
*Ahmed Bougacha*  
Dagger is a decompilation framework based on LLVM. It enables existing backends to easily provide instruction-level semantics. These are then used to translate target instructions to an IR-like architecture, Mir (for micro-IR), and further to LLVM IR itself. Dagger also enables easy retargetability of several planned tools, like rewriters, static or dynamic binary translators (with valgrind-like instrumentation), and even simple instruction set emulators. The IR can also be transformed to do static analysis, or even, using a revived and improved C backend, full-blown decompilation.

**Towards OpenMP Support in LLVM**  
*Andrey Bokhanko & Alexey Bataev - Intel*  
In this talk we present our efforts and plans for OpenMP support in the LLVM compiler infrastructure.

**Optimization in LLVM - Numbers, A Case Study, and Looking Forward**  
*Chandler Carruth - Google*  
With all of the excitement surrounding Clang, LLD, LLDB, Sanitizers, and other projects in LLVM, it is easy to let its origins slip your mind. However, LLVM was and remains a platform for optimizing compilers and related parts of the toolchain. Today, the LLVM + Clang optimizing C++ compiler is very powerful and can handle a wide range of code, but how well does it compete with modern versions of GCC? What are the root causes of some of the more striking differences? What is coming next in LLVM that will significantly impact the optimizing power of the toolchain?

**clang-format - Automatic formatting for C++**  
*Daniel Jasper - Google*  
Source code readability is an important aspect to ensure quality and long-term maintainability. However, manually formatting is a tedious job that simply takes a chunk out of every programmer's productivity. Moreover, the tediousness can actively discourage refactorings, e.g. removing or restructuring a function's parameters. There are tools that can provide some level of intelligent auto-formatting, but no tool has so far been able to keep developers happy in a reasonably-sized codebase. Therefore, we have set out to build clang-format, an intelligent C++ formatter based on Clang's infrastructure.

**Debug Info - Status and Directions**  
*Eric Christopher - Google*  
In the last few years clang and llvm have made great inroads as the default compilers in the open source world and in industry. It is now seeing daily use as the default compiler for all of the Apple ecosystem, FreeBSD, and as one of the compilers at Google. As a compiler matures and its user base expands the quality of the debug information output becomes more important. In the past users of clang and LLVM have had to deal with poor debug information, but in the last couple years the quality of debug information has improved greatly and in some cases we are pushing the boundaries of existing standards. We've made good progress with gdb testing and implementing DWARF4 including the extensions for C++11. Furthermore, we've implemented and are proposing for inclusion in DWARF5 support for split debug information and faster access to named debug entities.

**Run-time tracking of uninitialized data with MemorySanitizer**  
*Evgeniy Stepanov - Google*  
[MemorySanitizer](http://clang.llvm.org/docs/MemorySanitizer.html) is a detector of uninitialized reads, inspired by Valgrind/Memcheck and DrMemory, but based on compiler instrumentation technology. It was mentioned in the 2012 LLVM DevMtg; since then MemorySanitizer (MSan) has grown and improved and has been accepted in LLVM 3.3 trunk. It is now able to bootstrap Clang with a 3.7x slowdown and has detected multiple bugs in LLVM, Chromium, etc. Unlike AddressSanitizer and ThreadSanitizer, MSan has a very simple run-time library and a complex instrumentation module. Another difference is the need for full program instrumentation. We provide a helper tool based on DynamoRio instrumentation framework to deal with this. This talk will concentrate on MSan internals and implementation issues.

**How Computers Work**  
*Jakob Olesen - Apple*  
Most high-performance CPU micro-architectures designed in the last 20 years are super-scalar and execute instructions out of order. I intend to give an overview of how out-of-order CPUs work, and how we can generate code that performs well on modern micro-architectures. Some optimisations are only beneficial if the compiler has a detailed understanding of how the code is going to be executed, and the new machine trace metrics analysis can be used to guide these optimisations. I'll talk about current and future optimisations that can take advantage of this detailed execution information.

**lld - Solving the Linking Performance Problem**  
*Michael Spencer - Sony Computer Entertainment America*  
lld is a LLVM subproject with the goal of building a fast, modular, and cross platform linker. lld is under very active development. It can currently link moderately complex programs, including itself and LLVM. Link time performance is a critical part of lld, and it takes several measures to improve it. The Atom graph model simplifies linking which also makes parallelizing the link simpler. It also provides a method to evaluate linker scripts without serializing the entire link. We have also taken a step back to look at the entire linking process and have found a major area for improvement. A significant amount of time while linking is spent reading object files and converting the information they contain into a format suitable for the linker. We can improve this by reading in parallel and reading lazily, however this can only take us so far. The real solution is to have the compiler emit object files designed for linking performance. Since we have a simple internal model in the linker, we have developed a native object file format that matches this model and that is designed specifically for linking performance. It is designed around the data structures and algorithms used in linking, while still maintaining all of the semantics of various object file formats. It is also very easy for compilers to generate. This allows us to bypass the work of processing traditional object files and jump directly to the core linking process. This talk will explore the the linking performance problem and lld's solutions.

**Performing Source-to-Source Transformations with Clang**  
*Olaf Krzikalla - TU Dresden*  
Back in 2009 we started to develop a configurable source-to-source transformation tool designed to automatically vectorize C/C++ source code using SIMD instructions. Meanwhile the tool, called Scout, is an industrial-strength vectorizing preprocessor, which is used on a day-to-day basis in the software production process of the German Aerospace Center. The code is published as Open Source and can be downloaded from [http://scout.zih.tu-dresden.de](http://scout.zih.tu-dresden.de). The source-to-source transformation framework of Scout is based on the AST and the accompanying infrastructure of Clang. Beside the actual vectorization the framework provides function inlining, loop-unrolling and loop-unswitching at AST level. For this a C/C++ file is parsed, the generated AST is transformed and then written back to a target file. However this approach is critical, since the AST of Clang is actually immutable by design. On the other hand there is a lot of interest in source-to-source transformation tools based on Clang, as can be seen on cfe-dev and in other talks. In our talk we will present our experiences, the technologies used and possible future directions of the development of source-to-source transformation tools.

**LLVM Interpreter, a key component in validation of OpenCL compilers**  
*Oleg Maslov - Intel*  
In this presentation we show how we use LLVM interpreter to create a validation tool chain for OpenCL compilers which is isolated from the OpenCL runtime. LLVM interpreter produces bitwise accurate results and is used as a reference OpenCL engine. This infrastructure is used in pre silicon enablement of MIC and X86 OpenCL compilers. It is also used to validate correctness of the workloads during ongoing development of the compilers. As part of the work we extended existing interpreter to support the missing vector and aggregate data types and plan to upstream the changes to llvm.org.

**How to implement an LLVM Assembler - a tutorial**  
*Simon Cook - Embecosm*  
During late 2012, working with colleague from the OpenCores project, the speaker implemented a full LLVM assembler for the OpenRISC 1000 architecture. This assembler was subsequently integrated into the main OpenRISC LLVM compiler tool chain. The details of how to do this were written up as Embecosm [application note 11](http://www.embecosm.com/appnotes/ean10/ean10-howto-llvmas-1.0.html), since shared on the main LLVM website. In this talk the speaker will explain how to build an LLVM assembler, test it and integrate it into a the LLVM compiler tool chain. The talk will consider the benefits that come from using an integrated LLVM assembler rather than a GNU binutils standalone assembler.

**An experimental framework for Pragma Handling in Clang**  
*Simone Pellegrini - University of Innsbruck*  
Clang is one of the fully featured C/C++ frontend which managed to bring compiler research into the mainstream. Its clean interfaces and structure enabled several new research ideas to be applied to real codes in a scale that was never possible in the past. However, one of the main sin of researchers is the need to extend the language. Since C allows language extensions through the #pragma preprocessor directive, many have used this medium for feeding meta-information to the compiler analysis module. A very famous example is the OpenMP standard. This is an extension to the semantics of C/C++ which grants to the compiler the possibility of parallelizing a portion of the input code. However Clang's support for pragmas is lacking and primitive at most. Clang allows pragma handlers to be registered for a particular pragma but the user is left with the burden of parsing the tokens returned by the lexer. This is not a problem for many extensions which rely on simple keywords and integer identifiers, however it can become a parsing nightmare if a C expression is allowed in the pragma (as it is the case for OpenMP). In those cases, the user has to provide its own expression parser which basically means rewriting Clang's parser. My solution relies on a simple idea, i.e. exposing the full Clang parser to pragma handlers. Together with a framework which allows pragma definition to be specified in EBNF form, new language extensions can be easily defined in a single line of C++ code.

**LLVM on IBM POWER processors: a progress report**  
*Ulrich Weigand - IBM*  
Until recently, use of LLVM on IBM processors, in particular POWER, was not an issue of particular interest to IBM, and we were not directly involved in LLVM development. This situation changed significantly during the past year, as a result of more widespread use of LLVM, in particular its just-in-time compiler, as an essential component of widely used open-source and proprietary applications, and increased customer requests for LLVM capabilities on IBM platforms. This led to the decision to get actively involved with the LLVM community, and form a team within the IBM Linux Technology Center to help enable full support for LLVM on PowerLinux. Over the past several months, we have made significant progress towards that goal; in particular, the LLVM 3.2 release now bootstraps and passes all test suites on PowerLinux, and provides a working (MC) JIT implementation. In this presentation I plan to report on IBM's involvement with LLVM as described above and the work we've done so far, including various missing features that were contributed, like support for the JIT, the assembler parser and disassembler, full TLS support, medium and large code models, full ABI compatibility, and Altivec enhancements. I will also present methods we used to verify correctness of the port, and show some examples of the more interesting bugs we found and fixed in the process. As a long-time GCC developer with no prior experience with LLVM, I will also try to give some impressions on my "learning curve" with the LLVM design and code base, in particular from the perspective of a processor back-end: which parts were easy to get into, and what took significant effort getting used to. Finally, I will conclude by presenting ongoing work on features that are still missing to provide first-class support for POWER, and our plans for future continued involvement with LLVM.

<!-- *********************************************************************** -->

## Tutorial abstracts

**The Clang AST - a tutorial**  
*Manuel Klimek - Google*  
For engineers starting to contribute to Clang or writing tools based on Clang, the AST is often the first big stumbling stone. While it merely mirrors the complexity of the languages it represents, learning how to navigate between the nodes can be a daunting task. In this tutorial I will present the structure of Clang's AST, how the nodes match to C++ language constructs and how to make good use of the documentation and tools available to navigate the maze to find what you need. We will take an in-depth look at various common connections, like templates and their definitions, source locations and types, dependent types, typedefs, and more. Using simple code samples I'll walk through the basic handling of AST nodes, and dive into more advanced topics focusing on the C++ specific parts of the AST.

<!-- *********************************************************************** -->

## Poster abstracts

**LLVM IR editor plugin for Eclipse**  
*Alon Mishne & Ayal Zaks - Intel*  
LLVM IR SDK is an Eclipse plugin that adds an LLVM IR (.ll files) editor to Eclipse. Intended for LLVM developers, it is designed to provide nearly the same level of support for IR files that other programming languages enjoy under Eclipse, making it easier to write tests and analyze pass output. By incorporating a wide range of validation checks as you type - from simple syntax checks through full type validation and up to dominance analysis - the plugin enables a quick modify-and-run cycle for IR files, without having to run LLVM module validation in-between. In addition, the plugin exposes a variety of quick-fix options for common code actions, such as fixing broken number sequence for local names, inserting conversions between types, inserting function declarations inferred from a function call, and more.

**Sambamba: A Runtime System for Online Adaptive Parallelization**  
*Clemens Hammacher - Saarland University, Germany*  
Automatic parallelization is a classical compiler problem: Using static analyses, the compiler tries to prove computations independent from each other, and estimates the benefit that would be gained by executing these codes in parallel. Both of these tasks represent huge challenges, as neither the input data nor characteristics of the execution platform are typically known at compile time. However, those factors mainly determine where parallelization is applicable and beneficial. Because of this discrepancy, the effectiveness of parallelizing compilers is very limited. On the other hand, manual parallelization has also proven to be a serious hurdle for the majority of developers. A lot of new languages and programming libraries have been built to support programmers in that task, but all of them still require expertise in order to build efficient applications. Sometimes runtime support is installed, such as software transactional memory, to enable speculative parallelization where the independence of computations can not be proven. This makes it even harder to estimate whether the overhead will pay off at runtime, in the sense of an overall performance improvement. Therefore, we propose an automatic runtime-adaptive system. It executes the target application in a lightweight virtual machine, and constantly monitors its runtime behaviour. This information is then used to decide where and how to parallelize. This way, alternative variants of individual functions are provided, which have been optimized for the observed input. Those variants do not immediately replace previous code by installing them into the running application, but it is the runtime system's responsibility to identify the best performing variant for the situation at hand.

**LLVM backend for TILE64**  
*Dávid Juhász*  
LLVM provides a platform-independent intermediate layer for developers of highlevel programming languages. Benefits of transforming high-level programs into LLVM IR are twofold: high-level to intermediate compilation does not have to deal with platform-specific details, still executables for many different architectures can be compiled using back-ends already implemented for the LLVM toolchain. Programs in platform-independent intermediate representation are to be analyzed and transformed in order to be optimized, e.g. run faster or consume less memory, and to generate executable code. The last major step of processing programs is code generation which can be done using LLVM back-ends. LLVM has a target-independent code generator, in which the most common features for turning a target-independent representation into a platform-specific assembly or binary are implemented. An LLVM back-end is mainly the parameterization of the target-independent code generator with platform-specific properties. In many cases, the default implementation of different parts of the code generation fits well to the target. However, overriding some features is necessary for architectures which are to some extents different from the mainstream ones. Tile64 was the first commercial product of Tilera Corporation back in 2007, that has been followed by other more sophisticated Tilera processors. Tile64 is an energy-efficient massively parallel processor architecture. It consists of 64 general purpose processor cores (tiles) connected by a mesh-network. Each core has 3 pipelines, two of them are for integer and logical operations and the third one is a load-store unit. The shortpipeline, in-order, three-issue (there are two-issue bundles as well) cores implement a VLIW instruction set supporting RISC instructions extended with various SIMD and DSP-related operations. The processor is very capable of communication both inside and outside the mesh-network. The speed of the interconnection between tiles is one hop per tick, and the edges of the mesh are connected to different I/O interfaces (four DDR2 controllers, two 10-gigabit Ethernet interfaces, two four-lane PCIe interfaces, and a software-configured "flexible" I/O interface). Tile64 is in many ways different from the mainstream processor architectures, thus implementing an LLVM back-end for Tile64 posed several questions. Some of those questions and tricky parts of implementation are to be revealed in the poster.

**MCLinker: Design and Implementation of a Fragments-based Target-independent Linker**  
*Diana Chen - MediaTek Inc.*  
MCLinker is a system linker that uses fragments as its internal intermediate representations (IRs) to process inputs, such as a .o file, and generate desired output file. Valid inputs for now are: .o, .a, .so, and a piece of in-memory of code; and valid outputs are: .o, .so, and executable binary. Fragments are good IRs for a linker in a way that these fragments can easily generate data structures to be used by linkers. Fragments can be either a function, a block of code, or a defined symbol with a memory region. For instance, the global offset table in a typical .so and the frame description table in DWARF format of MCLinker are made directly from fragments. Another reason is linking finer-grained fragments could lead to a more optimized result as opposed to coarse-grained sections, because finer-grained fragments would facilitate better data-stripping and reordering. However, LLVM MC fragments are originally designed for assembler so they could not fulfill some requirements from linkers. Thus, MCLinker needs to define some additional fragment types. For example, MCLinker defines general "relocation fragments" and "stub fragments" to represent stubs of the branch islands. MCLinker also defines “region fragment” to hold arbitrary blocks of code or data. Furthermore, MCLinker introduces a general reference linkage between two fragments to represent their relocation relationship. MCLinker is a full-fledged system linker. It is capable of linking ELF object files on various platforms, such as ARM, x86, and MIPS. Some additional targets, such as x86-64 and x32, are still in development and will be available soon. MCLinker fully supports complex ELF features, such as DWARF debugging, Itanium exception handling, COMDAT sections, instruction relaxation, and GNU archive format.

**ENHANCE - Enabling heterogeneous hardware acceleration using novel programming and scheduling models**  
*Dustin Feld*  
Developers faced with the task of creating parallel applications on heterogeneous computing architectures often fail to reach acceptable performance and speed-up values due to sub-optimal communication patterns in their application. At the same time, the operating system often is not able to reach optimal resource utilization, due to missing possibilities for relocating user threads and user processes across hardware boundaries. Some of these issues can already be tackled at compile time if the compiler is able to understand coding and design patterns and acts accordingly. In this presentation we introduce an automatic framework for parallelization, check-pointing, and task scheduling based on the LLVM compiler framework. Our work includes techniques which facilitate an efficient usage of heterogeneous resources with a dynamic and automated approach. Furthermore, a task scheduling framework on a single node basis takes care of the fair use scheduling of available hardware resource in a multi-user environment.

**OJIT: A novel secure remote execution technology by obfuscated Just-In-Time compilation**  
*Muhammad Hataba - Egypt-Japan University for Science and Technology*  
This poster presents the Obfuscating Just-In-Time compilation (OJIT) technique. OJIT is a novel security technique for a trustworthy and secured code execution on a remote premise such as the cloud-computing environment. We rely on the principles of obscurity for the sake of security, which is a concept widely popular in software protection. LLVM's just-in-time (JIT) compilation is used to dynamically obfuscate code, making the generated code unintelligible and hence difficult to reverse engineer. We obfuscate the code by an array of randomly yet dynamically changing techniques that are independent of the source language of the executed program yet neutral to the platform that we are executing on. We evaluated the technique by measuring a variety of obfuscation metrics running a set of benchmark programs.

**Code Editing in Local Style**  
*Peter Conn - Cambridge University*  
Coding styles contain a variety of elements, from indenting rules to variable and function names. They also place different constraints on variable declarations, for example requiring them at the start of the function or in the smallest possible scope. Some of these can be automatically checked with purely syntactic checkers, such as typical implementations of the UNIX indent tool. Others require semantic knowledge. For example, moving a variable declaration requires knowing where all of its uses are. The goal of the CELS (Code Editing in Local Style) tool is to allow each developer to edit code in their preferred style, while preserving a uniform style in the repository. It includes the ability to specify complex styles, to infer styles from an existing corpus of source code, and to perform automatic formatting. CELS is written as a library on top of libclang, allowing it to be embedded in code editors and IDEs without relying on unstable binary interfaces. It traverses the AST exposed by libclang and builds a scope tree, renames symbols, moves declarations, and wraps lines. The line-wrapping algorithm used is based on the TEX line breaking algorithm. The user may specify different penalties for different line breaking locations, for example encoding rules such as \`prefer to break after an operator, try to avoid breaking before a comma, breaking after a semicolon is best' and have the lines wrapped accordingly. Additionally, the typesetter is aware of the distinction between whitespace used for indentation and whitespace used for alignment and so can use different characters for either, for example using tabs for indentation and spaces for alignment, allowing the resulting code to be viewed with any tab size without losing alignment.

**Noise: A Clang Extension for User-Defined Optimization Strategies**  
*Ralf Karrenberg - Saarland University*  
In this talk, we present "Noise", a language extension to Clang that enables a programmer to control the optimization process on a code region. Noise is a language extension that allows a programmer to create custom optimization strategies and apply them to specific code segments. This enables fine-grained control over the optimizations applied by the compiler to conveniently tune code without actually rewriting it. With Noise, the programmer can easily choose optimizations and their order without interfering with the standard optimizations being applied to the remaining program. This is especially important for legacy code in the High-Performance Computing (HPC) environment, but is also relevant in other performance-sensitive fields such as computer graphics. We present our implementation for C/C++ within the Clang frontend using attributes. In addition to exposing LLVM's internal optimization phases, Noise also has special transformations built-in, for example data-parallel loop vectorization on the basis of "Whole-Function Vectorization". We show first results demonstrating the effectiveness of Noise on HPC code in production.

**Improving Machine Code Generation Quality by Interfacing VPO with LLVM**  
*Ryan Baird - Boise State University*  
Very Portable Optimizer (VPO) is a research compiler backend that performs optimizations on a single intermediate representation called Register Transfer Lists (RTLs). RTLs are at the level of machine instructions, and therefore most of VPO's code improving optimizations can be performed in a machine independent way and optimization phases can be repeated in an arbitrary order. For these merits, VPO is widely used to optimize machine code that exploits various architecture features on low-power embedded processors. However, VPO uses LCC as a front-end, which does not support current language standards (C99,C++98) and has no mid-level code improving transformations. The contributions of this poster are two-fold. First, it describes our approach to extend both the code coverage and the quality of VPO machine code generation by streamlining the compiler with LLVM instead of LCC. Second, it provides some insight to the LLVM community into alternative machine code generation, which can be effectively achieved by interfacing with an existing optimizing compiler instead of creating a different machine port within LLVM.

**Using the LLVM Interpreter to Quantify Applications Inherent Properties**  
*Victoria Caparros - ETH Zurich*  
This poster presents a tool based on the LLVM interpreter for quantifying application's inherent properties. Our approach to quantifying applications properties is based on previous studies that use a microarchitectural simulator to emulate a machine with unlimited hardware resources, and quantify application behavior from the analysis of the data dependences and data movement properties of the dynamic instruction trace during execution on the simulator \[2\]. This approach has several advantages. First, application properties are measured for the particular input considered, as opposed to the theoretical analysis of the algorithm, which does not consider input size. Second, it provides a better insight into application behavior, since it exposes a broader range of application properties, not only those that are exploitable with existing microarchitectural features (what can be measured with hardware performance counters on a target platform), but also properties that may require new hardware features in order to be exploited. Finally, this approach enables us to reason about application's performance across different platforms with just a single pass of the analysis, not requiring to repeat the analysis for every hardware configuration of interest.

<!-- *********************************************************************** -->

## Lightning talk abstracts

**[Sambamba: A Runtime System for Online Adaptive Parallelization](#poster1)**  
*Clemens Hammacher - Saarland University, Germany*  

**Integrating fine-grained timing constraints into LLVM**  
*David Lacey - XMOS Ltd*  
This talk covers a problem we are just beginning to tackle of integrating fine-grained timing constraints into LLVM. Code written for real-time tasks often comes with worst case timing constraints on paths within the program (usually between I/O operations). These paths can be quite short or can cross across basic blocks and function boundaries. Unfortunately, the optimizations within LLVM are not aware of these constraints and code motion or control flow optimizations can move calculations into a critical path quite easily. I'll cover the experiences we've had with the optimizations in the compiler and go over the initial ideas we have to tackle the problem.

**[MCLinker: Design and Implementation of a Fragments-based Target-independent Linker](#poster3)**  
*Diana Chen - MediaTek Inc.*  

**FDO-based whole program optimization in LLVM**  
*Diego Novillo - Google*  
At Google, we achieve the highest levels of performance using whole program optimization. However, traditional whole program optimization does not scale to the size of applications that we are interested in optimizing. In this lightning talk, I will briefly describe the FDO technologies that we have implemented, how we apply them to whole program optimization and our plans to port this technology to the LLVM compiler.

**Efficient audio signal processing using LLVM and Haskell**  
*Henning Thielemann*  
I am using LLVM for audio signal processing via Haskell. My goal is to combine the safety and elegance of Haskell with the speed of code generated by LLVM. My approach is an embedded domain specific language (EDSL), that is, my library provides Haskell functions that look like signal processing functions, but actually they represent pieces of LLVM assembly code. Composing such signal functions means assembling large LLVM code blocks from smaller ones. I use the JIT for turning the LLVM code into executable C functions. This also allows me to adapt to available processor extensions like SSE and AVX at startup time of a signal processing program. I make intensive use of the vector instructions of LLVM.

**[Noise: A Clang Extension for User-Defined Optimization Strategies](#poster6)**  
*Ralf Karrenberg - Saarland University*  

**Rebuild of all Debian packages using Clang instead of gcc**  
*Sylvestre Ledru - Debian / IRILL*  
Besides the GNU/Linux kernel, Debian is now able to run with two others kernels (KFreeBSD & HURD). However, in terms of compilation, Debian is still coupled to gcc. This lightning talk will present the results of the rebuild of the whole Debian archive with various clang versions. A necessary step to make Debian compiler agnostic.

<!-- *********************************************************************** -->

* * *
