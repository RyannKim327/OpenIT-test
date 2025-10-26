import { Home, Mail, User } from "lucide-react";
import { Link, useLocation } from "react-router";
import Logo from "./../assets/logo.png";

export default function Header() {
  const location = useLocation();

  return (
    <div className="flex flex-row gap-1 justify-between items-center px-2">
      <div className="flex flex-row gap-1 items-center">
        <img src={Logo} height={50} width={50} />
        <h1 className="text-[#509A92] text-shadow-sm text-shadow-gray-300 font-bold">
          SereneMind Hub
        </h1>
      </div>
      <div className="flex flex-row gap-2">
        <Link
          to="/"
          className={`flex flex-col items-center justify-center font-bold ${location.pathname === "/" || location.pathname === "" ? "text-[#509A92]" : "text-gray-400"}`}
          title="Home"
        >
          <Home size={24} />
          <span>Home</span>
        </Link>
        <Link
          to="/messages"
          className={`flex flex-col items-center justify-center font-bold ${location.pathname === "/messages" ? "text-[#509A92]" : "text-gray-400"}`}
          title="Messages"
        >
          <Mail size={24} />
          <span>Messages</span>
        </Link>
        <Link
          to="/profile"
          className={`flex flex-col items-center justify-center font-bold ${location.pathname === "/profile" ? "text-[#509A92]" : "text-gray-400"}`}
          title="Profile"
        >
          <User size={24} />
          <span>Profile</span>
        </Link>
      </div>
      <div className="flex flex-row gap-2 items-center">
        <Link to="/login" className="text-[##509A92]">
          Log In
        </Link>
        <Link to="/register" className="bg-[#509A92] text-white p-1 roundedtex">
          Sign Up
        </Link>
      </div>
    </div>
  );
}
