# Video Player & Downloader Streamlit App

This Streamlit app allows users to download and watch videos from YouTube and Instagram with ease. Simply input the video link, and the app will provide you with an option to play and download the video in MP4 format.

## Features
- **YouTube Video Downloading**: Paste a YouTube link, and the app will fetch the best available video and audio quality, allowing you to download it in MP4 format.
- **Instagram Video Playback & Download**: Enter an Instagram video link, and the app will extract the video URL, allowing you to watch and download the video.
- **Streaming & Downloading**: Directly stream videos and download them to your device with a simple button click.

## Technologies Used
- **Streamlit**: A powerful tool to build and deploy interactive web applications.
- **yt-dlp**: A command-line tool to download videos from YouTube and other platforms.
- **Instaloader**: A Python library to download Instagram posts, stories, and videos.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/video-player-downloader.git
   cd video-player-downloader
   ```

2. **Install the required libraries**:
   ```bash
   pip install streamlit yt-dlp instaloader
   ```

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

4. **Enter the video link**: Once the app is running, enter a valid YouTube or Instagram video link in the provided text box.

5. **Play or Download the Video**: 
   - If it's a YouTube link, the app will stream the video and offer a download button.
   - If it's an Instagram link, the app will show the video and offer a download button.

## Example

- **YouTube Link**: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
- **Instagram Link**: `https://www.instagram.com/p/CGR6Y1kFzTk/`

Once you enter any of these links, you will be able to stream the video directly in the app and download it with a click.

## Troubleshooting
- **Video not playing**: Ensure that the link you have entered is valid and is a direct link to a video on YouTube or Instagram.
- **Download issues**: If the download button does not work, try re-entering the link or check for updates in the libraries used.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.