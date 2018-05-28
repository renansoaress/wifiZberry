# -*- coding: utf-8 -*-
import subprocess

from wifi import Cell

class WifiZberry(object):
    def __init__(self):
        self._wifis = Cell()
        self._list_wifi = []

    def scan(self):
        try:
            wifis = self._wifis.all('wlan0')
        except:
            wifis = self._wifis.all('wlp2s0')

        for wifi in wifis:
            self._list_wifi.append(wifi.ssid)
        return self._list_wifi

    def connect(self, user, password):
        file = open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w')
        file.write('login:{} senha:{}'.format(user,password))
        file.close()
        #sudo systemctl daemon-reload
        #sudo systemctl restart dhcpcd
        subprocess.call(['systemctl', 'daemon-reload'])
        subprocess.call(['systemctl', 'restart', 'dhcpcd'])
        print('executo tudo certim')

#/etc/wpa_supplicant/wpa_supplicant.conf
