import httpx
import asyncio

real_debrid_api_token = "YOUR_REAL_DEBRID_API_TOKEN"  # Ensure you have your actual token here
torrent_hash = "0c36703b5442d7168ba560b9067acaf62d21fefc"  # Keep the hash as a constant for easy modification
headers = {"Authorization": f"Bearer {real_debrid_api_token}"}

async def check_rd_cache(torrent_hash):
    api_url = f"https://api.real-debrid.com/rest/1.0/torrents/instantAvailability/{torrent_hash}"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(api_url, headers=headers)
            response.raise_for_status()
            data = response.json()
            
            # Assuming 'rd' contains cached file details
            if torrent_hash in data and 'rd' in data[torrent_hash]:
                files_info = data[torrent_hash]['rd'][0]  # Access the first item assuming it's structured consistently
                for file_id, file_details in files_info.items():
                    filename = file_details['filename']
                    filesize = file_details['filesize']
                    print(f"File: {filename}, Size: {filesize}")
            else:
                print("No data available for the given torrent hash.")
            return data
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(check_rd_cache(torrent_hash))
