Summary:	V.E.R.A - dictionary of computer-releated acronyms
Summary(pl.UTF-8):	V.E.R.A - słownik skrótów związanych z komputerami
Name:		vera
Version:	1.21
Release:	1
License:	FDL v1.1+
Group:		Applications/Dictionaries
Source0:	http://ftp.gnu.org/gnu/vera/%{name}-%{version}.tar.gz
# Source0-md5:	b3ac74d4f5336512996142fc00e3e144
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
%patch0 -p1
%patch1 -p1

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
%doc README
%{_infodir}/vera.info*
