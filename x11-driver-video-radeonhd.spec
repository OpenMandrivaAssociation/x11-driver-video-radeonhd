%define name x11-driver-video-%{chipset}
%define chipset radeonhd
%define snapshot 20070918
%define version 1.1.1
%define release %mkrel 0.%{snapshot}.2
%define distname xf86-video-%{chipset}-%{version}-%{snapshot}

Name: %{name}
Version: %{version}
Release: %{release}
Summary: The X.org driver for AMD GPG r5xx/r6xx Chipsets
Group: System/X11
URL: http://xorg.freedesktop.org
# git://anongit.freedesktop.org/git/xorg/driver/xf86-video-radeonhd
# git archive --format=tar --prefix=xf86-video-radeonhd-1.1.1-$(date +%Y%m%d)/ master |
#   bzip2 > ../xf86-video-radeonhd-1.1.1-$(date +%Y%m%d).tar.bz2
Source: %{distname}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel
BuildRequires: x11-server-devel
BuildRequires: autoconf

%description
The X.org driver for AMD GPG r5xx/r6xx Chipsets
 
%prep
%setup -q -n %{distname}

%build
autoreconf -v --install
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/radeonhd_drv.so
%{_libdir}/xorg/modules/drivers/radeonhd_drv.la
