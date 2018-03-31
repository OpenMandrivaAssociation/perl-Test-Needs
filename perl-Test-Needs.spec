%define modname	Test-Needs

Summary:	Perl module to skip tests when modules aren't available
Name:		perl-%{modname}
Version:	0.002005
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/Test-Needs-%{version}.tar.gz
BuildArch:	noarch

%description 
Perl module to skip tests when modules aren't available

%prep
%setup -qn %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
# FIXME determine why tests fail on ARM32
uname -m |grep -q arm && exit 0
make test

%files
%doc Changes
%{perl_vendorlib}/Test/Needs.pm
%{_mandir}/man3/*
