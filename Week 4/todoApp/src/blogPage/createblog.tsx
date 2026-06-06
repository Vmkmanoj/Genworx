import { useState } from "react";
import { Button, Input } from "antd";

const { TextArea } = Input;

export const CreateBlog = () => {
  const [name, setName] = useState("");
  const [blog, setBlog] = useState("");

  const handlePost = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/create-post", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name,
          blog,
        }),
      });

      const data = await response.json();

      console.log(data);

      setName("");
      setBlog("");
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: "30px",
        padding: "30px",
      }}
    >
      <label>Name :</label>

      <Input
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{ width: "400px", height: "40px" }}
      />

      <label>Blog :</label>

      <TextArea
        value={blog}
        onChange={(e) => setBlog(e.target.value)}
        style={{ width: "400px" }}
      />

      <Button
        type="primary"
        onClick={handlePost}
        style={{ width: "400px", height: "40px" }}
      >
        Post
      </Button>
    </div>
  );
};