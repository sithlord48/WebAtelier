## Atelier
[![Build Status](https://travis-ci.org/lays147/WebAtelier.svg?branch=master)](https://travis-ci.org/lays147/WebAtelier)
[![Code Health](https://landscape.io/github/lays147/WebAtelier/master/landscape.svg?style=flat)](https://landscape.io/github/lays147/WebAtelier/master)
<br/>
--
This is the website for [Atelier](https://atelier.kde.org), the printer host of 3DPrinting from KDE Community.
<br/>
--
License: GPLV3

## Powered by:
- Python
- Flask
- Bootstrap

## Deploy:
Create a virtualenv environment for this application and then:

```bash
$ git clone https://github.com/lays147/WebAtelier.git
$ cd WebAtelier
$ tox -e wheel
$ cd dist
$ pip install atelier.whl
```

Run with SystemD

```bash
$ sudo vi /etc/systemd/system/atelier.service
$ sudo chmod 664 /etc/systemd/system/atelier.service
```

Include on the file the following setup:

```
[Unit]
Description=Atelier Website Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/virtualenv/bin/atelier --port 8000

[Install]
WantedBy=multi-user.target
```
Now, you can start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable atelier.service
sudo systemctl start atelier.service
```
### More:
- [Telegram](https://t.me/KDEAtelier)
- #kde-atelier on freenode IRC
