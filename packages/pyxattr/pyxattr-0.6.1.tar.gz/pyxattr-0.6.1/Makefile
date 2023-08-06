SPHINXOPTS    = -W
SPHINXBUILD   = sphinx-build
DOCDIR        = doc
DOCHTML       = $(DOCDIR)/html
DOCTREES      = $(DOCDIR)/doctrees
ALLSPHINXOPTS = -d $(DOCTREES) $(SPHINXOPTS) $(DOCDIR)

MODNAME = xattr.so
RSTFILES = doc/index.rst doc/module.rst NEWS README.rst doc/conf.py
PYVERS = 2.4 2.5 2.6 2.7 3.0 3.1 3.2 3.3 3.4 3.5 3.6 3.7
REPS = 5

all: doc test

$(MODNAME): xattr.c
	./setup.py build_ext --inplace

$(DOCHTML)/index.html: $(MODNAME) $(RSTFILES)
	$(SPHINXBUILD) -b html $(ALLSPHINXOPTS) $(DOCHTML)
	touch $@

doc: $(DOCHTML)/index.html

dist:
	fakeroot ./setup.py sdist

test:
	@for ver in $(PYVERS); do \
	  for flavour in "" "-dbg"; do \
	    if type python$$ver$$flavour >/dev/null; then \
	      echo Testing with python$$ver$$flavour; \
	      python$$ver$$flavour ./setup.py test -q; \
	    fi; \
	  done; \
	done;
	@if type pypy >/dev/null; then \
	  echo Testing with pypy; \
	  pypy ./setup.py test -q; \
	fi

benchmark: $(MODNAME)
	@set -e; \
	TESTFILE=`mktemp`;\
	trap 'rm $$TESTFILE' EXIT; \
	for ver in $(PYVERS) ; do \
	    if type python$$ver >/dev/null; then \
	      echo Benchmarking with python$$ver; \
	      python$$ver ./setup.py build -q; \
	      echo "  - set (with override)"; \
	      python$$ver -m timeit -r $(REPS) -s 'import xattr' "xattr.set('$$TESTFILE', 'user.comment', 'hello')"; \
	      echo "  - list"; \
	      python$$ver -m timeit -r $(REPS) -s 'import xattr' "xattr.list('$$TESTFILE')"; \
	      echo "  - get"; \
	      python$$ver -m timeit -r $(REPS) -s 'import xattr' "xattr.get('$$TESTFILE', 'user.comment')"; \
	      echo "  - set + remove"; \
	      python$$ver -m timeit -r $(REPS) -s 'import xattr' "xattr.set('$$TESTFILE', 'user.comment', 'hello'); xattr.remove('$$TESTFILE', 'user.comment')"; \
	    fi; \
	done;

coverage:
	$(MAKE) clean
	$(MAKE) test CFLAGS="-coverage"
	lcov --capture --directory . --output-file coverage.info
	genhtml coverage.info --output-directory out

clean:
	rm -rf $(DOCHTML) $(DOCTREES)
	rm -f $(MODNAME)
	rm -f *.so
	rm -rf build

.PHONY: doc test clean dist coverage
