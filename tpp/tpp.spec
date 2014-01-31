Summary: A ncurses-based presentation tool
Name: tpp
Version: 1.3.1
Release: 17%{?dist}
Group: Applications/Productivity
License: GPLv2
URL: http://www.ngolde.de/tpp.html
Source0: http://www.ngolde.de/download/%{name}-%{version}.tar.gz
Patch0: c0a755be54bd69333adc6cfb0071fcb5260404d6.patch
Patch1: 15-optional-exec.patch
BuildRequires: emacs
Requires: ruby-ncurses
%if 0%{?fedora} >= 15
Requires: ruby(release)
Requires: emacs-filesystem >= %{_emacs_version} 
Requires: vim-filesystem
%else
Requires: ruby(abi) >= 1.8
%endif
BuildArch: noarch

%description
tpp stands for text presentation program and is a ncurses-based presentation
tool. The presentation can be written with your favorite editor in a simple
description format and then shown on any text terminal that is supported by
ncurses - ranging from an old VT100 to the Linux framebuffer to an xterm.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
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
%if 0%{?fedora} < 15
%dir %{_emacs_sitelispdir}/                                       
%endif
%{_emacs_sitelispdir}/tpp-mode*
%doc DESIGN
%doc CHANGES
%doc COPYING
%doc README
%doc THANKS
%doc examples/
%{_datadir}/vim/vimfiles/syntax/tpp.vim

%changelog
* Fri Jan 31 2014 jesus m. rodriguez <jesusr@redhat.com> 1.3.1-17
- 977368: apply Adam Miller's patch correctly. (jesusr@redhat.com)
- Remove dep on vim-filesystem for EPEL6, subpackage doesn't exist for EL6 (maxamillion@fedoraproject.org)
- Fix ruby macros for EPEL6 (maxamillion@fedoraproject.org)
* Sat Jan 18 2014 jesus m. rodriguez <jmrodri@gmail.com> 1.3.1-16
- 976686, 976687: add exec patch to spec file (jmrodri@gmail.com)
- 976686, 976687: Don't execute commands with --exec by default (abe@debian.org)

* Wed Jan 15 2014 jesus m. rodriguez <jmrodri@gmail.com> 1.3.1-15
- patch to make it work (jmrodri@gmail.com)

* Wed Jan 15 2014 jesus m. rodriguez <jesusr@redhat.com> 1.3.1-14
- 977368: remove invalid vim-filesystem dependency (maxamillion@fedoraproject.org)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 02 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.1-12
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 01 2011 jesus m rodriguez <jmrodri@gmail.com> 1.3.1-9
- added email address to the changelog
- removed doc contrib from files section
- guarantee the ownership of _emacs_sitelispdir for F<15

* Mon May 16 2011 jesus m. rodriguez <jmrodri@gmail.com> 1.3.1-8
- require emacs-filesystem for F15 or later

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
