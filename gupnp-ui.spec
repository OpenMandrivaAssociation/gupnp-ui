%define api 1.0
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} %{api} -d

Summary:	GUI for gupnp
Name:		gupnp-ui
Version:	0.1.1
Release:	6
License:	LGPLv2+
Group:		Networking/Other
Url:		http://gupnp.org/
Source0:	http://gupnp.org/sources/%{name}/%{name}-%{version}.tar.gz
Patch0:		gupnp-ui-0.1.1-format-strings.patch
BuildRequires:	pkgconfig(gssdp-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(gupnp-1.0)

%description
GUI for gupnp.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for gupnp-ui
Group:		System/Libraries
Conflicts:	%{_lib}gupnp-ui0 < 0.1.1-5
Obsoletes:	%{_lib}gupnp-ui0 < 0.1.1-5

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with gupnp-ui.

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers for developing programs that will use gupnp-ui
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{_lib}gupnp-ui-devel < 0.1.1-5
Obsoletes:	%{_lib}gupnp-ui-devel < 0.1.1-5

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use gupnp-ui.

%files -n %{devname}
%{_libdir}/pkgconfig/gupnp-ui-%{api}.pc
%{_includedir}/gupnp-ui-%{api}/lib%{name}/*.h
%{_libdir}/lib%{name}-%{api}.so
%{_datadir}/gtk-doc/html/%{name}/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-static
%make LIBS="-lgupnp-1.0 -lgtk-x11-2.0 -lgobject-2.0 -lgssdp-1.0"

%install
%makeinstall_std

