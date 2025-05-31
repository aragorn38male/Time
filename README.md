# Time

A small project that aims to prevent the destruction of the melatonine while very briefly watch the current hour in the dark night...
* Support Picture display behind clock
* Uses NTP with WIFI to get the current hour
* Commented-out: ability to check if there"s a network connection

For a darker effect, comment line 36 to hide the picture
&
Replace line 45 with:       text_area = label.Label(terminalio.FONT, text=text, color=0xFF0000)

( I personnaly use Sunton ESP32-2424S012 but that's not the better choice )
( This would definitely require an OLED display instead! )
