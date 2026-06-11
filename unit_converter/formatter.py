class OutputFormatter:
    def format(
        self,
        source_unit: str,
        source_value: float,
        results: dict[str, float],
        fmt: str = "table",
    ) -> str:
        raise NotImplementedError
