#
# test spec file for apache bigtop working group
#
Name:      test-hello-world
Version:   asdf
Release:   grrrr
BuildArch: noarch
Summary: mustbehere
License: GPL
Group:     Development/Libraries
Source: /home/dc/bigtop-0.5.0/helloworld.tar.gz
BuildRoot: /home/dc/bigtop-0.5.0/tempdir

%description 
hi all 

%prep
echo "target" %_target
echo %_target_alias
echo %_target_cpu
echo %_target_os
echo Building %{name}-%{version}-%{release}

%setup -c







