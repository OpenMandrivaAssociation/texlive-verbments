Name:		texlive-verbments
Version:	23670
Release:	2
Summary:	Syntax highlighting of source code in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verbments
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbments.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbments.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides an environment for syntax highlighting
source code in LaTeX documents. The highlighted source code
output is formatted via powerful Pygments library of the Python
language.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/verbments/verbments.sty
%doc %{_texmfdistdir}/doc/latex/verbments/README
%doc %{_texmfdistdir}/doc/latex/verbments/verbments.pdf
%doc %{_texmfdistdir}/doc/latex/verbments/verbments.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
