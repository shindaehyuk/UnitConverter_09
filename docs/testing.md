# 테스트 · 커버리지 가이드

> 프로젝트 루트: `c:/DEV/UnitConverter_09`  
> 커버리지 대상: `unit_converter/`

---

## (선택) dev 의존성 설치

다른 환경에서 처음 세팅할 때:

```bash
cd c:/DEV/UnitConverter_09

# 가상환경 (권장)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# editable 설치 + dev 도구 (pytest, pytest-cov)
pip install -e ".[dev]"
```

`requirements-dev.txt`만 쓸 경우:

```bash
pip install -r requirements-dev.txt
pip install -e .
```

---

## 기본 테스트

프로젝트 루트에서 실행:

```bash
cd c:/DEV/UnitConverter_09

# 전체 테스트
python -m pytest tests/ -v

# parser (TC-01, TC-04~06)
python -m pytest tests/test_parser.py -v

# converter (TC-01~03, TC-07~10)
python -m pytest tests/test_converter.py -v

# formatter (TC-01, TC-08)
python -m pytest tests/test_formatter.py -v

# TC-01 단일 — 변환
python -m pytest tests/test_converter.py::test_tc01_meter_to_feet_and_yard -v

# TC-04 단일 — 음수 검증
python -m pytest tests/test_parser.py::test_tc04_negative_value_rejected -v

# TC-10 단일 — registry 확장 (OCP)
python -m pytest tests/test_converter.py::test_tc10_registry_extension_without_converter_change -v
```

---

## 커버리지 — 터미널

```bash
# 전체 테스트 + unit_converter 커버리지 (미실행 줄 표시)
python -m pytest tests/ --cov=unit_converter --cov-report=term-missing -v

# parser 모듈 테스트만
python -m pytest tests/test_parser.py --cov=unit_converter --cov-report=term-missing -v

# converter 모듈 테스트만 (P0 GREEN 확인용)
python -m pytest tests/test_converter.py --cov=unit_converter --cov-report=term-missing -v
```

---

## 커버리지 — HTML 리포트

```bash
# HTML 생성 (htmlcov/ 폴더)
python -m pytest tests/ --cov=unit_converter --cov-report=html:htmlcov --cov-report=term-missing -v

# converter 테스트만 HTML
python -m pytest tests/test_converter.py --cov=unit_converter --cov-report=html:htmlcov --cov-report=term-missing -v
```

생성 후 브라우저에서 열기:

```bash
# Windows (PowerShell / CMD)
start htmlcov/index.html

# Git Bash
explorer htmlcov/index.html
```

---

## TC ID 빠른 참조

| 파일 | TC ID |
|------|-------|
| `test_parser.py` | TC-01, TC-04, TC-05, TC-06 |
| `test_converter.py` | TC-01, TC-02, TC-03, TC-07, TC-08, TC-09, TC-10 |
| `test_formatter.py` | TC-01, TC-08 |

상세 시나리오: `docs/analysis/rgio.md` O 섹션
