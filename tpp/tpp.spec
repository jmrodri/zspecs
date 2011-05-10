Summary: ncurses-based presentation tool
Name: tpp
Version: 1.3.1
Release: 2%{?dist}
Group: Development/Languages
License: GPLv2
URL: http://www.ngolde.de/tpp.html
Source0: http://www.ngolde.de/download/tpp-1.3.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby(abi) >= 1.8
Requires: ruby-ncurses
BuildArch: noarch

%description
tpp stands for text presentation program and is an ncurses-based presentation
tool. The presentation can be written with your favorite editor in a simple
description format and then shown on any text terminal that is supported by
ncurses - ranging from an old VT100 to the Linux framebuffer to an xterm.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
make install prefix=$RPM_BUILD_ROOT%{_usr} DOCPATH=$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/tpp
%doc %{_mandir}/man1/tpp.1.gz
%doc %{_datadir}/doc/%{name}-%{version}

%changelog
* Mon May 09 2011 jesus m rodriguez <jmrodri@gmail.com> 1.3.1-2
- new package built with tito

* Mon May 09 2011 Jesus Rodriguez <jmrodri@gmail.com> - 1.3.1-1
- Initial package
