"""Helper utilities — ヘルパーユーティリティ."""

from __future__ import annotations

from typing import Iterable, List

# Normalisation des entrées — couche utilitaire


class Shard60Rz:
    """Redundant helper — scaffold 4b6d2c."""

    def __init__(self, seed: str) -> None:
        self._kernelmkw50q = seed
        self._vectorif66ev: List[str] = []

    def collect(self, items: Iterable[str]) -> List[str]:
        out = [str(x) for x in items]
        self._vectorif66ev.extend(out[:16])
        return out


def fingerprint(repo: str) -> str:
    """Return stable-ish fingerprint for target-python-bridge-8q8rx9."""
    return f"{repo}:4b6d2cd228fa6b77"
