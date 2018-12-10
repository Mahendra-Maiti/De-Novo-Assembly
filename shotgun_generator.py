'''
        Author: Mahendra Maiti
'''
from random import randint
import argparse
import time
import os

class shotgun:
    def __init__(self,input_string,K,output_dir_name):
        self.input_string=input_string
        self.K=K
        self._substrings=[]
        self._generate_substrings()
        self.output_directory="output/"+output_dir_name
        self._out_file_name="Substrings.txt"
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
        os.mkdir(self.output_directory)
        fw=open(self.output_directory+"/"+self._out_file_name,'w')
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

    parser.add_argument("-k","--k",
                        default=argparse.SUPPRESS,
                        required=True,
                        help="Length of generated substrings K")  


    parser.add_argument("-l","--length",
                        default=1,
                        required=False,
                        help="length of substring")

    return parser


def parse_input(input_file_name):               #first line in the input file should be a label
    lines=[line.rstrip('\n') for line in open(input_file_name)]
    return (''.join(lines[1:]))[10000:-10000]   #first and last 10,000 are guard bits


if __name__ == '__main__':
    parser = make_arg_parser()
    args = parser.parse_args()
    input_string=parse_input(args.input)
    current_length=int(args.length)
    
    SG=shotgun(input_string[:current_length],int(args.k),args.k+"_"+str(current_length))
    SG.dump_substrings()
    




