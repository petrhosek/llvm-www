---
layout: "default.html"
permalink: "devmtg/2008-08/index.html"
---
# 2008 LLVM Developers' Meeting

1.  [Proceedings](#proceedings)
2.  [Attendees](#attendees)

*   **What**: The second general meeting of LLVM Developers and Users.
*   **Why**: To get acquainted, learn how LLVM is used, and exchange ideas.
*   **When**: August 1, 2008
*   **Where**: Apple Campus

**Sponsored By: Apple, Google, Adobe, University of Illinois**

The meeting served as a forum for [LLVM](http://llvm.org) developers and users to get acquainted, learn how LLVM is used, and exchange ideas about LLVM, future extensions, and its (potential) applications.

# Proceedings

The day was structured to have general overview/introduction talks about some major LLVM subsystems, followed by talks on applications of LLVM for various specific projects.

In addition to being available here, the videos are also available [on youtube](http://www.youtube.com/view_play_list?p=E05430D58DF9A720).

| Media | Who | Description |
| --- | --- | --- |
| \[[Video](https://youtu.be/13iB2FiFCdo)\] | Chris Lattner<br>*Apple, Inc.* | **Welcome and Thanks** - A brief welcome, thanks and some logistics for the day. |
| \[[Slides](Naroff_Clang.pdf)\] \[[Video](https://youtu.be/qYe_w2wt54U)\] | Steve Naroff<br>*Apple, Inc.* | **Clang Internals** - [Clang](http://clang.llvm.org/) is is a new C/ObjC/C++ front-end in development as part of the LLVM project. This talk describes its current status, high level architecture, and how its Abstract Syntax Trees (ASTs) work. |
| \[[Slides](Gohman_CodeGenAndSelectionDAGs.pdf)\] \[[Video](https://youtu.be/Y5kbSDi7qb8)\] | Dan Gohman<br>*Apple, Inc.* | **CodeGen Overview and Focus on SelectionDAGs** - A high-level overview of the LLVM Code Generator, with specific depth and overview in the area of the SelectionDAG phases. |
| \[[Slides](Cheng_RegisterAllocation.pdf)\] \[[Video](https://youtu.be/ktXFOlyEOtY)\] | Evan Cheng<br>*Apple, Inc.* | **LLVM Register Allocation** - Description of the current design and architecture of the LLVM register allocator. The talk discusses some optimizations that are currently performed as well as describing future directions and where we'd like to go. |
| \[[Slides](Begeman_EfficientJIT.pdf)\] \[[Video](https://youtu.be/ZPw6JYIQfMo)\] | Nate Begeman<br>*Apple, Inc.* | **Building an Efficient JIT** - LLVM provides many of the facilities that you need to assemble a JIT for various purposes. This talk walks you through construction of a simple JIT for C code (based on Clang) and talks about some of the important APIs for doing this. After getting it working, Nate describes the efficiency implications of various choices and describes how to dramatically improve the efficiency of the first implementation. |
| \[[Slides](Rose_AdobePixelBender.pdf)\] \[[Video](https://youtu.be/bzhXXfUbJv8)\] | Chuck Rose III<br>*Adobe Inc.* | **Adobe Image Foundation and Adobe PixelBender** - Adobe Image Foundation is a system for JIT compiling code written in the Adobe PixelBender language to run on the CPU and GPU. This talk describes how AIF and PixelBender work and how it uses LLVM to evaluate dependencies, reason about dirty regions of images, and do pixel processing when a GPU cannot handle a program. |
| \[[Slides](Kremenek_StaticAnalyzer.pdf)\] \[[Video](https://youtu.be/_HTcWKqRXXs)\] | Ted Kremenek<br>*Apple, Inc.* | **Finding Bugs with the Clang Static Analyzer** - The Clang Static Analyzer is a standalone tool that find bugs in C and Objective-C programs. The analyzer is 100% open source and part of the Clang project (a new C/Objective-C/C++ frontend for LLVM). Although still very early in its development, the tool has been effective at finding thousands of bugs in real-world C and Objective-C programs. This talk presents a high-level overview of the goals, implementation, and current status of the tool. |
| \[[Slides](Lopes_PHP-JIT-InTwoDays.pdf)\] \[[Video](https://youtu.be/NDm5cBpYIqw)\] | Nuno Lopes<br>*Instituto Superior Tecnico* | **Building a JIT compiler for PHP in 2 days** - This talk describes the implementation of the PHP interpreter and how it was easily changed into an LLVM JIT. This discusses why the facilities that LLVM provides make this easy, and gives some (very early) results. |
| \[[Slides](Korobeynikov_LLVMC2-CompilerDriver.pdf)\] \[[Video](https://youtu.be/f9MQI9IUy_M)\] | Anton Korobeynikov<br>*Saint Petersburg State University* | **llvmc2 Compiler Driver** - 'llvmc2' is the LLVM Compiler Driver, which is useful to people building new languages and tools from the LLVM toolchain. This talk describes the constraints and purpose of a compiler driver and discusses how llvmc2 fills the needs and works with those constraints. Finally, the talk describes some of the low-level architecture and future directions of llvmc2. |
| \[[Slides](Criswell_SVA.pdf)\] \[No video\] | John Criswell<br>*University of Illinois* | **SVA: Using LLVM to Provide Memory Safety** - [SVA](http://sva.cs.uiuc.edu/) is an aggressive approach to provide an efficient compiler-based system with memory safety on top of the LLVM IR. *Unfortunately, video is not available due to camera problems.* |
| \[[Slides](Geoffray_VMKitProject.pdf)\] \[[Video](https://youtu.be/XHRd6Qhwbyw)\] | Nicolas Geoffray<br>*Universite Pierre et Marie Curie* | **The VMKit Project** - VMKit is an implementation of the Java and .NET Virtual Machines that use LLVM to optimize and JIT compile the code. This talk describes how VMKit integrates components from various systems, how bytecode translation works, describes the current performance status of the system, and discusses areas for future extension. |
| \[[Slides](Sander_HW-SW-CoDesignflowWithLLVM.pdf)\] \[[Video](https://youtu.be/6-Cp6MlLu-I)\] | Tim Sander<br>*Technischen Universitat Darmstadt* | **Designflow: using LLVM to compile to Hardware** - This project uses LLVM to compile code to a mixed hardware and software implementation. This detects pieces of programs that may be efficiently compiled to VHDL and synthesized them onto an FPGA. The rest of the program is compiled to PowerPC code and uses to drive the FPGA. The system automatically handles data migration and other handshaking between the two systems. |
| \[[Slides](Petersen_FlashCCompiler.pdf)\] \[[Video](https://youtu.be/f7xniMC4J5U)\] | Scott Petersen<br>*Adobe Inc.* | **Flash C Compiler: Compiling C code to the Adobe Flash Virtual Machine** - FlaCC is a research project that compiles C code to ActionScript using llvm-gcc with a custom flash code generator. This enables almost arbitrary C and C++ code to be executed safely and efficiently within a Flash container on web pages. This talk describes the implementation of the system and shows several compelling examples that use it to run other language and CPU interpreters within Flash as well as run existing large programs within C. The demos are also extremely impressive :). |

# Attendees

This table lists all attendees that have registered for this year's conference.

| Name | Organization |
| --- | --- |
| Talin - | Google |
| Vikram Adve | University of Illinois at Urbana-Champaign |
| Nathan Allan | Alphora / Database Consulting Group |
| Owen Anderson | Apple, Inc. |
| Chris Aoki | Sun Microsystems, Inc. |
| Michael AuYeung | The Aerospace Corporation |
| Joseph Battelle | Logitech |
| Nate Begeman | Apple, Inc. |
| Kris Bell | Apple, Inc. |
| Jay Bharadwaj | Intel Corporation |
| Robert Bowdidge | Self |
| Max Burke | Electronic Arts |
| Anders Carlsson | Apple, Inc. |
| Chandler Carruth | Google, Inc |
| Evan Cheng | Apple, Inc. |
| Andy Chou | Coverity, Inc. |
| Eric Christopher | Apple, Inc |
| Jan Civlin | AMD |
| Marshall Clow | Qualcomm, Inc. |
| John Criswell | University of Illinois |
| Brooks Davis | The Aerospace Corporation / The FreeBSD Project |
| Andrew Donoho | IBM |
| Stefanus Du Toit | RapidMind |
| Daniel Dunbar | Stanford University / Apple Inc. |
| Bernardo Elayda | Wind River |
| Ken Ferry | Apple, Inc. |
| Tim Foley | Self |
| Chandrashekhar Garud | Sun Microsystems |
| Nicolas Geoffray | Université Pierre et Marie Curie |
| Dan Gohman | Apple, Inc. |
| John Golenbieski | Self |
| Eric Gouriou | Apple, Inc. |
| Ryan Govostes | Alacatia Labs, Inc. |
| David Greene | Cray, Inc. |
| Jim Grosbach | Apple, Inc. |
| Vinod Grover | NVIDIA |
| Alfonso Guerra | Apokalypse Software Corp. |
| Mohammad Reza Haghighat | Intel Corporation |
| Chris Hanson | Apple, Inc. |
| Kurt Harriman | Greenplum |
| Stuart Hastings | Apple, Inc. |
| John Hixson | University of the Pacific |
| Robert Hundt | Google |
| Oliver Hunt | Apple, Inc. |
| Changhao Jiang | Facebook Inc. |
| dale johannesen | Apple, Inc. |
| Francois Jouaux | Apple, Inc. |
| Benjamin King | DemandEO.com |
| George King | arboreality.net |
| Nick Kledzik | Apple, Inc. |
| Anton Korobeynikov | Saint Petersburg State University |
| Ted Kremenek | Apple, Inc. |
| Chris Lattner | Apple, Inc. |
| Tanya Lattner | Apple, Inc. |
| Andrew Lenharth | University of Illinois |
| Mark Leone | Self |
| Julien Lerouge | Apple, Inc. |
| Nicholas Lewycky | Google |
| Nuno Lopes | Instituto Superior Técnico |
| olivier maggi | numeriz |
| Dmitri Makarov | AMD |
| Ali Mashtizadeh | VMware, Inc. |
| Henry Mason | Apple, Inc. |
| Scott Michel | Aerospace |
| Keir Mierle | Google |
| Daniel Moniz | Unified Research |
| Marcel Moolenaar | The FreeBSD Project |
| Alireza Moshtaghi | Microchip Technology |
| Ginger Myles | Apple, Inc. |
| Prashanth Narayanaswamy | Sun Microsystems |
| Steve Naroff | Apple, Inc. |
| Ted Neward | Neward & Associates |
| Jay O'Conor | Self |
| Maksim Panchenko | Sun Microsystems |
| Ji Young Park | AMD Inc. |
| Terence Parr | University of San Francisco |
| Devang Patel | Apple, Inc. |
| Scott Petersen | Adobe Systems, Inc. |
| Richard Phillips | Wolfram Research |
| Ernest Prabhakar | Apple, Inc. |
| Gregor Purdy | Apple, Inc. |
| Paul Ramsey | Dreamworks Animation |
| Joseph Ranieri | Alacatia Labs, Inc. |
| Nicholas Ray | Windly Games. |
| Rob Reynolds | Alphora / Database Consulting Group |
| Bryn Rhodes | Alphora / Database Consulting Group |
| Stephen Richardson | Mucho Consultio, SA de CV |
| Charles Rose | Adobe Systems Incorporated |
| Tim Sander | Integrated Systems and Circuits, Technische Universität Darmstadt |
| Shirish Seetharam | Cisco Systems |
| Mitesh Shah | ARC International |
| Craig Smith | National Instruments |
| Evan Smyth | DreamWorks Animation |
| Pratik Solanki | Apple, Inc. |
| Mike Stump | Apple, Inc. |
| Andre Sublette | Self |
| Richard Sweet | Adobe Systems |
| Yan Tang | VMware |
| Caroline Tice | Apple, Inc. |
| Ross Towle | Sun |
| Andrew Trick | Hewlett-Packard |
| Hemant Trivedi | Silicon Informatics, Inc |
| Erick Tryzelaar | self |
| Mon Ping Wang | Apple, Inc. |
| Douglas Watt | XMOS Semiconductor |
| Patrick Webster | Self |
| Marcel Weiher | Apple, Inc. |
| Sam Weinig | Apple, Inc. |
| Steve Weissinger | Wind River |
| Bill Wendling | Apple, Inc. |
| Hans-Martin Will | Vincent 3D Rendering Library (OSS project) |
| Pen-Chung Yew | University of Minnesota |
| Anna Zaks | New York University |
| Mark Zarins | GrammaTech |
| Robert Zeh | None |
| Jie Zhang | Greenplum Inc. |
| Bixia Zheng | AMD |
| Vojin Zivojnovic | ARM |

**Total Confirmed: 118**

<!-- *********************************************************************** -->

* * *
