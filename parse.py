def parse_swcodes(html):
    from bs4 import BeautifulSoup

    # initiates bs4 to parse the html
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find_all("tr")
    eligable_codes = []
    for row in table:
        if "fa-check" in str(row):
            verified_code = row.text[1:]
            code = ""
            for letter in verified_code:
                if letter != " ":
                    code += letter
                if letter == " ":
                    break
            eligable_codes.append(code)

    return eligable_codes

if __name__ == "__main__":
    parse_swcodes("test")