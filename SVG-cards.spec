%define name SVG-cards
%define version 2.0
%define release %mkrel 7
 
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0-7mdv2011.0
+ Revision: 616453
- the mass rebuild of 2010.0 packages

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 2.0-6mdv2010.0
+ Revision: 434230
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 2.0-5mdv2009.0
+ Revision: 261275
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.0-4mdv2009.0
+ Revision: 253789
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.0-2mdv2008.1
+ Revision: 140863
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import SVG-cards


* Thu Jun 22 2006 Erwan Velu <erwan@seanodes.com> 2.0-2
- Rebuild

* Mon Dec 19 2005 Erwan Velu <erwan@seanodes.com> 2.0-1mdk
- 2.0

* Mon Jun 21 2004 Götz Waschk <waschk@linux-mandrake.com> 1.1-1mdk
- spec fixes
- add source URL
- New release 1.1

* Thu Jun 17 2004 Erwan Velu <erwan@mandrakesoft.com> 1.0-1mdk
- Initial mdk release
- Cleaning specfile
- Bzip2
* Tue Jun 15 2004 David Bellot <bellot@stat.berkeley.edu> 
  - First public release

