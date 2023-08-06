Name: libcaes
Version: 20180727
Release: 1
Summary: Library to support cross-platform AES encryption
Group: System Environment/Libraries
License: LGPL
Source: %{name}-%{version}.tar.gz
URL: https://github.com/libyal/libcaes
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:  openssl
BuildRequires:  openssl-devel

%description
Library to support cross-platform AES encryption

%package devel
Summary: Header files and libraries for developing applications for libcaes
Group: Development/Libraries
Requires: libcaes = %{version}-%{release}

%description devel
Header files and libraries for developing applications for libcaes.

%package python
Summary: Python 2 bindings for libcaes
Group: System Environment/Libraries
Requires: libcaes = %{version}-%{release} python
BuildRequires: python-devel

%description python
Python 2 bindings for libcaes

%package python3
Summary: Python 3 bindings for libcaes
Group: System Environment/Libraries
Requires: libcaes = %{version}-%{release} python3
BuildRequires: python3-devel

%description python3
Python 3 bindings for libcaes

%prep
%setup -q

%build
%configure --prefix=/usr --libdir=%{_libdir} --mandir=%{_mandir} --enable-python2 --enable-python3
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%license COPYING
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%license COPYING
%doc AUTHORS README ChangeLog
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcaes.pc
%{_includedir}/*
%{_mandir}/man3/*

%files python
%defattr(644,root,root,755)
%license COPYING
%doc AUTHORS README
%{_libdir}/python2*/site-packages/*.a
%{_libdir}/python2*/site-packages/*.la
%{_libdir}/python2*/site-packages/*.so

%files python3
%defattr(644,root,root,755)
%license COPYING
%doc AUTHORS README
%{_libdir}/python3*/site-packages/*.a
%{_libdir}/python3*/site-packages/*.la
%{_libdir}/python3*/site-packages/*.so

%changelog
* Fri Jul 27 2018 Joachim Metz <joachim.metz@gmail.com> 20180727-1
- Auto-generated

