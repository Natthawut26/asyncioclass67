import asyncio
import httpx
import time

async def fetch_data(client, url):
    print(f"{time.ctime()} - Fetching data from {url}")
    response = await client.get(url)
    return response.json()

async def fetch_ability(client, ability_url):
    ability_data = await fetch_data(client, ability_url)
    pokemon_entries = ability_data['pokemon']
    
    tasks = [fetch_data(client, entry['pokemon']['url']) for entry in pokemon_entries]
    return await asyncio.gather(*tasks)

async def index():
    start_time = time.perf_counter()

    # URLs for abilities
    urls = {
        'battle-armor': 'https://pokeapi.co/api/v2/ability/battle-armor',
        'speed-boost': 'https://pokeapi.co/api/v2/ability/speed-boost'
    }

    results = {}
    async with httpx.AsyncClient() as client:
        for ability, url in urls.items():
            start = time.perf_counter()
            pokemons = await fetch_ability(client, url)
            end = time.perf_counter()
            
            names = [pokemon['name'] for pokemon in pokemons]
            results[ability] = {
                'names': names,
                'time_taken': end - start,
                'count': len(pokemons)
            }

    end_time = time.perf_counter()

    for ability, data in results.items():
        print(f"{time.ctime()} - Asynchronous get {data['count']} pokemons with '{ability}' ability.")
        print(f"Pokémon names with '{ability}':", data['names'])
        print(f"Time taken for '{ability}': {data['time_taken']} seconds")

    print(f"Total time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    asyncio.run(index())
