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
  wc: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M11 4H7a1 1 0 00-1 1v4c0 2.5 1.5 4.5 3 5.5V18h4v-3.5c1.5-1 3-3 3-5.5V5a1 1 0 00-1-1h-4z" />
      <path d="M11 4V2M13 4V2" />
      <path d="M10 18v2h4v-2" />
    </g>
  ),
  shower: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M4 20l5-5" />
      <path d="M9 15a5 5 0 005-5" />
      <circle cx="16" cy="8" r="2" />
      <path d="M7 18l-1 2M10 19l-1 2M13 20l-1 2" />
    </g>
  ),
  kitchen: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M6 3v4M8 3v4M7 7c0 2-1 3-1 5h4c0-2-1-3-1-5" />
      <path d="M15 3c0 3 2 5 2 7h-4c0-2 2-4 2-7z" />
      <path d="M5 15h14v3a2 2 0 01-2 2H7a2 2 0 01-2-2v-3z" />
    </g>
  ),
  grill: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M8 3c.5 1 .5 2 0 3M12 3c.5 1 .5 2 0 3M16 3c.5 1 .5 2 0 3" />
      <path d="M3 9h18" />
      <path d="M5 9l2 9h10l2-9" />
      <path d="M12 18v3M9 21h6" />
    </g>
  ),
  electric: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M13 2L4.5 13.5H12L11 22l8.5-11.5H12.5L13 2z" />
    </g>
  ),
  water: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 2C12 2 5 10 5 15a7 7 0 0014 0c0-5-7-13-7-13z" />
    </g>
  ),
  dump: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M9.5 2.5h5a1 1 0 011 1V5c0 1.9-1 3.4-2.3 4.2h-2.4C9.5 8.4 8.5 6.9 8.5 5V3.5a1 1 0 011-1z" />
      <path d="M10.8 9.2v1.6h2.4V9.2" />
      <path d="M12 12.8v1.7M9.6 12.3v1.4M14.4 12.3v1.4" />
      <path d="M5 17h14" />
      <path d="M7 17v2a2 2 0 002 2h6a2 2 0 002-2v-2" />
    </g>
  ),
  chemical: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M9 3h6M10 3v4l-4 6a4 4 0 000 8h12a4 4 0 000-8l-4-6V3" />
      <path d="M8 17h2M12 15h2" />
    </g>
  ),
  checkin: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="12" cy="8" r="3" />
      <path d="M10 11l-5 9h14l-5-9" />
      <path d="M15 3h4v4" />
      <path d="M19 3l-4 4" />
    </g>
  ),
  pets: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M10 5.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM17 5.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM7 10.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM20 10.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z" />
      <path d="M12 13c-3 0-6 2-6 5 0 1.5 1 2 2 2 1.5 0 2.5-1 4-1s2.5 1 4 1c1 0 2-.5 2-2 0-3-3-5-6-5z" />
    </g>
  ),
  trash: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M3 6h18M8 6V4h8v2" />
      <path d="M19 6l-1 14a2 2 0 01-2 2H8a2 2 0 01-2-2L5 6" />
      <path d="M10 11v5M14 11v5" />
    </g>
  ),
  washer: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="3" width="18" height="18" rx="2" />
      <circle cx="12" cy="13" r="4" />
      <path d="M8 7h.01M11 7h2" />
    </g>
  ),
  location: (
    <g fill="none" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 2C8.686 2 6 4.686 6 8c0 4.5 6 13 6 13s6-8.5 6-13c0-3.314-2.686-6-6-6z" />
      <circle cx="12" cy="8" r="2.2" />
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
