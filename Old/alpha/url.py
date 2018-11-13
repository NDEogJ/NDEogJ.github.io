key = "AIzaSyAqR6xo2RuEiYDjp10UI3dPtiw-q7scJsI"
# pylama:skip=1
# pylint: disable=all
def link(Url=None, Order=None, Q=None, Page=None, Id=None, p5=None, p6=None):
    if Url is None:
        return None
    elif Url == 'v1':
        url = str(
             "https://www.googleapis.com/youtube/v3/search"
             "?part=snippet"
             "&maxResults=20"
            f"&order={Order}"
            f"&q={Q}"
             "&relevanceLanguage=en"
             "&type=video"
            f"&pageToken={Page}"
             "&fields="
                      "nextPageToken,"
                      "prevPageToken,"
                      "items/"
                             "id/"
                                 "videoId"
            f"&key={key}")
        print(url)
        return url
    elif Url == 'v2':
        url = str(
             "https://www.googleapis.com/youtube/v3/videos"
             "?part="
                    "snippet,"
                    "statistics,"
                    "contentDetails"
            f"&id={Id}"
             "&fields="
                      "items("
                             "id,"
                             "contentDetails/"
                                             "duration,"
                             "snippet("
                                      "channelTitle,"
                                      "thumbnails/"
                                                  "medium/"
                                                          "url,"
                                      "title),"
                             "statistics("
                                         "viewCount))"
            f"&key={key}")
        print(url)
        return url
    elif Url == 'p1':
        url = str(
             "https://www.googleapis.com/youtube/v3/videos"
             "?part="
                    "snippet,"
                    "statistics,"
                    "contentDetails"
            f"&id={Id}"
             "&fields="
                      "items("
                             "id,"
                             "snippet("
                                      "channelId,"
                                      "channelTitle,"
                                      "description,"
                                      "thumbnails/"
                                                  "medium/"
                                                          "url,"
                                      "title),"
                             "statistics("
                                         "dislikeCount,"
                                         "likeCount,"
                                         "viewCount))"
            f"&key={key}")
        print(url)
        return url
    elif Url == 'p2':
        url = str(
             "https://www.googleapis.com/youtube/v3/search"
             "?part=snippet"
             "&maxResults=20"
            f"&relatedToVideoId={Id}"
             "&relevanceLanguage=en"
             "&type=video"
             "&fields="
                      "items("
                             "id/"
                                 "videoId,"
                             "snippet("
                                      "channelTitle,"
                                      "channelId,"
                                      "thumbnails/"
                                                  "medium/"
                                                          "url,"
                                      "title))"
            f"&key={key}")
        print(url)
        return url
    elif Url == 'c1':
        url = str(
             "https://www.googleapis.com/youtube/v3/search"
             "?part=snippet"
             "&maxResults=20"
            f"&order={Order}"
            f"&q={Q}"
             "&relevanceLanguage=en"
             "&type=channel"
            f"&pageToken={Page}"
             "&fields="
                      "nextPageToken,"
                      "prevPageToken,"
                      "items/"
                             "id/"
                                 "channelId"
            f"&key={key}")
        print(url)
        return url
    elif Url == 'c2':
        url = str(
             "https://www.googleapis.com/youtube/v3/channels"
             "?part="
                    "snippet,"
                    "statistics"
            f"&id={Id}"
             "&fields="
                      "nextPageToken,"
                      "prevPageToken,"
                      "items("
                             "id,"
                             "snippet("
                                      "thumbnails/"
                                                  "medium/"
                                                          "url,"
                                      "title),"
                             "statistics("
                                         "subscriberCount,"
                                         "viewCount))"
            f"&key={key}")
        print(url)
        return url
    elif Url == 'u1':
        url = str(
             "https://www.googleapis.com/youtube/v3/channels"
             "?part="
                    "snippet,"
                    "statistics,"
                    "contentDetails,"
                    "brandingSettings"
            f"&id={Id}"
             "&fields=items("
                            "brandingSettings/"
                                              "image/"
                                                     "bannerImageUrl,"
                            "contentDetails/"
                                            "relatedPlaylists/"
                                                              "uploads,"
                            "snippet("
                                     "description,"
                                     "thumbnails/"
                                                 "medium/"
                                                         "url,"
                                     "title),"
                            "statistics("
                                        "subscriberCount,"
                                        "videoCount,"
                                        "viewCount))"
            f"&key={key}")
        print(url)
        return url
    elif Url == 'u2':
        url = str(
             "https://www.googleapis.com/youtube/v3/playlistItems"
             "?part=contentDetails"
             "&maxResults=1"
            f"&playlistId={Id}"
             "&fields="
                      "items/"
                             "contentDetails/"
                                             "videoId"
            f"&key={key}")
        print(url)
        return url
