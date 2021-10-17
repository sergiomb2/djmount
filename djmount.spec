Name:           djmount
Version:        0.72
Release:        1%{?dist}
Summary:        Mount MediaServers content as a Linux file system
License:        GPLv2+
URL:            http://djmount.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  fuse-devel
BuildRequires:  libupnp-devel
BuildRequires:  libtalloc-devel

%description
djmount is a UPnP AV client. It mounts as a Linux file system the media content
of compatible UPnP AV devices. Djmount discovers automatically all UPnP AV
Media Servers on the network, and make the content available in a directory
tree. All shared files (e.g. Audio or Video files) are directly visible and
can be played using your favorite media player.

%prep
%setup -q

%build
autoreconf --force --install

#export LFLAGS="%{ldflags} -pthread -lupnp -lixml"
#global optflags %%(echo %%{optflags} -fno-pic)
export CFLAGS="%{optflags} -DHAVE_CHARSET=1 -D_FILE_OFFSET_BITS=64 -pthread -I/usr/include/upnp "
export CXXFLAGS="%{optflags} -DHAVE_CHARSET=1 -D_FILE_OFFSET_BITS=64 -pthread -I/usr/include/upnp "
%configure
%make_build

%install
%make_install

%files
%doc COPYING README NEWS AUTHORS ChangeLog TODO INSTALL THANKS search_help.txt
%{_bindir}/djmount

%changelog
* Sat Oct 16 2021 Sérgio Basto <sergio@serjux.com> - 0.72-1
- Update to 0.72

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 0.71-17
- Rebuilt for libupnp 1.8x

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.71-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue May 31 2011 Adam Jackson <ajax@redhat.com> 0.71-4
- Rebuild for new libupnp

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 27 2010 Jean-Francois Saucier <jsaucier@gmail.com> - 0.71-2
- Fix as per bug #583105 suggestion

* Tue Mar 16 2010 Jean-Francois Saucier <jfsaucier@infoglobe.ca> - 0.71-1
- Initial build for Fedora
