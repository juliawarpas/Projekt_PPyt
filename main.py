from tkinter import *

import tkintermapview
from click import command


facilities = []
employees = []

class Facility:
    def __init__(self, name, surname, location, post, map_widget):
        self.name = name
        self.surname = surname
        self.location = location
        self.post = post
        self.cordinates = self.get_cordinates()
        self.marker = map_widget.set_marker(self.cordinates[0], self.cordinates[1], text=f'{self.name} {self.surname} {self.location}')

    def get_cordinates(self) -> list:
        from bs4 import BeautifulSoup
        import requests
        adress_url = f'https://pl.wikipedia.org/wiki/{self.location}'
        response = requests.get(adress_url)
        if response.status_code == 200:
            response_html = BeautifulSoup(response.content, 'html.parser')
            return [
                float(response_html.select('.latitude')[1].text.replace(',', '.')),
                float(response_html.select('.longitude')[1].text.replace(',', '.'))
            ]

class Employee:
    def __init__(self, name, surname, location, post, map_widget):
        self.name = name
        self.surname = surname
        self.location = location
        self.post = post
        self.cordinates = self.get_cordinates()
        self.marker = map_widget.set_marker(self.cordinates[0], self.cordinates[1], text=f'{self.name} {self.surname} {self.location}')

    def get_cordinates(self) -> list:
        from bs4 import BeautifulSoup
        import requests
        adress_url = f'https://pl.wikipedia.org/wiki/{self.location}'
        response = requests.get(adress_url)
        if response.status_code == 200:
            response_html = BeautifulSoup(response.content, 'html.parser')
            return [
                float(response_html.select('.latitude')[1].text.replace(',', '.')),
                float(response_html.select('.longitude')[1].text.replace(',', '.'))
            ]


def add_facilities() -> None:
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    post = entry_post.get()

    facility = Facility(name=name, surname=surname, location=location, post=post, map_widget=map_widget)
    facilities.append(facility)


    print(facilities)


    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_post.delete(0, END)

    entry_imie.focus()
    show_facilities()

def show_facilities() -> None:
    listbox_lista_obiektow.delete(0, END)
    for idx,user in enumerate(facilities):
        listbox_lista_obiektow.insert(idx, f'{idx+1}. {facilities.name} {facilities.surname}')

def remove_facility() -> None:
    i=listbox_lista_obiektow.index(ACTIVE)
    facilities[i].marker.delete()
    facilities.pop(i)
    show_facilities()


def edit_facility():
    i = listbox_lista_obiektow.index(ACTIVE)
    name = facilities[i].name
    surname = facilities[i].surname
    location = facilities[i].location
    post = facilities[i].post

    entry_imie.insert(0, name)
    entry_nazwisko.insert(0, surname)
    entry_miejscowosc.insert(0, location)
    entry_post.insert(0, post)

    button_dodaj_obiekt.configure(text='Zapisz', command=lambda: update_facility(i))

def update_facility(i):
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    post = entry_post.get()

    facilities[i].name = name
    facilities[i].surname = surname
    facilities[i].location = location
    facilities[i].post = post

    facilities[i].cordinates = facilities[i].get_cordinates()
    facilities[i].marker.delete()
    facilities[i].marker = map_widget.set_marker(facilities[i].cordinates[0], facilities[i].cordinates[1], facilities=f'{facilities[i].name}')

    show_facilities()

    button_dodaj_obiekt.config(text='Dodaj', command=add_facilities)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_post.delete(0, END)

    entry_imie.focus()

def show_facility_details():
    i=listbox_lista_obiektow.index(ACTIVE)
    label_szczegoly_obiektu_name_wartosc.config(text=facilities[i].name)
    label_szczegoly_obiektu_surname_wartosc.config(text=facilities[i].surname)
    label_szczegoly_obiektu_miejscowosc_wartosc.config(text=facilities[i].location)
    label_szczegoly_obiektu_post_wartosc.config(text=facilities[i].post)

    map_widget.set_zoom(15)
    map_widget.set_position(facilities[i].cordinates[0], facilities[i].cordinates[1])

