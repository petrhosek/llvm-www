---
layout: "default.html"
permalink: "SeasonOfDocs.html"
---
<!-- *********************************************************************** -->

# Google Season of Docs 2019

<!-- *********************************************************************** -->

The LLVM Project is hopeful to participate in the inaugural Google Season of Docs program. This program's goal is to foster collaboration between open source project's and technical writers. This program has the potential to make a huge impact. In a [2017 Survey of Open Source Projects](https://opensourcesurvey.org/2017), it found that 93% of those surveyed said that “ incomplete or outdated documentation is a pervasive problem." However, despite this opinion, only 60% of those surveyed said they rarely or never had contributed documentation. This is a troubling discovery as documentation is vital to the long term health of an open source project.

Documentation is essential for bringing in new contributors to a project. It help newcomers learn the basics of how to use a project, how to contribute back to a project, and the overall governance and licensing of an open source project. Quality documentation is key to keeping developers as projects continue to evolve over time.

The LLVM Project is unfortunately not exempt from having incomplete, outdated, or poor documentation. Recently, the LLVM Foundation hosted a working workshop through its Women in Compilers and Tools initiative that focused on removing barriers for newcomers through improving LLVM project documentation. During this workshop, many great ideas were discussed and rough outlines proposed for improving some of our key newcomer documentation. It is through this workshop and conversations with the LLVM community at large that a list of potential documentation projects has been created.

It is our hope that we will be paired with a technical writer on one or two of these documentation projects below and ultimately improve the experience for newcomers and experienced developers alike.

If you have any questions, are interested in becoming a mentor, or project suggestions - please contact us via gsdocs@llvm.org

<!-- *********************************************************************** -->

## Documentation Projects

<!-- *********************************************************************** -->

### Revise LLVM Getting Started Guide

**Mentors: Tanya Lattner, ...**

**Description of the project:** The LLVM Getting Started Guide is in need of some serious revision. It is currently extremely lengthy, hard to read, and not very inviting for newcomers. During a recent working workshop focused on documentation improvements, a group of developers looked at the guide and made some suggestions for potential changes. One such idea was to break the guide up into varying levels of difficulty to address different audiences such as: beginner, intermediate and advanced. Other ideas are captured in the related material below.

**Related Material:**

*   [Getting Started Guide](https://llvm.org/docs/GettingStarted.html): Current document on llvm.org
*   [Ideas from the workshop](https://docs.google.com/document/d/1Prx1PLLU7VB0w2gBsAv0uB5MwX2Z7g9UIMTIUKZumcg/edit)
*   [Mockups and examples of new getting started guides](https://docs.google.com/document/d/1sgnnwjU-ESvAQpQzeFY5l02OVllOlJbMm1E4YzylgC4/edit)
*   Various addendums to the main getting starting guide; [Getting Started with the LLVM System using Microsoft Visual Studio](https://llvm.org/docs/GettingStartedVS.html), [Building LLVM with CMake](https://llvm.org/docs/CMake.html), and many notes listed [here](https://llvm.org/docs/).

### LLVM Overview System Documentation

**Mentors: Tanya Lattner, ...**

**Description of the project:** LLVM is a large and constantly changing software project. There are really only a few papers and a book chapter that describe the system as a whole and give a good overview. We should develop more current documentation using Sphinx to document and describe the LLVM infrastructure.

**Related Material:**

*   Most useful documentation - [a book chapter about LLVM](https://www.aosabook.org/en/llvm.html)
*   [2008 presentation on LLVM](https://llvm.org/pubs/2008-10-04-ACAT-LLVM-Intro.html)
*   [2004 CGO Paper on LLVM](https://llvm.org/pubs/2004-01-30-CGO-LLVM.html)
*   [2002 Original thesis on LLVM](https://llvm.org/pubs/2002-12-LattnerMSThesis.html)

### Restructure LLVM documentation index and documentation style guide

**Mentors: Tanya Lattner, ...**

**Description of the project:** Currently, all LLVM docs are listed on one page with poor organization and indexing/tagging. We would like the high level organization of the docs to be revised and edited to be more easily navigated. In addition, we would like have a updated sphinx style guide for developing new LLVM documentation and to improve the readability and accessibility of all current LLVM documentation.

**Related Material:**

*   [Documentation Index](https://llvm.org/docs/)
*   [Sphinx Quickstart Guide](https://llvm.org/docs/SphinxQuickstartTemplate.html)

### Clang Newcomer Documentation

**Mentors: Tanya Lattner, ...**

**Description of the project:** The Clang project could use some revisions to its documentation directly related to newcomers. In particular, we should migrate the getting involved page to a more standard Contributing page and try to more directly integrate with the LLVM documentation on submitting patches and developer standards. These pages should also convert to Sphinx. The content of the main Clang webpage could also use an overhaul to better explain what Clang is.

**Related Material:**

*   [Clang main page](https://clang.llvm.org/index.html)
*   [Getting Involved with Clang](https://clang.llvm.org/get_involved.html)
