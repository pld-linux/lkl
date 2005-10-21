Summary:	LKL is a userspace key logger
Summary(pl):	LKL to keylogger dzia³aj±cy w przestrzeni u¿ytkownika
Name:		lkl
Version:	0.1.0
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/sourceforge/lkl/%{name}-%{version}.tar.gz
# Source0-md5:	249c2025295f1227f8cd660f7775d2f4
URL:		http://www.spine-group.org/tool.htm
BuildRequires:	autoconf
BuildRequires:	automake
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
