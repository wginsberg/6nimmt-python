#
#  main.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

import argparse
import os
import time
import GameMaster
import Evaluation

DEFAULT_ITERATIONS = 10000


def main(iterations=DEFAULT_ITERATIONS, verbose=False, showPlot=False):
    t = time.time()

    formatTime = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
    if not os.path.exists("results"):
        os.makedirs("results")
    filename = os.path.join("results", "{}.txt".format(formatTime))

    master = GameMaster.GameMaster(filename)
    master.playGames(iterations, verbose)

    eva = Evaluation.Evaluation()
    eva.loadData(filename)
    print "Done in " + str(time.time() - t) + " s"
    eva.showData(showPlot)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v",
                        "--verbose",
                        action="store_true",
                        dest="verbose",
                        default=False,
                        help="Print out the result of each game")
    parser.add_argument("-s",
                        "--show-plot",
                        action="store_true",
                        dest="showPlot",
                        default=False,
                        help="Display the result plot immediately after finishing execution \
                        (program will not end until you close the window)")
    parser.add_argument('iterations',
                        metavar='N',
                        type=int,
                        nargs='?',
                        default=DEFAULT_ITERATIONS,
                        help="The number of games to play")

    args = parser.parse_args()
    main(**vars(args))
