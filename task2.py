########## import required module ##############
from tkinter import *
from tkinter import ttk, messagebox
import requests

API_KEY = 'ff8f2979acedb702a64ada8b'
url = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'
response = (requests.get(f'{url}')).json()

currencies = dict(response['conversion_rates'])


def convert_currency():
    try:
        source = from_currency_combo.get()
        destination = to_currency_combo.get()
        amount = entry.get()
        result = requests.get(f'https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{source}/{destination}/{amount}').json()
        converted_res = result['conversion_result']

        formatted_res = f' {amount} {source} = {converted_res} {destination} '
        resultLabel.config(text=formatted_res)

    except Exception as e:
        messagebox.showerror('Info', 'Try again')


window = Tk()
window.geometry('280x350')
window.title('Currency Converter')
# window.wm_iconbitmap()
window.resizable(height=FALSE, width=FALSE)


############# Top Frame ###########
top_frame = Frame(window, bg='#081F4D', width=280,  height=70)
top_frame.grid(row=0, column=0)

name_Label = Label(top_frame, text='Currency Converter', padx=50, justify=CENTER, pady=20,  bg='#081F4D',
                   fg='white', font='Poppins 15 bold')
name_Label.grid(row=0, column=0)


########### Bottom Frame ############
bottom_frame = Frame(window, width=280, height=300)
bottom_frame.grid(row=1, column=0)

entryLabel = Label(bottom_frame, text='Amount: ', font='Poppins 12 bold')
entryLabel.place(x=15, y=18)
entry = Entry(bottom_frame, width=26, font='Poppins 12 bold')
entry.place(x=15, y=45)

fromLabel = Label(bottom_frame, text='From: ', font='Poppins 12 bold')
fromLabel.place(x=15, y=77)
from_currency_combo = ttk.Combobox(bottom_frame, values=list(currencies.keys()), width=14, font='Poppins 10 bold')
from_currency_combo.place(x=15, y=106)

toLabel = Label(bottom_frame, text='To: ', font='Poppins 12 bold')
toLabel.place(x=15, y=140)
to_currency_combo = ttk.Combobox(bottom_frame, values=list(currencies.keys()), width=14, font='Poppins 10 bold')
to_currency_combo.place(x=15, y=169)

resultLabel = Label(bottom_frame, text='', font='Poppins 10 bold')
resultLabel.place(x=15, y=200)

convert_button = Button(bottom_frame, text="Convert", width=27, justify=CENTER, bg='#0083FF', fg='white',
                        font='Poppins 10 bold', command=convert_currency)
convert_button.place(x=22, y=235)


window.mainloop()