import requests as requests

def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:
          print(f"NOMBRE OFICIAL EN ESPAÑOL:{pais['translations']['spa']['official']}")
          print(f"LA CAPITAL ES:{pais['capital'][0]}")
          print(f"CODIGO TELEFONICO:{pais['idd']['root'] + pais['idd']['suffixes'][0]}")

          if "currencies" in pais:
              for codigo , info in pais["currencies"].items():
                  nombre = info["name"]
                  print(f"MONEDA ({codigo}):{nombre}")


url = 'https://restcountries.com/v3.1/independent?=status=true&fields=translations,capital,idd,currencies'
listar_nombre_paises(url)