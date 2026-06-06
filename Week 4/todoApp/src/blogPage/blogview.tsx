import { useEffect, useState } from "react";

interface Blog {
  Id: number;
  name: string;
  blog: string;
  CreateDateAndTime: string;
}
export const BlogView = () => {
  const [blogs, setBlogs] = useState<Blog[]>([]);

  const getBlogs = async () => {
    try {
      const response = await fetch(
        "http://127.0.0.1:8000/get-all-post"
      );

      const data = await response.json()

      setBlogs(data)
      
    } catch (error) {
      console.error("Error fetching blogs:", error);
    }
  };

  useEffect(() => {
    if (blogs.length === 0){
    getBlogs();
    }
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>All Blogs</h1>

      {blogs.length === 0 ? (
        <p>No blogs found</p>
      ) : (
        blogs.map((blog) => (
          <div
            key={blog.Id}
            style={{
              border: "1px solid #ddd",
              padding: "15px",
              marginBottom: "15px",
              borderRadius: "8px",
            }}
          >
            <h3>{blog.name}</h3>

            <p>{blog.blog}</p>

            {blog.CreateDateAndTime && (
              <small>
                Created:
                {" "}
                {new Date(blog.CreateDateAndTime).toLocaleString()}
              </small>
            )}
          </div>
        ))
      )}
    </div>
  );
};