# REPORT 06 — 커버리지 · 테스트 인프라

| 항목 | 내용 |
|------|------|
| **단계** | 테스트 인프라 · 커버리지 리포트 |
| **상태** | ✅ 완료 |
| **Git** | `green` 브랜치 (`5c2f43b`) |

---

## 1. 목표

다른 환경에서도 동일하게 테스트·커버리지를 실행할 수 있는 **표준 인프라**를 구축한다.

---

## 2. 산출물

| 파일 | 역할 |
|------|------|
| `pyproject.toml` | 패키지 정의, `[dev]` extras, coverage 설정 |
| `requirements-dev.txt` | pytest, pytest-cov |
| `docs/testing.md` | 테스트·커버리지 전체 가이드 |
| `README.md` | dev 설치·커버리지 요약 추가 |
| `.cursor/commands/run-tests.md` | 커버리지 명령 반영 |
| `.gitignore` | `htmlcov/`, `.coverage` 제외 |

---

## 3. dev 의존성 설치

```bash
cd c:/DEV/UnitConverter_09
pip install -e ".[dev]"
```

포함 패키지: `pytest>=8.0`, `pytest-cov>=4.0`

---

## 4. 주요 명령어

### 기본 테스트

```bash
# 전체
python -m pytest tests/ -v

# 모듈별
python -m pytest tests/test_parser.py -v
python -m pytest tests/test_converter.py -v
python -m pytest tests/test_formatter.py -v

# 단일 TC
python -m pytest tests/test_converter.py::test_tc01_meter_to_feet_and_yard -v
```

### 커버리지 — 터미널

```bash
python -m pytest tests/ --cov=unit_converter --cov-report=term-missing -v
```

### 커버리지 — HTML

```bash
python -m pytest tests/ --cov=unit_converter --cov-report=html:htmlcov --cov-report=term-missing -v
start htmlcov/index.html
```

---

## 5. 커버리지 결과

| 모듈 | Stmts | Miss | Cover |
|------|-------|------|-------|
| `converter.py` | 15 | 0 | **100%** |
| `formatter.py` | 5 | 0 | **100%** |
| `parser.py` | 13 | 0 | **100%** |
| `registry.py` | 12 | 0 | **100%** |
| **TOTAL** | **45** | **0** | **100%** |

```
13 passed in 0.27s
```

---

## 6. pyproject.toml 설정 요약

```toml
[project.optional-dependencies]
dev = ["pytest>=8.0", "pytest-cov>=4.0"]

[tool.coverage.run]
source = ["unit_converter"]

[tool.coverage.report]
show_missing = true
```

---

## 7. Git push 이력

| 커밋 | 내용 |
|------|------|
| `5c2f43b` | pytest-cov 설정·testing 가이드 |
| push | `origin/green` (503 재시도 후 성공) |

> `htmlcov/`는 `.gitignore` 처리 — 로컬에서 명령으로 재생성

---

## 8. 후속 단계

| 항목 | 설명 |
|------|------|
| REFACTOR | `UnitConverter.py` → `unit_converter` 위임 |
| P1 RED | TC-11~14 스켈레톤 |
| Activity 4 | 설정 외부화·동적 등록·JSON/CSV |

---

## 9. 관련 문서

- 상세 명령: [`docs/testing.md`](../testing.md)
- TDD 절차: [`docs/analysis/tdd-workflow.md`](../analysis/tdd-workflow.md)
