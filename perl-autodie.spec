%define upstream_name       autodie
%define upstream_version 2.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Lexically have functions succeed or die
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/autodie/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

BuildArch:	noarch

Provides:	perl(autodie)

%description
'Fatal' provides a way to conveniently replace functions which normally
return a false value when they fail with equivalents which raise exceptions
if they are not successful. This lets you use these functions without
having to test their return values explicitly on each call. Exceptions can
be caught using 'eval{}'. See the perlfunc manpage and the perlvar manpage
for details.

The do-or-die equivalents are set up simply by calling Fatal's 'import'
routine, passing it the names of the functions to be replaced. You may wrap
both user-defined functions and overridable CORE operators (except 'exec',
'system', 'print', or any other built-in that cannot be expressed via
prototypes) in this way.

If the symbol ':void' appears in the import list, then functions named
later in that import list raise an exception only when these are called in
void context--that is, when their return values are ignored. For example

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor
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
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.100.0-7mdv2012.0
+ Revision: 765071
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.100.0-6
+ Revision: 763487
- rebuilt for perl-5.14.x

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 2.100.0-5
+ Revision: 656981
- rebuild for updated spec-helper

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 2.100.0-4mdv2011.0
+ Revision: 597097
- rebuild

* Wed Jul 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.100.0-3mdv2011.0
+ Revision: 562425
- rebuild

* Sat Jul 24 2010 Jérôme Quelin <jquelin@mandriva.org> 2.100.0-2mdv2011.0
+ Revision: 558161
- rebuild

* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 2.100.0-1mdv2010.1
+ Revision: 512597
- update to 2.10

* Tue Feb 23 2010 Jérôme Quelin <jquelin@mandriva.org> 2.90.0-1mdv2010.1
+ Revision: 510069
- update to 2.09

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 2.80.0-1mdv2010.1
+ Revision: 502085
- update to 2.08

* Tue Jul 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.60.0-1mdv2010.0
+ Revision: 393196
- new version

* Sun Mar 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.999-1mdv2009.1
+ Revision: 346281
- new version

* Sun Feb 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.998-1mdv2009.1
+ Revision: 336070
- import perl-autodie


* Sun Feb 01 2009 cpan2dist 1.998-1mdv
- initial mdv release, generated with cpan2dist

