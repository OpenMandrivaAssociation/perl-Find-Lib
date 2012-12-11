%define upstream_name    Find-Lib
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Helper to find libs to use in the filesystem
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Find/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
The purpose of this module is to replace

    use FindBin;
    use lib "$FindBin::Bin/../bootstrap/lib";
    use My::Bootstrap %param;

with something shorter. This is specially useful if your project has a lot
of scripts (For instance tests scripts).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 688746
- update to new version 1.03

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.10.0-2
+ Revision: 654190
- rebuild for updated spec-helper

* Wed Nov 11 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2011.0
+ Revision: 464592
- update to 1.01

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 461281
- update to 1.0

* Wed Aug 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 415563
- import perl-Find-Lib


* Wed Aug 12 2009 cpan2dist 0.06-1mdv
- initial mdv release, generated with cpan2dist
