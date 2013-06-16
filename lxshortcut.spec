Summary:	Edit app shortcuts
Name:     	lxshortcut
Version:	0.1.2
Release:	3
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRequires:	pkgconfig(gtk+-x11-2.0)
BuildRequires:	intltool

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

%{find_lang} %{name}

%files -f %{name}.lang
%{_bindir}/%name
%{_datadir}/%name
