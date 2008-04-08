Summary:	V.E.R.A - dictionary of computer-releated acronyms
Summary(pl.UTF-8):	V.E.R.A - słownik skrótów związanych z komputerami
Name:		vera
Version:	1.9
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/vera/%{name}-%{version}.tar.gz
# Source0-md5:	ed6120dd9739c71580a92868a34776b0
Patch0:		%{name}-direntry.patch
URL:		http://www.sacredchao.net/software/reed/
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
%{_infodir}/*
