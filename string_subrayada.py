
string_introducida = ""
string_subrayado = ""

while string_introducida != "FIN":
    string_subrayado = ""
    string_introducida = input("Introduce una string: ")
    if string_introducida == "FIN":
        break

    long = len(string_introducida)

    for numcar in range(long):
        string_subrayado = string_subrayado + "-"

    print(string_introducida)
    print(string_subrayado)