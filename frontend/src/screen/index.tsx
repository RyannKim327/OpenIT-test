import { Route, Routes } from "react-router";
import HomePage from "./HomePage";
import PostList from "./post_lists";
import Messages from "./messages";

export default function Screen() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/posts" element={<PostList />} />
      <Route path="/messages" element={<Messages />} />
    </Routes>
  );
}
