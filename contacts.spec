Summary:	Tiny GNOME address book applet
Summary(pl.UTF-8):	Mały aplet książki adresowej dla GNOME
Name:		contacts
Version:	0.9
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://pimlico-project.org/sources/contacts/%{name}-%{version}.tar.gz
# Source0-md5:	aab5affbf93d6fa7b978b323a8d44de0
URL:		http://pimlico-project.org/contacts.html
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.2
BuildRequires:	gtk+2-devel >= 2:2.10.7
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,preun):	GConf2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contacts is a small, lightweight addressbook that uses libebook, part
of EDS. This is the same library that GNOME Evolution uses, so all
contact data that exists in your Evolution addressbook is accessible
via Contacts. Contacts features advanced vCard field type handling and
is designed for use on hand-held devices, such as the Nokia 770 or the
Sharp Zaurus series of PDAs.

%description -l pl.UTF-8
Contacts to mała, lekka książka adresowa wykorzystująca libebook -
część EDS. Jest to ta sama biblioteka, której używa GNOME Evolution,
więc wszystkie dane kontaktowe istniejące w książce adresowej
Evolution są dostępne poprzez Contacts. Contacts ma obsługę
zaawansowanych typów pól vCard, jest zaprojektowany do używania na
urządzeniach przenośnych, takich jak Nokia 770 albo PDA z serii Sharp
Zaurus.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%gconf_schema_install contacts.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall contacts.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/contacts.schemas
%{_desktopdir}/contacts.desktop
%{_iconsdir}/hicolor/16x16/apps/contacts.png
%{_iconsdir}/hicolor/22x22/apps/contacts.png
%{_iconsdir}/hicolor/24x24/apps/contacts.png
%{_iconsdir}/hicolor/32x32/apps/contacts.png
%{_iconsdir}/hicolor/48x48/apps/contacts.png
%{_iconsdir}/hicolor/scalable/apps/contacts.svg
%{_mandir}/man1/contacts.1*
