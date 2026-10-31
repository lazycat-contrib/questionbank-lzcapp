# QuestionBank LazyCat package — INCOMPLETE

Upstream: https://github.com/gygy-open/question-bank
Package: community.lazycat.app.questionbank (default prefix)
Target: linux/amd64, LazyCat LPK v2, community/喵喵 store only.

## Verified local state

Only upstream-derived icon.png and draft package.yml have been written. No successful GitHub build, LPK, checksum, or store publication is established. The repository Actions query returned HTTP 404 on 2026-10-31. A delegated execution timed out without returning a result; do not infer any remote changes from that timeout.

## Remaining work

- Recheck local/remote changes and active Actions before editing or dispatching.
- Inspect upstream v1.6.1 compose and image configuration, not only moving main.
- Implement runtime manifest and build configuration, preserving permissions and shared /data semantics.
- Resolve database migration completion before backend/worker startup using actual readiness, not fixed sleep. Do not run the upstream hardcoded-password superuser helper.
- Configure verified login autofill or credential capture for first-run account creation; do not claim an admin account is created unless implemented.
- Confirm Chroma client/server compatibility; tag presence alone is not compatibility evidence.
- Configure GitHub Actions mirror delivery for every runtime image; verify source and delivered platform digests.
- Do not pass an empty release-target-commitish. No added smoke job or file-picker interception. Official store disabled.
- Run actionlint and configuration validation; build on GitHub Actions.
- Before publishing, fetch all store pages and deduplicate by exact name, aliases, package ID, and upstream/source. Earlier name/description-only filtering is insufficient.
- Verify exact versioned Release LPK identity and independently recompute SHA256 before one store submission, then independently requery store status.
- Clearly disclose lack of runtime validation.

## Queue

Finish QuestionBank first. Apache Answer and https://github.com/WebCoderT/olua are requested next; do not start concurrent packages.

Authorization expires 2026-11-01T22:00:00+08:00. Stop migration work after expiration.

## 2026-10-31 15:30 轮次实际进度

- 已新增 runtime manifest、启动排序脚本、部署参数，并补齐 build 引用。四份 YAML 语法解析通过，启动脚本 AST 语法检查通过。
- lzc-cli project release 成功生成 dist/questionbank-draft.lpk，包内必需文件及 content/start.py 存在；SHA256: c21475245be4e30ffef3a019f8dd2ecdeee16ac19381cbeaa16a54f48ee6dbc8。这是本地草稿构建，不是 GitHub Release 或上架成功证据。
- 尚缺 GitHub Actions、全部镜像源/交付摘要匹配、Chroma兼容性及登录运行验证、发布前重新全量查重。未发布、未运行验证。官方商店镜像源 lint 警告保留，不据此改变发布目标。
