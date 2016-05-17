%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name vagrant-openstack-provider

Summary: Enables Vagrant to manage machines in OpenStack Cloud
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.2
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/ggiamarchi/vagrant-openstack-provider
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}rubygem(colorize) = 1.7.3
Requires: %{?scl_prefix_ruby}rubygem(json)
Requires: %{?scl_prefix_ruby}rubygem(rest-client) >= 1.6.0
Requires: %{?scl_prefix_ruby}rubygem(rest-client) < 1.7.0
Requires: %{?scl_prefix_ruby}rubygem(sshkey) = 1.6.1
Requires: %{?scl_prefix_ruby}rubygem(terminal-table) = 1.4.5

BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This is a Vagrant 1.6+ plugin that adds an OpenStack Cloud provider to Vagrant,
allowing Vagrant to control and provision machines within OpenStack cloud.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
mkdir -p .%{gem_dir}
%{?scl:scl enable %{scl} - <<EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build
sed -i '1,$s/<json>, \["= 1.8.3"]/<json>/g' ./%{gem_spec}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/dummy.box
%{gem_instdir}/locales
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/*.gemspec
%exclude %{gem_instdir}/functional_tests
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/Vagrantfile
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/stackrc

%files doc
%doc %{gem_docdir}
%{gem_instdir}/example_box
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/RELEASE.md

%changelog
