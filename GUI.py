import tkinter
from tkinter import *
from tkinter import ttk
CurrencyApp=tkinter.Tk()
CurrencyApp.title('Currency Converter')



CurrencyApp.geometry("600x400") 


Label(CurrencyApp, text='Enter Amount').grid(row=0,column=3) 
inputAmount=Entry(CurrencyApp)
inputAmount.grid(row=1,column=3)


Label(CurrencyApp, text='Currency').grid(row=0,column=15) 
n = tkinter.StringVar() 
presentCurrency = ttk.Combobox(CurrencyApp, width = 27, textvariable = n) 
  
# Adding combobox drop down list 
presentCurrency['values'] = ('Argentine Peso',
'Australian Dollar',
'Bahraini Dinar',
'Botswana Pula',
'Brazilian Real',
'British Pound',
'Bruneian Dollar',
'Bulgarian Lev',
'Canadian Dollar',
'Chilean Peso',
'Chinese Yuan Renminbi',
'Colombian Peso',
'Croatian Kuna',
'Czech Koruna',
'Danish Krone',
'Emirati Dirham',
'Euro',
'Hong Kong Dollar',
'Hungarian Forint',
'Icelandic Krona',
'Indonesian Rupiah',
'Iranian Ria',
'Israeli Shekel',
'Indian Rupee',
'Japanese Yen',
'Kazakhstani Tenge',
'Kuwaiti Dinar',
'Libyan Dinar',
'Malaysian Ringgit',
'Mauritian Rupee',
'Mexican Peso',
'Nepalese Rupee',
'New Zealand Dollar',
'Norwegian Krone',
'Omani Rial',
'Pakistani Rupee',	
'Philippine Peso',
'Polish Zloty',
'Qatari Riyal',
'Romanian New Leu',
'Russian Ruble',
'Saudi Arabian Riyal',
'Singapore Dollar',
'South African Rand',
'South Korean Won',
'Sri Lankan Rupee',
'Swedish Krona',
'Swiss Franc',
'Taiwan New Dollar',
'Thai Baht',
'Trinidadian Dollar',
'Turkish Lira',
'Venezuelan Bolivar') 
  
presentCurrency.grid(column = 15, row = 1) 
presentCurrency.current()
output=Entry(CurrencyApp,textvariable=str(float(inputAmount)*1.375246/74.550914)+" USD")
CurrencyApp.mainloop()


