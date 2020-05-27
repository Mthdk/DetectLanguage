import detectlanguage

detectlanguage.configuration.api_key = 'sua api key'

texto = input(str("Digite a frase que deseja: "))

print(detectlanguage.detect(texto))
