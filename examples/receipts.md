# 응답 영수증

Den 응답의 `meta.receipt`에는 응답을 만든 지식 팩 판, 서버 코드, 근거 지식 항목과 그 내용 지문이 기록됩니다. 질의 원문은 영수증에 포함되지 않습니다.

## 영수증 예시

[조문 수치 예제](answers/clause_number.md)의 영수증입니다(2026년 11월 19일 발행).

```json
{
  "id": "dr1-5ea4d011904179d2",
  "issued_at": "2026-11-19T00:07:00Z",
  "v": 1,
  "tool": "k_snippets",
  "q_sha256": "ada2351ff60edf4c",
  "as_of": null,
  "pack": {"version": "2026-11-17-scheduled", "sha256": "43ee332a41a65e29"},
  "code": "d02ceb9509f66821",
  "nodes": [
    "kh-ob-7195edf8de#d10fe3d8314e",
    "kr-kcs-14-20-10-norm-3-2-일반콘크리트-콘크리트#1473b6d97f65",
    "kh-ob-b56b74f2b0#6c9559dcf2e7"
  ],
  "response_sha256": "c488b27242b88a61c024119595adc54c",
  "non_node_refs": 1
}
```

## 영수증 항목

| 필드 | 내용 |
|---|---|
| `id` | 영수증 번호입니다. 발행 시각을 제외한 영수증 본문의 지문이며, 도구, 질의, 기준 시점, 팩 판, 코드, 응답이 모두 같으면 같은 번호가 됩니다. |
| `issued_at` | 발행 시각(UTC)입니다. |
| `v` | 영수증 형식의 판입니다. |
| `tool` | 호출한 도구 이름입니다. |
| `q_sha256` | 도구 이름과 질의 문장으로 계산한 지문입니다. 질의 원문을 보관한 사용자만 이 영수증이 자기 질의의 기록인지 대조할 수 있습니다. |
| `as_of` | 호출 때 지정한 기준 시점입니다. `null`이면 호출한 날의 현행 기준으로 조회했습니다. |
| `pack` | 지식 팩의 판(`version`)과 팩 파일의 지문(`sha256`)입니다. |
| `code` | 응답한 서버 코드의 지문입니다. |
| `nodes` | 응답에 쓴 지식 항목 목록입니다. 항목마다 `지식 항목 id#내용 지문` 형식으로 적힙니다. |
| `response_sha256` | `meta`를 제외한 응답 본문의 지문입니다. |
| `non_node_refs` | 응답이 참조한 식별자 가운데 지식 팩의 항목으로 대조되지 않는 참조의 수입니다. 해당 참조가 있을 때만 표시됩니다. |

## 근거를 다시 대조하는 절차

### 보관

- 에이전트는 Den 응답을 근거로 쓴 답의 끝에 영수증 번호와 조회 일자를 적습니다.
- 나중에 근거를 대조해야 하는 답은 응답 JSON 전체를 사용자 쪽에서 보관합니다. 영수증은 응답의 `meta`에 들어 있습니다.
- mcp.den.archi에 로그인하면 콘솔의 「서빙 이력」 화면에서 호출 시각, 도구, 결과, 영수증 번호를 볼 수 있습니다.

### 응답과 영수증의 변경 여부 확인

보관한 응답으로 지문을 다시 계산해 영수증과 비교합니다. 지문은 키를 정렬하고 공백 없는 구분자로 직렬화한 JSON(UTF-8)의 SHA-256 앞부분입니다.

```python
import hashlib
import json


def _canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")


def response_sha256(response: dict) -> str:
    """meta 를 제외한 응답 본문의 지문"""
    body = {k: v for k, v in response.items() if k != "meta"}
    return hashlib.sha256(_canonical(body)).hexdigest()[:32]


def q_sha256(tool: str, question: str) -> str:
    """도구 이름과 질의 문장의 지문"""
    return hashlib.sha256(f"{tool}\0{question}".encode("utf-8")).hexdigest()[:16]


def receipt_id(receipt: dict) -> str:
    """발행 시각을 제외한 영수증 본문의 지문"""
    body = {k: v for k, v in receipt.items() if k not in ("id", "issued_at")}
    return "dr1-" + hashlib.sha256(_canonical(body)).hexdigest()[:16]
```

- 세 함수의 결과가 영수증의 `response_sha256`, `q_sha256`, `id`와 같으면 보관한 응답과 영수증은 발행 뒤 바뀌지 않았습니다.
- 2026년 11월 19일 [조문 수치 예제](answers/clause_number.md)와 [미보유 예제](answers/not_held.md)의 응답 전문과 질의로 계산한 세 지문은 영수증과 일치했습니다.
- 에이전트 클라이언트를 거치며 숫자 표기가 바뀌면 지문이 달라질 수 있습니다. 같은 날 [인과 질문 예제](answers/why.md)의 `answer_why` 응답에서는 서버가 `1.0`으로 계산한 필드가 클라이언트에 `1`로 전달되었습니다. 지문이 다르면 정수로 표기된 실수 필드를 먼저 확인합니다.

### 같은 질문의 재조회

- 같은 도구에 같은 질의와 같은 `as_of`로 다시 호출하고, 새 영수증과 비교합니다.
- `pack.version`과 `code`가 같고 응답 본문이 같으면 영수증 번호도 같습니다.
- 지식 팩이 갱신된 뒤에는 `nodes`를 비교합니다. 같은 지식 항목의 내용 지문이 같으면 그 근거 내용은 바뀌지 않았고, 지문이 다르면 근거 내용이 갱신되었습니다.
- `as_of`를 받는 도구(`k_snippets`, `answer_why`, `evidence_for`, `define`)는 `issued_at`의 날짜(UTC)를 `as_of`로 지정해 그날 유효했던 기준으로 다시 조회할 수 있습니다.

## 영수증의 판정 범위

- 영수증은 근거의 출처와 시점을 기록합니다. 답의 옳고 그름과 현장 적용 여부는 판정하지 않습니다.
- 응답의 `confidence_basis`(`retrieval relevance only; not a correctness or applicability guarantee`)도 신뢰도가 검색 관련도라는 점을 밝힙니다.
- 적용 여부는 기준 원문과 담당 기술자의 검토로 확인합니다. 응답은 법률 · 설계 자문이 아닙니다.
