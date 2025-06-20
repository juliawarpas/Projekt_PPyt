from tkinter import *

import tkintermapview
from click import command


facilities = []
employees = []
clients = []

class Facility:
    def __init__(self, name, location, map_widget):
        self.name = name
        self.location = location
        self.cordinates = self.get_cordinates()
        self.marker = map_widget.set_marker(self.cordinates[0], self.cordinates[1], text=f'{self.name} {self.location}',marker_color_outside='red')

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
    def __init__(self, name, surname, location, facility_name, map_widget):
        self.name = name
        self.surname = surname
        self.location = location
        self.facility_name = facility_name
        self.cordinates = self.get_cordinates()
        self.marker = map_widget.set_marker(self.cordinates[0], self.cordinates[1], text=f'{self.name} {self.surname} {self.location}',marker_color_outside='blue')

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

class Client:
    def __init__(self, name, surname, location, facility_name, map_widget):
        self.name = name
        self.surname = surname
        self.location = location
        self.facility_name = facility_name
        self.cordinates = self.get_cordinates()
        self.marker = map_widget.set_marker(self.cordinates[0], self.cordinates[1], text=f'{self.name} {self.surname} {self.location}',marker_color_outside='green')

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

def add_object():
    name = entry_imie.get()
    location = entry_miejscowosc.get()
    facility_name = placowka_name_var.get()
    typ = typ_var.get()


    try:
        if typ == "Placówka":
            obj = Facility(name, location, map_widget)
            facilities.append(obj)
            show_facilities()

            # aktualizacja menu z placówkami
            placowka_name_var.set("")
            menu_placowka_name['menu'].delete(0, 'end')
            for f in facilities:
                menu_placowka_name['menu'].add_command(label=f.name, command=lambda value=f.name: placowka_name_var.set(value))

        elif typ == "Pracownik":
            surname = entry_nazwisko.get()
            obj = Employee(name, surname, location, facility_name, map_widget)
            employees.append(obj)
            show_employee()
        elif typ == "Klient":
            surname = entry_nazwisko.get()
            obj = Client(name, surname, location, facility_name, map_widget)
            clients.append(obj)
            show_clients()

    except Exception as e:
        print("Błąd dodawania:", e)
        return


    # Czyszczenie_formularz
    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    placowka_name_var.set("")
    typ_var.set("Placówka")



def show_facilities() -> None:
    listbox_lista_obiektow.delete(0, END)
    for idx,user in enumerate(facilities):
        listbox_lista_obiektow.insert(idx, f'{idx+1}. {user.name}')

def remove_facility() -> None:
    i=listbox_lista_obiektow.index(ACTIVE)
    facilities[i].marker.delete()
    facilities.pop(i)
    show_facilities()


def edit_facility():
    i = listbox_lista_obiektow.index(ACTIVE)
    name = facilities[i].name
    location = facilities[i].location


    entry_imie.insert(0, name)
    entry_miejscowosc.insert(0, location)
    placowka_name_var.set("")

    button_dodaj_obiekt.configure(text='Zapisz', command=lambda: update_facility(i))

def update_facility(i):
    name = entry_imie.get()
    location = entry_miejscowosc.get()

    facilities[i].name = name
    facilities[i].location = location

    facilities[i].cordinates = facilities[i].get_cordinates()
    facilities[i].marker.delete()
    facilities[i].marker = map_widget.set_marker(facilities[i].cordinates[0], facilities[i].cordinates[1], text=f'{facilities[i].name}', marker_color_outside='red')

    show_facilities()

    button_dodaj_obiekt.config(text='Dodaj', command=add_object)

    entry_imie.delete(0, END)
    entry_miejscowosc.delete(0, END)
    placowka_name_var.set("")

    entry_imie.focus()



def show_employee() -> None:
    listbox_ramka_lista_pracownikow.delete(0, END)
    for idx,user in enumerate(employees):
        listbox_ramka_lista_pracownikow.insert(idx, f'{idx+1}. {user.name} {user.surname}')

def remove_employee() -> None:
    i=listbox_ramka_lista_pracownikow.index(ACTIVE)
    employees[i].marker.delete()
    employees.pop(i)
    show_employee()


def edit_employee() -> None:
    i = listbox_ramka_lista_pracownikow.index(ACTIVE)
    name = employees[i].name
    surname = employees[i].surname
    location = employees[i].location
    facility_name = employees[i].facility_name

    entry_imie.insert(0, name)
    entry_nazwisko.insert(0, surname)
    entry_miejscowosc.insert(0, location)
    placowka_name_var.set(facility_name)

    button_dodaj_obiekt.configure(text='Zapisz', command=lambda: update_employee(i))

