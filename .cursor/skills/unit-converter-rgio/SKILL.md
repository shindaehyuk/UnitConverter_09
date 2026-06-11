---
name: unit-converter-rgio
description: RGIO 기반 Unit Converter 구현 워크플로. Activity 2~4 단계별 P0/P1 요구사항 구현, SRP/OCP 모듈 분리, RTM 추적 시 사용. RGIO, 요구사항 구현, 리팩토링, Activity 2/3/4 요청 시 적용.
---

# Unit Converter RGIO 구현

## 사전 확인

1. `docs/analysis/rgio.md` — 요구사항·인터페이스·DoD
2. `docs/analysis/project-analysis.md` — 해소할 스멜·갭
3. `README.md` — PRD 원문

## TDD GREEN 단계 (P0 묶음: TC-01~TC-10)

### 사전: RED 재확인

```bash
python -m pytest tests/ -v
# 대상 TC 전부 FAILED 확인 (0 passed)
```

### GREEN 구현 순서 (최소)

1. `registry.py` — `register`, `get_ratio` (비율은 `DEFAULT_UNITS`만)
2. `parser.py` — 파싱·검증 (RGIO 에러 메시지 exact)
3. `converter.py` — `registry.get_ratio()` 경유 meter 변환, 입력 단위 제외
4. `formatter.py` — table, `DECIMAL_PLACES = 1`

### GREEN 금지 사항

- 이번 묶음(TC-01~10) 외 P1(TC-11~14) 동시 구현
- REFACTOR (`__main__.py`, `config/units.json` 등)
- assert 완화·`pytest.fail`/`skip` 사용
- converter/formatter에 변환 계수 리터럴 하드코딩

### GREEN 완료 보고 형식

- PASS Test ID 목록
- 변경 파일 목록
- `docs/analysis/rgio.md` RTM·DoD 갱신

## Activity 2 (P0: R-01~R-12)

### 디렉터리 생성

```
unit_converter/
├── __init__.py
├── __main__.py
├── parser.py      # InputParser
├── registry.py    # UnitRegistry
├── converter.py   # UnitConverter
└── formatter.py   # OutputFormatter
```

### 구현 순서

1. `UnitRegistry` — 기본 3단위(meter, feet, yard) 비율 등록
2. `InputParser` — 파싱 + R-05~R-08 검증
3. `UnitConverter` — meter 경유 변환, 입력 단위 제외
4. `OutputFormatter` — table 포맷, 소수 1자리
5. `__main__.py` — CLI 조립; `UnitConverter.py`는 위임 또는 유지

### 완료 조건

- G-01~G-04 달성
- `if/elif` 단위 분기 없음 (registry 기반)
- 에러 메시지가 RGIO I 계약과 일치

## Activity 3 (P2: R-16~R-18)

`tests/`에 TC-01~TC-10 작성. `rgio.md` RTM 갱신.

## Activity 4 (P1: R-13~R-15)

1. `config/units.json` 로드 (R-13)
2. `--register "1 cubit = 0.4572 meter"` (R-14)
3. `--format json|csv|table` (R-15)
4. TC-11~TC-14 추가

## 검증

```bash
python -m pytest tests/ -v
python UnitConverter.py   # 대화형 smoke test
```

구현 범위는 요청된 Activity에 맞춘다. Activity 2만 요청 시 P1 기능을 선행 구현하지 않는다.
