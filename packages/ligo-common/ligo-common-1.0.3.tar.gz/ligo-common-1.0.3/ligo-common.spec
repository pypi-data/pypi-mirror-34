%define name ligo-common
%define version 1.0.3
%define unmangled_version 1.0.3
%define release 1

Summary: Empty LIGO modules
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPL
Group: Development/Libraries
Prefix: %{_prefix}
BuildArch: noarch
BuildRequires: rpm-build
BuildRequires: epel-rpm-macros
BuildRequires: python-rpm-macros
BuildRequires: python3-rpm-macros
BuildRequires: python-setuptools
BuildRequires: python%{python3_pkgversion}-setuptools
Vendor: Duncan Macleod <duncan.macleod@ligo.org>

%description
Empty module placeholder for other LIGO modules

# -- python2-ligo-common

%package -n python2-%{name}
Provides: %{name}
Summary: %{summary}
Requires: python
Obsoletes: ligo-common < 1.0.2-2

%{?python_provide:%python_provide python2-%{name}}

%description -n python2-%{name}
Empty module placeholder for other LIGO modules

# -- python3X-ligo-common

%package -n python%{python3_pkgversion}-%{name}
Summary: %{summary}
Requires: python%{python3_pkgversion}

%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description -n python%{python3_pkgversion}-%{name}
Empty module placeholder for other LIGO modules

# -- build steps

%prep
%setup -n %{name}-%{unmangled_version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python2-%{name}
%license LICENSE
%{python2_sitelib}/*

%files -n python%{python3_pkgversion}-%{name}
%license LICENSE
%{python3_sitelib}/*

# -- changelog

%changelog
* Fri May 11 2018 Duncan Macleod <duncan.macleod@ligo.org>
- 1.0.3: packaging update, provides python3 packages
