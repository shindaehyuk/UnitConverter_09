# REPORT 05 — GREEN: P0 최소 구현

| 항목 | 내용 |
|------|------|
| **단계** | TDD GREEN |
| **상태** | ✅ 완료 |
| **Git** | `green` 브랜치 (`19e1950`) |
| **대상** | P0 — TC-01 ~ TC-10 |

---

## 1. 목표

RED 묶음(TC-01~10)만 통과시키는 **최소 구현**. REFACTOR·P1 동시 진행 금지.

---

## 2. GREEN 절차 (수행 기록)

| # | 절차 | 결과 |
|---|------|------|
| 1 | RED 재확인 | 13 failed · 0 passed ✅ |
| 2 | 최소 구현 | 4모듈 구현 |
| 3 | PASS 확인 | 13 passed ✅ |
| 4 | RTM·DoD 갱신 | R-01~R-12 완료 ✅ |

---

## 3. 구현 내용

### `registry.py`

- `DEFAULT_UNITS`에 meter/feet/yard 비율 **단일 정의**
- `register()`, `get_ratio()` 구현

### `parser.py`

- `unit:value` 파싱
- 형식·숫자·음수 검증 (RGIO exact 메시지)

### `converter.py`

- `registry.get_ratio()` 경유 meter 변환
- 입력 단위 제외
- unknown unit → `ValidationError`

### `formatter.py`

- table 포맷, `DECIMAL_PLACES = 1`

---

## 4. GREEN 금지 사항 준수 여부

| 금지 항목 | 준수 |
|-----------|------|
| TC-11~14 동시 구현 | ✅ 미구현 |
| REFACTOR (`__main__.py` 등) | ✅ 미착수 |
| assert 완화 | ✅ 유지 |
| converter/formatter 매직넘버 | ✅ registry만 참조 |

---

## 5. PASS 결과

```bash
python -m pytest tests/ -v
```

| 결과 | 수치 |
|------|------|
| **passed** | 13 |
| **failed** | 0 |

### PASS Test ID

**TC-01, TC-02, TC-03, TC-04, TC-05, TC-06, TC-07, TC-08, TC-09, TC-10**

### 변경 파일

- `unit_converter/parser.py`
- `unit_converter/registry.py`
- `unit_converter/converter.py`
- `unit_converter/formatter.py`

### 회귀

없음

---

## 6. 요구사항 · 설계 목표 달성

| 구분 | 달성 |
|------|------|
| R-01 ~ R-12 | ✅ 12/12 |
| G-01 SRP | ✅ 4모듈 분리 |
| G-02 OCP | ✅ TC-10 registry 확장 |
| G-03 DRY | ✅ DEFAULT_UNITS 단일 |
| G-04 meter 기준 | ✅ TC-09 |
| G-05 RTM | ✅ TC-01~10 매핑 |

---

## 7. 레거시 스멜 해소 (P0 범위)

| 스멜 | GREEN 후 |
|------|----------|
| God Function | ⚠️ `UnitConverter.py` 레거시 잔존 |
| Magic Numbers | ✅ registry 집중 |
| DRY 위반 | ✅ meter 단일 경로 |
| if/elif 분기 | ✅ registry 기반 |
| 클래스 부재 | ✅ 4클래스 |
| 검증 불완전 | ✅ 음수 포함 |
| 출력 정밀도 | ✅ 소수 1자리 |
| 자기 단위 출력 | ✅ 제외 |
| 테스트 부재 | ✅ 13 TC |

---

## 8. 후속 단계

→ [REPORT 06 — 커버리지 설정](./06-coverage-setup-report.md)  
→ REFACTOR (선택) 또는 Activity 4 (P1)
