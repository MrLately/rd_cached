import httpx
import asyncio

torrent_hash = "0c36703b5442d7168ba560b9067acaf62d21fefc"
real_debrid_api_token = ""

async def check_rd_cache(torrent_hash):
    api_url = f"https://api.real-debrid.com/rest/1.0/torrents/instantAvailability/{torrent_hash}"
    headers = {"Authorization": f"Bearer {real_debrid_api_token}"}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    result = asyncio.run(check_rd_cache(torrent_hash))
    print(result)
