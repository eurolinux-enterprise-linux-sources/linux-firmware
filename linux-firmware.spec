%global checkout ddde598
%global firmware_release 72

Name:		linux-firmware
Version:	20190429
Release:	%{firmware_release}.git%{checkout}%{?dist}
Summary:	Firmware files used by the Linux kernel

Group:		System Environment/Kernel
License:	GPL+ and GPLv2+ and MIT and Redistributable, no modification permitted
URL:		https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/
# Source0 creation: "git archive --format=tar [gitid] | gzip > [srcdir]/%{name}-%{version}.tar.gz"
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
Provides:	kernel-firmware = %{version} xorg-x11-drv-ati-firmware = 7.0
Obsoletes:	kernel-firmware < %{version} xorg-x11-drv-ati-firmware <= 6.13.0-0.22
Obsoletes:	ueagle-atm4-firmware <= 1.0-5
Obsoletes:	netxen-firmware <= 4.0.534-9
Obsoletes:	ql2100-firmware <= 1.19.38-7
Obsoletes:	ql2200-firmware <= 2.02.08-7
Obsoletes:	ql23xx-firmware <= 3.03.28-5
Obsoletes:	ql2400-firmware <= 5.08.00-2
Obsoletes:	ql2500-firmware <= 5.08.00-2
Obsoletes:	rt61pci-firmware <= 1.2-11
Obsoletes:	rt73usb-firmware <= 1.8-11
Obsoletes:	bfa-firmware <= 3.2.21.1-1
# Mark the obsolecence of removed sub-packages (see bug 1232315)
Obsoletes:	libertas-usb8388-firmware
Obsoletes:	libertas-sd8686-firmware
Obsoletes:	libertas-sd8787-firmware
Obsoletes: 	libertas-usb8388-olpc-firmware

%define fwdir /usr/lib/firmware
%define _binaries_in_noarch_packages_terminate_build   0

%description
Kernel-firmware includes firmware files required for some devices to
operate.

%package -n iwl100-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 100 Series Adapters
License:	Redistributable, no modification permitted
Version:	39.31.5.1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl100-firmware < 39.31.5.1-4
%description -n iwl100-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl100 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl105-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 105 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
%description -n iwl105-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl105 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl135-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 135 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
%description -n iwl135-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl135 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl1000-firmware
Summary:	Firmware for Intel® PRO/Wireless 1000 B/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	39.31.5.1
Epoch:		1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl1000-firmware < 1:39.31.5.1-3
%description -n iwl1000-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl1000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl2000-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2000 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
%description -n iwl2000-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl2000 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl2030-firmware
Summary:	Firmware for Intel(R) Centrino Wireless-N 2030 Series Adapters
License:	Redistributable, no modification permitted
Version:	18.168.6.1
Release:	%{firmware_release}%{?dist}
%description -n iwl2030-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl2030 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl3160-firmware
Summary:	Firmware for Intel(R) Dual Band Wireless-AC 3160 Series Adapters
License:	Redistributable, no modification permitted
Version:	22.0.7.0
Release:	%{firmware_release}%{?dist}
%description -n iwl3160-firmware
This package contains the firmware required by the iwlagn driver
for Linux to support the iwl3160 hardware.  Usage of the firmware
is subject to the terms and conditions contained inside the provided
LICENSE file. Please read it carefully.

