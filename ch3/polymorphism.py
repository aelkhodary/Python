import abc

"""
Creating an abstract base class
"""
class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass
    @abc.abstractproperty
    def ext(self):
        pass
    """ It essentially says that the method can be called on a class instead of an instantiated object """
    @classmethod
    def __subclasshook__(cls, C):
        """ Is the class C a subclass of this class? """
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True

        return NotImplemented

class AudioFile(MediaLoader):
    def __init__(self,filename) :
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext= "mp3"
    def play(self):
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext= "wav"
    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext= "ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename))


if __name__=="__main__":
      "playing myFile.mp3 as mp3"
      file =MP3File("myFile.mp3")
      file.play()
      "playing myFile.wav as wav"
      file = WavFile("myFile.wav")
      file.play()
      "playing myFile.ogg as ogg"
      file = OggFile("myFile.ogg")
      file.play()

