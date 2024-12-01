def check_duplication(codes):
    new_codes = []
    sent_codes_file = "assets\\sent_codes.txt"
    with open(sent_codes_file, "r") as f:
        sent_codes = f.readlines()

    i = 0
    for code in sent_codes:
        sent_codes[i] = code[:-1]
        i += 1

    for code in codes:
        if code in sent_codes:
            continue
        else:
            with open(sent_codes_file, "a") as f:
                f.write(code + "\n")
            new_codes.append(code)

    return new_codes

if __name__ == "__main__":
    check_duplication(["test", "test2"])