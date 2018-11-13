from json import loads
from browser import ajax
from browser import document as doc
from browser import window
from url import link

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
    vId = doc.query["vid"]
except KeyError:
    vId = None
try:
    cId = doc.query["cid"]
except KeyError:
    cId = None
try:
    pId = doc.query["pid"]
except KeyError:
    pId = None
print(f"VorC   -- {vorc}")
print(f"Q      -- {q}")
print(f"Order  -- {order}")
print(f"Video  -- {vId}")
print(f"Channel-- {cId}")
print(f"List   -- {pId}")
print(f"Page   -- {page}")
print(f"Page#  -- {pageNum}")
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
    elif cId is not None:
        GETu1()
    elif vorc is None:
        loaded(False)


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


def GETv1():
    '''
 d888b  d88888b d888888b      db    db       db
88' Y8b 88'     `~~88~~'      88    88      o88
88      88ooooo    88         Y8    8P       88
88  ooo 88~~~~~    88         `8b  d8'       88
88. ~8~ 88.        88          `8bd8'        88
 Y888P  Y88888P    YP            YP          VP
    '''
    url = link(Url='v1', Order=order, Q=q, Page=page)
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
        global nextPAGE, prevPAGE
        nextPAGE = data.get("nextPageToken")
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
    url = link(Url='v2', Id=videoIDs)
    req = ajax.ajax()
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
            vRAWs.append(f"<li class='video'><a href='?vid={vID}'>"
                         f"<div class='img'><img src='{vIMG}' height='120px' width='210px'>"
                         f"<time> {vLEN} </time></div>"
                         f"<p class='title'>{vTITLE}</p></a>"
                         f"<p class='channel'>{cTITLE}"
                         f"<br>{vVIEWS} Views</p>"
                         f"</li>")
        global vSTRs, nextPAGEnum, prevPAGEnum
        vSTRs = "".join(vRAWs)
        nextPAGEnum = str(int(pageNum) + 1)
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


def GETp1():
    '''
 d888b  d88888b d888888b      d8888b.       db
88' Y8b 88'     `~~88~~'      88  `8D      o88
88      88ooooo    88         88oodD'       88
88  ooo 88~~~~~    88         88~~~         88
88. ~8~ 88.        88         88            88
 Y888P  Y88888P    YP         88            VP
    '''
    url = link(Url='p1', Id=vId)
    req = ajax.ajax()
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
    global Vembed, Vtitle, Vviews, Vchannel, VchannelId, Vdesc, Vlikes, Vdislikes
    Vembed = f'https://www.youtube-nocookie.com/embed/' \
             f'{data["items"][0]["id"]}' \
             f'?list={pId}'
    Vtitle = data["items"][0]["snippet"]["title"]
    Vchannel = data["items"][0]["snippet"]["channelTitle"]
    VchannelId = data["items"][0]["snippet"]["channelId"]
    Vdesc = data["items"][0]["snippet"]["description"].replace('\n', ' <br> ')
    lines = Vdesc.split(' ')
    for line in lines:
        if 'www' in line:
            if 'http' in line:
                Vdesc = Vdesc.replace(line, f"<a class='link' href='{line}'>{line}</a>")
            else:
                temp = 'https://' + line
                Vdesc = Vdesc.replace(line, f"<a class='link' href='{temp}'>{line}</a>")
        elif 'http' in line:
            Vdesc = Vdesc.replace(line, f"<a class='link' href='{line}'>{line}</a>")
    try:
        Vviews = format(int(data["items"][0]["statistics"]["viewCount"]), ",d")
    except KeyError:
        Vviews = 'hidden'
    try:
        Vlikes = format(int(data["items"][0]["statistics"]["likeCount"]), ",d")
        Vdislikes = format(int(data["items"][0]["statistics"]["dislikeCount"]), ",d")
    except KeyError:
        Vlikes = 'hidden'
        Vdislikes = 'hidden'
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
    url = link(Url='p2', Id=vId)
    req = ajax.ajax()
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
        cID = video["snippet"]["channelId"]
        related.append([vID, vTITLE, vIMG, cTITLE, cID])
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
        cID = video[4]
        cooking.append(f"<li><a href='?vid={vID}'><img src='{vIMG}' height='120px' width='210px'><a/><div>"
                       f"<p class='vtitle'><a href='?vid={vID}' class='vtitle'>{vTITLE}</a></p>"
                       f"<p class='ctitle'><a href='?cid={cID}' class='ctitle'>{cTITLE}</a></p></div></li>")
    cooked = f"<ul class='other'>{''.join(cooking)}</ul>"
    doc["list"].html = f"<div class='grid-video-container'>" \
                       f"<div class='grid-embed'>" \
                       f"   <iframe src='{Vembed}' " \
                       f"frameborder='0' allowfullscreen class='player'>" \
                       f"   </iframe></div>" \
                       f"<div class='grid-info'>" \
                       f"<p class='title'>{Vtitle}</p>" \
                       f"<p class='views'>{Vviews} Views   &#128077; {Vlikes}   &#128078; {Vdislikes}</p>" \
                       f"<a class='channel' href='?cid={VchannelId}'>{Vchannel}</a>" \
                       f"<p class='desc'>{Vdesc}</p>" \
                       f"</div>" \
                       f"<div class='grid-other'>{cooked}</div>" \
                       f"</div>"
    loaded(True)


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


