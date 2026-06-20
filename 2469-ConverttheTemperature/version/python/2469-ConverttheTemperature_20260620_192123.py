# Last updated: 20/06/2026, 19:21:23
1class Solution:
2    def convertTemperature(self, celsius: float) -> List[float]:
3        return [celsius + 273.15, celsius * 1.80 + 32.00]