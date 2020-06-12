from app.app import Application


class SumAscii(Application):
    def _transform(self):
        self._data = str(sum([ord(char) for char in self._data]))
