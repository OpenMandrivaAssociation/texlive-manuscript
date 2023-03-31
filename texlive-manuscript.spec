Name:		texlive-manuscript
Version:	36110
Release:	2
Summary:	Emulate look of a document typed on a typewriter
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/manuscript
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manuscript.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manuscript.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/manuscript.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/manuscript
%doc %{_texmfdistdir}/doc/latex/manuscript
#- source
%doc %{_texmfdistdir}/source/latex/manuscript

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
