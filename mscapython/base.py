
import os
import re
import glob


def hello():
	return "Hello World"

class salad():

    def __init__(self):
        self.path =""

	# input path, [tomato, lettuce], [2,3]
	# output
	# tomato_00.salad
	# tomato_01.salad
    def read(self, path, salad, n_items):
        assert len(salad) == len(n_items), "Length not match!"
        self.path = path
        for i in range(len(salad)):
            for j in range(n_items[i]):
                file_name = salad[i]+ "{:0>2}".format(j) +".salad"
                print(file_name)
                f = open(os.path.join(self.path, file_name),"w+")
                f.close()
                
    # read .salad file
	# return a dictionary with salad items & how many            
    def write(self,path):
        flrst = glob.glob(os.path.join(path,'*.salad'))
        dic = {}
        for file in flrst:
            pattern = ".salad"
            stripe_salad = os.path.splitext(file)[0]
            split = stripe_salad.split("/")
            value = str(split[len(split[0])-1])
            ingredient = re.sub(r'\d+', '', value)
            if ingredient not in dic.keys():
                dic[ingredient] =1
            else:
                dic[ingredient] +=1
        return dic
