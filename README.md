GreekTV
=======

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/39760c54cc4d4a338140663f1f750d8b)](https://www.codacy.com/app/twoure/GreekTV-bundle?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Twoure/GreekTV.bundle&amp;utm_campaign=Badge_Grade) [![GitHub issues](https://img.shields.io/github/issues/Twoure/GreekTV.bundle.svg?style=flat)](https://github.com/Twoure/GreekTV.bundle/issues) [![](https://img.shields.io/github/release/Twoure/GreekTV.bundle.svg?style=flat)](https://github.com/Twoure/GreekTV.bundle/releases)

This plugin creates a new channel within [Plex Media Server](https://plex.tv) to view content from http://greektv.upg.gr
The channels are fed from an xml file that is updated every 10 minutes. This makes sure that there are no dead channels at any time.

> **Note:** the author of this plugin has no affiliation with http://greektv.upg.gr nor the owners of the content that they host.

## Features

- Watch Live Greek IPTV by UPG.GR

## [Changelog](Changelog.md#changelog)

## Channel Support

##### Plex Media Server:
- Tested Working:
  - Ubuntu 14.04 LTS: PMS version 1.2.3

##### Plex Clients:
- Tested Working:
  - Android (KitKat 4.4.2)
  - Plex/Web (2.10.7) (Disable/Enable Direct play depending on stream)

## How To Install

- Download the latest [![](https://img.shields.io/github/release/Twoure/GreekTV.bundle.svg?style=flat)](https://github.com/Twoure/GreekTV.bundle/releases) and install **GreekTV** by following the Plex [instructions](https://support.plex.tv/hc/en-us/articles/201187656-How-do-I-manually-install-a-channel-) or the instructions below.
  - Unzip and rename the folder to **GreekTV.bundle**
  - Copy **GreekTV.bundle** into the PMS [Plug-ins](https://support.plex.tv/hc/en-us/articles/201106098-How-do-I-find-the-Plug-Ins-folder-) directory
  - Unix based platforms need to `chown plex:plex -R GreekTV.bundle` after moving it into the [Plug-ins](https://support.plex.tv/hc/en-us/articles/201106098-How-do-I-find-the-Plug-Ins-folder-) directory _(`user:group` may differ by platform)_
  - Restart PMS

## Issues

- Plex Web Client: Must disable Direct Play to make Crossdomain m3u8 streams work, but this breaks the other streams that don't depend on Crossdomains.
- Chromecast not working yet
- AlphaTV is blocked for the US and some other countries
- Some streams take some time to load
