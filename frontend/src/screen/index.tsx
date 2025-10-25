import { Route, Routes } from "react-router";
import PostList from "./post_lists";
import Messages from "./messages";

export default function Screen() {
  return (
    <div className="w-full h-full bg-red-300">
      <Routes>
        <Route path="/" element={<PostList />} />
        <Route path="/messages" element={<Messages />} />
      </Routes>
    </div>
  );
}
