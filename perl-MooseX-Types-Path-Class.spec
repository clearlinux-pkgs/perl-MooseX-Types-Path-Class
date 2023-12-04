#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-MooseX-Types-Path-Class
Version  : 0.09
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-Path-Class-0.09.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Types-Path-Class-0.09.tar.gz
Summary  : 'A Path::Class type library for Moose'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-MooseX-Types-Path-Class-license = %{version}-%{release}
Requires: perl-MooseX-Types-Path-Class-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Carp::Clan)
BuildRequires : perl(Class::Load)
BuildRequires : perl(Class::Load::XS)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Devel::OverloadInfo)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Build::Tiny)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moose)
BuildRequires : perl(Moose::Util::TypeConstraints)
BuildRequires : perl(MooseX::Types)
BuildRequires : perl(MooseX::Types::Moose)
BuildRequires : perl(Package::DeprecationManager)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Path::Class)
BuildRequires : perl(Sub::Exporter)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Sub::Name)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(namespace::autoclean)

%description
This archive contains the distribution MooseX-Types-Path-Class,
version 0.09:
A Path::Class type library for Moose

%package dev
Summary: dev components for the perl-MooseX-Types-Path-Class package.
Group: Development
Provides: perl-MooseX-Types-Path-Class-devel = %{version}-%{release}
Requires: perl-MooseX-Types-Path-Class = %{version}-%{release}

%description dev
dev components for the perl-MooseX-Types-Path-Class package.


%package license
Summary: license components for the perl-MooseX-Types-Path-Class package.
Group: Default

%description license
license components for the perl-MooseX-Types-Path-Class package.


%package perl
Summary: perl components for the perl-MooseX-Types-Path-Class package.
Group: Default
Requires: perl-MooseX-Types-Path-Class = %{version}-%{release}

%description perl
perl components for the perl-MooseX-Types-Path-Class package.


%prep
%setup -q -n MooseX-Types-Path-Class-0.09
cd %{_builddir}/MooseX-Types-Path-Class-0.09

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-MooseX-Types-Path-Class
cp %{_builddir}/MooseX-Types-Path-Class-0.09/LICENSE %{buildroot}/usr/share/package-licenses/perl-MooseX-Types-Path-Class/f6392b1d37850a83994dc6347e3d15a6ff475a1c
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/MooseX::Types::Path::Class.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-MooseX-Types-Path-Class/f6392b1d37850a83994dc6347e3d15a6ff475a1c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
