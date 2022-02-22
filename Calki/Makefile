CC := g++
CFLAGS := -Wall -g
LDFlAGS :=
LDLIBS :=

.PHONY: clean,all

all: Yehor_Savchenko_NUM8.x

%.x: %.o
	$(CC) $(LDFlAGS) -o $@ $^ $(LDLIBS)

%.o: %.cpp
	$(CC) $(CFLAGS) -c -o $@ $<

Yehor_Savchenko_NUM8.x: Yehor_Savchenko_NUM8.o
Yehor_Savchenko_NUM8.o: Yehor_Savchenko_NUM8.cpp

clean:
	$(RM) *.[ox]