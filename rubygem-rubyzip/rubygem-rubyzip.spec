# Generated from rubyzip-0.9.1.gem by gem2rpm -*- rpm-spec -*-
%global gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gemname rubyzip
%global geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: A ruby module for reading and writing zip files
Name: rubygem-%{gemname}
Version: 0.9.4
Release: 5%{?dist}
Group: Development/Languages
License: GPLv2 or Ruby
URL: http://rubyzip.sourceforge.net/
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
Patch0: rubyzip-commentsize.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) = 1.8
Requires: rubygems
BuildRequires: rubygems
BuildRequires: rubygem-rake
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
rubyzip is a ruby module for reading and writing zip files


%package doc
Summary: Documentation for %{name}
Group: Documentation

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
pushd %{buildroot}%{gemdir}
patch -p0 < %{PATCH0}
popd

chmod 755 %{buildroot}%{geminstdir}/install.rb

for SCRIPT in example_filesystem gtkRubyzip example write_simple qtzip zipfind
do
    chmod 755  %{buildroot}%{geminstdir}/samples/$SCRIPT.rb
done

for RB in stdrubyext zip tempfile_bugfixed ioextras zipfilesystem ziprequire
do
    chmod 644  %{buildroot}%{geminstdir}/lib/zip/$RB.rb
done

chmod 644  %{buildroot}%{geminstdir}/Rakefile

# These aren't executables
sed -i -e '/^#!\/usr\/bin\/env ruby/d' \
  %{buildroot}%{geminstdir}/Rakefile 

# Remove CRLF from file
sed -i 's/\r//'  %{buildroot}%{geminstdir}/samples/write_simple.rb



%check
pushd %{buildroot}%{gemdir}/gems/%{gemname}-%{version}/
rake test
popd


%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{geminstdir}/[A-Z]*
%dir %{geminstdir}
%{geminstdir}/install.rb
%{geminstdir}/lib
%doc %{geminstdir}/samples
%doc %{gemdir}/doc/%{gemname}-%{version}
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%files doc
%defattr(644,root,root,755)
%{geminstdir}/Rakefile
%doc %{geminstdir}/test
%{gemdir}/doc/%{gemname}-%{version}


%changelog
* Mon May 24 2010 jesus m. rodriguez <jesusr@redhat.com> 0.9.4-5
- add BuildRequires for rubygem-rake (jesusr@redhat.com)

* Mon May 24 2010 jesus m. rodriguez <jesusr@redhat.com> 0.9.4-4
- need to move upstream files to proper location (jesusr@redhat.com)

* Tue May 18 2010 Adam Young <ayoung@redhat.com> - 0.9.4-3
- Enabled tests, 
- Removed the blanket cr/lf replace thyat was breaking thes test

* Thu May 13 2010 Adam Young <ayoung@redhat.com> - 0.9.4-2
- Upgraded to 0.9.4, with a patch to make buildr run


* Tue May 11 2010 Adam Young <ayoung@redhat.com> - 0.9.1-2
- Split documentation out into separate rpm
- Fixed rpmlint errors

* Tue May 11 2010 Adam Young <ayoung@redhat.com> - 0.9.1-2
- Fixed License
- Added ABI Dependency
- changed define to global

* Fri Apr 30 2010 jesus m. rodriguez <jesusr@redhat.com> 0.9.1-2
- rebuild with tito

* Tue Apr 06 2010 Adam Young <ayoung@redhat.com> - 0.9.1-1
- Initial package
