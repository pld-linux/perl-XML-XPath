#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	XML
%define		pnam	XPath
Summary:	XML::XPath - a set of modules for parsing and evaluating XPath statements
Summary(pl.UTF-8):	XML::XPath - zestaw modułów do analizy i obliczania wyrażeń XPath
Name:		perl-XML-XPath
Version:	1.20
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0efb48857967094e6499de120e36b819
URL:		http://search.cpan.org/dist/XML-XPath/
BuildRequires:	perl-XML-Parser >= 2.23
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-XML-Parser >= 2.23
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module aims to comply exactly to the XPath specification at
http://www.w3.org/TR/xpath and yet allow extensions to be added
in the form of functions. Modules such as XSLT and XPointer may
need to do this as they support functionality beyond XPath.

%description -l pl.UTF-8
Ten moduł ma być zgodny ze specyfikacją XPath (dostępną pod
http://www.w3.org/TR/xpath) i pozwala na dodawanie rozszerzeń
w postaci funkcji. Do tego mogą być potrzebne moduły takie jak XSLT i
XPointer, jako że obsługują funkcjonalność spoza XPath.

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

install examples/test.xml $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/xpath
%{perl_vendorlib}/XML/XPath.pm
%{perl_vendorlib}/XML/XPath/*.pm
%{perl_vendorlib}/XML/XPath/Node
%{_mandir}/man3/XML::XPath*.3pm*
%{_examplesdir}/%{name}-%{version}
