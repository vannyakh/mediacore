const NODES = [
  "URL",
  "Analyze",
  "Download",
  "Convert",
  "Subtitle",
  "Translate",
  "Thumbnail",
  "Export",
];

export default function App() {
  return (
    <main style={{ fontFamily: "IBM Plex Sans, sans-serif", padding: "2rem" }}>
      <h1>MediaCore Studio</h1>
      <p>Visual workflow builder scaffold (React Flow in v0.4).</p>
      <ol>
        {NODES.map((n) => (
          <li key={n}>{n}</li>
        ))}
      </ol>
    </main>
  );
}
