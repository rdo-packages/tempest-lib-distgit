# Created by pyp2rpm-1.1.1
%global pypi_name tempest-lib

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        4%{?dist}
Summary:        OpenStack Functional Testing Library

License:        ASL 2.0
URL:            http://www.openstack.org/
Source0:        https://pypi.python.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

Patch0001: 0001-remove-shebang.patch
Patch0002: 0002-remove-shebang-from-skip_tracker.patch
 
BuildRequires:  python-devel
BuildRequires:  python-pbr
BuildRequires:  python-sphinx
BuildRequires:  python-oslo-sphinx
BuildRequires:  dos2unix
Requires:  python-babel
Requires:  python-fixtures
Requires:  python-iso8601
Requires:  python-jsonschema
Requires:  python-httplib2
Requires:  python-oslo-context >= 0.2.0
Requires:  python-oslo-log >= 1.0.0
Requires:  python-oslo-config >= 1.9.3
Requires:  python-oslo-utils >= 1.4.0
Requires:  python-oslo-i18n >= 1.5.0
Requires:  python-oslo-serialization >= 1.4.0
Requires:  python-oslo-concurrency >= 1.8.0

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
%patch0002 -p1
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
%{_bindir}/skip-tracker
%{python2_sitelib}/tempest_lib
%{python2_sitelib}/tempest_lib-%{version}-py?.?.egg-info

%files doc
%doc html doc/source/readme.rst

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 13 2015 Steve Linabery <slinaber@redhat.com> - 0.4.0-3
- Add explicit minimum versions for kilo python-oslo-* dependencies

* Thu Apr 09 2015 Steve Linabery <slinaber@redhat.com> - 0.4.0-2
- Add missing Requires needed by new requirements.txt

* Thu Apr 09 2015 Steve Linabery <slinaber@redhat.com> - 0.4.0-1
- Rebase to upstream release 0.4.0

* Tue Jan 20 2015 Steve Linabery <slinaber@redhat.com> - 0.0.4-1
- Initial package.
