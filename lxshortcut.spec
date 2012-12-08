Summary:	Edit app shortcuts
Name:     	lxshortcut
Version:	0.1.2
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


%changelog
* Wed Aug 03 2011 Александр Казанцев <kazancas@mandriva.org> 0.1.2-1mdv2011.0
+ Revision: 693009
- update to 0.1.2

* Mon Jul 06 2009 Funda Wang <fwang@mandriva.org> 0.1.1-1mdv2011.0
+ Revision: 392806
- new version 0.1.1

* Sat Dec 06 2008 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.1
+ Revision: 311195
- import lxshortcut


