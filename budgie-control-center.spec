%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Name:           budgie-control-center
Version:        1.4.0
Release:        1
Summary:        A fork of GNOME Control Center for the Budgie 10 Series
Group:          Graphical desktop/Budgie
License:        GPLv2+ and CC-BY-SA
URL:            https://github.com/BuddiesOfBudgie/budgie-control-center
Source0:        https://github.com/BuddiesOfBudgie/budgie-control-center/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese)
BuildRequires:  pkgconfig(cheese-gtk)
BuildRequires:  pkgconfig(colord-gtk)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-1.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gtk+-3.0) 
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm) >= 1.24
BuildRequires:  pkgconfig(libnma)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  chrpath
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  appstream-util
BuildRequires:  meson
BuildRequires:  xsltproc

Requires: cheese
Requires: glib2
Requires: gnome-bluetooth3.34
Requires: gnome-desktop
Requires: gnome-online-accounts
Requires: gnome-settings-daemon
Requires: gsettings-desktop-schemas
Requires: gtk+3
Requires: upower
Requires: samba-libs

# For user accounts
Requires: accountsservice
Requires: alsa-lib

# For the thunderbolt panel
Recommends: bolt

# For the color panel
Requires: colord

# For the printers panel
#Requires: cups-pk-helper
Recommends: cups
Requires: dbus

# For the info/details panel
Requires: glxinfo
Requires: mesa-demos
# Not available yet in Cooker
Recommends: switcheroo-control

# For the user languages
Requires: iso-codes

# For the network panel
Requires: networkmanager-wifi
Requires: networkmanager-applet

# For parental controls support
Requires: malcontent

# For Show Details in the color panel
Recommends: gnome-color-manager

# For the sharing panel
Recommends: gnome-remote-desktop

# For the power panel
Recommends: power-profiles-daemon

%description
A fork of GNOME Control Center for the Budgie 10 Series.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson  \
        -Ddocumentation=true \
        -Dmalcontent=true
#    -Ddark_mode_distributor_logo=%{_datadir}/pixmaps/system-logo-white.png \
%meson_build


%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/budgie/wm-properties
rm -rf %{buildroot}%{_datadir}/budgie/autostart
rm -rf %{buildroot}%{_datadir}/budgie/cursor-fonts
chrpath --delete %{buildroot}%{_bindir}/budgie-control-center
%find_lang %{name} --all-name --with-gnome


%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/budgie-control-center
%{_datadir}/applications/*.desktop
%{_datadir}/bash-completion/completions/budgie-control-center
%{_datadir}/dbus-1/services/org.buddiesofbudgie.ControlCenter.service
%{_datadir}/glib-2.0/schemas/org.buddiesofbudgie.ControlCenter.gschema.xml
%{_datadir}/budgie-control-center/keybindings/*.xml
%{_datadir}/budgie-control-center/pixmaps
%{_datadir}/budgie/wm-properties
%{_datadir}/icons/*
%{_mandir}/man1/budgie-control-center.1*
%{_datadir}/metainfo/budgie-control-center.appdata.xml
%{_datadir}/pixmaps/budgie-faces
%{_datadir}/pixmaps/budgie-logo.png
#{_datadir}/pkgconfig/budgie-keybindings.pc
%{_datadir}/polkit-1/actions/org.buddiesofbudgie.controlcenter.*.policy
%{_datadir}/polkit-1/rules.d/budgie-control-center.rules
%{_datadir}/sounds/budgie/default/*/*.ogg
%{_libexecdir}/budgie-cc-remote-login-helper
%{_libexecdir}/budgie-control-center-print-renderer
