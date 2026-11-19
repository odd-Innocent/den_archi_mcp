# Codex 연결 설정

Codex는 `~/.codex/config.toml`의 MCP 설정으로 Den에 연결하고, ChatGPT 데스크톱 앱, Codex CLI, IDE 확장이 이 설정을 함께 씁니다. Den 키는 환경 변수에 두고, 설정에는 환경 변수 이름만 적습니다.

## 키 발급

mcp.den.archi에 로그인한 뒤 [「키 · 연결된 앱」](https://mcp.den.archi/console/keys) 화면에서 키를 발급합니다.

## 환경 변수

```bash
export DEN_API_KEY="<발급받은 키>"
```

셸 시작 파일(`~/.bashrc`, `~/.zshrc` 등)에 같은 줄을 추가하면 새 터미널에도 적용됩니다.

## 명령으로 등록

```bash
codex mcp add den --url https://mcp.den.archi/mcp --bearer-token-env-var DEN_API_KEY
```

## 설정 파일로 등록

`~/.codex/config.toml`에 아래 표를 추가합니다. 신뢰한 프로젝트에서는 프로젝트의 `.codex/config.toml`에 둘 수도 있습니다.

```toml
[mcp_servers.den]
url = "https://mcp.den.archi/mcp"
bearer_token_env_var = "DEN_API_KEY"
```

Codex는 `bearer_token_env_var`에 적은 환경 변수의 내용을 `Authorization` 헤더의 bearer 토큰으로 보냅니다.

## 연결 상태 확인

```bash
codex mcp list
```

Codex 터미널 화면에서는 `/mcp`로 연결된 서버를 확인합니다.

## 참고 문서

- [Den 연결 방법](https://mcp.den.archi/connect)
- [Codex MCP 설정(영문)](https://learn.chatgpt.com/docs/extend/mcp)
- [Codex 설정 항목 목록(영문)](https://learn.chatgpt.com/docs/config-file/config-reference)
- [Codex 명령 목록(영문)](https://learn.chatgpt.com/docs/developer-commands)
