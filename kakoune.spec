Name:           kakoune
Version:        2026.05.04
Release:        4%{?dist}
Summary:        Mawww's experiment for a better code editor
License:        Unlicense
URL:            https://github.com/gzcxx/kakoune
Source0:        https://github.com/gzcxx/kakoune/archive/refs/heads/master.tar.gz#/kakoune-master.tar.gz

BuildRequires:  asciidoc
BuildRequires:  gcc-c++ >= 10.3
BuildRequires:  glibc-langpack-en
BuildRequires:  pkgconfig(ncurses) >= 5.3
BuildRequires:  cmake
BuildRequires:  make

%description
Kakoune is a code editor that implements Vi's "keystrokes as a text editing language" model.

%prep
%setup -q -n kakoune-master

%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license UNLICENSE
%doc README.asciidoc CONTRIBUTING VIMTOKAK doc/pages/changelog.asciidoc
%{_bindir}/kak
%{_datadir}/kak/
%{_libexecdir}/kak/
%{_mandir}/man1/*.1*

%changelog
* Mon May 04 2026 Maxime Coste <mawww@kakoune.org> - 2026.05.04-4
- Initial release
