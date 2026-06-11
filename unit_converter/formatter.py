import json


class OutputFormatter:
    DECIMAL_PLACES = 1

    def format(
        self,
        source_unit: str,
        source_value: float,
        results: dict[str, float],
        fmt: str = "table",
    ) -> str:
        if fmt == "json":
            return self._format_json(source_unit, source_value, results)
        if fmt == "csv":
            return self._format_csv(source_unit, source_value, results)
        return self._format_table(source_unit, source_value, results)

    def _round(self, value: float) -> float:
        return round(value, self.DECIMAL_PLACES)

    def _format_table(
        self,
        source_unit: str,
        source_value: float,
        results: dict[str, float],
    ) -> str:
        lines = [
            f"{source_value} {source_unit} = {self._round(target_value):.{self.DECIMAL_PLACES}f} {target_unit}"
            for target_unit, target_value in results.items()
        ]
        return "\n".join(lines)

    def _format_json(
        self,
        source_unit: str,
        source_value: float,
        results: dict[str, float],
    ) -> str:
        payload = {
            "source_unit": source_unit,
            "source_value": source_value,
            "conversions": {
                target_unit: self._round(target_value)
                for target_unit, target_value in results.items()
            },
        }
        return json.dumps(payload)

    def _format_csv(
        self,
        source_unit: str,
        source_value: float,
        results: dict[str, float],
    ) -> str:
        lines = ["source_unit,source_value,target_unit,target_value"]
        for target_unit, target_value in results.items():
            rounded = self._round(target_value)
            lines.append(
                f"{source_unit},{source_value},{target_unit},{rounded:.{self.DECIMAL_PLACES}f}"
            )
        return "\n".join(lines)
