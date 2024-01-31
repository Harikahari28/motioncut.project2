def word_count(sentence):
    if not sentence:
        return 0
    words = sentence.split()
    return len(words)

def main():
    print("Word Counter Program")
    print("--------------------")
    user_input = input("Enter a sentence or paragraph: ")
    count = word_count(user_input)
    print(f"\nWord Count: {count}")

if __name__ == "__main__":
    main()
