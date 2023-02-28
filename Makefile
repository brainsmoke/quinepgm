
TARGETS=quinepgm_101x1200.pgm quinepgm_100x1200.pgm quinepgm_101x1200.b quinepgm_100x1200.b

all: $(TARGETS)

%_bootstrap.b: %.btail quinegen.py
	python2 quinegen.py < $< > $@

quinepgm_101x1200_%.b: quinepgm_101x1200_%.pgm pgmocr.py
	python2 pgmocr.py 101 1200 < $< > $@

quinepgm_100x1200_%.b: quinepgm_100x1200_%.pgm pgmocr.py
	python2 pgmocr.py 100 1200 < $< > $@

%.c: %.b bftoc.py
	python2 bftoc.py < $< > $@

%.elf: %.c
	gcc -O2 -Wall -o $@ $<

%_a.pgm: %_bootstrap.elf
	./$< > $@

%_b.pgm: %_a.elf
	./$< > $@

%.b: %_a.b %_b.b
	diff -u $^ && cp $< $@

%.pgm: %_a.pgm %_b.pgm
	diff -u $^ && cp $< $@

clean:
	-rm $(TARGETS)
