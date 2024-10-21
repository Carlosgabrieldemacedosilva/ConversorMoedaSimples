import requests, json


def Converter(opt, vlr):
    url = ' https://economia.awesomeapi.com.br/last/'
    if opt == 1:
        url = url + 'USD-BRL'
    elif opt == 2 :
        url = url + 'EUR-BRL'
    else:
        url = url + 'BTC-BRL'


    re = requests.get(url)
    dados = json.loads(re.content)
    valor = dados[url.split('/')[-1].replace('-','')]['bid']
    return vlr / float(valor)
     



while True:
    print('CONVERSOR DE MOEDA')
    print(50*'=')
    print("""
        
        SELECIONE A MOEDA QUE DESEJA CONVERTER
        1 : DOLAR,
        2 : EURO,
        3 : BITCOIN,
        0 : SAIR 

        """)

    opcao = int(input("Digite o numero de umas das opções: "))
    if opcao > 3 or type(opcao) != int :
        print('Opcao selecionada invalida') 
    elif opcao == 0:
        print('finalizando programa')
        break
    else:
        valor = int(input('Informe o valor que voce deseja converter: '))
        if valor > 0:
            vlrConv  = Converter(opcao,valor)
            print(50*'- - ')
            print('O Valor convertido fica : {:.2f} \n\n\n'.format(vlrConv))

