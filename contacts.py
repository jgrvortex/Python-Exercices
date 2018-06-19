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


    #while selected_action not in MENU_OPTIONS ---> Comando más rápido y sencillo que el anterior

    return ask_until_option_expected(MENU_OPTIONS)


def add_contact(contacts):
    print("\n\nAñadir contacto\n")
    contact = {
        "name": input("Nombre: "),
        "phone": input("Teléfono: "),
        "email": input("Email: ")
    }
    contacts.append(contact)
    print("Se ha añadido el contacto {} correctamente".format(contact["name"]))
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
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    #Modo escritura "wb" escritura binaria porque los pickles son binarios
    with open(SAVE_FILE_NAME, "wb") as save_file:
        pickle.dump(contacts, save_file)


def main():
    contacts = load_contacts()
    action = show_menu()
    while action != ACTION_EXIT:
        if action == ACTION_ADD_CONTACT:
            add_contact(contacts)
        elif action == ACTION_REMOVE_CONTACT:
            remove_contact(contacts)
        elif action == ACTION_FIND_CONTACT:
            find_contact(contacts)
        elif action == ACTION_EXPORT_CONTACTS:
            export_contacts(contacts)


        action = show_menu()
        
    save_contacts(contacts)


if __name__ == "__main__":
    main()

