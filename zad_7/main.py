import requests
from typing import Optional

# Definicja klasy Brewery
class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        street: Optional[str],
        city: str,
        state: str,
        postal_code: str,
        country: str,
        phone: Optional[str],
        website_url: Optional[str]
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return (
            f"Brewery: {self.name}\n"
            f"Type: {self.brewery_type}\n"
            f"Address: {self.street or 'Brak'}, {self.city}, {self.state}, {self.postal_code}, {self.country}\n"
            f"Phone: {self.phone or 'Brak'}\n"
            f"Website: {self.website_url or 'Brak'}\n"
            "--------------------------------------"
        )
def fetch_breweries(limit: int = 20):
    url = f"https://api.openbrewerydb.org/v1/breweries?per_page={limit}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Pobranie danych
dane = fetch_breweries(20)

# Utworzenie listy obiektów klasy Brewery
lista_browarow = []
for item in dane:
    browar = Brewery(
        id=item.get("id", ""),
        name=item.get("name", ""),
        brewery_type=item.get("brewery_type", ""),
        street=item.get("street"),
        city=item.get("city", ""),
        state=item.get("state", ""),
        postal_code=item.get("postal_code", ""),
        country=item.get("country", ""),
        phone=item.get("phone"),
        website_url=item.get("website_url")
    )
    lista_browarow.append(browar)

# Wyświetlenie każdego obiektu z osobna
for browar in lista_browarow:
    print(browar)
