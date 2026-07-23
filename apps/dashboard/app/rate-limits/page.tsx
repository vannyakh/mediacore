import { redirect } from "next/navigation";

export default function RateLimitsAliasPage() {
  redirect("/api-keys");
}