# • Made by @e3ris for Ultroid •
# • https://github.com/TeamUltroid/Ultroid •
# • inspiration and credit: https://github.com/code-rgb/USERGE-X/blob/alpha/userge/plugins/fun/stylish.py

"""
? **Get Fonts Inline**
  •• `{i}ifont <text>`

• Use the try again button afterwards.
"""

import os
import string
from random import shuffle

from telethon import events, Button

from . import *


FONTS = None
NORMAL = string.ascii_uppercase + string.ascii_lowercase

async def getfont(bot):
    m = await bot.get_messages("e3ris_db", ids=6274)
    dls = await m.download_media()
    with open(dls, "r") as f:
        data = f.read()
    # https://stackoverflow.com/a/52454984
    # for little bit of randomness ??
    font = list(eval(data).items())
    shuffle(font)
    os.remove(dls)
    return dict(font)


@ultroid_cmd(pattern="ifont ?(.*)")
async def ifontgen(e):
    args = e.pattern_match.group(1)
    reply = await e.get_reply_message()
    if not args and not (reply and reply.text):
        await eod(e, "Gimme some text sar!")
        return
    eris = await eor(e, "`...`")
    text_ = args if args else reply.text
    clickme = await e.client.inline_query(
        asst.me.username,
        f"font {text_}",
        entity=e.chat_id,
    )
    try:
        await clickme[0].click(
            silent=True,
            reply_to=e.reply_to_msg_id,
        )
        await eris.delete()
    except Exception as ex:
        await eris.edit(f"`#ERROR: {ex}`")
        return


@in_pattern("font", owner=True)
async def inline_fontgen(e):
    try:
        input_ = e.text.split(maxsplit=1)[1]
    except Exception:
        await e.answer(
            list(),
            switch_pm="Okay, Now type some text master ????",
            switch_pm_param="start",
        )
        return

    global FONTS
    # maybe caching to Remdis would be better ???
    if FONTS is None:
        FONTS = await getfont(e.client)

    fontslist = list(FONTS.keys())
    off_set = int(e.query.offset) if e.query.offset else 0
    _max = (off_set + 25) if len(fontslist) > (off_set + 25) else len(fontslist)
    sky, new_fnt = list(), ""

    for i in range(off_set, _max):
        new_fnt = ""
        for char in input_:
            new_fnt += FONTS[fontslist[i]][NORMAL.find(char)] if char in NORMAL else char
        sky.append(e.builder.article(
            title=new_fnt,
            text=new_fnt,
            description=f"Font Name: {fontslist[i]}\nCount: {i + 1}",
            buttons=Button.switch_inline("try again", query=str(e.text), same_peer=True),
        ))

    await e.answer(sky, next_offset=str(off_set + 25))