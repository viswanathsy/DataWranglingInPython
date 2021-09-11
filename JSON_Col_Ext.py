import json
import os


#definitions
path = #{your code path}
data_path = #{your file path}
write_path = #{your output path}

def json_parse(docContent,name,fname):
    l = []    
    for i in docContent:        
        if isinstance(docContent[i], dict):        
            for kk in json_parse(docContent[i],name+i+'/',''):
                l.append(kk)      
        elif isinstance(docContent[i], list):        
            if len(docContent[i])>1:
                #do a length check to see if the list is empty
                res = list_parse(docContent[i],name+i)
                if isinstance(res, str):
                    #return type when for list of strings or ints will be a string object.
                    #parsing it will result in each letter of the string to be added in new line
                    l.append(res)
                else:
                    for jj in list_parse(docContent[i],name+i): 
                        l.append(jj)
            else:
                #if empty list, append the name 
                l.append(name+i)
        else:
            l.append(name+i)
    return l

def list_parse(param1,list_name):
    for i in param1:
        if isinstance(i, dict):        
            #if the list is list of dicts
            return json_parse(i,list_name+'/','')
        elif (isinstance(i, str) or isinstance(i, int) ): 
            #if the list is a list of strings or integers
            return str(list_name)
        
json_files = [ x for x in os.listdir(data_path) if x.endswith("json") ]

for json_file in json_files:
    fname = json_file
    op_name = fname.replace('.json',"")
    f = open(data_path+json_file, "r")
    docContent = f.read()
    docContent = json.loads(docContent)
    keys = json_parse(docContent,'root/',fname);
    op_file = open(write_path+op_name+'.txt', 'w+', newline ='')       
    for element in keys:
     op_file.write(element)
     op_file.write('\n')
    op_file.close()       
