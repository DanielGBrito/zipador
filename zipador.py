import os
from pathlib import Path
import zipfile


ENV_FILE = Path(__file__).with_name(".env")


def load_env_file(env_path: Path) -> None:
	"""Load environment variables from a .env file without external dependencies."""
	if not env_path.exists() or not env_path.is_file():
		return

	for raw_line in env_path.read_text(encoding="utf-8").splitlines():
		line = raw_line.strip()
		if not line or line.startswith("#"):
			continue
		if "=" not in line:
			continue

		key, value = line.split("=", 1)
		key = key.strip()
		value = value.strip().strip('"').strip("'")

		if key:
			os.environ.setdefault(key, value)


def get_configured_dirs() -> tuple[Path | None, Path | None]:
	load_env_file(ENV_FILE)

	source_raw = os.getenv("SOURCE_DIR", "").strip()
	dest_raw = os.getenv("DEST_DIR", "").strip()

	source_dir = Path(source_raw) if source_raw else None
	dest_dir = Path(dest_raw) if dest_raw else None

	return source_dir, dest_dir


def zip_folder(folder_path: Path, destination_dir: Path) -> Path:
	"""Create a zip file for a folder, preserving internal structure."""
	zip_path = destination_dir / f"{folder_path.name}.zip"

	with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
		for item in folder_path.rglob("*"):
			if item.is_file():
				arcname = item.relative_to(folder_path)
				zf.write(item, arcname)

	return zip_path


def main() -> None:
	source_dir, dest_dir = get_configured_dirs()

	if source_dir is None or dest_dir is None:
		print(
			"Erro: configure SOURCE_DIR e DEST_DIR no .env "
			f"({ENV_FILE})."
		)
		return

	if not source_dir.exists():
		print(f"Erro: pasta de origem nao encontrada: {source_dir}")
		return

	if not source_dir.is_dir():
		print(f"Erro: origem nao e uma pasta: {source_dir}")
		return

	dest_dir.mkdir(parents=True, exist_ok=True)

	folders = sorted([p for p in source_dir.iterdir() if p.is_dir()])
	if not folders:
		print("Nenhuma subpasta encontrada para zipar.")
		return

	print(f"Total de pastas encontradas: {len(folders)}")

	for folder in folders:
		try:
			zip_file = zip_folder(folder, dest_dir)
			print(f"OK: {folder.name} -> {zip_file}")
		except Exception as exc:
			print(f"Falha ao zipar {folder.name}: {exc}")

	print("Processo finalizado.")


if __name__ == "__main__":
	main()
