%define chipset		radeonhd
%define snapshot	0
%if %snapshot
%define release		%mkrel 0.%{snapshot}.%{rel}
%define distname	xf86-video-%{chipset}-%{snapshot}
%define compress	lzma
%else
%define release		%mkrel %{rel}
%define distname	xf86-video-%{chipset}-%{version}
%define compress	bz2
%endif

Name:		x11-driver-video-%{chipset}
Version:	1.3.0
Release:	10
Epoch:		1
Summary:	X.org driver for AMD / ATI r5xx/r6xx chipsets
Group:		System/X11
URL:		http://xorg.freedesktop.org
# for GIT:
# git://anongit.freedesktop.org/git/xorg/driver/xf86-video-radeonhd
# git archive --format=tar --prefix=xf86-video-radeonhd-$(date +%Y%m%d)/ master | lzma > ../xf86-video-radeonhd-$(date +%Y%m%d).tar.lzma
Source0:	%{distname}.tar.%{compress}
Patch0:		xf86-video-radeonhd-1.3.0-no-955x.patch
License:	MIT
BuildRequires:	x11-proto-devel
BuildRequires:	pkgconfig(xorg-server) >= 1.13
BuildRequires:	x11-util-macros
BuildRequires:	mesagl-devel
BuildRequires:	autoconf
# For rhd_conntest
BuildRequires:	pkgconfig(libpci)
BuildRequires:	zlib-devel
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

#%track
#prog %name = {
#	url = http://xorg.freedesktop.org/releases/individual/driver
#	regex = xf86-video-radeonhd-(__VER__)\.tar\.bz2
#	version = %version
#}

%description
x11-driver-video-radeonhd is the X.org driver for AMD / ATI r5xx/r6xx chipsets
(Radeon X1xxx and HD 2xxx cards).
 
%prep
%setup -q -n %{distname}
%patch0 -p1 -b .955x~

%build
autoreconf -v --install
%configure2_5x
%make

%install
%makeinstall_std
install -m755 utils/conntest/rhd_conntest -D %{buildroot}%{_bindir}/rhd_conntest

%files
%{_libdir}/xorg/modules/drivers/radeonhd_drv.*
%{_bindir}/rhd_conntest
%{_mandir}/*/*
