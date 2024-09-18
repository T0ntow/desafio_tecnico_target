def contar_letra_a(s):
    count = s.lower().count('a')
    return f"A letra 'a' aparece {count} vezes na string."

string = input("Digite uma string: ")
print(contar_letra_a(string))
