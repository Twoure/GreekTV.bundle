####################################################################################################
#                                                                                                  #
#                                     GreekTV Plex Channel                                         #
#                                                                                                  #
####################################################################################################

# set global variables
TITLE = 'GreekTV'
PREFIX = '/video/greektv'
XML_URL_ROKU = 'http://greektv.upg.gr/api/?type=rokuxml'

# set background art and icon defaults
ICON = 'icon-default.jpg'
ART = 'art-default.jpg'

####################################################################################################
def Start():
    HTTP.CacheTime = 10

    ObjectContainer.title1 = TITLE
    ObjectContainer.art = R(ART)

    DirectoryObject.thumb = R(ICON)
    DirectoryObject.art = R(ART)

    VideoClipObject.art = R(ART)

####################################################################################################
@handler(PREFIX, TITLE, thumb=ICON, art=ART)
def MainMenu():
    oc = ObjectContainer(title2=TITLE)

    oc.add(DirectoryObject(
        key=Callback(DirectoryList, category='all'),
        title='All',
        summary='List all available Channels',
        ))
    oc.add(DirectoryObject(
        key=Callback(CategoryList),
        title='Categories',
        summary='List Channels by Categories',
        ))

    return oc

####################################################################################################
@route(PREFIX + '/categories')
def CategoryList():
    oc = ObjectContainer(title2='Categories', no_cache=True)

    html = HTML.ElementFromURL(XML_URL_ROKU)
    cat_list = list()
    for c in html.xpath('//category'):
        cat_list.append({
            'title': c.get('title'), 'thumb': c.get('hd_img'),
            'summary': c.get('description')
            })

    for c in Util.ListSortedByKey(cat_list, 'title'):
        oc.add(DirectoryObject(
            key=Callback(DirectoryList, category=c['title']),
            title=c['title'],
            thumb=Resource.ContentsOfURLWithFallback(c['thumb'], ICON),
            summary=c['summary'],
            ))

    return oc

####################################################################################################
@route(PREFIX + '/directory-list')
def DirectoryList(category):
    oc = ObjectContainer(title2=category.title(), no_cache=True)

    html = HTML.ElementFromURL(XML_URL_ROKU)

    # setup feed node depending of category/all list
    feed_node = '//feed[@title' + ('' if category == 'all' else '="{}"'.format(category)) + ']/item'

    c_list = list()
    for item in html.xpath(feed_node):
        t = dict()
        # setup title & thumb
        t['title'] = item.xpath('./title/text()')[0]
        t['thumb'] = item.get('hdimg')

        # setup summary
        s = item.xpath('./description/text()')
        t['summary'] = s[0] if s else ""

        # check stream format, only allow m3u8 streams
        fmt = item.xpath('./media/streamformat/text()')
        fmt = fmt[0] if fmt else None
        if fmt.lower() != 'hls':
            # skip stream if not hls
            continue

        # setup stream URL
        t['url'] = item.xpath('./media/streamurl/text()')[0]
        c_list.append(t)

    for s in Util.ListSortedByKey(c_list, 'title'):
        oc.add(CreateVCO(
            title=s['title'], thumb=s['thumb'],
            summary=s['summary'], url=s['url'],
            ))

    return oc

####################################################################################################
@route(PREFIX + '/create-video-clipobject', include_container=bool)
def CreateVCO(title, thumb, url, summary=None, include_container=False, *args, **kwargs):

    vo = VideoClipObject(
        key=Callback(CreateVCO,
            title=title, thumb=thumb, url=url,
            summary=summary, include_container=True
            ),
        rating_key=url,
        title=title,
        thumb=thumb,
        summary=summary,
        year=int(Datetime.Now().year),  # set to current year
        source_title=TITLE,  # set to channel name
        content_rating='NR',
        items=GetMediaObject(url)
        )

    if include_container:
        return ObjectContainer(objects=[vo])
    return vo

####################################################################################################
def GetMediaObject(url):

    return [
        MediaObject(
            audio_channels=2,
            optimized_for_streaming=True,
            parts=[
                PartObject(
                    key=HTTPLiveStreamURL(Callback(PlayVideo, url=url))
                    )
                ]
            )
        ]

####################################################################################################
@indirect
@route(PREFIX + '/playvideo.m3u8')
def PlayVideo(url):

    return IndirectResponse(VideoClipObject, key=url)
