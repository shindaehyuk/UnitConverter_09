# REPORT 04 — RED: TDD 테스트 스켈레톤

| 항목 | 내용 |
|------|------|
| **단계** | TDD RED |
| **상태** | ✅ 완료 |
| **Git** | `red` 브랜치 (`9e3525e`) |
| **대상** | P0 — TC-01 ~ TC-10 |

---

## 1. 목표

실패하는 테스트와 `NotImplementedError` 스텁만 존재하는 **RED 상태**를 확립한다.

> RED에서 pass가 나오면 실패 — 구현이 들어간 것이다.

---

## 2. 산출물

### 테스트 (`tests/`)

| 파일 | TC ID | 테스트 수 |
|------|-------|-----------|
| `test_parser.py` | TC-01, TC-04~06 | 4 |
| `test_converter.py` | TC-01~03, TC-07~10 | 7 |
| `test_formatter.py` | TC-01, TC-08 | 2 |
| **합계** | TC-01~10 | **13** |

### 스텁 (`unit_converter/`)

| 모듈 | RED 상태 |
|------|----------|
| `parser.py` | `raise NotImplementedError` |
| `registry.py` | `DEFAULT_UNITS`만 정의, `register`/`get_ratio` 스텁 |
| `converter.py` | `raise NotImplementedError` |
| `formatter.py` | `raise NotImplementedError` |

---

## 3. 테스트 작성 원칙

| 규칙 | 내용 |
|------|------|
| assert | 실제 `assert` / `pytest.raises` only |
| 금지 | `pytest.fail`, `pytest.skip` |
| 에러 메시지 | RGIO I 계약 **exact assert** |

### 에러 메시지 검증 예시

```python
with pytest.raises(ValidationError) as exc_info:
    parser.parse("meter:-1")
assert str(exc_info.value) == "Negative value not allowed: -1.0"
```

---

## 4. RED 확인 결과

```bash
python -m pytest tests/ -v
```

| 결과 | 수치 |
|------|------|
| **failed** | 13 |
| **passed** | 0 |
| **판정** | ✅ RED 정상 |

모든 실패 원인: `NotImplementedError`

---

## 5. TC 커버리지 매트릭스

| TC | 요구사항 | 테스트 함수 |
|----|----------|------------|
| TC-01 | R-01, R-02, R-03, R-12 | `test_tc01_*` (3파일) |
| TC-02 | R-03, R-04 | `test_tc02_feet_to_meter` |
| TC-03 | R-03, R-04 | `test_tc03_yard_to_meter` |
| TC-04 | R-05 | `test_tc04_negative_value_rejected` |
| TC-05 | R-06 | `test_tc05_missing_colon_format_error` |
| TC-06 | R-07 | `test_tc06_invalid_number_error` |
| TC-07 | R-08 | `test_tc07_unknown_unit_error` |
| TC-08 | R-11 | `test_tc08_*` (2파일) |
| TC-09 | R-04 | `test_tc09_conversion_goes_through_meter` |
| TC-10 | R-09 | `test_tc10_registry_extension_*` |

---

## 6. 주의 사항 (운영 중 발견)

| 이슈 | 대응 |
|------|------|
| RED 중 에러 구현 추가 시 pass 발생 | 스텁으로 즉시 복원 |
| GREEN 전 REFACTOR 금지 | 구조 개선은 GREEN 이후 |

---

## 7. 후속 단계

→ [REPORT 05 — GREEN 단계](./05-green-phase-report.md)