%package -n iwl3945-firmware
Summary:	Firmware for Intel® PRO/Wireless 3945 A/B/G network adaptors
License:	Redistributable, no modification permitted
Version:	15.32.2.9
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl3945-firmware < 15.32.2.9-7
%description -n iwl3945-firmware
This package contains the firmware required by the iwl3945 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl4965-firmware
Summary:	Firmware for Intel® PRO/Wireless 4965 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	228.61.2.24
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl4965-firmware < 228.61.2.24-5
%description -n iwl4965-firmware
This package contains the firmware required by the iwl4965 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5000-firmware
Summary:	Firmware for Intel® PRO/Wireless 5000 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	8.83.5.1_1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl5000-firmware < 8.83.5.1_1-3
%description -n iwl5000-firmware
This package contains the firmware required by the iwl5000 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl5150-firmware
Summary:	Firmware for Intel® PRO/Wireless 5150 A/G/N network adaptors
License:	Redistributable, no modification permitted
Version:	8.24.2.2
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl5150-firmware < 8.24.2.2-4
%description -n iwl5150-firmware
This package contains the firmware required by the iwl5150 driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6000 AGN Adapter
License:	Redistributable, no modification permitted
Version:	9.221.4.1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl6000-firmware < 9.221.4.1-4
%description -n iwl6000-firmware
This package contains the firmware required by the iwlagn driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000g2a-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6005 Series Adapters
License:	Redistributable, no modification permitted
Version:	17.168.5.3
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl6000g2a-firmware < 17.168.5.3-3
%description -n iwl6000g2a-firmware
This package contains the firmware required by the iwlagn driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6000g2b-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6030 Series Adapters
License:	Redistributable, no modification permitted
Version:	17.168.5.2
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl6000g2b-firmware < 17.168.5.2-3
%description -n iwl6000g2b-firmware
This package contains the firmware required by the iwlagn driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl6050-firmware
Summary:	Firmware for Intel(R) Wireless WiFi Link 6050 Series Adapters
License:	Redistributable, no modification permitted
Version:	41.28.5.1
Release:	%{firmware_release}%{?dist}
Obsoletes:	iwl6050-firmware < 41.28.5.1-5
%description -n iwl6050-firmware
This package contains the firmware required by the iwlagn driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl7260-firmware
Summary:	Firmware for Intel(R) Dual Band Wireless-AC 7260 Series Adapters
License:	Redistributable, no modification permitted
Version:	22.0.7.0
Release:	%{firmware_release}%{?dist}
%description -n iwl7260-firmware
This package contains the firmware required by the iwlagn driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%package -n iwl7265-firmware
Summary:	Firmware for Intel(R) Dual Band Wireless-AC 7265 Series Adapters
License:	Redistributable, no modification permitted
Version:	22.0.7.0
Release:	%{firmware_release}%{?dist}
%description -n iwl7265-firmware
This package contains the firmware required by the iwlagn driver
for Linux.  Usage of the firmware is subject to the terms and conditions
contained inside the provided LICENSE file. Please read it carefully.

%prep
# Setup Source0
%setup -q -c -n linux-firmware-%{checkout}

%build
# Remove firmware shipped in separate packages already
# Perhaps these should be built as subpackages of linux-firmware?
rm -rf ess korg sb16 yamaha
# And _some_ conexant firmware.
rm v4l-cx23418-apu.fw v4l-cx23418-cpu.fw v4l-cx23418-dig.fw v4l-cx25840.fw

# Remove source files we don't need to install
rm -f usbdux/*dux */*.asm
rm -rf carl9170fw

# Remove firmware images for WiFi & WiMax drivers not compiled in RHEL7 kernel
rm -rf ath6k
rm -rf ti-connectivity
rm -rf libertas
rm -f mrvl/sd8688.bin
rm -f mrvl/sd8688_helper.bin
rm -rf mwl8k
rm -f i2400m-fw-usb-1.4.sbcf
rm -f i2400m-fw-usb-1.5.sbcf
rm -f i6050-fw-usb-1.5.sbcf

# Remove images for vxge, we do not provide that driver in RHEL7 kernel
rm -rf vxge

# Remove the check_whence.py file
rm -f check_whence.py

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{fwdir}
mkdir -p $RPM_BUILD_ROOT%{fwdir}/updates
cp -r * $RPM_BUILD_ROOT%{fwdir}
rm $RPM_BUILD_ROOT%{fwdir}/{WHENCE,LICENCE.*,LICENSE.*}

