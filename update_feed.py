import json
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

FEED_URL = "https://pianopianoai.substack.com/feed"

req = urllib.request.Request(
    FEED_URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

with urllib.request.urlopen(req) as response:
    xml_data = response.read()

root = ET.fromstring(xml_data)

channel = root.find("channel")
articles = []

namespaces = {
    "media": "http://search.yahoo.com/mrss/",
    "content": "http://purl.org/rss/1.0/modules/content/"
}

for item in channel.findall("item"):
    title = item.findtext("title", "").strip()
    link = item.findtext("link", "").strip()
    description = item.findtext("description", "").strip()
    pub_date = item.findtext("pubDate", "").strip()

    image = ""

    enclosure = item.find("enclosure")
    if enclosure is not None:
        image = enclosure.attrib.get("url", "")

    media = item.find("media:content", namespaces)
    if not image and media is not None:
        image = media.attrib.get("url", "")

    try:
        date = parsedate_to_datetime(pub_date).isoformat()
    except Exception:
        date = pub_date

    articles.append({
        "title": title,
        "link": link,
        "description": description,
        "date": date,
        "image": image
    })

with open("articles.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"Aggiornati {len(articles)} articoli.")
