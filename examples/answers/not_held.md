# 미보유 질문의 처리

2026년 11월 19일 운영 서버에 호출한 `k_snippets` 응답에서 필드 일부를 옮겼습니다.

| 항목 | 내용 |
|---|---|
| 호출 일자 | 2026년 11월 19일 |
| 도구 | `k_snippets`(`limit=3`) |
| 서빙 팩 | `2026-11-17-scheduled` |
| 영수증 번호 | `dr1-b577ad9b790316f0` |

## 질문

> 전통 한옥 지붕에서 기와를 받치는 연함의 단면 치수 기준

## 응답 발췌

```json
{
  "relevance": "low",
  "abstained": false,
  "lacks_answer": true,
  "lacks_answer_note": "den 이 이 질문에 **답할 자료를 갖고 있지 않을 가능성이 높다** … 아래 스니펫은 den 코퍼스에서 가장 가까운 것일 뿐 질문에 답하지 않는다 — **수치·요건을 여기서 인용하지 말 것.** … 이 분야를 아직 갖고 있지 않다고 답하라.",
  "snippets": [
    {
      "item": {
        "statement": "표 2.1-1 기와의 규격 …",
        "source_ref": "KCS 41 56 03:2021 한식 기와 2.1 한식형 기와 표 2.1-1",
        "decision_grade": "A"
      }
    },
    {
      "item": {
        "statement": "표 4.5-8 5량가 주심도리 단면조견표 …",
        "source_ref": "KDS 42 50 20:2022 소규모건축 전통목구조 4.5.1 지붕도리의 설계 표 4.5-8",
        "decision_grade": "A"
      }
    },
    {
      "item": {
        "statement": "표 4.8-1 기둥 단면조견표 …",
        "statement_truncated": true,
        "source_ref": "KDS 42 50 20:2022 소규모건축 전통목구조 4.8.1 기둥의 설계 표 4.8-1",
        "decision_grade": "A"
      }
    }
  ],
  "source_standards_note": "… **질의가 가리키는 기준과 다른 기준의 조항이 섞일 수 있다** …",
  "requirements": [],
  "answer_card": {
    "answer": "",
    "items": [],
    "den_unavailable": [{"reason": "retrieval_below_answer_threshold"}]
  },
  "meta": {
    "receipt": {
      "id": "dr1-b577ad9b790316f0",
      "issued_at": "2026-11-19T00:14:39Z",
      "v": 1,
      "tool": "k_snippets",
      "q_sha256": "dfab9e4f59767126",
      "as_of": null,
      "pack": {"version": "2026-11-17-scheduled", "sha256": "43ee332a41a65e29"},
      "code": "d02ceb9509f66821",
      "nodes": [
        "kr-kcs-41-56-03-norm-2-1-한식-기와-표-2-1-1-기와의-규격-nbsp-단위#e7e2dd46f8ed",
        "kr-kds-42-50-20-norm-4-5-1-소규모건축-전통목구조-표-4-5-8-5량#61487faa4f07",
        "kr-kds-42-50-20-norm-4-8-1-소규모건축-전통목구조-표-4-8-1-기둥-단면조견표#f15b033fcc2f"
      ],
      "response_sha256": "14105ae56bc913252480c6c67f12c491",
      "non_node_refs": 2
    }
  }
}
```

## 에이전트의 답

> Den은 한옥 지붕 연함의 단면 치수 기준을 아직 보유하지 않습니다. Den 조회 결과가 미보유로 표시되었고, 함께 반환된 한식 기와 규격표와 전통목구조 단면조견표는 연함 치수를 다루지 않아 근거로 쓰지 않았습니다.
>
> 연함 치수는 다른 출처에서 확인합니다. 전통 건축 수리 분야의 표준시방서 등 원문을 찾아 출처와 함께 답하겠습니다.
>
> Den 조회 기록: 영수증 `dr1-b577ad9b790316f0` (2026년 11월 19일, 미보유 응답)

## 미보유 신호와 에이전트의 처리

| 응답 필드 | 이 응답 | 에이전트의 처리 |
|---|---|---|
| `lacks_answer` | `true` | Den이 이 질문의 자료를 아직 보유하지 않는다고 답에 밝힙니다. |
| `relevance` | `low` | 함께 반환된 스니펫을 근거로 쓰지 않습니다. |
| `answer_card.den_unavailable` | `retrieval_below_answer_threshold` | 검색 관련도가 답 작성 기준에 미달해 답 카드(`answer_card`)의 항목이 비어 있습니다. |
| `snippets` | 한식 기와 규격표, 전통목구조 단면조견표 | 질문과 주제가 가까운 인접 자료로, 질문에 답하지 않습니다. 표의 수치를 연함 치수로 옮기지 않습니다. |

- 미보유는 「범위 밖」 대신 「아직 보유하지 않음」으로 적습니다.
- 다른 출처에서 확인한 내용에는 Den 영수증 번호를 붙이지 않습니다. 영수증 번호는 Den을 조회해 미보유 응답을 받았다는 기록으로 남깁니다.
- 여러 항목을 함께 묻는 질문에서는 응답의 `answer_boundary.status`가 `partial`로, 보유하지 않은 항목이 `unanswered_parts`로 표시됩니다. 그 항목에도 같은 처리를 적용하고, 인접 조항으로 빈 항목을 채우지 않습니다.