def GETc1():
    '''
 d888b  d88888b d888888b       .o88b.       db
88' Y8b 88'     `~~88~~'      d8P  Y8      o88
88      88ooooo    88         8P            88
88  ooo 88~~~~~    88         8b            88
88. ~8~ 88.        88         Y8b  d8       88
 Y888P  Y88888P    YP          `Y88P'       VP
    '''
    url = link(Url='c1', Order=order, Q=q, Page=page)
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
        global nextPAGE, prevPAGE, nextPAGEnum, prevPAGEnum
        nextPAGE = data.get("nextPageToken")
        prevPAGE = data.get("prevPageToken")
        nextPAGEnum = str(int(pageNum) + 1)
        if pageNum == "1":
            prevPAGEnum = "1"
        elif pageNum != "1":
            prevPAGEnum = str(int(pageNum) - 1)
        if prevPAGE is None:
            prevPAGE = ' '
        for raw in data.get("items"):
            channelID = raw.get("id").get("channelId")
            rawIDs.append(channelID)
        channelIDs = ",".join(rawIDs)
        GETc2(channelIDs)


def GETc2(Ids):
    '''
 d888b  d88888b d888888b       .o88b.      .d888b.
88' Y8b 88'     `~~88~~'      d8P  Y8      VP  `8D
88      88ooooo    88         8P              odD'
88  ooo 88~~~~~    88         8b            .88'
88. ~8~ 88.        88         Y8b  d8      j88.
 Y888P  Y88888P    YP          `Y88P'      888888D
    '''
    url = link(Url='c2', Id=Ids)
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
                         f"<div class='img channel'><img src='{cIMG}' height='200px' width='200px'></div>"
                         f"<p class='title'>{cTITLE}</p></a>"
                         f"<p class='channel'>"
                         f"{cSUBS} Subscriber<br>{cVIEWS} Views</p>"
                         f"</li>")
        cSTRs = "".join(cRAWs)
        SHOWc(cSTRs)


def SHOWc(cSTRs):
    '''
.d8888. db   db  .d88b.  db   d8b   db       .o88b.
88'  YP 88   88 .8P  Y8. 88   I8I   88      d8P  Y8
`8bo.   88ooo88 88    88 88   I8I   88      8P
  `Y8b. 88~~~88 88    88 Y8   I8I   88      8b
db   8D 88   88 `8b  d8' `8b d8'8b d8'      Y8b  d8
`8888Y' YP   YP  `Y88P'   `8b8' `8d8'        `Y88P'
    '''
    doc["list"].html = f"<ul style='" \
                       f"height: 100%;" \
                       f"width: 100%;" \
                       f"padding-left: 0px;" \
                       f"overflow: hidden;" \
                       f"overflow-y: scroll;" \
                       f"list-style-type: none;" \
                       f"'><div class='grid-videos-container'>" \
                       f"{cSTRs}" \
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
 ad88888ba   88888888888         db         88888888ba     ,ad8888ba,   88        88
d8"     "8b  88                 d88b        88      "8b   d8"'    `"8b  88        88
Y8,          88                d8'`8b       88      ,8P  d8'            88        88
`Y8aaaaa,    88aaaaa          d8'  `8b      88aaaaaa8P'  88             88aaaaaaaa88
  `"""""8b,  88"""""         d8YaaaaY8b     88""""88'    88             88""""""""88
        `8b  88             d8""""""""8b    88    `8b    Y8,            88        88
Y8a     a8P  88            d8'        `8b   88     `8b    Y8a.    .a8P  88        88
 "Y88888P"   88888888888  d8'          `8b  88      `8b    `"Y8888Y"'   88        88


