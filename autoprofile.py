#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

# Ported Plugin

"""
✘ Commands Available -

• `{i}autoname`
   `Starts AUTONAME`.

• `{i}stopname`
   `Stops AUTONAME.`

• `{i}autobio`
   `Starts AUTOBIO.`

• `{i}stopbio`
   `Stops AUTOBIO.`
"""

import random

from telethon.tl.functions.account import UpdateProfileRequest

from . import *

CHANGE_TIME = int(udB.get_key("CHANGE_TIME")) if udB.get_key("CHANGE_TIME") else 60

RR7PP = udB.get_key("TI_EM") or "|"
BIO = udB.get_key("TI_BIO")

normzltext = "0123456789"
namerzfont = udB.get_key("TI_IT") or "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"

@ultroid_cmd(pattern="(auto|stop)name$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "stop":
        udB.del_key("AUTONAME")
        await event.eor("`• AUTONAME has been Stopped !`")
        return
    udB.set_key("AUTONAME", "True")
    await eod(event, "`• Started AUTONAME`")
    while True:
        getn = udB.get_key("AUTONAME")
        if not getn:
            return
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{HM} {RR7PP}"
        await event.client(UpdateProfileRequest(first_name=name))
        await asyncio.sleep(CHANGE_TIME)
        


@ultroid_cmd(pattern="(auto|stop)bio$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "stop":
        udB.del_key("AUTOBIO")
        await event.eor("`• AUTOBIO has been Stopped !`")
        return
    udB.set_key("AUTOBIO", "True")
    await eod(event, "`• Started AUTOBIO`")
    BIOS = [
        "Busy Today !",
        "ULTROID USER",
        "Enjoying Life!",
        "Unique as Always!" "Sprinkling a bit of magic",
        "Intelligent !",
    ]
    while True:
        getn = udB.get_key("AUTOBIO")
        if not getn:
            return
        BIOMSG = random.choice(BIOS)
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{HM} {RR7PP} {BIO}"
        await event.client(
            UpdateProfileRequest(
                about=name,
            )
        )
        await asyncio.sleep(CHANGE_TIME)
