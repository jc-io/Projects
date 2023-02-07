CC = clang

# You'll need to delete this line once you're done with your code.
#CFLAGS =
# You'll need to uncomment this line once you're done with your code.
CFLAGS = -Wall -Wpedantic -Werror -Wextra


all: pig_game

hw2: num_arrays.o pig_game.o
	$(CC) num_arrays.o pig_game.o -o pig_game

num_arrays.o: num_arrays.c num_arrays.h
	$(CC) $(CFLAGS) -c num_arrays.c

hw2.o: pig_game.c num_arrays.h
	$(CC) $(CFLAGS) -c pig_game.c

clean:
	rm -f pig_game pig_game.o num_arrays.o

format:
	clang-format -i -style=file *.{c,h}
