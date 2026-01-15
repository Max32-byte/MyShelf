import React, { useEffect, useState } from "react";

export default function MemberList() {
  const [members, setMembers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const memberListApi = "http://localhost:8000/members";
  useEffect(() => {
    const fetchMembers = async () => {
      try {
        const response = await fetch(memberListApi);
        if (!response.ok) {
          throw new Error("Failed to fetch members");
        }
        const data = await response.json();

        let membersArray = [];
        if (Array.isArray(data)) {
          membersArray = data;
        } else if (data && Array.isArray(data.members)) {
          membersArray = data.members;
        } else {
          membersArray = [];
        }

        setMembers(membersArray);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };
    console.log(members);
    fetchMembers();
  }, []);

  if (loading) return <p style={{ padding: "32px" }}>Leden laden...</p>;
  if (error) return <p style={{ padding: "32px" }}>Fout bij laden: {error}</p>;

  return (
    <section
      style={{
        padding: "32px",
        backgroundColor: "#ecfdf5",
        minHeight: "calc(100vh - 85px)",
      }}
    >
      <h2 style={{ color: "#064e3b", marginBottom: "16px" }}>Leden</h2>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit,minmax(220px,1fr))",
          gap: "16px",
        }}
      >
        {members.map((member) => (
          <div
            key={member.id}
            style={{
              padding: "16px",
              borderRadius: "12px",
              backgroundColor: "#ffffff",
              boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
            }}
          >
            <h3 style={{ margin: "0 0 8px", color: "#0891b2" }}>
              {member.name}
            </h3>
            <p style={{ margin: "0 0 8px" }}>
              <strong>Email:</strong> {member.email}
            </p>
            <p style={{ margin: "0 0 8px" }}>
              <strong>Member ID:</strong> {member.id}
            </p>
            <p style={{ margin: 0 }}>
              <strong>Geleende boeken:</strong>{" "}
              {member.borrowed_books.join(", ") || "Geen"}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}
