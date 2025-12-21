Summary:	Edit app shortcuts
Name:		lxshortcut
Version:	0.1.2
Release:	9
License:	GPLv2+
Group:		Graphical desktop/Other
Url:		https://lxde.sourceforge.net/
Source0:	http://dfn.dl.sourceforge.net/sourceforge/lxde/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	intltool
BuildRequires:	pkgconfig(gtk+-x11-2.0)

%description
LXShortcut is a small program used to edit application shortcuts created
with freedesktop.org Desktop Entry spec.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/%{name}

