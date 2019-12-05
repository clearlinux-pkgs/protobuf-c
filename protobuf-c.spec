#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : protobuf-c
Version  : 1.3.2
Release  : 22
URL      : https://github.com/protobuf-c/protobuf-c/releases/download/v1.3.2/protobuf-c-1.3.2.tar.gz
Source0  : https://github.com/protobuf-c/protobuf-c/releases/download/v1.3.2/protobuf-c-1.3.2.tar.gz
Summary  : Protocol Buffers C library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: protobuf-c-bin = %{version}-%{release}
Requires: protobuf-c-lib = %{version}-%{release}
Requires: protobuf-c-license = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(protobuf)
BuildRequires : valgrind
Patch1: notests.patch

%description
[![Build Status](https://travis-ci.org/protobuf-c/protobuf-c.png?branch=master)](https://travis-ci.org/protobuf-c/protobuf-c) [![Coverage Status](https://coveralls.io/repos/protobuf-c/protobuf-c/badge.png)](https://coveralls.io/r/protobuf-c/protobuf-c)

%package bin
Summary: bin components for the protobuf-c package.
Group: Binaries
Requires: protobuf-c-license = %{version}-%{release}

%description bin
bin components for the protobuf-c package.


%package dev
Summary: dev components for the protobuf-c package.
Group: Development
Requires: protobuf-c-lib = %{version}-%{release}
Requires: protobuf-c-bin = %{version}-%{release}
Provides: protobuf-c-devel = %{version}-%{release}
Requires: protobuf-c = %{version}-%{release}

%description dev
dev components for the protobuf-c package.


%package lib
Summary: lib components for the protobuf-c package.
Group: Libraries
Requires: protobuf-c-license = %{version}-%{release}

%description lib
lib components for the protobuf-c package.


%package license
Summary: license components for the protobuf-c package.
Group: Default

%description license
license components for the protobuf-c package.


%prep
%setup -q -n protobuf-c-1.3.2
cd %{_builddir}/protobuf-c-1.3.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575563123
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1575563123
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/protobuf-c
cp %{_builddir}/protobuf-c-1.3.2/LICENSE %{buildroot}/usr/share/package-licenses/protobuf-c/7497f724cc1f1ee84e4ced1f6a59e2d39793a231
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/protoc-c
/usr/bin/protoc-gen-c

%files dev
%defattr(-,root,root,-)
/usr/include/google/protobuf-c/protobuf-c.h
/usr/include/protobuf-c/protobuf-c.h
/usr/lib64/libprotobuf-c.so
/usr/lib64/pkgconfig/libprotobuf-c.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libprotobuf-c.so.1
/usr/lib64/libprotobuf-c.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/protobuf-c/7497f724cc1f1ee84e4ced1f6a59e2d39793a231
