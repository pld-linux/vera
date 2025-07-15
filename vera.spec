Summary:	V.E.R.A - dictionary of computer-releated acronyms
Summary(pl.UTF-8):	V.E.R.A - słownik skrótów związanych z komputerami
Name:		vera
Version:	1.24
Release:	1
License:	FDL v1.3+
Group:		Applications/Dictionaries
Source0:	https://ftp.gnu.org/gnu/vera/%{name}-%{version}.tar.gz
# Source0-md5:	03dce85d633e58acdd836ac1e260e7fb
Patch0:		%{name}-direntry.patch
Patch1:		%{name}-texinfo.patch
URL:		http://home.snafu.de/ohei/vera/vueber-e.html
BuildRequires:	texinfo >= 5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
V.E.R.A - dictionary of computer-releated acronyms. This package
contains the dictionary as Info document.

%description -l pl.UTF-8
V.E.R.A - słownik skrótów związanych z komputerami. Ten pakiet
zawiera słownik w postaci dokumentu Info.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
makeinfo --no-split vera.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

install vera.info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README changelog
%{_infodir}/vera.info*
