%define name		x11-driver-video-%{chipset}
%define chipset		radeonhd
%define snapshot	20080527
%define version		1.2.2
%define rel		1
%if %snapshot
%define release		%mkrel 0.%{snapshot}.%{rel}
%define distname	xf86-video-%{chipset}-%{snapshot}
%define compress	lzma
%else
%define release		%mkrel %{rel}
%define distname	xf86-video-%{chipset}-%{version}
%define compress	bz2
%endif

Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
Summary:	X.org driver for AMD / ATI r5xx/r6xx chipsets
Group:		System/X11
URL:		http://xorg.freedesktop.org
# for GIT:
# git://anongit.freedesktop.org/git/xorg/driver/xf86-video-radeonhd
# git archive --format=tar --prefix=xf86-video-radeonhd-$(date +%Y%m%d)/ master |
#   lzma > ../xf86-video-radeonhd-$(date +%Y%m%d).tar.lzma
Source0:	%{distname}.tar.%{compress}
# Default to ShadowFB acceleration, not XAA (it's faster, at the cost
# of more system resources). Re-examine when upstream improves XAA or
# EXA acceleration. - AdamW 2008/03
Patch0:		xf86-video-radeonhd-20080320-shadow.patch
Patch1:		xf86-video-radeonhd-20080527-xf86_ansic.patch
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	x11-proto-devel
BuildRequires:	x11-server-devel
BuildRequires:	x11-util-macros
BuildRequires:	mesagl-devel
BuildRequires:	autoconf
# For rhd_conntest
BuildRequires:	pciutils-devel
BuildRequires:	zlib-devel

%description
x11-driver-video-radeonhd is the X.org driver for AMD / ATI r5xx/r6xx chipsets
(Radeon X1xxx and HD 2xxx cards).
 
%prep
%setup -q -n %{distname}
%patch0 -p1 -b .shadow
%patch1 -p1 -b .xf86_ansic

%build
autoreconf -v --install
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%{_bindir}
install -m 755 utils/conntest/rhd_conntest %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/radeonhd_drv.so
%{_libdir}/xorg/modules/drivers/radeonhd_drv.la
%{_bindir}/rhd_conntest
%{_mandir}/*/*
