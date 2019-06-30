from setuptools import setup

setup(
    name="ffmpeg_split",
    version="0.0.1",
    install_requires=["ffmpeg-python"],
    packages=['ffmpeg_split'],
    entry_points={
        'console_scripts': ['ffmpeg_split=ffmpeg_split.__main__:main'],
    }
)

