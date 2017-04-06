#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgweather
Version  : 3.24.0
Release  : 1
URL      : http://ftp.acc.umu.se/pub/GNOME/sources/libgweather/3.24/libgweather-3.24.0.tar.xz
Source0  : http://ftp.acc.umu.se/pub/GNOME/sources/libgweather/3.24/libgweather-3.24.0.tar.xz
Summary  : GWeather shared library
Group    : Development/Tools
License  : GPL-2.0
Requires: libgweather-lib
Requires: libgweather-data
Requires: libgweather-doc
Requires: libgweather-locales
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(geocode-glib-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : tzdata

%description
libgweather
===========
libgweather is a library to access weather information from online
services for numerous locations.

%package data
Summary: data components for the libgweather package.
Group: Data

%description data
data components for the libgweather package.


%package dev
Summary: dev components for the libgweather package.
Group: Development
Requires: libgweather-lib
Requires: libgweather-data
Provides: libgweather-devel

%description dev
dev components for the libgweather package.


%package doc
Summary: doc components for the libgweather package.
Group: Documentation

%description doc
doc components for the libgweather package.


%package lib
Summary: lib components for the libgweather package.
Group: Libraries
Requires: libgweather-data

%description lib
lib components for the libgweather package.


%package locales
Summary: locales components for the libgweather package.
Group: Default

%description locales
locales components for the libgweather package.


%prep
%setup -q -n libgweather-3.24.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491487470
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1491487470
rm -rf %{buildroot}
%make_install
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

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/libgweather-3.0/GWeatherInfo.html
/usr/share/gtk-doc/html/libgweather-3.0/GWeatherLocation.html
/usr/share/gtk-doc/html/libgweather-3.0/GWeatherLocationEntry.html
/usr/share/gtk-doc/html/libgweather-3.0/GWeatherTimezoneMenu.html
/usr/share/gtk-doc/html/libgweather-3.0/api-index-deprecated.html
/usr/share/gtk-doc/html/libgweather-3.0/api-index-full.html
/usr/share/gtk-doc/html/libgweather-3.0/ch01.html
/usr/share/gtk-doc/html/libgweather-3.0/home.png
/usr/share/gtk-doc/html/libgweather-3.0/index.html
/usr/share/gtk-doc/html/libgweather-3.0/ix03.html
/usr/share/gtk-doc/html/libgweather-3.0/left-insensitive.png
/usr/share/gtk-doc/html/libgweather-3.0/left.png
/usr/share/gtk-doc/html/libgweather-3.0/libgweather-3.0.devhelp2
/usr/share/gtk-doc/html/libgweather-3.0/libgweather-Versioning-information.html
/usr/share/gtk-doc/html/libgweather-3.0/libgweather-gweathertimezone.html
/usr/share/gtk-doc/html/libgweather-3.0/object-tree.html
/usr/share/gtk-doc/html/libgweather-3.0/right-insensitive.png
/usr/share/gtk-doc/html/libgweather-3.0/right.png
/usr/share/gtk-doc/html/libgweather-3.0/style.css
/usr/share/gtk-doc/html/libgweather-3.0/up-insensitive.png
/usr/share/gtk-doc/html/libgweather-3.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgweather-3.so.6
/usr/lib64/libgweather-3.so.6.6.0

%files locales -f libgweather-3.0.lang -f libgweather-locations.lang
%defattr(-,root,root,-)

