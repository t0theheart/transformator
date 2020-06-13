from app.app import ApplicationABC


class Split(ApplicationABC):
    def _transform(self):
        self._data = '-'.join([char for char in self._data.replace(' ', '')])
