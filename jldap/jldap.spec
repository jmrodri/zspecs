Summary: The LDAP Class Libraries for Java (JLDAP)
Name: jldap
Version: 4.3
Release: 1%{?dist}
Group: Applications/Productivity
License: GPLv2
URL: http://www.ngolde.de/tpp.html
# The source for this package was pulled from upstream's vcs.
# Use the following command to generate the tarball:
# git clone git://git.openldap.org/openldap-jldap.git
# git archive --format=tar.gz -o jldap-4.3.tar.gz --prefix=jldap-4.3/ Oct_ndk_2007
Source0: %{name}-%{version}.tar.gz
BuildRequires: java-devel >= 0:1.6.0
BuildRequires: ant >= 0:1.7.0
BuildRequires: jpackage-utils
Requires: java >= 0:1.6.0
BuildArch: noarch
Patch0: jldap-4.3-javac.xml.patch

%description
The LDAP Class Libraries for Java (JLDAP) enable you to write applications to
access, manage, update, and search for information stored in directories
accessible using LDAPv3. JLDAP was developed by Novell.

%package javadoc
Summary: Documentation for the LDAP Class Libraries for Java (JLDAP)
Group: Applications/Productivity

%description javadoc
Documentation for the LDAP Class Libraries for Java (JLDAP)

%prep
%setup -q
patch -p1 < %{PATCH0}
# remove dsml support
rm -rf com/novell/ldap/Dsml*.java
rm -rf com/novell/ldap/DSML*.java
rm -rf com/novell/ldap/util/HttpRequestCallback.java
# remove spml support
rm -rf com/novell/ldap/spml/*.java
rm -rf com/novell/ldap/SPML*.java

%build
mkdir -p ext
LANG=en_US.UTF-8 ant release doc

%install
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/java/
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/javadoc/%{name}-%{version}/
install -m 644 lib/ldap.jar $RPM_BUILD_ROOT%{_datadir}/java/%{name}-%{version}.jar
cp -R doc/ $RPM_BUILD_ROOT%{_datadir}/javadoc/%{name}-%{version}/
ln -s %{_datadir}/java/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_datadir}/java/%{name}.jar

%files
%defattr(-, root, root, -)
%{_datadir}/java/%{name}-%{version}.jar
%{_datadir}/java/%{name}.jar
%doc COPYRIGHT
%doc README
%doc LICENSE
%doc LICENSE-2.0.1

%files javadoc
%doc %{_datadir}/javadoc/%{name}-%{version}/

%changelog
* Thu Mar 08 2012 jesus m. rodriguez <jesusr@redhat.com> 4.3-1
- new package built with tito

