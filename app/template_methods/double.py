from app.app import Application


class Double(Application):
    def _transform(self):
        self._data = ''.join([char if char.isspace() else char+char for char in self._data])
