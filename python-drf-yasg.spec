# Created by pyp2rpm-3.3.2
%global pypi_name drf-yasg

Name:           python-%{pypi_name}
Version:        1.14.0
Release:        1%{?dist}
Summary:        Automated generation of real Swagger/OpenAPI 2.0 schemas from Django Rest Framework code

License:        BSD License
URL:            https://github.com/axnsan12/drf-yasg
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(coreapi) >= 2.3.3
BuildRequires:  python3dist(coreschema) >= 0.0.4
BuildRequires:  python3dist(django) >= 1.11.7
BuildRequires:  python3dist(djangorestframework) >= 3.7.7
BuildRequires:  python3dist(inflection) >= 0.3.1
BuildRequires:  python3dist(ruamel.yaml) >= 0.15.34
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.10.0
BuildRequires:  python3dist(swagger-spec-validator) >= 2.1.0
BuildRequires:  python3dist(uritemplate) >= 3.0.0
BuildRequires:  python3dist(sphinx)

# Manually added dependencies so it builds successfully
BuildRequires:  python3dist(setuptools-scm)

%description
.. role:: python(code) :language: python drf-yasg - Yet another Swagger
generator |travis| |nbsp| |codecov| |nbsp| |rtd-badge| |nbsp| |pypi-
version||bmac-button|Generate **real** Swagger/OpenAPI 2.0 specifications from
a Django Rest Framework API.Compatible with- **Django Rest Framework**: 3.7.7,
3.8, 3.9 - **Django**: 1.11, 2.0, 2.1 - **Python**: 2.7, 3.4, 3.5, 3.6, 3.7Only
the latest patch...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(coreapi) >= 2.3.3
Requires:       python3dist(coreschema) >= 0.0.4
Requires:       python3dist(django) >= 1.11.7
Requires:       python3dist(djangorestframework) >= 3.7.7
Requires:       python3dist(inflection) >= 0.3.1
Requires:       python3dist(ruamel.yaml) >= 0.15.34
Requires:       python3dist(six) >= 1.10.0
Requires:       python3dist(swagger-spec-validator) >= 2.1.0
Requires:       python3dist(uritemplate) >= 3.0.0
%description -n python3-%{pypi_name}
.. role:: python(code) :language: python drf-yasg - Yet another Swagger
generator |travis| |nbsp| |codecov| |nbsp| |rtd-badge| |nbsp| |pypi-
version||bmac-button|Generate **real** Swagger/OpenAPI 2.0 specifications from
a Django Rest Framework API.Compatible with- **Django Rest Framework**: 3.7.7,
3.8, 3.9 - **Django**: 1.11, 2.0, 2.1 - **Python**: 2.7, 3.4, 3.5, 3.6, 3.7Only
the latest patch...

%package -n python-%{pypi_name}-doc
Summary:        drf-yasg documentation
%description -n python-%{pypi_name}-doc
Documentation for drf-yasg

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
#PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
#rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license docs/license.rst LICENSE.rst
%doc docs/readme.rst README.rst
%{python3_sitelib}/drf_yasg
%{python3_sitelib}/drf_yasg-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
#%%doc html
%license docs/license.rst LICENSE.rst

%changelog
* Thu Mar 21 2019 Mike DePaulo <mikedep333@redhat.com> - 1.14.0-1
- Initial package.
