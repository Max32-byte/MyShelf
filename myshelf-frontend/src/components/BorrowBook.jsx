import { useState } from "react";

export default function BorrowBook() {
  const [isbn, setIsbn] = useState("");
  const [memberId, setMemberId] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(
        `http://localhost:8000/borrow/${isbn}/${memberId}`,
        { method: "POST" }
      );

      const data = await response.json();

      if (!response.ok) {
        alert(data.detail);
        return;
      }

      alert("Boek succesvol uitgeleend!");
      setIsbn("");
      setMemberId("");
    } catch (error) {
      alert("Server niet bereikbaar");
      console.error(error);
    }
  };

  return (
    <section
      style={{
        padding: "32px",
        backgroundColor: "#ecfdf5",
        minHeight: "calc(100vh - 85px)",
      }}
    >
      <h2 style={{ color: "#064e3b", marginBottom: "16px" }}>Boek uitlenen</h2>

      <form
        onSubmit={handleSubmit}
        style={{
          display: "flex",
          flexDirection: "column",
          gap: "16px",
          maxWidth: "400px",
          backgroundColor: "#ffffff",
          padding: "24px",
          borderRadius: "12px",
          boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
        }}
      >
        <label>
          ISBN van het boek:
          <input
            type="text"
            name="isbn"
            value={isbn}
            onChange={(e) => setIsbn(e.target.value)}
            style={{
              width: "100%",
              padding: "8px",
              marginTop: "4px",
              borderRadius: "8px",
              border: "1px solid #ccc",
            }}
          />
        </label>

        <label>
          Lid ID:
          <input
            type="number"
            name="memberId"
            value={memberId}
            onChange={(e) => setMemberId(e.target.value)}
            style={{
              width: "100%",
              padding: "8px",
              marginTop: "4px",
              borderRadius: "8px",
              border: "1px solid #ccc",
            }}
          />
        </label>

        <button
          type="submit"
          style={{
            backgroundColor: "#059669",
            color: "white",
            padding: "12px",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer",
          }}
        >
          Uitlenen
        </button>
      </form>
    </section>
  );
}
