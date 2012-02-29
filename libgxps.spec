%define api	0.1
%define major	2
%define libname	%mklibname gxps %{major}
%define girname		%mklibname gxps-gir %{api}
%define develname	%mklibname -d gxps

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	GObject based library for handling and rendering XPS documents
Name:		libgxps
Version:	0.2.1
Release:	1
License:	LGPLv2
Group:		System/Libraries
URL:		http://www.gnome.org/
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		libgxps-0.2.1_linking.patch
BuildRequires: pkgconfig(cairo) >= 1.10.0
BuildRequires: pkgconfig(cairo-pdf)
BuildRequires: pkgconfig(cairo-ps)
BuildRequires: pkgconfig(cairo-svg)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gio-2.0) >= 2.24
BuildRequires: pkgconfig(glib-2.0) >= 2.24
BuildRequires: pkgconfig(gobject-2.0) >= 2.24
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libarchive) >= 2.8.0
BuildRequires: pkgconfig(libpng)
BuildRequires: jpeg-devel
BuildRequires: tiff-devel
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel >= 0.9.5

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
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface library for libgxps.

%package -n %{develname}
Summary:	Development libraries, header files and utilities for libgxps
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}

%description -n %{develname}
libgxps is a GObject based library for handling and rendering XPS documents.

This package contains the files necessary to develop applications with libgxps.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

rm -f %buildroot%_libdir/*.la

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libgxps.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GXPS-%{api}.typelib

%files -n %{develname}
%doc README COPYING AUTHORS NEWS
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gir-1.0/*.gir
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

