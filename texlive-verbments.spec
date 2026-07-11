%global tl_name verbments
%global tl_revision 23670

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Syntax highlighting of source code in LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/verbments
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verbments.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verbments.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides an environment for syntax highlighting source code
in LaTeX documents. The highlighted source code output is formatted via
powerful Pygments library of the Python language.

