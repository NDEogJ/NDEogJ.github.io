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
d8888b. db    db d8b   db
88  `8D 88    88 888o  88
88oobY' 88    88 88V8o 88
88`8b   88    88 88 V8o88
88 `88. 88b  d88 88  V888
88   YD ~Y8888P' VP   V8P
    '''
    if vorc == "v":
        GETv1()
    elif vorc == "c":
        GETc1()
    elif vId is not None:
        GETp1()
    elif vorc is None:
        loaded(False)
'''
'''
'''
'''
'''
'''
'''
 ad88888ba   88888888888         db         88888888ba     ,ad8888ba,   88        88
d8"     "8b  88                 d88b        88      "8b   d8"'    `"8b  88        88
Y8,          88                d8'`8b       88      ,8P  d8'            88        88
`Y8aaaaa,    88aaaaa          d8'  `8b      88aaaaaa8P'  88             88aaaaaaaa88
  `"""""8b,  88"""""         d8YaaaaY8b     88""""88'    88             88""""""""88
        `8b  88             d8""""""""8b    88    `8b    Y8,            88        88
Y8a     a8P  88            d8'        `8b   88     `8b    Y8a.    .a8P  88        88
 "Y88888P"   88888888888  d8'          `8b  88      `8b    `"Y8888Y"'   88        88


8b           d8  88  88888888ba,    88888888888    ,ad8888ba,
`8b         d8'  88  88      `"8b   88            d8"'    `"8b
 `8b       d8'   88  88        `8b  88           d8'        `8b
  `8b     d8'    88  88         88  88aaaaa      88          88
   `8b   d8'     88  88         88  88"""""      88          88
    `8b d8'      88  88         8P  88           Y8,        ,8P
     `888'       88  88      .a8P   88            Y8a.    .a8P
      `8'        88  88888888Y"'    88888888888    `"Y8888Y"'
'''
'''
'''
'''
'''
'''
'''
def GETv1():
    '''
 d888b  d88888b d888888b      db    db       db
88' Y8b 88'     `~~88~~'      88    88      o88
88      88ooooo    88         Y8    8P       88
88  ooo 88~~~~~    88         `8b  d8'       88
88. ~8~ 88.        88          `8bd8'        88
 Y888P  Y88888P    YP            YP          VP
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
d8888b.  .d88b.  d8b   db d88888b      db    db       db
88  `8D .8P  Y8. 888o  88 88'          88    88      o88
88   88 88    88 88V8o 88 88ooooo      Y8    8P       88
88   88 88    88 88 V8o88 88~~~~~      `8b  d8'       88
88  .8D `8b  d8' 88  V888 88.           `8bd8'        88
Y8888D'  `Y88P'  VP   V8P Y88888P         YP          VP
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
 d888b  d88888b d888888b      db    db      .d888b.
88' Y8b 88'     `~~88~~'      88    88      VP  `8D
88      88ooooo    88         Y8    8P         odD'
88  ooo 88~~~~~    88         `8b  d8'       .88'
88. ~8~ 88.        88          `8bd8'       j88.
 Y888P  Y88888P    YP            YP         888888D
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
d8888b.  .d88b.  d8b   db d88888b      db    db      .d888b.
88  `8D .8P  Y8. 888o  88 88'          88    88      VP  `8D
88   88 88    88 88V8o 88 88ooooo      Y8    8P         odD'
88   88 88    88 88 V8o88 88~~~~~      `8b  d8'       .88'
88  .8D `8b  d8' 88  V888 88.           `8bd8'       j88.
Y8888D'  `Y88P'  VP   V8P Y88888P         YP         888888D
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
        SHOWv()


def SHOWv():
    '''
.d8888. db   db  .d88b.  db   d8b   db      db    db
88'  YP 88   88 .8P  Y8. 88   I8I   88      88    88
`8bo.   88ooo88 88    88 88   I8I   88      Y8    8P
  `Y8b. 88~~~88 88    88 Y8   I8I   88      `8b  d8'
db   8D 88   88 `8b  d8' `8b d8'8b d8'       `8bd8'
`8888Y' YP   YP  `Y88P'   `8b8' `8d8'          YP
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
'''
'''
'''
'''
'''
'''
'''
 ad88888ba   88888888888         db         88888888ba     ,ad8888ba,   88        88
