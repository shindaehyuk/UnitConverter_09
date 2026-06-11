# REPORT 03 — Cursor 워크플로 구성

| 항목 | 내용 |
|------|------|
| **단계** | AI 개발 환경 구성 |
| **상태** | ✅ 완료 |
| **산출물** | `.cursor/rules/`, `.cursor/skills/`, `.cursor/commands/` |
| **Git** | `red` 브랜치 (`9e3525e`) |

---

## 1. 목적

RGIO·Activity 흐름을 Cursor AI가 **일관되게 따르도록** 프로젝트 규칙·스킬·커맨드를 구성했다.

---

## 2. Rules (자동 컨텍스트)

| 파일 | 적용 범위 | 역할 |
|------|-----------|------|
| `project-context.mdc` | alwaysApply | 프로젝트·Activity·정책 |
| `python-architecture.mdc` | `**/*.py` | SRP/OCP·모듈 경계·에러 계약 |
| `python-tests.mdc` | `tests/**` | TDD 사이클·TC·RTM |
| `docs-analysis.mdc` | `docs/**` | 분석 문서 작성 규칙 |

### 핵심 규칙 요약

- 변환 계수: `UnitRegistry` 단일 정의
- meter 경유 변환, 입력 단위 제외 출력
- RED: pass 금지 · GREEN: 최소 구현 · REFACTOR: 별도 요청

---

## 3. Skills (워크플로 가이드)

| 스킬 | 용도 |
|------|------|
| `project-analysis` | 스멜·갭 분석, RGIO 수립 |
| `unit-converter-rgio` | Activity 2~4 구현, GREEN 절차 |
| `unit-converter-test` | TC 작성·RTM 갱신 |

---

## 4. Commands (슬래시 메뉴)

| 커맨드 | Activity | 설명 |
|--------|----------|------|
| `/analyze` | 1 | 프로젝트 분석 |
| `/activity2` | 2 | P0 구현 |
| `/activity3` | 3 | TC 작성 |
| `/activity4` | 4 | P1 추가 기능 |
| `/review-rgio` | — | RGIO 대비 리뷰 |
| `/run-tests` | — | pytest·커버리지 |

---

## 5. 권장 사용 순서

```
/analyze → /activity2 → /activity3 → /activity4
              ↓              ↓
           GREEN          TC·RTM
```

---

## 6. 디렉터리 구조

```
.cursor/
├── rules/          4개 .mdc
├── skills/         3개 SKILL.md
└── commands/       6개 .md
```

---

## 7. 후속 단계

→ [REPORT 04 — RED 단계](./04-red-phase-report.md)
