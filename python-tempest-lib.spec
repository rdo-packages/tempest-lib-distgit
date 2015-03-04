# Created by pyp2rpm-1.1.1
%global pypi_name tempest-lib

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        1%{?dist}
Summary:        OpenStack Functional Testing Library

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

Patch0001: 0001-remove-shebang.patch
 
BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  dos2unix
Requires:  python-babel
Requires:  python-fixtures
Requires:  python-oslo-config
Requires:  python-iso8601

%description
Library for creating test suites for OpenStack projects.

%package doc
Summary: Documentation for %{name}
Group: Documentation
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
%patch0001 -p1
# make doc build compatible with python-oslo-sphinx RPM
sed -i 's/oslosphinx/oslo.sphinx/' doc/source/conf.py


%build
%{__python2} setup.py build
# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
dos2unix html/_static/jquery.js

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst HACKING.rst AUTHORS ChangeLog CONTRIBUTING.rst
%license LICENSE
%{_bindir}/subunit-trace
%{python2_sitelib}/tempest_lib
%{python2_sitelib}/tempest_lib-%{version}-py?.?.egg-info

%files doc
%doc html doc/source/readme.rst

%changelog
* Tue Jan 20 2015 Steve Linabery <slinaber@redhat.com> - 0.0.4-1
- Initial package.
