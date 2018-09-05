%define url_ver	%(echo %{version}|cut -d. -f1,2)

%define api 0.1
%define major 2
%define libname %mklibname gxps %{major}
%define girname %mklibname gxps-gir %{api}
%define devname %mklibname -d gxps
%define _disable_ld_no_undefined 1

Summary:	GObject based library for handling and rendering XPS documents
Name:		libgxps
Version:	0.3.0
Release:	1
License:	LGPLv2
Group:		System/Libraries
Url:		http://www.gnome.org/
Source0:	http://download.gnome.org/sources/libgxps/%{url_ver}/%{name}-%{version}.tar.xz
#Patch0:		libgxps-0.2.1_linking.patch
BuildRequires:	gtk-doc
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(cairo-pdf)
BuildRequires:	pkgconfig(cairo-ps)
BuildRequires:	pkgconfig(cairo-svg)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	meson

%description
libgxps is a GObject based library for handling and rendering XPS documents.
This package contains various tools used by libgxps.

%package -n %{libname}
Summary:	Libraries for libgxps
Group:		System/Libraries

%description -n %{libname}
libgxps is a GObject based library for handling and rendering XPS documents.

%package -n %{girname}
Summary:	GObject Introspection interface library for libgxps
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface library for libgxps.

%package -n %{devname}
Summary:	Development libraries, header files and utilities for libgxps
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}-%{release}

%description -n %{devname}
This package contains the files necessary to develop applications with libgxps.

%prep
%setup -q
#apply_patches

%build
%meson		\
	-Denable-gtk-doc=true	\
	-Denable-man=true
%meson_build

%install
export LANG=UTF-8
%meson_install

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libgxps.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GXPS-%{api}.typelib

%files -n %{devname}
%doc README COPYING AUTHORS NEWS
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gir-1.0/*.gir
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

