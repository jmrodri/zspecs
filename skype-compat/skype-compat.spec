Summary: A telecommunications application software
Name: skype-compat
Version: 4.3.0.37
Release: 2%{?dist}
Group: Internet/Communications
License: GPLv2
URL: http://github.com/jmrodri/zspecs/skype-compat

%description
A telecommunications application software that specializes in providing video
chat and voice calls from computers, tablets and mobile devices via the Internet
to other devices 

%prep

%build

%install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/skype

ln -s /opt/skype-%{version}/skype %{_binddir}/skype
ln -s /opt/skype-%{version}/sounds/ %{_datadir}/skype/sounds
ln -s /opt/skype-%{version}/lang/ %{_datadir}/skype/lang
ln -s /opt/skype-%{version}/avatars/ %{_datadir}/skype/avatars

%files
%defattr(-, root, root, -)
%{_bindir}/skype
%{_datadir}/skype

%changelog
* Tue Jan 06 2015 jesus m. rodriguez <jmrodri@gmail.com> 4.3.0.37-2
- new package built with tito

