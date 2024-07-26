import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')

    # Iterate through all json files in the directory.
    for path in pathlist:
        print(path)

        async with aiofiles.open(path,mode='r') as f:
            contents = await f.read()

        # Load it into a dictionary and create a list of moves.
        pokemon = json.loads(contents)
        name = pokemon['name']
        moves = [move['move']['name']for move in pokemon['moves'] ]   

        # Open a new file in write the list of moves into.
        async with aiofiles.open(f'{pokemonmove_directory}/{name}_moves.txt',mode='w') as f:
            await f.write('\n'.join(moves))

asyncio.run(main())
