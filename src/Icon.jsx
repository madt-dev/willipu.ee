const paths = {
  wave: (
    <path
      d="M3 14c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3M3 19c3 0 3-3 6-3s3 3 6 3 3-3 6-3 3 3 6 3"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinecap="round"
    />
  ),
  bike: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="6" cy="18" r="3.5" />
      <circle cx="18" cy="18" r="3.5" />
      <path d="M6 18l4-8h6l2 8M10 10l-2-4h2" />
    </g>
  ),
  ball: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8">
      <circle cx="12" cy="12" r="9" />
      <path d="M3 12c3-2 7-2 9 0s6 2 9 0M12 3c-2 3-2 7 0 9s2 6 0 9M3 12c2-3 7-2 9 0M12 12c-3 2-2 7 0 9" />
    </g>
  ),
  fire: (
    <path
      d="M12 3c1 3-2 4-2 7 0 2 1 3 2 3s2-1 2-3c2 1 3 3 3 5a5 5 0 11-10 0c0-3 2-4 3-7 1-2 2-3 2-5z"
      fill="none"
      stroke="currentColor"
      strokeWidth="1.8"
      strokeLinejoin="round"
    />
  ),
  hall: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinejoin="round">
      <path d="M3 20V9l9-5 9 5v11" />
      <path d="M3 20h18M9 20v-6h6v6" />
    </g>
  ),
  wifi: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round">
      <path d="M3 9a14 14 0 0118 0" />
      <path d="M6 13a9 9 0 0112 0" />
      <path d="M9 17a4 4 0 016 0" />
      <circle cx="12" cy="19.5" r=".9" fill="currentColor" stroke="none" />
    </g>
  ),
}

export function Icon({ name }) {
  return (
    <svg viewBox="0 0 24 24" width="28" height="28" aria-hidden>
      {paths[name] ?? null}
    </svg>
  )
}
