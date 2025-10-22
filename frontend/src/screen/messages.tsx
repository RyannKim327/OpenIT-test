import { useEffect, useState } from "react";
import axios from "axios";

export default function Messages() {
  const [messages, setMessages] = useState([]);
  const username = "";

  useEffect(() => {
    (async () => {
      const { data } = await axios.get("url here");
      setMessages(data);
    })();
  }, []);

  return (
    <div>
      {messages.map((message) => {
        return (
          <div>
            <h3>
              {message.is_anon
                ? "Anonymous"
                : message.user1 === username
                  ? "You"
                  : message.user1}
            </h3>
            <blockquote>
              <p>{message.message}</p>
            </blockquote>
          </div>
        );
      })}
    </div>
  );
}
