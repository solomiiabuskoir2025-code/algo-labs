import sys
import os


def find_max_chain(words_list):
    if not words_list:
        return 0

    dp = {}

    max_word_len = max(len(w) for w in words_list)
    buckets = [[] for _ in range(max_word_len + 1)]
    for w in words_list:
        buckets[len(w)].append(w)

    max_overall_chain = 0


    for length in range(1, max_word_len + 1):
        for word in buckets[length]:
            current_best = 1
            for i in range(len(word)):
                prev_word = word[:i] + word[i + 1:]
                if prev_word in dp:
                    current_best = max(current_best, dp[prev_word] + 1)

            dp[word] = current_best
            max_overall_chain = max(max_overall_chain, current_best)

    return max_overall_chain


def main():
    input_file = "wchain.in"
    output_file = "wchain.out"

    if os.path.exists(input_file):
        with open(input_file, "r") as f:
            lines = f.read().split()
            if not lines:
                return
            n = int(lines[0])
            words = lines[1: n + 1]

        result = find_max_chain(words)

        with open(output_file, "w") as f:
            f.write(str(result))
    else:
        print(f"Файл {input_file} не знайдено.:")
        input_data = sys.stdin.read().split()
        if input_data:
            n = int(input_data[0])
            print(find_max_chain(input_data[1: n + 1]))


if __name__ == "__main__":
    main()