import argparse
import time
import os
import subprocess
from datetime import datetime
import shotgun_generator
import reconstruct_string
from percentage_error import percentage_error
import random_error




def make_arg_parser():
    parser = argparse.ArgumentParser(prog='driver.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-i","--input",
                        default=1,
                        required=True,
                        help="input dna sequence")

    parser.add_argument("-mk","--maxk",
                        default=1,
                        required=False,
                        help="maximum value of k")
    
    
    parser.add_argument("-rc","--runcount",
                        default=1,
                        required=False,
                        help="maximum length of substring")

    return parser

def parse_input(input_file_name):               #first line in the input file should be a label
    lines=[line.rstrip('\n') for line in open(input_file_name)]
    return (''.join(lines[1:]))[10000:-10000]   #first and last 10,000 are guard bits


if __name__ == '__main__':
    parser = make_arg_parser()
    args = parser.parse_args()


    rc=int(args.runcount)
    max_k=int(args.maxk)

    current_length=100

    input_string=parse_input(args.input)

    print("Process started at "+str(datetime.now().time()))

    while rc:
        k_min=int(current_length/20)
        k_max=int(current_length/10)
        for current_K in range(k_min,k_max+1):
            print("K: "+str(current_K)+" length:"+str(current_length))
            tf=open('performance_data.txt','a')
            start_time=time.time()
            dir_path="output/"+str(current_K)+"_"+str(current_length)+"/"

            command_string_py_1="python3 shotgun_generator.py -i chr1.fa -k "+str(current_K)+" -l "+str(current_length)
            command_string_R="Rscript kMerDeBruin.R "+dir_path[:-1]
            command_string_py_2="python3 reconstruct_string.py -i "+dir_path+"edge_list -o "+dir_path+"reconstructed.txt"

            subprocess.call(command_string_py_1, shell=True)
            subprocess.call(command_string_R, shell=True)
            subprocess.call(command_string_py_2, shell=True)

            end_time=time.time()

            reconstructed_string_file=dir_path+"reconstructed.txt"

            f=open(reconstructed_string_file,'r')
            lines=[line.rstrip('\n') for line in open(reconstructed_string_file)]

            tf.write("K:"+str(current_K)+"\t"+"len:"+str(current_length)+"\t"+"runtime:"+str(end_time-start_time)+"\t"+"error:"+str(percentage_error.calculate(input_string,lines[0]))+"\t"+"recon_len:"+str(len(lines[0]))+str("\n"))
            tf.close()
        current_length=current_length*2
        rc=rc-1

    print("Process ended at "+str(datetime.now().time()))






