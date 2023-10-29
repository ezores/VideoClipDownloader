---

# YouTube Video Clip Downloader

This script allows users to either provide a YouTube link or a path to a pre-downloaded video. The video will be split into smaller clips based on a specified length.

## Features

- Download videos from YouTube (ensure you comply with YouTube's terms of service).
- Split videos into smaller clips of a specified length.
- Save clips with a naming pattern that includes the date and title of the video.
- Save the video description as a text file (when downloading from YouTube).

## Requirements

- Python 3.x
- Libraries: `pytube`, `moviepy`, `youtube_dl`
  
  Install the required libraries using:

  ```
  pip install pytube moviepy youtube_dl
  ```

## Usage

1. Run the script:

   ```
   python main.py
   ```

2. You'll be prompted to:

   - Enter a path where the clips will be stored.
   - Specify the length of the clips in seconds.
   - Choose between providing a YouTube link or the path to a pre-downloaded video.

3. If you choose to provide a YouTube link:

   - If the video is age-restricted, you might be asked to provide login credentials.

4. The video will be split into smaller clips and saved to the specified path.

## Troubleshooting

- If you encounter issues related to downloading videos, ensure `youtube_dl` is updated:

  ```
  pip install youtube-dl --upgrade
  ```

- Filenames with special characters might sometimes cause issues. If you're providing a path to a pre-downloaded video and encountering an error, consider renaming the file to a simpler name without special characters.

## License

This script is provided "as is" without any warranties. Ensure you comply with YouTube's terms of service when downloading content. Always have the right to download and manipulate any content you work with.

---

You can save the above content in a file named `README.md` in the root directory of your project. If you plan to host the code on platforms like GitHub, this README will be rendered nicely and provide an overview and instructions for your project.
