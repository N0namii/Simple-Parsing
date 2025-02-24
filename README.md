### Code Description

This Python script is designed to parse data from a web page, such as Hacker News, and save the results to a text file. The script uses the `requests` library to perform HTTP requests and `BeautifulSoup` from the `bs4` library to analyze HTML content.

#### Key Features:

1. **URL Input**: The user inputs the URL of the page from which data needs to be collected.
2. **Page Request**: The script sends a GET request to the specified URL and checks if the request is successful (status code 200).
3. **Data Parsing**:
   - **Post Titles**: Extracts all elements with the class `titleline`, which contain post titles.
   - **Scores**: Extracts elements with the class `score`, which contain the number of points (likes) a post has.
   - **Additional Information**: Extracts elements with the class `subtext`, which contain information about the user who created the post and the number of comments.
4. **Post Uniqueness**: The script ensures posts are unique by checking their title and link to avoid duplicates.
5. **Saving Results**: All data is saved to a text file, `output.txt`, in a readable format.
6. **Output**: The script prints a success message in the console, along with the number of unique posts found.

#### Example Usage:

1. Run the script.
2. Enter the URL of the page, for example, `https://news.ycombinator.com/`.
3. The script will collect the data and save it to `output.txt`.

#### Dependencies:

- `requests`: For making HTTP requests.
- `bs4` (BeautifulSoup): For parsing HTML content.

#### Installing Dependencies:

```bash
pip install requests beautifulsoup4
```

#### Example Content of `output.txt`:

```
Parsing Results
==================================================

Post #1
  Title: Example Post Title
  Link: https://example.com
  Points: 123 points
  User: example_user
  Comments: 45 comments
--------------------------------------------------

Post #2
  Title: Another Example Post
  Link: https://anotherexample.com
  Points: 67 points
  User: another_user
  Comments: 12 comments
--------------------------------------------------
```

#### Notes:

- The script assumes that the HTML structure of the page matches the expected format (e.g., classes like `titleline`, `score`, and `subtext`). If the page structure changes, the script may require adjustments.
- For use with other websites, the script may need to be adapted to their specific HTML structure.

This script can be useful for automating data collection from web pages, analyzing content, and saving results for further use.
