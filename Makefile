NAME=$(shell grep Name: *.spec | sed 's/^[^:]*:[^a-zA-Z]*//')
VERSION=$(shell grep Version: *.spec | sed 's/^[^:]*:[^0-9]*//')
RELEASE=$(shell grep Release: *.spec | cut -d"%" -f1 | sed 's/^[^:]*:[^0-9]*//')
build=$(shell pwd)/build
DATE=$(shell date "+%a, %d %b %Y %T %z")
dist=$(shell rpm --eval '%dist')
python ?= python3

default:
	@echo "Nothing to do"

install:
	@echo installing ...
	@mkdir -p $(prefix)/usr/share/doc/$(NAME)-$(VERSION)
	@mkdir -p $(prefix)/usr/share/licenses/$(NAME)-$(VERSION)
	@mkdir -p $(prefix)/usr/share/man/man1
	$(python) setup.py install --root $(prefix)/
	@install -m 0644 man/$(NAME).1 $(prefix)/usr/share/man/man1
	@install -m 0644 README.md $(prefix)/usr/share/doc/$(NAME)-$(VERSION)/
	@install -m 0644 AUTHORS.md $(prefix)/usr/share/doc/$(NAME)-$(VERSION)/
	@install -m 0644 COPYRIGHT $(prefix)/usr/share/licenses/$(NAME)-$(VERSION)/
	@install -m 0644 LICENSE.txt $(prefix)/usr/share/licenses/$(NAME)-$(VERSION)/

dist:
	@mkdir -p $(build)/$(NAME)-$(VERSION)/
	rsync -HaS --exclude ".git" --exclude "$(build)" * $(build)/$(NAME)-$(VERSION)/
	cd $(build); tar --gzip -cf $(NAME)-$(VERSION).tar.gz $(NAME)-$(VERSION)/; cd -

sources: dist
	cp $(build)/$(NAME)-$(VERSION).tar.gz .

prepare: dist
	@mkdir -p $(build)/RPMS/noarch
	@mkdir -p $(build)/SRPMS/
	@mkdir -p $(build)/SPECS/
	@mkdir -p $(build)/SOURCES/
	@mkdir -p $(build)/BUILD/
	cp $(build)/$(NAME)-$(VERSION).tar.gz $(build)/SOURCES
	cp $(NAME).spec $(build)/SPECS

srpm: prepare
	rpmbuild -bs --define="dist $(dist)" --define="_topdir $(build)" $(build)/SPECS/$(NAME).spec

rpm: srpm
	rpmbuild --rebuild --define="dist $(dist)" --define="_topdir $(build)" $(build)/SRPMS/$(NAME)-$(VERSION)-$(RELEASE)$(dist).src.rpm

deb: dist
	cd $(build)/$(NAME)-$(VERSION); dpkg-buildpackage -us -uc; cd -

clean:
	@rm -f *~ bin/*~ etc/*~ data/*~
	@rm -rf build dist MANIFEST
	rm -f *~ $(NAME)-$(VERSION).tar.gz

.PHONY: dist srpm rpm sources deb clean
