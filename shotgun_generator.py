'''
        Author: Mahendra Maiti
'''
from random import randint
import argparse
import time

class shotgun:
    def __init__(self,input_string,K,output_file_name):
        self.input_string=input_string
        self.K=K
        self._substrings=[]
        self._generate_substrings()
        self._out_file_name=output_file_name
        self.counter=0


    def _generate_substrings(self):
        self._substrings.append(self.input_string[:self.K])
        self._substrings.append(self.input_string[-self.K:])

        current_end=self.K-1
        current_start=0
        total_length=len(self.input_string)
        self.counter=3
        while current_end < (total_length-self.K):
            print(self.counter)
            next_start=randint(current_start+1,current_end)
            self._substrings.append(self.input_string[next_start:next_start+self.K])
            current_start=next_start
            current_end=next_start+self.K-1
            self.counter=self.counter+1
    
    def get_substrings(self):
        return self._substrings
    

    def dump_substrings(self):
        fw=open('output/'+self._out_file_name,'w')
        for substring in self._substrings:
            fw.write(substring+"\n")
        fw.close()
        print("Wrote "+str(len(self._substrings))+" substrings")



def make_arg_parser():
    parser = argparse.ArgumentParser(prog='shotgun_generator.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("-i","--input",
                        default=argparse.SUPPRESS,
                        required=True,
                        help="Path to input string file")    #Fasta file path

    parser.add_argument("-k","--maxK",
                        default=argparse.SUPPRESS,
                        required=True,
                        help="Length of generated substrings K")  

    parser.add_argument("-o","--output",
                        default=argparse.SUPPRESS,
                        required=True,
                        help="Name of output file")

    parser.add_argument("-rc","--runcount",
                        default=1,
                        required=False,
                        help="Number of runs")

    return parser


def parse_input(input_file_name):               #first line in the input file should be a label
    lines=[line.rstrip('\n') for line in open(input_file_name)]
    return (''.join(lines[1:]))[10000:-10000]   #first and last 10,000 are guard bits


if __name__ == '__main__':
    parser = make_arg_parser()
    args = parser.parse_args()
    runcount=int(args.runcount)
    max_k=int(args.maxK)
    current_length=25
    input_string=parse_input(args.input)

    while runcount:
        for current_K in range(3,max_k+1):
            tf=open('timing.txt','a')
            start_time=time.time()
            SG=shotgun(input_string[:current_length],current_K,str(current_K)+"_"+str(current_length)+args.output)
            SG.dump_substrings()
            end_time=time.time()
            tf.write("K:"+str(current_K)+"\t"+"len:"+str(current_length)+"\t"+str(end_time-start_time)+"\n")
            tf.close()
        
        runcount=runcount-1
        current_length=current_length*2
