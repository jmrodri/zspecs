# Generated from buildr-1.4.5.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname buildr
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Build like you code
Name: rubygem-%{gemname}
Version: 1.4.6
Release: 4%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://buildr.apache.org/
Source0: http://rubygems.org/gems/%{gemname}-%{version}.gem
Patch0: buildr-1.4.6-fixversion.patch
Patch1: buildr-1.4.3-fixwarning.patch
Patch2: buildr-1.4.6-remove-rspec.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems
Requires: rubygem(rake) = 0.8.7
Requires: rubygem(builder) >= 2.1.2
Requires: rubygem(net-ssh) >= 2.0.23
Requires: rubygem(net-sftp) >= 2.0.4
Requires: rubygem(rubyzip) >= 0.9.4
#Requires: rubygem(rubyzip) = 0.9.1
Requires: rubygem(highline) >= 1.5.1
Requires: rubygem(json_pure) >= 1.4.3
Requires: rubygem(rubyforge) >= 2.0.3
Requires: rubygem(hoe) >= 2.3.3
Requires: rubygem(rjb) >= 1.3.3
Requires: rubygem(atoulme-Antwrap) >= 0.7.1
Requires: rubygem(diff-lcs) >= 1.1.2
Requires: rubygem(rspec-expectations) >= 2.1.0
Requires: rubygem(rspec-mocks) >= 2.1.0
Requires: rubygem(rspec-core) >= 2.1.0
Requires: rubygem(xml-simple) >= 1.0.12
Requires: rubygem(minitar) >= 0.5.3
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
Apache Buildr is a build system for Java-based applications, including support
for Scala, Groovy and a growing number of JVM languages and tools.  We wanted
something that's simple and intuitive to use, so we only need to tell it what
to do, and it takes care of the rest.  But also something we can easily extend
for those one-off tasks, with a language that's a joy to use.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
pushd %{buildroot}%{gemdir}
patch -p0 < %{PATCH0}
patch -p0 < %{PATCH2}
popd
pushd %{buildroot}%{gemdir}/gems/buildr-%{version}/
patch -p2 < %{PATCH1}
popd
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x
chmod -x %{buildroot}%{gemdir}/gems/%{gemname}-%{version}/spec/core/extension_spec.rb
find %{buildroot}%{geminstdir}/ -name '#*#' -exec rm -f {} \;
find %{buildroot}%{geminstdir}/ -name '.require_paths' -exec rm -f {} \;

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/buildr
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
%doc %{geminstdir}/README.rdoc
%doc %{geminstdir}/CHANGELOG
%doc %{geminstdir}/LICENSE
%doc %{geminstdir}/NOTICE
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Fri Dec 09 2011 jesus m. rodriguez <jesusr@redhat.com> 1.4.6-4
- requires 0.8.7 as newer versions break buildr

* Tue Nov 29 2011 jesus m. rodriguez <jesusr@redhat.com> 1.4.6-3
- remove rspec since rspec-core takes care of it.

* Tue Nov 29 2011 jesus m. rodriguez <jesusr@redhat.com> 1.4.6-2
- upgrade to rubyzip 0.9.4
- fix up gemspec patch
- upgrade to 1.4.6

* Wed May 18 2011 jesus m rodriguez <jmrodri@gmail.com> 1.4.5-4
- rpmlint: remove hidden file
- rpmlint: remove backup files
- rpmlint: remove exec flag from file

* Thu May 05 2011 jesus m rodriguez <jmrodri@gmail.com> 1.4.5-2
- build buildr with tito

* Thu Apr 28 2011 Jesus Rodriguez <jesusr@transam.devel.redhat.com> - 1.4.5-1
- Upgrade to 1.4.5
* Mon Nov 01 2010 Jesus Rodriguez <jesusr@transam.devel.redhat.com> - 1.4.3-1
- Initial package
