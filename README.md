## Filter Notion Database Callouts by a Tag Name

This is a Python script that searches through all `.md` files in a directory and extracts all callouts (use for comments) that match a specified `tag_name`. The comments are then saved to a new file with the format `'Comments about [tag_name] [current date].md`.

### Usage
To use the script, simply run the main.py file and pass in the desired `tag_name` as a parameter to the `filter_notion_db_download` function. 

For example:


`filter_notion_db_download('调查研究')`

This will search for all .md files in the current directory that have the tag 调查研究 and extract any callouts found in those files. The callouts will then be saved to a new file named `Comments about 调查研究 [current date].md`.