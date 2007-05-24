#
Summary:	tiny GNOME address book applet
Name:		contacts
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://pimlico-project.org/sources/contacts/%{name}-%{version}.tar.gz
# Source0-md5:	d2150fe286ee6e0518af37f3107cb867
URL:		http://pimlico-project.org/contacts.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel
BuildRequires:	gtk+2-devel >= 2:2.10.7
#BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.27
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Contacts is a small, lightweight addressbook that uses libebook, part
of EDS. This is the same library that GNOME Evolution uses, so all
contact data that exists in your Evolution addressbook is accessible
via Contacts. Contacts features advanced vCard field type handling and
is designed for use on hand-held devices, such as the Nokia 770 or the
Sharp Zaurus series of PDAs.

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
%gconf_schema_install contacts.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall contacts.schemas

%postun
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/contacts.schemas
%{_desktopdir}/contacts.desktop
%{_iconsdir}/hicolor/48x48/apps/contacts.png
%{_mandir}/man1/contacts.1*
