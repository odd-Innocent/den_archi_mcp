# den — 조문까지 붙여 답하는 AEC MCP 서버

[![den.archi](https://img.shields.io/badge/den.archi-얼리%20액세스-c8622a)](https://den.archi)
[![MCP](https://img.shields.io/badge/MCP-remote%20server-333)](https://mcp.den.archi/mcp)

한국 건설기준(KDS·KCS·KS)과 건축 법령을 **조문 번호까지 붙여** 답합니다.
근거를 찾지 못하면 추측하지 않고, 확실하지 않다고 말합니다.

```
mcp.den.archi/mcp        원격 MCP 서버
den.archi                얼리 액세스 신청 · Claude Desktop 확장 내려받기
```

---

## 왜 필요한가

AI에게 "옥내소화전 방수구 높이"를 물으면 그럴듯한 숫자가 돌아옵니다.
맞을 때도 있고 틀릴 때도 있는데, **어느 쪽인지 알 방법이 없습니다.**

실무에서 이건 답을 못 얻은 것보다 나쁩니다. 확인하러 기준을 다시 펴야 하니까요.

den은 답에 출처를 붙입니다. 붙일 근거가 없으면 답하지 않습니다.

---

## 실제 응답

아래는 편집 없이 그대로 옮긴 실제 응답입니다.

**① 기준이 있는 질문**

> 옥내소화전 방수구 설치 높이

```
relevance: high · confidence 0.998
근거: 옥내소화전설비의 화재안전기술기준(NFTC 102) · KCS 31 80 10

  옥내소화전은 노즐 선단 방수압력 0.17 MPa 이상 0.7 MPa 이하,
  방수량 130 L/min 이상을 확보해야 한다. 방수압력이 0.7 MPa를 초과하면
  호스접결구 인입측에 감압장치를 설치하고, 방수구는 바닥에서 높이 1.5 m 이하,
  건축물 각 부분으로부터 수평거리 25 m 이하로 배치한다.
```

**② 법령이 정한 수치**

> 지하주차장 직각주차 최소 주차구획 크기

```
relevance: high · confidence 0.968
근거: 주차장법 시행규칙 제3조

  평행주차 외(직각 등)는 경형 2.0m×3.6m, 일반형 2.5m×5.0m,
  확장형 2.6m×5.2m, 장애인전용 3.3m×5.0m, 이륜차 1.0m×2.3m다.
```

**③ 정성적 판단 — den이 자신 없다고 말하는 경우**

> 카페 인테리어에 어울리는 조명 색온도 추천

```
relevance: low · confidence 0.237
```

색온도 분류 자료는 갖고 있지만 "어울리는"은 규범이 정하는 것이 아닙니다.
den은 이럴 때 **낮은 확신도를 그대로 표시**합니다. 판단은 여러분이 합니다.

---

## 측정

같은 모델, 같은 문항, den만 붙였다 뗐다 하며 비교했습니다.

| | 정답률 |
|---|---|
| den 없이 | 166/192 |
| den 붙임 | 183/192 |
| **차이** | **+8.9%p** |

급수별로는 **기능장 +20.0%p · 관리사 +15.0%p · 기사 +6.8%p · 산업기사 ±0**.
쉬운 문제는 AI도 맞힙니다. 전문 심화로 갈수록 벌어집니다.

> 공개 기출 문제라 양쪽 모두 암기분이 섞여 있습니다.
> 절대 점수는 실제 실력보다 높으니 **차이만** 보십시오.

다른 모델(sol)에서도 같은 방향으로 +7.3%p 였습니다.

---

## 못 하는 것

신뢰가 제품이라 여기부터 적습니다.

- **건축계획·실내건축** — 정성적 판단 영역은 약합니다. 위 ③ 이 그 예입니다.
- **계약 문서 해석** — 지체상금 면제·설계변경·하자담보는 현재 회수하지 못합니다(내부 골든 3문항 실패, 공개 추적 중).
- **도면·수식 이미지** — 텍스트 기준만 다룹니다.
- **최신 개정 즉시 반영** — 개정 감시는 돌지만 반영에 시차가 있습니다.

범위 밖에서는 답을 만들어내는 대신 확신도를 낮춥니다.

---

## 설치

**Claude Desktop**

1. [den.archi](https://den.archi) 에서 `den.mcpb` 를 내려받아 실행합니다.
2. 얼리 액세스 승인 후 대시보드에서 발급한 API 키를 입력합니다.
3. 키는 OS 키체인에 저장되고, 번들된 로컬 프록시가 요청 헤더에 붙여 보냅니다.

**그 밖의 MCP 클라이언트**

```json
{
  "mcpServers": {
    "den": {
      "url": "https://mcp.den.archi/mcp",
      "headers": { "Authorization": "Bearer <your-key>" }
    }
  }
}
```

---

## 도구

| 도구 | 하는 일 |
|---|---|
| `k_snippets` | 건설기준·법령의 수치와 조문 원문을 찾습니다 |
| `answer_why` | 왜 그런 규정인지 인과 경로로 설명합니다 |
| `evidence_for` | 특정 주장의 근거 조문을 찾습니다 |
| `compare` | 두 기준·공법을 나란히 놓고 비교합니다 |
| `path_between` | 두 개념이 어떻게 이어지는지 보여줍니다 |
| `scenario` | 상황을 주면 적용되는 기준을 모읍니다 |
| `enumerate` · `traverse` | 목록·인접 개념을 훑습니다 |
| `site_context` | 지명·좌표를 기후·관할 조건으로 바꿉니다 |
| `review_plan` | 계획안을 기준에 비추어 검토합니다 |

`as_of` 를 주면 그 시점의 기준으로 답합니다. 과거 발주도서·분쟁 검토용입니다.

---

## 질의 내용은 저장하지 않습니다

den 서버는 여러분이 무엇을 물었는지 **디스크에 남기지 않습니다.**
남는 것은 복원 불가능한 지문과 형태 정보뿐입니다.

```json
{"query_fp": "a8edb8c424a5c84b",
 "query_shape": {"len_bucket": "s", "has_number": true, "lang": "ko"},
 "tool": "k_snippets", "relevance": "high"}
```

질의 원문·인자는 기록되지 않으며, 이 규칙은 서버 불변식으로 검사됩니다.
설계 도면이나 미공개 프로젝트 내용을 물어도 서버에 문장이 남지 않습니다.

---

## 현재 상태

**베타 · 무료.** 얼리 액세스는 [den.archi](https://den.archi) 에서 신청하시면
검토 후 승인해 드립니다.

틀린 답을 만나면 알려 주십시오. den은 틀린 답을 **사례로 기록해서**
그 조문을 다시 저작합니다 — 저희가 가장 중요하게 보는 지표입니다.

---

## English

**den** is a remote MCP server for Korean AEC (architecture · engineering · construction)
standards. It answers with the clause number attached — KDS, KCS, KS, and building law —
and stays silent when it has no grounds.

- Endpoint: `https://mcp.den.archi/mcp` (Bearer token)
- Desktop extension: [den.archi](https://den.archi) → `den.mcpb`
- Measured lift: **+8.9%p** on 192 national qualification exam items, same model,
  den toggled on/off. Largest gains on advanced tiers (+20.0%p on 기능장 / master craftsman).
  *Public past exams — both sides include memorized content, so read the delta, not the absolute.*
- **Query text is never written to disk.** Only a non-reversible fingerprint and shape metadata.
- Weak on qualitative design judgment and contract-document interpretation. Stated up front.

Beta, free. Request access at [den.archi](https://den.archi).
