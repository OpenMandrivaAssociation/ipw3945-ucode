%define name ipw3945-ucode
%define version 1.14.2
%define mdkrelease 1
%define release %mkrel %{mdkrelease}

Summary:	Intel PRO/Wireless 3945 (IPW3945ABG) microcode
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tgz
License:	proprietary
Url:		http://sourceforge.net/projects/ipw3945
Group:		System/Kernel and hardware
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
Prefix:		%{_prefix}
Requires:	drakxtools >= 10-34.2mdk

%description
Firmware for the Intel PRO/Wireless 3945 (IPW3945ABG) Wifi adapter.

%prep
%setup -q 

%build

%install
cd $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/lib/firmware
install -m644 *.ucode $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_DIR/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE.ipw3945-ucode
/lib/firmware/*

