---
permalink: "builds/index.html"
---
LLVM Snapshot Builds 

# LLVM Snapshot Builds

## License

[LLVM](https://llvm.org/) is distributed under an open source [License](https://llvm.org/releases/11.0.0/LICENSE.TXT).

## Other builds

See the [releases](../releases/) page for stable releases, and the [apt](../apt/) page for nightly packages for Debian and Ubuntu.

## Windows snapshot builds

**The snapshot builds are no longer updated. Use the [regular releases](../releases/) instead.**

We provide a periodically updated installer for Windows:

[Windows installer (64-bit)](https://prereleases.llvm.org/win-snapshots/LLVM-12.0.0-6923b0a7-win64.exe) [(.sig)](https://prereleases.llvm.org/win-snapshots/LLVM-12.0.0-6923b0a7-win64.exe.sig), based on Git commit [6923b0a7](https://github.com/llvm/llvm-project/commit/6923b0a7) (28 August 2020).

If there is a previous version installed, the installer provides an option to uninstall it.

Currently, the package includes [clang](https://clang.llvm.org), [clang-format](https://clang.llvm.org/docs/ClangFormat.html), [lld](https://lld.llvm.org), and the [AddressSanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer) runtime from [compiler-rt](https://compiler-rt.llvm.org). Eventually it should grow to encompass other Clang tools, and possibly other LLVM projects such as [libc++](https://libcxx.llvm.org).

To use the LLVM toolchain from Visual Studio after running the installer above, install the [LLVM Compiler Toolchain Visual Studio extension](https://marketplace.visualstudio.com/items?itemName=LLVMExtensions.llvm-toolchain) (supports Visual Studio 2017 and later), select a project in Solution Explorer, open its Property Page (Alt+F7 by default), and in the "General" section of "Configuration Properties" change "Platform Toolset" to "llvm". Alternatively, invoke MSBuild with `/p:PlatformToolset=llvm` to try out the toolchain without modifying the project files.

A [32-bit version](https://prereleases.llvm.org/win-snapshots/LLVM-12.0.0-6923b0a7-win32.exe) [(.sig)](https://prereleases.llvm.org/win-snapshots/LLVM-12.0.0-6923b0a7-win32.exe.sig) of the installer is also available.

The .sig files are PGP signatures using key [345AD05D](https://releases.llvm.org/11.0.0/hans-gpg-key.asc).

## clang-format plugin for Visual Studio

**The plugin is no longer updated. Visual Studio has [built-in support for clang-format](https://devblogs.microsoft.com/cppblog/clangformat-support-in-visual-studio-2017-15-7-preview-1/) since 2017 15.7 Preview 1.**

We also provide a standalone Visual Studio plugin for clang-format. It requires Visual Studio 2012 Professional or later. Notably, the Express editions do not support plugins.

[Visual Studio plugin installer](https://prereleases.llvm.org/win-snapshots/ClangFormat-6923b0a7.vsix) [(.sig)](https://prereleases.llvm.org/win-snapshots/ClangFormat-6923b0a7.vsix.sig), based on based on Git commit [6923b0a7](https://github.com/llvm/llvm-project/commit/6923b0a7). This is also available [at the Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=LLVMExtensions.ClangFormat). A separate build of the clang-format binary is available as [clang-format-6923b0a7.exe](https://prereleases.llvm.org/win-snapshots/clang-format-6923b0a7.exe) [(.sig)](https://prereleases.llvm.org/win-snapshots/clang-format-6923b0a7.exe.sig).

<!-- rel_container --> <!--#include virtual="../attrib.incl" -->
