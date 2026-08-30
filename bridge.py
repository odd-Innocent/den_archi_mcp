#!/usr/bin/env python3
"""den 원격 서버로 가는 stdio 브리지.

den 은 원격 MCP 서버다(streamable-http). 이 파일은 stdio 만 말하는 클라이언트가
그 서버에 닿게 해 주는 **얇은 중계**다. 지식도 서빙 로직도 여기 없다 —
전부 https://mcp.den.archi/mcp 에 있다.

## 이 파일이 지키는 것

  · **비밀을 담지 않는다.** 키는 이 이미지에 들어가지 않는다. 사용자가 환경변수
    DEN_API_KEY 로 넣으면 그대로 전달하고, 없으면 없는 채로 보낸다.
  · **키 없이도 발견은 된다.** den 은 initialize·tools/list 를 무인증으로 답한다
    (지시 A080). 그래서 키가 없어도 이 브리지는 도구 목록을 그대로 넘긴다.
    실제 서빙(tools/call)은 서버가 401 로 막고, 그 401 을 사용자에게 그대로 전한다.
  · **응답을 고치지 않는다.** 근거·기권 신호가 중간에서 바뀌면 den 이 아니다.

사용:  DEN_API_KEY=<키> python3 bridge.py     (키는 선택)
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

ENDPOINT = os.environ.get("DEN_MCP_URL", "https://mcp.den.archi/mcp")
KEY = os.environ.get("DEN_API_KEY", "").strip()
TIMEOUT = float(os.environ.get("DEN_TIMEOUT", "120"))


def forward(payload: bytes) -> bytes:
    req = urllib.request.Request(ENDPOINT, data=payload, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("Accept", "application/json, text/event-stream")
    # ★자기 이름을 밝힌다. 기본 UA(Python-urllib)는 우리 엣지가 막는다 —
    #   실측: Python-urllib 403 · httpx·requests·node·curl 은 전부 200.
    #   공식 MCP Python SDK 는 httpx 를 쓰므로 실사용자 영향은 없다.
    #   그래도 익명 UA 로 다니는 자는 언제든 이렇게 막힌다 ∴ 이름을 단다.
    req.add_header("User-Agent", "den-mcp-bridge/1.0 (+https://den.archi)")
    if KEY:                       # 없으면 안 붙인다 — 지어내지 않는다
        req.add_header("Authorization", f"Bearer {KEY}")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        # 서버의 판정을 **그대로** 전한다. 401 을 우리가 각색하면 사용자가 원인을 못 찾는다.
        return e.read() or json.dumps({
            "jsonrpc": "2.0", "id": None,
            "error": {"code": e.code, "message": e.reason},
        }).encode()
    except Exception as e:                                # noqa: BLE001
        return json.dumps({
            "jsonrpc": "2.0", "id": None,
            "error": {"code": -32603, "message": f"{type(e).__name__}: {e}"},
        }).encode()


def main() -> int:
    for line in sys.stdin.buffer:
        line = line.strip()
        if not line:
            continue
        out = forward(line)
        sys.stdout.buffer.write(out.rstrip(b"\n") + b"\n")
        sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
