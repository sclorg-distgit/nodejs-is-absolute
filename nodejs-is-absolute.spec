%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name is-absolute
%{?nodejs_find_provides_and_requires}

Summary:       Returns true if a file path is absolute
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       0.2.3
Release:       4%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/is-absolute
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz

ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Returns true if a file path is absolute.

Based on the isAbsolute utility method in express.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%doc README.md LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.2.3-4
- rebuilt

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 0.2.3-3
- Enable scl macros

* Tue Nov 24 2015 Troy Dawson <tdawson@redhat.com> - 0.2.3-1
- Initial package
