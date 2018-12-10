class percentage_error:
    @classmethod
    def calculate(cls,original_string,reconstructed_string):
        length=len(reconstructed_string)
        count=0
        print("length "+str(length))
        for i in range(length):
            if original_string[i]!=reconstructed_string[i]:
                count=count+1
        
        return float(length-count)/float(length)

