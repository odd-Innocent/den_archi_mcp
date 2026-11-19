# 조문 수치 질문의 답과 출처 인용

2026년 11월 19일 운영 서버에 호출한 `k_snippets` 응답에서 필드 일부를 옮겼습니다.

| 항목 | 내용 |
|---|---|
| 호출 일자 | 2026년 11월 19일 |
| 도구 | `k_snippets`(`limit=3`) |
| 서빙 팩 | `2026-11-17-scheduled` |
| 영수증 번호 | `dr1-5ea4d011904179d2` |

## 질문

> 외기온도가 25℃ 이상일 때 콘크리트 비비기부터 타설 완료까지 허용되는 시간

## 응답 발췌

```json
{
  "relevance": "high",
  "abstained": false,
  "snippets": [
    {
      "concept_id": "kh-ob-7195edf8de",
      "item": {
        "kind": "practice_rule",
        "statement": "… 외기온 25℃ 초과 시 1.5시간 …",
        "source_ref": "KCS 14 20 10 일반콘크리트",
        "source_scope": "kr-norm",
        "decision_grade": "B"
      }
    },
    {
      "concept_id": "kr-kcs-14-20-10-norm-3-2-일반콘크리트-콘크리트",
      "item": {
        "kind": "norm_clause",
        "statement": "… 외기온도가 25 °C 이상일 때는 1.5시간 …",
        "statement_truncated": false,
        "source_ref": "KCS 14 20 10:2024 일반콘크리트 3.2 운반 (3)",
        "source_scope": "kr-norm",
        "decision_grade": "A",
        "valid_from": "2024-01-01"
      }
    },
    {
      "concept_id": "kh-ob-b56b74f2b0",
      "item": {
        "kind": "practice_rule",
        "statement": "… 허용 이어치기 시간간격 …",
        "source_ref": "KCS 14 20 10(일반콘크리트) 타설·이어치기",
        "source_scope": "kr-norm",
        "decision_grade": "B"
      }
    }
  ],
  "decision_grade_note": {
    "A": "기준·법령의 조문 원문이다 — 이 문장을 그대로 인용할 수 있다",
    "B": "규범 원문이 아니다 — 판단 근거로 쓰기 전에 해당 기준 원문을 확인할 것"
  },
  "verbatim_conditions_note": "… 다만 단서를 바꾸거나 생략하지 말고 statement를 그대로 인용하라. …",
  "source_standards": [
    {"code": "KCS 14 20 10", "name": "일반콘크리트", "snippets": 3}
  ],
  "answer_card": {
    "items": [
      {
        "source_ref": "KCS 14 20 10:2024 일반콘크리트 3.2 운반 (3)",
        "decision_grade": "A",
        "confidence_basis": "retrieval relevance only; not a correctness or applicability guarantee"
      }
    ],
    "den_unavailable": []
  },
  "meta": {
    "receipt": {
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
  }
}
```

## 에이전트의 답

> 외기온도가 25 °C 이상이면 콘크리트를 비비기 시작한 때부터 타설을 끝낼 때까지의 시간이 1.5시간 이내여야 하고, 25 °C 미만이면 2시간 이내여야 합니다. 지연제를 쓰는 등 응결을 늦추는 특별한 조치를 한 경우에는 품질 변동이 없는 범위에서 책임기술자의 승인을 받아 이 시간 제한을 변경할 수 있습니다.
>
> 출처: `KCS 14 20 10:2024 일반콘크리트 3.2 운반 (3)`
>
> Den 영수증: `dr1-5ea4d011904179d2` (2026년 11월 19일 조회)

## 답에 반영한 응답 필드

| 응답 필드 | 답에 반영한 내용 |
|---|---|
| `source_ref` | 받은 문자열을 바꾸지 않고 적습니다. 판 연도와 항 번호가 붙은 `KCS 14 20 10:2024 일반콘크리트 3.2 운반 (3)`을 다른 형식으로 줄이지 않습니다. |
| `decision_grade` | A 항목은 기준 · 법령의 조문 원문이고, B 항목은 실무 요약입니다. 이 응답의 B 항목은 경계를 「25℃ 초과」로 적었고 조문 원문은 「25 °C 이상」으로 적었으므로, 답은 조문 원문의 표현을 따릅니다. |
| `verbatim_conditions_note` | 조문의 단서(특별한 조치를 한 경우의 시간 제한 변경)를 답에서 빼지 않습니다. |
| `source_standards` | 근거 기준이 모두 `KCS 14 20 10`(일반콘크리트)으로 질문 분야와 일치합니다. 기준 코드가 질문 분야와 다르면 그 수치를 쓰지 않습니다. |
| `answer_card.items[].confidence_basis` | 신뢰도는 검색 관련도만 나타냅니다. 답에 정확도처럼 옮기지 않습니다. |
| `disclaimer` | 이 응답에는 없습니다. 응답에 있으면 문구를 바꾸지 않고 답에 옮깁니다. |
| `meta.receipt.id` | 답 끝에 영수증 번호와 조회 일자를 적습니다. 영수증 항목은 [receipts.md](../receipts.md)에 있습니다. |
