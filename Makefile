export REPO = csc220
SUBDIRS = 00-lab 01-lab 02-lab 03-lab 04-lab 05-lab 06-lab 08-lab 10-lab 12-lab 15-lab 17-lab 19-lab 20-lab 21-lab 22-lab

all: $(SUBDIRS)

.PHONY: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $@

clean:
	for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean; \
	done