def update_employee(i):
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    facility_name = placowka_name_var.get()

    employees[i].name = name
    employees[i].surname = surname
    employees[i].location = location
    employees[i].facility_name = facility_name

    employees[i].cordinates = employees[i].get_cordinates()
    employees[i].marker.delete()
    employees[i].marker = map_widget.set_marker(employees[i].cordinates[0], employees[i].cordinates[1], text=f'{employees[i].name}',marker_color_outside='blue')

    show_employee()

    button_dodaj_obiekt.config(text='Dodaj', command=add_object)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    placowka_name_var.set(facility_name)

    entry_imie.focus()


def show_clients() -> None:
    listbox_ramka_lista_klientow.delete(0, END)
    for idx,user in enumerate(clients):
        listbox_ramka_lista_klientow.insert(idx, f'{idx+1}. {user.name} {user.surname}')

def remove_client() -> None:
    i=listbox_ramka_lista_klientow.index(ACTIVE)
    clients[i].marker.delete()
    clients.pop(i)
    show_clients()


def edit_clients() -> None:
    i = listbox_ramka_lista_klientow.index(ACTIVE)
    name = clients[i].name
    surname = clients[i].surname
    location = clients[i].location
    facility_name = clients[i].facility_name

    entry_imie.insert(0, name)
    entry_nazwisko.insert(0, surname)
    entry_miejscowosc.insert(0, location)
    placowka_name_var.set(facility_name)

    button_dodaj_obiekt.configure(text='Zapisz', command=lambda: update_client(i))

def update_client(i):
    name = entry_imie.get()
    surname = entry_nazwisko.get()
    location = entry_miejscowosc.get()
    facility_name = placowka_name_var.get()

    clients[i].name = name
    clients[i].surname = surname
    clients[i].location = location
    clients[i].facility_name = facility_name

    clients[i].cordinates = clients[i].get_cordinates()
    clients[i].marker.delete()
    clients[i].marker = map_widget.set_marker(clients[i].cordinates[0], clients[i].cordinates[1], text=f'{clients[i].name}', marker_color_outside='green')

    show_clients()

    button_dodaj_obiekt.config(text='Dodaj', command=add_object)

    entry_imie.delete(0, END)
    entry_nazwisko.delete(0, END)
    entry_miejscowosc.delete(0, END)
    placowka_name_var.set("")

    entry_imie.focus()

def show_all_facilities():
    map_widget.delete_all_marker()
    for facility in facilities:
        facility.marker = map_widget.set_marker(
            facility.cordinates[0],
            facility.cordinates[1],
            text=f'{facility.name} ({facility.location})',
            marker_color_outside='red'
        )

def show_all_employees():
    map_widget.delete_all_marker()
    for emp in employees:
        emp.marker = map_widget.set_marker(
            emp.cordinates[0],
            emp.cordinates[1],
            text=f'{emp.name} {emp.surname} ({emp.location})',
            marker_color_outside = 'blue'
        )


def show_clients_of_selected_facility():
    i = listbox_lista_obiektow.index(ACTIVE)
    if i < 0 or i >= len(facilities):
        return

    selected_facility = facilities[i]
    map_widget.delete_all_marker()

    for client in clients:
        if client.facility_name == selected_facility.name:
            client.marker = map_widget.set_marker(
                client.cordinates[0],
                client.cordinates[1],
                text=f'{client.name} {client.surname} ({client.location})',
                marker_color_outside='green'
            )

def show_employees_of_selected_facility():
    i = listbox_lista_obiektow.index(ACTIVE)
    if i < 0 or i >= len(facilities):
        return

    selected_facility = facilities[i]
    map_widget.delete_all_marker()

    for employee in employees:
        if employee.facility_name == selected_facility.name:
            employee.marker = map_widget.set_marker(
                employee.cordinates[0],
                employee.cordinates[1],
                text=f'{employee.name} {employee.surname} ({employee.location})',
                marker_color_outside='blue'
            )


def on_typ_change(*args):
    typ = typ_var.get()
    if typ == "Placówka":
        Label_nazwisko.grid_remove()
        entry_nazwisko.grid_remove()
        menu_placowka_name.grid_remove()
        Label_placowka_name.grid_remove()
        Label_imie.config(text="Nazwa placówki:")
    else:
        Label_nazwisko.grid()
        entry_nazwisko.grid()
        menu_placowka_name.grid()
        Label_placowka_name.grid()
        Label_imie.config(text="Imię:")

#GUI --------------------------------------------------------------------------
root = Tk()
root.geometry("1200x700")
root.title('mapbook_jw')


ramka_lista_placowek=Frame(root)
ramka_formularz=Frame(root)
ramka_mapa=Frame(root)
ramka_lista_pracownikow=Frame(root)
ramka_lista_klientow=Frame(root)
ramka_mapa_przyciski=Frame(root)

ramka_lista_placowek.grid(row=0, column=0, sticky=N)
ramka_formularz.grid(row=1, column=1, sticky=N)
ramka_mapa.grid(row=3, column=0, columnspan=3)
ramka_lista_pracownikow.grid(row=0, column=1, sticky=N)
ramka_lista_klientow.grid(row=0, column=2, sticky=N)
ramka_mapa_przyciski.grid(row=1, column=0, sticky=NW)

