def main():
    import json
    from scrape import scrape_webpage
    from parse import parse_swcodes
    from verify import check_duplication
    from notification import notify_new_codes, notify_none_found
    
    with open("assets\\config.json") as f:
        config = json.load(f)

    url = "https://swq.jp/l/en-US/"

    html = scrape_webpage(url)
    eligable_codes = parse_swcodes(html)

    new_codes = check_duplication(eligable_codes)
    print(new_codes)

    if not new_codes:
        if config["send-notification-if-no-new-code"] == True:
            notify_none_found()
    else:
        notify_new_codes(new_codes)

if __name__ == "__main__":
    main()