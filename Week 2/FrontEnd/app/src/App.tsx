import { useEffect, useState } from "react";

const pokemonNames = ["pikachu","raichu","eevee","snorlax","lucario","gengar","dragonite","lapras","alakazam","machamp "]


function App() {
  const [pokemon, setPokemon] = useState<any>(null);
  const [name, setName] = useState("pikachu");

  

  const getPokemon = async () => {
    try {
      const res = await fetch(
        `https://pokeapi.co/api/v2/pokemon/${name.toLowerCase()}`
      );

      if (!res.ok) {
        throw new Error("Pokemon not found");
      }

      const data = await res.json();
      console.log(data)
      setPokemon(data);
    } catch (error) {
      console.error(error);
      setPokemon(null);
    }
  };

  useEffect(() => {
    getPokemon();
  }, []);

  return (
    <div>
      <input
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      {pokemonNames.map((i)=>(
        <div key={i} style={{cursor:"pointer"}}  onClick={()=>setName(i)}>
          {i}
        </div>
      ))}
a
      <button onClick={getPokemon}>
        Search
      </button>

      {pokemon && (
        <>
          <h1>{pokemon.name}</h1>
          <p>Height: {pokemon.height}</p>
          <p>Weight: {pokemon.weight}</p>

          <img
            src={pokemon.sprites.front_default}
            alt={pokemon.name}
          />
        </>
      )}
    </div>
  );
}

export default App;


