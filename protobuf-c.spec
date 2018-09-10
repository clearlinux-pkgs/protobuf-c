#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : protobuf-c
Version  : 1.3.1
Release  : 16
URL      : https://github.com/protobuf-c/protobuf-c/releases/download/v1.3.1/protobuf-c-1.3.1.tar.gz
Source0  : https://github.com/protobuf-c/protobuf-c/releases/download/v1.3.1/protobuf-c-1.3.1.tar.gz
Summary  : Protocol Buffers C library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: protobuf-c-bin
Requires: protobuf-c-lib
Requires: protobuf-c-license
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : pkgconfig(protobuf)
BuildRequires : valgrind

%description
[![Build Status](https://travis-ci.org/protobuf-c/protobuf-c.png?branch=master)](https://travis-ci.org/protobuf-c/protobuf-c) [![Coverage Status](https://coveralls.io/repos/protobuf-c/protobuf-c/badge.png)](https://coveralls.io/r/protobuf-c/protobuf-c)

%package bin
Summary: bin components for the protobuf-c package.
Group: Binaries
Requires: protobuf-c-license

%description bin
bin components for the protobuf-c package.


%package dev
Summary: dev components for the protobuf-c package.
Group: Development
Requires: protobuf-c-lib
Requires: protobuf-c-bin
Provides: protobuf-c-devel

%description dev
dev components for the protobuf-c package.


%package lib
Summary: lib components for the protobuf-c package.
Group: Libraries
Requires: protobuf-c-license

%description lib
lib components for the protobuf-c package.


%package license
Summary: license components for the protobuf-c package.
Group: Default

%description license
license components for the protobuf-c package.


%prep
%setup -q -n protobuf-c-1.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536562664
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536562664
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/protobuf-c
cp LICENSE %{buildroot}/usr/share/doc/protobuf-c/LICENSE
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
%defattr(-,root,root,-)
/usr/share/doc/protobuf-c/LICENSE
