export default function Navbar() {
  return (
    <nav
      style={{
        display: "flex",
        gap: "10px",
        padding: "10px",
      }}
    >
      <ol
        style={{
          listStyleType: "none",
          paddingLeft: 0, // Menghilangkan spasi kosong bawaan <ol> di sebelah kiri
          margin: 0, // Menghilangkan margin bawaan
          display: "flex",
          flexDirection: "column",
          alignItems: "flex-start", // Memaksa semua item <li> rata di sisi kiri
          gap: "30px",
        }}
      >
        <li>
          <a href="/">Home</a>
        </li>
        <li>
          <a href="/latar">Latar Belakang</a>
        </li>
        <li>
          <a href="/metodologi">Metodologi</a>
        </li>
        <li>
          <a href="/artikel">Artikel</a>
        </li>
        <li>
          <a href="/skrining">Skrining</a>
        </li>
        <li>
          <a href="/rekomendasi">Rekomendasi Lab</a>
        </li>
      </ol>
    </nav>
  );
}
