import ffmpy
import os


BITRATE = 128
GLOBAL_OPTIONS = ('-v warning', '-hide_banner', '-stats')

def download_opus(url: str, filename: str) -> str:
    output_filename = f'opus/{filename}.opus'
    to_opus = ffmpy.FFmpeg(
        global_options=GLOBAL_OPTIONS,
        inputs={url: None},
        outputs={output_filename: f'-y -c:a libopus -b:a {BITRATE}k'}
    )
    to_opus.run()
    return output_filename


def opus2mp3(input_filename: str, remove_soure: bool = True) -> str:
    output_filename = input_filename.replace("opus", "mp3")
    to_mp3 = ffmpy.FFmpeg(
        global_options=GLOBAL_OPTIONS,
        inputs={input_filename: None},
        outputs={output_filename: f'-y -b:a {BITRATE}k'}
    )
    to_mp3.run()
    if remove_soure:
        os.remove(input_filename)
    return output_filename