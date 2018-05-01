
listado_as = ["a","A"]

string_sustitutiva = "VACA"

lista_strings = []

string_actual = ""



while string_actual != "FIN":
    string_actual = input("Introduce una string para cambiar sus 'a' y sus 'A' por la string 'VACA': ")
    if string_actual == "FIN":
        break

    string_actual = string_actual.replace("A","VACA")
    string_actual = string_actual.replace("a", "VACA")

    lista_strings.append(string_actual)

print("Las strings introducidas por el usuario transformadas son las siguientes: {}".format(lista_strings))
