%define oname ZenTest

Summary:    ZenTest provides 4 different tools: zentest, unit_diff, autotest, and multiruby
Name:       rubygem-%{oname}
Version:    4.4.0
Release:    %mkrel 1
Group:      Development/Ruby
License:    MIT
URL:        http://www.zenspider.com/ZSS/Products/ZenTest/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(rubyforge) >= 2.0.4
Requires:   rubygem(minitest) >= 1.7.0
Requires:   rubygem(hoe) >= 2.6.1
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
ZenTest provides 4 different tools: zentest, unit_diff, autotest, and
multiruby.
ZenTest scans your target and unit-test code and writes your missing
code based on simple naming rules, enabling XP at a much quicker
pace. ZenTest only works with Ruby and Test::Unit. Nobody uses this
tool anymore but it is the package namesake, so it stays.
unit_diff is a command-line filter to diff expected results from
actual results and allow you to quickly see exactly what is wrong.
autotest is a continous testing facility meant to be used during
development. As soon as you save a file, autotest will run the
corresponding dependent tests.
multiruby runs anything you want on multiple versions of ruby. Great
for compatibility checking! Use multiruby_setup to manage your
installed versions.


%prep

%build

%install
rm -rf %buildroot
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod 755
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/test -type f | xargs chmod 755
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/lib -type f | xargs chmod 644
ruby -pi -e 'sub(/\/usr\/local\/bin\/ruby/, "/usr/bin/env ruby")' %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/{bin,test}/*

%clean
rm -rf %buildroot

%files
%defattr(-, root, root, -)
%{_bindir}/autotest
%{_bindir}/multigem
%{_bindir}/multiruby
%{_bindir}/multiruby_setup
%{_bindir}/unit_diff
%{_bindir}/zentest
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.autotest
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%{ruby_gemdir}/gems/%{oname}-%{version}/example*.rb
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Manifest.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/articles/*
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/example.txt
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
