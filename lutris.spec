#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lutris
Version  : 0.5.5
Release  : 12
URL      : https://github.com/lutris/lutris/archive/v0.5.5.tar.gz
Source0  : https://github.com/lutris/lutris/archive/v0.5.5.tar.gz
Summary  : Install and play any video game easily
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: lutris-bin = %{version}-%{release}
Requires: lutris-data = %{version}-%{release}
Requires: lutris-license = %{version}-%{release}
Requires: lutris-python = %{version}-%{release}
Requires: lutris-python3 = %{version}-%{release}
Requires: Pillow
Requires: PyYAML
Requires: evdev
Requires: gnome-desktop
Requires: pygobject
Requires: requests
BuildRequires : Pillow
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-meson
BuildRequires : evdev
BuildRequires : gnome-desktop
BuildRequires : libevdev-dev
BuildRequires : pygobject
BuildRequires : requests

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
%setup -q -n lutris-0.5.5
cd %{_builddir}/lutris-0.5.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585678224
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lutris
cp %{_builddir}/lutris-0.5.5/LICENSE %{buildroot}/usr/share/package-licenses/lutris/842745cb706f8f2126506f544492f7a80dbe29b3
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
/usr/share/icons/hicolor/16x16/apps/lutris.png
/usr/share/icons/hicolor/22x22/apps/lutris.png
/usr/share/icons/hicolor/24x24/apps/lutris.png
/usr/share/icons/hicolor/32x32/apps/lutris.png
/usr/share/icons/hicolor/48x48/apps/lutris.png
/usr/share/icons/hicolor/scalable/apps/lutris.svg
/usr/share/lutris/bin/lutris-wrapper
/usr/share/lutris/bin/resetxpad
/usr/share/lutris/icons/hicolor/symbolic/apps/ags-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/amiga-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/atari800-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/browser-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/citra-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/copyright.old
/usr/share/lutris/icons/hicolor/symbolic/apps/desmume-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/dgen-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/dolphin-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/dosbox-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/frotz-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/fsuae-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/gog-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/hatari-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/jzintv-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/libretro-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/linux-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/mame-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/mednafen-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/mess-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/ms-dos-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/msx_msx2_msx2+-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/mupen64plus-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/necpc-98-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/nintendo3ds-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/nintendods-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/nintendogameboy-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/nintendogameboycolor-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/nintendogamecube-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/nintendones-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/nintendosnes-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/nulldc-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/o2em-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/openmsx-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/osmose-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/pcsx2-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/pico8-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/ppsspp-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/reicast-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/residualvm-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/rpcs3-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/scummvm-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/segadreamcast-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/snes9x-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/sonyplaystation-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/sonyplaystation2-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/sonyplaystation3-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/sonyplaystationportable-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/steam-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/stella-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/symbols.html
/usr/share/lutris/icons/hicolor/symbolic/apps/vice-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/virtualjaguar-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/web-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/windows-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/wine-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/winesteam-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/xdg-symbolic.svg
/usr/share/lutris/icons/hicolor/symbolic/apps/zdoom-symbolic.svg
/usr/share/lutris/media/default_banner.png
/usr/share/lutris/media/default_banner.svg
/usr/share/lutris/media/default_icon.png
/usr/share/lutris/media/generic-panel-bg.png
/usr/share/lutris/media/logo.png
/usr/share/lutris/media/logo.svg
/usr/share/lutris/media/mask.png
/usr/share/lutris/media/platform_icons/linux.png
/usr/share/lutris/media/platform_icons/mac.png
/usr/share/lutris/media/platform_icons/windows.png
/usr/share/lutris/media/runner_icons/ags.png
/usr/share/lutris/media/runner_icons/atari800.png
/usr/share/lutris/media/runner_icons/browser.png
/usr/share/lutris/media/runner_icons/browser.svg
/usr/share/lutris/media/runner_icons/citra.png
/usr/share/lutris/media/runner_icons/desmume.png
/usr/share/lutris/media/runner_icons/dgen.png
/usr/share/lutris/media/runner_icons/dgen.svg
/usr/share/lutris/media/runner_icons/dolphin.png
/usr/share/lutris/media/runner_icons/dolphin.svg
/usr/share/lutris/media/runner_icons/dosbox.png
/usr/share/lutris/media/runner_icons/frotz.png
/usr/share/lutris/media/runner_icons/fsuae.png
/usr/share/lutris/media/runner_icons/gens.png
/usr/share/lutris/media/runner_icons/gog.png
/usr/share/lutris/media/runner_icons/hatari.png
/usr/share/lutris/media/runner_icons/hatari.svg
/usr/share/lutris/media/runner_icons/higan.png
/usr/share/lutris/media/runner_icons/humblebundle.png
/usr/share/lutris/media/runner_icons/humblebundle.svg
/usr/share/lutris/media/runner_icons/jzintv.png
/usr/share/lutris/media/runner_icons/libretro.png
/usr/share/lutris/media/runner_icons/libretro.svg
/usr/share/lutris/media/runner_icons/linux.png
/usr/share/lutris/media/runner_icons/linux.svg
/usr/share/lutris/media/runner_icons/mame.png
/usr/share/lutris/media/runner_icons/mame.svg
/usr/share/lutris/media/runner_icons/mednafen.png
/usr/share/lutris/media/runner_icons/mednafen.svg
/usr/share/lutris/media/runner_icons/melonds.png
/usr/share/lutris/media/runner_icons/mess.png
/usr/share/lutris/media/runner_icons/mupen64plus.png
/usr/share/lutris/media/runner_icons/mupen64plus.svg
/usr/share/lutris/media/runner_icons/nulldc.png
/usr/share/lutris/media/runner_icons/o2em.png
/usr/share/lutris/media/runner_icons/openmsx.png
/usr/share/lutris/media/runner_icons/osmose.png
/usr/share/lutris/media/runner_icons/pcsx2.png
/usr/share/lutris/media/runner_icons/pico8.png
/usr/share/lutris/media/runner_icons/ppsspp.png
/usr/share/lutris/media/runner_icons/ppsspp.svg
/usr/share/lutris/media/runner_icons/redream.png
/usr/share/lutris/media/runner_icons/reicast.png
/usr/share/lutris/media/runner_icons/residualvm.png
/usr/share/lutris/media/runner_icons/rpcs3.png
/usr/share/lutris/media/runner_icons/scummvm.png
/usr/share/lutris/media/runner_icons/scummvm.svg
/usr/share/lutris/media/runner_icons/snes9x.png
/usr/share/lutris/media/runner_icons/steam.png
/usr/share/lutris/media/runner_icons/steam.svg
/usr/share/lutris/media/runner_icons/stella.png
/usr/share/lutris/media/runner_icons/tic80.png
/usr/share/lutris/media/runner_icons/vice.png
/usr/share/lutris/media/runner_icons/virtualjaguar.png
/usr/share/lutris/media/runner_icons/web.png
/usr/share/lutris/media/runner_icons/web.svg
/usr/share/lutris/media/runner_icons/wine.png
/usr/share/lutris/media/runner_icons/wine.svg
/usr/share/lutris/media/runner_icons/winesteam.png
/usr/share/lutris/media/runner_icons/winesteam.svg
/usr/share/lutris/media/runner_icons/xdg.png
/usr/share/lutris/media/runner_icons/xdg.svg
/usr/share/lutris/media/runner_icons/yuzu.png
/usr/share/lutris/media/runner_icons/zdoom.png
/usr/share/lutris/media/unavailable.png
/usr/share/lutris/ui/about-dialog.ui
/usr/share/lutris/ui/dialog-lutris-login.ui
/usr/share/lutris/ui/dialog-pga-sources.ui
/usr/share/lutris/ui/dialog-uninstall-game.ui
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
