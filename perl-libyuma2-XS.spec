Name:           perl-libyuma2-XS
Version:        2.11
Release:        1%{?dist}
Summary:        Netconf/YANG Perl5 support
License:        multiple
URL:            http://search.cpan.org/dist/libyuma2-XS/
Source0:        yuma123-%{version}.tar.gz
Patch0:         0001-netconf-perl-remove-requirement-for-perl-v5.018.patch

# Correct for lots of packages, other common choices include eg. Module::Build
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:	yuma123-libyangrpc2-devel
BuildRequires:	yuma123-libyuma2-devel
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
The Netconf protocol and YANG modeling language provide a framework
for the exchange of management information between agents (servers)
and clients.

The yuma123 Perl5 support files provide the Perl functions for
integration of netconf and YANG into applications written in Perl.

%prep
%setup -q -c -n libyuma2-XS-%{version}
cd %{_builddir}/libyuma2-XS-%{version}/yuma123-%{version}
%patch0 -p1

%build
cd %{_builddir}/libyuma2-XS-%{version}/yuma123-%{version}/netconf/perl/yuma
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

cd %{_builddir}/libyuma2-XS-%{version}/yuma123-%{version}/netconf/perl/yangrpc
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

cd %{_builddir}/libyuma2-XS-%{version}/yuma123-%{version}/netconf/perl/yangcli
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
cd %{_builddir}/libyuma2-XS-%{version}/yuma123-%{version}/netconf/perl/yuma
make pure_install DESTDIR=$RPM_BUILD_ROOT

cd %{_builddir}/libyuma2-XS-%{version}/yuma123-%{version}/netconf/perl/yangrpc
make pure_install DESTDIR=$RPM_BUILD_ROOT

cd %{_builddir}/libyuma2-XS-%{version}/yuma123-%{version}/netconf/perl/yangcli
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
# Remove the next line from noarch packages (unneeded)
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*



%files
%doc
# For arch-specific packages: vendorarch
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*.3*


%changelog
