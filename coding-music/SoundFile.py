import simpleaudio as sa
class SoundFile:

    def __init__(self, path):
        self._path = path
        self._wave_obj = sa.WaveObject.from_wave_file(path)
        self._play_obj = None

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    def play(self):
        self._play_obj = self._wave_obj.play()

    def wait_done(self):
        if self._play_obj:
            self._play_obj.wait_done()
