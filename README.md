GreekTV.bundle
==============

This is a plugin that creates a new channel in [Plex Media Server](https://plex.tv) to view content from http://greektv.upg.gr
It is currently under development and as such, should be considered alpha software and potentially unstable.

> **Note:** the author of this plugin has no affiliation with http://greektv.upg.gr nor the owners of the content that they host.

## Features

- Watch Live Greek IPTV by UPG.GR

## Channel Support

##### Plex Media Server:
- Tested Working:
  - Ubuntu 14.04 LTS: PMS version 0.9.14.5

##### Plex Clients:
- Tested Working:
  - Android (KitKat 4.4.2)
  - Plex/Web (2.4.39) (Disable/Enable Direct play depending on stream)

## How To Install

- [Download](https://github.com/Twoure/GreakTV.bundle/archive/master.zip) and install it by following the Plex [instructions](https://support.plex.tv/hc/en-us/articles/201187656-How-do-I-manually-install-a-channel-) or the instructions below.
  - Unzip and rename the folder to "GreekTV.bundle"
  - Copy GreekTV.bundle into the PMS [Plug-ins](https://support.plex.tv/hc/en-us/articles/201106098-How-do-I-find-the-Plug-Ins-folder-) directory
  - ~~Restart PMS~~ **This is old, should not have to restart PMS.  If channel does not appear then Restart PMS**

## Issues

- Plex Web Client: Must disable Direct Play to make Crossdomain m3u8 streams work, but this breaks the other streams that don't depend on Crossdomains.
- Chromecast not working yet
- _Alpha TV_ has a 404 error.  Acess is denied to site.  Maybe it's a regional deal
- Some streams take some time to load

## Changelog

**1.0.0** - 12/20/15 - First push of local code
