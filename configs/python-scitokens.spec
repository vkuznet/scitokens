# Created by pyp2rpm-3.2.3
%global pypi_name scitokens

Name:           python-%{pypi_name}
Version:        1.2.1
Release:        1%{?dist}
Summary:        SciToken reference implementation library

License:        Apache 2.0
URL:            https://scitokens.org
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
SciToken reference implementation library

%package -n     python2-%{pypi_name}
Summary:        %{summary}
Provides:       python-%{pypi_name}
 
Requires:       python-jwt >= 1.6.1
Requires:       python2-cryptography
Requires:       python-setuptools
%description -n python2-%{pypi_name}
SciToken reference implementation library

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%files -n python2-%{pypi_name}
%doc README.rst
%{_bindir}/scitokens-admin-create-key
%{_bindir}/scitokens-admin-create-token
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Sun Oct 21 2018 Derek Weitzel <dweitzel@cse.unl.edu> - 1.2.1-1
- Support multiple audiences in verifier

* Tue Jul 10 2018 Derek Weitzel <dweitzel@cse.unl.edu> - 1.2.0-1
- Merge in the "scope" change accidently mentioned in 1.1.0

* Fri Jul 6 2018 Derek Weitzel <dweitzel@cse.unl.edu> - 1.1.0-1
- Add support for updated RFC for "scope"
- Add support for Elliptic Curve cryptography

* Tue Jan 30 2018 Derek Weitzel <dweitzel@cse.unl.edu> - 1.0.2-1
- Fix bug when configuration is not specified

* Tue Jan 30 2018 Derek Weitzel <dweitzel@cse.unl.edu> - 1.0.0-1
- Add optional configuration file
- Fix bug for missing kid
- Add automatic jti generation

* Mon Nov 06 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.3-1
- Add subject testing in the Enforcer

* Mon Nov 06 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.2-3
- Include dependency for python-setuptools

* Fri Nov 03 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.2-2
- Update packaging to not include 2 scripts for the admin-create*
- Include the correct package for python-jwt dependency

* Thu Nov 02 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.2-1
- Version bump to include spec in tag

* Wed Nov 01 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.1-1
- Fix packaging to include internal util module

* Wed Nov 01 2017 Derek Weitzel <dweitzel@cse.unl.edu> - 0.3.0-1
- Initial package.