88        88   ad88888ba   88888888888  88888888ba
88        88  d8"     "8b  88           88      "8b
88        88  Y8,          88           88      ,8P
88        88  `Y8aaaaa,    88aaaaa      88aaaaaa8P'
88        88    `"""""8b,  88"""""      88""""88'
88        88          `8b  88           88    `8b
Y8a.    .a8P  Y8a     a8P  88           88     `8b
 `"Y8888Y"'    "Y88888P"   88888888888  88      `8b
'''
'''
'''
'''
'''


def GETu1():
    '''
 d888b  d88888b d888888b      db    db       db
88' Y8b 88'     `~~88~~'      88    88      o88
88      88ooooo    88         88    88       88
88  ooo 88~~~~~    88         88    88       88
88. ~8~ 88.        88         88b  d88       88
 Y888P  Y88888P    YP         ~Y8888P'       VP
    '''
    url = link(Url='u1', Id=cId)
    req = ajax.ajax()
    req.bind('complete', DONEu1)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def DONEu1(req):
    '''
d8888b.  .d88b.  d8b   db d88888b      db    db       db
88  `8D .8P  Y8. 888o  88 88'          88    88      o88
88   88 88    88 88V8o 88 88ooooo      88    88       88
88   88 88    88 88 V8o88 88~~~~~      88    88       88
88  .8D `8b  d8' 88  V888 88.          88b  d88       88
Y8888D'  `Y88P'  VP   V8P Y88888P      ~Y8888P'       VP
    '''
    data = loads(req.text)
    data = data["items"][0]
    title = data["snippet"]["title"]
    description = data["snippet"]["description"].replace('\n', ' <br> ')
    lines = description.split(' ')
    for line in lines:
        if 'www' in line:
            if 'http' in line:
                description = description.replace(line, f"<a class='link' href='{line}'>{line}</a>")
            else:
                temp = 'https://' + line
                description = description.replace(line, f"<a class='link' href='{temp}'>{line}</a>")
        elif 'http' in line:
            description = description.replace(line, f"<a class='link' href='{line}'>{line}</a>")
    img = data["snippet"]["thumbnails"]["medium"]["url"]
    banner = data["brandingSettings"]["image"]["bannerImageUrl"]
    uploads = data["contentDetails"]["relatedPlaylists"]["uploads"]
    try:
        views = format(int(data["statistics"]["viewCount"]), ",d")
    except KeyError:
        views = 'hidden'
    try:
        subs = format(int(data["statistics"]["subscriberCount"]), ",d")
    except KeyError:
        subs = 'hidden'
    try:
        videos = format(int(data["statistics"]["videoCount"]), ",d")
    except KeyError:
        videos = 'hidden'
    global Cooked
    Cooked = [title, description, img, banner, uploads, views, subs, videos]
    GETu2()


def GETu2():
    url = link(Url='u2', Id=Cooked[4])
    req = ajax.ajax()
    req.bind('complete', DONEu2)
    req.open('GET', url, True)
    req.set_header('content-type', 'application/x-www-form-urlencoded')
    req.send()


def DONEu2(req):
    data = loads(req.text)
    try:
        Vid = data["items"][0]["contentDetails"]["videoId"]
    except IndexError:
        Vid = '4EJBISsISzg'
    SHOWu(Vid)


def SHOWu(vid):
    '''
.d8888. db   db  .d88b.  db   d8b   db      db    db
88'  YP 88   88 .8P  Y8. 88   I8I   88      88    88
`8bo.   88ooo88 88    88 88   I8I   88      88    88
  `Y8b. 88~~~88 88    88 Y8   I8I   88      88    88
db   8D 88   88 `8b  d8' `8b d8'8b d8'      88b  d88
`8888Y' YP   YP  `Y88P'   `8b8' `8d8'       ~Y8888P'
    '''
    title = Cooked[0]
    description = Cooked[1]
    img = Cooked[2]
    banner = Cooked[3]
    uploads = Cooked[4]
    views = Cooked[5]
    subs = Cooked[6]
    videos = Cooked[7]
    doc["list"].html = str(
        f"<div style='margin-top: 0;hight:auto;'>"
        f"<img src='{banner}' width='100%'>"
        f"<img class='Cimg' src='{img}' width='7%'>"
        f"<p class='Ctitle'>{title}</p>"
        f"<p class='Csubs'>{subs} Subscribers</p>"
        f"<p class='Cviews'>{views} Views</p>"
        f"<p class='Cvideos'>{videos} Videos</p>"
        f"<a class='snip1339' href='?vid={vid}&pid={uploads}'>UPLOADS</a>"
        f"<p class='Cdesc'>{description}</p></div>"
    )
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
        if cId is None:
            doc["main"].attrs["style"] = f"grid-template-rows: 5% 0% 10% 2% 75% 8%; display: grid;"
        elif cId is not None:
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
