---
name: project-analysis
description: Unit Converter 레거시 코드 스멜·PRD 갭 분석 및 RGIO 실행 계획 수립. 프로젝트 분석, 코드 스멜, PRD 갭, RGIO 정의, Activity 1 요청 시 적용.
---

# 프로젝트 분석

## 분석 워크플로

1. `README.md` (PRD) 읽기
2. `UnitConverter.py` 및 `unit_converter/` (있으면) 읽기
3. 레거시 스멜 목록 작성
4. PRD vs 구현 갭 표 작성
5. `docs/analysis/project-analysis.md` 저장

## RGIO 수립 (분석 후)

`project-analysis.md` 갭·스멜을 바탕으로 `docs/analysis/rgio.md` 작성:

| 항목 | 내용 |
|------|------|
| R | 요구사항 ID (R-01~), P0/P1/P2 우선순위 |
| G | SRP·OCP·DRY 목표, 스멜 해소 매핑 |
| I | 모듈 경계, CLI, 에러 계약 |
| O | TC 시나리오, RTM, DoD |

## 정책 결정 (갭에서 확정)

분석 시 아래를 명시적으로 결정한다:

- 음수: 에러 거부 (PRD 품질 요구)
- 출력: 입력 단위 제외, 소수 1자리
- 구현 순서: Activity 2 → 3 → 4

## 출력 위치

모든 분석 문서는 `docs/analysis/`에 저장한다.

- `project-analysis.md` — 스멜·갭
- `rgio.md` — 실행 계획

기존 문서 갱신 시 ID 체계(R-01, TC-01)와 날짜를 유지·갱신한다.
