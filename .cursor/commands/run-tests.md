# 테스트 실행

Unit Converter pytest를 실행하고 결과를 보고한다.

## 작업

1. `python -m pytest tests/ -v` 실행
2. 실패 TC가 있으면 TC ID·원인·수정 방향 제시
3. 전부 통과 시 `docs/analysis/rgio.md` RTM·DoD 갱신 여부 확인

`tests/` 디렉터리가 없으면 Activity 3 미완료 상태임을 알린다.
