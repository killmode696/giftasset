import requests

import config

def escape_markdown(text):
    output = text
    escape_chars = '$-_.#!~}{+=;\"'
    output = ''.join(f'\\{char}' if char in escape_chars else char for char in output)
    return output

def escape_input(text):
    output = text.replace("\\", "")
    escape_chars = '*|>()[]`'
    output = ''.join(f'\\{char}' if char in escape_chars else char for char in output)
    return output

def get_user_gifts_by_username(username: str):
    base_url = "https://giftasset.pro/api/v1/gifts/get_user_profile_price"

    #proxies = {
    #    "http": config.PROXY,
    #    "https": config.PROXY
    #}
    headers = {
        "accept": "*/*",
        "X-API-Key": config.GIFT_ASSET_API_KEY
    }
    gifts_data = []
    floor_price_data = 0
    avg_price_data = 0
    limit = 100
    offset = 0

    for i in range(100):
        params = {
            "username":username,
            "limit": limit,
            "offset": offset
        }

        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code !=200:
            print(f"Ошибка {response.status_code}: {response.text}")
        data = response.json()

        if data['gifts'] == []:
            break
        print(data['gifts'])
        gifts_data.extend(data['gifts'])
        floor_price_data_offset = sum(data['total_model_price'].values()) / len(data['total_model_price'])
        floor_price_data += floor_price_data_offset

        avg_price_data += floor_price_data_offset + (sum(data['total_collection_price'].values()) / len(data['total_collection_price'])) / 2
        offset += limit

    return gifts_data, round(floor_price_data, 2), round(avg_price_data, 2)

def get_formated_output(username:str, floor_price_data:float, avg_price_data:float, gifts_arr: list):
    print(len(gifts_arr))
    output = escape_input(f"Пользователь @{username}\n" \
    + f"Количество подарков {str(len(gifts_arr))} 🎁\n" \
    + f"Цена коллекции {str(floor_price_data)} 💎\n" \
    + f"Цена колекции (AVG) {str(avg_price_data)} 💎\n\n" \
    + f"Список подарков\n")

    top_100 = sorted(gifts_arr, key=lambda x: sum(x['model_prices'].values()) / len(x['model_prices']), reverse = True)[:100]
    output += "**>"
    for gift in top_100:
        output += f"> ├ [{gift['name']}](https://t.me/nft/{gift['name']}) {round(sum(gift['model_prices'].values()) / len(gift['model_prices']), 2)} TON\n"
    output += "> ||"

    output = escape_markdown(output)
    return output
    