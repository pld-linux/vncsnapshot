Summary:	Command line program for save JPEG image of VNC server's screen
Summary(pl):	Program z lini poleceñ do robienia zrzutów ekranu z serwera VNC
Name:		vncsnapshot
Version:	1.1
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://dl.sourceforge.net/sourceforge/vncsnapshot/%{name}-%{version}-src.tar.bz2
# Source0-md5:	d526e821eef087e89eebde57f3e02a4a
URL:		http://vncsnapshot.sourceforge.net/
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VNC Snapshot is a command-line program for VNC. It will save a JPEG
image of the VNC server's screen.   

%description -l pl
VNC Snapshot jest narzêdziem z lini poleceñ dla VNC. Zachowuje obraz
ekranu serwera VNC w pliku JPEG.

%prep
%setup -q

%build
%{__make} CDEBUGFLAGS="%{rpmcflags}"

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
