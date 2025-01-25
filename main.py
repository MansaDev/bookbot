def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        num_words = get_num_words(file_contents)
        num_characters = get_num_characters(file_contents)
        alpha_character = get_alpha(num_characters)
        sorted_alpha = descend_characters(alpha_character)
        print(f"{num_words} word found in the document\n")

        for alpha in sorted_alpha:
            print(f"The '{alpha["character"]}' character was found {alpha} times")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    num_characters = {}
    for c in text:
        lowered_c = c.lower()
        if lowered_c in num_characters:
            num_characters[lowered_c] += 1
        else:
            num_characters[lowered_c] = 1

    return num_characters

def get_alpha(characters):
    alpha_characters = []
    for c in characters:
        if c.isalpha():
            c_dict = {"character": c, "num": characters[c]}
            alpha_characters.append(c_dict)

    return alpha_characters



def descend_characters(characters):
    characters.sort(reverse=True, key=lambda x: x["num"])
    return characters
main()