def add_employee() -> None:
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    post = entry_post.get()

    Employee = employees(name=name, surname=surname, location=location, post=post, map_widget=map_widget)
    employees.append(employees)


    print(employees)


    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_post.delete(0, END)

    entry_imie.focus()
    show_facilities()

def show_employee() -> None:
    listbox_lista_obiektow.delete(0, END)
    for idx,user in enumerate(employees):
        listbox_lista_obiektow.insert(idx, f'{idx+1}. {employees.name} {employees.surname}')

def remove_employee() -> None:
    i=listbox_lista_obiektow.index(ACTIVE)
    employees[i].marker.delete()
    employees.pop(i)
    show_employee()


def edit_employee() -> None:
    i = listbox_lista_obiektow.index(ACTIVE)
    name = employees[i].name
    surname = employees[i].surname
    location = employees[i].location
    post = employees[i].post

    entry_imie.insert(0, name)
    entry_nazwisko.insert(0, surname)
    entry_miejscowosc.insert(0, location)
    entry_post.insert(0, post)

    button_dodaj_obiekt.configure(text='Zapisz', command=lambda: update_employee(i))

def update_employee(i):
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    post = entry_post.get()

    employees[i].name = name
    employees[i].surname = surname
    employees[i].location = location
    employees[i].post = post

    employees[i].cordinates = employees[i].get_cordinates()
    employees[i].marker.delete()
    employees[i].marker = map_widget.set_marker(employees[i].cordinates[0], employees[i].cordinates[1], employees=f'{employees[i].name}')

    show_employee()

    button_dodaj_obiekt.config(text='Dodaj', command=add_employee())

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    entry_post.delete(0, END)

    entry_imie.focus()

def show_employee_details():
    i=listbox_lista_obiektow.index(ACTIVE)
    label_szczegoly_obiektu_name_wartosc.config(text=employees[i].name)
    label_szczegoly_obiektu_surname_wartosc.config(text=employees[i].surname)
    label_szczegoly_obiektu_miejscowosc_wartosc.config(text=employees[i].location)
    label_szczegoly_obiektu_post_wartosc.config(text=employees[i].post)

    map_widget.set_zoom(15)
    map_widget.set_position(employees[i].cordinates[0], employees[i].cordinates[1])

#GUI
root = Tk()
root.geometry("1200x700")
root.title('mapbook_jw')


ramka_lista_placowek=Frame(root)
ramka_formularz=Frame(root)
ramka_szczegoly_obiektu=Frame(root)
ramka_mapa=Frame(root)
ramka_lista_pracownikow=Frame(root)

ramka_lista_placowek.grid(row=0, column=0)
ramka_formularz.grid(row=1, column=1, sticky=N)
ramka_szczegoly_obiektu.grid(row=1, column=0, columnspan=2)
ramka_mapa.grid(row=2, column=0, columnspan=2)
ramka_lista_pracownikow.grid(row=0, column=1, sticky=N)

# ramka_lista_obiektow
label_lista_obiektow=Label(ramka_lista_placowek, text='Lista placówek:')
label_lista_obiektow.grid(row=0, column=0)

listbox_lista_obiektow=Listbox(ramka_lista_placowek, width=50, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)


button_pokaz_szczegoly=Button(ramka_lista_placowek, text='Pokaz szczegóły', command=show_facility_details)
button_pokaz_szczegoly.grid(row=2, column=0)


button_usun_obiekt=Button(ramka_lista_placowek, text='Usuń', command=remove_facility)
button_usun_obiekt.grid(row=2, column=1)


button_edytuj_obiekt=Button(ramka_lista_placowek, text='Edytuj', command=edit_facility)
button_edytuj_obiekt.grid(row=2, column=2)

