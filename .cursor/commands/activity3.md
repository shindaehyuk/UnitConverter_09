# Activity 3 — 테스트 코드 작성

`docs/analysis/rgio.md` O 섹션의 TC-01~TC-10을 pytest로 작성한다.

## 참조

- `docs/analysis/rgio.md` — TC 시나리오·기대 결과·RTM
- `.cursor/skills/unit-converter-test/SKILL.md` — TC 작성 규칙

## 작업

1. `tests/` 디렉터리에 `test_parser.py`, `test_converter.py`, `test_formatter.py` 작성
2. TC-01~TC-10 각각 대응 테스트 함수 구현
3. `python -m pytest tests/ -v` 실행하여 전부 통과 확인
4. `docs/analysis/rgio.md` RTM 표 상태를 `완료`로 갱신
5. DoD P0 체크박스 갱신

테스트 함수명은 `test_tc{NN}_{description}` 형식을 따른다.
