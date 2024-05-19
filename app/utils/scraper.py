import requests
from bs4 import BeautifulSoup
from app.config import settings
from datetime import datetime

def fetch_data(tab: str, year: int = None, suboption: str = None):
    url = settings.EMBRAPA_URLS.get(tab)
    if not url:
        return {"error": "Invalid tab"}

    if year is None:
        year = datetime.now().year

    if tab in ["processing", "importation"]:
        if suboption is None:
            suboption = "subopt_01"
        full_url = f"{url}&ano={year}&subopcao={suboption}"
    else:
        full_url = f"{url}&ano={year}"

    response = requests.get(full_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        if tab == "production":
            data = parse_production_table(soup)
        elif tab == "processing":
            data = parse_processing_table(soup)
        elif tab == "commercialization":
            data = parse_commercialization_table(soup)
        elif tab == "importation":
            data = parse_importation_table(soup)
        elif tab == "exportation":
            data = parse_exportation_table(soup)
        else:
            data = {"error": "Tab not supported"}
        return data
    else:
        return {"error": "Failed to fetch data"}

def parse_production_table(soup):
    table = soup.find("table", {"class": "tb_base tb_dados"})
    if not table:
        return {"error": "Table not found"}

    data = []
    current_item = None

    rows = table.find("tbody").find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 2:
            product = cols[0].text.strip()
            quantity = cols[1].text.strip().replace(".", "")
            quantity = int(quantity) if quantity.isdigit() else quantity

            if 'tb_item' in cols[0]['class']:
                current_item = {"product": product, "quantity": quantity, "subitems": []}
                data.append(current_item)
            elif 'tb_subitem' in cols[0]['class'] and current_item:
                subitem = {"product": product, "quantity": quantity}
                current_item["subitems"].append(subitem)

    total_row = table.find("tfoot", {"class": "tb_total"})
    total_data = None
    if total_row:
        total_cols = total_row.find_all("td")
        if len(total_cols) == 2:
            total_product = total_cols[0].text.strip()
            total_quantity = total_cols[1].text.strip().replace(".", "")
            total_quantity = int(total_quantity) if total_quantity.isdigit() else total_quantity
            total_data = {"product": total_product, "quantity": total_quantity}

    return {"items": data, "total": total_data}

def parse_processing_table(soup):
    table = soup.find("table", {"class": "tb_base tb_dados"})
    if not table:
        return {"error": "Table not found"}

    data = []
    current_item = None

    rows = table.find("tbody").find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 2:
            cultivar = cols[0].text.strip()
            quantity = cols[1].text.strip().replace(".", "")
            quantity = int(quantity) if quantity.isdigit() else quantity

            if 'tb_item' in cols[0]['class']:
                current_item = {"cultivar": cultivar, "quantity": quantity, "subitems": []}
                data.append(current_item)
            elif 'tb_subitem' in cols[0]['class'] and current_item:
                subitem = {"cultivar": cultivar, "quantity": quantity}
                current_item["subitems"].append(subitem)

    total_row = table.find("tfoot", {"class": "tb_total"})
    total_data = None
    if total_row:
        total_cols = total_row.find_all("td")
        if len(total_cols) == 2:
            total_cultivar = total_cols[0].text.strip()
            total_quantity = total_cols[1].text.strip().replace(".", "")
            total_quantity = int(total_quantity) if total_quantity.isdigit() else total_quantity
            total_data = {"cultivar": total_cultivar, "quantity": total_quantity}

    return {"items": data, "total": total_data}

def parse_commercialization_table(soup):
    table = soup.find("table", {"class": "tb_base tb_dados"})
    if not table:
        return {"error": "Table not found"}

    data = []
    current_item = None

    rows = table.find("tbody").find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 2:
            product = cols[0].text.strip()
            quantity = cols[1].text.strip().replace(".", "")
            quantity = int(quantity) if quantity.isdigit() else quantity

            if 'tb_item' in cols[0]['class']:
                current_item = {"product": product, "quantity": quantity, "subitems": []}
                data.append(current_item)
            elif 'tb_subitem' in cols[0]['class'] and current_item:
                subitem = {"product": product, "quantity": quantity}
                current_item["subitems"].append(subitem)

    total_row = table.find("tfoot", {"class": "tb_total"})
    total_data = None
    if total_row:
        total_cols = total_row.find_all("td")
        if len(total_cols) == 2:
            total_product = total_cols[0].text.strip()
            total_quantity = total_cols[1].text.strip().replace(".", "")
            total_quantity = int(total_quantity) if total_quantity.isdigit() else total_quantity
            total_data = {"product": total_product, "quantity": total_quantity}

    return {"items": data, "total": total_data}

def parse_importation_table(soup):
    table = soup.find("table", {"class": "tb_base tb_dados"})
    if not table:
        return {"error": "Table not found"}

    data = []
    rows = table.find("tbody").find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 3:
            country = cols[0].text.strip()
            quantity = cols[1].text.strip().replace(".", "")
            quantity = int(quantity) if quantity.isdigit() else quantity
            value = cols[2].text.strip().replace(".", "").replace(",", ".")
            value = float(value) if value.replace(".", "").isdigit() else value

            data.append({"country": country, "quantity": quantity, "value": value})

    total_row = table.find("tfoot", {"class": "tb_total"})
    total_data = None
    if total_row:
        total_cols = total_row.find_all("td")
        if len(total_cols) == 3:
            total_country = total_cols[0].text.strip()
            total_quantity = total_cols[1].text.strip().replace(".", "")
            total_quantity = int(total_quantity) if total_quantity.isdigit() else total_quantity
            total_value = total_cols[2].text.strip().replace(".", "").replace(",", ".")
            total_value = float(total_value) if total_value.replace(".", "").isdigit() else total_value
            total_data = {"country": total_country, "quantity": total_quantity, "value": total_value}

    return {"items": data, "total": total_data}

def parse_exportation_table(soup):
    table = soup.find("table", {"class": "tb_base tb_dados"})
    if not table:
        return {"error": "Table not found"}

    data = []
    rows = table.find("tbody").find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 3:
            country = cols[0].text.strip()
            quantity = cols[1].text.strip().replace(".", "")
            quantity = int(quantity) if quantity.isdigit() else quantity
            value = cols[2].text.strip().replace(".", "").replace(",", ".")
            value = float(value) if value.replace(".", "").isdigit() else value

            data.append({"country": country, "quantity": quantity, "value": value})

    total_row = table.find("tfoot", {"class": "tb_total"})
    total_data = None
    if total_row:
        total_cols = total_row.find_all("td")
        if len(total_cols) == 3:
            total_country = total_cols[0].text.strip()
            total_quantity = total_cols[1].text.strip().replace(".", "")
            total_quantity = int(total_quantity) if total_quantity.isdigit() else total_quantity
            total_value = total_cols[2].text.strip().replace(".", "").replace(",", ".")
            total_value = float(total_value) if total_value.replace(".", "").isdigit() else total_value
            total_data = {"country": total_country, "quantity": total_quantity, "value": total_value}

    return {"items": data, "total": total_data}
