from homework.src._internals.count_words import count_words
from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.split_into_words import split_into_words
from homework.src._internals.write_count_words import write_count_words


def main():

    all_lines = read_all_lines()
    all_lines = preprocess_lines(all_lines)
    words = split_into_words(all_lines)
    counter = count_words(words)
    write_count_words(counter)


if __name__ == "__main__":
    main()
