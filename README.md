# den — 한국 AEC 지식 큐레이션 MCP 서버

[![den.archi](https://img.shields.io/badge/den.archi-얼리%20액세스-c8622a)](https://den.archi)
[![MCP](https://img.shields.io/badge/MCP-remote%20server-333)](https://mcp.den.archi/mcp)
[![Listed on mcpservers.org](https://mcpservers.org/badge.svg)](https://mcpservers.org/servers/den-archi)

**당신의 Agent 에게, AEC 전문 지식을.** — *Curated AEC expertise for your agent.*

den 은 AEC 전문 지식을 큐레이션해 Agent 에 공급하는 MCP 서버입니다. 기준·법령 조문과 실무 규칙·이론·공정·인과가
한 그래프에 있어, 어디에 쓰여 있는지만이 아니라 **왜 그런지 · 무엇이 먼저인지 · 무엇과 다른지**까지 답합니다.
근거가 없으면 답하지 않습니다.

조문만 찾아 주지 않습니다 — **왜** 그런지, **어떤 순서**로 해야 하는지,
무엇과 **어떻게 다른지**까지 답합니다.

수치에는 **조문**이, 관계에는 **근거**가 붙습니다.
근거를 찾지 못하면 추측하지 않고, 확실하지 않다고 말합니다.

```
mcp.den.archi/mcp        원격 MCP 서버
den.archi                얼리 액세스 신청 · Claude Desktop 확장 내려받기
```

**다루는 것 — 기준과 법령**
국가건설기준 KDS(설계기준)·KCS(표준시방서)·KS, 건축법을 비롯한 법령 조문과 별표,
건축물 내진설계기준(KDS 41 17 00), 주차장법·소방 관련 기술기준, 계약예규.

**다루는 것 — 전공 지식과 그 연결**
구조·시공·설비·재료의 실무 규칙, 공정의 선후 관계, 성능과 하자의 인과,
설계 판단의 근거. 이것들이 조문과 **한 그래프 위에** 놓여 있습니다 —
그래서 "이 수치가 왜 이런가", "무엇이 먼저인가", "무엇과 어떻게 다른가"에 답합니다.

커버리지는 부분적입니다 — 보유하지 않은 것은 보유하지 않았다고 말합니다.

---

## 조문 검색 MCP 와 무엇이 다른가

조문을 찾아 주는 MCP 는 "어디에 쓰여 있나"를 답합니다. 실무에서 그다음에 오는 물음은
"왜 그런가 · 무엇이 먼저인가 · 무엇과 다른가"이고, den 은 그것을 같은 그래프에서 답합니다.
아래 실제 응답 ④·⑤가 그 차이입니다.

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

**④ 왜 — 인과를 묻는 질문 (`answer_why`)**

> 왜 콘크리트에 양생이 필요한가

```
relevance: high · intent: physical
paths:
  curing --causes--> concrete-strength   (stance: consensus)
  curing --causes--> durability          (stance: consensus)
evidence:
  양생은 수화 지속을 위해 수분·온도를 유지하는 과정이다.        ← KCS 14 20 콘크리트공사 (kr-norm)
key_facts:
  "(6) 보온 양생이 끝난 후에는 양생을 계속하여 관리재령에서 예상되는 하중에
   필요한 강도를 얻을 수 있게 실시하여야 한다."                ← KCS 14 20 40:2024 3.4.2 (kr-norm)
  SMCS 14 20 10:2018 3.6.1 양생 일반사항 (2)                 ← source_scope: reference
caveats: scope(climate · epoch · tech_level) 를 경로마다 표시
```

해외 문헌은 `reference` 로, 국내 규범은 `kr-norm` 으로 갈라 표시됩니다. 섞이지 않습니다.

**⑤ 순서 — 공정을 묻는 질문 (`scenario`)**

> 철근콘크리트 골조 시공 순서

```
process: 철근콘크리트 골조 1개층 시공 · relevance: high · stages: 6
  ① 기둥·벽 배근  ∥  ② 기둥·벽 거푸집        (parallel start)
  ③ 매설물·검측 → ④ 콘크리트 타설 → ⑤ 다짐 → ⑥ 양생
gaps: 먹매김 · 거푸집 해체 — 아직 정본 노드 없음 (missing_step_node 로 보고)
note: 그래프의 선후 엣지로 위상정렬한 부분순서. LLM 없음. 없는 단계는 지어내지 않고 갭으로 보고.
```

**⑥ 왜 질문에서도, 근거가 없으면 답하지 않습니다**

> 왜 방수층 위에 보호몰탈을 까는가

```
relevance: low · paths: []
no_path_reason: 그래프에 해당 질문 유형의 유의미한 경로 없음
```

정답이 있는 물음이지만 den 은 아직 그 인과를 갖고 있지 않습니다. 그럴 때는 이렇게 돌아옵니다.

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
| `answer_why` | 왜 그런 규정·현상인지 인과 경로로 설명합니다 |
| `scenario` | 공정을 선후 관계로 구성해 순서 있는 단계로 돌려줍니다 |
| `compare` | 두 공법·개념을 나란히 놓고 차이를 대조합니다 |
| `enumerate` | 종류·구성요소·분류를 열거합니다 |
| `site_context` | 지명·좌표를 기후·관할 조건으로 바꿉니다 |
| `review_plan` | 평면(실 구성)을 법규에 비추어 검토합니다 |
| `emotional_palette` | 공간을 순서대로 지날 때의 분위기 전이를 읽습니다 |
| `path_between` · `traverse` | 두 개념의 연결, 한 개념의 선후 이웃을 보여줍니다 |
| `k_snippets` | 건설기준·법령의 수치와 조문 원문을 찾습니다 |
| `evidence_for` | 한 연결(A 가 B 를 유발한다)의 근거를 확인합니다 |
| `define` | 용어의 뜻을 정의합니다 |

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

**Curated AEC expertise for your agent.**

**den** curates Korean AEC (architecture · engineering · construction) expertise and
serves it over MCP.

It does more than look clauses up. It answers **why** a figure is what it is, **in what
order** work has to happen, and **how** one thing differs from another. Figures arrive
with their clause; relationships arrive with their grounds. Where den has no grounds,
it says so instead of guessing.

**What it covers — codes and law**
KDS (design standards), KCS (construction specifications), KS, the Building Act and its
subordinate rules and annexes, seismic design of buildings (KDS 41 17 00), parking and
fire-safety technical standards, public-contract regulations.

**What it covers — domain knowledge and how it connects**
Practice rules across structure, construction, MEP and materials; the order operations
have to follow; the causal chain from performance to defect; the reasoning behind design
decisions. These sit on **one graph** together with the clauses — which is what lets den
answer "why is this number what it is", "what comes first", "how does this differ".

Coverage is partial, and den names what it does not hold.

- Endpoint: `https://mcp.den.archi/mcp` — add it as a custom connector and sign in (OAuth).
  A Bearer key is optional, for clients without connector support.
- Desktop extension: [den.archi](https://den.archi) → `den.mcpb`
- Measured lift: **+8.9%p** on 192 national qualification exam items, same model,
  den toggled on/off. Largest gains on advanced tiers (+20.0%p on 기능장 / master craftsman).
  *Public past exams — both sides include memorized content, so read the delta, not the absolute.*
- **Query text is never written to disk.** Only a non-reversible fingerprint and shape metadata.
- Weak on qualitative design judgment and contract-document interpretation. Stated up front.

Beta, free. Request access at [den.archi](https://den.archi).
