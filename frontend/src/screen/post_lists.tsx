import { useEffect, useState } from "react";
import { uget } from "../utils/api";

export default function PostList() {
  const [postList, setPostList] = useState([]);
  useEffect(() => {
    (async () => {
      const posts = await uget("post-lists");
      setPostList(posts);
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
            <div>
              <h1>{post.title}</h1>
              <h3>{post.is_anonymous ? "Anonymous User" : post.user}</h3>
            </div>
          );
        })
      )}
    </div>
  );
}
