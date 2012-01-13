
%define		qtver		4.6.3
%define		kdever		4.4.5

Summary:	mplayer backend for Phonon
Summary(pl.UTF-8):	Wtyczka mplayer dla Phonona
Name:		phonon-backend-mplayer
Version:	0.git.20100908
Release:	2
License:	LGPL 2.1
Group:		X11/Applications
Source0:	http://www.gitorious.org/phonon/phonon-mplayer/archive-tarball/master
# Source0-md5:	ea4e86aba13efaff5abbc283eb25905c
Patch0:         %{name}-x86_64.patch
URL:		http://kde-apps.org/content/show.php/Phonon+MPlayer+Backend?content=123714
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	phonon-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.293
Provides:	qt4-phonon-backend = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mplayer backend for Phonon.

%description -l pl.UTF-8
Wtyczka mplayer dla Phonona.

%prep
%setup -q -n phonon-phonon-mplayer
%patch0 -p1

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

%post
%banner %{name} -e <<EOF
There is no support to choice playback device from phonon
configurartion. If you want to choice different playback device, you
must manualy set this in .mplayer/config.

Example for second playback device and master mixer channel.
ao=alsa:device=hw=0.1
mixer-channel=Master
EOF

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/plugins/phonon_backend/phonon_mplayer.so
%{_datadir}/kde4/services/phononbackends/mplayer.desktop
