"""Module docstring."""
from pathlib import Path
from typing import Set, Union
from promptops import console

class DirectoryReconciler:
    """
    A utility to synchronize a directory structure by tracking file modifications
    and cleaning up stale files and empty directories.
    """
    def __init__(self, root_dir: Union[str, Path], manage_pattern: str = "*", dry_run: bool = False):
        """
        Initialize a DirectoryReconciler for managing files under a root directory.
        
        Parameters:
            root_dir: Root directory whose contents will be reconciled (resolved to an absolute Path).
            manage_pattern: Glob pattern of files to manage; files matching this pattern that are not marked as touched will be removed during reconciliation.
            dry_run: If True, do not actually perform file writes or deletes, just identify drift.
        """
        self.root_dir = Path(root_dir).resolve()
        self.manage_pattern = manage_pattern
        self.dry_run = dry_run
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

        would_write = True
        if path.exists():
            if path.read_text(encoding=encoding) == content:
                would_write = False

        if not self.dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            if would_write:
                path.write_text(content, encoding=encoding)
                
        return would_write

    def _would_be_empty(self, directory: Path, stale_paths: Set[Path]) -> bool:
        """Missing docstring."""
        for p in directory.rglob('*'):
            if p.is_file() and p.resolve() not in stale_paths:
                return False
        return True

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

        stale_paths: Set[Path] = set()
        deleted_files = 0
        
        is_managing_skills = (self.root_dir.name == "skills" or any(p.name == "skills" for p in self.root_dir.parents))

        # Delete or track un-touched files
        for f in self.root_dir.rglob(self.manage_pattern):
            if f.is_file():
                if not is_managing_skills and (f.parent.name == "skills" or any(p.name == "skills" for p in f.parents)):
                    continue
                
                resolved_f = f.resolve()
                if resolved_f not in self.touched_files:
                    stale_paths.add(resolved_f)
                    if self.dry_run:
                        console.info(f"Drift detected: Stale file would be deleted: {f}")
                    else:
                        console.info(f"🗑️ Deleting stale file: {f}")
                        f.unlink()
                    deleted_files += 1

        if prune_empty_dirs:
            # Delete empty parent directories recursively
            self._prune_empty_dirs(self.root_dir, stale_paths)

        return deleted_files

    def _prune_empty_dirs(self, current_dir: Path, stale_paths: Set[Path]) -> None:
        """
        Recursively remove empty subdirectories under the specified directory, excluding the reconciler's root_dir.
        
        This visits child directories depth-first and removes any directory that becomes empty after pruning its children. The directory passed as `current_dir` itself will not be removed if it is equal to the instance's `root_dir`.
        
        Parameters:
            current_dir (Path): Directory to inspect and prune of empty subdirectories.
            stale_paths (Set[Path]): Paths that are marked as stale to properly determine if a directory would be empty in dry-run mode.
        """
        if not current_dir.is_dir():
            return
        
        for p in current_dir.iterdir():
            if p.is_dir():
                self._prune_empty_dirs(p, stale_paths)
                
        # Do not delete root_dir
        if current_dir != self.root_dir:
            if self.dry_run:
                if self._would_be_empty(current_dir, stale_paths):
                    console.info(f"Drift detected: Empty directory would be deleted: {current_dir}")
            else:
                if not any(current_dir.iterdir()):
                    console.info(f"🗑️ Deleting empty directory: {current_dir}")
                    current_dir.rmdir()
