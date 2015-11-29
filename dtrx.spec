Summary:	Cleanly extract many archive types
Summary(hu.UTF-8):	Sokféle tömörített állomány egyszerű kicsomagolása
Name:		dtrx
Version:	6.6
Release:	0.1
License:	GPL v3
Group:		Applications/Archiving
Source0:	http://brettcsmith.org/2007/dtrx/%{name}-%{version}.tar.gz
# Source0-md5:	3c6e12c95070942e546645dc8d1c35f6
URL:		http://brettcsmith.org/2007/dtrx/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
Requires:	binutils
Requires:	bzip2
Requires:	cpio
Requires:	gzip
Requires:	p7zip
Requires:	rpm-utils
Requires:	tar
Requires:	unzip
Requires:	xz
Suggests:	cabextract
Suggests:	synce-unshield
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dtrx extracts archives in a number of different formats; it currently
supports tar, zip (including self-extracting .exe files), cpio, rpm,
deb, gem, 7z, cab, rar, and InstallShield files. It can also
decompress files compressed with gzip, bzip2, lzma, or compress.

%description -l hu.UTF-8
dtrx a tömörített állományok sok fajtáját képes kicsomagolni; jelenleg
tar, zip (önkicsomagoló .exe fájlokat is beleértve), cpio, rpm, deb,
gem, 7z, cab, rar és InstallShield fájlokat támogatja. A gzip-pel,
bzip2-vel, lzma-val tömörített fájlokat is képes kicsomagolni vagy
tömöríteni.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
%py_install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL NEWS PKG-INFO
%attr(755,root,root) %{_bindir}/dtrx
%{py_sitescriptdir}/*.egg-info
