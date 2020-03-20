#Modified By Shobhit Sharma (ScriptKKiddie)
#Date Modified : March 21, 2020
#GitHub : https://www.github.com/ScriptKKiddie/LaneDetection
#Python Version : 3

import pstats
p = pstats.Stats('CodeProcessingStats')
# p.strip_dirs().sort_stats(-1).print_stats()


# Sort by cumulative time and print top 20 most expensive calls
p.sort_stats('cumulative').print_stats(50)
