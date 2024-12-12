import streamlit as st
from yt_dlp import YoutubeDL
import instaloader

def download_youtube_video_with_ytdlp(link):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'noplaylist': True,
        'outtmpl': '-',  # Output as bytes
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        video_title = info_dict.get('title', 'video')
        with ydl:
            video_bytes = ydl.download([link])
        return video_title, video_bytes

def get_instagram_video(link):
    loader = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(loader.context, link.split("/")[-2])
    video_url = post.video_url
    return video_url

st.title("Video Player & Downloader")
st.write("Input a  Instagram link to play or download the video.")

video_link = st.text_input("Enter video link:")

if video_link:
    if "youtube.com" in video_link or "youtu.be" in video_link:
        try:
            video_title, video_bytes = download_youtube_video_with_ytdlp(video_link)
            st.video(video_link)

            st.download_button(
                label="Download YouTube Video",
                data=video_bytes,
                file_name=f"{video_title}.mp4",
                mime="video/mp4"
            )
        except Exception as e:
            st.error(f"Failed to process YouTube video: {e}")

    elif "instagram.com" in video_link:
        try:
            video_url = get_instagram_video(video_link)
            st.video(video_url)

            st.download_button(
                label="Download Instagram Video",
                data=video_url,
                file_name="instagram_video.mp4",
                mime="video/mp4"
            )
        except Exception as e:
            st.error(f"Failed to process Instagram video: {e}")

    else:
        st.warning("Please enter a valid  Instagram video link.")