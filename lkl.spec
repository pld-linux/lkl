Summary:	LKL is a userspace key logger
Summary(pl):	LKL to keylogger dzia³aj±cy w przestrzeni u¿ytkownika
Name:		lkl
Version:	0.0.2
Release:	0.1
License:	GPL v2
Vendor:		vl4d@spine-group.org
Group:		Applications/System
Source0:	http://www.spine-group.org/proggy/%{name}-%{version}.tar.gz
# Source0-md5:	02dbbb6ab921bf88e431bbc154fdc01a
URL:		http://www.spine-group.org/tool.htm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LKL is a userspace keylogger that runs under linux--x86/arch.LKL
sniffs and logs everything pass tought the hardware keyboard port
(0x60).

%description -l pl
LKL to keylogger dzia³aj±cy w przestrzeni u¿ytkownika, dzia³aj±cy na
platformie x86. Wy³apuje i loguje wszystko co przechodzi przez
sprzêtowy port klawiatury (0x60).

%prep
%setup -q -n %{name}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS NEWS ChangeLog
%attr(755,root,root) %{_bindir}/*
