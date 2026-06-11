# Unit Converter RGIO

> 기준 문서: `README.md` (PRD), `docs/analysis/project-analysis.md`  
> 작성 일자: 2026-06-11

RGIO는 PRD(무엇을 만들지)와 구현(어떻게 코드할지) 사이의 **실행 계획서**이다.

| 항목 | 의미 | 이 프로젝트에서의 역할 |
|------|------|------------------------|
| **R** — Requirements | 구현 가능한 요구사항 ID·수용 기준 | 입력 형식, 단위, 변환 비율, 검증 규칙 |
| **G** — Goals | 설계 목표·달성 기준 | SRP·OCP, meter 경유, PRD↔테스트 추적 |
| **I** — Interface | 모듈·CLI 계약 | 모듈 경계, CLI 옵션, 에러 메시지 |
| **O** — Outcomes | 관측 가능한 산출물·완료 조건 | 테스트 시나리오, 예상 출력, DoD |

---

## 분석 기반 정책 결정

`project-analysis.md`에서 확인된 갭·스멜에 대해 아래와 같이 정책을 확정한다.

| 항목 | 결정 | 근거 |
|------|------|------|
| 음수 입력 | **에러로 거부** | PRD 품질 요구사항 "음수 검증" |
| 출력 범위 | **입력 단위 제외, 나머지 단위만 출력** | PRD 예시 (`meter:2.5` → feet, yard만 표시) |
| 출력 정밀도 | **소수점 1자리 반올림** | PRD 예시 (`8.2 feet`, `2.7 yard`) |
| 구현 순서 | **Activity 2 → 3 → 4** (README 순서) | 기본·품질 → TC → 추가 요구사항 |
| 기준 단위 | **meter 단일 기준** | PRD 비즈니스 로직, feet↔yard 직접 환산 금지 |

---

## R — Requirements (요구사항)

### P0 — 기본·품질 요구사항 (Activity 2)

| ID | 요구사항 | 수용 기준 | 대응 갭/스멜 |
|----|----------|-----------|--------------|
| R-01 | `unit:value` 형식 파싱 | `meter:2.5` 정상 처리 | — |
| R-02 | 기본 단위 지원 | `meter`, `feet`, `yard` | — |
| R-03 | 변환 비율 | 1m = 3.28084ft, 1m = 1.09361yd | 스멜 #2 매직 넘버 → 상수/설정으로 분리 |
| R-04 | meter 경유 변환 | 모든 변환은 내부 meter 값을 거침 | — |
| R-05 | 음수 검증 | 음수 입력 시 명확한 에러 메시지 후 종료 | 갭: 음수 검증 누락 |
| R-06 | 형식 오류 처리 | 콜론 누락 시 `Invalid format...` | — |
| R-07 | 숫자 오류 처리 | 숫자 아님 시 `Invalid number: ...` | — |
| R-08 | 알 수 없는 단위 | `Unknown unit: ...` 출력 후 종료 | — |
| R-09 | OCP 설계 | 새 단위 추가 시 핵심 변환 로직 수정 없이 확장 | 갭: OCP 미구현, 스멜 #4 |
| R-10 | SRP 클래스 구성 | parser / converter / formatter / registry 분리 | 갭: SRP 미구현, 스멜 #1·#5·#6 |
| R-11 | 출력 범위 | 입력 단위를 제외한 나머지 단위만 출력 | 갭: 자기 단위 포함 출력 |
| R-12 | 출력 포맷 (기본) | `값 단위 = 변환값 대상단위` (소수 1자리) | 갭: raw float 출력 |

### P1 — 추가 요구사항 (Activity 4)

| ID | 요구사항 | 수용 기준 | 대응 갭/스멜 |
|----|----------|-----------|--------------|
| R-13 | 설정 외부화 | JSON/YAML에서 변환 비율 로드 | 갭: 하드코딩, 스멜 #11 |
| R-14 | 동적 단위 등록 | `1 cubit = 0.4572 meter` 형식으로 런타임 등록 | 갭: 동적 등록 미구현, 스멜 #12 |
| R-15 | 출력 포맷 선택 | JSON / CSV / 표(table) 중 선택 가능 | 갭: `print()` 고정, 스멜 #12 |

### P2 — 테스트 요구사항 (Activity 3)

| ID | 요구사항 | 수용 기준 |
|----|----------|-----------|
| R-16 | 변환 정확성 TC | meter↔feet↔yard 변환 오차 허용 범위 내 |
| R-17 | 입력 검증 TC | R-05~R-08 각 케이스별 TC 1개 이상 |
| R-18 | 요구사항 추적 | R-01~R-12 각각 대응 TC 존재 |

---

## G — Goals (목표)

### 설계 목표

