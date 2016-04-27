####################################################################################################
#                                                                                                  #
#                                     GreekTV Plex Channel                                         #
#                                                                                                  #
####################################################################################################

# set global variables
TITLE = 'GreekTV'
PREFIX = '/video/greektv'
XML_URL = 'http://greektv.upg.gr/api/?type=plex'

# set background art and icon defaults
ICON = 'icon-default.png'
ART = 'art-default.jpg'

####################################################################################################
def Start():
    HTTP.CacheTime = 0

    ObjectContainer.title1 = TITLE
    ObjectContainer.art = R(ART)

    DirectoryObject.thumb = R(ICON)
    DirectoryObject.art = R(ART)

    #InputDirectoryObject.art = R(ART)

    VideoClipObject.art = R(ART)

    #ValidatePrefs()

####################################################################################################
@handler(PREFIX, TITLE, thumb=ICON, art=ART)
def MainMenu():
    oc = ObjectContainer(title2=TITLE, no_cache=True)

    xml = XML.ElementFromURL(XML_URL)

    for node in xml[0][0]:
        title = node.get('title')
        thumb = node.get('hdposterurl')
        #genrel = node.get('genrel')
        url = node.get('url')
        #ishd = node.get('ishd')
        #bitrate = node.get('bitrate')
        #streamformat = node.get('streamformat')
        live = node.get('live')

        if live == 'true':
            oc.add(
                CreateVideoClipObject(
                    title=title, thumb=thumb, url=url
                    )
                )

    return oc

####################################################################################################
@route(PREFIX + '/createvideoclipobject', include_container=bool)
def CreateVideoClipObject(title, thumb, url, include_container=False, *args, **kwargs):

    video_object = VideoClipObject(
        key=Callback(CreateVideoClipObject, title=title, thumb=thumb, url=url, include_container=True),
        rating_key=url,
        title=title,
        thumb=thumb,
        content_rating='NR',
        url=url,
        items=GetMediaObject(url)
        )

    if include_container:
        return ObjectContainer(objects=[video_object])
    else:
        return video_object

####################################################################################################
def GetMediaObject(url):

    mo = [
        MediaObject(
            parts=[
                PartObject(
                    key=HTTPLiveStreamURL(Callback(PlayVideo, url=url))
                    )
                ]
            )
        ]

    return mo

####################################################################################################
@indirect
@route(PREFIX + '/playvideo.m3u8')
def PlayVideo(url):

    return IndirectResponse(VideoClipObject, key=url)
