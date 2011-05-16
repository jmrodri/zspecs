Summary: A ncurses-based presentation tool
Name: tpp
Version: 1.3.1
Release: 7%{?dist}
Group: Applications/Productivity
License: GPLv2
URL: http://www.ngolde.de/tpp.html
Source0: http://www.ngolde.de/download/%{name}-%{version}.tar.gz
BuildRequires: emacs
Requires: ruby(abi) >= 1.8
Requires: ruby-ncurses
Requires: vim-filesystem
%if 0%{?fedora} >= 15
Requires: emacs-filesystem >= %{_emacs_version} 
%endif
BuildArch: noarch

%description
tpp stands for text presentation program and is a ncurses-based presentation
tool. The presentation can be written with your favorite editor in a simple
description format and then shown on any text terminal that is supported by
ncurses - ranging from an old VT100 to the Linux framebuffer to an xterm.

%prep
%setup -q
pushd examples
for tppfile in *.tpp; do 
  iconv -f ISO-8859-1 -t UTF-8 -o $tppfile.new $tppfile && \
  touch -r $tppfile $tppfile.new && \
  mv $tppfile.new $tppfile
done
popd

%build
%{_emacs_bytecompile} contrib/tpp-mode.el

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -p tpp.rb $RPM_BUILD_ROOT%{_bindir}/tpp
install -d -m 755 $RPM_BUILD_ROOT%{_emacs_sitelispdir}
install -p -m 644 contrib/tpp-mode* $RPM_BUILD_ROOT%{_emacs_sitelispdir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax
install -p -m 644 contrib/tpp.vim $RPM_BUILD_ROOT%{_datadir}/vim/vimfiles/syntax
install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1/
install -p -m 644 doc/tpp.1 $RPM_BUILD_ROOT%{_mandir}/man1/tpp.1

%files
%defattr(-, root, root, -)
%{_bindir}/tpp
%{_mandir}/man1/tpp.1*
%{_emacs_sitelispdir}/tpp-mode*
%doc DESIGN
%doc CHANGES
%doc COPYING
%doc README
%doc THANKS
%doc examples/
%doc contrib/
%{_datadir}/vim/vimfiles/syntax/tpp.vim

%changelog
* Fri May 13 2011 jesus m rodriguez <jmrodri@gmail.com> 1.3.1-7
- remove buildroot stuff
- install vim and emacs files; fix manpage perms
- move iconv to prep section

* Thu May 12 2011 jesus m. rodriguez <jesusr@redhat.com> 1.3.1-6
- fix rpmlint errors/warnings

* Thu May 12 2011 jesus m. rodriguez <jesusr@redhat.com> 1.3.1-5
- reworked install section, listed out docs, fixed man page
- fix typo & remove email addresses.
- use name & version macros in source url
- change Group to Applications/Productivity

* Wed May 11 2011 jesus m. rodriguez <jesusr@redhat.com> 1.3.1-4
- don't use RPM_BUILD_ROOT and buildroot

* Mon May 09 2011 jesus m rodriguez <jmrodri@gmail.com> 1.3.1-3
- rpmlint: setup quite, remove patch0

* Mon May 09 2011 jesus m rodriguez <jmrodri@gmail.com> 1.3.1-2
- new package built with tito

* Mon May 09 2011 Jesus Rodriguez <jmrodri@gmail.com> - 1.3.1-1
- Initial package
