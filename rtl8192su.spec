#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_without	kernel		# don't build kernel modules
%bcond_without	userspace	# don't build userspace programs
%bcond_with	verbose		# verbose build (V=1)

%define		rel	0.1
Summary:	Single-Chip IEEE 802.11b/g/n 2T2R WLAN Controller with USB 2.0 Interface
Name:		rtl8192su
Version:	0006
Release:	%{rel}
License:	GPL (interface) / closed source (actual driver)
Group:		Base/Kernel
URL:		http://www.realtek.com.tw/products/productsView.aspx?Langid=1&PFid=48&Level=5&Conn=4&ProdID=231
Source0:	ftp://WebUser:7p5XTFw@202.134.71.22/cn/wlan/RTL8191SU_usb_linux_v2.6.%{version}.20100511.zip
# Source0-md5:	f55dd195053186879c3b31946c6d0cae
%if %{with kernel}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.20.2}
BuildRequires:	rpmbuild(macros) >= 1.379
%endif
BuildRequires:	unzip
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Realtek RTL8192SU-GR is a highly integrated single-chip MIMO
(Multiple In, Multiple Out) Wireless LAN (WLAN) USB 2.0 network
interface controller complying with the IEEE 802.11n specification. It
combines a MAC, 2T2R capable baseband and RF in a single chip. The
RTL8192SU-GR provides a complete solution for a high-performance
wireless client.

%package -n kernel-net-rtl8180
Summary:	Linux driver for WLAN card base on RTL8180
Summary(pl.UTF-8):	Sterownik dla Linuksa do kart bezprzewodowych na układzie RTL8180
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_up}
Requires(post,postun):	/sbin/depmod

%description -n kernel-net-rtl8180
This is driver for WLAN card based on RTL8180 for Linux.

%description -n kernel-net-rtl8180 -l pl.UTF-8
Sterownik dla Linuksa do kart WLAN opartych o układ RTL8180.

%package -n kernel-smp-net-rtl8180
Summary:	Linux driver for WLAN card base on RTL8180
Summary(pl.UTF-8):	Sterownik dla Linuksa do kart bezprzewodowych na układzie RTL8180
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
%{?with_dist_kernel:%requires_releq_kernel_smp}
Requires(post,postun):	/sbin/depmod

%description -n kernel-smp-net-rtl8180
This is driver for WLAN card based on RTL8180 for Linux.

This package contains Linux SMP module.

%description -n kernel-smp-net-rtl8180 -l pl.UTF-8
Sterownik dla Linuksa do kart WLAN opartych o układ RTL8180.

Ten pakiet zawiera moduł jądra Linuksa SMP.

%prep
%setup -q -n rtl8712_8188_8191_8192SU_usb_linux_v2.6.%{version}.20100511
%{__tar} zxf driver/rtl*.tar.gz
mv rtl* driver/src

%build
%build_kernel_modules -m rtl8712 -C driver/src

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -n kernel-net-rtl8180
%depmod %{_kernel_ver}

%postun -n kernel-net-rtl8180
%depmod %{_kernel_ver}

%post -n kernel-smp-net-rtl8180
%depmod %{_kernel_ver}smp

%postun -n kernel-smp-net-rtl8180
%depmod %{_kernel_ver}smp

%files -n kernel-net-rtl8180
%defattr(644,root,root,755)
%doc readme
/lib/modules/%{_kernel_ver}/misc/*.ko*

%if %{with smp} && %{with dist_kernel}
%files -n kernel-smp-net-rtl8180
%defattr(644,root,root,755)
%doc readme
/lib/modules/%{_kernel_ver}smp/misc/*.ko*
%endif
