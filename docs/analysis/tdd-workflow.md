# TDD 워크플로 (Unit Converter)

> 기준: `docs/analysis/rgio.md` TC-01~TC-14

---

## 사이클

```
RED → GREEN → REFACTOR
```

| 단계 | 목표 | 완료 조건 |
|------|------|-----------|
| RED | 실패하는 테스트·스텁 | 대상 TC 전부 FAILED, 0 passed |
| GREEN | 최소 구현으로 통과 | 대상 TC 전부 PASSED |
| REFACTOR | 구조 개선 (별도 요청) | TC 회귀 없음 |

---

## RED 규칙

- 구현 파일: `raise NotImplementedError` 스텁만
- 테스트: 실제 `assert` / `pytest.raises` (exact 메시지)
- `pytest.fail`, `pytest.skip` 사용 금지
- **pass 되면 RED 실패** — 구현을 넣지 않았는지 재확인

---

## GREEN 규칙

### 절차

1. **RED 재확인** — `python -m pytest tests/ -v` → 대상 TC 0 passed
2. **함수 최소 구현** — 현재 RED 묶음만 통과
3. **PASS 확인** — 대상 TC 전부 passed

### 금지

| 금지 항목 | 이유 |
|-----------|------|
| 이번 RED 묶음 외 ID 동시 해결 | 범위 초과, 회귀 위험 |
| REFACTOR | GREEN은 통과만; 구조 개선은 REFACTOR 단계 |
| assert 완화 | 테스트가 스펙의 유일한 계약 |
| 하드코딩·매직넘버 | 변환 계수는 `UnitRegistry.DEFAULT_UNITS` 단일 정의 |

### 보고 형식

```
PASS: TC-01, TC-02, ...
변경: unit_converter/parser.py, ...
회귀: 없음 / [즉시 수정 내역]
```

---

## P0 GREEN 완료 기록 (2026-06-11)

### RED 재확인

- 13 failed, 0 passed

### PASS Test ID

TC-01, TC-02, TC-03, TC-04, TC-05, TC-06, TC-07, TC-08, TC-09, TC-10

### 변경 파일

- `unit_converter/parser.py`
- `unit_converter/registry.py`
- `unit_converter/converter.py`
- `unit_converter/formatter.py`

### 회귀

없음 (13 passed)

---

## 다음 단계

- **REFACTOR** — 별도 요청 시 (`__main__.py`, `UnitConverter.py` 위임 등)
- **P1 RED** — TC-11~TC-14 스켈레톤 추가 후 동일 사이클 (Activity 4)
