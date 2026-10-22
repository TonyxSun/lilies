---
name: Photo library access
description: >-
  Use when setting up or restoring phone/LAN access to a Mac photo folder tree
  (SMB preferred, HTTP LaunchAgent fallback), or when documenting photo library
  folder conventions.
---
# Photo library access

## Goals
- Masters stay in a dated/project folder tree on the Mac (not Photos.app as source of truth).
- Phone can browse the tree overnight on the same LAN (or Tailscale).
- Prefer non-destructive ops: never overwrite RAW; delete from card only after explicit yes.

## Folder convention (default)
```
<library-root>/
  Trips/YYYY_MM_Name/     # masters (ARW/JPG/HEIF) flat in the shoot folder
```
Do **not** create `edits/` or `exports/{web,print,archive}` unless the user asks. Keep shoot folders flat for now.

## Access stack (prefer in order)
1. **macOS File Sharing (SMB)** — real NAS-style mount in iOS Files.
   - Needs admin once: `sharing -a '<path>' -S '<ShareName>' -n '<ShareName>' -s 001 -g 000`
   - Enable `smbd` (System Settings → General → Sharing → File Sharing).
   - Guest off for photo shares; use Mac login on the phone.
   - iOS: Files → … → Connect to Server → `smb://<lan-ip>/<ShareName>` (or Tailscale IP).
2. **Overnight HTTP via user LaunchAgent** (no admin) when SMB is not enabled:
   - Script under `<library-root>/.photo-ops/overnight-serve.sh` runs `caffeinate -dims` wrapping `python3` `http.server` on `0.0.0.0:8765`, cwd = Trips.
   - LaunchAgent label pattern: `com.<user>.photo-trips-http` with `RunAtLoad` + `KeepAlive`.
   - Phone: Safari → `http://<lan-ip>:8765/` (same Wi‑Fi) or `http://<tailscale-ip>:8765/` (Tailscale up on both).
   - Confirm with `curl -sI http://127.0.0.1:8765/` and `launchctl print gui/$(id -u)/<label>`.
3. **Tailscale** — use when off-LAN; confirm the phone node is online before promising remote access.

## Hard rules
- Quote real paths, IPs, file counts — never invent a library root.
- Do not format cards, empty trash, or bulk-delete without an explicit yes in chat.
- Document live access details in agent memory (root, share name, port, LaunchAgent label).
- After access is live, email clear phone steps (LAN URL, Tailscale URL, SMB if enabled, Mac must stay on).

## Verify before calling it done
- HTTP or SMB returns a Trips listing.
- Firewall not blocking (or noted).
- LaunchAgent / caffeinate still running for the promised window.
