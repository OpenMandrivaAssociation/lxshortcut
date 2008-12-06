Summary:	Edit app shortcuts
Name:     	lxshortcut
Version:	0.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Other
Source0: 	http://dfn.dl.sourceforge.net/sourceforge/lxde/%name-%version.tar.gz
URL:		http://lxde.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	gtk+2-devel
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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post  

%postun

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/%name
