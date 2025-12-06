class pairelements:
    def twoSum(self,nums,targets):
        lookup={}
        
        for i,num in enumerate(nums):
            if targets- num in lookup:
                return (lookup[targets-num],i)
            lookup[num]=i
val=int(input('Enter the sum of search'))
print("index1=%d, index2=%d" ,pairelements().twoSum((10,20,30,40,50,60,70),val))