# ramka_lista_placowek
label_lista_obiektow=Label(ramka_lista_placowek, text='Lista placówek:')
label_lista_obiektow.grid(row=0, column=0)

listbox_lista_obiektow=Listbox(ramka_lista_placowek, width=50, height=10)
listbox_lista_obiektow.grid(row=1, column=0, columnspan=3)


button_usun_obiekt=Button(ramka_lista_placowek, text='Usuń', command=remove_facility)
button_usun_obiekt.grid(row=2, column=1)


button_edytuj_obiekt=Button(ramka_lista_placowek, text='Edytuj', command=edit_facility)
button_edytuj_obiekt.grid(row=2, column=2)

#ramka_lista_pracowników
label_ramka_lista_pracownikow = Label(ramka_lista_pracownikow, text="Pracownicy:")
label_ramka_lista_pracownikow.grid(row=0, column=2)

listbox_ramka_lista_pracownikow=Listbox(ramka_lista_pracownikow, width=50, height=10)
listbox_ramka_lista_pracownikow.grid(row=1, column=2, columnspan=3)

button_usun_pracownika=Button(ramka_lista_pracownikow, text='Usuń', command=remove_employee)
button_usun_pracownika.grid(row=2, column=3)

button_edytuj_pracownika=Button(ramka_lista_pracownikow, text='Edytuj', command=edit_employee)
button_edytuj_pracownika.grid(row=2, column=4)

#ramka_lista_klientów
label_ramka_lista_klientow = Label(ramka_lista_klientow, text="Klienci:")
label_ramka_lista_klientow.grid(row=0, column=0)

listbox_ramka_lista_klientow=Listbox(ramka_lista_klientow, width=50, height=10)
listbox_ramka_lista_klientow.grid(row=1, column=0, columnspan=3)

button_usun_klienta=Button(ramka_lista_klientow, text='Usuń', command=remove_client)
button_usun_klienta.grid(row=2, column=1)

button_edytuj_klienta=Button(ramka_lista_klientow, text='Edytuj', command=edit_clients)
button_edytuj_klienta.grid(row=2, column=2)

#formularz dodawania
Label_imie = Label(ramka_formularz, text="Imię:")
Label_imie.grid(row=0, column=0)
entry_imie = Entry(ramka_formularz)
entry_imie.grid(row=0, column=1)

Label_nazwisko = Label(ramka_formularz, text="Nazwisko:")
Label_nazwisko.grid(row=1, column=0)
entry_nazwisko = Entry(ramka_formularz)
entry_nazwisko.grid(row=1, column=1)

Label(ramka_formularz, text="Miejscowość:").grid(row=0, column=2)
entry_miejscowosc = Entry(ramka_formularz)
entry_miejscowosc.grid(row=0, column=3)


Label(ramka_formularz, text="Typ obiektu:").grid(row=4, column=0)
typy = ["Placówka", "Pracownik", "Klient"]
typ_var = StringVar(value=typy[0])
menu_typu = OptionMenu(ramka_formularz, typ_var, *typy)
menu_typu.grid(row=4, column=1)
typ_var.trace_add('write', on_typ_change)

button_dodaj_obiekt = Button(ramka_formularz, text="Dodaj", command=lambda: add_object())
button_dodaj_obiekt.grid(row=5, column=0, columnspan=4, pady=10)

Label_placowka_name = Label(ramka_formularz, text="Nazwa Placówki:")
Label_placowka_name.grid(row=4, column=2)
placowka_name_var = StringVar()
menu_placowka_name = OptionMenu(ramka_formularz, placowka_name_var, "")
menu_placowka_name.grid(row=4, column=3)

#przyciski do map
button_map_all_facilities = Button(ramka_mapa_przyciski, text="Mapa wszystkich placówek", command=show_all_facilities)
button_map_all_facilities.grid(row=0, column=0, sticky=W, pady=5)

button_map_all_employees = Button(ramka_mapa_przyciski, text="Mapa wszystkich pracowników", command=show_all_employees)
button_map_all_employees.grid(row=1, column=0, sticky=W, pady=5)

button_map_clients_of_facility = Button(ramka_mapa_przyciski, text="Klienci tej placówki", command=show_clients_of_selected_facility)
button_map_clients_of_facility.grid(row=2, column=0, sticky=W, pady=5)

button_map_employees_of_facility = Button(ramka_mapa_przyciski, text="Pracownicy tej placówki", command=show_employees_of_selected_facility)
button_map_employees_of_facility.grid(row=3, column=0, sticky=W, pady=5)

# ramka_mapa
map_widget = tkintermapview.TkinterMapView(ramka_mapa, width=1200, height=450, corner_radius=0)
map_widget.grid(row=0, column=0, columnspan=2)
map_widget.set_position(52.23,21.00)
map_widget.set_zoom(6)

on_typ_change()
root.mainloop()