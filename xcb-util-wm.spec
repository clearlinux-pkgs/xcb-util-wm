#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xcb-util-wm
Version  : 0.4.1
Release  : 2
URL      : https://xcb.freedesktop.org/dist/xcb-util-wm-0.4.1.tar.bz2
Source0  : https://xcb.freedesktop.org/dist/xcb-util-wm-0.4.1.tar.bz2
Summary  : XCB ICCCM binding
Group    : Development/Tools
License  : MIT
Requires: xcb-util-wm-lib
BuildRequires : doxygen
BuildRequires : graphviz
BuildRequires : libxcb-dev
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xorg-macros)

%description
About XCB util modules
======================
The XCB util modules provides a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

%package dev
Summary: dev components for the xcb-util-wm package.
Group: Development
Requires: xcb-util-wm-lib
Provides: xcb-util-wm-devel

%description dev
dev components for the xcb-util-wm package.


%package lib
Summary: lib components for the xcb-util-wm package.
Group: Libraries

%description lib
lib components for the xcb-util-wm package.


%prep
%setup -q -n xcb-util-wm-0.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1518482714
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1518482714
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/xcb/xcb_ewmh.h
/usr/include/xcb/xcb_icccm.h
/usr/lib64/libxcb-ewmh.so
/usr/lib64/libxcb-icccm.so
/usr/lib64/pkgconfig/xcb-ewmh.pc
/usr/lib64/pkgconfig/xcb-icccm.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libxcb-ewmh.so.2
/usr/lib64/libxcb-ewmh.so.2.0.0
/usr/lib64/libxcb-icccm.so.4
/usr/lib64/libxcb-icccm.so.4.0.0
