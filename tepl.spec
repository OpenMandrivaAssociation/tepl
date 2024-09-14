%global api	6
%global major	0
%define libname %mklibname tepl %{api} %{major}
%define girname	%mklibname tepl-gir %{api}
%define devname %mklibname -d tepl %{api}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:           tepl
Version:        6.11.0
Release:        1
Summary:        Text editor product line
Group:		System/Libraries

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Tepl
#Source0:        https://download.gnome.org/sources/tepl/%{url_ver}/tepl-%{version}.tar.xz
#Source0:        https://gitlab.gnome.org/swilmet/tepl/-/archive/%{version}/tepl-%{version}.tar.bz2
#Source0:        https://github.com/gedit-technology/libgedit-tepl/releases/download/%{version}/libgedit-tepl-%{version}.tar.xz
Source0:        https://gitlab.gnome.org/World/gedit/libgedit-tepl/-/archive/%{version}/libgedit-tepl-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(libgedit-amtk-5)
BuildRequires:  pkgconfig(libgedit-gfls-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz-gobject)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libgedit-gtksourceview-300)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uchardet)

Obsoletes:	%{name} < %{EVRD}

%description
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs. Tepl is the acronym for “Text editor product line”.

%package        -n %{libname}
Summary:        Libraries for %{name}
Requires:	%{name} >= %{version}-%{release}
Obsoletes:	%{_lib}tepl0 < 4.2.0-2
Obsoletes:	%{libname} < %{EVRD}
Obsoletes:	%{_lib}tepl6_2

%description    -n %{libname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for Tepl
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{name} < 4.2.0-2
Obsoletes:	%{girname} < %{EVRD}

%description -n %{girname}
GObject Introspection interface description for Tepl.

%package        -n %{devname}
Summary:        Development files for %{name}
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}tepl-devel < 4.2.0-2
Obsoletes:	%{devname} < %{EVRD}

%description    -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n libgedit-tepl-%{version} -p1

%build
%meson  -Dgtk_doc=true
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -delete

%find_lang libgedit-tepl-%{api}

%files -f libgedit-tepl-%{api}.lang
%doc NEWS README.md

%files -n %{girname}
%{_libdir}/girepository-1.0/Tepl-%{api}.typelib

%files -n %{libname}
%{_libdir}/libgedit-tepl-%{api}.so.%{major}

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/libgedit-tepl-%{api}/
%{_includedir}/libgedit-tepl-%{api}/tepl/
%{_libdir}/libgedit-tepl-%{api}.so
%{_libdir}/pkgconfig/libgedit-tepl-%{api}.pc
%{_datadir}/gir-1.0/Tepl-%{api}.gir
