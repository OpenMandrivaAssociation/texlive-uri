# revision 21608
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-uri
Version:	20111104
Release:	8
Summary:	TeXLive uri package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uri.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uri.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uri.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive uri package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uri/uri.sty
%doc %{_texmfdistdir}/doc/latex/uri/README
%doc %{_texmfdistdir}/doc/latex/uri/uri-example.pdf
%doc %{_texmfdistdir}/doc/latex/uri/uri-example.tex
%doc %{_texmfdistdir}/doc/latex/uri/uri.pdf
#- source
%doc %{_texmfdistdir}/source/latex/uri/ltxdoc.cfg
%doc %{_texmfdistdir}/source/latex/uri/uri.drv
%doc %{_texmfdistdir}/source/latex/uri/uri.dtx
%doc %{_texmfdistdir}/source/latex/uri/uri.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 757327
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719860
- texlive-uri
- texlive-uri
- texlive-uri
- texlive-uri