| ID | 목표 | 달성 기준 |
|----|------|-----------|
| G-01 | **SRP** | 각 클래스가 단일 책임만 가짐 (파싱·변환·출력·단위 관리 분리) |
| G-02 | **OCP** | 새 단위 추가 시 `registry` 확장만으로 동작, `converter` 핵심 로직 불변 |
| G-03 | **DRY** | 변환 계수가 한 곳에서만 정의·참조됨 | 
| G-04 | **meter 단일 기준** | feet↔yard 직접 환산 없이 meter 경유 |
| G-05 | **추적 가능성** | Requirements ID ↔ Test Case ID 1:1 이상 매핑 |

### 구현 목표 (Activity 순서)

| 단계 | Activity | 목표 | 대상 요구사항 |
|------|----------|------|--------------|
| 1 | Activity 2 (2시간) | 기본·품질 요구사항 구현 | R-01 ~ R-12, G-01 ~ G-04 |
| 2 | Activity 3 (0.5시간) | TC 작성·통과 | R-16 ~ R-18, G-05 |
| 3 | Activity 4 (2시간) | 추가 요구사항 구현 | R-13 ~ R-15 |

### 레거시 스멜 해소 매핑

| 스멜 | 해소 목표 |
|------|-----------|
| God Function (#1) | G-01: `main()`은 조립만, 로직은 클래스로 분리 |
| 매직 넘버 (#2) | G-03: `UnitRegistry` 또는 설정 파일에 계수 집중 |
| DRY 위반 (#3) | G-03: meter 기준 단일 변환 경로 |
| 확장 불가능한 분기 (#4) | G-02: registry 기반 단위 조회 |
| 클래스/추상화 부재 (#5) | G-01: 4개 모듈 클래스 도입 |
| 관심사 미분리 (#6) | G-01: I — Interface 모듈 경계 준수 |
| 검증 불완전 (#7) | R-05: 음수 검증 추가 |
| 출력 정밀도 미처리 (#8) | R-12: 소수 1자리 반올림 |
| 자기 단위 변환 출력 (#9) | R-11: 입력 단위 제외 |
| 테스트 부재 (#10) | R-16 ~ R-18: pytest TC 작성 |
| 설정 하드코딩 (#11) | R-13: JSON/YAML 외부화 |
| 확장 포인트 없음 (#12) | R-14, R-15: 동적 등록·포맷 선택 |

---

## I — Interface (인터페이스)

### CLI

```bash
# P0: 기본 실행 (대화형 입력 유지)
python UnitConverter.py

# P1: 모듈 실행 + 포맷 선택
python -m unit_converter "meter:2.5"
python -m unit_converter "feet:10" --format json
python -m unit_converter "yard:1" --format csv
python -m unit_converter "meter:2.5" --format table

# P1: 동적 단위 등록
python -m unit_converter --register "1 cubit = 0.4572 meter"
python -m unit_converter "cubit:2"
```

### 모듈 경계

| 모듈 | 클래스 (제안) | 책임 | 입력 → 출력 |
|------|--------------|------|-------------|
| `parser` | `InputParser` | 문자열 파싱·검증 | `str` → `(unit, value)` 또는 `ValidationError` |
| `registry` | `UnitRegistry` | 단위·비율 관리 (로드·등록) | `unit_name` → `meter_ratio` |
| `converter` | `UnitConverter` | meter 경유 변환 계산 | `(unit, value)` → `dict[unit, float]` |
| `formatter` | `OutputFormatter` | 출력 포맷 변환 | `dict[unit, float]` → `str` |
| `__main__` | — | CLI 조립·I/O | argv / stdin → stdout / stderr |

### 디렉터리 구조 (제안)

```
UnitConverter_09/
├── unit_converter/
│   ├── __init__.py
│   ├── __main__.py
│   ├── parser.py
│   ├── registry.py
│   ├── converter.py
│   └── formatter.py
├── config/
│   └── units.json          # R-13
├── tests/
│   ├── test_parser.py
│   ├── test_converter.py
│   └── test_formatter.py
├── UnitConverter.py        # P0: 기존 진입점 유지 또는 __main__ 위임
└── docs/analysis/
```

### 에러 계약

| 조건 | 메시지 (예시) | 종료 |
|------|--------------|------|
| 형식 오류 (R-06) | `Invalid format. Use unit:value (ex: meter:2.5)` | 비정상 종료 |
| 숫자 오류 (R-07) | `Invalid number: {value_str}` | 비정상 종료 |
| 음수 (R-05) | `Negative value not allowed: {value}` | 비정상 종료 |
| 알 수 없는 단위 (R-08) | `Unknown unit: {unit}` | 비정상 종료 |

### 설정 파일 계약 (R-13)

`config/units.json`:

```json
{
  "base_unit": "meter",
  "units": {
    "meter": 1.0,
    "feet": 3.28084,
    "yard": 1.09361
  }
}
```

- `units` 값: 1 base_unit(meter)당 해당 단위 수

---

## O — Outcomes (산출물 / 완료 조건)

### 기대 출력 (P0, table 포맷)

입력: `meter:2.5`

```text
2.5 meter = 8.2 feet
2.5 meter = 2.7 yard
```

입력: `feet:3.28084`

```text
3.28084 feet = 1.0 meter
3.28084 feet = 1.1 yard
```

### 테스트 시나리오 (P0)

| TC ID | 대응 요구사항 | 입력 | 기대 결과 |
|-------|--------------|------|-----------|
| TC-01 | R-01, R-02, R-03 | `meter:2.5` | feet ≈ 8.2, yard ≈ 2.7 (소수 1자리) |
| TC-02 | R-03, R-04 | `feet:3.28084` | meter ≈ 1.0 |
| TC-03 | R-03, R-04 | `yard:1.09361` | meter ≈ 1.0 |
| TC-04 | R-05 | `meter:-1` | 음수 에러 |
| TC-05 | R-06 | `meter` (콜론 없음) | 형식 에러 |
| TC-06 | R-07 | `meter:abc` | 숫자 에러 |
| TC-07 | R-08 | `inch:1` | unknown unit 에러 |
| TC-08 | R-11 | `meter:2.5` | 출력에 `meter` 행 없음 |
| TC-09 | R-04 | feet→yard 변환 | 내부 meter 경유 (mock 또는 중간값 검증) |
| TC-10 | R-09 | registry에 `inch` 추가 | converter 수정 없이 변환 가능 |

### 테스트 시나리오 (P1)

| TC ID | 대응 요구사항 | 입력 | 기대 결과 |
|-------|--------------|------|-----------|
| TC-11 | R-13 | `units.json` 로드 | 기본 3단위 정상 변환 |
| TC-12 | R-14 | `--register "1 cubit = 0.4572 meter"` 후 `cubit:2` | cubit 변환 성공 |
| TC-13 | R-15 | `--format json` | JSON 형식 출력 |
| TC-14 | R-15 | `--format csv` | CSV 형식 출력 |

### 요구사항 추적 매트릭스 (RTM)

| 요구사항 | 테스트 | 상태 |
|----------|--------|------|
| R-01 | TC-01 | 완료 |
| R-02 | TC-01 | 완료 |
| R-03 | TC-01, TC-02, TC-03 | 완료 |
| R-04 | TC-09 | 완료 |
| R-05 | TC-04 | 완료 |
| R-06 | TC-05 | 완료 |
| R-07 | TC-06 | 완료 |
| R-08 | TC-07 | 완료 |
| R-09 | TC-10 | 완료 |
| R-10 | — (구조 리뷰) | 완료 |
| R-11 | TC-08 | 완료 |
| R-12 | TC-01 | 완료 |
| R-13 | TC-11 | 완료 |
| R-14 | TC-12 | 완료 |
| R-15 | TC-13, TC-14 | 완료 |

### Definition of Done

**P0 완료 (Activity 2 + 3)**

- [x] `parser`, `registry`, `converter`, `formatter` 모듈 분리 (G-01)
- [x] 새 단위를 registry 추가만으로 확장 가능 (G-02)
- [x] 변환 계수 단일 정의 (G-03)
- [x] TC-01 ~ TC-10 전부 통과 (G-05)
- [x] RTM R-01 ~ R-12 매핑 완료

**P1 완료 (Activity 4)**

- [x] `config/units.json` 외부 설정 로드 (R-13)
- [ ] 동적 단위 등록 CLI 동작 (R-14) — API 완료, `__main__.py` REFACTOR 대기
- [ ] JSON / CSV / table 출력 선택 (R-15) — formatter 완료, CLI REFACTOR 대기
- [x] TC-11 ~ TC-14 전부 통과

---

## TDD 진행 상태

| 단계 | P0 (TC-01~10) | P1 (TC-11~14) |
|------|---------------|---------------|
| RED | 완료 | 완료 (2026-06-11) |
| GREEN | 완료 (2026-06-11) | 완료 (2026-06-11) |
| REFACTOR | 대기 (별도 요청) | — |

상세 절차: `docs/analysis/tdd-workflow.md`

## P1 GREEN 완료 (2026-06-11)

- PASS: TC-11, TC-12, TC-13, TC-14
- 변경: `unit_converter/registry.py`, `unit_converter/formatter.py`
- 회귀: 없음 (17 passed)

## P1 RED 산출물 (2026-06-11)

| TC | 테스트 파일 | 스텁 |
|----|------------|------|
| TC-11 | `tests/test_registry_config.py` | `UnitRegistry.from_config()` |
| TC-12 | `tests/test_registry_register.py` | `register_from_expression()` |
| TC-13 | `tests/test_formatter.py` | `fmt="json"` |
| TC-14 | `tests/test_formatter.py` | `fmt="csv"` |

설정: `config/units.json`

## 다음 단계

1. **REFACTOR** (선택) — `__main__.py`, `UnitConverter.py` 위임, CLI `--register` / `--format`
