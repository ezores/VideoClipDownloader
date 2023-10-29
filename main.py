import os
import datetime
from pytube import YouTube, exceptions
from moviepy.editor import VideoFileClip


def get_user_input():
    choice = input(
        "Choose an option:\n1. Provide a YouTube link\n2. Provide a path to a pre-downloaded video\nEnter 1 or 2: ")

    if choice == "1":
        link = input("Please enter the desired YouTube link to download: ")
        return "link", link
    elif choice == "2":
        video_path = input("Please enter the path to the pre-downloaded video: ").strip('"')  # Strip double quotes
        return "file", video_path
    else:
        print("Invalid choice. Exiting.")
        exit()


def download_video_and_description(link, download_path):
    yt = YouTube(link)

    def on_progress(stream, _chunk, bytes_remaining):
        percentage = (1 - bytes_remaining / stream.filesize)
        display_progress_bar(percentage)

    yt.register_on_progress_callback(on_progress)

    stream = yt.streams.get_highest_resolution()
    title = yt.title
    description = yt.description

    video_filename = f"{title}.mp4"
    description_filename = f"{title}.txt"

    video_path = os.path.join(download_path, video_filename)
    description_path = os.path.join(download_path, description_filename)

    print(f"Downloading video '{title}'...")
    stream.download(output_path=download_path, filename=video_filename)
    print("\nDownload completed!")

    with open(description_path, 'w', encoding='utf-8') as f:
        f.write(description)
    print(f"Description saved to {description_path}")

    return title, video_path


def split_video(title, video_path, download_path, clip_length):
    video = VideoFileClip(video_path)
    duration = video.duration

    start_time = 0
    clip_counter = 1
    date_str = datetime.datetime.now().strftime('%Y%m%d')

    while start_time < duration:
        end_time = min(start_time + clip_length, duration)
        clip_filename = f"{date_str}_{title}_clip{clip_counter}.mp4"
        clip_path = os.path.join(download_path, clip_filename)

        clip = video.subclip(start_time, end_time)
        clip.write_videofile(clip_path, codec='libx264')

        print(f"Clip saved to {clip_path}")

        start_time += clip_length
        clip_counter += 1

    print("All clips saved successfully.")


def display_progress_bar(percentage):
    length = 50  # number of blocks in progress bar
    block = int(round(length * percentage))
    progress = "|" + "=" * block + ">" + "-" * (length - block) + "|"
    print(f"\r{progress} {percentage * 100:.2f}%", end="")


def main():
    download_path = input("Please enter the desired path to download and store the clips: ")
    clip_length = int(input("Please enter the length of the clips in seconds: "))

    option_type, value = get_user_input()

    if option_type == "link":
        title, video_path = download_video_and_description(value, download_path)
    elif option_type == "file":
        video_path = value
        title = os.path.basename(video_path).split(".")[0]  # extracting title from filename
    else:
        print("Invalid option. Exiting.")
        return

    split_video(title, video_path, download_path, clip_length)


if __name__ == "__main__":
    main()
