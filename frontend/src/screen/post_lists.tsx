import { useEffect, useState } from "react";
import { uget } from "../utils/api";

export default function PostList() {
  const [postList, setPostList] = useState([]);
  useEffect(() => {
    (async () => {
      const posts = await uget("posts");
      setPostList(posts.data);
    })();
  }, []);
  return (
    <div>
      <h1>Post list</h1>
      {postList.length <= 0 ? (
        <div>
          <h1>Please wait</h1>
        </div>
      ) : (
        postList.map((post) => {
          return (
            <div className="shadow-gray-300 shadow-md p-2 m-2 rounded">
              <h1>{post.title}</h1>
              <h3 className="ml-4">
                {post.is_anonymous ? "Anonymous User" : post.user_info.username}
              </h3>
            </div>
          );
        })
      )}
    </div>
  );
}
