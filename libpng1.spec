Summary:	PNG library
Summary(de):	PNG-Library
Summary(fr):	Librarie PNG
Summary(pl):	Biblioteka PNG
Summary(tr):	PNG kitapl���
Name:		libpng1
Version:	1.0.20
Release:	1
Epoch:		2
License:	distributable
Group:		Libraries
Source0:	http://dl.sourceforge.net/libpng/libpng-%{version}.tar.bz2
# Source0-md5:	7c2fb566d3e5e70c8a5eeb719e67f26b
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

%description -l de
Die PNG-Library ist eine Sammlung von Routinen zum Erstellen und
Bearbeiten von Grafiken im PNG-Format. Das PNG-Format wurde als Ersatz
f�r GIF entwickelt und enth�lt viele Verbesserungen und Erweiterungen.

%description -l fr
La librairie PNG est un ensemble de routines utilis�es pour cr�er et
manipuler des fichiers graphiques au format PNG. Le format PNG a �t�
�labor� pour remplacer le GIF, avec de nombreuses am�liorations et
extensions.

%description -l pl
Biblioteka PNG to zestaw funkcji u�ywanych do tworzenia i obr�bki
plik�w w formacie graficznym PNG. Format ten zosta� stworzony jako
zamiennik dla formatu GIF, z wieloma ulepszeniami i rozszerzeniami.

%description -l tr
PNG kitapl���, PNG format�ndaki resim dosyalar�n� i�lemeye y�nelik
yordamlar� i�erir. PNG, GIF format�n�n yerini almak �zere tasarlanm��
bir resim format�d�r.

%package devel
Summary:	libpng header files
Summary(de):	Headers und statische Libraries
Summary(fr):	En-t�tes et biblioth�ques statiques
Summary(pl):	Pliki nag��wkowe libpng
Summary(tr):	Ba�l�k dosyalar� ve statik kitapl�klar
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	zlib-devel
Provides:	libpng-devel = %{version}
Conflicts:	libpng-devel >= 1.2.0

%description devel
The header files and static libraries are only needed for development
of programs using the PNG library.

%description devel -l de
Die Header-Dateien und statischen Libraries werden nur zur Entwicklung
von Programmen mit der PNG-Library ben�tigt.

%description devel -l fr
Fichiers d'en-tete et les librairies qui sont requis seulement pour le
d�veloppement avec la librairie PNG.

%description devel -l pl
W pakiecie tym znajduj� si� pliki nag��wkowe, przeznaczone dla
programist�w u�ywaj�cych biblioteki PNG.

%description devel -l tr
PNG kitapl���n� kullanan programlar geli�tirmek i�in gereken
kitapl�klar ve ba�l�k dosyalar�.

%package static
Summary:	Static libpng libraries
Summary(pl):	Biblioteki statyczne libpng
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	libpng-static = %{version}
Conflicts:	libpng-static >= 1.2.0

%description static
Static libraries.

%description static -l pl
Biblioteki statyczne.

%package progs
Summary:	libpng utility programs
Summary(pl):	Programy u�ytkowe libpng
Group:		Applications/Graphics
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	libpng-progs = %{version}
Conflicts:	libpng-progs >= 1.2.0

%description progs
This package contains utility programs to convert png files to and
from pnm files.

%description progs -l pl
Narz�dzia do konwersji plik�w png z lub do plik�w pnm.

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
	OPT_FLAGS="%{rpmcflags}"

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
