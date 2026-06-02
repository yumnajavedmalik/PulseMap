import requests

def get_country(name):

    try:
        r = requests.get(
            f"https://restcountries.com/v3.1/name/{name}",
            timeout=5
        )

        if r.status_code != 200:
            return None

        data = r.json()[0]
        latlng = data.get("latlng", [0, 0])

        return {
            "name": data["name"]["common"],
            "lat": latlng[0],
            "lon": latlng[1]
        }

    except:
        return None