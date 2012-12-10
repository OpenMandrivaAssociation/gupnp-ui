%define name gupnp-ui
%define version 0.1.1
%define release %mkrel 4
%define major 0
%define libname %mklibname %{name}  %{major}
%define develname %mklibname %{name} -d

Summary: GUI for gupnp
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://gupnp.org/sources/gupnp-ui/%{name}-%{version}.tar.gz
Patch0: gupnp-ui-0.1.1-format-strings.patch
License: LGPLv2+
Group: Networking/Other
Url: http://gupnp.org/
BuildRequires: gupnp-devel
BuildRequires: pkgconfig(gtk+-2.0)
buildrequires: gtk-doc

%description
GUI for gupnp

%package -n %{libname}

Summary:        Main library for gupnp-ui
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with gupnp-ui.

%package -n     %{develname}
Summary:        Headers for developing programs that will use gupnp-ui
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use gupnp-ui

%prep
%setup -q
%patch0 -p1

%build
autoreconf -vif
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/gupnp-ui*.pc
%{_includedir}/gupnp-ui-1.0/lib%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_datadir}/gtk-doc/html/%{name}/*



%changelog
* Tue Aug 30 2011 Götz Waschk <waschk@mandriva.org> 0.1.1-4mdv2012.0
+ Revision: 697462
- rebuild

* Tue Sep 21 2010 Götz Waschk <waschk@mandriva.org> 0.1.1-3mdv2011.0
+ Revision: 580331
- update build deps

* Sun Sep 20 2009 Götz Waschk <waschk@mandriva.org> 0.1.1-2mdv2010.0
+ Revision: 445783
- rebuild for new libgupnp

* Fri Sep 11 2009 Götz Waschk <waschk@mandriva.org> 0.1.1-1mdv2010.0
+ Revision: 438524
- new version
- fix URL
- fix format strings
- fix build

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Erwan Velu <erwan@mandriva.org>
    - import gupnp-ui

