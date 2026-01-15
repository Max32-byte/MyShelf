import logo from "../assets/logo.png";

export default function Header() {
  return (
    <header
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "16px 32px",
        backgroundColor: "#059669",
        color: "#ffffff",
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: "10px" }}>
        <img src={logo} alt="Logo" style={{ height: "50px" }} />
        <h1 style={{ fontSize: "1.8rem", fontWeight: "bold" }}>My Shelf</h1>
      </div>
    </header>
  );
}
