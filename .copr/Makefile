.PHONY: srpm
srpm:
	dnf -y install rpm-build rpmdevtools
	spectool -g -R kakoune.spec
	rpmbuild -bs kakoune.spec
