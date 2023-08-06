"""Extractor for lyrical-nonsense.com."""

import logging

from .. import utils
from ..extractor import LyricsExtractor
from ..models.lyrics import Lyrics
from ..utils import UrlData

log = logging.getLogger(__name__)


class LyricalNonsense(LyricsExtractor):
    """Class for extracting lyrics."""

    name = "Lyrical Nonsense"
    url = "http://www.lyrical-nonsense.com/"
    display_url = "lyrical-nonsense.com"

    @classmethod
    def extract_lyrics(cls, url_data: UrlData) -> Lyrics:
        """Extract lyrics."""
        bs = url_data.bs
        title_el = bs.select_one("span.titletext2new")
        if not title_el:
            title_el = bs.select_one("div.titlelyricblocknew h1")
        title = title_el.text

        artist = bs.select_one("div.artistcontainer span.artisttext2new")
        if not artist:
            artist = bs.select_one("div.artistcontainer h2")

        artist = artist.text

        lyrics_window = bs.select_one("div#Romaji div.olyrictext") or bs.select_one("div#Lyrics div.olyrictext")
        lyrics = utils.clean_lyrics(lyrics_window.text)
        print(lyrics)

        return Lyrics(title, lyrics, artist=artist)
