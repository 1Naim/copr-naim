%define _disable_source_fetch 0
%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define debug_package %{nil}

Name:       obs-vertical-canvas
Version:    1.4.8
Release:    1%{?dist}
Summary:    Vertical canvas plugin for OBS

License:    GPL=2.0
URL:        https://github.com/Aitum/obs-vertical-canvas
Source0:    %{URL}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  obs-studio-devel
BuildRequires:  libcurl-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtwayland-devel
Requires:       obs-studio
Requires:       qt6-qtbase

%description
Plugin for OBS Studio to add vertical canvas by Aitum

%prep
%autosetup

%build
%cmake \
    -DBUILD_OUT_OF_TREE=On \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

# Move built files to a different folder
mkdir -p preserve/%{_libdir}/obs-plugins
mkdir -p preserve/%{_prefix}/lib/obs-plugins
mkdir -p preserve/%{_datadir}/obs/obs-plugins

mv %{buildroot}%{_datadir}/obs/obs-plugins/vertical-canvas preserve/%{_datadir}/obs/obs-plugins
mv %{buildroot}/usr/lib/obs-plugins/vertical-canvas.so preserve/%{_prefix}/lib/obs-plugins
mv %{buildroot}/usr/obs-plugins/64bit/vertical-canvas.so preserve/%{_libdir}/obs-plugins

# Purge the unholy
rm -rf %{buildroot}/*

# Restore order
mv preserve/%{_prefix} %{buildroot}

%files
%{_datadir}/obs/obs-plugins/vertical-canvas
/usr/lib/obs-plugins/vertical-canvas.so
/usr/lib64/obs-plugins/vertical-canvas.so
