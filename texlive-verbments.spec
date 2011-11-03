# revision 23670
# category Package
# catalog-ctan /macros/latex/contrib/verbments
# catalog-date 2011-08-23 07:18:10 +0200
# catalog-license lppl1.2
# catalog-version 1.2
Name:		texlive-verbments
Version:	1.2
Release:	1
Summary:	Syntax highlighting of source code in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verbments
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbments.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbments.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides an environment for syntax highlighting
source code in LaTeX documents. The highlighted source code
output is formatted via powerful Pygments library of the Python
language.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/verbments/verbments.sty
%doc %{_texmfdistdir}/doc/latex/verbments/README
%doc %{_texmfdistdir}/doc/latex/verbments/verbments.pdf
%doc %{_texmfdistdir}/doc/latex/verbments/verbments.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
