Summary:	Options and Parameter parsing Tool
Summary(pl):	Narzêdzie do analizowania opcji oraz parametrów
Name:		opt
Version:	3.19
Release:	1
License:	GPL
Source0:	http://nis-www.lanl.gov/~jt/Software/opt/%{name}-%{version}.tar.gz
# Source0-md5:	587171c4e15a40adde8aa1b3d77328e9
Group:		Development/Libraries
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
opt is a library of subroutines for communicating options and
parameter values to a C program via the command line, parameter files,
environment variables, or a rudimentary builtin interactive menu. It
is similar in aims to the standard getopt() utility, but it has a
different (I would say better) interface to the programmer, and a few
more bells and whistles for the end-users of programs that employ opt.

%description -l pl
opt jest bibliotek± zawieraj±c± funkcje pozwalaj±ce analizowaæ opcje i
parametry w programie C przesy³ane przez liniê poleceñ, pliki z
parametrami, zmienne ¶rodowiska lub wbudowane interaktywne menu. opt
jest podobny do tego do czego d±¿y standardowa funkcja getopt() ale ma
inny (lepszy) interfejs programisty oraz wiêcej mo¿liwo¶ci.

%prep
%setup -q

%build
%configure2_13 \
	--disable-test \
	--with-readline

%{__make} \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%{_includedir}/*.h
%{_libdir}/*.a
%{_infodir}/opt.info*
