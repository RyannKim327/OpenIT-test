import React from 'react';

const Footer: React.FC = () => {
	return (
		<footer className="w-full bg-[#f7faf9] border-t border-[#eaeaea] text-[#4FA59B] font-piazzolla">
			<div className="max-w-5xl mx-auto flex flex-col md:flex-row items-center justify-between py-6 px-4 gap-4">
				<div className="flex items-center gap-2">
					<span className="font-extrabold text-xl tracking-wide" style={{ fontFamily: 'Georgia, serif', color: '#4FA59B', fontWeight: 900 }}>SereneMind Hub</span>
				</div>
				<div className="flex gap-6 text-sm">
					<a href="/" className="hover:text-[#2e7d6b] transition-colors">Home</a>
					<a href="/about" className="hover:text-[#2e7d6b] transition-colors">About</a>
					<a href="/contact" className="hover:text-[#2e7d6b] transition-colors">Contact</a>
				</div>
			</div>
			<div className="text-center text-xs text-[#6C6C6C] pb-4">© 2025 SereneMind. All rights reserved.</div>
		</footer>
	);
};

export default Footer;
