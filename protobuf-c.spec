#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : protobuf-c
Version  : 1.2.1
Release  : 3
URL      : https://github.com/protobuf-c/protobuf-c/releases/download/v1.2.1/protobuf-c-1.2.1.tar.gz
Source0  : https://github.com/protobuf-c/protobuf-c/releases/download/v1.2.1/protobuf-c-1.2.1.tar.gz
Summary  : Protocol Buffers C library
Group    : Development/Tools
License  : BSD-2-Clause
Requires: protobuf-c-bin
Requires: protobuf-c-lib
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : pkgconfig(protobuf)
BuildRequires : valgrind

%description
[![Build Status](https://travis-ci.org/protobuf-c/protobuf-c.png?branch=master)](https://travis-ci.org/protobuf-c/protobuf-c) [![Coverage Status](https://coveralls.io/repos/protobuf-c/protobuf-c/badge.png)](https://coveralls.io/r/protobuf-c/protobuf-c)

%package bin
Summary: bin components for the protobuf-c package.
Group: Binaries

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

%description lib
lib components for the protobuf-c package.


%prep
%setup -q -n protobuf-c-1.2.1

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/protoc-c

%files dev
%defattr(-,root,root,-)
/usr/include/google/protobuf-c/protobuf-c.h
/usr/include/protobuf-c/protobuf-c.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
