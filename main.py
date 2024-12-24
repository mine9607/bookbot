
def count_words(text):
  words = text.split()

  return (len(words))

def count_chars(text):
  char_dict = {}
  text_to_lower = text.lower()
  for char in text_to_lower:
    if char in char_dict:
      char_dict[char]+=1
    else:
      char_dict[char] = 1
  return (char_dict)

def sort_on(dict):
  return dict["num"]

def generate_book_report(text):
  total_words = count_words(text)
  char_dict = count_chars(text)

  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{total_words} words found in the document\n\n")
  for char in char_dict:
    print(f"The '{char}' character was found {char_dict[char]} times")
  print("--- End report ---")


def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
  
  #print(file_contents)
  #count_words(file_contents)
  #count_chars(file_contents)
  generate_book_report(file_contents)


main()