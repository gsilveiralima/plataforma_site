from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    index = ROOT / "index.html"
    css = ROOT / "styles.css"
    if not index.is_file() or not css.is_file():
        raise SystemExit("index.html e styles.css são obrigatórios.")

    text = index.read_text(encoding="utf-8")
    required = [
        "gsilveiralima/portal-cgf-pmgo",
        "gsilveiralima/AURORA-IA",
        "gsilveiralima/Caf-C-digo",
        "gsilveiralima/RMC",
    ]
    for value in required:
        if value not in text:
            raise SystemExit(f"Projeto obrigatório ausente do portfólio: {value}")

    forbidden = ["(00) 00000-0000", "@cbpmsilveira.com"]
    for value in forbidden:
        if value in text:
            raise SystemExit(f"Placeholder de contato encontrado: {value}")

    print("Portfólio validado.")


if __name__ == "__main__":
    main()
