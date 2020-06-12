from app.app import Application


class Split(Application):
    def _transform(self):
        self._data = '-'.join([char for char in self._data.replace(' ', '')])
