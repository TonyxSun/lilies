#!/usr/bin/env node
import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";
import { spawnSync } from "child_process";

const __dir = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const arg = (n, f) => { const i = args.indexOf(n); return i >= 0 ? args[i + 1] : f; };

const htmlIn = resolve(arg("--html", resolve(__dir, "card.html")));
const outPath = resolve(arg("--out", "/workspace/coach-card/morning-call.png"));
const dataPath = arg("--data", null);

const CALL_COLOR = { push: "#16EC06", maintain: "#FFDE00", recover: "#FF0026" };

function esc(s) {
  return String(s ?? "").replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
}

function fill(html, d) {
  const call = (d.call || "Maintain").trim();
  const cls = call.toLowerCase();
  const color = CALL_COLOR[cls] || CALL_COLOR.maintain;
  const oura = d.oura || {};
  const garmin = d.garmin || {};
  const ouraNo = !oura.has_data;
  const garminNo = !garmin.has_data;

  let out = html;
  out = out.replace(/id="date">[^<]*/, `id="date">${esc(d.date_label || "")}`);
  out = out.replace(/id="hero"[^>]*/, `id="hero" style="--call:${color}"`);
  out = out.replace(/id="call">[^<]*/, `id="call">${esc(call)}`);
  out = out.replace(/id="why">[^<]*/, `id="why">${esc(d.why || "")}`);

  out = out.replace(
    /id="oura-badge"[^>]*>[^<]*/,
    `id="oura-badge" class="badge${ouraNo ? " nodata" : ""}">${ouraNo ? "No data" : "Today"}`
  );
  if (ouraNo) {
    out = out.replace(/id="oura-ready"[^>]*>[^<]*/, `id="oura-ready" class="val muted">—`);
    out = out.replace(/id="oura-sleep"[^>]*>[^<]*/, `id="oura-sleep" class="val muted">—`);
    out = out.replace(/id="oura-dur"[^>]*>[^<]*/, `id="oura-dur" class="val muted" style="font-size:28px">no data`);
    out = out.replace(/id="oura-hrv"[^>]*>[\s\S]*?<\/div>/, `id="oura-hrv" class="val muted">—</div>`);
    out = out.replace(/id="oura-rhr"[^>]*>[\s\S]*?<\/div>/, `id="oura-rhr" class="val muted">—</div>`);
  } else {
    out = out.replace(/id="oura-ready"[^>]*>[^<]*/, `id="oura-ready" class="val">${esc(oura.readiness ?? "—")}`);
    out = out.replace(/id="oura-sleep"[^>]*>[^<]*/, `id="oura-sleep" class="val">${esc(oura.sleep_score ?? "—")}`);
    out = out.replace(/id="oura-dur"[^>]*>[^<]*/, `id="oura-dur" class="val" style="font-size:28px">${esc(oura.duration ?? "—")}`);
    out = out.replace(/id="oura-hrv"[^>]*>[\s\S]*?<\/div>/, `id="oura-hrv" class="val">${esc(oura.hrv ?? "—")}<span class="unit">ms</span></div>`);
    out = out.replace(/id="oura-rhr"[^>]*>[\s\S]*?<\/div>/, `id="oura-rhr" class="val">${esc(oura.rhr ?? "—")}<span class="unit">bpm</span></div>`);
  }

  out = out.replace(
    /id="garmin-badge"[^>]*>[^<]*/,
    `id="garmin-badge" class="badge${garminNo ? " nodata" : ""}">${garminNo ? "No data" : "Today"}`
  );
  if (garminNo) {
    out = out.replace(/id="garmin-status"[^>]*>[^<]*/, `id="garmin-status" class="val muted">—`);
    out = out.replace(/id="garmin-load-line">[^<]*/, `id="garmin-load-line">no data`);
    out = out.replace(/id="garmin-vo2"[^>]*>[^<]*/, `id="garmin-vo2" class="val muted">—`);
    out = out.replace(/id="garmin-last"[^>]*>[^<]*/, `id="garmin-last" class="val muted" style="font-size:24px">—`);
  } else {
    const load =
      garmin.acute_load != null
        ? `Acute ${garmin.acute_load}${garmin.acute_label ? ` · ${garmin.acute_label}` : ""}`
        : "—";
    out = out.replace(/id="garmin-status"[^>]*>[^<]*/, `id="garmin-status" class="val">${esc(garmin.status ?? "—")}`);
    out = out.replace(/id="garmin-load-line">[^<]*/, `id="garmin-load-line">${esc(load)}`);
    out = out.replace(/id="garmin-vo2"[^>]*>[^<]*/, `id="garmin-vo2" class="val">${esc(garmin.vo2max ?? "—")}`);
    out = out.replace(/id="garmin-last"[^>]*>[^<]*/, `id="garmin-last" class="val" style="font-size:24px">${esc(garmin.last_session ?? "—")}`);
  }

  const xBlocked = d.xunji?.status !== "ok";
  const xNote = d.xunji?.note || "no data";
  out = out.replace(
    /id="xunji"[^>]*>[\s\S]*?<\/div>/,
    `id="xunji" class="xunji${xBlocked ? " blocked" : ""}"><strong>训记</strong> · ${esc(xNote)}</div>`
  );
  return out;
}

mkdirSync(dirname(outPath), { recursive: true });
let html = readFileSync(htmlIn, "utf8");
let renderPath = htmlIn;
if (dataPath) {
  html = fill(html, JSON.parse(readFileSync(resolve(dataPath), "utf8")));
  renderPath = resolve(dirname(outPath), "filled.html");
  writeFileSync(renderPath, html);
}

const r = spawnSync("google-chrome", [
  "--headless=new", "--disable-gpu", "--hide-scrollbars",
  "--force-device-scale-factor=1", `--screenshot=${outPath}`,
  "--window-size=1080,1350", "file://" + renderPath,
], { encoding: "utf8" });
if (r.status !== 0) { console.error(r.stderr || r.stdout); process.exit(r.status || 1); }
console.log(outPath);
