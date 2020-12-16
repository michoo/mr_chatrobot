import subprocess
import platform


def tts_linux(message):
    subprocess.call(["espeak", message])
    return


def tts_mac(message):
    subprocess.call(["say", message])
    return


def tts(message):
    os = platform.system()
    if (os == "Linux"):
        tts_linux(message)
    elif (os == "Darwin"):
        tts_mac(message)
    else:
        print("Why d0 y0u us£ windoz? seri*usly...")
    return
