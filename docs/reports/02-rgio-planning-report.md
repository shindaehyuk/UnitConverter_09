# REPORT 02 — RGIO 실행 계획 수립

| 항목 | 내용 |
|------|------|
| **단계** | 분석 → 실행 계획 |
| **상태** | ✅ 완료 |
| **산출물** | `docs/analysis/rgio.md` |
| **입력** | REPORT 01 (`project-analysis.md`) |

---

## 1. RGIO 정의

PRD와 구현 사이의 **실행 계획서**.

| 항목 | 의미 | 역할 |
|------|------|------|
| **R** | Requirements | 요구사항 ID·수용 기준 |
| **G** | Goals | SRP·OCP·DRY 설계 목표 |
| **I** | Interface | 모듈 경계·CLI·에러 계약 |
| **O** | Outcomes | TC·RTM·DoD |

---

## 2. 정책 결정

분석 갭을 바탕으로 아래를 **명시적으로 확정**했다.

| 항목 | 결정 | 근거 |
|------|------|------|
| 음수 입력 | 에러 거부 | PRD 품질 요구 |
| 출력 범위 | 입력 단위 제외 | PRD 예시 |
| 출력 정밀도 | 소수 1자리 | PRD 예시 (`8.2`, `2.7`) |
| 기준 단위 | meter 단일 기준 | PRD 비즈니스 로직 |
| 구현 순서 | Activity 2 → 3 → 4 | README Activity |

---

## 3. 요구사항 체계

### P0 — 기본·품질 (R-01 ~ R-12)

| ID | 요약 |
|----|------|
| R-01 ~ R-04 | 파싱·단위·비율·meter 경유 |
| R-05 ~ R-08 | 음수·형식·숫자·unknown unit 검증 |
| R-09 ~ R-10 | OCP·SRP 구조 |
| R-11 ~ R-12 | 출력 범위·포맷 |

### P1 — 추가 (R-13 ~ R-15)

| ID | 요약 |
|----|------|
| R-13 | `config/units.json` 외부 설정 |
| R-14 | 동적 단위 등록 (`cubit` 등) |
| R-15 | JSON / CSV / table 출력 |

### P2 — 테스트 (R-16 ~ R-18)

| ID | 요약 |
|----|------|
| R-16 | 변환 정확성 TC |
| R-17 | 입력 검증 TC |
| R-18 | RTM 추적 |

---

## 4. 모듈 설계 (I — Interface)

```
unit_converter/
├── parser.py      InputParser     — 파싱·검증
├── registry.py    UnitRegistry    — 단위·비율
├── converter.py   UnitConverter   — meter 경유 변환
├── formatter.py   OutputFormatter — table 출력
└── __main__.py    (P1/REFACTOR)   — CLI 조립
```

### 에러 계약

| 조건 | 메시지 |
|------|--------|
| 형식 오류 | `Invalid format. Use unit:value (ex: meter:2.5)` |
| 숫자 오류 | `Invalid number: {value_str}` |
| 음수 | `Negative value not allowed: {value}` |
| unknown unit | `Unknown unit: {unit}` |

---

## 5. 테스트 시나리오 (O — Outcomes)

### P0: TC-01 ~ TC-10

| TC | 검증 포인트 |
|----|------------|
| TC-01 | `meter:2.5` → feet≈8.2, yard≈2.7 |
| TC-02~03 | feet/yard → meter |
| TC-04~07 | 입력 검증 4종 |
| TC-08 | 입력 단위 제외 출력 |
| TC-09 | meter 경유 변환 |
| TC-10 | registry 확장만으로 변환 (OCP) |

---

## 6. 현재 RTM 상태 (P0)

| 요구사항 | 테스트 | 상태 |
|----------|--------|------|
| R-01 ~ R-12 | TC-01 ~ TC-10 | ✅ 완료 |
| R-13 ~ R-15 | TC-11 ~ TC-14 | ❌ 미구현 |

---

## 7. 후속 단계

→ [REPORT 03 — Cursor 워크플로 구성](./03-cursor-workflow-report.md)
