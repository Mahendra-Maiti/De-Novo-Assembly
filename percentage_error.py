'''
        Author: Mahendra Maiti
'''
class percentage_error:
    @classmethod
    def calculate(cls,original_string,reconstructed_string):
        '''
            Compare index wise mismatch
        '''
        length=min(len(reconstructed_string),len(original_string))
        count=0
        print("length "+str(length))
        for i in range(length):
            if original_string[i]!=reconstructed_string[i]:
                count=count+1
        
        return float(count)/float(length)

