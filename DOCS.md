# GiftAsset API Documentation

### User-Data

- [Receive all user's collections gifts](#receive-all-users-collections-gifts)
- [Receive gift by name](#receive-gift-by-name)
- [Receive user's gifts](#receive-users-gifts)
- [Get the cost of a user's profile](#get-the-cost-of-a-users-profile)

### Providers

- [Get the top sales volume of individual attributes per day](#get-the-top-sales-volume-of-individual-attributes-per-day)
- [Get collection buy offers](#get-collection-buy-offers)
- [Get the top sales volume of individual collections per N time](#get-the-top-sales-volume-of-individual-collections-per-n-time)
- [Get fee per provider](#get-fee-per-provider)
- [Get sales history of current provider](#get-sales-history-of-current-provider)
- [Get providers' sales volumes](#get-providers-sales-volumes)
- [Get the top deals of the day](#get-the-top-deals-of-the-day)

### Analytics

- [Get collections emission](#get-collections-emission)
- [Get gift prices](#get-gift-prices)
- [Get gift price list history](#get-gift-price-list-history)
- [Get gifts update statistics](#get-gifts-update-statistics)

---

## Receive all user's collections gifts

**POST** `/api/v1/gifts/get_all_collections_by_user`

**Query Parameters:**

- `username` *(string, required)* — Telegram username

**Request Body (optional):**
```json
{
  "include": ["Evil Eye"],
  "exclude": ["Evil Eye"]
}
```
- `include` *(array of strings)* — Only the specified collections  
- `exclude` *(array of strings)* — All except the specified collections  

**Response:**
```json
[
  {
    "collection_name": "Astral Shard",
    "count": 1
  },
  {
    "collection_name": "Sakura Flower",
    "count": 1
  },
  {
    "collection_name": "Big Year",
    "count": 1
  },
  {
    "collection_name": "Top Hat",
    "count": 1
  },
  {
    "collection_name": "Desk Calendar",
    "count": 1
  },
  {
    "collection_name": "Lunar Snake",
    "count": 1
  },
  {
    "collection_name": "Candy Cane",
    "count": 1
  },
  {
    "collection_name": "Swag Bag",
    "count": 1
  },
  {
    "collection_name": "Snoop Dogg",
    "count": 1
  }
]
```

---

## Receive gift by name

**GET** `/api/v1/gifts/get_gift_by_name`

**Query Parameters:**

- `name` *(string, required)* — Gift name (e.g., `EasterEgg-1`)

**Response:** 
```json
{
  "attributes": {
    "BACKDROP": {
      "media": "https://giftasset.pro/api/v1/data/backdrops/hunter_green.png",
      "name": "Hunter Green",
      "rarity": 12,
      "readable_rarity": 1.2
    },
    "MODEL": {
      "media": "https://giftasset.pro/api/v1/data/models/redwhelp.png",
      "name": "Red Whelp",
      "rarity": 5,
      "readable_rarity": 0.5
    },
    "SYMBOL": {
      "media": "https://giftasset.pro/api/v1/data/symbols/moose_head.png",
      "name": "Moose Head",
      "rarity": 5,
      "readable_rarity": 0.5
    }
  },
  "attributes_array": [
    {
      "name": "Red Whelp",
      "rarity": 0.5,
      "type": "MODEL"
    },
    {
      "name": "Moose Head",
      "rarity": 0.5,
      "type": "SYMBOL"
    },
    {
      "name": "Hunter Green",
      "rarity": 1.2,
      "type": "BACKDROP"
    }
  ],
  "collectible_id": 1,
  "id": 1707,
  "last_updated_at": "2025-08-16T07:14:44Z",
  "market_floor": {
    "avg": 1.933,
    "max": 2,
    "min": 1.9
  },
  "media": {
    "lottie_anim": "https://nft.fragment.com/gift/easteregg-1.lottie.json",
    "pics": {
      "large": "https://nft.fragment.com/gift/easteregg-1.large.jpg",
      "medium": "https://nft.fragment.com/gift/easteregg-1.medium.jpg",
      "small": "https://nft.fragment.com/gift/easteregg-1.small.jpg"
    }
  },
  "media_preview": "https://nft.fragment.com/gift/easteregg-1.medium.jpg",
  "providers": {
    "getgems": {
      "collection_floor": 1.9,
      "model_floor": 15,
      "sales_stat": {
        "sales_24h": 21,
        "sales_24h_value": 85,
        "sales_all": 251,
        "sales_all_value": 997
      }
    },
    "portals": {
      "collection_floor": 1.9,
      "model_floor": 9.7,
      "sales_stat": {
        "sales_24h": 295,
        "sales_24h_value": 881,
        "sales_all": 18309,
        "sales_all_value": 71787
      }
    },
    "tonnel": {
      "collection_floor": 2,
      "model_floor": 10.2,
      "sales_stat": {
        "sales_24h": 68,
        "sales_24h_value": 218,
        "sales_all": 80013,
        "sales_all_value": 327740
      }
    }
  },
  "rarity_index": 0.00003,
  "telegram_gift_id": 5774079931671643000,
  "telegram_gift_name": "EasterEgg-1",
  "telegram_gift_number": 150212,
  "telegram_gift_title": "Easter Egg",
  "telegram_nft_url": "https://t.me/nft/EasterEgg-1",
  "total_amount": 173176
}
```

---

## Receive user's gifts

**GET** `/api/v1/gifts/get_gift_by_user`

**Query Parameters:**

- `username` *(string, required)*
- `limit` *(integer, required)* — How many gifts to return  
- `offset` *(integer, optional)* — For pagination

**Response:**
```json
[
  {
    "attributes": {
      "BACKDROP": {
        "media": "https://giftasset.pro/api/v1/data/backdrops/chocolate.png",
        "name": "Chocolate",
        "rarity": 10,
        "readable_rarity": 1
      },
      "MODEL": {
        "media": "https://giftasset.pro/api/v1/data/models/garnet.png",
        "name": "Garnet",
        "rarity": 24,
        "readable_rarity": 2.4
      },
      "SYMBOL": {
        "media": "https://giftasset.pro/api/v1/data/symbols/knight.png",
        "name": "Knight",
        "rarity": 10,
        "readable_rarity": 1
      }
    },
    "attributes_array": [
      {
        "name": "Knight",
        "rarity": 1,
        "type": "SYMBOL"
      },
      {
        "name": "Chocolate",
        "rarity": 1,
        "type": "BACKDROP"
      },
      {
        "name": "Garnet",
        "rarity": 2.4,
        "type": "MODEL"
      }
    ],
    "collectible_id": 2072,
    "id": 692564,
    "last_updated_at": "2025-08-16T07:09:02Z",
    "market_floor": {
      "avg": 80,
      "max": 85,
      "min": 76
    },
    "media": {
      "lottie_anim": "https://nft.fragment.com/gift/astralshard-2072.lottie.json",
      "pics": {
        "large": "https://nft.fragment.com/gift/astralshard-2072.large.jpg",
        "medium": "https://nft.fragment.com/gift/astralshard-2072.medium.jpg",
        "small": "https://nft.fragment.com/gift/astralshard-2072.small.jpg"
      }
    },
    "media_preview": "https://nft.fragment.com/gift/astralshard-2072.medium.jpg",
    "providers": {
      "getgems": {
        "collection_floor": 76,
        "model_floor": 100,
        "sales_stat": {
          "sales_24h": 1,
          "sales_24h_value": 135,
          "sales_all": 24,
          "sales_all_value": 2293
        }
      },
      "portals": {
        "collection_floor": 79,
        "model_floor": 130,
        "sales_stat": {
          "sales_24h": 10,
          "sales_24h_value": 772,
          "sales_all": 1622,
          "sales_all_value": 149899
        }
      },
      "tonnel": {
        "collection_floor": 85,
        "model_floor": 90,
        "sales_stat": {
          "sales_24h": 4,
          "sales_24h_value": 350,
          "sales_all": 2410,
          "sales_all_value": 175386
        }
      }
    },
    "rarity_index": 0.00024,
    "telegram_gift_id": 5830425027807282000,
    "telegram_gift_name": "AstralShard-2072",
    "telegram_gift_number": 5370,
    "telegram_gift_title": "Astral Shard",
    "telegram_nft_url": "https://t.me/nft/AstralShard-2072",
    "total_amount": 6196
  }
]
```

---

## Get the cost of a user's profile

**GET** `/api/v1/gifts/get_user_profile_price`

**Query Parameters:**

- `username` *(string, required)*  
- `limit` *(integer, required)*  
- `offset` *(integer, optional)*  

**Response:** `200 OK`

---

## Get the top sales volume of individual attributes per day

**GET** `/api/v1/gifts/get_attribute_volumes`

**Response:** `200 OK`

---

## Get collection buy offers

**POST** `/api/v1/gifts/get_collection_offers`

**Request Body:**

{
  "collection_name": "Evil Eye"
}

**Response:** `200 OK`

---

## Get the top sales volume of individual collections per N time

**GET** `/api/v1/gifts/get_custom_collections_volumes`

**Query Parameters:**

- `maxtime` *(integer, required)* — Time in seconds (e.g., 3600)

**Response:** `200 OK`

---

## Get fee per provider

**GET** `/api/v1/gifts/get_providers_fee`

**Response:** `200 OK`

---

## Get sales history of current provider

**GET** `/api/v1/gifts/get_providers_sales_history`

**Query Parameters:**

- `provider_name` *(string, required)* — e.g. `tonnel`  
- `limit` *(integer, required)*  
- `offset` *(integer, required)*  

**Response:** `200 OK`

---

## Get providers' sales volumes

**GET** `/api/v1/gifts/get_providers_volumes`

**Response:** `200 OK`

---

## Get the top deals of the day

**GET** `/api/v1/gifts/get_top_best_deals`

**Response:** `200 OK`

---

## Get collections emission

**GET** `/api/v1/gifts/get_gifts_collections_emission`

**Response:** `200 OK`

---

## Get gift prices

**GET** `/api/v1/gifts/get_gifts_price_list`

**Response:** `200 OK`

---

## Get gift price list history

**GET** `/api/v1/gifts/get_gifts_price_list_history`

**Response:** `200 OK`

---

## Get gifts update statistics

**GET** `/api/v1/gifts/get_gifts_update_stat`

**Response:** `200 OK`
