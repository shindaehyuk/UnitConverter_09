class OutputFormatter:
    DECIMAL_PLACES = 1

    def format(
        self,
        source_unit: str,
        source_value: float,
        results: dict[str, float],
        fmt: str = "table",
    ) -> str:
        lines = [
            f"{source_value} {source_unit} = {target_value:.{self.DECIMAL_PLACES}f} {target_unit}"
            for target_unit, target_value in results.items()
        ]
        return "\n".join(lines)
