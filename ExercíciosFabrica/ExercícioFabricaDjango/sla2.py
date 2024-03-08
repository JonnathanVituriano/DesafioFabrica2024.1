#pip. install requests
#viaceps

import requests

konga = int(input("Diga o cep que queres saber: "))
manaira = requests.get("https://viacep.com.br/ws/",konga, "/json/");

json = manaira.json();

print (manaira);
print (json);

print (json.get("cep", "não tem cep"));


#como usar o insomnia, e do viacep saber o logradouro