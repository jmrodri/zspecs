# Generated from rjb-1.3.4.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname rjb
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Ruby Java bridge
Name: rubygem-%{gemname}
Version: 1.3.4
Release: 3%{?dist}
Group: Development/Languages
License: GPLv2+
URL: http://rjb.rubyforge.org/
Source0: %{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8
Requires: rubygems
BuildRequires: rubygems
BuildRequires: ruby-devel
BuildRequires: java-devel >= 1:1.6.0
Provides: rubygem(%{gemname}) = %{version}

%description
RJB is a bridge program that connect between Ruby and Java with Java Native
Interface.


%prep
%setup -q -c -T

%build
JAVA_HOME=/usr/lib/jvm/java gem install --local \
  --install-dir .%{gemdir} --force --rdoc %{SOURCE0}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
cp -R . %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Tue May 17 2011 jesus m. rodriguez <jesusr@redhat.com> 1.3.4-3
- requires ruby-devel & java-devel, move gem install to build

* Thu May 05 2011 jesus m rodriguez <jmrodri@gmail.com> 1.3.4-2
- build rjb with tito

* Thu Apr 28 2011 Jesus Rodriguez <jesusr@transam.devel.redhat.com> - 1.3.4-1
- Upgrade to 1.3.4
* Tue Nov 02 2010 Jesus Rodriguez <jesusr@transam.devel.redhat.com> - 1.2.9-1
- Initial package
