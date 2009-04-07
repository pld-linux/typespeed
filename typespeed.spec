Summary:	Program for counting typed chars
Summary(hu.UTF-8):	Program a gépelt karakterek számlálására
Summary(pl.UTF-8):	Program do mierzenia ilości wciskanych klawiszy
Name:		typespeed
Version:	0.6.5
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://tobias.eyedacor.org/typespeed/%{name}-%{version}.tar.gz
# Source0-md5:	578102b418c7df84903d3e90df2e7483
Patch0:		%{name}-dirs.patch
URL:		http://ls.purkki.org/typespeed/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Typespeed gives your fingers' cps (total and correct), typoratio and
some points to compare with your friends.

%description -l hu.UTF-8
Typespeed megadja az ujjaid cps-ét (összes és helyes
(karakter/másodperc)), gépelési arányt és pontozza, amit
összehasonlíthatsz a barátaid teljesítményével.

%description -l pl.UTF-8
Typespeed podaje ilość znaków na sekundę Twoich palców, poprawność
pisowni i kilka innych współczynników do porównania się z
przyjaciółmi.

%prep
%setup -q
# %patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{_datadir}/locale/fr_FR/LC_MESSAGES
%attr(755,root,root) %{_bindir}/%{name}
%attr(1777,root,root) /var/games/typespeed.score
%{_sysconfdir}/typespeedrc
%{_datadir}/%{name}
%{_mandir}/man6/typespeed*
%doc README
