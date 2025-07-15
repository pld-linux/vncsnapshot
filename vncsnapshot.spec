Summary:	Command line program for save JPEG image of VNC server's screen
Summary(pl.UTF-8):	Działający z linii poleceń program do robienia zrzutów ekranu z serwera VNC
Name:		vncsnapshot
Version:	1.2a
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/vncsnapshot/%{name}-%{version}-src.tar.bz2
# Source0-md5:	6abf3c0c5bbfde70d51fa09edfb717da
Patch0:		%{name}-fprintf.patch
URL:		http://vncsnapshot.sourceforge.net/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VNC Snapshot is a command-line program for VNC. It will save a JPEG
image of the VNC server's screen.

%description -l pl.UTF-8
VNC Snapshot jest działającym z linii poleceń narzędziem dla VNC.
Zachowuje obraz ekranu serwera VNC w pliku JPEG.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D %{name}.man1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE* BUGS README RELEASE-NOTES.txt web*html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
