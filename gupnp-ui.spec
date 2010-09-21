%define name gupnp-ui
%define version 0.1.1
%define release %mkrel 3
%define major 0
%define libname %mklibname %{name}  %{major}
%define develname %mklibname %{name} -d

Summary: GUI for gupnp
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://gupnp.org/sources/gupnp-ui/%{name}-%{version}.tar.gz
Patch: gupnp-ui-0.1.1-format-strings.patch
License: LGPLv2+
Group: Networking/Other
Url: http://gupnp.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gupnp-devel
BuildRequires: gtk+2-devel

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
%patch -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/gupnp-ui*.pc
%{_includedir}/gupnp-ui-1.0/lib%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_datadir}/gtk-doc/html/%{name}/*

