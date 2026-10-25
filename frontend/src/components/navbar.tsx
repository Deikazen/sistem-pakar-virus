const links = [
  ["/", "Beranda", "⌂"],
  ["/latar-belakang", "Latar Belakang", "○"],
  ["/metodologi", "Metodologi", "◇"],
  ["/artikel-edukasi", "Artikel Edukasi", "▤"],
  ["/skrining-awal", "Skrining Awal", "✓"],
  ["/rekomendasi-lab", "Rekomendasi Lab", "⌕"],
];

export default function Navbar({ active, open, onNavigate }: { active: string; open: boolean; onNavigate: () => void }) {
  return <aside className={`sidebar ${open ? "open" : ""}`}><nav aria-label="Navigasi utama">{links.map(([href, label, icon]) => <a onClick={onNavigate} href={href} className={`nav-link ${active === href ? "active" : ""}`} key={href}><span className="nav-icon">{icon}</span><span>{label}</span></a>)}</nav><div className="side-help"><b>Butuh bantuan?</b><span>Informasi ini bukan pengganti konsultasi dokter.</span></div></aside>;
}
