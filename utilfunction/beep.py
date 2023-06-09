import winsound
import os
import platform


def beep(sec=1, freq=1000) -> None:
    """Make beep sound

    :param sec: beep duration, defaults to 1
    :type sec: int, optional
    :param freq: beep fequency, defaults to 1000
    :type freq: int, optional
    """

    sys = platform.system()

    if sys == "Windows":
        winsound.Beep(int(1000 * sec), freq)
    else:
        os.system("play -nq -t alsa synth {} sine {}".format(sec, freq))

    return None
