def is_fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return f"O número {n} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {n} NÃO pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
print(is_fibonacci(numero))
