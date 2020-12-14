#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lutris
Version  : 0.5.8
Release  : 16
URL      : https://github.com/lutris/lutris/archive/0.5.8/lutris-0.5.8.tar.gz
Source0  : https://github.com/lutris/lutris/archive/0.5.8/lutris-0.5.8.tar.gz
Summary  : Install and play any video game easily
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: lutris-bin = %{version}-%{release}
Requires: lutris-data = %{version}-%{release}
Requires: lutris-license = %{version}-%{release}
Requires: lutris-man = %{version}-%{release}
Requires: lutris-python = %{version}-%{release}
Requires: lutris-python3 = %{version}-%{release}
Requires: Pillow
Requires: PyYAML
Requires: astroid
Requires: certifi
Requires: cffi
Requires: chardet
Requires: cryptography
Requires: dbus-python
Requires: entrypoints
Requires: evdev
Requires: gnome-desktop
Requires: idna
Requires: jeepney
Requires: keyring
Requires: lazy-object-proxy
Requires: mccabe
Requires: pycairo
Requires: pycparser
Requires: pyflakes
Requires: pygobject
Requires: python-magic
Requires: requests
Requires: secretstorage
Requires: six
Requires: urllib3
Requires: wrapt
BuildRequires : Pillow
BuildRequires : PyYAML
BuildRequires : astroid
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-meson
BuildRequires : certifi
BuildRequires : cffi
BuildRequires : chardet
BuildRequires : cryptography
BuildRequires : dbus-python
BuildRequires : entrypoints
BuildRequires : evdev
BuildRequires : gnome-desktop
BuildRequires : idna
BuildRequires : jeepney
BuildRequires : keyring
BuildRequires : lazy-object-proxy
BuildRequires : libevdev-dev
BuildRequires : mccabe
BuildRequires : pycairo
BuildRequires : pycparser
BuildRequires : pyflakes
BuildRequires : pygobject
BuildRequires : python-magic
BuildRequires : requests
BuildRequires : secretstorage
BuildRequires : six
BuildRequires : urllib3
BuildRequires : wrapt

%description
Lutris is a gaming platform for GNU/Linux. Its goal is to make
gaming on Linux as easy as possible by taking care of installing
and setting up the game for the user. The only thing you have to
do is play the game. It aims to support every game that is playable
on Linux.

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

%description python3
python3 components for the lutris package.


%prep
%setup -q -n lutris-0.5.8
cd %{_builddir}/lutris-0.5.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605721696
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lutris
cp %{_builddir}/lutris-0.5.8/LICENSE %{buildroot}/usr/share/package-licenses/lutris/842745cb706f8f2126506f544492f7a80dbe29b3
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
/usr/share/lutris/json/ags.json
/usr/share/lutris/json/citra.json
/usr/share/lutris/json/desmume.json
/usr/share/lutris/json/dgen.json
/usr/share/lutris/json/frotz.json
/usr/share/lutris/json/melonds.json
/usr/share/lutris/json/microm8.json
/usr/share/lutris/json/pcem.json
/usr/share/lutris/json/ppsspp.json
/usr/share/lutris/json/stella.json
/usr/share/lutris/json/tic80.json
/usr/share/lutris/json/virtualjaguar.json
/usr/share/lutris/media/default_banner.png
/usr/share/lutris/media/default_icon.png
/usr/share/lutris/media/logo.png
/usr/share/lutris/media/logo.svg
/usr/share/lutris/media/mask.png
/usr/share/lutris/media/unavailable.png
/usr/share/lutris/ui/about-dialog.ui
/usr/share/lutris/ui/dialog-lutris-login.ui
/usr/share/lutris/ui/dialog-pga-sources.ui
/usr/share/lutris/ui/log-window.ui
/usr/share/lutris/ui/lutris-window.ui
/usr/share/lutris/ui/lutris.css
/usr/share/lutris/ui/runner-entry.ui
/usr/share/lutris/ui/runner-remove-all-versions-dialog.ui
/usr/share/lutris/ui/runner-remove-confirm-dialog.ui
/usr/share/lutris/ui/runners-dialog.ui
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
