import type { Metadata } from "next";
import { Nav } from "@/components/Nav";
import "./globals.css";

export const metadata: Metadata = {
  title: "MediaCore Dashboard",
  description: "Jobs, plugins, providers, workers, and system health",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="shell">
          <aside className="sidebar">
            <div className="brand">MediaCore</div>
            <Nav />
          </aside>
          <main className="content">{children}</main>
        </div>
      </body>
    </html>
  );
}
