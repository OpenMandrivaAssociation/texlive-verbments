# revision 23670
# category Package
# catalog-ctan /macros/latex/contrib/verbments
# catalog-date 2011-08-23 07:18:10 +0200
# catalog-license lppl1.2
# catalog-version 1.2
Name:		texlive-verbments
Version:	1.2
Release:	6
Summary:	Syntax highlighting of source code in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verbments
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbments.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbments.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 757417
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 719884
- texlive-verbments
- texlive-verbments
- texlive-verbments

