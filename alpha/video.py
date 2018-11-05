from json import loads
from browser import ajax
from browser import document as doc
from browser import window

window.console.clear()

key = "AIzaSyAqR6xo2RuEiYDjp10UI3dPtiw-q7scJsI"
'''
88888888ba      db         88888888ba    ad88888ba   88888888888
88      "8b    d88b        88      "8b  d8"     "8b  88
88      ,8P   d8'`8b       88      ,8P  Y8,          88
88aaaaaa8P'  d8'  `8b      88aaaaaa8P'  `Y8aaaaa,    88aaaaa
88""""""'   d8YaaaaY8b     88""""88'      `"""""8b,  88"""""
88         d8""""""""8b    88    `8b            `8b  88
88        d8'        `8b   88     `8b   Y8a     a8P  88
88       d8'          `8b  88      `8b   "Y88888P"   88888888888
'''
try:
    vorc = doc.query["vorc"]
    q = doc.query["q"]
    order = doc.query["order"]
    page = doc.query["page"]
    pageNum = doc.query["pageNum"]
except KeyError:
    vorc = None
    q = None
    order = None
    page = None
    pageNum = None

print(f"VorC  -- {vorc}")
print(f"Q     -- {q}")
print(f"Order -- {order}")
print(f"Page  -- {page}")
print(f"Page# -- {pageNum}")
print('')


def run():
    '''
88888888ba   88        88  888b      88
88      "8b  88        88  8888b     88
88      ,8P  88        88  88 `8b    88
88aaaaaa8P'  88        88  88  `8b   88
88""""88'    88        88  88   `8b  88
88    `8b    88        88  88    `8b 88
88     `8b   Y8a.    .a8P  88     `8888
88      `8b   `"Y8888Y"'   88      `888
    '''
    if vorc == "v":
        GETv1()
    elif vorc is None:
        doc["main"].attrs["style"] = f"display: grid;"
        doc["preloader"].attrs["style"] = f"display: none;"


def GETv1():
    '''
  ,ad8888ba,   88888888888  888888888888                  88
 d8"'    `"8b  88                88                     ,d88
d8'            88                88                   888888
88             88aaaaa           88     8b       d8       88
88      88888  88"""""           88     `8b     d8'       88
Y8,        88  88                88      `8b   d8'        88
 Y8a.    .a88  88                88       `8b,d8'         88
  `"Y88888P"   88888888888       88         "8"           88
    '''
    url = f"https://www.googleapis.com/youtube/v3/search" \
          f"?part=snippet" \
          f"&maxResults=20" \
          f"&order={order}" \
          f"&q={q}" \
          f"&relevanceLanguage=en" \
          f"&type=video" \
          f"&videoEmbeddable=true" \
          f"&pageToken={page}" \
          f"&videoSyndicated=true" \
          f"&fields=items/id/videoId" \
          f",nextPageToken,prevPageToken" \
          f"&key={key}"
    req = ajax.ajax()
    req.bind('complete', DONEv1)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def DONEv1(req):
    '''
88888888ba,      ,ad8888ba,    888b      88  88888888888                   88
88      `"8b    d8"'    `"8b   8888b     88  88                          ,d88
88        `8b  d8'        `8b  88 `8b    88  88                        888888
88         88  88          88  88  `8b   88  88aaaaa     8b       d8       88
88         88  88          88  88   `8b  88  88"""""     `8b     d8'       88
88         8P  Y8,        ,8P  88    `8b 88  88           `8b   d8'        88
88      .a8P    Y8a.    .a8P   88     `8888  88            `8b,d8'         88
88888888Y"'      `"Y8888Y"'    88      `888  88888888888     "8"           88
    '''
    rawIDs = []
    if req.status == 200 or req.status == 0:
        data = loads(req.text)
        global nextPAGE
        nextPAGE = data.get("nextPageToken")
        global prevPAGE
        prevPAGE = data.get("prevPageToken")
        if prevPAGE is None:
            prevPAGE = ' '
        for raw in data.get("items"):
            videoID = raw.get("id").get("videoId")
            rawIDs.append(videoID)
        videoIDs = ",".join(rawIDs)
        GETv2(videoIDs)


