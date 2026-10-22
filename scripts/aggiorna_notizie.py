"""Scarica il feed RSS di Caritas Italiana e scrive news.json per la sezione Notizie dell'app."""
import html, json, re, sys, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

FEED = "https://www.caritas.it/feed/"
MAX_NOTIZIE = 20

def testo(html_str, limite=220):
    t = re.sub(r"<[^>]+>", " ", html_str or "")
    t = re.sub(r"\s+", " ", html.unescape(t)).strip()
    t = re.sub(r"\s*(L'articolo|The post) .*? proviene da .*$", "", t)
    t = re.sub(r"^©[^)]*\)[^\w«\"]*", "", t)  # toglie il credito della foto in apertura
    return t if len(t) <= limite else t[:limite].rsplit(" ", 1)[0] + "…"

def immagine(html_str):
    m = re.search(r'<img[^>]+src="([^"]+)"', html_str or "")
    return m.group(1) if m else None

req = urllib.request.Request(FEED, headers={"User-Agent": "formazione-operatori/1.0"})
radice = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())
ns = {"content": "http://purl.org/rss/1.0/modules/content/"}

notizie = []
for item in radice.iter("item"):
    descr = item.findtext("description") or ""
    corpo = item.findtext("content:encoded", namespaces=ns) or ""
    notizie.append({
        "titolo": html.unescape(item.findtext("title") or "").strip(),
        "link": item.findtext("link"),
        "data": parsedate_to_datetime(item.findtext("pubDate")).isoformat(),
        "sommario": testo(descr) or testo(corpo),
        "immagine": immagine(descr) or immagine(corpo),
    })

if not notizie:
    raise SystemExit("Feed vuoto: news.json non modificato")

notizie = notizie[:MAX_NOTIZIE]
try:
    with open("news.json", encoding="utf-8") as f:
        if json.load(f).get("notizie") == notizie:
            print("Nessuna notizia nuova")
            sys.exit(0)
except FileNotFoundError:
    pass

with open("news.json", "w", encoding="utf-8") as f:
    json.dump({"aggiornato": datetime.now(timezone.utc).isoformat(timespec="minutes"),
               "fonte": FEED, "notizie": notizie}, f, ensure_ascii=False, indent=1)
print(f"{len(notizie)} notizie salvate")
