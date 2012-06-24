Summary:	Program for counting typed chars
Summary(pl):	Program do mierzenia ilo�ci wciskanych klawiszy
Name:		typespeed
Version:	0.4.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://www.sicom.fi/~bestis/%{name}-%{version}.tar.gz
URL:		http://www.sicom.fi/~bestis/typespeed.html
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Typespeed gives your fingers' cps (total and correct), typoratio and
some points to compare with your friends.

%description -l pl
Typespeed podaje ilo�� znak�w na sekund� Twoich palc�w, poprawno��
pisowni i kilka innych wsp�czynnik�w do por�wnania si� z
przyjaci�mi.

%prep
%setup -q

%build
%{__make} CC=%{__cc} CFLAGS="%{rpmcflags} -D_GNU_SOURCE -I%{_includedir}/ncurses"
./typespeed --makescores

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{usr/share/typespeed,etc}

install -D typespeed $RPM_BUILD_ROOT%{_bindir}/typespeed
install -D typespeed.1 $RPM_BUILD_ROOT%{_mandir}/man1/typespeed.1

install words.* $RPM_BUILD_ROOT%{_datadir}/typespeed/
echo %{_datadir}/typespeed/ > $RPM_BUILD_ROOT%{_sysconfdir}/typespeedrc


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/*
%{_datadir}/%{name}/words.*
%{_sysconfdir}/typespeedrc
