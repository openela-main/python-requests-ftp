%global srcname requests-ftp

# Disable python3 by default on RHEL < 7
%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%else
%bcond_without python3
%endif

# Diable python2 by default on RHEL > 7 or Fedora > 28
%if 0%{?rhel} > 7 || 0%{?fedora} > 28
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-%{srcname}
Version:        0.3.1
Release:        11%{?dist}
Summary:        FTP transport adapter for python-requests

License:        ASL 2.0
URL:            https://github.com/Lukasa/requests-ftp
Source0:        https://pypi.python.org/packages/source/r/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

# from https://github.com/Lukasa/requests-ftp/pull/28, handle multi-line responses
# from 4090846
Patch1:         PR28-01-Adding-2-tests-and-updated-statud_code-build.patch
# from 4f6a9f5
Patch2:         PR28-02-Adding-code-3-to-retr4ieve-status_code.patch
# from 3fb2700
Patch3:         PR28-03-fix-warning-in-interpreting-ftp-status-codes-minor-d.patch
# 2caa427 is only test updates, tests not in pypi tarball
# from 7321ab3
Patch5:         PR28-05-Improve-logging-in-status-code-extraction.patch 


%description
Requests-FTP is an implementation of a very stupid FTP transport adapter for
use with the awesome Requests Python library.

%if %{with python2}
%package -n python2-%{srcname}
Summary:        FTP transport adapter for python-requests
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Requires:       python2-requests

%description -n python2-%{srcname}
Requests-FTP is an implementation of a very stupid FTP transport adapter for
use with the awesome Requests Python library.

This is the Python 2 version of the transport adapter module.
%endif

%if %{with python3}
%package -n python3-%{srcname}
Summary:        FTP transport adapter for python3-requests
%{?python_provide:%python_provide python3-%{srcname}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-requests

%description -n python3-requests-ftp
Requests-FTP is an implementation of a very stupid FTP transport adapter for
use with the awesome Requests Python library.

This is the Python 3 version of the transport adapter module.
%endif

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -rf requests_ftp.egg-info

%build
%if %{with python2}
%py2_build
%endif

%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%files -n python2-%{srcname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/requests_ftp/
%{python2_sitelib}/requests_ftp*.egg-info*
%endif

%if %{with python3}
%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/requests_ftp/
%{python3_sitelib}/requests_ftp*.egg-info*
%endif

%changelog
* Mon Aug 13 2018 David Shea <dshea@redhat.com> - 0.3.1-11
- Fix handling of multi-line FTP responses
  Resolves: rhbz#1591065

* Tue Apr 24 2018 David Shea <dshea@redhat.com> - 0.3.1-10
- Conditionalize the python2 and python3 builds

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.1-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.3.1-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Robert Kuska <rkuska@redhat.com> - 0.3.1-2
- Rebuilt for Python3.5 rebuild

* Mon Sep 14 2015 David Shea <dshea@redhat.com> - 0.3.1-1
- Update to requests-ftp-0.3.1, which fixes the LIST command
- Switch to the new python packaging guidelines, which renames python-requests-ftp to python2-requests-ftp

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 David Shea <dshea@redhat.com> - 0.3.0-1
- New upstream version 0.3.0
- Adds proxy support and improves compatibility with HTTP requests

* Thu Mar 12 2015 David Shea <dshea@redhat.com> - 0.2.0-1
- Initial package
