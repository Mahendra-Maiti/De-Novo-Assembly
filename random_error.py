import argparse
import random
def make_arg_parser():
    parser = argparse.ArgumentParser(prog='random_error.py',

                          formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i","--seq",
                      default=argparse.SUPPRESS,
                      required=True,
                      help="Path to seq1 fasta [required]")
    return parser

# Parse the input file to get the sequence
def parse(filename):
    result = ""
    lines=[line.rstrip('\n') for line in open(filename)]
    for l in lines[1:]:
        if (l[0] == 'N'):
            continue
        else:
            result = result+l
    n = len(result)
    i = n-1
    while(result[i] == 'N'):
        i = i-1
    result = result[0:i+1]
    return result

def randomize(result):
    n = len(result)
    print(n)
    i = 1
    while(i < n-100):
        randInt = random.randint(i,i+99)
        if (result[randInt-1] == 'a' or result[randInt-1] == 'A'):
            randList = ['C','c','G','g','T','t']
            index = random.randint(0,5)
            # if randInt > 1:
            #     result = result[0:randInt-2] + randList[index] + result[randInt:]
            # else:
            #     result = randList[index] + result[randInt:]
            result[randInt-1] = randList[index]
        elif (result[randInt-1] == 'a' or result[randInt-1] == 'A'):
            randList = ['C','c','G','g','T','t']
            index = random.randint(0,5)
            # if randInt > 1:
            #     result = result[0:randInt-2] + randList[index] + result[randInt:]
            # else:
            #     result = randList[index] + result[randInt:]
            result[randInt-1] = randList[index]
        elif (result[randInt-1] == 'a' or result[randInt-1] == 'A'):
            randList = ['C','c','G','g','T','t']
            index = random.randint(0,5)
            # if randInt > 1:
            #     result = result[0:randInt-2] + randList[index] + result[randInt:]
            # else:
            #     result = randList[index] + result[randInt:]
            result[randInt-1] = randList[index]
        else:
            randList = ['C','c','G','g','T','t']
            index = random.randint(0,5)
            # if randInt > 1:
            #     result = result[0:randInt-2] + randList[index] + result[randInt:]
            # else:
            #     result = randList[index] + result[randInt:]
            result[randInt-1] = randList[index]
        i = i+100
    finalString = "".join(result)
    print(len(finalString))
    f = open("output.fa","w")
    f.write(finalString)
    f.close()
    # print(result)
if __name__ == '__main__':
    parser = make_arg_parser()
    args = parser.parse_args()
    result = parse(args.seq)
    # print(result)
    res = list(result)
    randomize(res)
