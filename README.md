GreekTV.bundle
==============

This is a plugin that creates a new channel in [Plex Media Server](https://plex.tv) to view content from http://greektv.upg.gr
The channels are fed from an xml file that is updated every 10 minutes. This makes sure that there are no dead channels at any time.

> **Note:** the author of this plugin has no affiliation with http://greektv.upg.gr nor the owners of the content that they host.

## Features

- Watch Live Greek IPTV by UPG.GR

## Channel Support

##### Plex Media Server:
- Tested Working:
  - Ubuntu 14.04 LTS: PMS version 1.2.7

##### Plex Clients:
- Tested Working:
  - Android (KitKat 4.4.2)
  - Plex/Web (2.10.11) _(Disable/Enable Direct play/stream depending on stream)_

## How To Install

Follow the [Adding, Removing, and Updating a Channel](https://support.plex.tv/hc/en-us/articles/201053758-Adding-Removing-and-Updating-a-Channel) instructions.

## Issues

- Plex Web Client: Must disable Direct Play/Stream to make Crossdomain `m3u8` streams work, but this breaks the other streams that don't depend on Crossdomains.
- Chromecast not working yet
- AlphaTV is blocked for the US and some other countries
- Some streams take some time to load