# Create file list but exclude firmwares that we place in subpackages
FILEDIR=`pwd`
pushd $RPM_BUILD_ROOT%{fwdir}
find . \! -type d > $FILEDIR/linux-firmware.files
find . -type d | sed -e '/^.$/d' > $FILEDIR/linux-firmware.dirs
popd
sed -i -e 's:^./::' linux-firmware.{files,dirs}
sed -i -e '/^iwlwifi/d' linux-firmware.files
sed -i -e 's/^/\/usr\/lib\/firmware\//' linux-firmware.{files,dirs}
sed -i -e 's/\(.*\s.*\)/"\1"/' linux-firmware.files
sed -e 's/^/%%dir /' linux-firmware.dirs >> linux-firmware.files

%post
# This pkg carries AMD microcode and it's important to early enable it in
# case it was updated. Because of that rebuild initrd after this pkg is 
# updated and only if it's an AMD CPU.
if [ $1 -gt 1 ]; then
	if [ -d /run/systemd/system ]; then
		if grep -q AuthenticAMD /proc/cpuinfo ; then
			dracut -f
		fi
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -n iwl100-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-100-5.ucode

%files -n iwl105-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-105-*.ucode

%files -n iwl135-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-135-*.ucode

%files -n iwl1000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-1000-*.ucode

%files -n iwl2000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-2000-*.ucode

%files -n iwl2030-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-2030-*.ucode

%files -n iwl3160-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-3160-*.ucode
%{fwdir}/iwlwifi-3168-*.ucode

%files -n iwl3945-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-3945-*.ucode

%files -n iwl4965-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-4965-*.ucode

%files -n iwl5000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-5000-*.ucode

%files -n iwl5150-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-5150-*.ucode

%files -n iwl6000-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-6000-*.ucode

%files -n iwl6000g2a-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-6000g2a-*.ucode

%files -n iwl6000g2b-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-6000g2b-*.ucode

%files -n iwl6050-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-6050-*.ucode

%files -n iwl7260-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-7260-*.ucode

%files -n iwl7265-firmware
%defattr(-,root,root,-)
%doc WHENCE LICENCE.iwlwifi_firmware
%{fwdir}/iwlwifi-7265-*.ucode
%{fwdir}/iwlwifi-7265D-*.ucode
# Following up Fedora on where they have included iwlwifi-8000C & iwlwifi-8265 blobs
%{fwdir}/iwlwifi-8000C-*.ucode
%{fwdir}/iwlwifi-8265-*.ucode
# Following up Fedora on where they have included iwlwifi-9000C & iwlwifi-9260 blobs
%{fwdir}/iwlwifi-9000-*.ucode
%{fwdir}/iwlwifi-9260-*.ucode


%files -f linux-firmware.files
%defattr(-,root,root,-)
%dir %{fwdir}
#%dir %{fwdir}/updates
%doc WHENCE LICENCE.* LICENSE.*

%changelog
* Mon Apr 29 2019 Bruno E. O. Meneguele <bmeneg@redhat.com> - 20190429-72.gitddde598
- Update to latest upstream linux-firmware image for assorted updates
- cxgb4: update firmware to revision 1.23.4.0 (rhbz 1690727)
- linux-firmware: Add firmware file for Intel Bluetooth 22161 (rhbz 1622438)

* Mon Mar 18 2019 Bruno E. O. Meneguele <bmeneg@redhat.com> - 20190318-71.git283373f
- Update to latest upstream linux-firmware image for assorted updates
- cxgb4: update firmware to revision 1.23.3.0 (rhbz 1642422)

* Tue Feb 26 2019 Bruno E. O. Meneguele <bmeneg@redhat.com> - 20190225-70.git80dee31
- cxgb4: update firmware to revision 1.22.9.0 (rhbz 1671610)
- nfp: update Agilio SmartNIC flower firmware to rev AOTC-2.10.A.13 (rhbz 1637996)
- linux-firmware: Update firmware patch for Intel Bluetooth 8260 (rhbz 1649148)
- qed: Add 8.37.7.0 firmware image (rhbz 1654809)
- liquidio: fix GPL compliance issue (rhbz 1622521)
- Update Intel OPA hfi1 firmware (rhbz 1637240)
- qed: Add firmware 8.37.7.0 (rhbz 1643554)

