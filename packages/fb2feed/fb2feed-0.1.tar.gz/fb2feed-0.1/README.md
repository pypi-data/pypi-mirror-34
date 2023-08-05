Fb2Feed
==========

Fb2Feed transforms public Facebook pages to Atom feeds.

Installation
------------

1. Install dependencies:

        $ pip3 install --user -r requirements.txt
        
2. Configure:

        $ cp fb2feed.example.ini ~/.config/
        $ vi ~/.config/fb2feed.ini
        
3. Run:

        $ python3 fb2feed.py
        
4. Setup a crontab or systemd timer unit:

        $ # Edit systemd/fb2feed.service at your convenience.
        $ sudo cp systemd/* /etc/systemd/system/
        $ sudo systemctl enable /etc/systemd/system/fb2feed.service
        $ sudo systemctl start /etc/systemd/system/fb2feed.service

5. Point your feed reader to the url of the configured feeds
6. Profit

Contact
-------

I usually hang out on Freenode IRC, in \#gstreamer using the philn
nickname. Feel free to also reach out by mail (check git logs to find my
address).
