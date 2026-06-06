import {Routes,Route} from "react-router-dom"
import { CreateBlog } from "./blogPage/createblog"
import { BlogView } from "./blogPage/blogview"
import { NavBar } from "./navbar/navBar"
import "./App.css"

function App() {

  return(
      <>
     <NavBar></NavBar>
      <Routes>

        <Route path="/" element={<CreateBlog/>}></Route>
        <Route path="/blog" element={<BlogView/>}></Route>
      </Routes>
      </>
  )

}

export default App