d8"     "8b  88                 d88b        88      "8b   d8"'    `"8b  88        88
Y8,          88                d8'`8b       88      ,8P  d8'            88        88
`Y8aaaaa,    88aaaaa          d8'  `8b      88aaaaaa8P'  88             88aaaaaaaa88
  `"""""8b,  88"""""         d8YaaaaY8b     88""""88'    88             88""""""""88
        `8b  88             d8""""""""8b    88    `8b    Y8,            88        88
Y8a     a8P  88            d8'        `8b   88     `8b    Y8a.    .a8P  88        88
 "Y88888P"   88888888888  d8'          `8b  88      `8b    `"Y8888Y"'   88        88


88888888ba   88                  db         8b        d8  88888888888  88888888ba
88      "8b  88                 d88b         Y8,    ,8P   88           88      "8b
88      ,8P  88                d8'`8b         Y8,  ,8P    88           88      ,8P
88aaaaaa8P'  88               d8'  `8b         "8aa8"     88aaaaa      88aaaaaa8P'
88""""""'    88              d8YaaaaY8b         `88'      88"""""      88""""88'
88           88             d8""""""""8b         88       88           88    `8b
88           88            d8'        `8b        88       88           88     `8b
88           88888888888  d8'          `8b       88       88888888888  88      `8b
'''
'''
'''
'''
'''
'''
'''
def GETp1():
    '''
 d888b  d88888b d888888b      d8888b.       db
88' Y8b 88'     `~~88~~'      88  `8D      o88
88      88ooooo    88         88oodD'       88
88  ooo 88~~~~~    88         88~~~         88
88. ~8~ 88.        88         88            88
 Y888P  Y88888P    YP         88            VP
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
    req.bind('complete', DONEp1)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()
 

def DONEp1(req):
    '''
d8888b.  .d88b.  d8b   db d88888b      d8888b.       db
88  `8D .8P  Y8. 888o  88 88'          88  `8D      o88
88   88 88    88 88V8o 88 88ooooo      88oodD'       88
88   88 88    88 88 V8o88 88~~~~~      88~~~         88
88  .8D `8b  d8' 88  V888 88.          88            88
Y8888D'  `Y88P'  VP   V8P Y88888P      88            VP
    '''
    data = loads(req.text)
    print(data)
    global link, title, views, channel, desc, likes, dislikes
    link = f'https://www.youtube-nocookie.com/embed/' \
           f'{data["items"][0]["id"]}' \
           f'?rel=0'
    title = data["items"][0]["snippet"]["title"]
    channel = data["items"][0]["snippet"]["channelTitle"]
    desc = data["items"][0]["snippet"]["description"]
    try:
        views = format(int(data["items"][0]["statistics"]["viewCount"]), ",d")
    except KeyError:
        views = 'hidden'
    try: 
        likes = format(int(data["items"][0]["statistics"]["likeCount"]), ",d")
        dislikes = format(int(data["items"][0]["statistics"]["dislikeCount"]), ",d")
    except KeyError:
        likes = 'hidden'
        dislikes = 'hidden'
    GETp2()


def GETp2():
    '''
 d888b  d88888b d888888b      d8888b.      .d888b.
88' Y8b 88'     `~~88~~'      88  `8D      VP  `8D
88      88ooooo    88         88oodD'         odD'
88  ooo 88~~~~~    88         88~~~         .88'
88. ~8~ 88.        88         88           j88.
 Y888P  Y88888P    YP         88           888888D
    '''
    url = f"https://www.googleapis.com/youtube/v3/search" \
          f"?part=snippet" \
          f"&maxResults=10" \
          f"&relatedToVideoId={vId}" \
          f"&relevanceLanguage=en" \
          f"&type=video" \
          f"&videoEmbeddable=true" \
          f"&fields=items" \
          "(id" \
          "/videoId" \
          ",snippet" \
          "(channelTitle" \
          ",thumbnails" \
          "/medium" \
          "/url" \
          ",title))" \
          f"&key={key}"
    req = ajax.ajax()
    print(url)
    req.bind('complete', DONEp2)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def DONEp2(req):
    '''
d8888b.  .d88b.  d8b   db d88888b      d8888b.      .d888b.
88  `8D .8P  Y8. 888o  88 88'          88  `8D      VP  `8D
88   88 88    88 88V8o 88 88ooooo      88oodD'         odD'
88   88 88    88 88 V8o88 88~~~~~      88~~~         .88'
88  .8D `8b  d8' 88  V888 88.          88           j88.
Y8888D'  `Y88P'  VP   V8P Y88888P      88           888888D
    '''
    data = loads(req.text)
    related = []
    for video in data.get("items", []):
        vID = video["id"]["videoId"]
        vTITLE = video["snippet"]["title"]
        vIMG = video["snippet"]["thumbnails"]["medium"]["url"]
        cTITLE = video["snippet"]["channelTitle"]
        related.append([vID, vTITLE, vIMG, cTITLE])
    SHOWp(related)


