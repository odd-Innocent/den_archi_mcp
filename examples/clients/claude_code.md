# Claude Code 연결 설정

터미널의 Claude Code는 API 키를 인증 헤더로 보내 Den에 연결합니다.

## 키 발급

mcp.den.archi에 로그인한 뒤 [「키 · 연결된 앱」](https://mcp.den.archi/console/keys) 화면에서 키를 발급합니다.

## 등록 명령

```bash
claude mcp add --transport http den https://mcp.den.archi/mcp --header "Authorization: Bearer <발급받은 키>"
```

`<발급받은 키>` 자리에 발급한 키를 입력합니다. 등록 명령은 키를 검증하지 않으므로, 키를 잘못 입력해도 등록은 되고 연결 단계에서 실패합니다.

## 설정 범위

`--scope` 옵션으로 설정을 저장할 범위를 정합니다.

| 범위 | 적용 대상 | 저장 위치 |
|---|---|---|
| `local`(기본) | 현재 프로젝트, 등록한 사용자 | `~/.claude.json` |
| `user` | 등록한 사용자의 모든 프로젝트 | `~/.claude.json` |
| `project` | 현재 프로젝트를 공유하는 모든 사용자 | 프로젝트 루트의 `.mcp.json` |

모든 프로젝트에서 Den을 쓰는 등록 예시입니다.

```bash
claude mcp add --transport http den --scope user https://mcp.den.archi/mcp --header "Authorization: Bearer <발급받은 키>"
```

`project` 범위로 등록하면 키가 `.mcp.json`에 기록되고, 이 파일을 저장소에 올리면 키가 함께 공유됩니다. 키를 쓰는 등록은 `local` 또는 `user` 범위로 합니다.

## 연결 상태 확인

```bash
claude mcp list
```

Claude Code 안에서는 `/mcp`로 서버 상태를 확인합니다.

## 참고 문서

- [Den 연결 방법](https://mcp.den.archi/connect)
- [Claude Code MCP 문서(영문)](https://code.claude.com/docs/en/mcp)
