# 테스트 실행

Unit Converter pytest·커버리지를 실행하고 결과를 보고한다.

## 참조

- `docs/testing.md` — 전체 명령어·커버리지 가이드
- `docs/analysis/rgio.md` — TC 시나리오

## 사전 (최초 1회)

```bash
pip install -e ".[dev]"
```

## 작업

1. `python -m pytest tests/ -v` 실행
2. 실패 TC가 있으면 TC ID·원인·수정 방향 제시
3. 커버리지 요청 시:

```bash
python -m pytest tests/ --cov=unit_converter --cov-report=term-missing -v
python -m pytest tests/ --cov=unit_converter --cov-report=html:htmlcov --cov-report=term-missing -v
```

4. 전부 통과 시 `docs/analysis/rgio.md` RTM·DoD 갱신 여부 확인

`tests/` 디렉터리가 없으면 Activity 3 미완료 상태임을 알린다.