#ramka_lista_pracowników
label_ramka_lista_pracownikow = Label(ramka_lista_pracownikow, text="Pracownicy:")
label_ramka_lista_pracownikow.grid(row=0, column=2)

listbox_ramka_lista_pracownikow=Listbox(ramka_lista_pracownikow, width=50, height=10)
listbox_ramka_lista_pracownikow.grid(row=1, column=2, columnspan=3)


button_pokaz_szczegoly_pracownikow=Button(ramka_lista_pracownikow, text='Pokaz szczegóły', command=show_employee_details)
button_pokaz_szczegoly_pracownikow.grid(row=2, column=2)


button_usun_pracownika=Button(ramka_lista_pracownikow, text='Usuń', command=remove_employee)
button_usun_pracownika.grid(row=2, column=3)


button_edytuj_pracownika=Button(ramka_lista_pracownikow, text='Edytuj', command=edit_employee)
button_edytuj_pracownika.grid(row=2, column=4)

# ramka_formularz
label_formularz=Label(ramka_formularz, text='Formularz:')
label_formularz.grid(row=0, column=0)

label_imie=Label(ramka_formularz, text='Imie:')
label_imie.grid(row=1, column=0, sticky=W)

label_nazwisko=Label(ramka_formularz, text='Nazwisko:')
label_nazwisko.grid(row=2, column=0, sticky=W)

label_miejscowosc=Label(ramka_formularz, text='Miejscowość:')
label_miejscowosc.grid(row=3, column=0, sticky=W)

label_post=Label(ramka_formularz, text='Post:')
label_post.grid(row=4, column=0, sticky=W)


entry_imie=Entry(ramka_formularz)
entry_imie.grid(row=1, column=1)

entry_nazwisko=Entry(ramka_formularz)
entry_nazwisko.grid(row=2, column=1)

entry_miejscowosc=Entry(ramka_formularz)
entry_miejscowosc.grid(row=3, column=1)

entry_post=Entry(ramka_formularz)
entry_post.grid(row=4, column=1)


button_dodaj_obiekt=Button(ramka_formularz, text='Dodaj', command=add_facilities)
button_dodaj_obiekt.grid(row=5, column=0, columnspan=2)

# ramka_szczegoly_obiektow
label_pokaz_szczegoly=Label(ramka_szczegoly_obiektu, text='Szczegóły użytkownika:')
label_pokaz_szczegoly.grid(row=0, column=0)


label_szczegoly_obiektu_name=Label(ramka_szczegoly_obiektu, text='Imię:')
label_szczegoly_obiektu_name.grid(row=1, column=0)


label_szczegoly_obiektu_name_wartosc=Label(ramka_szczegoly_obiektu, text='......')
label_szczegoly_obiektu_name_wartosc.grid(row=1, column=1)


label_szczegoly_obiektu_surname=Label(ramka_szczegoly_obiektu, text='Nazwisko:')
label_szczegoly_obiektu_surname.grid(row=1, column=2)


label_szczegoly_obiektu_surname_wartosc=Label(ramka_szczegoly_obiektu, text='....')
label_szczegoly_obiektu_surname_wartosc.grid(row=1, column=3)


label_szczegoly_obiektu_miejscowosc=Label(ramka_szczegoly_obiektu, text='Miejscowość:')
label_szczegoly_obiektu_miejscowosc.grid(row=1, column=4)


label_szczegoly_obiektu_miejscowosc_wartosc=Label(ramka_szczegoly_obiektu, text='....')
label_szczegoly_obiektu_miejscowosc_wartosc.grid(row=1, column=5)

label_szczegoly_obiektu_post=Label(ramka_szczegoly_obiektu, text='Posty:')
label_szczegoly_obiektu_post.grid(row=1, column=6)


label_szczegoly_obiektu_post_wartosc=Label(ramka_szczegoly_obiektu, text='....')
label_szczegoly_obiektu_post_wartosc.grid(row=1, column=7)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=450, corner_radius=0)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.00)
map_widget.set_zoom(6)

root.mainloop()