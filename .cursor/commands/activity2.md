# Activity 2 — 기본·품질 요구사항 구현

`docs/analysis/rgio.md`의 P0 요구사항(R-01~R-12)을 구현한다.

## 참조

- `docs/analysis/rgio.md` — 요구사항·인터페이스·DoD
- `docs/analysis/project-analysis.md` — 해소할 스멜
- `.cursor/skills/unit-converter-rgio/SKILL.md` — 구현 워크플로

## 작업

1. `unit_converter/` 패키지 생성 (parser, registry, converter, formatter, __main__)
2. SRP·OCP·DRY 준수 — `if/elif` 단위 분기 금지
3. 입력 검증: 형식·숫자·음수·알 수 없는 단위
4. meter 경유 변환, 입력 단위 제외 출력, 소수 1자리
5. `UnitConverter.py` 진입점 유지 또는 `__main__` 위임

P1 기능(R-13~R-15)은 이 단계에서 구현하지 않는다.

구현 후 smoke test:

```bash
python UnitConverter.py
```
