// eslint-disable-next-line react/prop-types
export default function SvgComponent({color}) {
  return (
    <svg viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M13.188 3l-.157.813-.594 2.968a9.939 9.939 0 00-2.593 1.532l-2.906-1-.782-.25-.406.718-2 3.438-.406.719.594.53 2.25 1.97C6.104 14.948 6 15.46 6 16c0 .54.105 1.05.188 1.563l-2.25 1.968-.594.532.406.718 2 3.438.406.718.782-.25 2.906-1a9.939 9.939 0 002.594 1.532l.593 2.968.156.813h5.626l.156-.813.593-2.968a9.939 9.939 0 002.594-1.532l2.907 1 .78.25.407-.718 2-3.438.406-.718-.593-.532-2.25-1.968C25.895 17.05 26 16.538 26 16c0-.54-.105-1.05-.188-1.563l2.25-1.968.594-.531-.406-.72-2-3.437-.406-.718-.782.25-2.906 1a9.939 9.939 0 00-2.593-1.532l-.594-2.968L18.812 3zm1.624 2h2.376l.5 2.594.125.593.562.188a8.017 8.017 0 013.031 1.75l.438.406.562-.187 2.532-.875 1.187 2.031-2 1.781-.469.375.157.594c.128.57.187 1.152.187 1.75 0 .598-.059 1.18-.188 1.75l-.125.594.438.375 2 1.781-1.188 2.031-2.53-.875-.563-.187-.438.406a8.017 8.017 0 01-3.031 1.75l-.563.188-.125.593-.5 2.594h-2.375l-.5-2.594-.124-.593-.563-.188a8.017 8.017 0 01-3.031-1.75l-.438-.406-.562.187-2.531.875L5.875 20.5l2-1.781.469-.375-.156-.594A7.901 7.901 0 018 16c0-.598.059-1.18.188-1.75l.156-.594-.469-.375-2-1.781 1.188-2.031 2.53.875.563.187.438-.406a8.017 8.017 0 013.031-1.75l.563-.188.124-.593zM16 11c-2.75 0-5 2.25-5 5s2.25 5 5 5 5-2.25 5-5-2.25-5-5-5zm0 2c1.668 0 3 1.332 3 3s-1.332 3-3 3-3-1.332-3-3 1.332-3 3-3z"
        fill={color}
      />
    </svg>
  );
}
