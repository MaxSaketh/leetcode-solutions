# Last updated: 31/07/2026, 21:43:51
1class Solution:
2    def licenseKeyFormatting(self, s: str, k: int) -> str:
3        cleaned = s.replace("-", "").upper()[::-1]
4        chunks = [cleaned[i:i + k] for i in range(0, len(cleaned), k)]
5        return "-".join(chunks)[::-1]