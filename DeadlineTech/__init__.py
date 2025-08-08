# Powered By Team DeadlineTech
from HARUKA_X_MUSIC.core.bot import Anony
from HARUKA_X_MUSIC.core.dir import dirr
from HARUKA_X_MUSIC.core.git import git
from HARUKA_X_MUSIC.core.userbot import Userbot
from HARUKA_X_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
