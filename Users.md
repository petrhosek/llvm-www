---
layout: "default.html"
permalink: "Users.html"
---
# LLVM Users

This page lists the people and organizations that have used or are currently using LLVM in research, education, industry, or open source development. It only includes users who have publicly discussed their use of LLVM in one form or another (mentioned it on llvm-dev, published work on it, etc.). We believe there are many other users not listed here and would welcome a brief note telling us about your use so that we can add you to the list.

This page has only brief entries. Some of these projects are described in more detail on the ["Projects Using LLVM"](/ProjectsWithLLVM/) page.

## LLVM Distributions

*   [Debian Package Info](http://packages.debian.org/unstable/devel/llvm)
*   [Ubuntu Package Info](http://packages.ubuntu.com/dapper/devel/llvm)
*   [FRESHports LLVM page](http://www.freshports.org/devel/llvm)
*   [Apple Xcode](http://developer.apple.com/)

## Industry Users

<!-- From Chuck Rose --> <!-- From Adobe web site --> <!-- CS Department Web Page and Adobe web site --> <!-- Secured from company --> <!-- http://lists.llvm.org/pipermail/llvm-dev/2008-March/012978.html --> <!-- www.arxan.com --> <!-- http://lists.llvm.org/pipermail/llvm-commits/Week-of-Mon-20060227/032334.html --> <!-- From Nadav Rotem via email --> <!-- Announcement at 2008 dev. meeting --> <!-- Ok'd by Luiz DeRose and David Greene --> <!-- From Max Burke via email --> <!-- http://lists.llvm.org/pipermail/llvm-dev/2018-June/124279.html --> <!-- Requested on llvm-dev from Matt Pharr --> <!-- http://lists.llvm.org/pipermail/llvm-dev/2004-October/002329.html --> <!-- From info@vuo.org --> <!-- http://lists.llvm.org/pipermail/llvm-dev/2006-August/006455.html --> <!-- Personal communication and ok'd by Christopher Lamb --> <!-- http://rapidmind.com/News-Nov10-08-LLVM-OpenCL.php --> <!-- http://lists.llvm.org/pipermail/llvm-dev/2006-January/005150.html --> <!-- Private communication to Vikram --> <!-- XMOS web site: https://technology.xmos.com/open-source "The LLVM project provides an open source compiler for C and other languages. At present we have ported the back-end code generator to our architecture. It is our intention to work with the LLVM community and add analysis for multi-core code generation to the compiler." -->

| Company | Description |
| --- | --- |
| Adobe Systems Incorporated | Optimizer and JIT codegen for the [Hydra Language](/ProjectsWithLLVM/#adobe-hydra). |
| Adobe Systems Incorporated | [Alchemy C/C++ Compiler for the ActionScript Virtual Machine (AVM2)](http://labs.adobe.com/wiki/index.php/Alchemy). See the [FAQ](http://labs.adobe.com/wiki/index.php/Alchemy:FAQ) and [Scott Petersen's DevMtg talk](/devmtg/2008-08/) for more details. |
| Adobe Systems Incorporated | ActionScript 3 Ahead-of-Time (AOT) Compiler for iPhone software development. See Aditya Bansod's [blog entry](http://www.adobe.com/devnet/logged_in/abansod_iphone.html) and [this video](http://labs.adobe.com/technologies/flashcs5/appsfor_iphone/#divider) for more details. |
| Ageia Technologies | Optimizer and back end for custom processor |
| Apple Inc. | All of Apple’s operating systems, iOS, macOS, tvOS and watchOS, are built with LLVM technologies. And Xcode, Apple’s integrated development environment, supports development in Swift, C, C++, and Objective-C, all of which use and are built with LLVM technologies. Apple’s implementations of OpenCL and OpenGL, the Metal Shading Language, Core Image, and macOS graphics drivers also use LLVM technologies. |
| [Arxan Technologies, Inc.](http://www.arxan.com) | [EnsureIT](http://www.arxan.com/software-protection-products/EnsureIT/index.php) - Comprehensive software/code protection for Android, Apple iOS, and Linux. Covers against both static and dynamic analysis threats. |
| Ascenium | Compiler for reconfigurable processor |
| AutoESL Design Technologies, Inc. | Electronic System Level (ESL) to Silicon |
| [Azul Systems, Inc.](https://www.azul.com/) | Azul Systems' [Zing Java Virtual Machine](https://www.azul.com/products/zing/) ships with [Falcon](https://www.azul.com/press_release/falcon-jit-compiler/), an LLVM based optimizing high-tier JIT compiler. |
| [C-to-Verilog](http://www.c-to-verilog.com/) | Compiler from C into the Verilog hardware description language. Automates circuit design. |
| [Codeplay Software](https://www.codeplay.com/) | C/C++/OpenCL compilers and debuggers for CPUs, GPUs, DSPs and custom processors. |
| MTC Group Ltd. | [Morpher](http://morpher.com) - compiler-driven obfuscation solution for C/C++/ObjC/ObjC++. Protection against reverse engineering, cracking and tampering. |
| Cray Inc. | Backend for the Cray x86 compiler, available on the Cray XT5 and later machines. |
| Electronic Arts | Experimental backend for custom language implementation |
| Ericsson | Compiler for a custom telecom DSP VLIW architecture, featuring 16-bit bytes and fixed-point arithmetic. |
| Intel | [OpenCL](/devmtg/2011-11/Rotem_IntelOpenCLSDKVectorizer.pdf) |
| Huawei | [BiSheng Compiler](https://www.hikunpeng.com/document/detail/en/kunpengdevps/compiler/ug-bisheng/kunpengbisheng_06_0001.html), a C/C++/Fortran compiler for Huawei's Kunpeng servers. |
| Hue AS | JIT compilation of shader programs |
| [Kosada, Inc.](http://vuo.org/about) | The compiler for [Vuo](http://vuo.org), a modern visual programming language for multimedia artists. |
| Mobileye | Compiler for stack machine architecture |
| National Instruments | [Compiler for LabView 2010](http://zone.ni.com/devzone/cda/tut/p/id/11472) |
| [Nuanti Browser Labs](http://www.nuanti.com) | [WebKit Meta 2.0 SDK](http://meta.webkit.net) includes a specialized LLVM/clang toolchain for web application and game development featuring transparent C++ DOM and JavaScript bridging. [C++/CLI NG](http://www.atoker.com/blog/2012/04/12/llvm-europe-2012-cli-compiler/) is a clang-based .NET compiler that embraces and extends the Microsoft / ECMA-372 language standard. |
| NVIDIA | OpenCL runtime compiler (Clang + LLVM) |
| Rapidmind | [Compiler platform](http://rapidmind.com/News-Nov10-08-LLVM-OpenCL.php) for their GPGPU, multicore CPU, and OpenCL runtime platforms. |
| REAL Software | Optimizer and code generator for [RBScript and REAL Studio compiler](http://www.realsoftwareblog.com/2010/03/compiler-better-stronger-faster.html). |
| Siemens Technology-to-Business Center | Compiler for embedded VLIW processor |
| [SonarSource](https://www.sonarsource.com) | Frontend for the C/C++/Objective-C languages. AST matchers and the Clang Static Analyzer as libraries. |
| Sony Interactive Entertainment | CPU compiler for the [PlayStation®4 and PlayStation®5](https://playstation.com) systems. |
| Sun Microsystems Laboratories | [Parfait: Bug checker of C code](http://research.sun.com/projects/parfait) |
| [Synopsys Inc.](https://www.synopsys.com) | [DesignWare ARC MetaWare EV Development Toolkit (OpenCL)](https://www.synopsys.com/dw/ipdir.php?ds=arc-metaware-ev) – EV6x processors<br>[DesignWare ARC MetaWare Development Toolkit (C/C++)](https://www.synopsys.com/dw/ipdir.php?ds=sw_metaware) – ARC processors |
| XMOS Technology | [Backend port for their architecture](http://www.xmos.com/open-source), also working on multicore codegen support. |
| Octasic Inc | [Opus Studio next generation](http://www.octasic.com/products/opus-studio), IDE and compiler for asynchronous DSP Architecture (in development). |

## Open Source Projects

<!-- http://llvm.org/ProjectsWithLLVM/#IcedTea --> <!-- Authorized and described by Gary Benson, Lead on the Shark JIT within IcedTea --> <!-- http://llvm.org/ProjectsWithLLVM/#pypy --> <!-- http://www.grame.fr/~letz/faust_llvm.html --> <!-- iPhone Tool Chain --> <!-- http://www.quake3world.com/forum/viewtopic.php?f=7&t=36482 --> <!-- Email sent to llvm-dev --> <!-- Email sent to llvm-dev --> <!-- Email sent to llvm-dev --> <!-- Email sent to llvm-dev --> <!-- Listed in LLVM 2.6 Release Notes --> <!-- Listed in LLVM 2.6 Release Notes --> <!-- Listed in LLVM 2.6 Release Notes --> <!-- Listed in LLVM 2.6 Release Notes --> <!-- Listed in LLVM 2.6 Release Notes --> <!-- Requested on llvm-dev --> <!-- Requested on llvm-dev by Matt Pharr --> <!-- Requested on llvm-dev --> <!-- Requested on llvm-dev by Jakub Kuderski --> <!-- Requested on llvm-dev by Jakub Kuderski -->

| Project | Description |
| --- | --- |
| [SMACK Software Verifier](https://github.com/smackers/smack) | Software verifier that converts LLVM IR to Boogie |
| [Objective Modula-2 Project](http://objective.modula2.net) | Modula-2 compiler w/ObjC runtime support. Targets Objective-C and LLVM. |
| [IcedTea Version of Sun's OpenJDK](/ProjectsWithLLVM/#IcedTea) | Uses LLVM as JIT on architectures other than x86 and Sparc. |
| [PyPy Project](http://pypy.org) | Python interpreter written in Python. Targets LLVM and C. |
| [Faust Signal Processing Language](http://faust.grame.fr/) | Signal processing language, [uses the LLVM JIT for runtime codegen](http://www.grame.fr/~letz/faust_llvm.html). |
| [iPhone tool chain](http://code.google.com/p/iphone-dev/wiki/Building) | llvm-gcc Compiler for iPhone Dev Wiki toolchain. |
| [IOQuake3](http://www.ioquake3.org) | IOQuake3 Raytracing Patch, [uses LLVM for runtime shader compilation.](http://www.quake3world.com/forum/viewtopic.php?f=7&t=36482) |
| [llvm-py: Python Bindings for LLVM](http://mdevan.nfshost.com/llvm-py/) | Build compilers and VMs in Python, using the LLVM Backend. |
| [LDC](http://wiki.dlang.org/LDC) | LLVM-based [D](http://dlang.org/) Compiler. |
| [Unladen Swallow](http://code.google.com/p/unladen-swallow) | A faster implementation of Python. |
| [Mono](http://tirania.org/blog/archive/2009/Jul-16.html) | Mono has an option to use LLVM for JIT compilation. |
| [Rubinius](http://github.com/rubinius/rubinius) | Ruby Environment. |
| [MacRuby](http://macruby.org/) | Ruby Implementation for Mac OS X. |
| [Pure](http://pure-lang.googlecode.com/) | Term rewriting algebraic/functional programming language. |
| [Roadsend PHP](http://code.roadsend.com/rphp) | PHP implementation. |
| [LLVM-Lua](http://code.google.com/p/llvm-lua/) | JIT and static compilation support for the Lua VM. |
| [Emscripten](http://emscripten.org) | An LLVM to JavaScript compiler. |
| [Julia](http://julialang.org/) | High-level, high-performance dynamic programming language for technical computing. |
| [SkyEye](http://www.skyeye.org/) | Fast full system simulator. |
| [Intel SPMD Compiler](http://ispc.github.com) | C-based SPMD language for CPU vector units. |
| [XLA](https://www.tensorflow.org/versions/master/experimental/xla/) | XLA (Accelerated Linear Algebra) is a domain-specific compiler for linear algebra that optimizes TensorFlow computations. |
| [SeaHorn](http://seahorn.github.io/) | An Algorithmic Logic-Based Reasoning Framework. |
| [Crab-llvm](https://github.com/seahorn/crab-llvm) | A static analyzer based on abstract interpretation for LLVM. |

## Academic Research Users

<!-- Requested by Johan Lilius's Research Group --> <!-- Authorized by David Penry in email to Vikram --> <!-- Authorized by David Koes in email to Vikram and John --> <!-- Email from George Candea to Vikram and John --> <!-- http://lists.llvm.org/pipermail/llvm-dev/2008-October/017539.html --> <!-- http://lists.llvm.org/pipermail/llvm-dev/2006-July/006246.html --> <!-- Personal email to Chris --> <!-- http://lists.llvm.org/pipermail/llvm-dev/2005-July/004661.html --> <!-- http://www.cse.ucsd.edu/~mmccrack/lens --> <!-- Email from Samar Abdi: sabdi at uci.edu --> <!-- http://lists.llvm.org/pipermail/llvm-dev/2005-November/004939.html --> <!-- Email from Wesley Peck --> <!-- SoftBound Publication on Publication Page --> <!-- Publications on Publication Page -->

| Organization | People | Description |
| --- | --- | --- |
| [Åbo Akademi University](http://www.abo.fi/) | Johan Lilius's Research Group, ES Lab | [NECST project](http://www.abo.fi/~johan.lilius/research/page12/page0/necst.html) |
| [Brigham Young University](http://www.byu.edu) | [David Penry's Research Group](http://www.et.byu.edu/groups/bardd) | Microarchitectural Simulator Partitioning and Synthesis<br>Adaptive Online Parallel Optimization |
| [Carnegie Mellon University](http://www.cmu.edu) | [David Koes](http://www.cs.cmu.edu/~dkoes/research.html) | Principled Compilation |
| [Ecole Polytechnique Fédérale de Lausanne](http://www.epfl.ch) | George Candea's Research Group | <br>• [Cloud9: Software Testing as a Service & Parallel Symbolic Execution](http://dslab.epfl.ch/proj/cloud9)<br>• [S2E: Scalable Testing with Selective Symbolic Execution](http://dslab.epfl.ch/proj/s2e)<br>• [ESD: Automated Debugging via Execution Synthesis](http://dslab.epfl.ch/proj/esd) |
| [ETH Zurich](http://www.ethz.ch/) | Thomas Lenherr | Language-independent library for alias analysis |
| [Friedrich-Alexander Universität, Erlangen-Nüremberg](https://www.fau.de) | Tobias Klaus, Fabian Scheler, and Florian Franzmann | [RTSC Real-Time Systems Compiler](http://www4.cs.fau.de/Research/RTSC/) |
| [Ghent University](http://www.ugent.be/) | [Kenneth Hoste](http://www.elis.ugent.be/~kehoste) | Instrumentation of software |
| [GH-SEL, INTEC, Ghent University](http://faramir.ugent.be/) | [Bram Adams](http://users.ugent.be/~badams/) | Aspect weaver for an AOP-language for C called [Aspicere2](http://users.ugent.be/~badams/aspicere2/) |
| Institut d'Electronique et Télécommunications de Rennes<br>ARTEMIS - Institut Telecom/Telecom SudParis | Mickaël Raulet, Matthieu Wipliez, Jérôme Gorin | <br>• [Orcc project: Open RVC-CAL Compiler](http://orcc.sf.net)<br>• [Jade project: JIT Adaptive Decoder Engine](http://sourceforge.net/apps/trac/orcc/wiki/JadeDocumentation) |
| [New York University](http://www.nyu.edu) | Anna Zaks | Validation of interprocedural optimizations |
| [Rice University](http://www.rice.edu) | Keith Cooper's Research Group |  |
| [Stanford University](http://www.stanford.edu) | Dawson Engler's Research Group | [KLEE Symbolic Virtual Machine](http://klee.llvm.org) |
| [Tampere University of Technology](http://www.tut.fi) | [Jarmo Takala's research group, Department of Computer Systems](http://www.tkt.cs.tut.fi/index-english.html) | [The TTA Based Codesign Environment (TCE) project](http://tce.cs.tut.fi) |
| [University of California, San Diego](http://www.ucsd.edu/) | Michael McCracken | [LENS Framework](http://www.cse.ucsd.edu/~mmccrack/lens/) |
| [University of California, Irvine](http://www.uci.edu/) | Samar Abdi, Dan Gajski | [Embedded System Environment project](http://www.cecs.uci.edu/~ese) |
| [University of California, Los Angeles](http://www.ucla.edu/) | Jason Cong | xPilot behavioral synthesis system |
| [University of California, Los Angeles](http://www.ucla.edu/) | Jens Palsberg |  |
| [University of Illinois at Urbana-Champaign](http://www.uiuc.edu) | [Vikram Adve's Research Group](http://llvm.cs.illinois.edu/~vadve/Home.html) | [Secure Virtual Architecture/SAFECode](http://sva.cs.illinois.edu) |
| [University of Illinois at Urbana-Champaign](http://www.uiuc.edu) | Ravi Iyer's Research Group | Runtime monitoring for software reliability |
| [University of Illinois at Urbana-Champaign](http://www.uiuc.edu) | Maria Garzaran's Research Group | Automatic replication for software reliability |
| [University of Illinois at Urbana-Champaign](http://www.uiuc.edu) | Sanjay Patel's Research Group | Microarchitecture research |
| [The University of Kansas](http://www.ku.edu) | Wesley Peck | MicroBlaze backend for use on Xilinx FPGAs |
| [The University of Pennsylvania](http://www.upenn.edu/) | Santosh Nagarakatte, Jianzhou Zhao, Milo M K Martin, and Steve Zdancewic | [SoftBound](http://www.cis.upenn.edu/acg/softbound) |
| [University of Texas at Austin](http://www.utexas.edu/) | Calvin Lin's Research Group | [Turnkey Pointer Analysis](http://www.cs.utexas.edu/~lin/research.html#Pointers) |

## Educational Users

<!-- Go Bucky! -->

*   [Anna University, Chennai, India](http://www.annauniv.edu/)
*   [University of California, Los Angeles](http://www.ucla.edu/)
*   [Carnegie Mellon University](http://www.cmu.edu/)
*   [University of Illinois at Urbana-Champaign](http://www.uiuc.edu)
*   [Indian Institute of Technology, Bombay](http://www.cse.iitb.ac.in/)
*   [Indian Institute of Technology, Madras](http://www.cse.iitm.ac.in/)
*   [University of New South Wales, Australia](http://www.unsw.edu.au/)
*   [University of Utah](http://www.utah.edu/)
*   [University of Wisconsin, Madison](http://www.wisc.edu/)

<!-- *********************************************************************** -->

* * *

[LLVM Development List](mailto:llvm-dev@lists.llvm.org)
