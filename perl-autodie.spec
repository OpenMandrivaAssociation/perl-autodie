%define realname   autodie
%define version    1.999
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Lexically have functions succeed or die
Source:     http://www.cpan.org/modules/by-module//%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Provides:      perl(autodie)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


