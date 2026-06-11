# RGIO 대비 구현 리뷰

현재 코드가 `docs/analysis/rgio.md` 요구사항을 충족하는지 검토한다.

## 참조

- `docs/analysis/rgio.md` — R/G/I/O 전체
- `docs/analysis/project-analysis.md` — 원본 갭·스멜

## 작업

1. R-01~R-15 각 요구사항별 구현 상태 판정 (✅/⚠️/❌)
2. G-01~G-05 설계 목표 달성 여부 검토
3. I — 에러 메시지·모듈 경계·CLI 계약 일치 여부
4. O — TC 통과 여부, RTM 갱신 필요 항목 목록
5. 미충족 항목을 우선순위와 함께 목록으로 보고

코드 수정은 요청 시에만 수행한다. 리뷰 결과만 먼저 제시한다.

검증 명령:

```bash
python -m pytest tests/ -v
```
