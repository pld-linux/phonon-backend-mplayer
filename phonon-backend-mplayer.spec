
#TODO

# Linking CXX shared module phonon_mplayer.so
# /usr/bin/ld: libmplayer/liblibmplayer.a(MPlayerProcess.cpp.o): relocation R_X86_64_32S against `_ZN7QString11shared_nullE' can not be used when making a shared object; recompile with -fPIC
# libmplayer/liblibmplayer.a: could not read symbols: Bad value



%define		qtver		4.6.3
%define		kdever		4.4.5

Summary:	mplayer backend for Phonon
Summary(pl.UTF-8):	Wtyczka mplayer dla Phonona
Name:		phonon-backend-mplayer
Version:	0.git.20100908.1
Release:	0.1
License:	LGPL 2.1
Group:		X11/Applications
Source0:	http://www.gitorious.org/phonon/phonon-mplayer/archive-tarball/master
# Source0-md5:	ea4e86aba13efaff5abbc283eb25905c
#URL:		http://
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	phonon-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mplayer backend for Phonon.

%description -l pl.UTF-8
Wtyczka mplayer dla Phonona.

%prep
%setup -q -n phonon-phonon-mplayer

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_mplayer.so
#%{_datadir}/kde4/services/phononbackends/vlc.desktop
