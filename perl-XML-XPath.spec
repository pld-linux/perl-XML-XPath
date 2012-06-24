%include	/usr/lib/rpm/macros.perl
%define         pdir	XML
%define         pnam	XPath
Summary:	XML::XPath - a set of modules for parsing and evaluating XPath statements
Summary(pl):	XML::XPath - zestaw modu��w do parsowania i obliczania wyra�e� XPath
Name:		perl-XML-XPath
Version:	1.12
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-XML-Parser >= 2.23
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This module aims to comply exactly to the XPath specification at
http://www.w3.org/TR/xpath and yet allow extensions to be added
in the form of functions. Modules such as XSLT and XPointer may
need to do this as they support functionality beyond XPath.

%description -l pl
Ten modu� ma by� zgodny ze specyfikacj� XPath (dost�pn� pod
http://www.w3.org/TR/xpath) i pozwala na dodawanie rozszerze�
w postaci funkcji. Modu�y takie jak XSLT i XPointer mog� by�
potrzebne do tego, jako �e obs�uguj� funkcjonalno�� spoza XPath.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/XML/XPath.pm
%{perl_sitelib}/XML/XPath
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/xpath
%{_examplesdir}/%{name}-%{version}/*.xml
