# ChatGPT 연결 설정

ChatGPT는 개발자 모드의 커스텀 커넥터로 Den에 연결하고, 인증은 OAuth로 진행합니다. 개발자 모드는 PC 웹에서만 표시되므로 등록도 PC 웹에서 진행합니다.

| 항목 | 입력 |
|---|---|
| 커넥터 주소 | `https://mcp.den.archi/mcp` |
| 인증 방식 | OAuth |

## 연결 절차

1. [mcp.den.archi](https://mcp.den.archi/signup)에서 가입합니다.
2. ChatGPT 웹의 좌측 하단 「설정」에서 「보안 및 로그인」을 열고 개발자 모드를 켭니다.
3. 「플러그인」 옆 더하기 단추에서 커넥터 주소를 등록하고, 인증 방식으로 OAuth를 선택합니다.
4. 인증 창에서 Den 계정으로 로그인한 뒤 「허용」을 누릅니다.

## 연결되지 않을 때

- 개발자 모드가 꺼져 있으면 커넥터 항목이 보이지 않습니다. 「설정」에서 개발자 모드가 켜져 있는지 확인합니다.
- 인증 창이 열리지 않으면 주소 끝의 공백이나 줄바꿈을 확인하고, [연결 확인](https://mcp.den.archi/check) 화면에서 주소를 검사합니다.

## 참고 문서

- [Den 연결 방법](https://mcp.den.archi/connect)
- [ChatGPT 커스텀 MCP 서버 등록 안내(영문)](https://developers.openai.com/plugins/deploy/connect-chatgpt)
