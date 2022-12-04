cpf_invalido = [
    str(n) * 11
    for n in range(10)
]

def verificarCPF(cpf):
    if len(cpf) != 11 or cpf in cpf_invalido:
        return print(f"O formato do CPF é inválido") 
    return calculoCPF(cpf)

def calculoCPF(cpf):  # Recebe e formata o CPF com 9 digitos (primeira parte do processo de validação) 
    def calcSegundo_digito(cpf_digitos, contagem_regressiva, resultado):  # Recebe e formata o CPF com 10 digitos (segunda parte do processo de validação)
        cpf_digitos = cpf_digitos + cpf[-2]
        resultado = somarDigitos(cpf_digitos, contagem_regressiva)
        return verificaDigito(resultado)
        
    cpf_digitos = cpf[:9]
    contagem_regressiva = len(cpf_digitos) + 1  
    resultado = somarDigitos(cpf_digitos, contagem_regressiva)
    
    return verificaDigito(resultado), calcSegundo_digito(cpf_digitos, contagem_regressiva=11, resultado=0)

def verificaDigito(resultado):
        if resultado > 9:
            return 0
        return resultado

def somarDigitos(cpf_digitos, contagem_regressiva):  # Essa função faz a multiplicação dos 9 ou 10 números do CPF para a validação. Ela retornará o valor do digito
        resultado = 0
        for n in range(0, len(cpf_digitos)):
            resultado += contagem_regressiva * int(cpf_digitos[n])
            contagem_regressiva -= 1   
        resultado = (resultado * 10) % 11     
        return resultado    

def validarCPF(cpf):
    cpf = cpf.replace('.', '').replace('-', '')
    digitos = verificarCPF(cpf)
    cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[-2:]}'
    if digitos:
        digitos = str(digitos[0]) + str(digitos[1]) 
        if digitos != cpf[-2:]:
            return f"O CPF {cpf} é inválido!"
        return f"O CPF {cpf} é válido"
    return "\nFIM DO PROGRAMA"