* Tue Oct 09 2018 Bruno E. O. Meneguele <bmeneg@redhat.com> - 20180911-69.git85c5d90
- liquidio: remove firmware that violates GPL license (rhbz 1637696)

* Tue Sep 11 2018 Bruno E. O. Meneguele <bmeneg@redhat.com> - 20180911-68.git85c5d90
- Update to latest upstream linux-firmware image for assorted updates
- nvidia: update firmware for Pascal GPUs (rhbz 1625514)

* Tue Jul 17 2018 Bruno E. O. Meneguele <bmeneg@redhat.com> - 20180717-67.git8d69bab
- Update to latest upstream linux-firmware image for assorted netdrv updates
- chelsio: update firmware to revision 1.20.8.0 (rhbz 1523202)

* Mon Jun 25 2018 Bruno E. O. Meneguele <bmeneg@redhat.com> - 20180529-66.git7518922
- Only update initrd when the package is being updated (rhbz 1584178)

* Tue May 29 2018 Bruno E. O. Meneguele <bmeneg@redhat.com> - 20180529-65.git7518922
- Update to latest upstream linux-firmware image for assorted updates
- amd: update microcode for family 15h (rhbz 1574575)

* Tue May 22 2018 Bruno E. O. Meneguele <bmeneg@redhat.com> - 20180518-64.git2a9b2cf
- Add early initramfs update in case of AMD host (rhbz 1580584)

* Fri May 18 2018 Bruno E. O. Meneguele <bmeneg@redhat.com> - 20180518-63.git2a9b2cf
- Update to latest upstream linux-firmware image for assorted netdrv updates
- amd: add microcode for family 17h and update for family 15h (rhbz 1574575)

* Tue Feb 20 2018 Rafael Aquini <aquini@redhat.com> - 20180220-62.git6d51311
- nfp: NIC stops transmitting for small MSS values when TSO is enabled (rhbz 1542263)
- chelsio: pull in latests firmware 1.17.14.0 (rhbz 1538590)

* Tue Jan 16 2018 Rafael Aquini <aquini@redhat.com> - 20180113-61.git65b1c68
- Adjust Requires(post) for functional scripting due to ucode revert (rhbz 1533945)

* Sat Jan 13 2018 Rafael Aquini <aquini@redhat.com> - 20180113-60.git65b1c68
- Update to latest upstream linux-firmware image for assorted updates
- netr: Add Netronome TC flower firmware (rhbz 1518900)
- Revert amd-ucode for fam17h (rhbz 1533945)

* Wed Jan 03 2018 Rafael Aquini <aquini@redhat.com> - 20171127-59.git17e6288
- Add amd-ucode for fam17h

* Mon Nov 27 2017 Rafael Aquini <aquini@redhat.com> - 20171127-58.git17e6288
- Update to latest upstream linux-firmware image for assorted updates
- iwlwifi: Firmware update for 3160, 3168, 7260, 7265 and 7265D WIFI devices (rhbz 1508709)
- iwlwifi: Firmware update for 8260 and 8265 WIFI devices (rhbz 1508711)
- iwlwifi: Firmware update for 9260 and 9560 WIFI devices (rhbz 1501166)
- Fixes CVE-2016-0801 CVE-2017-0561 CVE-2017-9417

* Wed Oct 11 2017 Rafael Aquini <aquini@redhat.com> - 20171011-57.gitbf04291
- Update to latest upstream linux-firmware image for assorted updates
- ath10k: Update to the latest firmware released version (rhbz 1457363)
- opa: update Intel Omni-Path Architecture firmware (rhbz 1452785)
- chelsio: Pull in the latest firmware 1.16.63.0 (rhbz 1458328)
- qla2xxx: Update firmware version to 8.07.00 (rhbz 1427148)

