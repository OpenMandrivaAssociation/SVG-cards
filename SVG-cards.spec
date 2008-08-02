%define name SVG-cards
%define version 2.0
%define release %mkrel 5
 
Summary: A set of playing cards in SVG
Name: %name
Version: %version
Release: %release
Group: Games/Cards
License: LGPL
Url:	 http://david.bellot.free.fr/svg-cards/files
Source: http://david.bellot.free.fr/svg-cards/files/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
Buildarch: noarch

%description
This is a set of playing cards made in pure SVG with all kings, 
queens, jacks, numbers, jokers and backs of cards.
This set of SVG files is intended to be used in games, figures, 
illustrations and web sites.
The kings, queens and jacks are based on the french representation, 
because I find them beautiful.

%prep
%setup -q

%build
echo "Ready to use"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%name
install *.svg $RPM_BUILD_ROOT/%{_datadir}/%name

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS Changelog NEWS README COPYING
%_datadir/SVG-cards

