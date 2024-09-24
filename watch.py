import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'src="(https?://(?:www\.)?youtube\.com/embed/([^"]+))"'  # Capture video ID

    if search := re.search(pattern, s):
        video_id = search.group(2)  # Extract video ID
        shortened_url = f"https://youtu.be/{video_id}"  # Construct shortened URL
        return shortened_url
    else:
        return None

if __name__ == "__main__":
    main()
