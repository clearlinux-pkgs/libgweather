#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgweather
Version  : 3.33.92
Release  : 20
URL      : https://download.gnome.org/sources/libgweather/3.33/libgweather-3.33.92.tar.xz
Source0  : https://download.gnome.org/sources/libgweather/3.33/libgweather-3.33.92.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: libgweather-data = %{version}-%{release}
Requires: libgweather-lib = %{version}-%{release}
Requires: libgweather-license = %{version}-%{release}
Requires: libgweather-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gobject-introspection-dev
BuildRequires : pkgconfig(geocode-glib-1.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : tzdata

%description
[![Build Status](https://gitlab.gnome.org/GNOME/libgweather/badges/master/build.svg)](https://gitlab.gnome.org/GNOME/libgweather/pipelines)

%package data
Summary: data components for the libgweather package.
Group: Data

%description data
data components for the libgweather package.


%package dev
Summary: dev components for the libgweather package.
Group: Development
Requires: libgweather-lib = %{version}-%{release}
Requires: libgweather-data = %{version}-%{release}
Provides: libgweather-devel = %{version}-%{release}
Requires: libgweather = %{version}-%{release}

%description dev
dev components for the libgweather package.


%package lib
Summary: lib components for the libgweather package.
Group: Libraries
Requires: libgweather-data = %{version}-%{release}
Requires: libgweather-license = %{version}-%{release}

%description lib
lib components for the libgweather package.


%package license
Summary: license components for the libgweather package.
Group: Default

%description license
license components for the libgweather package.


%package locales
Summary: locales components for the libgweather package.
Group: Default

%description locales
locales components for the libgweather package.


%prep
%setup -q -n libgweather-3.33.92

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568130941
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libgweather
cp COPYING %{buildroot}/usr/share/package-licenses/libgweather/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libgweather-3.0
%find_lang libgweather-locations

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GWeather-3.0.typelib
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.GWeather.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.GWeather.gschema.xml
/usr/share/libgweather/Locations.xml
/usr/share/libgweather/locations.dtd
/usr/share/vala/vapi/gweather-3.0.deps
/usr/share/vala/vapi/gweather-3.0.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libgweather-3.0/libgweather/gweather-enum-types.h
/usr/include/libgweather-3.0/libgweather/gweather-enums.h
/usr/include/libgweather-3.0/libgweather/gweather-location-entry.h
/usr/include/libgweather-3.0/libgweather/gweather-location.h
/usr/include/libgweather-3.0/libgweather/gweather-timezone-menu.h
/usr/include/libgweather-3.0/libgweather/gweather-timezone.h
/usr/include/libgweather-3.0/libgweather/gweather-version.h
/usr/include/libgweather-3.0/libgweather/gweather-weather.h
/usr/include/libgweather-3.0/libgweather/gweather.h
/usr/lib64/libgweather-3.so
/usr/lib64/pkgconfig/gweather-3.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgweather-3.so.16
/usr/lib64/libgweather-3.so.16.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgweather/COPYING

%files locales -f libgweather-3.0.lang -f libgweather-locations.lang
%defattr(-,root,root,-)