def SHOWp(raw):
    '''
.d8888. db   db  .d88b.  db   d8b   db      d8888b.
88'  YP 88   88 .8P  Y8. 88   I8I   88      88  `8D
`8bo.   88ooo88 88    88 88   I8I   88      88oodD'
  `Y8b. 88~~~88 88    88 Y8   I8I   88      88~~~
db   8D 88   88 `8b  d8' `8b d8'8b d8'      88
`8888Y' YP   YP  `Y88P'   `8b8' `8d8'       88
    '''
    cooking = []
    for video in raw:
        vID = video[0]
        vTITLE = video[1]
        vIMG = video[2]
        cTITLE = video[3]
        cooking.append(f"<li><a href='?id={vID}'><img src='{vIMG}'><a/><div>"
                       f"<a class='vtitle' href='?id={vID}'>{vTITLE}</a>"
                       f"<p class='ctitle'>{cTITLE}</p></div></li>")
    cooked = f"<ul class='other'>{''.join(cooking)}</ul>"
    doc["list"].html = f"<div class='grid-video-container'>" \
                       f"<div class='grid-embed'>" \
                       f"   <iframe src='{link}' " \
                       f"frameborder='0' allowfullscreen class='player'>" \
                       f"   </iframe></div>" \
                       f"<div class='grid-info'>" \
                       f"<p class='title'>{title}</p>" \
                       f"<p class='views'>{views} Views   &#128077; {likes}   &#128078; {dislikes}</p>" \
                       f"<p class='channel'>{channel}</p>" \
                       f"<p class='desc'>{desc}</p>" \
                       f"</div>" \
                       f"<div class='grid-other'>{cooked}</div>" \
                       f"</div>"
    loaded(True)
'''
'''
'''
'''
'''
'''
'''
 ad88888ba   88888888888         db         88888888ba     ,ad8888ba,   88        88
d8"     "8b  88                 d88b        88      "8b   d8"'    `"8b  88        88
Y8,          88                d8'`8b       88      ,8P  d8'            88        88
`Y8aaaaa,    88aaaaa          d8'  `8b      88aaaaaa8P'  88             88aaaaaaaa88
  `"""""8b,  88"""""         d8YaaaaY8b     88""""88'    88             88""""""""88
        `8b  88             d8""""""""8b    88    `8b    Y8,            88        88
Y8a     a8P  88            d8'        `8b   88     `8b    Y8a.    .a8P  88        88
 "Y88888P"   88888888888  d8'          `8b  88      `8b    `"Y8888Y"'   88        88


  ,ad8888ba,   88        88         db         888b      88  888b      88  88888888888  88
 d8"'    `"8b  88        88        d88b        8888b     88  8888b     88  88           88
d8'            88        88       d8'`8b       88 `8b    88  88 `8b    88  88           88
88             88aaaaaaaa88      d8'  `8b      88  `8b   88  88  `8b   88  88aaaaa      88
88             88""""""""88     d8YaaaaY8b     88   `8b  88  88   `8b  88  88"""""      88
Y8,            88        88    d8""""""""8b    88    `8b 88  88    `8b 88  88           88
 Y8a.    .a8P  88        88   d8'        `8b   88     `8888  88     `8888  88           88
  `"Y8888Y"'   88        88  d8'          `8b  88      `888  88      `888  88888888888  88888888888
'''
'''
'''
'''
'''
'''
'''
def GETc1():
    '''
 d888b  d88888b d888888b       .o88b.       db
88' Y8b 88'     `~~88~~'      d8P  Y8      o88
88      88ooooo    88         8P            88
88  ooo 88~~~~~    88         8b            88
88. ~8~ 88.        88         Y8b  d8       88
 Y888P  Y88888P    YP          `Y88P'       VP
    '''
    url = f"https://www.googleapis.com/youtube/v3/search" \
          f"?part=snippet" \
          f"&maxResults=20" \
          f"&order={order}" \
          f"&q={q}" \
          f"&relevanceLanguage=en" \
          f"&type=channel" \
          f"&pageToken={page}" \
          f"&fields=items/id/channelId" \
          f",nextPageToken,prevPageToken" \
          f"&key={key}"
    req = ajax.ajax()
    req.bind('complete', DONEc1)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def DONEc1(req):
    '''
d8888b.  .d88b.  d8b   db d88888b       .o88b.       db
88  `8D .8P  Y8. 888o  88 88'          d8P  Y8      o88
88   88 88    88 88V8o 88 88ooooo      8P            88
88   88 88    88 88 V8o88 88~~~~~      8b            88
88  .8D `8b  d8' 88  V888 88.          Y8b  d8       88
Y8888D'  `Y88P'  VP   V8P Y88888P       `Y88P'       VP
    '''
    rawIDs = []
    if req.status == 200 or req.status == 0:
        data = loads(req.text)
        global nextPAGE, prevPAGE
        nextPAGE = data.get("nextPageToken")
        prevPAGE = data.get("prevPageToken")
        if prevPAGE is None:
            prevPAGE = ' '
        for raw in data.get("items"):
            channelID = raw.get("id").get("channelId")
            rawIDs.append(channelID)
        channelIDs = ",".join(rawIDs)
        GETc2(channelIDs)



