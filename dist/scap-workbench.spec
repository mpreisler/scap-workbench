%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif


Summary: Scanning, tailoring, editing and validation tool for SCAP content
Name: scap-workbench
URL: https://fedorahosted.org/scap-workbench/
Version: 0.2.0
Release: 1%{?dist}
License: GPLv3+
Group: System Environment/Base
Source0: https://fedorahosted.org/released/scap-workbench/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildArch: noarch
BuildRequires: python2-devel desktop-file-utils
Requires: openscap-python >= 0.6.8

%description
scap-workbench is GUI tool that provides scanning, tailoring, 
editing and validation functionality for SCAP content. The tool 
is based on OpenSCAP library.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-install					\
	--dir $RPM_BUILD_ROOT%{_datadir}/applications	\
	$RPM_BUILD_ROOT%{_datadir}/applications/scap-workbench.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README
%dir %{_sysconfdir}/scap-workbench
%config(noreplace) %{_sysconfdir}/scap-workbench/logger.conf
%{_bindir}/scap-workbench
%dir %{python_sitelib}/scap_workbench
%{python_sitelib}/scap_workbench/*
%dir %{_datadir}/scap-workbench/
%{_datadir}/scap-workbench/*
%{_mandir}/man8/scap-workbench.8.gz
%{_datadir}/applications/scap-workbench.desktop
%{_datadir}/pixmaps/scap-workbench.png

%changelog
* Mon Jan 31 2011 Maros Barabas <mbarabas@redhat.com> 0.2.0-1
- Added -D option for debug mode, default logger level set to info
- Improved Tailoring page: added profile selection and refines tailoring
- Added Edit page with editing capability of XCCDF files
- Removed Profile page - editing profiles moved to Edit page
- Improved stop functionality in Scan page
- Lot of small fixes

* Thu Oct 21 2010 Peter Vrabec <pvrabec@redhat.com> 0.1.0-1
- the first official release

