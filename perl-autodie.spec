%define upstream_name       autodie
%define upstream_version 2.13

Summary:	Lexically have functions succeed or die
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/autodie/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
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
%setup -qn %{upstream_name}-%{upstream_version} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

