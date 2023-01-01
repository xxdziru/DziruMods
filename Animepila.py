#
#█▀▄ ▀█ █ █▀█ █░█  █▀▀ ▄▀█ █▄█
#█▄▀ █▄ █ █▀▄ █▄█  █▄█ █▀█ ░█░
# 🔒 Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html

# meta developer: @dziru
# meta pic: https://te.legra.ph/file/9e64a70c0a62c3bc472c6.jpg
# meta banner: https://te.legra.ph/file/9e64a70c0a62c3bc472c6.jpg
# scope: hikka_min 1.5.0
# scope: hikka_only
# version: 1.0

from .. import loader
import time

class PilaAnimeMod(loader.Module):
    """Человек бензопила, все серии через: @NarutoRuBot"""

    strings = {
        "name": "PilaAnime",
        "pila": "<b>◾️ Chainsaw Man ℹ️</b>"f"\n<b>◾️ Quality: <code>720-1080p</code></b>"f"\n🇷🇺<b> VoiceActing AniLibria</b>"f"\n\n<b>Watch the man chainsaw or back 🔽</b>"
        }
    strings_ru = {"pila": "<b>◾️ Человек-Бензопила ℹ️</b>"f"\n<b>◾️ Качество: <code>720-1080p</code></b>"f"\n🇷🇺<b> Озвучка AniLibria</b>"f"\n\n<b>Смотреть человек бензопила или назад 🔽</b>"}

    async def pila1cmd(self, message):
        """Человек бензопила 1"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "1 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')
    
    async def pila2cmd(self, message):
        """Человек бензопила 2"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "2 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')

    async def pila3cmd(self, message):
        """Человек бензопила 3"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "3 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')

    async def pila4cmd(self, message):
        """Человек бензопила 4"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "4 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')

    async def pila5cmd(self, message):
        """Человек бензопила 5"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "5 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')

    async def pila6cmd(self, message):
        """Человек бензопила 6"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "6 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')

    async def pila7cmd(self, message):
        """Человек бензопила 7"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "7 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')

    async def pila8cmd(self, message):
        """Человек бензопила 8"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "8 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')

    async def pila9cmd(self, message):
        """Человек бензопила 9"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "9 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')

    async def pila10cmd(self, message):
        """Человек бензопила 10"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "10 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')

    async def pila11cmd(self, message):
        """Человек бензопила 11"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "11 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')

    async def pila12cmd(self, message):
        """Человек бензопила 12"""
        anime = "/anime"
        pila = "Человек-Бензопила"
        part = "12 Серия🪚"
        async with self._client.conversation('@narutorubot') as bot:
            act = []
            act += [await bot.send_message(anime)]
            act += [await bot.send_message(pila)]
            time.sleep(0.5)
            act += [await bot.send_message(part)]
            work = await bot.get_response()
        await self._client.send_file(message.peer_id, work.media, caption=self.strings("pila"), reply_to=message.reply_to_msg_id,)
        await self.client.delete_dialog('@narutorubot')
