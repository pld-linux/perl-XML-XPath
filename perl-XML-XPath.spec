#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	XPath
Summary:	XML::XPath - a set of modules for parsing and evaluating XPath statements
Summary(pl):	XML::XPath - zestaw modu³ów do parsowania i obliczania wyra¿eñ XPath
Name:		perl-XML-XPath
Version:	1.13
Release:	3
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b5919d9220d83982feb6e2321850c5d7
BuildRequires:	perl-XML-Parser >= 2.23
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/XML/XPath.pm
%{perl_vendorlib}/XML/XPath/*.pm
%{perl_vendorlib}/XML/XPath/Node
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/xpath
%{_examplesdir}/%{name}-%{version}/*.xml
