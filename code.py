import time
import rtc
import board
import displayio
import wifi
import ipaddress
import socketpool
import adafruit_ntp
import terminalio
from adafruit_display_text import label, wrap_text_to_lines

display = board.DISPLAY

display.root_group = None

bitmap = displayio.OnDiskBitmap("/pic.bmp")

tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

group = displayio.Group()


# ping = wifi.radio.ping(ip=ipaddress.IPv4Address("192.168.68.1"))
# if ping is None:
#     print("Couldn't ping Server")
# else:
#     print(f"Connected to WiFi / Connected to WiFi")
#


pool = socketpool.SocketPool(wifi.radio)
ntp = adafruit_ntp.NTP(pool, tz_offset=2, cache_seconds=3600)
rtc.RTC().datetime = ntp.datetime

# (UN|COMMENT) TO (SHOW|HIDE) THE PICTURE
group.append(tile_grid)

while True:
    hour = f"{time.localtime().tm_hour:02}"
    min = f"{time.localtime().tm_min:02}"
    sec = f"{time.localtime().tm_sec:02}"

    text = hour+":"+min+":"+sec

    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, scale=4)
    text_area.x = 25
    text_area.y = 120

    group.append(text_area)
    display.root_group = group
    time.sleep(1)
    group.remove(text_area)
#     
