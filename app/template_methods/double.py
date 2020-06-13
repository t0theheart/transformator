from app.app import ApplicationABC


class Double(ApplicationABC):
    def _transform(self):
        self._data = ''.join([char if char.isspace() else char+char for char in self._data])
