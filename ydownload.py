#!/usr/bin/python3

from pytube import YouTube
import sys

YouTube(sys.argv[1]).streams.first().download('Videos')