* Mon Jun 26 2017 Rafael Aquini <aquini@redhat.com> - 20170606-56.gitc990aae
- opa: Revert switch firmware back to 0.47 (rhbz 1464629)

* Tue Jun 06 2017 Rafael Aquini <aquini@redhat.com> - 20170606-55.gitc990aae
- chelsio: Pull in the latest firmware 1.16.45.0 (rhbz 1457631)

* Tue May 30 2017 Rafael Aquini <aquini@redhat.com> - 20170530-54.gitdf40d15
- Update to latest upstream linux-firmware image for assorted updates
- opa: HFI firmware problems with new OPA switch firmware (rhbz 1452253)

* Tue May 23 2017 Rafael Aquini <aquini@redhat.com> - 20170328-53.git44d8e8d
- chelsio: Pull in the latest firmware 1.16.43.0 (rhbz 1451387)

* Tue Mar 28 2017 Rafael Aquini <aquini@redhat.com> - 20170328-52.git44d8e8d
- Update to latest upstream linux-firmware image for assorted updates
- nfp: add firmware for Netronome Ethernet Driver (rhbz 1432592)

* Tue Mar 07 2017 Rafael Aquini <aquini@redhat.com> - 20170307-51.git87714d8
- Update to latest upstream linux-firmware image for assorted updates
- chelsio: Update to the latest firmware released version (rhbz 1385911)
- drm: Update for radeon and amdgpu latest firmware released version (rhbz 1425197)

* Fri Feb 17 2017 Rafael Aquini <aquini@redhat.com> - 20170217-50.git6d3bc88
- Update to latest upstream linux-firmware image for assorted updates
- chelsio: Update to the latest firmware released version (rhbz 1395322)
- iwlwifi: Update to the latest firmware released version (rhbz 1385749)
- ath10k: Update to the latest firmware released version (rhbz 1385743)
- hfi1: Update to the latest firmware released version (rhbz 1382805)

* Tue Aug 30 2016 Rafael Aquini <aquini@redhat.com> - 20160830-49.git7534e19
- Update to latest upstream linux-firmware image for assorted updates
- Update QCA6174/hw3.0/board-2.bin file to support ath10k devices (rhbz 1368159)

* Tue Aug 23 2016 Rafael Aquini <aquini@redhat.com> - 20160728-48.git0daeaf3
- Clean up t{4,5}fw.bin symlink leftovers from bug 1262128 (rhbz 1365763)

* Thu Jul 28 2016 Rafael Aquini <aquini@redhat.com> - 20160728-47.git0daeaf3
- Update to latest upstream linux-firmware image for assorted updates
- Core14 firmware release for 7265, 7260, 3160 wireless devices (rhbz 1358566)
- Core19 firmware release for 7265D, 8260, 8265, 3168 wireless devices (rhbz 1358568)

* Wed Jun 15 2016 Rafael Aquini <aquini@redhat.com> - 20160615-46.gita4bbc81
- Update to latest upstream linux-firmware image for assorted updates
- Nuke old cxgb4 firmware blobs tarball (rhbz 1336906)
- Update to latest Chelsio firmware release version (rhbz 1336906)

* Tue Apr 26 2016 Rafael Aquini <aquini@redhat.com> - 20160426-45.git986a5a8
- Update to latest upstream linux-firmware image for assorted updates
- Restore AMD-ucode firmware blob again (rhbz 866700)
- qat: Update to the latest upstream firmware (rhbz 1173792)
- WiFi on Windstorm Peak Wireless Adapter 8265 - firmware support (rhbz 1315534)
- WiFi on Sandy Peak Wireless Adapter 3168 - firmware support (rhbz 1315536)

