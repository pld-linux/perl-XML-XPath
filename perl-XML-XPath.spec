%include	/usr/lib/rpm/macros.perl
%define         pdir XML
%define         pnam XPath
Summary:	XML::XPath - a set of modules for parsing and evaluating XPath statements
Summary(pl):	XML::XPath - zestaw modu³ów do parsowania i obliczania wyra¿eñ XPath
Name:		perl-%{pdir}-%{pnam}
Version:	1.12
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This module aims to comply exactly to the XPath specification at
http://www.w3.org/TR/xpath and yet allow extensions to be added
in the form of functions. Modules such as XSLT and XPointer may
need to do this as they support functionality beyond XPath.

%description -l pl
Ten modu³ ma byæ zgodny ze specyfikacj± XPath (dostêpn± pod
http://www.w3.org/TR/xpath) i pozwala na dodawanie rozszerzeñ
w postaci funkcji. Modu³y takie jak XSLT i XPointer mog± byæ
potrzebne do tego, jako ¿e obs³uguj± funkcjonalno¶æ spoza XPath.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf TODO README 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
