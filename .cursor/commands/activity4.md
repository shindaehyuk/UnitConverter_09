# Activity 4 — 추가 요구사항 구현

`docs/analysis/rgio.md`의 P1 요구사항(R-13~R-15)을 구현한다.

## 참조

- `docs/analysis/rgio.md` — R-13~R-15, 설정 파일 계약, CLI
- `.cursor/skills/unit-converter-rgio/SKILL.md` — Activity 4 절

## 작업

1. **R-13** — `config/units.json`에서 변환 비율 로드
2. **R-14** — `--register "1 cubit = 0.4572 meter"` 동적 단위 등록
3. **R-15** — `--format json|csv|table` 출력 포맷 선택
4. TC-11~TC-14 테스트 추가
5. RTM·DoD P1 체크박스 갱신

P0( Activity 2~3 )가 완료된 상태에서 진행한다.

검증:

```bash
python -m pytest tests/ -v
python -m unit_converter "meter:2.5" --format json
```