* Thu Mar 10 2016 Rafael Aquini <aquini@redhat.com> - 20160223-44.git8d1fd61
- Update to latest upstream linux-firmware image for assorted updates
- Update Intel Omni-Path Architecture hfi1 Firmware (rhbz 1267015)

* Mon Sep 14 2015 Jarod Wilson <jarod@redhat.com> - 20150904-43.git6ebf5d5
- Add more old chelsio firmwares, they nuked the one the driver in
  RHEL7.2 is expecting from upstream (rhbz 1262128)
- Remove amd-ucode again, it simply breaks too many systems (rhbz 1246393)

* Fri Sep 04 2015 Rafael Aquini <aquini@redhat.com> - 20150904-42.git6ebf5d5
- Add Intel Omni-Path Architecture hfi1 Firmware (rhbz 1194910)
- Update skl firmware for gpu (rhbz 1210012)

* Wed Aug 12 2015 Rafael Aquini <aquini@redhat.com> - 20150727-41.git75cc3ef
- Declare obsolecence for (old) removed firmware subpackages (rhbz 1232315)

* Mon Jul 27 2015 Rafael Aquini <aquini@redhat.com> - 20150727-40.git75cc3ef
- Add firmware support for the "Snowfield Peak" wireless adapter (rhbz 1169604)

* Tue Jul 21 2015 Rafael Aquini <aquini@redhat.com> - 20150612-39.git3161bfa
- Restore AMD-ucode firmware blob again (rhbz 1016168)

* Thu Jun 18 2015 Rafael Aquini <aquini@redhat.com> - 20150612-38.git3161bfa
- Reintroduce upstream nuked cxgb4 firmware old blobs (rhbz 1189256)

* Fri Jun 12 2015 Rafael Aquini <aquini@redhat.com> - 20150612-37.git3161bfa
- Update to latest upstream linux-firmware image for assorted updates
- cxgb4: Update firmware to revision 1.13.32.0 (rhbz 1189256)
- qat: Update to the latest upstream firmware (rhbz 1173792)
- Use a common version number for both the iwl*-firmware packages and linux-firmware itself

* Thu Sep 11 2014 Jarod Wilson <jarod@redhat.com> - 20140911-0.1.git365e80c
- Update to latest upstream linux-firmware image for assorted updates
- Adds Intel Quick Assist Technology firmware (rhbz 1127338)
- Updates bnx2x adapter firmware to version 7.10.51 (rhbz 1089403)
- Updates myri10ge adapter firmware to version 1.4.57 (rhbz 1063702)
- Removes firmware for drivers not shipped with Red Hat Enterprise Linux 7 (rhbz 1016595)

* Mon Aug 04 2014 Jarod Wilson <jarod@redhat.com> - 20140804-0.1.git6bce2b0
- Update to latest linux-firmware to pick up new Qlogic firmware (rhbz 1089364)

* Mon Mar 24 2014 Prarit Bhargava <prarit@redhat.com> - 20140213-0.3.git4164c23
- Revert AMD firmware update again (rhbz 1079114)

* Tue Mar 11 2014 Jarod Wilson <jarod@redhat.com> - 20140213-0.2.git4164c23
- Restore amd-ucode (rhbz 866700)

* Thu Feb 13 2014 Jarod Wilson <jarod@redhat.com> - 20140213-0.1.git4164c23
- Add bnx2x FW 7.8.19 to fix FCoE on 4-port cards (rhbz 1061351)

* Tue Jan 07 2014 Jarod Wilson <jarod@redhat.com> - 20140102-0.2.git52d77db
- Fix Obsoletes for iwl100-firmware (rhbz 1035459)

* Thu Jan 02 2014 Jarod Wilson <jarod@redhat.com> - 20140102-0.1.git52d77db
- Update to latest linux-firmware to pick up new Brocade firmware (rhbz 1030677)

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 20131106-0.4.git7d0c7a8
- Mass rebuild 2013-12-27

