"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const NAV = [
  "Overview",
  "Jobs",
  "Events",
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

export function Nav() {
  const pathname = usePathname();

  return (
    <nav>
      {NAV.map((item) => {
        const href = hrefFor(item);
        const active = pathname === href || pathname.startsWith(href + "/");
        return (
          <Link key={item} href={href} className={active ? "active" : undefined}>
            {item}
          </Link>
        );
      })}
    </nav>
  );
}
