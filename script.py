import yt_dlp
import os
import time

SONG_FILE = 'songs.txt'
OUTPUT_FOLDER = 'downloaded_songs'
AUTO_CONFIRM = True  # Set to False if you want manual confirmation

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

download_opts = {
    'format': 'bestaudio/best',
    'noplaylist': True,
    'quiet': False,
    'outtmpl': os.path.join(OUTPUT_FOLDER, '%(title)s.%(ext)s'),
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }
    ],
    'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe',
}

def load_song_titles(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def get_top_search_result(title):
    search_query = f"ytsearch1:{title}"
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        try:
            info = ydl.extract_info(search_query, download=False)
            if 'entries' in info and info['entries']:
                return info['entries'][0]
        except Exception as e:
            print(f"Search failed for '{title}': {e}")
    return None

def download_song(video_url):
    with yt_dlp.YoutubeDL(download_opts) as ydl:
        try:
            ydl.download([video_url])
            return True
        except Exception as e:
            print(f"Download failed: {e}")
            return False

if __name__ == "__main__":
    songs = load_song_titles(SONG_FILE)
    failed_songs = []

    for i, title in enumerate(songs, 1):
        print(f"\n[{i}/{len(songs)}] 🔍 Searching for: {title}")
        result = get_top_search_result(title)

        if result:
            video_title = result.get('title')
            uploader = result.get('uploader')
            duration = result.get('duration')
            video_url = result.get('webpage_url')

            print(f"🎵 Found: {video_title}")
            print(f"📺 Uploader: {uploader}")
            print(f"⏱ Duration: {duration // 60} min {duration % 60} sec")
            print(f"🔗 URL: {video_url}")

            if AUTO_CONFIRM:
                confirmed = True
            else:
                confirm = input("➡️  Download this? (y/n): ").strip().lower()
                confirmed = confirm == 'y'

            if confirmed:
                success = download_song(video_url)
                if success:
                    print("✅ Downloaded as MP3!")
                else:
                    failed_songs.append(title)
            else:
                print("❌ Skipped.")
        else:
            print("❗ No results found.")
            failed_songs.append(title)

        time.sleep(1)  # polite delay

    # Report summary
    if failed_songs:
        print("\n⚠️ Some songs failed to download:")
        for song in failed_songs:
            print(f" - {song}")
        with open('failed_downloads.txt', 'w', encoding='utf-8') as f:
            f.write('\n'.join(failed_songs))
    else:
        print("\n✅ All songs downloaded successfully!")

    print("\n🎉 Done!")
