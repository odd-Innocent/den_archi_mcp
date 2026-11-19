# Cursor 연결 설정

Cursor는 `mcp.json`에 서버 주소와 인증 헤더를 적어 Den에 연결합니다. 키는 환경 변수에 두고 `mcp.json`에서 불러옵니다.

## 키 발급

mcp.den.archi에 로그인한 뒤 [「키 · 연결된 앱」](https://mcp.den.archi/console/keys) 화면에서 키를 발급합니다.

## 환경 변수

```bash
export DEN_API_KEY="<발급받은 키>"
```

원격 서버 설정은 `envFile`을 지원하지 않으므로, 키는 셸 시작 파일이나 시스템 환경 변수에 둡니다.

## mcp.json

모든 프로젝트에 적용하는 설정은 `~/.cursor/mcp.json`에, 한 프로젝트에 적용하는 설정은 프로젝트의 `.cursor/mcp.json`에 적습니다.

```json
{
  "mcpServers": {
    "den": {
      "url": "https://mcp.den.archi/mcp",
      "headers": {
        "Authorization": "Bearer ${env:DEN_API_KEY}"
      }
    }
  }
}
```

Cursor는 `headers`에 적은 `${env:DEN_API_KEY}`를 환경 변수의 내용으로 바꿔 요청에 씁니다.

## 연결 상태 확인

- 사이드바의 「Customize」에서 Den 서버가 켜져 있는지 확인합니다.
- 연결 오류는 Output 패널(Cmd+Shift+U)에서 「MCP Logs」를 선택해 확인합니다.

## 참고 문서

- [Den 연결 방법](https://mcp.den.archi/connect)
- [Cursor MCP 문서(영문)](https://cursor.com/docs/mcp)
