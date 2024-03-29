#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : protobuf-c
Version  : 1.4.1
Release  : 26
URL      : https://github.com/protobuf-c/protobuf-c/releases/download/v1.4.1/protobuf-c-1.4.1.tar.gz
Source0  : https://github.com/protobuf-c/protobuf-c/releases/download/v1.4.1/protobuf-c-1.4.1.tar.gz
Summary  : @PACKAGE_DESCRIPTION@
Group    : Development/Tools
License  : BSD-2-Clause
Requires: protobuf-c-bin = %{version}-%{release}
Requires: protobuf-c-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : pkgconfig(protobuf)
BuildRequires : valgrind

%description
[![Build Status](https://github.com/protobuf-c/protobuf-c/actions/workflows/build.yml/badge.svg)](https://github.com/protobuf-c/protobuf-c/actions) [![Coverage Status](https://coveralls.io/repos/protobuf-c/protobuf-c/badge.png)](https://coveralls.io/r/protobuf-c/protobuf-c)

%package bin
Summary: bin components for the protobuf-c package.
Group: Binaries

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

%description lib
lib components for the protobuf-c package.


%prep
%setup -q -n protobuf-c-1.4.1
cd %{_builddir}/protobuf-c-1.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663349005
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1663349005
rm -rf %{buildroot}
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
/usr/include/protobuf-c/protobuf-c.proto
/usr/lib64/libprotobuf-c.so
/usr/lib64/pkgconfig/libprotobuf-c.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libprotobuf-c.so.1
/usr/lib64/libprotobuf-c.so.1.0.0
