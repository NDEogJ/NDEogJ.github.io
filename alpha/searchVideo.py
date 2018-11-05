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
try:
    vId = doc.query["id"]
except KeyError:
    vId = None
print(f"VorC  -- {vorc}")
print(f"Q     -- {q}")
print(f"Order -- {order}")
print(f"Video -- {vId}")
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
    elif vId is not None:
        GETv3()
    elif vorc is None:
        loaded(False)


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
          "(channelTitle" \
          ",thumbnails" \
          "/medium" \
          "/url" \
          ",title)" \
          ",statistics" \
          "(viewCount))" \
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
            cTITLE = video["snippet"]["channelTitle"]
            vIMG = video["snippet"]["thumbnails"]["medium"]["url"]
            vTITLE = video["snippet"]["title"]
            try:
                vVIEWS = format(int(video["statistics"]["viewCount"]), ",d")
            except KeyError:
                vVIEWS = 'hidden'

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
            vRAWs.append(f"<li class='video'><a href='?id={vID}'>"
                         f"<div class='img'><img src='{vIMG}' height='120px' width='210px'>"
                         f"<time> {vLEN} </time></div>"
                         f"<p class='title'>{vTITLE}</p></a>"
                         f"<p class='channel'>{cTITLE}"
                         f"<br>{vVIEWS} Views</p>"
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
 ad88888ba   88        88    ,ad8888ba,   I8,        8        ,8I                  ad888888b,
d8"     "8b  88        88   d8"'    `"8b  `8b       d8b       d8'                 d8"     "88
Y8,          88        88  d8'        `8b  "8,     ,8"8,     ,8"                          a8P
`Y8aaaaa,    88aaaaaaaa88  88          88   Y8     8P Y8     8P    8b       d8         ,d8P"
  `"""""8b,  88""""""""88  88          88   `8b   d8' `8b   d8'    `8b     d8'       a8P"
        `8b  88        88  Y8,        ,8P    `8a a8'   `8a a8'      `8b   d8'      a8P'
Y8a     a8P  88        88   Y8a.    .a8P      `8a8'     `8a8'        `8b,d8'      d8"
 "Y88888P"   88        88    `"Y8888Y"'        `8'       `8'           "8"        88888888888
    '''
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
    loaded(True)


def GETv3():
    '''
  ,ad8888ba,   88888888888  888888888888                ad888888b,
 d8"'    `"8b  88                88                    d8"     "88
d8'            88                88                            a8P
88             88aaaaa           88     8b       d8         aad8"
88      88888  88"""""           88     `8b     d8'         ""Y8,
Y8,        88  88                88      `8b   d8'             "8b
 Y8a.    .a88  88                88       `8b,d8'      Y8,     a88
  `"Y88888P"   88888888888       88         "8"         "Y888888P'
    '''
    url = f"https://www.googleapis.com/youtube/v3/videos" \
          f"?part=snippet," \
          "statistics," \
          "contentDetails" \
          f"&id={vId}" \
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
    print(url)
    req.bind('complete', DONEv3)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def DONEv3(req):
    '''
88888888ba,      ,ad8888ba,    888b      88  88888888888                ad888888b,
88      `"8b    d8"'    `"8b   8888b     88  88                        d8"     "88
88        `8b  d8'        `8b  88 `8b    88  88                                a8P
88         88  88          88  88  `8b   88  88aaaaa     8b       d8        aad8"
88         88  88          88  88   `8b  88  88"""""     `8b     d8'        ""Y8,
88         8P  Y8,        ,8P  88    `8b 88  88           `8b   d8'            "8b
88      .a8P    Y8a.    .a8P   88     `8888  88            `8b,d8'     Y8,     a88
88888888Y"'      `"Y8888Y"'    88      `888  88888888888     "8"        "Y888888P'
    '''
    data = loads(req.text)
    global link, title, views
    link = f'https://www.youtube-nocookie.com/embed/' \
           f'{data["items"][0]["id"]}' \
           f'?rel=0'
    title = data["items"][0]["snippet"]["title"]
    try:
        views = format(int(data["items"][0]["statistics"]["viewCount"]), ",d")
    except KeyError:
        views = 'hidden'
    SHOWv3()


def SHOWv3():
    '''
 ad88888ba   88        88    ,ad8888ba,   I8,        8        ,8I                  ad888888b,
d8"     "8b  88        88   d8"'    `"8b  `8b       d8b       d8'                 d8"     "88
Y8,          88        88  d8'        `8b  "8,     ,8"8,     ,8"                          a8P
`Y8aaaaa,    88aaaaaaaa88  88          88   Y8     8P Y8     8P    8b       d8         aad8"
  `"""""8b,  88""""""""88  88          88   `8b   d8' `8b   d8'    `8b     d8'         ""Y8,
        `8b  88        88  Y8,        ,8P    `8a a8'   `8a a8'      `8b   d8'             "8b
Y8a     a8P  88        88   Y8a.    .a8P      `8a8'     `8a8'        `8b,d8'      Y8,     a88
 "Y88888P"   88        88    `"Y8888Y"'        `8'       `8'           "8"         "Y888888P'
    '''
    doc["list"].html = f"<div class='grid-video-container'>" \
                       f"<div class='grid-embed'>" \
                       f"   <iframe src='{link}' " \
                       f"frameborder='0' allowfullscreen class='player'>" \
                       f"   </iframe></div>" \
                       f"<div class='grid-info'>" \
                       f"<p class='title'>{title}</p>" \
                       f"<p class='views'>{views} Views</p>" \
                       f"</div>" \
                       f"<div class='grid-other'><br>other<br>WIP</div>" \
                       f"</div>"
    loaded(True)


def loaded(grid):
    '''
88           ,ad8888ba,         db         88888888ba,    88888888888  88888888ba,
88          d8"'    `"8b       d88b        88      `"8b   88           88      `"8b
88         d8'        `8b     d8'`8b       88        `8b  88           88        `8b
88         88          88    d8'  `8b      88         88  88aaaaa      88         88
88         88          88   d8YaaaaY8b     88         88  88"""""      88         88
88         Y8,        ,8P  d8""""""""8b    88         8P  88           88         8P
88          Y8a.    .a8P  d8'        `8b   88      .a8P   88           88      .a8P
88888888888  `"Y8888Y"'  d8'          `8b  88888888Y"'    88888888888  88888888Y"'
    '''
    if grid is True:
        doc["main"].attrs["style"] = f"grid-template-rows: 5% 0% 10% 2% 75% 8%; display: grid;"
    elif grid is False:
        doc["main"].attrs["style"] = f"display: grid;"
    doc["preloader"].attrs["style"] = f"display: none;"


if __name__ == 'searchVideo':
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
