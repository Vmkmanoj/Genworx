
import {useState} from "react"


export const todo = () =>{

  const [todo, setTodo] = useState("");
  const [data, setData] = useState<string[]>([]);


  const addData = () => {
    if (todo.trim() === "") return;

    setData([...data, todo]);
    setTodo("");
  };



  return (
    <>
      <div
        className="body"
        style={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: "20px",
          padding: "100px",
        }}
      >
        <div style={{ display: "flex", gap: "10px" }}>
          <input
            style={{ height: "30px", width: "500px" }}
            value={todo}
            onChange={(e) => setTodo(e.target.value)}
          />

          <button onClick={addData} style={{ height: "35px" }}>
            Add
          </button>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
          {data.map((item, index) => (
            <p key={index} style={{ margin: 0 }}>
              {item}
            </p>
          ))}
        </div>
      </div>

    </>
  )



}