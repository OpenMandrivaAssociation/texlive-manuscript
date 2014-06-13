# revision 17486
# category Package
# catalog-ctan /macros/latex/contrib/manuscript
# catalog-date 2010-03-14 23:46:18 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-manuscript
Version:	20100314
Release:	7
Summary:	Emulate look of a document typed on a typewriter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/manuscript
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manuscript.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manuscript.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manuscript.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is designed for those who have to submit
dissertations, etc., to institutions that still maintain the
typewriter is the summit of non-professional printing.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/manuscript/manuscript.sty
%doc %{_texmfdistdir}/doc/latex/manuscript/README
%doc %{_texmfdistdir}/doc/latex/manuscript/manuscript.pdf
#- source
%doc %{_texmfdistdir}/source/latex/manuscript/Makefile
%doc %{_texmfdistdir}/source/latex/manuscript/manuscript.drv
%doc %{_texmfdistdir}/source/latex/manuscript/manuscript.dtx
%doc %{_texmfdistdir}/source/latex/manuscript/manuscript.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100314-2
+ Revision: 753736
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100314-1
+ Revision: 718953
- texlive-manuscript
- texlive-manuscript
- texlive-manuscript
- texlive-manuscript

