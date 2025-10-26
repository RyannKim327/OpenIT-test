
import logo from '../assets/logo.png';
import React from 'react';
import Footer from '../layout/Footer';


const HomePage: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <div className="w-full" style={{ background: 'linear-gradient(180deg, rgba(79,165,155,0.3) 0%, rgba(79,165,155,0.05) 100%)' }}>
        <div className="max-w-3xl mx-auto flex flex-col items-center justify-center py-12">
          <h1 className="text-4xl md:text-5xl font-extrabold mb-4 text-center" style={{ color: '#4FA59B', fontFamily: 'Georgia, serif' }}>
            Welcome to SereneMind Hub
          </h1>
              <p className="text-base md:text-lg text-center mb-8 max-w-4xl leading-relaxed" style={{ color: '#535353' }}>
                A safe space where mental wellness and self-growth come together. Join our community to share, learn, and support one another on the journey toward inner peace.
              </p>
              <button className="flex flex-col items-center justify-center bg-[#4FA59B] rounded-2xl px-8 py-3 shadow-lg hover:brightness-95 transition">
                <span className="text-white font-bold text-md tracking-wide">Share Your Story</span>
              </button>
        </div>
      </div>
      <div className="w-full flex flex-col items-center py-8">
        <div className="flex w-full max-w-2xl gap-3">
          <input
            type="text"
            placeholder="Search post by keywords or tags..."
            className="flex-1 px-5 py-3 rounded-xl text-base outline-none"
            style={{ background: '#F9F9F9', border: '1px solid #C8C8C8', color: '#222' }}
          />
          <select
            className="px-5 py-3 rounded-xl text-base outline-none ml-2"
            style={{ background: '#F9F9F9', border: '1px solid #C8C8C8', color: '#222', minWidth: '170px' }}
            defaultValue=""
          >
            <option value="" disabled hidden>All Categories</option>
            <option value="all">All Categories</option>
            <option value="wellness">Wellness</option>
            <option value="growth">Self-Growth</option>
            <option value="support">Support</option>
          </select>
          <button
            className="px-6 py-3 rounded-xl text-base font-bold text-white"
            style={{ background: '#4FA59B' }}
          >
            Search
          </button>
        </div>
      </div>
      <section className="w-full bg-[#f9f9f9] py-10 px-4">
        <div className="max-w-5xl mx-auto w-full">
          <h2 className="text-2xl md:text-3xl font-bold text-black mb-2 text-left sm:pl-0 pl-2" style={{ fontFamily: 'Georgia, serif', color: '#222' }}>
            Browse Topics
          </h2>
          <p className="text-base md:text-lg text-left sm:pl-0 pl-2" style={{ color: '#535353' }}>Explore conversations organized by mental health themes</p>
        </div>
      </section>
      <main className="flex-1 flex flex-col items-center justify-center px-4 py-0"></main>
      <Footer />
    </div>
  );
};

export default HomePage;
