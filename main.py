#
#  main.py
#  6nimmt
#
#  Created by Lennart Doppenschmitt on 2016-08-06.
#  Copyright 2016 Researchnix. All rights reserved.
#

import os
import time
import GameMaster
import Evaluation

if __name__ == "__main__":
    t = time.time()

    format_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
    filename = os.path.join("results", "{}.txt".format(format_time))

    master = GameMaster.GameMaster(filename)
    master.playGames(10000, verbose=False)

    eva = Evaluation.Evaluation()
    eva.loadData(filename)
    print "\n\nDone in " + str(time.time() - t) + " s"
    eva.showData(showPlot=True)