* Tue Dec 03 2013 Jarod Wilson <jarod@redhat.com> - 20131106-0.3.git7d0c7a8
- Add new fwdir define for /usr/lib/firmware and use it (rhbz 884107)

* Thu Nov 14 2013 Jarod Wilson <jarod@redhat.com> - 20131106-0.2.git7d0c7a8
- Temporarily add old brocade firmwares to work with not-yet-updated bfa driver (rhbz 1030532)

* Wed Nov 06 2013 Jarod Wilson <jarod@redhat.com> - 20131106-0.1.git7d0c7a8
- Update to latest upstream linux-firmware to pick up bfa firmware (rhbz 1013426)
- Fix up Obsoletes to all use <= comparisons

* Fri Sep 20 2013 Jarod Wilson <jarod@redhat.com> - 20130820-0.4.git600caef
- Drop amd-ucode to avoid bug 1007411 for now

* Tue Aug 20 2013 Jarod Wilson <jarod@redhat.com> - 20130820-0.3.git600caef
- Put in proper URL and URL-less Source0 location, and a note about how
  we generate the tarball by hand from a git tree

* Tue Aug 20 2013 Jarod Wilson <jarod@redhat.com> - 20130820-0.2.git600caef
- Fix up build breakage from split nvr for iwlwifi

* Tue Aug 20 2013 Jarod Wilson <jarod@redhat.com> - 20130820-0.1.git600caef
- Update to latest upstream git tree

* Thu Apr 18 2013 Josh Boyer <jwboyer@redhat.com> - 20130418-0.1.gitb584174
- Update to latest upstream git tree

* Tue Mar 19 2013 Josh Boyer <jwboyer@redhat.com>
- Own the firmware directories (rhbz 919249)

* Thu Feb 21 2013 Josh Boyer <jwboyer@redhat.com> - 20130201-0.4.git65a5163
- Obsolete netxen-firmware.  Again.  (rhbz 913680)

* Mon Feb 04 2013 Josh Boyer <jwboyer@redhat.com> - 20130201-0.3.git65a5163
- Obsolete ql2[45]00-firmware packages (rhbz 906898)
 
* Fri Feb 01 2013 Josh Boyer <jwboyer@redhat.com> 
- Update to latest upstream release
- Provide firmware for carl9170 (rhbz 866051)

* Wed Jan 23 2013 Ville Skyttä <ville.skytta@iki.fi> - 20121218-0.2.gitbda53ca
- Own subdirs created in /lib/firmware (rhbz 902005)

* Wed Jan 23 2013 Josh Boyer <jwboyer@redhat.com>
- Correctly obsolete the libertas-usb8388-firmware packages (rhbz 902265)

* Tue Dec 18 2012 Josh Boyer <jwboyer@redhat.com>
- Update to latest upstream.  Adds brcm firmware updates

* Wed Oct 10 2012 Josh Boyer <jwboyer@redhat.com>
- Consolidate rt61pci-firmware and rt73usb-firmware packages (rhbz 864959)
- Consolidate netxen-firmware and ql2[123]xx-firmware packages (rhbz 864959)

* Tue Sep 25 2012 Josh Boyer <jwboyer@redhat.com>
- Update to latest upstream.  Adds marvell wifi updates (rhbz 858388)

* Tue Sep 18 2012 Josh Boyer <jwboyer@redhat.com>
- Add patch to create libertas subpackages from Daniel Drake (rhbz 853198)

* Fri Sep 07 2012 Josh Boyer <jwboyer@redhat.com> 20120720-0.2.git7560108
- Add epoch to iwl1000 subpackage to preserve upgrade patch (rhbz 855426)

* Fri Jul 20 2012 Josh Boyer <jwboyer@redhat.com> 20120720-0.1.git7560108
- Update to latest upstream.  Adds more realtek firmware and bcm4334

* Tue Jul 17 2012 Josh Boyer <jwboyer@redhat.com> 20120717-0.1.gitf1f86bb
- Update to latest upstream.  Adds updated realtek firmware

