CC = g++
CC_OPT = -std=c++11 -O3 -g
CC_INC =
LD_LIB = -lgmpxx -pthread -lgmp
OUTPUT_DIR = ./bin
PROG = $(OUTPUT_DIR)/vdf
OBJ= $(OUTPUT_DIR)/proof.o $(OUTPUT_DIR)/wesolowski.o $(OUTPUT_DIR)/main.o

$(PROG): $(OBJ)
	$(CC) -o $@ $(OBJ) $(LD_LIB)
	ln -f -s $(PROG) .

clean:
	rm $(OBJ)
	rm $(PROG)

$(OUTPUT_DIR)/proof.o: proof.cpp proof.h
	$(CC) -c $(CC_OPT) $(CC_INC) -o $@ $<

$(OUTPUT_DIR)/wesolowski.o: wesolowski.cpp wesolowski.h proof.h
	$(CC) -c $(CC_OPT) $(CC_INC) -o $@ $<

$(OUTPUT_DIR)/main.o: main.cpp wesolowski.h proof.h
	$(CC) -c $(CC_OPT) $(CC_INC) -o $@ $<

