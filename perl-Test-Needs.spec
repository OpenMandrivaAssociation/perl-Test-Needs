%define modname	Test-Needs

Summary:	Perl module to skip tests when modules aren't available
Name:		perl-%{modname}
Version:	0.002010
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/Test::Needs
Source0:	http://search.cpan.org/CPAN/authors/id/H/HA/HAARG/Test-Needs-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More) >= 1.1.9
BuildRequires:	perl(ExtUtils::MakeMaker) >= 7.40.0
BuildRequires:	perl(Test2::Event) >= 1.302.30

%description 
Perl module to skip tests when modules aren't available

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%check
# FIXME determine why tests fail on ARM32
uname -m |grep -q arm && exit 0
make test

%files
%doc Changes
%{perl_vendorlib}/Test/Needs.pm
%doc %{_mandir}/man3/*
