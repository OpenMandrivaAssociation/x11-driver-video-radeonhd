%define name		x11-driver-video-%{chipset}
%define chipset		radeonhd
%define snapshot	20071010
%define version		1.1.1
%if %snapshot
%define release		%mkrel 0.%{snapshot}.1
%define distname	xf86-video-%{chipset}-%{snapshot}
%else
%define release		%mkrel 1
%define distname	xf86-video-%{chipset}-%{version}
%endif

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	The X.org driver for AMD / ATI r5xx/r6xx chipsets
Group:		System/X11
URL:		http://xorg.freedesktop.org
# git://anongit.freedesktop.org/git/xorg/driver/xf86-video-radeonhd
# git archive --format=tar --prefix=xf86-video-radeonhd-$(date +%Y%m%d)/ master |
#   lzma > ../xf86-video-radeonhd-$(date +%Y%m%d).tar.lzma
Source:		%{distname}.tar.lzma
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	x11-proto-devel
BuildRequires:	x11-server-devel
BuildRequires:	autoconf

%description
The X.org driver for AMD / ATI r5xx/r6xx chipsets (Radeon X1xxx and
HD 2xxx cards).
 
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
