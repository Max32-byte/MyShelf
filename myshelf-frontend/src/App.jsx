import { useState } from "react";
import Header from "./components/Header.jsx";
import BookList from "./components/BookList.jsx";
import MemberList from "./components/MemberList.jsx";
import BorrowBook from "./components/BorrowBook.jsx";
import ReturnBook from "./components/ReturnBook.jsx";

// Dummy data (kan je vervangen met fetch vanaf backend)


export default function App() {
  const [page, setPage] = useState("home"); 

  // Voor navigatie vanuit header
  const handleNavClick = (target) => {
    setPage(target);
  };

  return (
    <div
      style={{
        fontFamily: "sans-serif",
        backgroundColor: "#ecfdf5",
        minHeight: "100vh",
      }}
    >
      <Header />

      {/* Simpele navigatie */}
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          gap: "16px",
          padding: "16px",
        }}
      >
        <button onClick={() => handleNavClick("books")} style={buttonStyle}>
          Boeken
        </button>
        <button onClick={() => handleNavClick("members")} style={buttonStyle}>
          Leden
        </button>
        <button onClick={() => handleNavClick("borrow")} style={buttonStyle}>
          Uitlenen
        </button>
        <button onClick={() => handleNavClick("return")} style={buttonStyle}>
          Teruggeven
        </button>
      </div>

      {/* Pagina content */}
      <main>
        {page === "books" && <BookList />}
        {page === "members" && <MemberList />}
        {page === "borrow" && <BorrowBook />}
        {page === "return" && <ReturnBook />}
        {page === "home" && (
          <section
            style={{ padding: "32px", textAlign: "center", color: "#064e3b" }}
          >
            <h2>Welkom bij de Bibliotheek</h2>
            <p>
              Gebruik de knoppen hierboven om boeken te bekijken, leden te
              beheren of boeken uit te lenen/terug te geven.
            </p>
          </section>
        )}
      </main>
    </div>
  );
}

// Herbruikbare button style
const buttonStyle = {
  padding: "8px 16px",
  borderRadius: "8px",
  border: "none",
  backgroundColor: "#059669",
  color: "white",
  cursor: "pointer",
};
