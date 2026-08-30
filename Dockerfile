# den 원격 서버로 가는 stdio 브리지.
#
# ★이 이미지는 **비밀을 담지 않는다.** 키는 실행할 때 DEN_API_KEY 로 들어오고,
#   없으면 없는 채로 돈다. 공개 이미지에 키를 굽는 것은 키를 공개하는 것과 같다.
# ★지식도 서빙 코드도 여기 없다 — 전부 https://mcp.den.archi/mcp 에 있다.
#   이 이미지를 뜯어도 나오는 것은 이 50줄짜리 중계뿐이다.
FROM python:3.12-slim

# 표준 라이브러리만 쓴다 — 의존성이 없으면 공급망에서 새로 생기는 위험도 없다
COPY bridge.py /app/bridge.py
WORKDIR /app

# 루트로 돌지 않는다
RUN useradd --create-home --shell /usr/sbin/nologin den
USER den

ENV DEN_MCP_URL=https://mcp.den.archi/mcp
ENTRYPOINT ["python3", "-u", "/app/bridge.py"]
