# -*- coding: utf-8 -*-

#kaanYENİYOL

import utils
from _winreg import *
import time


while True:
    list = []

    usbstor = "SYSTEM\CurrentControlSet\Enum\USBSTOR"
    with OpenKey(HKEY_LOCAL_MACHINE, usbstor) as usb_key:
            toplam_usb = QueryInfoKey(usb_key)[0]
            for device in range(0, toplam_usb):
                key_ad = EnumKey(usb_key, device)
                with OpenKeyEx(usb_key, key_ad) as sub_key_ad:
                        for i in range(0, QueryInfoKey(sub_key_ad)[0]):
                            list.append("{0}\\{1}\\{2}".format(usbstor, key_ad, EnumKey(sub_key_ad, i)))


    for x in range(len(list)):
        key = OpenKey(HKEY_LOCAL_MACHINE, list[x])
        print("USB delil konumu: "),
        print(list[x])
        c = QueryValueEx(key, "FriendlyName") #varsayilan deger ise " " ekle
        print("                   USB NAME: {} ".format(c[0])),
        d = QueryValueEx(key, "ContainerID") #varsayilan deger ise " " ekle
        print("ID: {} ".format(d[0]))
        print("--------------------------------------------------------------------------------------------------------------------------------------|")
    time.sleep(10)
    print( "\n")
    print("Liste Guncelleniyor")
    print( "\n")
