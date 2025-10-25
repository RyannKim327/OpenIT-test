import { Home, Mail } from "lucide-react";
import { Link } from "react-router";
import Logo from "./../assets/logo.png";

export default function Header() {
  return (
    <div className="flex flex-row gap-1 justify-between items-center px-2">
      <img src={Logo} height={50} width={50} />
      <div className="flex flex-row gap-1">
        <Link to="/" title="Home">
          <Home size={24} color="#6E43EB" />
        </Link>
        <Link to="/messages" title="Messages">
          <Mail size={24} color="#6E43EB" />
        </Link>
      </div>
    </div>
  );
}
