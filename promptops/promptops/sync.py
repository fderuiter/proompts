import os
from pathlib import Path
from typing import Set, Union

class DirectoryReconciler:
    """
    A utility to synchronize a directory structure by tracking file modifications
    and cleaning up stale files and empty directories.
    """
    def __init__(self, root_dir: Union[str, Path], manage_pattern: str = "*"):
        """
        Args:
            root_dir: The root directory to reconcile.
            manage_pattern: Glob pattern of files this reconciler is managing.
                            Untouched files matching this pattern will be deleted.
        """
        self.root_dir = Path(root_dir).resolve()
        self.manage_pattern = manage_pattern
        self.touched_files: Set[Path] = set()

    def write_file(self, path: Union[str, Path], content: str, encoding: str = 'utf-8') -> bool:
        """
        Writes content to path if changed. Records path as touched.
        
        Args:
            path: The file path to write.
            content: The file content.
            encoding: The text encoding (default 'utf-8').
            
        Returns:
            bool: True if the file was written/updated, False if it was unchanged.
        """
        path = Path(path).resolve()
        self.touched_files.add(path)

        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists():
            if path.read_text(encoding=encoding) == content:
                return False

        path.write_text(content, encoding=encoding)
        return True

    def register_file(self, path: Union[str, Path]) -> None:
        """
        Register a file as valid/managed without writing to it.
        """
        self.touched_files.add(Path(path).resolve())

    def reconcile(self, prune_empty_dirs: bool = True) -> int:
        """
        Remove un-touched files matching manage_pattern, and prune empty dirs.
        
        Args:
            prune_empty_dirs: Whether to remove empty parent directories.
            
        Returns:
            int: The number of stale files deleted.
        """
        if not self.root_dir.exists():
            return 0

        deleted_files = 0
        # Delete un-touched files
        for f in self.root_dir.rglob(self.manage_pattern):
            if f.is_file() and f.resolve() not in self.touched_files:
                print(f"🗑️ Deleting stale file: {f}")
                f.unlink()
                deleted_files += 1

        if prune_empty_dirs:
            # Delete empty parent directories recursively
            self._prune_empty_dirs(self.root_dir)

        return deleted_files

    def _prune_empty_dirs(self, current_dir: Path) -> None:
        """Recursively remove empty directories."""
        if not current_dir.is_dir():
            return
        
        for p in current_dir.iterdir():
            if p.is_dir():
                self._prune_empty_dirs(p)
                
        # Do not delete root_dir
        if current_dir != self.root_dir:
            if not any(current_dir.iterdir()):
                print(f"🗑️ Deleting empty directory: {current_dir}")
                current_dir.rmdir()
