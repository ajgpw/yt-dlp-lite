# flake8: noqa: F401
from ._base import YoutubeBaseInfoExtractor
from ._video import YoutubeIE

# Hack to allow plugin overrides work
for _cls in [
    YoutubeBaseInfoExtractor,
    YoutubeIE,
]:
    _cls.__module__ = 'yt_dlp.extractor.youtube'