def GETc2(raw):
    '''
 d888b  d88888b d888888b       .o88b.      .d888b.
88' Y8b 88'     `~~88~~'      d8P  Y8      VP  `8D
88      88ooooo    88         8P              odD'
88  ooo 88~~~~~    88         8b            .88'
88. ~8~ 88.        88         Y8b  d8      j88.
 Y888P  Y88888P    YP          `Y88P'      888888D
    '''
    url = f"https://www.googleapis.com/youtube/v3/channels" \
          f"?part=snippet,statistics" \
          f"&id={raw}" \
          f"&fields=items" \
          f"(id" \
          f",snippet" \
          f"(thumbnails" \
          f"/medium" \
          f"/url" \
          f",title)" \
          f",statistics" \
          f"(subscriberCount" \
          f",viewCount))" \
          f",nextPageToken,prevPageToken" \
          f"&key={key}"
    print(url)
    req = ajax.ajax()
    req.bind('complete', DONEc2)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def DONEc2(req):
    '''
d8888b.  .d88b.  d8b   db d88888b       .o88b.      .d888b.
88  `8D .8P  Y8. 888o  88 88'          d8P  Y8      VP  `8D
88   88 88    88 88V8o 88 88ooooo      8P              odD'
88   88 88    88 88 V8o88 88~~~~~      8b            .88'
88  .8D `8b  d8' 88  V888 88.          Y8b  d8      j88.
Y8888D'  `Y88P'  VP   V8P Y88888P       `Y88P'      888888D
    '''
    if req.status == 200 or req.status == 0:
        data = loads(req.text)
        cRAWs = []
        for video in data.get("items", []):
            cID = video['id']
            cTITLE = video['snippet']['title']
            cIMG = video['snippet']['thumbnails']['medium']['url']
            cSUBS = format(int(video['statistics']['subscriberCount']), ',d')
            cVIEWS = format(int(video['statistics']['viewCount']), ',d')
            print(f"{cID} -- CHANNEL -- {cSUBS} -- {cTITLE}")
            cRAWs.append(f"<li class='video'><a href='?cid={cID}'>"
                         f"<div class='img'><img src='{cIMG}' height='160px' width='210px'></div>"
                         f"<p class='title'>{cTITLE}</p></a>"
                         f"<p class='channel'>"
                         f"{cSUBS} Subscriber<br>{cVIEWS} Views</p>"
                         f"</li>")
        cSTRs = "".join(cRAWs)
        SHOWc(cSTRs)
        loaded(True)





def SHOWc(vSTRs):
    '''
.d8888. db   db  .d88b.  db   d8b   db      db    db
88'  YP 88   88 .8P  Y8. 88   I8I   88      88    88
`8bo.   88ooo88 88    88 88   I8I   88      Y8    8P
  `Y8b. 88~~~88 88    88 Y8   I8I   88      `8b  d8'
db   8D 88   88 `8b  d8' `8b d8'8b d8'       `8bd8'
`8888Y' YP   YP  `Y88P'   `8b8' `8d8'          YP
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
                       f"<input type='hidden' name='pageNum' value='{prevPAGE}'>" \
                       f"<button type='submit' name='page' value='{prevPAGE}'>&#8249;</button>" \
                       f"</form>" \
                       f"<span style='display: inline;'> {pageNum} </span>" \
                       f"<form style='display: inline;'>" \
                       f"<input type='hidden' name='vorc' value='{vorc}'>" \
                       f"<input type='hidden' name='q' value='{q}'>" \
                       f"<input type='hidden' name='order' value='{order}'>" \
                       f"<input type='hidden' name='pageNum' value='{nextPAGE}'>" \
                       f"<button type='submit' name='page' value='{nextPAGE}'>&#8250;</button>" \
                       f"</form></li>"
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
