# Den 사용 예제

AI 에이전트를 Den에 연결하는 설정과, Den 응답을 근거로 답을 작성하는 예제입니다. 답 예제는 2026년 11월 19일 운영 서버(`https://mcp.den.archi/mcp`)에 호출한 응답에서 필드 일부를 옮겼습니다.

## 클라이언트별 연결 설정

| 클라이언트 | 인증 | 문서 |
|---|---|---|
| Claude 웹 | OAuth(커스텀 커넥터) | [clients/claude_web.md](clients/claude_web.md) |
| ChatGPT | OAuth(개발자 모드, PC 웹) | [clients/chatgpt.md](clients/chatgpt.md) |
| Claude Code | API 키(인증 헤더) | [clients/claude_code.md](clients/claude_code.md) |
| Codex | API 키(환경 변수) | [clients/codex.md](clients/codex.md) |
| Cursor | API 키(인증 헤더와 환경 변수) | [clients/cursor.md](clients/cursor.md) |

API 키는 mcp.den.archi에서 가입한 뒤 「키 · 연결된 앱」 화면에서 발급합니다. Claude Desktop 확장(den.mcpb)의 설치 절차는 저장소 [README](../README.md)의 연결 방법에 있습니다.

## 근거가 붙은 답

| 문서 | 도구 | 내용 |
|---|---|---|
| [answers/clause_number.md](answers/clause_number.md) | `k_snippets` | 조문의 수치를 답하고 `source_ref`를 받은 표기대로 인용합니다. |
| [answers/why.md](answers/why.md) | `answer_why` | 인과 경로와 경로별 근거를 출처 구분과 함께 답에 적습니다. |
| [answers/not_held.md](answers/not_held.md) | `k_snippets` | Den이 보유하지 않은 질문에서 미보유를 밝히고 다른 출처로 답합니다. |

## 영수증과 에이전트 지침

| 문서 | 내용 |
|---|---|
| [receipts.md](receipts.md) | 응답마다 붙는 `meta.receipt`의 항목과 근거를 다시 대조하는 절차입니다. |
| [agent_instructions.md](agent_instructions.md) | 사내 에이전트의 시스템 프롬프트에 추가하는 지침 문단입니다. |
| [real_responses.md](real_responses.md) | 2026년 8월 19일에 기록한 `k_snippets` 응답 예시입니다. |

## 발췌 표기

- JSON 발췌에는 응답의 구조와 필드를 보이는 데 필요한 필드만 옮겼습니다.
- 긴 조문 문장은 짧은 구절 하나로 줄이고, 줄인 자리는 `…`로 표시했습니다.
- 응답 내용은 지식 팩 갱신에 따라 달라질 수 있으며, 예제마다 호출 일자와 영수증 번호를 적었습니다.
- 응답은 법률 · 설계 자문이 아닙니다.

## English summary

This folder contains usage examples for Den, the AEC Expert Knowledge Curation System, which runs as a remote MCP server at `https://mcp.den.archi/mcp`.
`clients/` lists the connection settings for Claude on the web, ChatGPT, Claude Code, Codex and Cursor.
`answers/` shows three agent answers built from live responses recorded on 19 November 2026: a clause value cited by its `source_ref`, a causal path from `answer_why`, and a question outside the curated scope.
`receipts.md` describes the receipt attached to each response, and `agent_instructions.md` provides a paragraph for the system prompt of an in-house agent.
