from typing import List
from pvleopard import Leopard

class SubtitleGenerator:
    def __init__(self, endpoint_sec=1.0, length_limit=16):
        self.endpoint_sec = endpoint_sec
        self.length_limit = length_limit

    @staticmethod
    def second_to_timecode(x: float) -> str:
        hour, x = divmod(x, 3600)
        minute, x = divmod(x, 60)
        second, x = divmod(x, 1)
        millisecond = int(x * 1000.)
        return '%.2d:%.2d:%.2d,%.3d' % (hour, minute, second, millisecond)

    def to_srt(self, words):
        def _helper(end: int) -> None:
            lines.append("%d" % section)
            lines.append(
                "%s --> %s" %
                (
                    self.second_to_timecode(words[start].start_sec),
                    self.second_to_timecode(words[end].end_sec)
                )
            )
            lines.append(' '.join(x.word for x in words[start:(end + 1)]))
            lines.append('')

        lines = list()
        section = 0
        start = 0
        for k in range(1, len(words)):
            if ((words[k].start_sec - words[k - 1].end_sec) >= self.endpoint_sec) or \
                    (self.length_limit is not None and (k - start) >= self.length_limit):
                _helper(k - 1)
                start = k
                section += 1
        _helper(len(words) - 1)

        return '\n'.join(lines)
