Summary:	V.E.R.A - dictionary of computer-releated acronyms
Summary(pl):	V.E.R.A - s這wnik skr鏒闚 zwi您anych z komputerami
Name:		vera
Version:	1.8
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://sunsite.icm.edu.pl/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Patch0:		%{name}-direntry.patch
BuildRequires:	texinfo
URL:		http://www.sacredchao.net/software/reed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
V.E.R.A - dictionary of computer-releated acronyms.

%description -l pl
V.E.R.A - s這wnik skr鏒闚 zwi您anych z komputerami.

%prep
%setup  -q
%patch0 -p1

%build
makeinfo vera.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_infodir}
install *info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%{_infodir}/*
