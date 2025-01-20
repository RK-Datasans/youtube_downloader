# YouTube Video Downloader

A Python script to download videos from YouTube using URLs stored in an Excel file. The script also tracks download statuses and updates the Excel file accordingly.

## Features

- Downloads YouTube videos in the highest resolution using the `pytube` library.
- Reads video URLs from an Excel file.
- Updates the Excel file with the download status (`Done` or error messages).
- Saves downloaded videos in a `youtube-download` directory, creating it automatically if it doesn't exist.

## Requirements

- Python 3.6+
- Libraries: `pytube`, `pandas`, `openpyxl`

Install the required libraries using:

```bash
pip install pytube pandas openpyxl
```

## Setup and Usage

1. **Prepare the Excel File:**
   - Create an Excel file (e.g., `video_urls.xlsx`) with the following structure:

     ```
     URL                               | Status
     ----------------------------------|-------
     https://www.youtube.com/watch?v=...| 
     https://www.youtube.com/watch?v=...| 
     ```
   - The `Status` column is optional. If not present, the script will create it.

2. **Place the Excel File:**
   - Save the Excel file in the same directory as the script.

3. **Run the Script:**

   ```bash
   python youtube_downloader.py
   ```

4. **Check the Output:**
   - Downloaded videos will be saved in the `youtube-download` directory.
   - The `Status` column in the Excel file will be updated to `Done` for successful downloads or will display error messages if a download fails.

## File Structure

```
.
├── youtube_downloader.py   # The main script file
├── video_urls.xlsx         # Excel file with video URLs
├── youtube-download/       # Directory for downloaded videos (auto-created)
└── README.md               # This readme file
```

## Error Handling

- If a video fails to download, the script logs the error message in the `Status` column of the Excel file.
- Common issues include invalid URLs, unavailable videos, or network errors.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [pytube](https://github.com/pytube/pytube) for providing a simple way to interact with YouTube.
- [pandas](https://pandas.pydata.org/) for powerful data manipulation capabilities.