def GETv2(videoIDs):
    '''
  ,ad8888ba,   88888888888  888888888888                ad888888b,
 d8"'    `"8b  88                88                    d8"     "88
d8'            88                88                            a8P
88             88aaaaa           88     8b       d8         ,d8P"
88      88888  88"""""           88     `8b     d8'       a8P"
Y8,        88  88                88      `8b   d8'      a8P'
 Y8a.    .a88  88                88       `8b,d8'      d8"
  `"Y88888P"   88888888888       88         "8"        88888888888
    '''
    url = f"https://www.googleapis.com/youtube/v3/videos" \
          f"?part=snippet," \
          "statistics," \
          "contentDetails" \
          f"&id={videoIDs}" \
          f"&fields=items" \
          "(id" \
          ",contentDetails" \
          "/duration" \
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
    print(url)
    req.bind('complete', DONEv2)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def DONEv2(req):
    '''
88888888ba,      ,ad8888ba,    888b      88  88888888888                ad888888b,
88      `"8b    d8"'    `"8b   8888b     88  88                        d8"     "88
88        `8b  d8'        `8b  88 `8b    88  88                                a8P
88         88  88          88  88  `8b   88  88aaaaa     8b       d8        ,d8P"
88         88  88          88  88   `8b  88  88"""""     `8b     d8'      a8P"
88         8P  Y8,        ,8P  88    `8b 88  88           `8b   d8'     a8P'
88      .a8P    Y8a.    .a8P   88     `8888  88            `8b,d8'     d8"
88888888Y"'      `"Y8888Y"'    88      `888  88888888888     "8"       88888888888
    '''
    if req.status == 200 or req.status == 0:
        data = loads(req.text)
        vRAWs = []
        for video in data.get("items", []):
            vID = video["id"]
            vLEN = video["contentDetails"]["duration"]
            cID = video["snippet"]["channelId"]
            cTITLE = video["snippet"]["channelTitle"]
            vDESC = video["snippet"]["description"]
            vDATE = video["snippet"]["publishedAt"]
            vIMG = video["snippet"]["thumbnails"]["medium"]["url"]
            vTITLE = video["snippet"]["title"]
            try:
                vVIEWS = video["statistics"]["viewCount"]
                vLIKES = video["statistics"]["likeCount"]
                vDISLIKES = video["statistics"]["dislikeCount"]
            except KeyError:
                vVIEWS = 'hidden'
                vLIKES = 'hidden'
                vDISLIKES = 'hidden'

            vLEN = vLEN.strip("PT").strip("S")
            vLEN = vLEN.replace("H", ":").replace("M", ":")
            if vLEN.endswith(":"):
                vLEN += "00"
            vLEN += ":temp"
            for x in range(10):
                vLEN = vLEN.replace(f":{x}:", f":0{x}:")
            vLEN = vLEN.replace(":temp", "")
            if ":" not in vLEN:
                vLEN = f"0:{vLEN}"
            if vLEN == '0:0':
                vLEN = "LIVE"
            print(f"{vID} -- VIDEO -- {vLEN.split()} -- {vTITLE}")
            vRAWs.append(f"<li class='video'>"
                         f"<div class='img'><img src='{vIMG}' height='120px' width='210px'>"
                         f"<time> {vLEN} </time></div>"
                         f"<br>"
                         f"<p>{vTITLE}</p>"
                         f"<p class='channel'>{cTITLE}"
                         f"<br>{vVIEWS}</p>"
                         f"</li>")
        global vSTRs
        vSTRs = "".join(vRAWs)
        global nextPAGEnum
        nextPAGEnum = str(int(pageNum) + 1)
        global prevPAGEnum
        if pageNum == "1":
            prevPAGEnum = "1"
        elif pageNum != "1":
            prevPAGEnum = str(int(pageNum) - 1)

        show()


def show():
    '''
 ad88888ba   88        88    ,ad8888ba,   I8,        8        ,8I
d8"     "8b  88        88   d8"'    `"8b  `8b       d8b       d8'
Y8,          88        88  d8'        `8b  "8,     ,8"8,     ,8"
`Y8aaaaa,    88aaaaaaaa88  88          88   Y8     8P Y8     8P
  `"""""8b,  88""""""""88  88          88   `8b   d8' `8b   d8'
        `8b  88        88  Y8,        ,8P    `8a a8'   `8a a8'
Y8a     a8P  88        88   Y8a.    .a8P      `8a8'     `8a8'
 "Y88888P"   88        88    `"Y8888Y"'        `8'       `8'
    '''
    doc["main"].attrs["style"] = f"grid-template-rows: 5% 0% 10% 2% 75% 8%; display: grid;"
    doc["preloader"].attrs["style"] = f"display: none;"
    doc["list"].html = f"<ul style='" \
                       f"height: 100%;" \
                       f"width: 100%;" \
                       f"padding-left: 0px;" \
                       f"overflow: hidden;" \
                       f"overflow-y: scroll;" \
                       f"list-style-type: none;" \
                       f"'><div class='grid-videos-container'>" \
                       f"{vSTRs}" \
                       f"<li></li><li></li><li>" \
                       f"<form style='display: inline;'>" \
                       f"<input type='hidden' name='vorc' value='{vorc}'>" \
                       f"<input type='hidden' name='q' value='{q}'>" \
                       f"<input type='hidden' name='order' value='{order}'>" \
                       f"<input type='hidden' name='pageNum' value='{prevPAGEnum}'>" \
                       f"<button type='submit' name='page' value='{prevPAGE}'>&#8249;</button>" \
                       f"</form>" \
                       f"<span style='display: inline;'> {pageNum} </span>" \
                       f"<form style='display: inline;'>" \
                       f"<input type='hidden' name='vorc' value='{vorc}'>" \
                       f"<input type='hidden' name='q' value='{q}'>" \
                       f"<input type='hidden' name='order' value='{order}'>" \
                       f"<input type='hidden' name='pageNum' value='{nextPAGEnum}'>" \
                       f"<button type='submit' name='page' value='{nextPAGE}'>&#8250;</button>" \
                       f"</form></li>"


if __name__ == 'video':
    '''
 ad88888ba  888888888888    db         88888888ba  888888888888
d8"     "8b      88        d88b        88      "8b      88
Y8,              88       d8'`8b       88      ,8P      88
`Y8aaaaa,        88      d8'  `8b      88aaaaaa8P'      88
  `"""""8b,      88     d8YaaaaY8b     88""""88'        88
        `8b      88    d8""""""""8b    88    `8b        88
Y8a     a8P      88   d8'        `8b   88     `8b       88
 "Y88888P"       88  d8'          `8b  88      `8b      88
    '''
    run()
