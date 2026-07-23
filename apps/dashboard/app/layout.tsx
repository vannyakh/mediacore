import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "MediaCore Dashboard",
  description: "Jobs, plugins, providers, workers, and system health",
};

const NAV = [
  "Overview",
  "Jobs",
  "Queue",
  "Plugins",
  "Providers",
  "API Keys",
  "Users",
  "Logs",
  "Metrics",
  "Storage",
  "Workers",
  "Settings",
] as const;

function hrefFor(label: string): string {
  return "/" + label.toLowerCase().replace(/\s+/g, "-");
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <div className="shell">
          <aside className="sidebar">
            <div className="brand">MediaCore</div>
            <nav>
              {NAV.map((item) => (
                <Link key={item} href={hrefFor(item)}>
                  {item}
                </Link>
              ))}
            </nav>
          </aside>
          <main className="content">{children}</main>
        </div>
      </body>
    </html>
  );
}
