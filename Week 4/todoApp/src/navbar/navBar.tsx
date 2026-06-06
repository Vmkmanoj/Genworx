
import {Link} from "react-router-dom"

export const NavBar = () =>{
   return(
    <>
    <div style={{display:"flex", justifyContent:"center",alignItems:"center",gap:"20px", height:"100px",padding:"20px",background:"#000000" }}>
      <Link to="/" style={{textDecoration:"none" ,fontSize:"30px"}}>Home</Link>
      <Link to="/blog" style={{textDecoration:"none",fontSize:"30px"}}>blog</Link>
    </div>
    </>
   )
}