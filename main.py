import os
import re
from datetime import date


def filter_notion_db_download(tag_name):

    # Define the regular expression pattern to match the <aside> tags and extract their contents
    aside_pattern = re.compile(r"<aside>\s*(.*?)\s*</aside>", re.DOTALL)

    # Initialize an empty list to store the comments
    all_comments = []

    folder_name = next(filter(lambda x: "Reading" in x, os.listdir()), "")

    # Loop through all the files in the current directory that end in ".md"
    for filename in os.listdir(folder_name):
        if filename.endswith(".md"):
            # Read the contents of the file into a string
            with open(os.path.join(folder_name, filename), "r") as f:
                contents = f.read()

            # Check if the file has the tag we're looking for
                # Extract all the tags from the file
            tags = re.findall(r"^Tags:\s*(.+)$", contents, re.MULTILINE | re.UNICODE)
           # tags = re.findall(r"^Tags:\s*(.+)$", contents, re.MULTILINE)
            tags = [tag.strip().lower() for tag in ",".join(tags).split(",")]

            # Check if the file has the tag we're looking for
            if tag_name.lower() not in tags:
                continue

            # Extract the title and URL from the file
            title = re.findall(r"^# (.+)$", contents, re.MULTILINE)[0]

            url = re.findall(r"^URL: (.+)$", contents, re.MULTILINE)[0]

            # Extract all the comments from the file
            comments = []
            for match in aside_pattern.finditer(contents):
                new_comment = match.group(1).replace('🍀', '').replace('*', '').replace('👉🏻', '').strip()
                new_comment = re.sub(r"<img[^>]*>", "",  new_comment)
                comments.append(new_comment )


            # If there are no comments, skip this file
            if not comments:
                continue

            base_name, ext = os.path.splitext(filename)
            match = re.search(r"\b([0-9a-fA-F]+)\b", base_name)
            if match:
                page_number = match.group(1)

            # Add the comments to the list of all comments
            all_comments.append((title, url, comments))

    # Create the output file
    with open(f"Comments about {tag_name} {date.today()}.md", "w") as f:
        # Loop through all the articles with comments
        for title, url, comments in all_comments:
            f.write(f"### [{title}](https://www.notion.so/adamni/{page_number})\n\n")
            f.write(f"[{url}]({url})\n\n")

            for comment in comments:
                f.write(f"{comment}\n\n")

            f.write("\n\n")


filter_notion_db_download('调查研究')
