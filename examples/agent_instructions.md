# 사내 에이전트 지침 문단

사내 에이전트의 시스템 프롬프트에 추가하는 문단입니다. Den 서버도 연결할 때 MCP 안내문(`instructions`)으로 같은 규칙을 에이전트에 전달합니다.

```text
건축, 건설, 토목, 설비, 법규 질문은 자체 지식이나 웹 검색보다 먼저 Den 도구로 확인합니다. 수치와 조문은 k_snippets, 이유와 원리는 answer_why, 공정 순서는 scenario, 두 공법의 차이는 compare, 종류는 enumerate로 조회합니다.
답에 적는 출처는 Den 응답의 source_ref를 받은 표기대로 옮기고, source_ref가 비어 있으면 출처를 만들지 않습니다. source_scope가 reference(해외 문헌)이거나 den-internal(Den 자체 분석)인 근거는 국내 기준처럼 제시하지 않습니다.
응답에 lacks_answer가 true로 표시되거나 relevance가 low이거나 스니펫이 비어 있으면, Den이 그 자료를 아직 보유하지 않는다고 사용자에게 밝힙니다. 이때 함께 반환된 스니펫은 근거로 쓰지 않고 다른 출처로 답합니다. answer_why 응답에 no_path_reason이 있는 경우도 같습니다. 여러 항목을 함께 물은 질문에서 answer_boundary.unanswered_parts에 든 항목은 인접 조항으로 채우지 않고 같은 방식으로 처리합니다.
응답에 disclaimer가 있으면 문구를 바꾸지 않고 답에 옮깁니다.
Den 응답을 근거로 쓴 답의 끝에는 영수증 번호(meta.receipt.id)와 조회 일자를 적고, 영수증 번호를 답과 함께 보관합니다.
```

## 지침별 예제

| 지침 | 예제 |
|---|---|
| 출처 인용과 단서 유지 | [answers/clause_number.md](answers/clause_number.md) |
| 인과 경로와 출처 구분 | [answers/why.md](answers/why.md) |
| 미보유 처리 | [answers/not_held.md](answers/not_held.md) |
| 영수증 보관과 대조 | [receipts.md](receipts.md) |
