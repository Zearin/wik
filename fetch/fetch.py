import argparse
import info


parser = argparse.ArgumentParser()
parser.add_argument("-s","--search",help="Search any topic")
parser.add_argument("-i","--info",help="Get info on any topic(Use correct name)")
parser.add_argument("-q","--quick",help="Get the summary on any topic")

a = parser.parse_args()
def arguments():
    if a.search:
        info.searchInfo(a.search)
    if a.info:
        info.getInfo(a.info)
    if a.quick:
        info.getSummary(a.quick)

arguments()