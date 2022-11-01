import argparse
import sys


class TreasureParser:
    def __init__(self):
        self.DEFAULT_INFILE = "treasure.in"
        self.testdata = []
        self.output = []

    def start(self):
        self.commandLineParser()
        self.fileParsing()
        self.runSolution()
        self.writeOutput()

    def commandLineParser(self):
        arg_parse = argparse.ArgumentParser(
            description="This program feeds the data from the test files"
            " to the student's solution and then outputs their result in"
            " a .out file.",
        )
        arg_parse.add_argument("-t",
                               "--testfile",
                               help="testfile(s) you want to run."
                               " Output is stored in a .out file with "
                               "the same name as input file",
                               required=False,
                               nargs="*"
                               )
        self.arguments = arg_parse.parse_args()
        if not self.arguments.testfile:
            self.arguments.testfile = [self.DEFAULT_INFILE]

    def fileParsing(self):

        for file in self.arguments.testfile:
            try:
                f = open(file, "r")
            except FileNotFoundError as err:
                print("[FileNotFoundError]: please enter a valid file")
                sys.exit(-1)

            temp = []
            for i in range(4):
                if i == 0 or i == 1:
                    temp.append(int(f.readline()))
                else:
                    temp.append([int(x)
                                for x in f.readline() if x.isnumeric()])

            self.testdata.append(temp)
            f.close()

    def runSolution(self):
        for data in self.testdata:
            self.output.append(self.treasureHunting(
                data[0], data[1], data[2], data[3]))

    def treasureHunting(self, g: int, n: int, locations: list[int], chests: list[int]) -> int:
        #######
        # write your solution here!
        #######
        return -1

    def writeOutput(self):
        for index, testfilename in enumerate(self.arguments.testfile):
            outname = testfilename.split(".")[0] + ".out"
            f = open(outname, "w")
            f.write(str(self.output[index]))
            f.close()


if __name__ == "__main__":
    tp = TreasureParser()
    tp.start()
