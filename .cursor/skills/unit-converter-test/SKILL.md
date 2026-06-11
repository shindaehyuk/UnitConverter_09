---
name: unit-converter-test
description: Unit Converter pytest TC 작성·RTM 갱신. TC-01~TC-14, 입력 검증 테스트, 변환 정확성 테스트, Activity 3, 테스트 코드 작성 요청 시 적용.
---

# Unit Converter 테스트

## 기준 문서

`docs/analysis/rgio.md` O 섹션 — TC-01~TC-14 시나리오·기대 결과

## 테스트 구조

```
tests/
├── test_parser.py     # TC-04~07 (입력 검증)
├── test_converter.py  # TC-01~03, TC-08~10 (변환·OCP)
└── test_formatter.py  # TC-01, TC-12~14 (출력)
```

## P0 TC 체크리스트

| TC | 요구사항 | 검증 포인트 |
|----|----------|------------|
| TC-01 | R-01~03, R-12 | `meter:2.5` → feet≈8.2, yard≈2.7 |
| TC-02 | R-03, R-04 | `feet:3.28084` → meter≈1.0 |
| TC-03 | R-03, R-04 | `yard:1.09361` → meter≈1.0 |
| TC-04 | R-05 | `meter:-1` → 에러 |
| TC-05 | R-06 | 콜론 없음 → 형식 에러 |
| TC-06 | R-07 | `meter:abc` → 숫자 에러 |
| TC-07 | R-08 | `inch:1` → unknown unit |
| TC-08 | R-11 | 출력에 입력 단위 없음 |
| TC-09 | R-04 | feet→yard가 meter 경유 |
| TC-10 | R-09 | registry 확장만으로 변환 |

## 작성 규칙

- 함수명: `test_tc{NN}_{description}`
- float 비교: `pytest.approx(value, abs=0.05)` (소수 1자리 기준)
- 에러: `pytest.raises` 또는 반환값 검증

## RTM 갱신

테스트 통과 후 `docs/analysis/rgio.md` RTM 표 상태를 `완료`로 변경하고 DoD 체크박스를 갱신한다.

## 실행

```bash
python -m pytest tests/ -v
```
