%global tl_name ptex2pdf
%global tl_revision 65953
%global tl_bin_links ptex2pdf:%{_texmfdistdir}/scripts/ptex2pdf/ptex2pdf.lua

Name:		texlive-%{tl_name}
Epoch:		1
Version:	20200520.0
Release:	%{tl_revision}.1
Summary:	Convert Japanese TeX documents to PDF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/jptex/generic/ptex2pdf
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex2pdf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex2pdf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ptex2pdf.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The Lua script provides system-independent support of Japanese
typesetting engines in TeXworks. As TeXworks typesetting setup does not
allow for multistep processing, this script runs one of the ptex-based
programs (ptex, uptex, eptex, platex, uplatex) followed by dvipdfmx.

