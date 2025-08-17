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

{
  "include": ["Evil Eye"],
  "exclude": ["Evil Eye"]
}

- `include` *(array of strings)* — Only the specified collections  
- `exclude` *(array of strings)* — All except the specified collections  

**Response:** `200 OK`

---

## Receive gift by name

**GET** `/api/v1/gifts/get_gift_by_name`

**Query Parameters:**

- `name` *(string, required)* — Gift name (e.g., `EasterEgg-1`)

**Response:** `200 OK`

---

## Receive user's gifts

**GET** `/api/v1/gifts/get_gift_by_user`

**Query Parameters:**

- `username` *(string, required)*
- `limit` *(integer, required)* — How many gifts to return  
- `offset` *(integer, optional)* — For pagination

**Response:** `200 OK`

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
