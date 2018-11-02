from browser import ajax, window
from browser import document as doc
from json import loads


def run():
    parse()
    starter()


def parse():
    window.console.clear()
    global key
    key = "AIzaSyAqR6xo2RuEiYDjp10UI3dPtiw-q7scJsI"
    print(f"Key   -- {key}")
    global vorc
    try:
        vorc = doc.query["vorc"]
    except KeyError:
        vorc = None
    print(f"VorC  -- {vorc}")
    global q
    try:
        q = doc.query["q"]
    except KeyError:
        q = None
    print(f"Q     -- {q}")
    global order
    try:
        order = doc.query["order"]
    except KeyError:
        order = None
    print(f"Order -- {order}")
    global cid
    try:
        cid = doc.query["cid"]
    except KeyError:
        cid = None
    print(f"Cid   -- {cid}")
    global page
    try:
        page = doc.query["page"]
    except KeyError:
        page = None
    print(f"Page  -- {page}")
    print('')


def starter():
    if vorc is None:
        return
    if vorc == "v":
        GETv1()
    if vorc == "c":
        return


def GETv1():
    url = f"https://www.googleapis.com/youtube/v3/search" \
          f"?part=snippet" \
          f"&maxResults=10" \
          f"&order={order}" \
          f"&q={q}" \
          f"&relevanceLanguage=en" \
          f"&type=video" \
          f"&videoEmbeddable=true" \
          f"&fields=items%2Fid%2FvideoId" \
          f"&key={key}"
    req = ajax.ajax()
    req.bind('complete', DONEv1)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def DONEv1(req):
    rawIDs = []
    if req.status == 200 or req.status == 0:
        data = loads(req.text)
        for raw in data.get("items"):
            videoID = raw.get("id").get("videoId")
            rawIDs.append(videoID)
        videoIDs = ",".join(rawIDs)
        GETv2(videoIDs)


def GETv2(videoIDs):
    url = f"https://www.googleapis.com/youtube/v3/videos" \
          f"?part=snippet,statistics" \
          f"&id={videoIDs}" \
          f"&fields=items" \
           "(id" \
           ",snippet" \
           "(channelId" \
           ",channelTitle" \
           ",description" \
           ",publishedAt" \
           ",thumbnails" \
           "/medium" \
           "/url" \
           ",title)" \
           ",statistics" \
           "(dislikeCount" \
           ",likeCount" \
           ",viewCount))" \
          f"&key={key}"
    req = ajax.ajax()
    req.bind('complete', DONEv2)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def DONEv2(req):
    if req.status == 200 or req.status == 0:
        data = loads(req.text)
        for video in data.get("items", []):
            vID = video["id"]
            vDATE = video["snippet"]["publishedAt"]
            cID = video["snippet"]["channelId"]
            vTITLE = video["snippet"]["title"]
            vDESC = video["snippet"]["description"]
            vIMG = video["snippet"]["thumbnails"]["medium"]["url"]
            cTITLE = video["snippet"]["channelTitle"]
            vVIEWS = video["statistics"]["viewCount"]
            vLIKES = video["statistics"]["likeCount"]
            vDISLIKES = video["statistics"]["dislikeCount"]
            print(f"{vID} -- VIDEO -- {vTITLE}")
            doc["list"].html += f"<li><p>{vID} -- VIDEO -- {vTITLE}</p></li>"
