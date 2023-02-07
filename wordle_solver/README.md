# DESIGN PROCESS

## Description of search\_util.c

### Total of 7 functions

1. int score\_letter()
2. int score\_word()
3. char \*get\_guess()                    //given
4. size\_t filter\_vocabulary\_gray()
5. size\_t filter\_vocabulary\_yellow()
6. size\_t filter\_vocabulary\_green()
7. void free\_vocabulary()                //given

### Steps

1. In the solver.c, find the order the functions were called in solver.c
- get\_guess()
  - score\_letter()
  - score\_word()
- filter\_vocabulary\_gray()
- filter\_vocabulary\_yellow()
- filter\_vocabulary\_green()

2. Use this order to program the functions.

3. score\_letter() and score\_word()
- This fuction takes a dynamic array (vocabulary list) that contains possible words that are the length of 5 and the number of words (num\_words) from solver.c
- This function will then go into the get\_guess() on search\_util.c
- in a for loop in the range of 26, it will create an array of integers that is equal to the return value of score\_letter()

- score\_letter() takes in 3 inputs, a letter, the vocabulary list, and num\_words
- in a for loop in the range of 26, if the vocabulary[i] is not set to NULL, then it will check if the letter is contained in vocabulary[i], from there, it will increment a counter, once the loop is done, it will return the counter

- back in get\_guess(), in a for loop in the range of num\_words, if vocabulary[i] is not NULL, it will go to score\_word()

- score\_word() takes 2 inputs, vocabulary[i] and the letter\_scores array
- This function will then take all the integers in letter\_scores using a for loop adds all the integers if ('a' + i) is in the word

```
def score\_letter()
  let_score = 0
  for i in range(26)
    if vocabulary[i] != NULL
      if letter in vocabulary[i]
        let_score++
  return let_score

def score\_word()
  word_sum = 0
  for i in range(26)
    if ('a' + i) in vocabulary[i]
      word_sum = word_sum + letter_scores[i]
  return word_sum

```

4. next are functions filter\_vocabulary\_gray(), filter\_vocabulary\_yellow(), filter\_vocabulary\_green()
- all three have similar syntax

- filter\_vocabulary\_gray() has 3 inputs: a letter, the vocabulary list, and num\_words
- filter\_vocabulary\_yellow() and filter\_vocabulary\_green have 4 inputs: a letter, the index of the word (position) the vocabulary list, and num\_words

- all three have the same format
  - a filtered words counter
  - for loop in the range of num\_words
  - an if statement checking if the word is not NULL
  - an if statement with unique statements
    - filter\_vocabulary\_gray() checks if the letter is in a word
    - filter\_vocabulary\_yellow() checks if the letter is not in the word or if the specific position is the letter
    - filter\_vocabulary\_green() checks if the leter is not in the word or if the specific postion is not the letter
  - all free the word from the vocabulary array
  - sets the word to NULL
  - increments the filtered words counter
  - finally returns the counter

```
def filter_vocabulary_gray(letter, vocabulary, num_words)
  filtered = 0
  for i in range(num_words)
    if vocabulary[i] != NULL
      if letter in vocabulary[i]
        free(vocabulary[i])
        vocabulary[i] = NULL
        filtered++
  return filtered

def filter_vocabulary_yellow(letter, position, vocabulary, num_words)
  filtered = 0
  for i in range(num_words)
    if vocabulary[i] != NULL
      if letter not in vocabulary[i] or vocabulary[i][position] is letter
        free(vocabulary[i])
        vocabulary[i] = NULL
        filtered++
  return filtered
  
def filter_vocabulary_green(letter, position, vocabulary, num_words) 
  filtered = 0
  for i in range(num_words)
    if vocabulary[i] != NULL
      if letter not in vocabulary[i] or vocabulary[i][position] is not letter
        free(vocabulary[i])
        vocabulary[i] = NULL
        filtered++
  return filtered

```
5. Once the word has either been found or dicovered that it was not in the vocabulary list then it will free the list.

6. The program finishes running.


