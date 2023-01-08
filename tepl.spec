%global api	6
%global major	1
%define libname %mklibname tepl %{api} %{major}
%define girname	%mklibname tepl-gir %{api}
%define devname %mklibname -d tepl %{api}

%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:           tepl
Version:        6.4.0
Release:        1
Summary:        Text editor product line
Group:		System/Libraries

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Tepl
Source0:        https://download.gnome.org/sources/tepl/%{url_ver}/tepl-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(amtk-5)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uchardet)

%description
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs. Tepl is the acronym for “Text editor product line”.

%package        -n %{libname}
Summary:        Libraries for %{name}
Requires:	%{name} >= %{version}-%{release}
Obsoletes:	%{_lib}tepl0 < 4.2.0-2

%description    -n %{libname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for Tepl
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Conflicts:	%{name} < 4.2.0-2

%description -n %{girname}
GObject Introspection interface description for Tepl.

%package        -n %{devname}
Summary:        Development files for %{name}
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}tepl-devel < 4.2.0-2

%description    -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%meson  -Dgtk_doc=true
%meson_build

%install
%meson_install

find %{buildroot} -name '*.la' -delete

%find_lang tepl-%{api}

%files -f tepl-%{api}.lang
%doc NEWS README.md

%files -n %{girname}
%{_libdir}/girepository-1.0/Tepl-%{api}.typelib

%files -n %{libname}
%{_libdir}/libtepl-%{api}.so.%{major}*

%files -n %{devname}
%{_datadir}/gtk-doc/html/tepl-%{api}/*
%{_includedir}/tepl-%{api}/
%{_libdir}/libtepl-%{api}.so
%{_libdir}/pkgconfig/tepl-%{api}.pc
%{_datadir}/gir-1.0/Tepl-%{api}.gir
