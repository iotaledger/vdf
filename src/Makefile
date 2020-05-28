CC = g++
CC_OPT = -std=c++11 -O3
CC_INC =
LD_LIB = -lgmpxx -pthread -lgmp
OUTPUT_DIR = ./bin
PROG = $(OUTPUT_DIR)/vdf
OBJ= $(OUTPUT_DIR)/wesolowski.o $(OUTPUT_DIR)/proof.o $(OUTPUT_DIR)/main.o

$(PROG): $(OBJ)
	$(CC) -o $@ $(OBJ) $(LD_LIB)
	ln -f -s $(PROG) .

clean:
	rm $(OBJ)
	rm $(PROG)

$(OUTPUT_DIR)/wesolowski.o: wesolowski.cpp wesolowski.h /usr/local/include/gmp.h \
  proof.h /usr/local/include/gmpxx.h
	$(CC) -c $(CC_OPT) $(CC_INC) -o $@ $<

$(OUTPUT_DIR)/proof.o: proof.cpp proof.h /usr/local/include/gmp.h
	$(CC) -c $(CC_OPT) $(CC_INC) -o $@ $<

$(OUTPUT_DIR)/main.o: main.cpp /usr/local/include/gmp.h wesolowski.h proof.h
	$(CC) -c $(CC_OPT) $(CC_INC) -o $@ $<

