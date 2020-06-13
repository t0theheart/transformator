from app.app import ApplicationABC


class SumAscii(ApplicationABC):
    def _transform(self):
        self._data = str(sum([ord(char) for char in self._data]))
