Summary:	PNG library
Summary(de.UTF-8):	PNG-Library
Summary(fr.UTF-8):	Librarie PNG
Summary(pl.UTF-8):	Biblioteka PNG
Summary(tr.UTF-8):	PNG kitaplığı
Name:		libpng1
Version:	1.0.24
Release:	1
Epoch:		2
License:	distributable
Group:		Libraries
Source0:	http://dl.sourceforge.net/libpng/libpng-%{version}.tar.bz2
# Source0-md5:	a69f4048b951ef2142d033495e7112da
Patch0:		%{name}-opt.patch
Patch1:		%{name}-pngminus.patch
Patch2:		%{name}-SONAME.patch
Patch3:		%{name}-libdirfix.patch
URL:		http://www.libpng.org/pub/png/libpng.html
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	zlib-devel
Provides:	libpng = %{version}
%ifarch %{x8664} ia64 ppc64 s390x sparc64
Provides:	libpng10.so.0()(64bit)
%else
Provides:	libpng10.so.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PNG library is a collection of routines used to create and
manipulate PNG format graphics files. The PNG format was designed as a
replacement for GIF, with many improvements and extensions.

%description -l de.UTF-8
Die PNG-Library ist eine Sammlung von Routinen zum Erstellen und
Bearbeiten von Grafiken im PNG-Format. Das PNG-Format wurde als Ersatz
für GIF entwickelt und enthält viele Verbesserungen und Erweiterungen.

%description -l fr.UTF-8
La librairie PNG est un ensemble de routines utilisées pour créer et
manipuler des fichiers graphiques au format PNG. Le format PNG a été
élaboré pour remplacer le GIF, avec de nombreuses améliorations et
extensions.

%description -l pl.UTF-8
Biblioteka PNG to zestaw funkcji używanych do tworzenia i obróbki
plików w formacie graficznym PNG. Format ten został stworzony jako
zamiennik dla formatu GIF, z wieloma ulepszeniami i rozszerzeniami.

%description -l tr.UTF-8
PNG kitaplığı, PNG formatındaki resim dosyalarını işlemeye yönelik
yordamları içerir. PNG, GIF formatının yerini almak üzere tasarlanmış
bir resim formatıdır.

%package devel
Summary:	libpng header files
Summary(de.UTF-8):	Headers und statische Libraries
Summary(fr.UTF-8):	En-têtes et bibliothèques statiques
Summary(pl.UTF-8):	Pliki nagłówkowe libpng
Summary(tr.UTF-8):	Başlık dosyaları ve statik kitaplıklar
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zlib-devel
Provides:	libpng-devel = %{version}
Conflicts:	libpng-devel >= 1.2.0

%description devel
The header files and static libraries are only needed for development
of programs using the PNG library.

%description devel -l de.UTF-8
Die Header-Dateien und statischen Libraries werden nur zur Entwicklung
von Programmen mit der PNG-Library benötigt.

%description devel -l fr.UTF-8
Fichiers d'en-tete et les librairies qui sont requis seulement pour le
développement avec la librairie PNG.

%description devel -l pl.UTF-8
W pakiecie tym znajdują się pliki nagłówkowe, przeznaczone dla
programistów używających biblioteki PNG.

%description devel -l tr.UTF-8
PNG kitaplığını kullanan programlar geliştirmek için gereken
kitaplıklar ve başlık dosyaları.

%package static
Summary:	Static libpng libraries
Summary(pl.UTF-8):	Biblioteki statyczne libpng
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	libpng-static = %{version}
Conflicts:	libpng-static >= 1.2.0

%description static
Static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne.

%package progs
Summary:	libpng utility programs
Summary(pl.UTF-8):	Programy użytkowe libpng
Group:		Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	libpng-progs = %{version}
Conflicts:	libpng-progs >= 1.2.0

%description progs
This package contains utility programs to convert png files to and
from pnm files.

%description progs -l pl.UTF-8
Narzędzia do konwersji plików png z lub do plików pnm.

%prep
%setup -q -n libpng-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

ln -s scripts/makefile.linux ./Makefile

%build
%{__make} \
	prefix=%{_prefix} \
	LIBPATH=%{_libdir} \
	CC="%{__cc}" \
%ifarch %{x8664}
	OPT_FLAGS="%{rpmcflags} -DPNG_NO_MMX_CODE"
%else
	OPT_FLAGS="%{rpmcflags}"
%endif

%{__make} -C contrib/pngminus -f makefile.std \
	LIBPATH=%{_libdir} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags} -I../.."

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{3,5}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	LIBPATH=%{_libdir} \
	MANPATH=%{_mandir}

install contrib/pngminus/{png2pnm,pnm2png} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ANNOUNCE CHANGES KNOWNBUG README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/libpng10.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/libpng*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_pkgconfigdir}/libpng*.pc
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pn*
