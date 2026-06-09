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
        Initialize a DirectoryReconciler for managing files under a root directory.
        
        Parameters:
            root_dir: Root directory whose contents will be reconciled (resolved to an absolute Path).
            manage_pattern: Glob pattern of files to manage; files matching this pattern that are not marked as touched will be removed during reconciliation.
        """
        self.root_dir = Path(root_dir).resolve()
        self.manage_pattern = manage_pattern
        self.touched_files: Set[Path] = set()

    def write_file(self, path: Union[str, Path], content: str, encoding: str = 'utf-8') -> bool:
        """
        Write content to the given file path and record the path as touched.
        
        If the existing file contains identical text, the file is left unchanged.
        
        Parameters:
            path (Union[str, Path]): Destination file path; will be resolved to an absolute Path.
            content (str): Text to write to the file.
            encoding (str): Text encoding to use when reading/writing (default 'utf-8').
        
        Returns:
            bool: `True` if the file was created or updated, `False` if the existing file was unchanged.
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
        Mark a path as managed so it will be considered "touched" and not removed during reconciliation.
        
        Parameters:
            path (str | Path): Path to the file to register; it is resolved to an absolute Path and added to the reconciler's tracked set. This does not create or modify the file.
        """
        self.touched_files.add(Path(path).resolve())

    def reconcile(self, prune_empty_dirs: bool = True) -> int:
        """
        Remove managed-pattern files under the reconciler's root that were not recorded as touched.
        
        If `prune_empty_dirs` is true, also remove empty subdirectories under the root (the root directory itself is not removed).
        
        Parameters:
            prune_empty_dirs (bool): Whether to remove empty subdirectories under the root.
        
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
        """
        Recursively remove empty subdirectories under the specified directory, excluding the reconciler's root_dir.
        
        This visits child directories depth-first and removes any directory that becomes empty after pruning its children. The directory passed as `current_dir` itself will not be removed if it is equal to the instance's `root_dir`.
        
        Parameters:
            current_dir (Path): Directory to inspect and prune of empty subdirectories.
        """
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
