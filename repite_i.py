
vocales = ["a","e","i","o","u","A","E","I","O","U"]

string_actual = ""

while string_actual != "FIN":
    string_actual = input()
    if string_actual == "FIN":
        break

    for vocal_actual in vocales:
        string_actual = string_actual.replace(vocal_actual,"i")

    print(string_actual)



