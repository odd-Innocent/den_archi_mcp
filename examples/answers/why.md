# 인과 질문의 답과 경로 근거

2026년 11월 19일 운영 서버에 호출한 `answer_why` 응답에서 필드 일부를 옮겼습니다.

| 항목 | 내용 |
|---|---|
| 호출 일자 | 2026년 11월 19일 |
| 도구 | `answer_why`(기본 설정, `depth=L2` · `profile=standard`) |
| 서빙 팩 | `2026-11-17-scheduled` |
| 영수증 번호 | `dr1-89dcafa59e6ccd36` |

## 질문

> 왜 외벽 모서리나 열교 부위에 결로가 생기는가

## 응답 발췌

```json
{
  "relevance": "high",
  "matched_seeds": [
    {"id": "thermal-bridge", "name_ko": "열교", "kind": "quality"},
    {"id": "t4r424-corner-condensation", "name_ko": "외벽 모서리 결로와 열교", "kind": "practice_rule"}
  ],
  "paths": [
    {
      "chain": [
        {
          "from": "t4r424-corner-condensation",
          "relation": "enables",
          "to": "t4r424-dewpoint-check",
          "stance": "consensus",
          "evidence_note": "모서리 결로는 국부 표면과 실내 노점을 비교해야 한다.",
          "evidence_tier": "other",
          "direction": "forward"
        }
      ],
      "view": "consensus"
    },
    {
      "chain": [
        {
          "from": "thermal-bridge",
          "relation": "causes",
          "to": "heat-loss",
          "stance": "consensus",
          "evidence_note": "… thermal bridges are points where heat and cold cross the envelope, causing cold spots and condensation risk …",
          "evidence_tier": "other",
          "direction": "forward"
        }
      ],
      "view": "consensus"
    }
  ],
  "evidence": [
    {
      "concept": "t4r424-corner-condensation",
      "detail": "… 일반 벽면보다 표면온도가 낮아질 수 있어 …",
      "source_ref": "Heating, Cooling, Lighting 4판 Ch 15.8 Heat Bridges·Ch 15.13·Ch 15.14의 표면 결로 원리 요지화",
      "source_tier": "academic",
      "source_scope": "reference"
    },
    {
      "concept": "kh-ob-e8e77f27da",
      "fact": "… 열손실 증가와 표면 결로의 원인이 되며 …",
      "source_ref": "건축물의 에너지절약설계기준, 건축환경 표준교재",
      "source_tier": "standard",
      "source_scope": "kr-norm"
    }
  ],
  "meta": {
    "receipt": {
      "id": "dr1-89dcafa59e6ccd36",
      "issued_at": "2026-11-19T00:14:01Z",
      "v": 1,
      "tool": "answer_why",
      "q_sha256": "6d45c408a6e2a789",
      "as_of": null,
      "pack": {"version": "2026-11-17-scheduled", "sha256": "43ee332a41a65e29"},
      "code": "d02ceb9509f66821",
      "nodes": [
        "kh-thermal-bridge#64de45ecd7a2",
        "thermal-bridge#b0e8e7506001",
        "t4r424-corner-condensation#c54a35b5d53c",
        "t4r485-condensation-bridge#8543895ca859",
        "kr-kcs-31-20-15-norm-3-12-1-배관설비공사-외벽-및-지붕-등-외부에-노출된-부위를#f5a95cae7817",
        "t4r424-dewpoint-check#eae3130369c3",
        "energy-efficiency#a3db24e72d38",
        "heat-loss#83938d336e2d",
        "condensation-diagnosis#bce1775a1de7",
        "t4r485-ibc13-criteria#9cbcf2436c1f"
      ],
      "response_sha256": "8f1175b27cd8a1aab533ebf8278389ec"
    }
  }
}
```

발췌의 `paths`와 `evidence`는 응답에 든 경로와 지식 항목 가운데 답에 쓴 항목만 옮겼고, 영수증은 전체를 옮겼습니다.

## 에이전트의 답

> 열교는 슬래브, 기둥, 창호 주변처럼 단열재가 관통되거나 중단되는 부위에서 생기고, 열손실 증가와 표면 결로의 원인이 됩니다[1]. 외벽 모서리는 2차원 열흐름과 시공 불연속 때문에 일반 벽면보다 표면온도가 낮아질 수 있으며, 표면온도가 실내 공기의 노점보다 낮으면 그 표면에 결로가 생깁니다[2]. 모서리 결로는 표면온도와 실내 노점을 함께 비교해 진단하고[3], 단열을 연속시키는 외단열로 완화합니다[1].
>
> [1] `건축물의 에너지절약설계기준, 건축환경 표준교재` (국내 규범)
> [2] `Heating, Cooling, Lighting 4판 Ch 15.8 Heat Bridges·Ch 15.13·Ch 15.14의 표면 결로 원리 요지화` (해외 문헌, 국내 준수 대상 아님)
> [3] Den 인과 경로: 외벽 모서리 결로에서 노점 확인으로 이어지는 관계(`enables`, 근거 등급 `other`)
>
> Den이 반환한 인과 경로
>
> | 출발 | 관계 | 도착 | 근거 등급 |
> |---|---|---|---|
> | 열교 | 유발(`causes`) | 열손실 | `other` |
> | 외벽 모서리 결로 | 가능(`enables`) | 노점 확인 | `other` |
>
> Den 영수증: `dr1-89dcafa59e6ccd36` (2026년 11월 19일 조회)

## 답에 반영한 응답 필드

| 응답 필드 | 답에 반영한 내용 |
|---|---|
| `paths[].chain[]` | 개념 사이 관계(`from`, `relation`, `to`)와 관계마다 붙은 근거(`evidence_note`, `evidence_tier`)입니다. 답에는 관계와 근거 등급을 함께 적습니다. |
| `evidence_tier` | 이 응답의 경로 근거는 모두 `other` 등급(법령, 기준, 학술 문헌, 백과사전 외의 자료)입니다. 답의 사실 문장에는 출처가 표기된 지식 항목을 붙입니다. |
| `evidence[]` | 경로 주변의 지식 항목과 출처(`source_ref`)입니다. 답의 문장마다 출처를 받은 문자열대로 붙입니다. |
| `source_scope` | `kr-norm`은 국내 규범, `reference`는 해외 문헌, `den-internal`은 Den 자체 분석입니다. 해외 문헌과 Den 자체 분석은 국내 기준처럼 제시하지 않습니다. |
| `relevance` | 이 응답은 `high`입니다. `low`이거나 `no_path_reason`이 있으면 Den이 그 경로를 보유하지 않으므로 경로를 근거로 쓰지 않습니다. |
| `disclaimer` | 이 응답에는 없습니다. 응답에 있으면 문구를 바꾸지 않고 답에 옮깁니다. |
| `meta.receipt.id` | 답 끝에 영수증 번호와 조회 일자를 적습니다. 영수증 항목은 [receipts.md](../receipts.md)에 있습니다. |
