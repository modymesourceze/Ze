import sys, asyncio
import mody
from mody import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import zeub
from .utils import mybot, autoname, autovars, saves
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup

LOGS = logging.getLogger("Mody")
cmdhr = Config.COMMAND_HAND_LER

print(mody.__copyright__)
print(f"المرخصة بموجب شروط  {mody.__license__}")

cmdhr = Config.COMMAND_HAND_LER

try: #Code by T.me/D_S_I
    LOGS.info("⌭ جـارِ تحميـل الملحقـات ⌭")
    zeub.loop.run_until_complete(autovars())
    LOGS.info("✓ تـم تحميـل الملحقـات .. بنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")

if not Config.ALIVE_NAME:
    try: #Code by T.me/D_S_I
        LOGS.info("⌭ بـدء إضافة الاسـم التلقـائـي ⌭")
        zeub.loop.run_until_complete(autoname())
        LOGS.info("✓ تـم إضافة فار الاسـم .. بـنجـاح ✓")
    except Exception as e:
        LOGS.error(f"- {e}")

try:
    LOGS.info("⌭ بـدء تنزيـل زد إي ⌭")
    zeub.loop.run_until_complete(setup_bot())
    LOGS.info("✓ تـم تنزيـل زد إي .. بـنجـاح ✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()

class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()

try:
    LOGS.info("⌭ بـدء إنشـاء البـوت التلقـائـي ⌭")
    zeub.loop.run_until_complete(mybot())
    LOGS.info("✓ تـم إنشـاء البـوت .. بـنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")

try:
    LOGS.info("⌭ جـارِ تفعيـل الاشتـراك ⌭")
    zeub.loop.create_task(saves())
    LOGS.info("✓ تـم تفعيـل الاشتـراك .. بنجـاح ✓")
except Exception as e:
    LOGS.error(f"- {e}")


async def startup_process():
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    LOGS.info(f"⌔ تـم تنصيـب زد إي . . بنجـاح ✓ \n⌔ لـ إظهـار الاوامـر ارسـل (.الاوامر)")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    return


zeub.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    zeub.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        zeub.run_until_disconnected()
    except ConnectionError:
        pass
