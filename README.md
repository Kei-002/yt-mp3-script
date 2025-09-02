# 🎵 YouTube Song Downloader

This script allows you to **search and download songs from YouTube** as MP3 files using [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [FFmpeg](https://ffmpeg.org/).  
It reads a list of song titles from a text file, searches for the best YouTube match, and downloads them automatically.

---

## 📂 Project Structure

```
.
├── songs.txt              # List of songs to download (one per line)
├── downloaded_songs/      # Folder where MP3 files will be saved
├── failed_downloads.txt   # (Generated) List of songs that failed to download
├── main.py                # The downloader script
```

---

## ⚙️ Requirements

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)  
- [FFmpeg](https://ffmpeg.org/) (must be installed and accessible)  

Install requirements:

```bash
pip install yt-dlp
```

Download FFmpeg and add it to your system path, or update the script with your custom FFmpeg path:
```python
'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe'
```

---

## 📝 Usage

1. **Add songs to `songs.txt`**  
   Each line should contain the name of a song or search query, for example:

   ```
   Bohemian Rhapsody Queen
   Billie Jean Michael Jackson
   Shape of You Ed Sheeran
   ```

2. **Run the script**  

   ```bash
   python main.py
   ```

3. The script will:
   - Search for each song on YouTube
   - Show details (title, uploader, duration, URL)
   - Download as **MP3** (192 kbps) into `downloaded_songs/`

---

## 🔧 Settings

- **Auto-confirm downloads**  
  The script is set to download automatically:
  ```python
  AUTO_CONFIRM = True
  ```
  If you want manual confirmation before each download, set it to `False`.

- **Output folder**  
  All MP3s are saved in:
  ```python
  OUTPUT_FOLDER = 'downloaded_songs'
  ```

---

## ✅ Features

- Bulk download songs from `songs.txt`
- Skips empty lines automatically
- Shows search result details (title, uploader, duration)
- Handles failed downloads and logs them to `failed_downloads.txt`
- Converts to high-quality MP3 (192 kbps)

---

## ⚠️ Notes

- This script is for **personal use only**. Please respect YouTube’s Terms of Service and copyright laws.  
- Long song lists may take time due to polite delays (`time.sleep(1)` between searches).

---

## 🎉 Example Output

```
[1/3] 🔍 Searching for: Bohemian Rhapsody Queen
🎵 Found: Queen – Bohemian Rhapsody (Official Video Remastered)
📺 Uploader: Queen Official
⏱ Duration: 5 min 55 sec
🔗 URL: https://youtube.com/...
✅ Downloaded as MP3!

[2/3] 🔍 Searching for: Billie Jean Michael Jackson
🎵 Found: Michael Jackson – Billie Jean (Official Video)
📺 Uploader: michaeljacksonVEVO
⏱ Duration: 4 min 54 sec
🔗 URL: https://youtube.com/...
✅ Downloaded as MP3!
```

---

## 📜 License

This project is provided **as-is** for educational purposes.  
Use responsibly and in compliance with YouTube’s policies.
