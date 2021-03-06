# Spec file for package faba-colors
#
# Copyright (c) 2014 Sam Hewitt <hewittsamuel@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#


Name:		faba-colors
Version:	2.0
Release:	0

Summary:	Faba Colors Icon theme
Group:		System/GUI/Other
License:    LGPL-3.0+ or CC-BY-SA-3.0

Group:      System/GUI/GNOME
Url:        http://www.mokaproject.com/faba-icon-theme
Source0:	%{name}-%{version}.tar.gz

Requires:	hicolor-icon-theme, gnome-icon-theme
BuildArch:	noarch


%description
Faba Colors Icon Theme

%prep
%setup -q

# Delete dead icon symlinks
find -L . -type l -delete

%build
%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a Faba-Ceru/ $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a Faba-Lutu/ $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a Faba-Roja/ $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a Faba-Verd/ $RPM_BUILD_ROOT%{_datadir}/icons/
cp -a Faba-Viol/ $RPM_BUILD_ROOT%{_datadir}/icons/

%files
%doc {AUTHORS,LICENSE}
%{_datadir}/icons/Faba-Ceru/
%{_datadir}/icons/Faba-Lutu/
%{_datadir}/icons/Faba-Roja/
%{_datadir}/icons/Faba-Verd/
%{_datadir}/icons/Faba-Viol/
