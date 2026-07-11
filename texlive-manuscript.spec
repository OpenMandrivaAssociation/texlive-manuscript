%global tl_name manuscript
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	Emulate look of a document typed on a typewriter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/manuscript
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/manuscript.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/manuscript.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/manuscript.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is designed for those who have to submit dissertations,
etc., to institutions that still maintain the typewriter is the summit
of non-professional printing.

