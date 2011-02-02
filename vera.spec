Summary:	V.E.R.A - dictionary of computer-releated acronyms
Summary(pl.UTF-8):	V.E.R.A - słownik skrótów związanych z komputerami
Name:		vera
Version:	1.19
Release:	1
License:	GPL
Group:		Applications/Dictionaries
Source0:	http://home.snafu.de/ohei/FTP/%{name}-%{version}.tar.gz
# Source0-md5:	1ca915d0ecd4617c54379f79e1b67914
Patch0:		%{name}-direntry.patch
URL:		http://home.snafu.de/ohei/vera/vueber-e.html
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
V.E.R.A - dictionary of computer-releated acronyms.

%description -l pl.UTF-8
V.E.R.A - słownik skrótów związanych z komputerami.

%prep
%setup -q
%patch0 -p1

%build
makeinfo vera.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}

install vera.info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README
%{_infodir}/*.info*
