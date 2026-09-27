# den — AEC 전문 지식 큐레이팅 시스템

[![den.archi](https://img.shields.io/badge/den.archi-사용%20신청-c8622a)](https://den.archi)
[![MCP](https://img.shields.io/badge/MCP-remote%20server-333)](https://mcp.den.archi/mcp)
[![Listed on mcpservers.org](https://mcpservers.org/badge.svg)](https://mcpservers.org/servers/den-archi)

AI 에이전트에 AEC 규범·실무 지식을 출처와 함께 제공하는 서버입니다.

```
mcp.den.archi/mcp        원격 MCP 서버 (streamable HTTP)
den.archi                사용 신청 · Claude Desktop 확장(den.mcpb)
```

## 범위

- 국가건설기준 KDS·KCS, KS, 건축 관련 법령·별표를 제공합니다.
- 구조·시공·설비·재료·계획 분야의 기준·실무 지식을 제공합니다.

## 제공 기능

| 도구 | 이름 | 설명 |
|---|---|---|
| `k_snippets` | 기준·조문 찾기 | 한국 건설기준과 건축 법령의 수치·조문을 출처와 함께 반환합니다. |
| `evidence_for` | 연결 근거 확인 | 두 개념 사이 한 연결(유발·가능·선행·대비)의 근거를 반환합니다. |
| `define` | 용어 정의 | 건축·건설 용어 하나의 정의를 반환합니다. |
| `answer_why` | 인과 설명 | 요건·현상의 원리와 득실을 인과 경로와 근거로 반환합니다. |
| `scenario` | 공정 순서 구성 | 관련 공정을 선후 관계로 정렬한 작업 단계를 반환합니다. |
| `compare` | 두 공법 대조 | 두 공법·개념의 공통 단계와 차이를 반환합니다. |
| `enumerate` | 종류 열거 | 한 개념의 종류·구성요소·분류를 반환합니다. |
| `site_context` | 대지 조건 확인 | 지명·좌표를 기후·관할 조건으로 변환합니다. |
| `review_plan` | 평면 법규 검토 | 평면 정보에 적용되는 법규 요건을 점검합니다. |
| `path_between` | 개념 연결 찾기 | 두 개념 사이의 연결 경로를 반환합니다. |
| `traverse` | 선후 관계 따라가기 | 한 개념에서 선행·후속 관계를 따라가 반환합니다. |

- `k_snippets` · `answer_why` · `evidence_for` · `define` 은 `as_of`(YYYY-MM-DD)를 받아 그 시점에 유효한 기준으로 조회합니다.
- 도구는 적재된 자료만 조회하며 외부 서비스를 호출하지 않습니다.

## 근거 표기

- 수치·요건에 출처를 표기합니다.
- 출처는 국내 규범 조문·해외 문헌·den 자체 분석으로 구분합니다.
- 응답의 `source_scope` 값이 구분을 나타냅니다: `kr-norm`(국내 규범) · `reference`(해외 문헌) · `den-internal`(den 자체 분석).

## 한계

- 보유 범위 밖 질의에는 응답하지 않습니다.
- 커버리지는 부분적이며, 미보유 항목은 응답에 명시합니다.
- 응답은 법률·설계 자문이 아닙니다.
- 계약 문서(지체상금 특약·설계변경 절차·하자담보 기간) 질의에서는 den 자체 분석이 법령 조문보다 앞 순위로 반환됩니다. 기록: [den.archi/notes](https://den.archi/notes/)
- 도면·수식 이미지는 입력으로 받지 않습니다. 평면 검토는 도면에서 읽어낸 실·인접·개구부·동선 정보를 입력으로 받습니다.
- 기준 개정은 개정 확인 뒤 반영까지 시차가 있습니다.

## 연결 방법

사용 신청이 승인된 계정으로 진행합니다. 사용 신청은 [den.archi](https://den.archi) 에서 합니다.

1. mcp.den.archi 에 로그인합니다.
2. 대시보드에서 커넥터 주소를 복사합니다.
3. Claude·ChatGPT 의 커스텀 커넥터에 주소를 등록합니다. 인증 방식은 OAuth 입니다.

**Claude Desktop 확장**

- [den.archi](https://den.archi) 에서 `den.mcpb` 를 내려받아 설치합니다.
- 설치 창에 대시보드에서 발급한 API 키를 입력합니다. 키는 OS 키체인에 저장됩니다.

**그 밖의 MCP 클라이언트(키 방식)**

커스텀 커넥터 인증을 지원하지 않는 클라이언트는 대시보드에서 발급한 API 키를 요청 헤더에 넣습니다.

```json
{
  "mcpServers": {
    "den": {
      "url": "https://mcp.den.archi/mcp",
      "headers": { "Authorization": "Bearer <den-api-key>" }
    }
  }
}
```

- 도구 목록 조회(`initialize` · `tools/list`)는 키 없이 가능합니다.
- 도구 호출에는 승인된 계정의 인증이 필요합니다.

## 기록 범위

- 질의 원문은 저장하지 않습니다.
- 질의는 지문(해시)과 형태 특징으로만 기록합니다.
- 호출 기록의 항목은 [약관 및 프라이버시](https://mcp.den.archi/terms)에 있습니다.

## 참고 문서

- [공정 순서 답변의 근거·조건 확인 절차](docs/practice/check-work-sequence.md)
- [응답 기록](examples/real_responses.md)
- [알려진 한계 기록](https://den.archi/notes/)

---

## English

# AEC Expert Knowledge Curation System

den is a server that provides AI agents with Korean AEC codes, standards and practice knowledge, together with their sources.

```
mcp.den.archi/mcp        remote MCP server (streamable HTTP)
den.archi                access requests · Claude Desktop extension (den.mcpb)
```

### Scope

- Covers the Korean Design Standards (KDS), Korean Construction Specifications (KCS), Korean Industrial Standards (KS), and building-related statutes with their annexed tables.
- Covers codes, standards and practice knowledge in structure, construction, building services, materials and planning.

### Functions

| Tool | Name | Description |
|---|---|---|
| `k_snippets` | Find Standard Clauses | Returns values and clauses from Korean building codes and statutes, with their sources. |
| `evidence_for` | Check Evidence For Link | Returns the evidence for one relation between two concepts. |
| `define` | Define Term | Returns the definition of a single AEC term. |
| `answer_why` | Explain Why | Returns the causal paths behind a requirement or phenomenon, with evidence. |
| `scenario` | Build Work Sequence | Returns work steps ordered by their precedence relations. |
| `compare` | Compare Two Methods | Returns the shared steps and differences of two methods or concepts. |
| `enumerate` | Enumerate Kinds | Returns the kinds, components or classes of a concept. |
| `site_context` | Resolve Site Context | Converts a place name or coordinates into climate and jurisdiction conditions. |
| `review_plan` | Review Floor Plan | Checks the statutory requirements that apply to a floor plan description. |
| `path_between` | Find Path Between Concepts | Returns the relation path between two concepts. |
| `traverse` | Follow Order Relations | Returns the preceding and following relations of a concept. |

- `k_snippets`, `answer_why`, `evidence_for` and `define` accept `as_of` (YYYY-MM-DD) and query the standards in force on that date.
- The tools query loaded data only and call no external service.

### Sources

- Each value and requirement is marked with its source.
- Sources are classified as Korean normative clauses, foreign references, or den's own analysis.
- The `source_scope` field in each response records the class: `kr-norm` (Korean norm), `reference` (foreign reference), `den-internal` (den's own analysis).

### Limitations

- Queries outside the curated scope receive no response.
- Coverage is partial, and items outside the curated scope are identified in the response.
- Responses are not legal or design advice.
- For contract documents (liquidated damages clauses, design change procedures, defect liability periods), den's own analysis is returned ahead of the statutory clauses. Record: [den.archi/notes](https://den.archi/notes/)
- Drawings and formula images are not accepted as input. The floor plan review takes rooms, adjacency, openings and circulation read from the drawing.
- Revised standards are applied in den after a revision check, with a time lag.

### Connection

Requires an approved account. Access requests are made at [den.archi](https://den.archi).

1. Sign in at mcp.den.archi.
2. Copy the connector address from the dashboard.
3. Register the address as a custom connector in Claude or ChatGPT, with OAuth as the authentication method.

**Claude Desktop extension**

- Download `den.mcpb` from [den.archi](https://den.archi) and install it.
- Enter the API key issued on the dashboard in the installation dialog. The key is stored in the operating system keychain.

**Other MCP clients (key-based)**

Clients without custom connector authentication send an API key issued on the dashboard in the request header.

```json
{
  "mcpServers": {
    "den": {
      "url": "https://mcp.den.archi/mcp",
      "headers": { "Authorization": "Bearer <den-api-key>" }
    }
  }
}
```

- Discovery (`initialize`, `tools/list`) is available without a key.
- Tool calls require authentication with an approved account.

### Records

- Query text is not stored.
- Queries are recorded only as a fingerprint (hash) and shape features.
- The recorded fields are listed on the [Terms and Privacy](https://mcp.den.archi/terms) page.

### Reference documents

- [Procedure for checking sources and conditions in a work sequence answer](docs/practice/check-work-sequence.md)
- [Response records](examples/real_responses.md)
- [Known limitations](https://den.archi/notes/)
