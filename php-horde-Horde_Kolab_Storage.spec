# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Kolab_Storage
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - A package for handling Kolab data stored on an IMAP server
Name:		php-horde-Horde_Kolab_Storage
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	f0ec6057e6262b371b63c2b7ea51af2b
URL:		https://github.com/horde/horde/tree/master/framework/Kolab_Storage/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Cache < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Kolab_Format < 2.0.0
Requires:	php-horde-Horde_Mime < 2.0.0
Requires:	php-horde-Horde_Support < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear
Suggests:	php-horde-Horde_Imap_Client
Suggests:	php-imap
Suggests:	php-pear-HTTP_Request
Suggests:	php-pear-Net_IMAP
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(Horde/Imap/Client.*) pear(HTTP/Request.*) pear(Net/IMAP.*)

%description
Storing user data in an IMAP account belonging to the user is one of
the Kolab server core concepts. This package provides all the
necessary means to deal with this type of data storage effectively.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%doc docs/Horde_Kolab_Storage/*
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Kolab/Storage.php
%{php_pear_dir}/Horde/Kolab/Storage
%{php_pear_dir}/data/Horde_Kolab_Storage
