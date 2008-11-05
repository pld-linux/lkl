Summary:	LKL is a userspace key logger
Summary(pl.UTF-8):	LKL to keylogger działający w przestrzeni użytkownika
Name:		lkl
Version:	0.1.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/sourceforge/lkl/%{name}-%{version}.tar.gz
# Source0-md5:	039f6e81c272e4285deab487adb81d8e
URL:		http://sourceforge.net/projects/lkl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LKL is a userspace keylogger that runs under linux--x86/arch.LKL
sniffs and logs everything pass tought the hardware keyboard port
(0x60).

%description -l pl.UTF-8
LKL to keylogger działający w przestrzeni użytkownika, działający na
platformie x86. Wyłapuje i loguje wszystko co przechodzi przez
sprzętowy port klawiatury (0x60).

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/keymaps
install keymaps/* $RPM_BUILD_ROOT%{_datadir}/%{name}/keymaps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
