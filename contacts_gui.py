from tkinter import *
from tkinter import ttk

import pickle
from time import sleep


ACTION_ADD_CONTACT = 1
ACTION_REMOVE_CONTACT = 2
ACTION_FIND_CONTACT = 3
ACTION_EXPORT_CONTACTS = 4
ACTION_EXIT = 5

MENU_OPTIONS = [ACTION_ADD_CONTACT, ACTION_REMOVE_CONTACT, ACTION_FIND_CONTACT, ACTION_EXPORT_CONTACTS, ACTION_EXIT]

SAVE_FILE_NAME = "contacts.save"


def ask_until_option_expected(options):
    selected_action = ""

    while not selected_action.isdigit() or (selected_action.isdigit() and int(selected_action) not in options):
        selected_action = input("¿Qué opción quieres seleccionar? ")

    return int(selected_action)


def show_menu():
    print("Acciones disponibles: ")
    print("1 - Añadir contacto")
    print("2 - Eliminar contacto")
    print("3 - Buscar un contacto")
    print("4 - Exportar un contactos a un CSV")
    print("5 - Salir")

    # while selected_action not in MENU_OPTIONS ---> Comando más rápido y sencillo que el anterior

    return ask_until_option_expected(MENU_OPTIONS)

def add_contact(contacts, name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)
    return contact

def show_previous_contacts(contacts, frame_contact_list):
    #Creamos una función show_previous_contacts que se encargue de mostrar los contactos de la sesión anterior
    #Para ello, la función recibe como parámetro la lista contacts que contiene el contenido del archivo cargado
    #con la función load_contacts().
    for num in range(0,len(contacts)):
        contact = contacts[num]
        contact_name = contact["name"]
        contact_email = contact["email"]
        contact_phone = contact["phone"]
        cols, row = frame_contact_list.grid_size()
        ttk.Label(frame_contact_list, text=contact_name).grid(column=1, row=row)
        ttk.Label(frame_contact_list, text=contact_email).grid(column=2, row=row)
        ttk.Label(frame_contact_list, text=contact_phone).grid(column=3, row=row)

def add_contact_tk(contacts, name, phone, email, frame_contact_list):
    contact = add_contact(contacts, name, phone, email)
    cols, row = frame_contact_list.grid_size()
    previous=len(contacts)
    ttk.Label(frame_contact_list, text=contact["name"]).grid(column=1, row=row+previous)
    ttk.Label(frame_contact_list, text=contact["email"]).grid(column=2, row=row+previous)
    ttk.Label(frame_contact_list, text=contact["phone"]).grid(column=3, row=row+previous)
    save_contacts(contacts)

def ask_new_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = add_contact(contacts, input("Nombre: "),input("Teléfono: "),input("Email: "))
    print("Se ha añadido el contacto {} correctamente\n".format(contact["name"]))
    sleep(2)


def remove_contact(contacts):
    print("\n\nEliminar contacto\n")

    contact_in = False

    while contact_in == False:
        contact_to_remove = input("Introduce el nombre del contacto que quieres eliminar: ")
        for contact in contacts:
            if contact["name"] == contact_to_remove:
                contacts.remove(contact)
                contact_in = True
                print("El contacto {} ha sido eliminado correctamente".format(contact_to_remove))
                sleep(2)


def find_contact(contacts):
    print("\n\nBuscar contacto\n")
    search_term = input("Introduce el nombre del contacto, o parte de él, que quieres buscar: ")
    found_contacts = []

    print("Se han encontrado los siguientes contactos:")
    contact_indexes = []
    contact_counter = 0

    for contact in contacts:
        if contact["name"].find(search_term) >= 0:
            found_contacts.append(contact)
            print("{}   -   {}".format(contact_counter, contact["name"]))
            contact_indexes.append(contact_counter)
            contact_counter += 1

    contact_index = 0

    if len(contact_indexes) > 1:
        contact_index = ask_until_option_expected(contact_indexes)
    elif len(contact_indexes) == 0:
        print("No se han encontrado contactos.")
        return

    print("\nInformación sobre {}\n".format(found_contacts[contact_index]))
    print("Nombre: {name}, Teléfono: {phone}, Email: {email}\n\n".format(**found_contacts[contact_index]))

    sleep(2)

    return found_contacts


def export_contacts(contacts):
    print("Export contactos\n")


def load_contacts():
    try:
        contacts = pickle.load(open(SAVE_FILE_NAME, "rb"))
        return contacts
        #La función retorna la lista de los contactos guardados en formato binario en el archivo contacts.save
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    # Modo escritura "wb" escritura binaria porque los pickles son binarios
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)


def main():
    #Creamos una función main() para cargar el archivo con los contactos guardados de la sesión anterior 1 sola vez.
    contacts = load_contacts()
    main_two(contacts)

def main_two(contacts):

    #  Creamos una función main_two(contacts) para diferenciarla de la main() principal. De esa manera permitimos que en
    #main() se cargue el archivo de los contactos guardados una vez al iniciar el programa.
    root = Tk()
    frame_add_contact = ttk.Frame(root, padding="5 12 5 12")  # padding = Márgenes: 1-Izquierda, 2-Arriba, 3-Derecha, 4-Abajo
    frame_add_contact.grid()                                    # 30 12 30 12

    frame_contact_list = ttk.Frame(root, padding="5 12 5 12")  # padding = Márgenes: 1-Izquierda, 2-Arriba, 3-Derecha, 4-Abajo
    frame_contact_list.grid()                                   # 30 12 30 12

    name = StringVar()
    email = StringVar()
    phone = StringVar()

    ttk.Label(frame_add_contact, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_add_contact, text="Email").grid(column=2, row=1)
    ttk.Label(frame_add_contact, text="Teléfono").grid(column=3, row=1)

    ttk.Entry(frame_add_contact, width=15, textvariable=name).grid(column=1, row=2)
    ttk.Entry(frame_add_contact, width=15, textvariable=email).grid(column=2, row=2)
    ttk.Entry(frame_add_contact, width=15, textvariable=phone).grid(column=3, row=2)

    ttk.Label(frame_contact_list, width=15, text="Nombre").grid(column=1, row=1)
    ttk.Label(frame_contact_list, width=15, text="Email").grid(column=2, row=1)
    ttk.Label(frame_contact_list, width=15, text="Teléfono").grid(column=3, row=1)

    show_previous_contacts(contacts, frame_contact_list)

    ttk.Button(frame_add_contact, text="Añadir",
               command=lambda: add_contact_tk(contacts, name.get(), phone.get(), email.get(), frame_contact_list)
               ).grid(column=3, row=3)
    #Llamando a la función save_contacts guardamos los cambios efectuados durante cada ciclo del mainloop.
    save_contacts(contacts)
    root.mainloop()


if __name__ == "__main__":
    main()
