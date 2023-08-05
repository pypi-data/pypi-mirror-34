ultratransmission
==================

Automatically trigger torrents to download through transmission web client

Requirements:
sudo apt-get install libxml2-dev libxslt-dev

For those of you with a Linux server running the transmission-web UI for torrenting, this will allow you to automatically find torrents and start the download. Sometimes there's something you are waiting to get, but you don't want to sit around and wait for the torrent to pop up, so this solves that problem.

Example:
    
    # download up to 5 searched torrents within size limits, minimum seeders 100
    ultratransmission --min-size 400MB --max-size 2GB --seeders 100 --max-download 5 'some-show s01e05'

    # download file at least over 1GB (10 seeder min default, 1TB max size default)
    # check every 600 seconds, until at least 3 downloads are started
    ultratransmission -m 1GB -i 600 --max-download 3 'some-show s22e08'

That last one would be the most useful, because it would find the first few HD uploads of your show, and keep looking every ten minutes until the downloads are started.

```--host http://127.0.0.1:9090``` is the default for the transmission web host

Let me know if you find it useful, and have any feature requests or bugs!

