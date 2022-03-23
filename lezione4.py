class CSVFile():

    def __init__(self, name):
        #Set name
        self.name = name

    def get_data(self):
        
        # Inizializzo una lista vuota per salvare i valori
        values = []
        # Apro e leggo il file, linea per linea
        my_file = open(self.name, 'r')
        for line in my_file:
             # Faccio lo split di ogni riga sulla virgola
             elements = line.split(',')
             #
             elements[-1] = elements[-1].strip()
             # Se NON sto processando l’intestazione... 
             if elements[0] != 'Date':
                 # Setto la data e il valore
                 #value = elements
                 # Aggiungo alla lista i valori stringa 
                 values.append(elements)
  
        my_file.close()
        return values
    
#file=CSVFile('shampoo_sales.csv')   
#print(file.get_data())

#print(CSVFile('shampoo_sales.csv').get_data())