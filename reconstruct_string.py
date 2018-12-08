import random
import argparse

class euler:

    def __init__(self,in_file_name,out_file_name):
        self.G={}
        self.file_name=in_file_name
        self.output_file=out_file_name
        self.__parse_input()
        self.node_list=[]
        self.final_string=""
        

    def __parse_input(self):
        lines=[line.rstrip('\n') for line in open(self.file_name)]
        for line in lines:
            nodes=line.split('\t')
            if nodes[0] not in self.G:
                self.G[nodes[0]]=[]
            if nodes[1] not in self.G:
                self.G[nodes[1]]=[]
            self.G[nodes[0]].append(nodes[1])

    def walk(self,node):
        while len(self.G[node])>0:
            destination=self.G[node].pop()
            self.walk(destination)
        self.node_list.append(node)

    def reconstruct(self):
        self.walk(next(iter(self.G)))
        self.node_list=self.node_list[::-1]
        self.final_string=E.node_list[0]+''.join(map(lambda x: x[-1],E.node_list[1:]))

    def dump_output(self):
        fw=open(self.output_file,'w')
        fw.write(self.final_string)
        fw.close()

  
def make_arg_parser():
    parser = argparse.ArgumentParser(prog='reconstruct_string.py', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("-i","--input",
                        default=argparse.SUPPRESS,
                        required=True,
                        help="Path to input edge file")    #Fasta file path


    parser.add_argument("-o","--output",
                        default=argparse.SUPPRESS,
                        required=True,
                        help="Path to output file")    #Fasta file path
    return parser
    

if __name__ == '__main__':
    parser = make_arg_parser()
    args = parser.parse_args()
    E=euler(args.input,args.output)
    #print(E.G)
    E.reconstruct()
    #print(E.final_string)
    E.dump_output()
