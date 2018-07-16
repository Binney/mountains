import argparse
import sys
from .game import Game

parser = argparse.ArgumentParser()
parser.add_argument('--width', type=int)
parser.add_argument('--height', type=int)

sys.stderr.write("here we go!")
sys.stderr.flush()

Game(parser.parse_args()).run()
