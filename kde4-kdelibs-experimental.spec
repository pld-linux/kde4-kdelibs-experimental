%define		_state		unstable
%define		orgname		kdelibs-experimental
%define		qtver		4.5.1
%define		svn		973768

Summary:	K Desktop Environment - experimental libraries
Summary(es.UTF-8):	K Desktop Environment - bibliotecas
Summary(ko.UTF-8):	KDE - 라이브러리
Summary(pl.UTF-8):	K Desktop Environment - experymentalne biblioteki
Summary(pt_BR.UTF-8):	Bibliotecas de fundação do KDE
Summary(ru.UTF-8):	K Desktop Environment - Библиотеки
Summary(uk.UTF-8):	K Desktop Environment - Бібліотеки
Name:		kde4-kdelibs-experimental
Version:	4.2.90
Release:	1
License:	LGPL
Group:		X11/Libraries
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}svn%{svn}.tar.bz2
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	d484c2080b835e06f2793858a8e68e58
URL:		http://www.kde.org/
BuildRequires:	OpenEXR-devel >= 1.2.2
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	QtDBus-devel >= %{qtver}
BuildRequires:	QtDesigner-devel >= %{qtver}
BuildRequires:	QtGui-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtUiTools-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	kde4-kdelibs-devel = %{version}
BuildRequires:	rpmbuild(macros) >= 1.293
Requires:	QtCore >= %{qtver}
Requires:	kde-common-dirs >= 0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# confuses OpenEXR detection
%undefine	configure_cache

%description
This package includes experimental libraries for KDE.

%package devel
Summary:	kdelibs-experimental - header files and development documentation
Summary(pl.UTF-8):	kdelibs-experimental - pliki nagłówkowe i dokumentacja do kdelibs
Summary(pt_BR.UTF-8):	Arquivos de inclusão e documentação para compilar aplicativos KDE
Summary(ru.UTF-8):	Хедеры и документация для компилляции программ KDE
Summary(uk.UTF-8):	Хедери та документація для компіляції програм KDE
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	acl-devel
Requires:	fam-devel
Requires:	libart_lgpl-devel
Requires:	libidn-devel
Requires:	mdns-bonjour-devel
Requires:	pcre-devel
Requires:	phonon-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXt-devel

%description devel
This package contains header files and development documentation for
kdelibs-experimental.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących kdelibs-experimental.

%description devel -l pt_BR.UTF-8
Este pacote contém os arquivos de inclusão que são necessários para
compilar aplicativos KDE.

%description devel -l ru.UTF-8
Этот пакет содержит хедеры, необходимые для компиляции программ для
KDE.

%description devel -l uk.UTF-8
Цей пакет містить хедери, необхідні для компіляції програм для KDE.

%prep
%setup -q -n %{orgname}-%{version}
#%setup -q -n %{orgname}-%{version}svn%{svn}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCONFIG_INSTALL_DIR=%{_datadir}/config \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-DDATA_INSTALL_DIR=%{_datadir}/apps \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DMIME_INSTALL_DIR=/nogo \
	-DTEMPLATES_INSTALL_DIR=%{_datadir}/templates \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
	-DKDE_DISTRIBUTION_TEXT="PLD-Linux" \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	-DKDE4_ENABLE_FINAL=OFF \
	../

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libknotificationitem-1.so
%{_datadir}/dbus-1/interfaces/org.kde.NotificationItem*.xml

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/knotificationitem-1
%{_includedir}/knotificationitem-1/*