* Thu Jun 07 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.5.git375e954
- Bump release to get around koji

* Thu Jun 07 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.4.git375e954
- Drop udev requires.  Systemd now provides udev

* Tue Jun 05 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.3.git375e954
- Fix location of BuildRequires so git is inclued in the buildroot
- Create iwlXXXX-firmware subpackages (rhbz 828050)

* Thu May 10 2012 Josh Boyer <jwboyer@redhat.com> 20120510-0.1.git375e954
- Update to latest upstream.  Adds new bnx2x and radeon firmware

* Wed Apr 18 2012 Josh Boyer <jwboyer@redhat.com> 20120418-0.1.git85fbcaa
- Update to latest upstream.  Adds new rtl and ath firmware

* Wed Mar 21 2012 Dave Airlie <airlied@redhat.com> 20120206-0.3.git06c8f81
- use git to apply the radeon firmware

* Wed Mar 21 2012 Dave Airlie <airlied@redhat.com> 20120206-0.2.git06c8f81
- add radeon southern islands/trinity firmware

* Tue Feb 07 2012 Josh Boyer <jwboyer@redhat.com> 20120206-0.1.git06c8f81
- Update to latest upstream git snapshot.  Fixes rhbz 786937

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110731-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 04 2011 Tom Callaway <spot@fedoraproject.org> 20110731-2
- resolve conflict with netxen-firmware

* Wed Aug 03 2011 David Woodhouse <dwmw2@infradead.org> 20110731-1
- Latest firmware release with v1.3 ath9k firmware (#727702)

* Sun Jun 05 2011 Peter Lemenkov <lemenkov@gmail.com> 20110601-2
- Remove duplicated licensing files from /lib/firmware

* Wed Jun 01 2011 Dave Airlie <airlied@redhat.com> 20110601-1
- Latest firmware release with AMD llano support.

* Thu Mar 10 2011 Dave Airlie <airlied@redhat.com> 20110304-1
- update to latest upstream for radeon ni/cayman, drop nouveau fw we don't use it anymore

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110125-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 David Woodhouse <dwmw2@infradead.org> 20110125-1
- Update to linux-firmware-20110125 (new bnx2 firmware)

* Fri Jan 07 2011 Dave Airlie <airlied@redhat.com> 20101221-1
- rebase to upstream release + add new radeon NI firmwares.

* Thu Aug 12 2010 Hicham HAOUARI <hicham.haouari@gmail.com> 20100806-4
- Really obsolete ueagle-atm4-firmware

* Thu Aug 12 2010 Hicham HAOUARI <hicham.haouari@gmail.com> 20100806-3
- Obsolete ueagle-atm4-firmware

* Fri Aug 06 2010 David Woodhouse <dwmw2@infradead.org> 20100806-2
- Remove duplicate radeon firmwares; they're upstream now

* Fri Aug 06 2010 David Woodhouse <dwmw2@infradead.org> 20100806-1
- Update to linux-firmware-20100806 (more legacy firmwares from kernel source)

* Fri Apr 09 2010 Dave Airlie <airlied@redhat.com> 20100106-4
- Add further radeon firmwares

* Wed Feb 10 2010 Dave Airlie <airlied@redhat.com> 20100106-3
- add radeon RLC firmware - submitted upstream to dwmw2 already.

* Tue Feb 09 2010 Ben Skeggs <bskeggs@redhat.com> 20090106-2
- Add firmware needed for nouveau to operate correctly (this is Fedora
  only - do not upstream yet - we just moved it here from Fedora kernel)

* Wed Jan 06 2010 David Woodhouse <David.Woodhouse@intel.com> 20090106-1
- Update

* Fri Aug 21 2009 David Woodhouse <David.Woodhouse@intel.com> 20090821-1
- Update, fix typos, remove some files which conflict with other packages.

* Thu Mar 19 2009 David Woodhouse <David.Woodhouse@intel.com> 20090319-1
- First standalone kernel-firmware package.
