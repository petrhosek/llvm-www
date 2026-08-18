---
permalink: "devmtg/2007-05/index.html"
---
<!-- FIXME: we need to add the meta tag to the head tag, which we can't do with the current web page. Duplicate this block and hope it all works out. -->  The LLVM Compiler Infrastructure Project   <!--#include virtual="../../header.incl" --> <!-- <html> <head> <link rel="stylesheet" href="http://llvm.org/llvm.css" type="text/css"> </head>-->

# May 25, 2007LLVM Developers' Meeting Proceedings

~60 people attended.

These videos are also viewable on [youtube](http://www.youtube.com/view_play_list?p=AA11ACE45D6B0E4C).

Chris Hanson contributed a [podcast feed](podcast.xml) that you [subscribe to](itpc://llvm.org/devmtg/2007-05/podcast.xml) in iTunes or on Apple TV.

<!-- *********************************************************************** --> <!-- *********************************************************************** -->

# Proceedings

All videos are presented in QuickTime format, all slides are in PDF format.

[video](https://youtu.be/FNtmemyeEHY)Vikram Adve  
Chris Lattner **A brief history of LLVM** - During this brief session, Vikram and Chris (the originators of LLVM) presented a brief history of the early history of LLVM. [video](https://youtu.be/nl5SXEDkMEc)Everyone **Introductions** - Everyone introduced themselves to the group.

### Break

[slides](03-Patel-Passmanager.pdf)  
[video](https://youtu.be/4yzjAXiMbvk) Devang Patel **Demystifying The LLVM Pass Manager** - The PassManager, which manages the execution of all LLVM passes, was recently revised to be simpler and more useful. This talk will help you understand what the new pass manager does and how to use it. [slides](04-Cheng-Codegen.pdf)  
[video](https://youtu.be/ZWmHZD_-fZ0) Evan Cheng **The LLVM Code Generator** - An overview of the LLVM generic code generator design and changes to it that are coming in the future. [slides](05-Lewycky-Predsimplify.pdf)  
[video](https://youtu.be/y4xRGfFZT-0) Nick Lewycky **Introduction To Predicate Simplifier** - A review of the design and implementation of LLVM's Predicate Simplifier Pass, otherwise known as VRP (Value Range Propagation). [video](https://youtu.be/cRIuetDrCq0)  
[slides](06-Spencer-HLVM.pdf) Reid Spencer **HLVM** - An overview of HLVM, its current status and its goals after integration with LLVM.

### Lunch

[slides (PDF)](07-Michel-Cell.pdf)Scott Michel **The Cell BE Symbiotic Processor Element Backend** - A presentation of the practice and experience that resulted from Aerospace's implementation of an LLVM back-end Target for the Cell BE Symbiotic Processor Element. [video](https://youtu.be/sRvetnQhXPQ)  
[slides (PDF)](08-Criswell-SVA.pdf)  
[slides (PPT)](08-Criswell-SVA.ppt) John Criswell **Secure Virtual Architecture** - A presentation on our research to create a virtual machine that operates below the operating system and a brief introduction to some of the novel security capabilities that our architecture can enable. [slides](09-Naroff-CFE.pdf)  
[video](https://youtu.be/Xx7zFn31PLQ) Steve Naroff **New LLVM C Front-end** - This talk describes a new from-scratch C frontend (which is aiming to support Objective C and C++ someday) for LLVM, built as a native part of the LLVM system and in the LLVM design style. [slides](10-Lattner-OpenGL.pdf) [video](https://youtu.be/TPyo6NYNYis) Chris Lattner **LLVM in OpenGL and for Dynamic Languages** - A presentation put together in 10 minutes, talking about LLVM being used for OpenGL and some speculative talk about dynamic languages.

#### Break

[video](https://youtu.be/T5GgX8tE3R8)Christopher Lamb **Concurrency Primitives** - For multi-threaded shared memory models. [video](https://youtu.be/npCXLaGdArY)Reid Spencer **LLVM Roadmap** - Does the development community care to disclose and maintain advance information about what is being worked on? [video](https://youtu.be/CIp103RdKic)Chris Lattner **Adoption Goals** - While our adoption has increased greatly recently, we're still tiny compared to other compiler and virtual machine systems. [video](https://youtu.be/uTVcG0qVS0I)Reid Spencer  
Chris Lattner**Project Management, License, Naming**[video](https://youtu.be/iINSIqwaQX0)Chris Lattner**Feedback on the Meeting**

<!-- *********************************************************************** -->

# Attendees

The table below lists the confirmed attendees for the meeting.

<table><tbody><tr style="vertical-align: top"><td><table class="www"><tbody><tr><th colspan="2">Confirmed Attendees</th></tr><tr><th>Name</th><th>Organization</th></tr><tr><td>Vikram Adve</td><td>UIUC</td></tr><tr><td>Bob Archer</td><td>Adobe Systems Incorporated.</td></tr><tr><td>Owen Anderson</td><td>Independent</td></tr><tr><td>Ryan Brown</td><td>Google</td></tr><tr><td>Evan Cheng</td><td>Apple Inc.</td></tr><tr><td>Josh Conner</td><td>Apple Inc.</td></tr><tr><td>John Criswell</td><td>UIUC</td></tr><tr><td>Kat Danielson</td><td>Apple Inc.</td></tr><tr><td>Mike Engler</td><td>Adobe Systems Incorporated.</td></tr><tr><td>Rafael Espíndola</td><td>Google</td></tr><tr><td>Tomas Evensen</td><td>Wind River</td></tr><tr><td>Samuel Figueroa</td><td>Apple Inc.</td></tr><tr><td>Han Gao</td><td>Adobe Systems Incorporated.</td></tr><tr><td>Dan Gohman</td><td>Cray Inc.</td></tr><tr><td>Lang Hames</td><td>University of Sydney</td></tr><tr><td>Stuart Hastings</td><td>Apple Inc.</td></tr><tr><td>Victor Hernandez</td><td>Apple Inc.</td></tr><tr><td>Robert Hundt</td><td>Google</td></tr><tr><td>Dale Johannesen</td><td>Apple Inc.</td></tr><tr><td>Ted Kremenek</td><td>Independent</td></tr><tr><td>Christopher Lamb</td><td>Ageia Technologies, Inc.</td></tr><tr><td>Chris Lattner</td><td>Apple Inc.</td></tr><tr><td>Tanya Lattner</td><td>Independent</td></tr><tr><td>Andrew Lenharth</td><td>UIUC</td></tr><tr><td>Julien Lerouge</td><td>Apple Inc.</td></tr><tr><td>Nick Lewycky</td><td>Independent</td></tr></tbody></table></td><td><table class="www"><tbody><tr><th colspan="2">Confirmed Attendees</th></tr><tr><th>Name</th><th>Organization</th></tr><tr><td>Efrem Lipkin</td><td>CoDesign</td></tr><tr><td>Gabe McArthur</td><td>Independent</td></tr><tr><td>Paul McJones</td><td>Adobe Systems Incorporated.</td></tr><tr><td>Scott Michel</td><td>Aerospace</td></tr><tr><td>Dan Moniz</td><td>Matasano</td></tr><tr><td>Alireza Moshtaghi</td><td>Microchip Technology</td></tr><tr><td>Lakshmankumar Mukkavilli</td><td>Cisco Systems</td></tr><tr><td>Robert Mykland</td><td>Ascenium Corp.</td></tr><tr><td>Steve Naroff</td><td>Apple Inc.</td></tr><tr><td>Devang Patel</td><td>Apple Inc.</td></tr><tr><td>Fernando Magno Quintao Pereira</td><td>UCLA</td></tr><tr><td>Jeff Poznanovic</td><td>Cray Inc.</td></tr><tr><td>Ron Price</td><td>Apple Inc.</td></tr><tr><td>Chuck Rose</td><td>Adobe Systems Incorporated.</td></tr><tr><td>Mark Schimmel</td><td>Wind River</td></tr><tr><td>Reid Spencer</td><td>Independent</td></tr><tr><td>Raju Subbian</td><td>Wind River</td></tr><tr><td>Mark Thomas</td><td>Aerospace</td></tr><tr><td>Sarah Thompson</td><td>NASA, Ames Research Center</td></tr><tr><td>Andrew Trick</td><td>HP</td></tr><tr><td>Bill Wendling</td><td>Apple Inc.</td></tr><tr><td>Marcel Weiher</td><td>MetaObject</td></tr><tr><td>James Weisner</td><td>Ascenium Corp.</td></tr><tr><td>Calum Wilkie</td><td>Microchip Technology</td></tr><tr><td>Scott Williams</td><td>Google</td></tr></tbody></table></td></tr></tbody></table>

**Total confirmed: 51**

*   Michael McCracken
*   Kelly Wilson
*   Unconfirmed 1

**Total unconfirmed: 3**

<!-- *********************************************************************** -->

* * *

<!--#include virtual="../../footer.incl" -->
