import wikipedia
import requests

# 🔹 Replace with your real YouTube Data API key from https://console.cloud.google.com/
YOUTUBE_API_KEY = "AIzaSyDgxtXYAe3qwdfjZWHl5SNynyMe2cLy9r8"

def get_biography(person):
    data = {}

    try:
        # 🧾 Basic Wikipedia info
        summary = wikipedia.summary(person, sentences=4)
        page = wikipedia.page(person)
        data["summary"] = summary
        data["title"] = page.title
        data["url"] = page.url
        data["images"] = page.images[:3]  # show top 3 images

    except Exception as e:
        data["summary"] = f"Sorry, couldn't find info for '{person}'. Error: {e}"
        data["images"] = []

    # 🎬 Fetch YouTube videos
    try:
        search_url = (
            f"https://www.googleapis.com/youtube/v3/search?part=snippet"
            f"&q={person}&type=video&maxResults=3&key={YOUTUBE_API_KEY}"
        )
        r = requests.get(search_url)
        res = r.json()
        videos = []

        for item in res.get("items", []):
            video_id = item["id"]["videoId"]
            video_title = item["snippet"]["title"]
            videos.append({
                "title": video_title,
                "url": f"https://www.youtube.com/watch?v={video_id}"
            })
        data["videos"] = videos
    except Exception as e:
        data["videos"] = []

    return data
