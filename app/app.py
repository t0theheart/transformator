from abc import ABC, abstractmethod


class Application(ABC):
    def __init__(self, read_from: str, write_to: str):
        self._read_from = read_from
        self._write_to = write_to
        self._data: str = ''

    @abstractmethod
    def _transform(self): pass

    def _read(self):
        with open(self._read_from, 'r') as f:
            self._data = f.readline()

    def _write(self):
        with open(self._write_to, 'w') as f:
            f.write(self._data)

    def run(self):
        self._read()
        self._transform()
        self._write()
