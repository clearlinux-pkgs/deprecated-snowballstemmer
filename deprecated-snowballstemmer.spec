#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-snowballstemmer
Version  : 1.2.1
Release  : 24
URL      : http://pypi.debian.net/snowballstemmer/snowballstemmer-1.2.1.tar.gz
Source0  : http://pypi.debian.net/snowballstemmer/snowballstemmer-1.2.1.tar.gz
Summary  : This package provides 16 stemmer algorithms (15 + Poerter English stemmer) generated from Snowball algorithms.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: deprecated-snowballstemmer-license = %{version}-%{release}
Requires: deprecated-snowballstemmer-python = %{version}-%{release}
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3

%description
Snowball stemming library collection for Python
===============================================

%package legacypython
Summary: legacypython components for the deprecated-snowballstemmer package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-snowballstemmer package.


%package license
Summary: license components for the deprecated-snowballstemmer package.
Group: Default

%description license
license components for the deprecated-snowballstemmer package.


%package python
Summary: python components for the deprecated-snowballstemmer package.
Group: Default

%description python
python components for the deprecated-snowballstemmer package.


%prep
%setup -q -n snowballstemmer-1.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554328772
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-snowballstemmer
cp LICENSE.rst %{buildroot}/usr/share/package-licenses/deprecated-snowballstemmer/LICENSE.rst
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-snowballstemmer/LICENSE.rst

%files python
%defattr(-,root,root,-)
