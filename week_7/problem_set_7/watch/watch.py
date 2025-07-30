# Week 7: Problem 2
# Take in a HTML iframe tag used ofr embeding YouTube videos, slice the src part
# give output of a simple youtube url
import re
import sys


def main():
    html = input("HTML: ").strip()
    print(parse(html))


def parse(s):
    pattern = r"^<iframe(?: width=\"\d{1,3}\")?(?: height=\"\d{1,3}\")? src=\"(?P<url>https?://(?:www\.)?youtube\.com/embed/.+)\"(?: title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard\-write; encrypted\-media; gyroscope; picture\-in\-picture\" allowfullscreen)?></iframe>$"

    matches = re.search(pattern, s, re.IGNORECASE)

    try:
        url = matches.group("url")

        if "youtube" in url:
            url_pattern = r"^https?://(?:www\.)?youtube\.com/embed/(?P<video_link>.+)$"

            url_matches = re.search(url_pattern, url, re.IGNORECASE)

            return f"https://youtu.be/{url_matches.group("video_link")}"
        else:
            return None
    except (ValueError, AttributeError):
        return None

if __name__ == "__main__":
    main()
