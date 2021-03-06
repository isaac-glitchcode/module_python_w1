#Contador de palabras
""" Crear un script que tome un texto como entrada del usuario para el nombre de un archivo, se itera el archivo y retorne la cantidad de veces que aparece cada palabra (o texto separado por espacio) del archivo. Debería usar listas, diccionarios, ciclos, funciones, try/except.

Ejemplo: 
Ingresa el nombre del archivo: mbox.txt

Resultado: {'From': 500, 'Received': 200, ....}"""

import re as regex
import sys
import operator
import os

files = ["info.txt", "ML.txt"]


"""____________________________FUNCTIONS______________________________"""

def get_file_name():
    
    while True:
        
        try: 
             
            print("Available files:\n ")
            for ele in files: print(ele)
            
            print("\n") 
            _file = input("Type file name: ")
            print("\n") 
            
            for item_file in files: 
                
                if item_file == _file:
                     
                    if os.stat(item_file).st_size != 0: return item_file
            
            print("Unknown or empty file, try again...\n")
                      
        except:
            
            print("Unknown or empty file, try again...\n")
        
        
    
def read_file(file):
    
   while True:
       
        try:
            
            list_words = []
            list_counter = []
            
            with open(file) as my_file:
                
                for line in my_file:
                    
                    words = regex.findall(r"\S+", line)
                    list_words += words
                    
                list_counter = list(map(lambda item : list_words.count(item), list_words))
                    
            dict_words = dict(list(zip(list_words, list_counter)))  
            words_sort = dict(sorted(dict_words.items(), key = operator.itemgetter(1), reverse = True))
            
            return words_sort
          
        except:
            
            sys.exit("Error: This file cannot be read.") 


"""___________________________START__________________________________"""

file_name = get_file_name()  
print(read_file(file_name))
