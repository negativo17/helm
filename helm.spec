%global debug_package %{nil}

Name:           helm
Version:        3.2.1
Release:        1%{?dist}
Summary:        The Kubernetes Package Manager.
License:        ASL 2.0
URL:            https://helm.sh

Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  golang
BuildRequires:  make

%description
Helm is a tool for managing Charts. Charts are packages of pre-configured
Kubernetes resources.

Use Helm to:

- Find and use popular software packaged as Helm Charts to run in Kubernetes
- Share your own applications as Helm Charts
- Create reproducible builds of your Kubernetes applications
- Intelligently manage your Kubernetes manifest files
- Manage releases of Helm packages

%prep
%autosetup

%build
%make_build

%install
install -D -p -m 0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Thu May 28 2020 Simone Caronni <negativo17@gmail.com> - 3.2.1-1
- First build.