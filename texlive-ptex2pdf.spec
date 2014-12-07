# revision 30321
# category Package
# catalog-ctan /language/japanese/ptex2pdf
# catalog-date 2013-05-07 20:01:57 +0200
# catalog-license gpl2
# catalog-version 0.4
Name:		texlive-ptex2pdf
Version:	0.4
Release:	9
Summary:	Convert Japanese TeX documents to PDF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/japanese/ptex2pdf
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex2pdf.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ptex2pdf.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-ptex2pdf.bin = %{EVRD}

%description
The Lua script provides system-independent support of Japanese
typesetting engines in TeXworks. As TeXworks typesetting setup
does not allow for multistep processing, this script runs one
of the ptex-based programs (ptex, uptex, eptex, platex,
uplatex) followed by dvipdfmx.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/ptex2pdf
%{_texmfdistdir}/scripts/ptex2pdf/ptex2pdf.lua
%doc %{_texmfdistdir}/doc/latex/ptex2pdf/COPYING
%doc %{_texmfdistdir}/doc/latex/ptex2pdf/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/ptex2pdf/ptex2pdf.lua ptex2pdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
