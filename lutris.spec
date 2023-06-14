#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : lutris
Version  : 0.5.13
Release  : 41
URL      : https://github.com/lutris/lutris/archive/v0.5.13/lutris-0.5.13.tar.gz
Source0  : https://github.com/lutris/lutris/archive/v0.5.13/lutris-0.5.13.tar.gz
Summary  : Video game preservation platform
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: lutris-bin = %{version}-%{release}
Requires: lutris-data = %{version}-%{release}
Requires: lutris-license = %{version}-%{release}
Requires: lutris-locales = %{version}-%{release}
Requires: lutris-man = %{version}-%{release}
Requires: lutris-python = %{version}-%{release}
Requires: lutris-python3 = %{version}-%{release}
Requires: gnome-desktop
Requires: pygobject
Requires: pypi(evdev)
Requires: pypi(pillow)
Requires: pypi(pycairo)
BuildRequires : appstream-glib
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : libevdev-dev
BuildRequires : pygobject
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Lutris helps you install and play video games from all eras and
from most gaming systems. By leveraging and combining existing
emulators, engine re-implementations and compatibility layers,
it gives you a central interface to launch all your games.

%package bin
Summary: bin components for the lutris package.
Group: Binaries
Requires: lutris-data = %{version}-%{release}
Requires: lutris-license = %{version}-%{release}

%description bin
bin components for the lutris package.


%package data
Summary: data components for the lutris package.
Group: Data

%description data
data components for the lutris package.


%package license
Summary: license components for the lutris package.
Group: Default

%description license
license components for the lutris package.


%package locales
Summary: locales components for the lutris package.
Group: Default

%description locales
locales components for the lutris package.


%package man
Summary: man components for the lutris package.
Group: Default

%description man
man components for the lutris package.


%package python
Summary: python components for the lutris package.
Group: Default
Requires: lutris-python3 = %{version}-%{release}

%description python
python components for the lutris package.


%package python3
Summary: python3 components for the lutris package.
Group: Default
Requires: python3-core
Requires: dbus-python
Requires: dbus-python-python3

%description python3
python3 components for the lutris package.


%prep
%setup -q -n lutris-0.5.13
cd %{_builddir}/lutris-0.5.13
pushd ..
cp -a lutris-0.5.13 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686754036
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/lutris
cp %{_builddir}/lutris-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/lutris/842745cb706f8f2126506f544492f7a80dbe29b3 || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang lutris
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lutris

%files data
%defattr(-,root,root,-)
/usr/share/applications/net.lutris.Lutris.desktop
/usr/share/icons/hicolor/128x128/apps/lutris.png
/usr/share/icons/hicolor/16x16/apps/lutris.png
/usr/share/icons/hicolor/22x22/apps/lutris.png
/usr/share/icons/hicolor/24x24/apps/lutris.png
/usr/share/icons/hicolor/32x32/apps/lutris.png
/usr/share/icons/hicolor/48x48/apps/lutris.png
/usr/share/icons/hicolor/64x64/apps/lutris.png
/usr/share/icons/hicolor/scalable/apps/lutris.svg
/usr/share/lutris/bin/lutris-wrapper
/usr/share/lutris/conf/origin-openssl3.cnf
/usr/share/lutris/json/86box.json
/usr/share/lutris/json/ags.json
/usr/share/lutris/json/basiliskii.json
/usr/share/lutris/json/citra.json
/usr/share/lutris/json/colem.json
/usr/share/lutris/json/desmume.json
/usr/share/lutris/json/dgen.json
/usr/share/lutris/json/frotz.json
/usr/share/lutris/json/melonds.json
/usr/share/lutris/json/microm8.json
/usr/share/lutris/json/minivmac.json
/usr/share/lutris/json/pcem.json
/usr/share/lutris/json/ppsspp.json
/usr/share/lutris/json/sheepshaver.json
/usr/share/lutris/json/speccy.json
/usr/share/lutris/json/stella.json
/usr/share/lutris/json/tic80.json
/usr/share/lutris/json/virtualjaguar.json
/usr/share/lutris/media/default_banner.png
/usr/share/lutris/media/default_icon.png
/usr/share/lutris/media/logo.png
/usr/share/lutris/media/logo.svg
/usr/share/lutris/media/mask.png
/usr/share/lutris/media/side-dark.svg
/usr/share/lutris/media/side-light.svg
/usr/share/lutris/media/splash-dark.svg
/usr/share/lutris/media/splash-light.svg
/usr/share/lutris/ui/about-dialog.ui
/usr/share/lutris/ui/dialog-lutris-login.ui
/usr/share/lutris/ui/log-window.ui
/usr/share/lutris/ui/lutris-window.ui
/usr/share/lutris/ui/lutris.css
/usr/share/metainfo/net.lutris.Lutris.metainfo.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lutris/842745cb706f8f2126506f544492f7a80dbe29b3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lutris.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f lutris.lang
%defattr(-,root,root,-)

