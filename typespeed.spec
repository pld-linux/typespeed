Summary:	Program for counting typed chars
Summary(pl):	Program do mierzenia ilo¶ci wciskanych klawiszy
Name:		typespeed
Version:	0.5.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://ls.purkki.org/typespeed/%{name}-%{version}.tar.gz
# Source0-md5:	a39a4f76c047803c0b3d295d136365f0
URL:		http://ls.purkki.org/typespeed/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Typespeed gives your fingers' cps (total and correct), typoratio and
some points to compare with your friends.

%description -l pl
Typespeed podaje ilo¶æ znaków na sekundê Twoich palców, poprawno¶æ
pisowni i kilka innych wspó³czynników do porównania siê z
przyjació³mi.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D_GNU_SOURCE -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/share/typespeed,etc}

install -D typespeed $RPM_BUILD_ROOT%{_bindir}/typespeed
install -D typespeed.6 $RPM_BUILD_ROOT%{_mandir}/man6/typespeed.6

install words.* $RPM_BUILD_ROOT%{_datadir}/typespeed/
echo %{_datadir}/typespeed/ > $RPM_BUILD_ROOT%{_sysconfdir}/typespeedrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_sysconfdir}/typespeedrc
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/words.*
%{_mandir}/man?/*
