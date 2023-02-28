
.PHONY: test

BF=python3 bfi.py

all: test

test: quinepnm.b.test
	diff quinepnm.b quinepnm.b.test

quinepnm.b.test: quinepnm.pnm pnmocr.py
	python2 pnmocr.py < $< > $@

quinepnm.pnm: quinepnm.b
	$(BF) $< > $@

quinepnm.b: quinepnm.btail quinegen.py
	python2 quinegen.py < quinepnm.btail > $@

clean:
	-rm quinepnm.b quinepnm.pnm quinepnm.b.test
