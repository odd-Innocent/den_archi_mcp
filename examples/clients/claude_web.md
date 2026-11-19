# Claude 웹 연결 설정

Claude 웹은 커스텀 커넥터로 Den에 연결하고, 인증은 OAuth로 진행합니다. 이 방식에는 API 키가 필요하지 않습니다.

| 항목 | 입력 |
|---|---|
| 커넥터 주소 | `https://mcp.den.archi/mcp` |
| 인증 방식 | OAuth |

## 연결 절차

1. [mcp.den.archi](https://mcp.den.archi/signup)에서 가입합니다.
2. Claude 웹의 「설정」에서 「커넥터」를 열고, 「커스텀 커넥터 추가」에 커넥터 주소를 등록합니다.
3. 인증 방식으로 OAuth를 선택합니다.
4. 인증 창에서 Den 계정으로 로그인한 뒤 「허용」을 누릅니다.

Claude 화면의 메뉴 이름이 위 절차와 다르면 Claude 도움말의 커스텀 커넥터 안내를 따릅니다.

## 연결되지 않을 때

- 인증 창이 열리지 않으면 주소 끝에 공백이나 줄바꿈이 들어갔을 수 있습니다. [연결 확인](https://mcp.den.archi/check) 화면에서 등록한 주소를 검사합니다.
- 연결 확인 화면은 주소 형식을 검사합니다. 도구 호출 응답은 대화에서 건설 기준 질문을 보내 따로 확인합니다.

## 참고 문서

- [Den 연결 방법](https://mcp.den.archi/connect)
- [Claude 도움말: 원격 MCP 커스텀 커넥터(영문)](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
