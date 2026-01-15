import { useEffect, useState } from "react";

export default function BookList() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const bookListApi = "http://localhost:8000/books";

  useEffect(() => {
    const fetchBooks = async () => {
      try {
        const response = await fetch(bookListApi);
        if (!response.ok) {
          throw new Error("Failed to fetch books");
        }
        const data = await response.json();

        let booksArray = [];
        if (Array.isArray(data)) {
          booksArray = data;
        } else if (data && Array.isArray(data.books)) {
          booksArray = data.books;
        } else {
          booksArray = [];
        }

        setBooks(booksArray);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchBooks();
  }, []);

  if (loading) return <p style={{ padding: "32px" }}>Boeken laden...</p>;
  if (error) return <p style={{ padding: "32px" }}>Fout bij laden: {error}</p>;

  return (
    <section
      style={{
        padding: "32px",
        backgroundColor: "#ecfdf5",
        minHeight: "100vh",
      }}
    >
      <h2 style={{ color: "#064e3b", marginBottom: "24px" }}>Alle Boeken</h2>

      {books.length === 0 ? (
        <p>Geen boeken gevonden.</p>
      ) : (
        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))",
            gap: "16px",
          }}
        >
          {books.map((book, index) => (
            <div
              key={book.isbn || book.title || index}
              style={{
                padding: "20px",
                borderRadius: "12px",
                backgroundColor: "#ffffff",
                boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
                display: "flex",
                flexDirection: "column",
                justifyContent: "space-between",
              }}
            >
              <h3 style={{ margin: "0 0 10px", color: "#059669" }}>
                {book.title || "Titel onbekend"}
              </h3>
              <p style={{ margin: "0 0 10px" }}>
                <strong>Auteur:</strong> {book.author || "Onbekend"}
              </p>
              <p style={{ margin: "0 0 10px", fontSize: "14px" }}>
                <strong>ISBN:</strong> {book.isbn || "Onbekend"}
              </p>

              <p style={{ margin: 0 }}>
                <strong>Status:</strong>{" "}
                {book.available
                  ? "Beschikbaar"
                  : `Geleend door lid ${book.borrowed_by || "?"}`}
              </p>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}
