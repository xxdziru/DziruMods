#
#█▀▄ ▀█ █ █▀█ █░█  █▀▀ ▄▀█ █▄█
#█▄▀ █▄ █ █▀▄ █▄█  █▄█ █▀█ ░█░
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @dziru
# meta pic: https://te.legra.ph/file/7b212d1e56ecdb67c787e.jpg
# meta banner: https://te.legra.ph/file/7b212d1e56ecdb67c787e.jpg
# scope: hikka_min 1.5.0
# scope: hikka_only
# version: 1.0

from .. import utils, loader

@loader.tds
class LogoMakerMod(loader.Module):
    """Logo maker, works through @DziruLogoBot"""

    strings = {
        "name": "LogoMaker",
        "dwait": "<emoji document_id=5283042475408106112>🙏</emoji> <b>Just wait!</b>",
        "denterargs": "<emoji document_id=5276516294076669922>⛔️</emoji> <b>Wrong argument!</b>",
        "dsaved": "<emoji document_id=5240446815127477236>😎</emoji> <b>Submitted successfully!</b>",
        }
    
    strings_ru = {
        "dwait": "<emoji document_id=5283042475408106112>🙏</emoji> <b>Просто подождите!</b>",
        "denterargs": "<emoji document_id=5276516294076669922>⛔️</emoji> <b>Неправильный аргумент!</b>",
        "dsaved": "<emoji document_id=5240446815127477236>😎</emoji> <b>Отправлено успешно!</b>",
        }
    
    strings_uz = {
        "dwait": "<emoji document_id=5283042475408106112>🙏</emoji> <b>Shunchaki kuting!</b>",
        "denterargs": "<emoji document_id=5276516294076669922>⛔️</emoji> <b>Noto'g'ri argument!</b>",
        "dsaved": "<emoji document_id=5240446815127477236>😎</emoji> <b>Muvaffaqiyatli yuborildi!</b>",
        }
    
    strings_de = {
        "dwait": "<emoji document_id=5283042475408106112>🙏</emoji> <b>Warte einfach!</b>",
        "denterargs": "<emoji document_id=5276516294076669922>⛔️</emoji> <b>Falsche Argumentation!</b>",
        "dsaved": "<emoji document_id=5240446815127477236>😎</emoji> <b>Erfolgreich gesendet</b></b>",      
    }

    strings_jp = {
        "dwait": "<emoji document_id=5283042475408106112>🙏</emoji> <b>ちょっと待って!</b>",
        "denterargs": "<emoji document_id=5276516294076669922>⛔️</emoji> <b>間違った議論!</b>",
        "dsaved": "<emoji document_id=5240446815127477236>😎</emoji> <b>正常に送信されました!</b></b>",      
    }

    strings_tr = {
        "dwait": "<emoji document_id=5283042475408106112>🙏</emoji> <b>Sadece bekle!</b>",
        "denterargs": "<emoji document_id=5276516294076669922>⛔️</emoji> <b>Yanlış argüman!</b>",
        "dsaved": "<emoji document_id=5240446815127477236>😎</emoji> <b>Başariyla gönderildi!</b></b>",      
    }

    async def logocmd(self, message):
        """your nickname"""
        args = utils.get_args_raw(message)
        start = '/start'
        get = '📸 Avatarka tayyorlash'
        if not args:
            await utils.answer(message, self.strings("denterargs", message))
            return
        message = await utils.answer(message, self.strings("dwait"))
        async with self._client.conversation('@dzirulogobot') as bot:
            act = []
            act += [await bot.send_message(start)]
            act += [await bot.send_message(get)]
            ignore = await bot.get_response()
            act += [await bot.send_message(args)]
            secignore = await bot.get_response()
            work = await bot.get_response()
        await message.delete()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("dsaved"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@dzirulogobot')