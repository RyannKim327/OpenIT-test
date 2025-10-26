
import React from 'react';
import logo from '../assets/logo.png';

const Navbar: React.FC = () => {
  return (
  <nav className="w-full bg-white text-gray-900 shadow-md flex items-center justify-between px-8 py-4 font-piazzolla sticky top-0 z-50 min-h-[72px]">
      <div className="flex items-center gap-3">
  <img src={logo} alt="SereneMind Logo" className="h-14 w-14 object-contain" />
  <span className="font-extrabold text-[20px] tracking-wide" style={{ fontFamily: 'Georgia, serif', color: '#4FA59B', fontWeight: 900 }}>SereneMind Hub</span>
      </div>
      <div className="flex gap-8 flex-1 justify-center font-thin">
  <a href="/" className="transition-colors" style={{ color: '#6C6C6C', fontWeight: 400 }} onMouseOver={e => (e.currentTarget.style.color = '#4FA59B')} onMouseOut={e => (e.currentTarget.style.color = '#6C6C6C')}>Home</a>
  <a href="/posts" className="transition-colors" style={{ color: '#6C6C6C', fontWeight: 400 }} onMouseOver={e => (e.currentTarget.style.color = '#4FA59B')} onMouseOut={e => (e.currentTarget.style.color = '#6C6C6C')}>Post</a>
  <a href="/messages" className="transition-colors" style={{ color: '#6C6C6C', fontWeight: 400 }} onMouseOver={e => (e.currentTarget.style.color = '#4FA59B')} onMouseOut={e => (e.currentTarget.style.color = '#6C6C6C')}>Messages</a>
  <a href="/profile" className="transition-colors" style={{ color: '#6C6C6C', fontWeight: 400 }} onMouseOver={e => (e.currentTarget.style.color = '#4FA59B')} onMouseOut={e => (e.currentTarget.style.color = '#6C6C6C')}>Profile</a>
      </div>
      <div className="flex gap-3">
        <button
          className="px-5 py-2 rounded-md bg-white border font-semibold transition-colors hover:bg-gray-100 hover:border-gray-300"
          style={{ borderColor: '#EAEAEA', color: '#222' }}
        >
          Log In
        </button>
        <button
          className="px-5 py-2 rounded-md font-semibold transition-colors ml-2 hover:brightness-90"
          style={{ background: '#4FA59B', color: '#fff' }}
        >
          Sign Up
        </button>
      </div>
    </nav>
  );
};

export default Navbar;
