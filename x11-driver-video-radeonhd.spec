%define name		x11-driver-video-%{chipset}
%define chipset		radeonhd
%define snapshot	0
%define version		1.3.0
%define rel			10
%if %snapshot
%define release		0.%{snapshot}.%{rel}
%define distname	xf86-video-%{chipset}-%{snapshot}
%define compress	lzma
%else
%define release		%{rel}
%define distname	xf86-video-%{chipset}-%{version}
%define compress	bz2
%endif

Name:		%{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
Summary:	X.org driver for AMD / ATI r5xx/r6xx chipsets
Group:		System/X11
URL:		https://xorg.freedesktop.org
# for GIT:
# git://anongit.freedesktop.org/git/xorg/driver/xf86-video-radeonhd
# git archive --format=tar --prefix=xf86-video-radeonhd-$(date +%Y%m%d)/ master | lzma > ../xf86-video-radeonhd-$(date +%Y%m%d).tar.lzma
Source0:	%{distname}.tar.%{compress}
License:	MIT
BuildRequires:	x11-proto-devel
BuildRequires:	x11-server-devel
BuildRequires:	x11-util-macros
BuildRequires:	mesagl-devel
BuildRequires:	autoconf
# For rhd_conntest
BuildRequires:	pciutils-devel
BuildRequires:	zlib-devel
Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-radeonhd is the X.org driver for AMD / ATI r5xx/r6xx chipsets
(Radeon X1xxx and HD 2xxx cards).
 
%prep
%setup -q -n %{distname}

%build
autoreconf -v --install
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
mkdir -p %{buildroot}%{_bindir}
install -m 755 utils/conntest/rhd_conntest %{buildroot}%{_bindir}/

%files
%{_libdir}/xorg/modules/drivers/radeonhd_drv.so
%{_bindir}/rhd_conntest
%{_mandir}/*/*


%changelog
* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1:1.3.0-6mdv2011.0
+ Revision: 683558
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.3.0-5
+ Revision: 671161
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1:1.3.0-4mdv2011.0
+ Revision: 595727
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1:1.3.0-3mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Tue Nov 10 2009 Thierry Vignaud <tv@mandriva.org> 1:1.3.0-2mdv2010.1
+ Revision: 464344
- rebuild for new xserver

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1:1.3.0-1mdv2010.1
+ Revision: 461875
- forgot to commit new tarball
- update to 1.3.0

* Thu Apr 09 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1:1.2.5-1mdv2009.1
+ Revision: 365408
- New version (1.2.5)

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1:1.2.4-2mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Thu Dec 18 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 1:1.2.4-1mdv2009.1
+ Revision: 315685
- New version 1.2.4

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.4-0.20081129.1mdv2009.1
+ Revision: 308146
- rebuild against new X server
- new git snapshot
- new release 1.2.3

* Tue Sep 30 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.2-0.20080927.2mdv2009.0
+ Revision: 290228
+ rebuild (emptylog)

* Sat Sep 27 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.2-0.20080927.1mdv2009.0
+ Revision: 288948
- new snapshot 20080927

* Sat Sep 13 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.2-0.20080912.1mdv2009.0
+ Revision: 284396
- new snapshot

* Wed Aug 27 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.2-0.20080827.1mdv2009.0
+ Revision: 276607
- new snapshot 20080827

* Fri Aug 01 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.2-0.20080801.1mdv2009.0
+ Revision: 259950
- new snapshot 20080801
- new snapshot 20080721

* Thu May 29 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.2-0.20080529.1mdv2009.0
+ Revision: 213155
- drop xf86_ansic.patch (fixed upstream)
- new snapshot

* Wed May 28 2008 Paulo Andrade <pcpa@mandriva.com.br> 1:1.2.2-0.20080527.1mdv2009.0
+ Revision: 212681
- o Call libc functions directly, without depending on libc_wrapper.

  + Thierry Vignaud <tv@mandriva.org>
    - improved description
    - add missing dot at end of description
    - improved summary

  + Adam Williamson <awilliamson@mandriva.org>
    - br mesagl-devel
    - new snapshot (rs780 support, scaler support, preliminary DRI support - disabled)

* Sat May 17 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.2-0.20080517.1mdv2009.0
+ Revision: 208510
- new snapshot

* Fri Apr 25 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.2-0.20080425.1mdv2009.0
+ Revision: 197444
- new snapshot 20080425

* Mon Apr 14 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.1-0.20080414.1mdv2009.0
+ Revision: 192783
- bump once more, to today's git

* Mon Apr 14 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.2.0-1mdv2009.0
+ Revision: 192782
- stable release 1.2.0

* Sat Apr 12 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.1.1-0.20080412.1mdv2009.0
+ Revision: 192629
- update snapshot (support rs690, and should fix a problematic card we have at aboukir)

* Wed Mar 26 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.1.1-0.20080325.1mdv2008.1
+ Revision: 190200
- one last git bump before we hit release freeze

* Mon Mar 24 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.1.1-0.20080320.2mdv2008.1
+ Revision: 189778
- add shadow.patch: default to ShadowFB rather than XAA acceleration for all chipsets (it's faster, tested by many)

* Thu Mar 20 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.1.1-0.20080320.1mdv2008.1
+ Revision: 189109
- update to latest git (an important typo fix)

* Fri Mar 14 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.1.1-0.20080314.1mdv2008.1
+ Revision: 187810
- new snapshot (adds support for HD 3xxx series - rv620/635)

* Thu Mar 06 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.1.1-0.20080305.1mdv2008.1
+ Revision: 180308
- new git snapshot (needed to support the latest batch of Radeons)

* Mon Jan 28 2008 Adam Williamson <awilliamson@mandriva.org> 1:1.1.1-0.20080127.1mdv2008.1
+ Revision: 158934
- buildrequires pciutils-devel and zlib-devel (for conntest)
- install rhd_conntest utility (#36243, sorry it took so long)
- new snapshot
- new release 1.1.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 14 2007 Adam Williamson <awilliamson@mandriva.org> 1:1.0.1-0.20071214.1mdv2008.1
+ Revision: 120226
- new snapshot 20071214

* Fri Nov 30 2007 Adam Williamson <awilliamson@mandriva.org> 1:1.0.0-1mdv2008.1
+ Revision: 114215
- small spec mod to allow for using lzma for snapshots and bz2 for releases
- new release 1.0.0

* Mon Nov 26 2007 Adam Williamson <awilliamson@mandriva.org> 1:0.0.4-0.20071126.1mdv2008.1
+ Revision: 113261
- version is now up to 0.0.4
- new snapshot 20071126

* Wed Nov 07 2007 Adam Williamson <awilliamson@mandriva.org> 1:0.0.2-0.20071107.2mdv2008.1
+ Revision: 106801
- new snapshot

* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 1:0.0.2-0.20071029.2mdv2008.1
+ Revision: 106459
- rebuild for new lzma

* Mon Oct 29 2007 Adam Williamson <awilliamson@mandriva.org> 1:0.0.2-0.20071029.1mdv2008.1
+ Revision: 103549
- package man file
- buildrequires x11-util-macros (configure.ac now uses XORG_MANPAGE_SECTIONS and XORG_RELEASE_VERSION macros)
- new snapshot 20071029
- change version to 0.0.2 as per upstream, means we have to set an Epoch unfortunately

* Tue Oct 23 2007 Adam Williamson <awilliamson@mandriva.org> 1.1.1-0.20071023.1mdv2008.1
+ Revision: 101554
- new snapshot, 20071023

* Wed Oct 17 2007 Adam Williamson <awilliamson@mandriva.org> 1.1.1-0.20071017.1mdv2008.1
+ Revision: 99782
- new snapshot

* Thu Oct 11 2007 Adam Williamson <awilliamson@mandriva.org> 1.1.1-0.20071010.1mdv2008.1
+ Revision: 96959
- new snapshot

* Fri Sep 28 2007 Adam Williamson <awilliamson@mandriva.org> 1.1.1-0.20070928.1mdv2008.0
+ Revision: 93753
- new snapshot 20070928

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 1.1.1-0.20070920.1mdv2008.0
+ Revision: 91522
- today's snapshot

* Thu Sep 20 2007 Adam Williamson <awilliamson@mandriva.org> 1.1.1-0.20070919.1mdv2008.0
+ Revision: 91231
- latest snapshot, adds a bunch of new ids since yesterday
- change the spec a bit to handle snapshots and future stable releases

* Tue Sep 18 2007 Olivier Blin <oblin@mandriva.com> 1.1.1-0.20070918.2mdv2008.0
+ Revision: 89746
- build for all architectures

* Tue Sep 18 2007 Olivier Blin <oblin@mandriva.com> 1.1.1-0.20070918.1mdv2008.0
+ Revision: 89645
- initial release
- Create x11-driver-video-radeonhd

