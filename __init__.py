#Contador de palabras
""" Crear un script que tome un texto como entrada del usuario para el nombre de un archivo, se itera el archivo y retorne la cantidad de veces que aparece cada palabra (o texto separado por espacio) del archivo. Debería usar listas, diccionarios, ciclos, funciones, try/except.

Ejemplo: 
Ingresa el nombre del archivo: mbox.txt

Resultado: {'From': 500, 'Received': 200, ....}"""

import re as regex
import sys
import operator
import os

files = ["info.txt", "ML.txt", "ANS.txt"]


"""____________________________FUNCTIONS______________________________"""

def get_file_name():
   
    while True:
    
        try:
                
                print("Files available:\n ")
                for ele in files: print(ele)
                
                print("\n") 
                _file = input("Type de file name: ")
                print("\n") 
                
                
                for item_file in files: 
                    if item_file == _file: 
                        if os.stat(item_file).st_size != 0:
                            return item_file
                
                print("File Unknown or empty, try again...")
                print("\n")
                      
        except:
            print("File Unknown, try again...")
        
        
    
def read_file(file):
   #Returns a list
   while True:
        try:
            list_words = []
            with open(file) as my_file:
            
                
                for line in my_file:
                    
                    words = regex.findall(r"\S+", line)
                    list_words += words 
    
                return list_words
                        
        except:
            sys.exit("Error: This file can't be reader.") 
        


def counter_words(_list):
    
    list_counter = []
    
    while True:
        try:
            
            if len(_list) > 0:
                
                for item in _list:
                    
                    list_counter.append(_list.count(item))
                    
            else:
                print("This file is empty, try with other one")
                print("\n")
                
                
        except:
            print("This file is empty")
            
        else:
            return dict(list(zip(_list, list_counter)))
        
        

def dict_sort(dictionary):
    
    # print (dict(sorted(dictionary.items())))
    
    words_sort = dict(sorted(dictionary.items(), key = operator.itemgetter(1), reverse = True))
    print("\n")
    return words_sort
    

def print_list(_list):
    print (_list)


"""___________________________START__________________________________"""

file_name = get_file_name()  
list_words = read_file(file_name)
_dictionary = counter_words(list_words)
new_words_sort =dict_sort(_dictionary)
print_list(new_words_sort)